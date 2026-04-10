"""
Connector Shopee — Multi-Conta (3 lojas Budamix)
Busca dados via API Shopee e retorna no formato padrão do marketplace-report.
Consolida pedidos, pagamentos e info de todas as contas.
"""

import asyncio
import hashlib
import hmac
import json
import logging
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = logging.getLogger('connector.shopee')

# ─── Config ──────────────────────────────────────────────────────────────────

PLATFORM = 'shopee'
PLATFORM_DISPLAY = 'Shopee'
PARTNER_ID = 2031533
PARTNER_KEY = 'shpk494d456e49555973537464767779694476566c796e5579724648436b676c'
HOST = 'https://partner.shopeemobile.com'
TOKENS_DIR = Path('/root/.openclaw/workspace/integrations/shopee')
ACCOUNTS_FILE = TOKENS_DIR / 'accounts.json'

# ─── Lazy imports ────────────────────────────────────────────────────────────

_aiohttp_available = None

def _check_aiohttp():
    global _aiohttp_available
    if _aiohttp_available is None:
        try:
            import aiohttp
            _aiohttp_available = True
        except ImportError:
            _aiohttp_available = False
            log.warning("aiohttp não instalado. pip install aiohttp")
    return _aiohttp_available

# ─── Account/Token Management ───────────────────────────────────────────────

def load_accounts():
    """Carrega contas Shopee do accounts.json."""
    if not os.path.exists(ACCOUNTS_FILE):
        log.error(f"Arquivo de contas não encontrado: {ACCOUNTS_FILE}")
        return {}
    with open(ACCOUNTS_FILE) as f:
        data = json.load(f)
    accounts = {}
    for a in data['accounts']:
        alias = a['alias']
        display = a.get('shop_name', alias.replace('-', ' ').title())
        if alias == 'budamix-store':
            display = 'Budamix Store'
        accounts[alias] = {
            'alias': alias,
            'display': display,
            'shop_id': a['shop_id'],
            'token_file': TOKENS_DIR / a['token_file'],
        }
    return accounts


def load_tokens(account):
    """Carrega tokens de um arquivo de conta."""
    with open(account['token_file']) as f:
        return json.load(f)


def save_tokens(account, tokens):
    """Salva tokens atualizados."""
    with open(account['token_file'], 'w') as f:
        json.dump(tokens, f, indent=2)


def compute_sign(path, ts, access_token=None, shop_id=None):
    """Calcula HMAC-SHA256 para assinatura Shopee."""
    if access_token and shop_id:
        base = f"{PARTNER_ID}{path}{ts}{access_token}{shop_id}"
    else:
        base = f"{PARTNER_ID}{path}{ts}"
    return hmac.new(PARTNER_KEY.encode(), base.encode(), hashlib.sha256).hexdigest()

# ─── Async API Client ───────────────────────────────────────────────────────

class ShopeeApiClient:
    """Client per-account com rate limiting e retry."""

    def __init__(self, account, tokens):
        self.account = account
        self.access_token = tokens['access_token']
        self.shop_id = tokens['shop_id']
        self.semaphore = asyncio.Semaphore(8)
        self.req_times = []

    def build_url(self, path, params=None):
        ts = int(time.time())
        sign = compute_sign(path, ts, self.access_token, self.shop_id)
        qs = (f"partner_id={PARTNER_ID}&shop_id={self.shop_id}"
              f"&timestamp={ts}&access_token={self.access_token}&sign={sign}")
        for k, v in (params or {}).items():
            qs += f"&{k}={v}"
        return f"{HOST}{path}?{qs}"

    async def rate_limit(self):
        now = time.time()
        self.req_times.append(now)
        self.req_times = [t for t in self.req_times if t > now - 1]
        if len(self.req_times) > 10:
            await asyncio.sleep(0.15)

    async def get(self, http_session, path, params=None):
        import aiohttp
        async with self.semaphore:
            await self.rate_limit()
            url = self.build_url(path, params)
            for attempt in range(3):
                try:
                    async with http_session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                        data = await resp.json()
                        if data.get('error') and 'too many' in str(data.get('message', '')).lower():
                            await asyncio.sleep(2 ** attempt)
                            url = self.build_url(path, params)
                            continue
                        return data
                except Exception as e:
                    if attempt < 2:
                        await asyncio.sleep(1)
                        url = self.build_url(path, params)
                    else:
                        return {"error": str(e)}
            return {"error": "max retries"}

# ─── Token Refresh ───────────────────────────────────────────────────────────

async def refresh_token(http_session, account, tokens):
    """Refresh access token para uma conta."""
    path = "/api/v2/auth/access_token/get"
    ts = int(time.time())
    sign = compute_sign(path, ts)
    url = f"{HOST}{path}?partner_id={PARTNER_ID}&timestamp={ts}&sign={sign}"
    body = {
        "refresh_token": tokens['refresh_token'],
        "partner_id": PARTNER_ID,
        "shop_id": account['shop_id'],
    }
    async with http_session.post(url, json=body) as resp:
        data = await resp.json()
    if data.get('error'):
        raise RuntimeError(f"Token refresh falhou para {account['alias']}: {data}")
    new_tokens = {
        'shop_id': account['shop_id'],
        'access_token': data['access_token'],
        'refresh_token': data['refresh_token'],
        'access_token_expire_in': data.get('expire_in', 14400),
        'refresh_token_expire_in': 2592000,
        'token_obtained_at': int(time.time()),
        'partner_id': PARTNER_ID,
        'updated_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
    }
    save_tokens(account, new_tokens)
    log.info(f"  Token refreshed: {account['alias']}")
    return new_tokens


async def ensure_valid_token(http_session, account):
    """Carrega tokens, refresh se expirado, retorna tokens válidos."""
    tokens = load_tokens(account)
    obtained = tokens.get('token_obtained_at', 0)
    expire_in = tokens.get('access_token_expire_in', 0)
    if time.time() > obtained + expire_in - 300:
        log.info(f"  Token expirado para {account['alias']}, refreshing...")
        tokens = await refresh_token(http_session, account, tokens)
    return tokens

# ─── Data Fetchers (Async) ──────────────────────────────────────────────────

def ts_to_iso(ts_val):
    """Converte Unix timestamp para string ISO."""
    if not ts_val:
        return ''
    try:
        dt = datetime.fromtimestamp(ts_val, tz=timezone(timedelta(hours=-3)))
        return dt.strftime('%Y-%m-%dT%H:%M:%S-03:00')
    except Exception:
        return ''


async def fetch_orders_account(client, http_session, time_from, time_to, account):
    """Busca pedidos de uma conta Shopee."""
    all_orders = []

    # Shopee limita janela a 15 dias
    windows = []
    current = time_from
    while current < time_to:
        window_end = min(current + 15 * 86400, time_to)
        windows.append((current, window_end))
        current = window_end

    for status in ['COMPLETED', 'SHIPPED', 'READY_TO_SHIP', 'IN_CANCEL', 'CANCELLED']:
        for wf, wt in windows:
            cursor = "0"
            while True:
                r = await client.get(http_session, '/api/v2/order/get_order_list', {
                    'time_range_field': 'create_time',
                    'time_from': wf,
                    'time_to': wt,
                    'page_size': 50,
                    'cursor': cursor,
                    'order_status': status,
                })
                resp = r.get('response', {})
                for o in resp.get('order_list', []):
                    all_orders.append({'order_sn': o['order_sn'], 'status': status})
                if not resp.get('more'):
                    break
                cursor = resp.get('next_cursor', '0')

    # Deduplicate
    seen = set()
    unique = []
    for o in all_orders:
        if o['order_sn'] not in seen:
            seen.add(o['order_sn'])
            unique.append(o)

    if not unique:
        return []

    # Fetch details in batches of 50
    order_sns = [o['order_sn'] for o in unique]
    status_map = {o['order_sn']: o['status'] for o in unique}
    details = {}

    for i in range(0, len(order_sns), 50):
        batch = order_sns[i:i + 50]
        r = await client.get(http_session, '/api/v2/order/get_order_detail', {
            'order_sn_list': ','.join(batch),
            'response_optional_fields': 'buyer_user_id,buyer_username,estimated_shipping_fee,actual_shipping_fee,pay_time,item_list,total_amount',
        })
        for order in r.get('response', {}).get('order_list', []):
            details[order['order_sn']] = order

    # Convert to standard format
    standardized = []
    for o in unique:
        sn = o['order_sn']
        detail = details.get(sn, {})

        # Map status
        shopee_status = status_map.get(sn, 'UNKNOWN')
        status_mapping = {
            'COMPLETED': 'paid',
            'SHIPPED': 'shipped',
            'READY_TO_SHIP': 'confirmed',
            'IN_CANCEL': 'cancelling',
            'CANCELLED': 'cancelled',
        }

        # Build order_items
        order_items = []
        for item in detail.get('item_list', []):
            order_items.append({
                'item': {
                    'id': str(item.get('item_id', '')),
                    'title': item.get('item_name', ''),
                    'seller_sku': item.get('item_sku', '') or item.get('model_sku', ''),
                },
                'quantity': item.get('model_quantity_purchased', 1),
                'unit_price': item.get('model_discounted_price', item.get('model_original_price', 0)),
            })

        total_amount = detail.get('total_amount', 0)

        std_order = {
            'id': sn,
            'date_created': ts_to_iso(detail.get('create_time', 0)),
            'status': status_mapping.get(shopee_status, shopee_status.lower()),
            'status_raw': shopee_status,
            'total_amount': total_amount,
            'currency_id': 'BRL',
            'order_items': order_items,
            'buyer': {
                'id': str(detail.get('buyer_user_id', '')),
                'nickname': detail.get('buyer_username', ''),
            },
            'shipping_fee': detail.get('estimated_shipping_fee', 0),
            'platform': 'shopee',
            'shop_id': account['shop_id'],
            'shop_name': account['display'],
        }
        standardized.append(std_order)

    return standardized


async def fetch_payments_account(client, http_session, order_sns, account):
    """Busca escrow details para pagamentos de uma conta."""
    payments = []

    for i in range(0, len(order_sns), 50):
        batch = order_sns[i:i + 50]
        tasks = []
        for sn in batch:
            tasks.append(_fetch_single_escrow(client, http_session, sn))
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for sn, result in zip(batch, results):
            if isinstance(result, Exception):
                log.warning(f"Erro escrow {sn}: {result}")
                continue
            if result is None:
                continue

            income = result.get('order_income', {})

            bruto = income.get('cost_of_goods_sold', 0) or 0
            liquido = income.get('escrow_amount', 0) or 0
            commission = income.get('commission_fee', 0) or 0
            service = income.get('service_fee', 0) or 0
            transaction = income.get('credit_card_transaction_fee', 0) or 0
            campaign = income.get('campaign_fee', 0) or 0
            fbs = income.get('fbs_fee', 0) or 0
            seller_voucher = abs(income.get('seller_voucher', 0) or 0)
            shopee_voucher = abs(income.get('shopee_voucher', 0) or 0)

            fee_details = []
            if commission: fee_details.append({'type': 'commission', 'amount': round(abs(commission), 2)})
            if service: fee_details.append({'type': 'service_fee', 'amount': round(abs(service), 2)})
            if transaction: fee_details.append({'type': 'transaction_fee', 'amount': round(abs(transaction), 2)})
            if campaign: fee_details.append({'type': 'campaign_fee', 'amount': round(abs(campaign), 2)})
            if fbs: fee_details.append({'type': 'fbs_fee', 'amount': round(abs(fbs), 2)})

            payment = {
                'id': f"{sn}_escrow",
                'date_created': '',  # Escrow doesn't always have date
                'status': 'approved' if liquido > 0 else 'pending',
                'transaction_amount': round(bruto, 2),
                'total_paid_amount': round(bruto, 2),
                'net_received_amount': round(liquido, 2),
                'fee_details': fee_details,
                'order_id': sn,
                'payment_type': 'escrow',
                'platform': 'shopee',
                'shop_id': account['shop_id'],
                'shop_name': account['display'],
                'vouchers': {
                    'seller_voucher': round(seller_voucher, 2),
                    'shopee_voucher': round(shopee_voucher, 2),
                },
            }
            payments.append(payment)

    return payments


async def _fetch_single_escrow(client, http_session, order_sn):
    """Busca escrow detail de um pedido."""
    r = await client.get(http_session, '/api/v2/payment/get_escrow_detail', {'order_sn': order_sn})
    if r.get('error') and r['error'] != '':
        return None
    return r.get('response', {})


async def fetch_shop_info_account(client, http_session, account):
    """Busca info da loja Shopee."""
    r = await client.get(http_session, '/api/v2/shop/get_shop_info')
    resp = r.get('response', r)
    if not resp or r.get('error'):
        return {
            'id': account['shop_id'],
            'nickname': account['display'],
            'platform': 'shopee',
            'status': {'site_status': 'unknown'},
        }
    return {
        'id': account['shop_id'],
        'nickname': resp.get('shop_name', account['display']),
        'platform': 'shopee',
        'description': resp.get('description', ''),
        'status': {
            'site_status': resp.get('status', 'NORMAL'),
        },
        'seller_reputation': {
            'level_id': 'N/A',
        },
    }


async def fetch_items_account(client, http_session, account):
    """Busca itens ativos de uma conta Shopee."""
    all_items = []
    offset = 0
    page_size = 50

    while True:
        r = await client.get(http_session, '/api/v2/product/get_item_list', {
            'offset': offset,
            'page_size': page_size,
            'item_status': 'NORMAL',
        })
        resp = r.get('response', {})
        items = resp.get('item', [])

        for item in items:
            all_items.append({
                'id': str(item.get('item_id', '')),
                'status': item.get('item_status', 'NORMAL'),
                'platform': 'shopee',
                'shop_id': account['shop_id'],
                'shop_name': account['display'],
                'update_time': item.get('update_time', 0),
            })

        if not resp.get('has_next_page', False) or not items:
            break
        offset += page_size

    total = resp.get('total_count', len(all_items))
    return all_items, total


async def fetch_traffic_account(client, http_session, account):
    """Busca dados de tráfego de uma conta Shopee.
    Usa shop performance + item base info para views/likes por item."""
    traffic = []

    # 1) Shop-level performance
    shop_sessions = 0
    shop_views = 0
    shop_conversion = 0.0
    try:
        r = await client.get(http_session, '/api/v2/shop/get_shop_performance')
        resp = r.get('response', {})
        if resp and not r.get('error'):
            perf = resp.get('performance', resp)
            shop_sessions = perf.get('visits', perf.get('shop_visits', 0)) or 0
            shop_views = perf.get('views', perf.get('page_views', 0)) or 0
            shop_conversion = perf.get('conversion_rate', perf.get('cr', 0)) or 0
    except Exception as e:
        log.warning(f"     Erro shop performance {account['alias']}: {e}")

    # 2) Item-level traffic — get item list then base info in batches
    try:
        item_ids = []
        offset = 0
        while True:
            r = await client.get(http_session, '/api/v2/product/get_item_list', {
                'offset': offset,
                'page_size': 50,
                'item_status': 'NORMAL',
            })
            resp = r.get('response', {})
            items = resp.get('item', [])
            for item in items:
                item_ids.append(str(item.get('item_id', '')))
            if not resp.get('has_next_page', False) or not items:
                break
            offset += 50

        # Fetch base info in batches of 50 for views/likes
        for i in range(0, len(item_ids), 50):
            batch = item_ids[i:i + 50]
            r = await client.get(http_session, '/api/v2/product/get_item_base_info', {
                'item_id_list': ','.join(batch),
            })
            resp = r.get('response', {})
            for item in resp.get('item_list', []):
                views = item.get('views', item.get('likes', 0)) or 0
                likes = item.get('likes', 0) or 0
                sales = item.get('sales', item.get('sold', 0)) or 0
                conversion = round((sales / views * 100), 2) if views > 0 else 0

                traffic.append({
                    'item_id': str(item.get('item_id', '')),
                    'title': item.get('item_name', item.get('name', '')),
                    'sessions': views,  # Shopee doesn't distinguish sessions/views
                    'page_views': views,
                    'conversion_rate': conversion,
                    'date': '',
                    'platform': 'shopee',
                    'shop_id': account['shop_id'],
                    'shop_name': account['display'],
                    'likes': likes,
                })

    except Exception as e:
        log.warning(f"     Erro item traffic {account['alias']}: {e}")

    # If no item-level data, add shop-level as a single entry
    if not traffic and (shop_sessions or shop_views):
        traffic.append({
            'item_id': f"shop_{account['shop_id']}",
            'title': f"Loja {account['display']} (consolidado)",
            'sessions': shop_sessions,
            'page_views': shop_views,
            'conversion_rate': shop_conversion,
            'date': '',
            'platform': 'shopee',
            'shop_id': account['shop_id'],
            'shop_name': account['display'],
        })

    return traffic


async def fetch_ads_account(client, http_session, account):
    """Busca campanhas de ads de uma conta Shopee via Marketing API."""
    ads = []

    try:
        # Get all campaigns
        r = await client.get(http_session, '/api/v2/marketing/get_all_campaign_list')
        resp = r.get('response', {})
        if r.get('error') and r['error'] != '':
            log.warning(f"     Ads API indisponível para {account['alias']}: {r.get('message', r.get('error', ''))}")
            return []

        campaign_list = resp.get('campaign_list', [])
        if not campaign_list:
            log.info(f"     Nenhuma campanha ads para {account['alias']}")
            return []

        # Get details for each campaign
        for campaign in campaign_list:
            cid = campaign.get('campaign_id', '')
            cname = campaign.get('campaign_name', '')
            cstatus = campaign.get('status', 'normal')

            # Get campaign detail with metrics
            try:
                detail_r = await client.get(http_session, '/api/v2/marketing/get_campaign_detail', {
                    'campaign_id': cid,
                })
                detail_resp = detail_r.get('response', {})
                if detail_r.get('error') and detail_r['error'] != '':
                    detail_resp = {}
            except Exception:
                detail_resp = {}

            # Extract metrics
            metrics = detail_resp.get('metrics', detail_resp)
            cost = float(metrics.get('cost', metrics.get('total_cost', 0)) or 0)
            revenue = float(metrics.get('broad_order_amount', metrics.get('total_sales', metrics.get('revenue', 0))) or 0)
            clicks = int(metrics.get('clicks', metrics.get('total_clicks', 0)) or 0)
            impressions = int(metrics.get('impressions', metrics.get('total_impressions', 0)) or 0)

            # Cost in Shopee is sometimes in micro-units (divide by 100000)
            if cost > 100000:
                cost = cost / 100000
            if revenue > 100000:
                revenue = revenue / 100000

            roas = round(revenue / cost, 2) if cost > 0 else 0
            acos = round((cost / revenue * 100), 2) if revenue > 0 else 0
            cpc = round(cost / clicks, 2) if clicks > 0 else 0
            ctr = round((clicks / impressions * 100), 2) if impressions > 0 else 0

            status_str = 'active' if cstatus in ('ongoing', 'normal', 'active') else 'paused'

            ads.append({
                'campaign_id': str(cid),
                'campaign_name': cname or f"Campanha {cid}",
                'status': status_str,
                'cost': round(cost, 2),
                'revenue': round(revenue, 2),
                'clicks': clicks,
                'impressions': impressions,
                'roas': roas,
                'acos': acos,
                'cpc': cpc,
                'ctr': ctr,
                'platform': 'shopee',
                'shop_id': account['shop_id'],
                'shop_name': account['display'],
            })

        log.info(f"     {len(ads)} campanhas ads para {account['alias']}")
        return ads

    except Exception as e:
        log.warning(f"     Erro buscando ads {account['alias']}: {e}")
        return []


# ─── Async Orchestrator ─────────────────────────────────────────────────────

async def _fetch_all_async(begin_date, end_date, needed_data):
    """Orquestra busca assíncrona de todas as contas."""
    import aiohttp

    accounts = load_accounts()
    if not accounts:
        log.error("Nenhuma conta Shopee configurada")
        return {
            'platform': PLATFORM,
            'platform_display': PLATFORM_DISPLAY,
            'orders': [],
            'payments': [],
            'seller_info': None,
            'items': [],
            'items_total': 0,
            'traffic': [],
            'ads': [],
        }

    # Convert dates to timestamps
    time_from = int(time.mktime(time.strptime(begin_date, '%Y-%m-%d')))
    fim_date = datetime.strptime(end_date, '%Y-%m-%d')
    time_to = int(time.mktime((fim_date + timedelta(days=1) - timedelta(seconds=1)).timetuple()))

    all_orders = []
    all_payments = []
    all_seller_info = []
    all_items = []
    total_items = 0
    all_traffic = []
    all_ads = []

    async with aiohttp.ClientSession() as http_session:
        for alias, account in accounts.items():
            log.info(f"   Conta: {account['display']} ({alias})")

            try:
                tokens = await ensure_valid_token(http_session, account)
                client = ShopeeApiClient(account, tokens)
            except Exception as e:
                log.warning(f"   Erro de autenticação {alias}: {e}")
                continue

            # Orders
            if 'orders' in needed_data:
                try:
                    orders = await fetch_orders_account(client, http_session, time_from, time_to, account)
                    all_orders.extend(orders)
                    log.info(f"     {len(orders)} pedidos")
                except Exception as e:
                    log.warning(f"     Erro pedidos {alias}: {e}")

            # Payments (needs order SNs from completed orders)
            if 'payments' in needed_data:
                try:
                    # Get completed order SNs for escrow
                    completed_sns = [o['id'] for o in all_orders
                                     if o.get('shop_id') == account['shop_id']
                                     and o.get('status') in ('paid', 'shipped')]
                    if completed_sns:
                        payments = await fetch_payments_account(client, http_session, completed_sns, account)
                        all_payments.extend(payments)
                        log.info(f"     {len(payments)} pagamentos")
                    else:
                        log.info(f"     0 pagamentos (sem pedidos concluídos)")
                except Exception as e:
                    log.warning(f"     Erro pagamentos {alias}: {e}")

            # Seller info
            if 'seller_info' in needed_data:
                try:
                    info = await fetch_shop_info_account(client, http_session, account)
                    all_seller_info.append(info)
                except Exception as e:
                    log.warning(f"     Erro seller info {alias}: {e}")

            # Items
            if 'items' in needed_data or 'items_total' in needed_data:
                try:
                    items, total = await fetch_items_account(client, http_session, account)
                    all_items.extend(items)
                    total_items += total
                    log.info(f"     {total} itens ativos")
                except Exception as e:
                    log.warning(f"     Erro itens {alias}: {e}")

            # Traffic
            if 'traffic' in needed_data:
                try:
                    traffic = await fetch_traffic_account(client, http_session, account)
                    all_traffic.extend(traffic)
                    log.info(f"     {len(traffic)} registros de tráfego")
                except Exception as e:
                    log.warning(f"     Erro tráfego {alias}: {e}")

            # Ads
            if 'ads' in needed_data:
                try:
                    ads = await fetch_ads_account(client, http_session, account)
                    all_ads.extend(ads)
                    log.info(f"     {len(ads)} campanhas ads")
                except Exception as e:
                    log.warning(f"     Erro ads {alias}: {e}")

    # Consolidar seller_info (primeira conta como principal, com lista de todas)
    seller_info = None
    if all_seller_info:
        seller_info = all_seller_info[0]
        if len(all_seller_info) > 1:
            seller_info['all_shops'] = all_seller_info

    return {
        'platform': PLATFORM,
        'platform_display': PLATFORM_DISPLAY,
        'orders': all_orders,
        'payments': all_payments,
        'seller_info': seller_info,
        'items': all_items,
        'items_total': total_items,
        'traffic': all_traffic,
        'ads': all_ads,
    }

# ─── Main Interface ──────────────────────────────────────────────────────────

def fetch_all(begin_date, end_date, needed_data):
    """
    Interface principal do connector Shopee.
    Busca apenas os dados solicitados de TODAS as contas e retorna consolidado.

    Args:
        begin_date: str YYYY-MM-DD
        end_date: str YYYY-MM-DD
        needed_data: set of strings ('orders', 'payments', 'seller_info', 'items', 'items_total', 'traffic', 'ads')

    Returns:
        dict no formato padrão do marketplace-report
    """
    log.info(f"🟧 Connector Shopee — {begin_date} a {end_date}")

    if not _check_aiohttp():
        log.error("aiohttp não disponível. Retornando dados vazios.")
        return {
            'platform': PLATFORM,
            'platform_display': PLATFORM_DISPLAY,
            'orders': [],
            'payments': [],
            'seller_info': None,
            'items': [],
            'items_total': 0,
            'traffic': [],
            'ads': [],
        }

    try:
        # Check if there's already a running event loop
        try:
            loop = asyncio.get_running_loop()
            # We're inside an async context, need to use nest_asyncio or create task
            import nest_asyncio
            nest_asyncio.apply()
            return asyncio.run(_fetch_all_async(begin_date, end_date, needed_data))
        except RuntimeError:
            # No running loop, safe to use asyncio.run()
            return asyncio.run(_fetch_all_async(begin_date, end_date, needed_data))
    except Exception as e:
        log.error(f"Erro fatal no connector Shopee: {e}")
        return {
            'platform': PLATFORM,
            'platform_display': PLATFORM_DISPLAY,
            'orders': [],
            'payments': [],
            'seller_info': None,
            'items': [],
            'items_total': 0,
            'traffic': [],
            'ads': [],
        }

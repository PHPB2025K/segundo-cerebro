"""
Connector Amazon BR (SP-API)
Busca dados via SP-API e retorna no formato padrão do marketplace-report.
"""

import csv
import io
import json
import logging
import os
import time
from datetime import datetime, timedelta, timezone

log = logging.getLogger('connector.amazon')

# ─── Config ──────────────────────────────────────────────────────────────────

PLATFORM = 'amazon'
PLATFORM_DISPLAY = 'Amazon'
CREDENTIALS_FILE = "/root/.openclaw/workspace/integrations/amazon/.sp-api-credentials.json"
MARKETPLACE_ID = "A2Q3Y263D00KWC"  # Amazon BR

# ─── Lazy imports (avoid crash if sp_api not installed) ──────────────────────

_sp_api_available = None

def _check_sp_api():
    global _sp_api_available
    if _sp_api_available is None:
        try:
            from sp_api.api import Orders, Finances, Reports
            from sp_api.base import Marketplaces
            from sp_api.base.exceptions import SellingApiRequestThrottledException
            _sp_api_available = True
        except ImportError:
            _sp_api_available = False
            log.warning("python-amazon-sp-api não instalado. pip install python-amazon-sp-api")
    return _sp_api_available

# ─── Helpers ─────────────────────────────────────────────────────────────────

def load_credentials():
    """Carrega credenciais SP-API do arquivo JSON."""
    if not os.path.exists(CREDENTIALS_FILE):
        log.error(f"Credenciais não encontradas: {CREDENTIALS_FILE}")
        return None
    with open(CREDENTIALS_FILE) as f:
        return json.load(f)


def api_call_with_retry(func, max_retries=5, **kwargs):
    """Executa chamada API com retry e backoff exponencial para throttling."""
    from sp_api.base.exceptions import SellingApiRequestThrottledException

    for attempt in range(max_retries):
        try:
            return func(**kwargs)
        except SellingApiRequestThrottledException:
            wait = min(2 ** attempt * 2, 30)
            log.warning(f"Throttled. Aguardando {wait}s (tentativa {attempt + 1}/{max_retries})...")
            time.sleep(wait)
        except Exception as e:
            if 'QuotaExceeded' in str(e) or 'Throttl' in str(e).lower():
                wait = min(2 ** attempt * 2, 30)
                log.warning(f"Rate limit. Aguardando {wait}s (tentativa {attempt + 1}/{max_retries})...")
                time.sleep(wait)
            else:
                log.warning(f"Erro na chamada API: {e}")
                if attempt == max_retries - 1:
                    return None
                time.sleep(2)
    log.error(f"Falha após {max_retries} tentativas")
    return None


def extract_amount(amount_obj):
    """Extrai valor numérico de um objeto Amount da Amazon."""
    if not amount_obj:
        return 0.0
    if isinstance(amount_obj, (int, float)):
        return float(amount_obj)
    if isinstance(amount_obj, dict):
        return float(amount_obj.get('CurrencyAmount', amount_obj.get('Amount', 0)) or 0)
    return 0.0


def sum_charge_list(charge_list, filter_type=None):
    """Soma valores de uma lista de charges/fees."""
    if not charge_list:
        return 0.0
    total = 0.0
    for item in charge_list:
        if filter_type and item.get('ChargeType', item.get('FeeType', '')) != filter_type:
            continue
        total += extract_amount(item.get('ChargeAmount', item.get('FeeAmount', 0)))
    return total


def _request_and_download_report(reports_api, report_type, begin, end, max_wait=120):
    """Cria um report request, poll até completar, e baixa o CSV/JSON.
    Returns raw document string or None."""
    try:
        # Create report
        create_resp = api_call_with_retry(
            reports_api.create_report,
            reportType=report_type,
            marketplaceIds=[MARKETPLACE_ID],
            dataStartTime=f"{begin}T00:00:00Z",
            dataEndTime=f"{end}T23:59:59Z",
        )
        if not create_resp:
            return None
        payload = create_resp.payload if hasattr(create_resp, 'payload') else create_resp
        report_id = payload.get('reportId') if isinstance(payload, dict) else None
        if not report_id:
            log.warning(f"Não obteve reportId para {report_type}")
            return None

        # Poll for completion
        elapsed = 0
        interval = 10
        while elapsed < max_wait:
            time.sleep(interval)
            elapsed += interval
            status_resp = api_call_with_retry(reports_api.get_report, reportId=report_id)
            if not status_resp:
                continue
            sp = status_resp.payload if hasattr(status_resp, 'payload') else status_resp
            if isinstance(sp, dict):
                status = sp.get('processingStatus', '')
                if status == 'DONE':
                    doc_id = sp.get('reportDocumentId')
                    if doc_id:
                        doc_resp = api_call_with_retry(
                            reports_api.get_report_document,
                            document_id=doc_id,
                            download=True,
                        )
                        if doc_resp:
                            dp = doc_resp.payload if hasattr(doc_resp, 'payload') else doc_resp
                            if isinstance(dp, dict):
                                return dp.get('document', dp.get('body', ''))
                            if isinstance(dp, (str, bytes)):
                                return dp if isinstance(dp, str) else dp.decode('utf-8', errors='replace')
                    return None
                elif status in ('CANCELLED', 'FATAL'):
                    log.warning(f"Report {report_type} falhou: {status}")
                    return None
            interval = min(interval + 5, 30)

        log.warning(f"Report {report_type} timeout após {max_wait}s")
        return None
    except Exception as e:
        log.warning(f"Erro ao solicitar report {report_type}: {e}")
        return None

# ─── Data Fetchers ───────────────────────────────────────────────────────────

def fetch_orders(begin, end, credentials):
    """Busca pedidos via Orders API."""
    from sp_api.api import Orders
    from sp_api.base import Marketplaces

    orders_api = Orders(credentials=credentials, marketplace=Marketplaces.BR)
    all_orders = []
    next_token = None
    page = 0

    while True:
        page += 1
        log.info(f"   Buscando pedidos — página {page}...")

        try:
            if next_token:
                response = api_call_with_retry(
                    orders_api.get_orders,
                    NextToken=next_token,
                )
            else:
                # Amazon requires ISO 8601 format
                created_after = f"{begin}T00:00:00Z"
                created_before = f"{end}T23:59:59Z"

                # PostedBefore can't be in the future
                now_utc = datetime.now(timezone.utc) - timedelta(minutes=3)
                end_dt = datetime.strptime(end, '%Y-%m-%d').replace(
                    hour=23, minute=59, second=59, tzinfo=timezone.utc
                )
                if end_dt > now_utc:
                    created_before = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')

                response = api_call_with_retry(
                    orders_api.get_orders,
                    CreatedAfter=created_after,
                    CreatedBefore=created_before,
                    MarketplaceIds=[MARKETPLACE_ID],
                    MaxResultsPerPage=100,
                )
        except Exception as e:
            log.warning(f"Erro buscando pedidos: {e}")
            break

        if response is None:
            break

        payload = response.payload if hasattr(response, 'payload') else response
        if isinstance(payload, dict):
            orders_list = payload.get('Orders', [])
            all_orders.extend(orders_list)
            next_token = payload.get('NextToken')
        else:
            break

        if not next_token:
            break

        time.sleep(0.5)

    # Fetch order items for each order
    standardized = []
    for order in all_orders:
        amazon_order_id = order.get('AmazonOrderId', '')

        # Fetch items for this order
        order_items_std = []
        try:
            items_response = api_call_with_retry(
                orders_api.get_order_items,
                order_id=amazon_order_id,
            )
            if items_response:
                items_payload = items_response.payload if hasattr(items_response, 'payload') else items_response
                if isinstance(items_payload, dict):
                    for item in items_payload.get('OrderItems', []):
                        order_items_std.append({
                            'item': {
                                'id': item.get('ASIN', ''),
                                'title': item.get('Title', ''),
                                'seller_sku': item.get('SellerSKU', ''),
                            },
                            'quantity': item.get('QuantityOrdered', 0),
                            'unit_price': extract_amount(item.get('ItemPrice', {})) / max(item.get('QuantityOrdered', 1), 1),
                        })
            time.sleep(0.3)  # Rate limit between item calls
        except Exception as e:
            log.warning(f"Erro buscando itens do pedido {amazon_order_id}: {e}")

        # Map Amazon status to standard
        status_map = {
            'Pending': 'pending',
            'Unshipped': 'confirmed',
            'PartiallyShipped': 'partially_shipped',
            'Shipped': 'shipped',
            'Canceled': 'cancelled',
            'Unfulfillable': 'cancelled',
        }
        amazon_status = order.get('OrderStatus', 'Unknown')

        # Extract total amount
        order_total = extract_amount(order.get('OrderTotal', {}))

        std_order = {
            'id': amazon_order_id,
            'date_created': order.get('PurchaseDate', ''),
            'status': status_map.get(amazon_status, amazon_status.lower()),
            'status_raw': amazon_status,
            'total_amount': order_total,
            'currency_id': order.get('OrderTotal', {}).get('CurrencyCode', 'BRL') if isinstance(order.get('OrderTotal'), dict) else 'BRL',
            'order_items': order_items_std,
            'buyer': {
                'id': order.get('BuyerInfo', {}).get('BuyerEmail', '') if isinstance(order.get('BuyerInfo'), dict) else '',
            },
            'fulfillment_channel': order.get('FulfillmentChannel', ''),
            'platform': 'amazon',
        }
        standardized.append(std_order)

    return standardized


def fetch_payments(begin, end, credentials):
    """Busca eventos financeiros via Finances API e converte para formato padrão."""
    from sp_api.api import Finances
    from sp_api.base import Marketplaces

    fin = Finances(credentials=credentials, marketplace=Marketplaces.BR)
    all_payments = []
    next_token = None
    page = 0

    # Collect all financial events
    events = {
        'ShipmentEventList': [],
        'RefundEventList': [],
        'ServiceFeeEventList': [],
        'AdjustmentEventList': [],
        'GuaranteeClaimEventList': [],
    }

    while True:
        page += 1
        log.info(f"   Buscando eventos financeiros — página {page}...")

        try:
            if next_token:
                response = api_call_with_retry(
                    fin.list_financial_events,
                    NextToken=next_token,
                )
            else:
                end_dt = datetime.strptime(end, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                now_utc = datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(minutes=3)
                if end_dt > now_utc:
                    posted_before = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
                else:
                    posted_before = f"{end}T23:59:59Z"

                response = api_call_with_retry(
                    fin.list_financial_events,
                    PostedAfter=f"{begin}T00:00:00Z",
                    PostedBefore=posted_before,
                    MaxResultsPerPage=100,
                )
        except Exception as e:
            log.warning(f"Erro buscando eventos financeiros: {e}")
            break

        if response is None:
            break

        payload = response.payload if hasattr(response, 'payload') else response
        if isinstance(payload, dict):
            fin_events = payload.get('FinancialEvents', payload)
            if isinstance(fin_events, dict):
                for key in events:
                    items = fin_events.get(key, []) or []
                    events[key].extend(items)

            next_token = payload.get('NextToken')
        else:
            break

        if not next_token:
            break

        time.sleep(0.5)

    # Convert to standard payment format
    def process_shipment_events(event_list, event_type='settlement'):
        payments = []
        for event in event_list:
            order_id = event.get('AmazonOrderId', '')
            posted_date = event.get('PostedDate', '')

            item_list = event.get('ShipmentItemList', []) or event.get('ShipmentItemAdjustmentList', []) or []

            total_charges = 0
            total_fees = 0
            fee_details = []

            for item in item_list:
                charge_list = item.get('ItemChargeList', []) or item.get('ItemChargeAdjustmentList', []) or []
                fee_list = item.get('ItemFeeList', []) or item.get('ItemFeeAdjustmentList', []) or []

                total_charges += sum_charge_list(charge_list)
                item_fees = sum_charge_list(fee_list)
                total_fees += item_fees

                # Collect fee details
                for fee in fee_list:
                    fee_type = fee.get('FeeType', 'Unknown')
                    fee_amount = extract_amount(fee.get('FeeAmount', 0))
                    if fee_amount != 0:
                        fee_details.append({
                            'type': fee_type,
                            'amount': round(abs(fee_amount), 2),
                        })

            net = total_charges + total_fees

            payment = {
                'id': f"{order_id}_{event_type}",
                'date_created': posted_date[:19].replace('T', ' ') if posted_date else '',
                'status': 'approved' if event_type == 'settlement' else event_type,
                'transaction_amount': round(total_charges, 2),
                'total_paid_amount': round(total_charges, 2),
                'net_received_amount': round(net, 2),
                'fee_details': fee_details,
                'order_id': order_id,
                'payment_type': event_type,
                'platform': 'amazon',
            }
            payments.append(payment)

        return payments

    # Process all event types
    all_payments.extend(process_shipment_events(events['ShipmentEventList'], 'settlement'))
    all_payments.extend(process_shipment_events(events['RefundEventList'], 'refund'))
    all_payments.extend(process_shipment_events(events['GuaranteeClaimEventList'], 'dispute'))

    # Service fees
    for event in events.get('ServiceFeeEventList', []):
        fee_list = event.get('FeeList', []) or []
        total = sum_charge_list(fee_list)
        if total != 0:
            order_id = event.get('AmazonOrderId', 'SERVICE_FEE')
            fee_details = []
            for fee in fee_list:
                fee_type = fee.get('FeeType', 'Unknown')
                fee_amount = extract_amount(fee.get('FeeAmount', 0))
                if fee_amount != 0:
                    fee_details.append({'type': fee_type, 'amount': round(abs(fee_amount), 2)})

            all_payments.append({
                'id': f"{order_id}_service_fee",
                'date_created': '',
                'status': 'service_fee',
                'transaction_amount': 0,
                'total_paid_amount': 0,
                'net_received_amount': round(total, 2),
                'fee_details': fee_details,
                'order_id': order_id,
                'payment_type': 'service_fee',
                'platform': 'amazon',
            })

    # Adjustments
    for event in events.get('AdjustmentEventList', []):
        amount = extract_amount(event.get('AdjustmentAmount', {}))
        adj_type = event.get('AdjustmentType', 'Adjustment')
        posted_date = event.get('PostedDate', '')

        all_payments.append({
            'id': f"adjustment_{adj_type}_{posted_date[:10] if posted_date else 'unknown'}",
            'date_created': posted_date[:19].replace('T', ' ') if posted_date else '',
            'status': 'adjustment',
            'transaction_amount': round(amount, 2),
            'total_paid_amount': round(amount, 2),
            'net_received_amount': round(amount, 2),
            'fee_details': [],
            'order_id': '',
            'payment_type': 'adjustment',
            'platform': 'amazon',
        })

    return all_payments


def fetch_seller_info():
    """Retorna info básica do seller (SP-API não tem endpoint direto equivalente ao ML)."""
    return {
        'id': 'amazon_br_seller',
        'nickname': 'GB Importadora / Budamix',
        'platform': 'amazon',
        'marketplace': 'Amazon BR',
        'marketplace_id': MARKETPLACE_ID,
        'seller_reputation': {
            'level_id': 'N/A',
            'power_seller_status': 'N/A',
        },
        'status': {
            'site_status': 'active',
        },
    }


def fetch_items(credentials):
    """Busca itens ativos via Reports API (GET_MERCHANT_LISTINGS_ALL_DATA).
    Fluxo assíncrono: createReport → poll getReport → download CSV."""
    try:
        from sp_api.api import Reports
        from sp_api.base import Marketplaces

        reports_api = Reports(credentials=credentials, marketplace=Marketplaces.BR)

        log.info("   Items: solicitando GET_MERCHANT_LISTINGS_ALL_DATA...")
        doc = _request_and_download_report(
            reports_api,
            'GET_MERCHANT_LISTINGS_ALL_DATA',
            # Listings report doesn't use date range, but API requires it — use wide range
            '2020-01-01',
            datetime.now(timezone.utc).strftime('%Y-%m-%d'),
            max_wait=180,
        )

        if not doc:
            log.warning("   Items: report não retornou dados. Retornando lista vazia.")
            return [], 0

        # Parse tab-delimited CSV
        items = []
        reader = csv.DictReader(io.StringIO(doc), delimiter='\t')
        for row in reader:
            status = row.get('status', row.get('Status', '')).lower()
            if status not in ('active', 'ativo', ''):
                continue
            items.append({
                'id': row.get('asin1', row.get('ASIN1', row.get('asin', ''))),
                'title': row.get('item-name', row.get('Title', '')),
                'seller_sku': row.get('seller-sku', row.get('Seller SKU', '')),
                'price': float(row.get('price', row.get('Price', 0)) or 0),
                'quantity': int(row.get('quantity', row.get('Quantity', 0)) or 0),
                'status': 'active',
                'platform': 'amazon',
            })

        log.info(f"   Items: {len(items)} itens ativos encontrados via report")
        return items, len(items)

    except Exception as e:
        log.warning(f"Erro buscando itens via Reports API: {e}")
        return [], 0


def fetch_traffic(begin, end, credentials):
    """Busca dados de tráfego via Reports API (GET_SALES_AND_TRAFFIC_REPORT).
    Retorna lista no formato padrão: sessions, page_views, conversion_rate por ASIN."""
    try:
        from sp_api.api import Reports
        from sp_api.base import Marketplaces

        reports_api = Reports(credentials=credentials, marketplace=Marketplaces.BR)

        log.info("   Traffic: solicitando GET_SALES_AND_TRAFFIC_REPORT...")
        doc = _request_and_download_report(
            reports_api,
            'GET_SALES_AND_TRAFFIC_REPORT',
            begin,
            end,
            max_wait=180,
        )

        if not doc:
            log.warning("   Traffic: report não retornou dados.")
            return []

        # Parse JSON report
        try:
            report_data = json.loads(doc) if isinstance(doc, str) else doc
        except (json.JSONDecodeError, TypeError):
            # Maybe it's CSV — try tab-delimited
            traffic = []
            reader = csv.DictReader(io.StringIO(doc), delimiter='\t')
            for row in reader:
                traffic.append({
                    'item_id': row.get('(Child) ASIN', row.get('asin', '')),
                    'title': row.get('Title', row.get('title', '')),
                    'sessions': int(row.get('Sessions', row.get('sessions', 0)) or 0),
                    'page_views': int(row.get('Page Views', row.get('pageViews', 0)) or 0),
                    'conversion_rate': float(row.get('Unit Session Percentage', row.get('unitSessionPercentage', 0)) or 0),
                    'date': begin,
                    'platform': 'amazon',
                })
            return traffic

        # JSON format (newer reports)
        traffic = []
        sales_traffic = report_data.get('salesAndTrafficByAsin', [])
        if not sales_traffic:
            sales_traffic = report_data.get('reportData', report_data.get('results', []))

        for entry in sales_traffic:
            asin_data = entry if isinstance(entry, dict) else {}
            child_asin = asin_data.get('childAsin', asin_data.get('parentAsin', ''))
            traffic_data = asin_data.get('trafficByAsin', asin_data)

            sessions = traffic_data.get('sessions', traffic_data.get('browserSessions', 0)) or 0
            page_views = traffic_data.get('pageViews', traffic_data.get('browserPageViews', 0)) or 0
            conversion = traffic_data.get('unitSessionPercentage',
                         traffic_data.get('buyBoxPercentage', 0)) or 0

            traffic.append({
                'item_id': child_asin,
                'title': asin_data.get('title', ''),
                'sessions': int(sessions),
                'page_views': int(page_views),
                'conversion_rate': float(conversion),
                'date': asin_data.get('date', begin),
                'platform': 'amazon',
            })

        log.info(f"   Traffic: {len(traffic)} ASINs com dados de tráfego")
        return traffic

    except Exception as e:
        log.warning(f"Erro buscando tráfego Amazon: {e}")
        return []


def fetch_ads(begin, end, credentials):
    """Busca dados de Ads. Tenta Supabase (Bidspark) primeiro, fallback para SP-API Reports."""
    ads = []

    # Tentativa 1: Supabase Bidspark (amazon_campaigns)
    try:
        ads = _fetch_ads_supabase(begin, end)
        if ads:
            log.info(f"   Ads: {len(ads)} campanhas via Supabase/Bidspark")
            return ads
    except Exception as e:
        log.warning(f"   Ads Supabase indisponível: {e}")

    # Tentativa 2: SP-API Reports (GET_SPONSORED_PRODUCTS_REPORT)
    try:
        from sp_api.api import Reports
        from sp_api.base import Marketplaces

        reports_api = Reports(credentials=credentials, marketplace=Marketplaces.BR)

        log.info("   Ads: solicitando relatório Sponsored Products via SP-API...")
        doc = _request_and_download_report(
            reports_api,
            'GET_SPONSORED_PRODUCTS_REPORT',
            begin,
            end,
            max_wait=180,
        )

        if not doc:
            log.warning("   Ads: report não retornou dados.")
            return []

        # Parse tab-delimited CSV
        reader = csv.DictReader(io.StringIO(doc), delimiter='\t')
        campaigns_agg = {}
        for row in reader:
            cid = row.get('Campaign Id', row.get('campaignId', 'unknown'))
            cname = row.get('Campaign Name', row.get('campaignName', ''))
            cstatus = row.get('Campaign Status', row.get('status', 'active')).lower()

            if cid not in campaigns_agg:
                campaigns_agg[cid] = {
                    'campaign_id': cid,
                    'campaign_name': cname,
                    'status': 'active' if cstatus in ('enabled', 'active', 'ativo') else 'paused',
                    'cost': 0.0,
                    'revenue': 0.0,
                    'clicks': 0,
                    'impressions': 0,
                    'platform': 'amazon',
                }

            c = campaigns_agg[cid]
            c['cost'] += float(row.get('Spend', row.get('cost', 0)) or 0)
            c['revenue'] += float(row.get('7 Day Total Sales', row.get('attributedSales7d', row.get('sales', 0))) or 0)
            c['clicks'] += int(row.get('Clicks', row.get('clicks', 0)) or 0)
            c['impressions'] += int(row.get('Impressions', row.get('impressions', 0)) or 0)

        for c in campaigns_agg.values():
            c['roas'] = round(c['revenue'] / c['cost'], 2) if c['cost'] > 0 else 0
            c['acos'] = round((c['cost'] / c['revenue'] * 100), 2) if c['revenue'] > 0 else 0
            c['cpc'] = round(c['cost'] / c['clicks'], 2) if c['clicks'] > 0 else 0
            c['ctr'] = round((c['clicks'] / c['impressions'] * 100), 2) if c['impressions'] > 0 else 0
            ads.append(c)

        log.info(f"   Ads: {len(ads)} campanhas via SP-API Reports")
        return ads

    except Exception as e:
        log.warning(f"Erro buscando ads Amazon via Reports: {e}")
        return []


def _fetch_ads_supabase(begin, end):
    """Tenta buscar dados de ads do Supabase (Bidspark integration)."""
    import urllib.request
    import urllib.error

    supabase_url = os.environ.get('SUPABASE_URL', '')
    supabase_key = os.environ.get('SUPABASE_KEY', '')
    if not supabase_url or not supabase_key:
        return []

    url = (f"{supabase_url}/rest/v1/amazon_campaigns"
           f"?date=gte.{begin}&date=lte.{end}"
           f"&select=campaign_id,campaign_name,status,cost,revenue,clicks,impressions")

    req = urllib.request.Request(url, headers={
        'apikey': supabase_key,
        'Authorization': f'Bearer {supabase_key}',
    })
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        rows = json.loads(resp.read())
    except Exception:
        return []

    # Aggregate by campaign
    campaigns_agg = {}
    for row in rows:
        cid = str(row.get('campaign_id', ''))
        if cid not in campaigns_agg:
            campaigns_agg[cid] = {
                'campaign_id': cid,
                'campaign_name': row.get('campaign_name', ''),
                'status': row.get('status', 'active'),
                'cost': 0.0, 'revenue': 0.0, 'clicks': 0, 'impressions': 0,
                'platform': 'amazon',
            }
        c = campaigns_agg[cid]
        c['cost'] += float(row.get('cost', 0) or 0)
        c['revenue'] += float(row.get('revenue', 0) or 0)
        c['clicks'] += int(row.get('clicks', 0) or 0)
        c['impressions'] += int(row.get('impressions', 0) or 0)

    ads = []
    for c in campaigns_agg.values():
        c['roas'] = round(c['revenue'] / c['cost'], 2) if c['cost'] > 0 else 0
        c['acos'] = round((c['cost'] / c['revenue'] * 100), 2) if c['revenue'] > 0 else 0
        c['cpc'] = round(c['cost'] / c['clicks'], 2) if c['clicks'] > 0 else 0
        c['ctr'] = round((c['clicks'] / c['impressions'] * 100), 2) if c['impressions'] > 0 else 0
        ads.append(c)
    return ads


# ─── Main Interface ──────────────────────────────────────────────────────────

def fetch_all(begin_date, end_date, needed_data):
    """
    Interface principal do connector Amazon.
    Busca apenas os dados solicitados e retorna no formato padrão.

    Args:
        begin_date: str YYYY-MM-DD
        end_date: str YYYY-MM-DD
        needed_data: set of strings ('orders', 'payments', 'seller_info', 'items', 'items_total', 'traffic', 'ads')

    Returns:
        dict no formato padrão do marketplace-report
    """
    log.info(f"🟠 Connector Amazon — {begin_date} a {end_date}")

    result = {
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

    if not _check_sp_api():
        log.error("python-amazon-sp-api não disponível. Retornando dados vazios.")
        return result

    credentials = load_credentials()
    if not credentials:
        log.error("Credenciais Amazon não disponíveis. Retornando dados vazios.")
        return result

    if 'orders' in needed_data:
        log.info("   → Pedidos Amazon...")
        try:
            result['orders'] = fetch_orders(begin_date, end_date, credentials)
            log.info(f"     {len(result['orders'])} pedidos")
        except Exception as e:
            log.warning(f"Erro buscando pedidos Amazon: {e}")

    if 'payments' in needed_data:
        log.info("   → Pagamentos/Finances Amazon...")
        try:
            result['payments'] = fetch_payments(begin_date, end_date, credentials)
            log.info(f"     {len(result['payments'])} eventos financeiros")
        except Exception as e:
            log.warning(f"Erro buscando pagamentos Amazon: {e}")

    if 'seller_info' in needed_data:
        log.info("   → Info vendedor Amazon...")
        result['seller_info'] = fetch_seller_info()

    if 'items' in needed_data or 'items_total' in needed_data:
        log.info("   → Anúncios Amazon...")
        try:
            items, total = fetch_items(credentials)
            result['items'] = items
            result['items_total'] = total
            log.info(f"     {total} itens")
        except Exception as e:
            log.warning(f"Erro buscando itens Amazon: {e}")

    if 'traffic' in needed_data:
        log.info("   → Tráfego Amazon...")
        try:
            result['traffic'] = fetch_traffic(begin_date, end_date, credentials)
            log.info(f"     {len(result['traffic'])} registros de tráfego")
        except Exception as e:
            log.warning(f"Erro buscando tráfego Amazon: {e}")

    if 'ads' in needed_data:
        log.info("   → Ads Amazon...")
        try:
            result['ads'] = fetch_ads(begin_date, end_date, credentials)
            log.info(f"     {len(result['ads'])} campanhas")
        except Exception as e:
            log.warning(f"Erro buscando ads Amazon: {e}")

    return result

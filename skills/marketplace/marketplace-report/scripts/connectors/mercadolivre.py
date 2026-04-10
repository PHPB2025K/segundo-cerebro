"""
Connector Mercado Livre / Mercado Pago
Busca dados via API e retorna no formato padrão do marketplace-report.
"""

import json
import logging
import os
import subprocess
import urllib.request
import urllib.error

log = logging.getLogger('connector.ml')

# ─── Config ──────────────────────────────────────────────────────────────────

USER_ID = 532562281
PLATFORM = 'mercadolivre'
PLATFORM_DISPLAY = 'Mercado Livre'

TOKEN_FILES = {
    'vendas': '/root/.openclaw/.ml-tokens.json',
    'finance': '/root/.openclaw/.ml-tokens-finance.json',
    'metrics': '/root/.openclaw/.ml-tokens-metrics.json',
}
REFRESH_SCRIPT = '/root/.openclaw/workspace/skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh'

# ─── Helpers ─────────────────────────────────────────────────────────────────

def refresh_tokens():
    for app_type in ['vendas', 'finance', 'metrics']:
        try:
            result = subprocess.run(['bash', REFRESH_SCRIPT, app_type],
                                    capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                log.info(f"Token ML/{app_type} renovado")
            else:
                log.warning(f"Falha refresh ML/{app_type}: {result.stderr[:100]}")
        except Exception as e:
            log.warning(f"Erro refresh ML/{app_type}: {e}")


def load_token(app_type):
    path = TOKEN_FILES.get(app_type)
    if not path or not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)['access_token']


def api_get(url, token, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
            resp = urllib.request.urlopen(req, timeout=30)
            return json.loads(resp.read())
        except Exception as e:
            if attempt == retries:
                log.warning(f"API ML falhou: {url}: {e}")
                return None


def fetch_paginated(base_url, token, limit=50, max_pages=20):
    all_results = []
    offset = 0
    for _ in range(max_pages):
        sep = '&' if '?' in base_url else '?'
        data = api_get(f"{base_url}{sep}limit={limit}&offset={offset}", token)
        if not data:
            break
        results = data.get('results', [])
        all_results.extend(results)
        if offset + limit >= data.get('paging', {}).get('total', 0) or not results:
            break
        offset += limit
    return all_results

# ─── Data Fetchers ───────────────────────────────────────────────────────────

def fetch_orders(begin, end, token):
    url = (f"https://api.mercadolibre.com/orders/search?seller={USER_ID}"
           f"&order.date_created.from={begin}T00:00:00.000-03:00"
           f"&order.date_created.to={end}T23:59:59.000-03:00&sort=date_desc")
    return fetch_paginated(url, token)


def fetch_payments(begin, end, token):
    url = (f"https://api.mercadopago.com/v1/payments/search"
           f"?begin_date={begin}T00:00:00Z&end_date={end}T23:59:59Z"
           f"&sort=date_created&criteria=desc")
    return fetch_paginated(url, token)


def fetch_seller_info(token):
    return api_get(f"https://api.mercadolibre.com/users/{USER_ID}", token)


def fetch_active_items(token):
    data = api_get(f"https://api.mercadolibre.com/users/{USER_ID}/items/search?status=active", token)
    if not data:
        return [], 0
    item_ids = data.get('results', [])
    total = data.get('paging', {}).get('total', 0)
    items = []
    for item_id in item_ids[:50]:
        item = api_get(f"https://api.mercadolibre.com/items/{item_id}", token)
        if item:
            items.append(item)
    return items, total


def fetch_ads(begin, end, token):
    """Busca campanhas ML Ads com métricas."""
    ADV_ID = '172453'
    SITE = 'MLB'
    url = (f"https://api.mercadolibre.com/marketplace/advertising/{SITE}/advertisers/{ADV_ID}"
           f"/product_ads/campaigns/search?metrics=clicks,prints,cost,total_amount,acos,roas,cpc,ctr"
           f"&date_from={begin}&date_to={end}&limit=50")
    data = api_get(url, token)
    if not data or 'results' not in data:
        return []

    ads = []
    for c in data.get('results', []):
        m = c.get('metrics', {})
        cost = m.get('cost', 0) or 0
        revenue = m.get('total_amount', 0) or 0
        clicks = m.get('clicks', 0) or 0
        impressions = m.get('prints', 0) or 0
        ads.append({
            'campaign_id': str(c.get('id', '')),
            'campaign_name': c.get('name', ''),
            'status': c.get('status', 'active'),
            'cost': float(cost),
            'revenue': float(revenue),
            'clicks': int(clicks),
            'impressions': int(impressions),
            'roas': float(m.get('roas', 0) or 0),
            'acos': float(m.get('acos', 0) or 0),
            'cpc': float(m.get('cpc', 0) or 0),
            'ctr': float(m.get('ctr', 0) or 0),
            'platform': 'mercadolivre',
        })
    return ads


# ─── Main Interface ──────────────────────────────────────────────────────────

def fetch_all(begin_date, end_date, needed_data):
    """
    Interface principal do connector.
    Busca apenas os dados solicitados e retorna no formato padrão.
    
    Args:
        begin_date: str YYYY-MM-DD
        end_date: str YYYY-MM-DD
        needed_data: set of strings ('orders', 'payments', 'seller_info', 'items', 'items_total')
    
    Returns:
        dict no formato padrão do marketplace-report
    """
    log.info(f"🟢 Connector ML — {begin_date} a {end_date}")
    
    refresh_tokens()
    token_vendas = load_token('vendas')
    token_finance = load_token('finance')
    
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

    if 'orders' in needed_data:
        log.info("   → Pedidos ML...")
        result['orders'] = fetch_orders(begin_date, end_date, token_vendas)
        log.info(f"     {len(result['orders'])} pedidos")
    
    if 'payments' in needed_data:
        log.info("   → Pagamentos MP...")
        result['payments'] = fetch_payments(begin_date, end_date, token_finance)
        log.info(f"     {len(result['payments'])} pagamentos")
    
    if 'seller_info' in needed_data:
        log.info("   → Info vendedor ML...")
        result['seller_info'] = fetch_seller_info(token_vendas)
    
    if 'items' in needed_data or 'items_total' in needed_data:
        log.info("   → Anúncios ML...")
        items, total = fetch_active_items(token_vendas)
        result['items'] = items
        result['items_total'] = total
        log.info(f"     {total} ativos")

    if 'ads' in needed_data:
        log.info("   → Ads ML...")
        try:
            result['ads'] = fetch_ads(begin_date, end_date, token_vendas)
            log.info(f"     {len(result['ads'])} campanhas ads")
        except Exception as e:
            log.warning(f"Erro buscando ads ML: {e}")

    return result

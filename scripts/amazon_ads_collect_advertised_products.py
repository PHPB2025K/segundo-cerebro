#!/usr/bin/env python3
import argparse, datetime as dt, gzip, io, json, os, sys, time
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Iterable, List, Optional
import requests

AMAZON_TOKEN_URL = 'https://api.amazon.com/auth/o2/token'
AMAZON_REPORT_URL = 'https://advertising-api.amazon.com/reporting/reports'
DEFAULT_TIMEOUT = 60


def q(s: str) -> str:
    return s.replace("'", "''")


def dec(v: Any) -> Optional[str]:
    if v is None or v == '':
        return None
    try:
        return str(Decimal(str(v)))
    except (InvalidOperation, ValueError):
        return None


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


class SupabaseAdmin:
    def __init__(self, project_ref: str, mgmt_token: str):
        self.project_ref = project_ref
        self.url = f'https://api.supabase.com/v1/projects/{project_ref}/database/query'
        self.s = requests.Session()
        self.s.headers.update({'Authorization': f'Bearer {mgmt_token}', 'Content-Type': 'application/json'})

    def query(self, sql: str) -> List[Dict[str, Any]]:
        r = self.s.post(self.url, json={'query': sql}, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):
            return data
        return [data]


class AmazonAdsClient:
    def __init__(self, client_id: str, client_secret: str, refresh_token: str, profile_id: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.profile_id = profile_id
        self.access_token = None
        self.s = requests.Session()

    def refresh_access_token(self) -> str:
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        r = self.s.post(AMAZON_TOKEN_URL, data=payload, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        token = r.json()['access_token']
        self.access_token = token
        return token

    def _headers(self, create=False):
        if not self.access_token:
            self.refresh_access_token()
        content = 'application/vnd.createasyncreportrequest.v3+json' if create else 'application/json'
        return {
            'Amazon-Advertising-API-ClientId': self.client_id,
            'Amazon-Advertising-API-Scope': self.profile_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': content,
        }

    def create_report(self, start_date: str, end_date: str, time_unit: str = 'DAILY') -> str:
        payload = {
            'name': f'SP advertised product report {start_date} to {end_date}',
            'startDate': start_date,
            'endDate': end_date,
            'configuration': {
                'adProduct': 'SPONSORED_PRODUCTS',
                'groupBy': ['advertiser'],
                'columns': [
                    'campaignId', 'campaignName', 'adGroupId', 'adId',
                    'advertisedAsin', 'advertisedSku', 'date',
                    'impressions', 'clicks', 'cost', 'sales7d', 'purchases7d',
                    'unitsSoldClicks7d', 'acosClicks7d', 'roasClicks7d',
                    'clickThroughRate', 'costPerClick'
                ],
                'reportTypeId': 'spAdvertisedProduct',
                'timeUnit': time_unit,
                'format': 'GZIP_JSON'
            }
        }
        r = self.s.post(AMAZON_REPORT_URL, headers=self._headers(create=True), json=payload, timeout=DEFAULT_TIMEOUT)
        if r.status_code >= 400:
            raise requests.HTTPError(f'{r.status_code} creating report: {r.text[:1000]}', response=r)
        return r.json()['reportId']

    def get_report(self, report_id: str) -> Dict[str, Any]:
        r = self.s.get(f'{AMAZON_REPORT_URL}/{report_id}', headers=self._headers(), timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def wait_report(self, report_id: str, poll_seconds=10, max_wait_seconds=600) -> Dict[str, Any]:
        deadline = time.time() + max_wait_seconds
        while time.time() < deadline:
            data = self.get_report(report_id)
            status = data.get('status')
            if status == 'COMPLETED':
                return data
            if status in {'FAILED', 'CANCELLED'}:
                raise RuntimeError(f'Report {report_id} ended with status={status}: {data}')
            time.sleep(poll_seconds)
        raise TimeoutError(f'Report {report_id} not completed in time')

    def download_report(self, url: str) -> List[Dict[str, Any]]:
        r = self.s.get(url, timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        raw = gzip.GzipFile(fileobj=io.BytesIO(r.content)).read()
        data = json.loads(raw.decode('utf-8'))
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and 'rows' in data:
            return data['rows']
        raise RuntimeError(f'Unexpected report payload type: {type(data)}')


def daterange(start: dt.date, end: dt.date) -> Iterable[dt.date]:
    cur = start
    while cur <= end:
        yield cur
        cur += dt.timedelta(days=1)


def fetch_token_row(db: SupabaseAdmin) -> Dict[str, Any]:
    rows = db.query("select profile_id, marketplace, refresh_token, client_id, client_secret from public.amazon_ads_tokens order by created_at desc limit 1;")
    if not rows:
        raise RuntimeError('amazon_ads_tokens sem registros')
    return rows[0]


def fetch_campaign_role_map(db: SupabaseAdmin) -> Dict[str, Dict[str, Any]]:
    rows = db.query("select product_group_id::text as product_group_id, campaign_id, campaign_role from public.amazon_ads_campaign_roles where active = true;")
    return {r['campaign_id']: r for r in rows}


def ensure_sql_table(db: SupabaseAdmin, sql_path: str):
    sql = open(sql_path, 'r', encoding='utf-8').read()
    db.query(sql)


def sql_value(v: Any) -> str:
    if v is None:
        return 'null'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float, Decimal)):
        return str(v)
    return f"'{q(str(v))}'"


def upsert_rows(db: SupabaseAdmin, rows: List[Dict[str, Any]]):
    if not rows:
        return
    chunksize = 200
    for i in range(0, len(rows), chunksize):
        chunk = rows[i:i+chunksize]
        values = []
        for r in chunk:
            values.append("(" + ", ".join([
                sql_value(r.get('report_date')), sql_value(r.get('campaign_id')), sql_value(r.get('campaign_name')),
                sql_value(r.get('ad_group_id')), sql_value(r.get('ad_id')), sql_value(r.get('advertised_asin')),
                sql_value(r.get('advertised_sku')), sql_value(r.get('product_group_id')), sql_value(r.get('campaign_role')),
                sql_value(r.get('impressions', 0)), sql_value(r.get('clicks', 0)), sql_value(r.get('spend', '0')),
                sql_value(r.get('sales_7d', '0')), sql_value(r.get('purchases_7d', 0)), sql_value(r.get('units_sold_7d', 0)),
                sql_value(r.get('acos_7d')), sql_value(r.get('roas_7d')), sql_value(r.get('ctr')), sql_value(r.get('cpc_avg')),
                sql_value(r.get('currency')), sql_value(json.dumps(r.get('raw_payload', {}), ensure_ascii=False)), sql_value(r.get('collected_at'))
            ]) + ")")
        sql = f"""
insert into public.amazon_ads_advertised_products_daily (
  report_date, campaign_id, campaign_name, ad_group_id, ad_id, advertised_asin, advertised_sku,
  product_group_id, campaign_role, impressions, clicks, spend, sales_7d, purchases_7d, units_sold_7d,
  acos_7d, roas_7d, ctr, cpc_avg, currency, raw_payload, collected_at
) values
{',\n'.join(values)}
on conflict (report_date, campaign_id, ad_group_id, ad_id, advertised_asin, advertised_sku_key) do update set
  campaign_name = excluded.campaign_name,
  product_group_id = excluded.product_group_id,
  campaign_role = excluded.campaign_role,
  impressions = excluded.impressions,
  clicks = excluded.clicks,
  spend = excluded.spend,
  sales_7d = excluded.sales_7d,
  purchases_7d = excluded.purchases_7d,
  units_sold_7d = excluded.units_sold_7d,
  acos_7d = excluded.acos_7d,
  roas_7d = excluded.roas_7d,
  ctr = excluded.ctr,
  cpc_avg = excluded.cpc_avg,
  currency = excluded.currency,
  raw_payload = excluded.raw_payload,
  collected_at = excluded.collected_at;
"""
        db.query(sql)


def normalize_row(raw: Dict[str, Any], role_map: Dict[str, Dict[str, Any]], collected_at: str) -> Dict[str, Any]:
    campaign_id = str(raw.get('campaignId') or raw.get('campaign_id') or '')
    m = role_map.get(campaign_id, {})
    report_date = raw.get('date') or raw.get('reportDate')
    return {
        'report_date': report_date,
        'campaign_id': campaign_id,
        'campaign_name': raw.get('campaignName'),
        'ad_group_id': str(raw.get('adGroupId') or '') or None,
        'ad_id': str(raw.get('adId') or ''),
        'advertised_asin': raw.get('advertisedAsin'),
        'advertised_sku': raw.get('advertisedSku'),
        'product_group_id': m.get('product_group_id'),
        'campaign_role': m.get('campaign_role'),
        'impressions': int(raw.get('impressions') or 0),
        'clicks': int(raw.get('clicks') or 0),
        'spend': dec(raw.get('cost')) or '0',
        'sales_7d': dec(raw.get('sales7d')) or '0',
        'purchases_7d': int(raw.get('purchases7d') or 0),
        'units_sold_7d': int(raw.get('unitsSoldClicks7d') or 0),
        'acos_7d': dec(raw.get('acosClicks7d')),
        'roas_7d': dec(raw.get('roasClicks7d')),
        'ctr': dec(raw.get('clickThroughRate')),
        'cpc_avg': dec(raw.get('costPerClick')),
        'currency': raw.get('currencyCode') or raw.get('currency'),
        'raw_payload': raw,
        'collected_at': collected_at,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--project-ref', default=os.getenv('SUPABASE_PROJECT_REF'))
    ap.add_argument('--supabase-token', default=os.getenv('SUPABASE_ACCESS_TOKEN'))
    ap.add_argument('--start-date')
    ap.add_argument('--end-date')
    ap.add_argument('--days', type=int, default=1)
    ap.add_argument('--poll-seconds', type=int, default=10)
    ap.add_argument('--max-wait-seconds', type=int, default=600)
    ap.add_argument('--ensure-schema', action='store_true')
    ap.add_argument('--schema-sql', default='/root/segundo-cerebro/sql/amazon_ads_advertised_products_daily.sql')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--report-id', help='Resume/download an existing Amazon Ads report id for a single date range')
    args = ap.parse_args()
    if not args.project_ref or not args.supabase_token:
        raise SystemExit('Missing SUPABASE_PROJECT_REF or SUPABASE_ACCESS_TOKEN')
    db = SupabaseAdmin(args.project_ref, args.supabase_token)
    if args.ensure_schema:
        ensure_sql_table(db, args.schema_sql)
    token_row = fetch_token_row(db)
    client = AmazonAdsClient(
        client_id=token_row['client_id'],
        client_secret=token_row['client_secret'],
        refresh_token=token_row['refresh_token'],
        profile_id=token_row['profile_id'],
    )
    role_map = fetch_campaign_role_map(db)
    today = dt.date.today()
    if args.start_date:
        start = dt.date.fromisoformat(args.start_date)
        end = dt.date.fromisoformat(args.end_date or args.start_date)
    else:
        end = today - dt.timedelta(days=1)
        start = end - dt.timedelta(days=args.days - 1)
    total_rows = 0
    collected_at = now_utc()
    for d in daterange(start, end):
        day = d.isoformat()
        report_id = args.report_id if args.report_id else client.create_report(day, day, time_unit='DAILY')
        meta = client.wait_report(report_id, poll_seconds=args.poll_seconds, max_wait_seconds=args.max_wait_seconds)
        rows = client.download_report(meta['url'])
        norm = [normalize_row(r, role_map, collected_at) for r in rows if r.get('advertisedAsin') and r.get('adId')]
        total_rows += len(norm)
        if args.dry_run:
            print(json.dumps({'date': day, 'report_id': report_id, 'rows': len(norm), 'sample': norm[:2]}, ensure_ascii=False))
        else:
            upsert_rows(db, norm)
            print(json.dumps({'date': day, 'report_id': report_id, 'rows': len(norm)}, ensure_ascii=False))
    print(json.dumps({'ok': True, 'start_date': start.isoformat(), 'end_date': end.isoformat(), 'total_rows': total_rows}, ensure_ascii=False))

if __name__ == '__main__':
    main()

create table if not exists public.amazon_ads_advertised_products_daily (
  id bigserial primary key,
  report_date date not null,
  campaign_id text not null,
  campaign_name text,
  ad_group_id text,
  ad_id text not null,
  advertised_asin text not null,
  advertised_sku text,
  advertised_sku_key text generated always as (coalesce(advertised_sku, '')) stored,
  product_group_id uuid,
  campaign_role text,
  impressions integer not null default 0,
  clicks integer not null default 0,
  spend numeric(12,2) not null default 0,
  sales_7d numeric(12,2) not null default 0,
  purchases_7d integer not null default 0,
  units_sold_7d integer not null default 0,
  acos_7d numeric(10,4),
  roas_7d numeric(12,4),
  ctr numeric(10,6),
  cpc_avg numeric(12,4),
  currency text,
  raw_payload jsonb,
  collected_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint amazon_ads_advertised_products_daily_uniq
    unique (report_date, campaign_id, ad_group_id, ad_id, advertised_asin, advertised_sku_key)
);

create index if not exists idx_aapd_report_date on public.amazon_ads_advertised_products_daily(report_date desc);
create index if not exists idx_aapd_campaign on public.amazon_ads_advertised_products_daily(campaign_id, report_date desc);
create index if not exists idx_aapd_asin on public.amazon_ads_advertised_products_daily(advertised_asin, report_date desc);
create index if not exists idx_aapd_group on public.amazon_ads_advertised_products_daily(product_group_id, report_date desc);

create or replace function public.touch_amazon_ads_advertised_products_daily_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_touch_aapd_updated_at on public.amazon_ads_advertised_products_daily;
create trigger trg_touch_aapd_updated_at
before update on public.amazon_ads_advertised_products_daily
for each row execute function public.touch_amazon_ads_advertised_products_daily_updated_at();

create or replace view public.amazon_ads_advertised_products_daily_enriched as
select
  d.*,
  pga.product_name,
  pg.group_name
from public.amazon_ads_advertised_products_daily d
left join public.amazon_ads_product_group_asins pga
  on pga.product_group_id = d.product_group_id
 and pga.asin = d.advertised_asin
left join public.amazon_ads_product_groups pg
  on pg.id = d.product_group_id;

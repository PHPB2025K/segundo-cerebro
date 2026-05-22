#!/usr/bin/env python3
"""Probe ML Ads API availability.

Investigação de timing: quando exatamente a API ML Marketplace Advertising
disponibiliza as métricas do dia anterior?

Chama o mesmo endpoint que o `ml-snapshot-fetcher.py` usa e salva um snapshot
mínimo (timestamp da chamada + soma cost + soma revenue + nº de campanhas
com cost>0). Resultado fica em /root/.openclaw/ml-ads-probe/.

Uso: probe-ml-ads-availability.py [YYYY-MM-DD]
Default: ontem em BRT (igual ao cron oficial).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, "/root/segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors")
import mercadolivre as ml  # noqa: E402

BRT = timezone(timedelta(hours=-3))
PROBE_DIR = Path("/root/.openclaw/ml-ads-probe")
PROBE_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    if len(sys.argv) > 1:
        target_date = sys.argv[1]
    else:
        target_date = (datetime.now(BRT).date() - timedelta(days=1)).isoformat()

    ml.refresh_tokens()
    token = ml.load_token("vendas")
    campaigns = ml.fetch_ads(target_date, target_date, token)

    active = [c for c in campaigns if (c.get("status") or "").lower() == "active"]
    with_spend = [c for c in campaigns if c.get("cost", 0) > 0]

    snapshot = {
        "probed_at_brt": datetime.now(BRT).isoformat(timespec="seconds"),
        "target_date": target_date,
        "campaigns_total": len(campaigns),
        "campaigns_active": len(active),
        "campaigns_with_cost_gt_zero": len(with_spend),
        "total_cost_brl": round(sum(c.get("cost", 0) for c in campaigns), 2),
        "total_revenue_brl": round(sum(c.get("revenue", 0) for c in campaigns), 2),
        "ads_available": len(with_spend) > 0,
    }

    stamp = datetime.now(BRT).strftime("%Y-%m-%d-%H%M")
    out = PROBE_DIR / f"probe-{target_date}-from-{stamp}.json"
    out.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False))
    print(json.dumps(snapshot, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

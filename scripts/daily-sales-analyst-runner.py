#!/usr/bin/env python3
"""
Daily Sales Analyst Runner — Phase 4 (Dry-Run)

Executes Layer 0 + 7 layers sequentially, generates auditable artifacts
per date/recipient, with NO real send.

Usage:
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --dry-run
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --shadow
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --dry-run --recipients lucas,yasmin
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --dry-run --package path/to/package.json

Limitations:
    - Deterministic fallback: no LLM calls. Layers 1-6 produce placeholder
      artifacts based on data package metrics. QA marks them accordingly.
    - send_real_allowed=false enforced in all modes.
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- Constants ---
WORKSPACE = Path(__file__).resolve().parent.parent
CONFIG_PATHS = [
    WORKSPACE / "shared" / "daily-sales-analyst" / "config" / "daily-sales-analyst.json",
    Path("/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/config/daily-sales-analyst.json"),
]
DEFAULT_PACKAGE_DIR = Path("/root/segundo-cerebro/reports/daily-sales-report-v2/layered/packages")
RUNS_DIR = WORKSPACE / "shared" / "daily-sales-analyst" / "runs"

VALID_MODES = {"dry-run": "DRY_RUN", "shadow": "SHADOW", "preview": "PREVIEW"}
ALL_RECIPIENTS = ["lucas", "yasmin", "leonardo"]

RECIPIENT_PLATFORM = {
    "lucas": "shopee",
    "yasmin": "mercado_livre",
    "leonardo": "amazon",
}

RECIPIENT_ACCOUNTS = {
    "lucas": ["shopee-budamix-store", "shopee-budamix-oficial-2", "shopee-budamix-shop-3"],
    "yasmin": ["mercado-livre"],
    "leonardo": ["amazon"],
}

# --- Helpers ---

def load_config():
    for p in CONFIG_PATHS:
        if p.exists():
            with open(p) as f:
                return json.load(f)
    print("FATAL: Config daily-sales-analyst.json not found.", file=sys.stderr)
    sys.exit(1)


def load_package(date_str, package_path=None):
    if package_path:
        p = Path(package_path)
    else:
        p = DEFAULT_PACKAGE_DIR / date_str / "package.json"
    if not p.exists():
        return None, str(p)
    with open(p) as f:
        return json.load(f), str(p)


def now_utc():
    return datetime.now(timezone.utc).isoformat()


def get_failed_checks(data_readiness):
    failed = []
    for c in data_readiness.get("checks", []):
        if c.get("status") == "fail":
            failed.append(c)
    return failed


def recipient_data(package, recipient_name):
    """Extract recipient-specific data from package."""
    key = recipient_name.capitalize()
    return package.get("recipients", {}).get(key, {})


def accounts_data(package, recipient_name):
    """Extract account-level data for a recipient."""
    slugs = RECIPIENT_ACCOUNTS.get(recipient_name, [])
    platforms = package.get("platforms", {})
    return {s: platforms[s] for s in slugs if s in platforms}


# --- Layer Generators (Deterministic Fallback) ---

def gen_layer00_data_package(package, run_dir, recipient_name):
    """Copy data package as 00-data-package.json for each recipient."""
    path = run_dir / recipient_name / "00-data-package.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(package, f, indent=2, ensure_ascii=False)
    return str(path)


def gen_layer01_estrategica(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 1: Strategic analysis (deterministic fallback)."""
    path = run_dir / recipient_name / "01-estrategica.md"
    rec = recipient_data(package, recipient_name)
    accs = accounts_data(package, recipient_name)

    if blocked:
        content = f"""# Camada 1 — Analise Estrategica: {recipient_name.capitalize()}
## Status: BLOCKED
**Motivo:** {block_reason}
**Data:** {package.get('date', 'N/A')}

> Analise bloqueada por Data Readiness NOT_READY.
> Nenhum raciocinio estrategico foi executado.
> Este artefato e um placeholder deterministico (sem LLM).
"""
    else:
        totals = rec.get("totals", {})
        content = f"""# Camada 1 — Analise Estrategica: {recipient_name.capitalize()}
## Status: FALLBACK_DETERMINISTICO
**Data:** {package.get('date', 'N/A')}
**Plataforma:** {rec.get('platform', 'N/A')}

### Metricas Consolidadas
- Pedidos: {totals.get('orders', 'N/A')}
- GMV: R$ {totals.get('gmv', 'N/A')}
- Ticket Medio: R$ {totals.get('ticket_medio', 'N/A')}
- Cancelamentos: {totals.get('cancelamentos', 'N/A')}

> **AVISO:** Este artefato foi gerado por fallback deterministico.
> Nao houve analise LLM profunda. Os dados acima sao extraidos
> diretamente do data package para auditoria.
"""
    with open(path, "w") as f:
        f.write(content)
    return str(path)


def gen_layer02_tatica(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 2: Tactical analysis (deterministic fallback)."""
    path = run_dir / recipient_name / "02-tatica.md"
    accs = accounts_data(package, recipient_name)

    if blocked:
        content = f"""# Camada 2 — Analise Tatica: {recipient_name.capitalize()}
## Status: BLOCKED
**Motivo:** {block_reason}

> Analise bloqueada. Placeholder deterministico.
"""
    else:
        lines = [f"# Camada 2 — Analise Tatica: {recipient_name.capitalize()}",
                 f"## Status: FALLBACK_DETERMINISTICO",
                 f"**Data:** {package.get('date', 'N/A')}\n"]
        for slug, acc in accs.items():
            m = acc.get("metrics", {})
            h = acc.get("historical", {})
            changes = h.get("changes", {})
            lines.append(f"### {acc.get('account_name', slug)}")
            lines.append(f"- Pedidos: {m.get('pedidos_validos', 'N/A')} | GMV: R$ {m.get('gmv', 'N/A')}")
            lines.append(f"- Ticket: R$ {m.get('ticket_medio', 'N/A')}")
            lines.append(f"- vs 7d: {changes.get('orders_vs_7d_pct', 'N/A')}% pedidos, {changes.get('gmv_vs_7d_pct', 'N/A')}% GMV")
            lines.append(f"- vs 30d: {changes.get('orders_vs_30d_pct', 'N/A')}% pedidos, {changes.get('gmv_vs_30d_pct', 'N/A')}% GMV")
            qf = acc.get("quality_flags", [])
            if qf:
                lines.append(f"- Quality flags: {', '.join(f['code'] for f in qf)}")
            lines.append("")
        lines.append("> **AVISO:** Fallback deterministico, sem analise LLM.")
        content = "\n".join(lines)

    with open(path, "w") as f:
        f.write(content)
    return str(path)


def gen_layer03_operacional(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 3: Operational analysis (deterministic fallback)."""
    path = run_dir / recipient_name / "03-operacional.md"
    accs = accounts_data(package, recipient_name)

    if blocked:
        content = f"""# Camada 3 — Analise Operacional: {recipient_name.capitalize()}
## Status: BLOCKED
**Motivo:** {block_reason}

> Analise bloqueada. Placeholder deterministico.
"""
    else:
        lines = [f"# Camada 3 — Analise Operacional: {recipient_name.capitalize()}",
                 f"## Status: FALLBACK_DETERMINISTICO",
                 f"**Data:** {package.get('date', 'N/A')}\n"]
        for slug, acc in accs.items():
            m = acc.get("metrics", {})
            lines.append(f"### {acc.get('account_name', slug)}")
            top = m.get("top_products", [])[:5]
            if top:
                lines.append("**Top Produtos:**")
                for i, p in enumerate(top, 1):
                    lines.append(f"  {i}. {p.get('title', 'N/A')} — qty: {p.get('quantity', 0)}")
            lines.append(f"- Top3 concentracao: {m.get('top3_concentration', 'N/A')}%")
            lines.append(f"- Top5 concentracao: {m.get('top5_concentration', 'N/A')}%")
            ff = m.get("fulfillment", {})
            if ff.get("amazon_fba", 0) > 0:
                lines.append(f"- FBA: {ff['amazon_fba']} pedidos")
            lines.append("")
        lines.append("> **AVISO:** Fallback deterministico, sem analise LLM.")
        content = "\n".join(lines)

    with open(path, "w") as f:
        f.write(content)
    return str(path)


def gen_layer04_granular(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 4: Granular investigation (JSON)."""
    path = run_dir / recipient_name / "04-granular.json"
    accs = accounts_data(package, recipient_name)
    rec = recipient_data(package, recipient_name)

    if blocked:
        data = {
            "layer": "04-granular",
            "recipient": recipient_name,
            "status": "BLOCKED",
            "reason": block_reason,
            "date": package.get("date"),
            "investigations": [],
            "fallback": True,
            "llm_used": False,
        }
    else:
        investigations = []
        for slug, acc in accs.items():
            m = acc.get("metrics", {})
            h = acc.get("historical", {}).get("changes", {})
            inv = {
                "account": slug,
                "pedidos": m.get("pedidos_validos"),
                "gmv": m.get("gmv"),
                "ticket_medio": m.get("ticket_medio"),
                "orders_vs_30d_pct": h.get("orders_vs_30d_pct"),
                "gmv_vs_30d_pct": h.get("gmv_vs_30d_pct"),
                "top3_concentration": m.get("top3_concentration"),
                "quality_flags": [f["code"] for f in acc.get("quality_flags", [])],
            }
            investigations.append(inv)
        data = {
            "layer": "04-granular",
            "recipient": recipient_name,
            "status": "FALLBACK_DETERMINISTICO",
            "date": package.get("date"),
            "platform": rec.get("platform"),
            "investigations": investigations,
            "fallback": True,
            "llm_used": False,
            "warning": "Dados extraidos diretamente do package. Sem investigacao LLM profunda.",
        }

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return str(path)


def gen_layer05_condensadora(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 5: Condenser (JSON)."""
    path = run_dir / recipient_name / "05-condensadora.json"
    rec = recipient_data(package, recipient_name)

    if blocked:
        data = {
            "layer": "05-condensadora",
            "recipient": recipient_name,
            "status": "BLOCKED",
            "reason": block_reason,
            "date": package.get("date"),
            "condensed_output": None,
            "fallback": True,
            "llm_used": False,
        }
    else:
        totals = rec.get("totals", {})
        data = {
            "layer": "05-condensadora",
            "recipient": recipient_name,
            "status": "FALLBACK_DETERMINISTICO",
            "date": package.get("date"),
            "platform": rec.get("platform"),
            "condensed_output": {
                "orders": totals.get("orders"),
                "gmv": totals.get("gmv"),
                "ticket_medio": totals.get("ticket_medio"),
                "cancelamentos": totals.get("cancelamentos"),
            },
            "fallback": True,
            "llm_used": False,
            "warning": "Condensacao deterministica. Sem LLM.",
        }

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return str(path)


def gen_layer06_slack_preview(package, run_dir, recipient_name, blocked, block_reason):
    """Layer 6: Slack preview (markdown)."""
    path = run_dir / recipient_name / "06-slack-preview.md"
    rec = recipient_data(package, recipient_name)

    if blocked:
        content = f"""# Camada 6 — Slack Preview: {recipient_name.capitalize()}
## Status: BLOCKED
**Motivo:** {block_reason}

> Mensagem Slack NAO gerada. Data Readiness bloqueou a pipeline.
> send_real_allowed = false
"""
    else:
        totals = rec.get("totals", {})
        content = f"""# Camada 6 — Slack Preview: {recipient_name.capitalize()}
## Status: FALLBACK_DETERMINISTICO
**Data:** {package.get('date', 'N/A')}
**send_real_allowed:** false

### Preview (placeholder — sem formatacao LLM)

> Resumo {package.get('date')}: {rec.get('platform', 'N/A')}
> Pedidos: {totals.get('orders', 'N/A')} | GMV: R$ {totals.get('gmv', 'N/A')} | Ticket: R$ {totals.get('ticket_medio', 'N/A')}
> Cancelamentos: {totals.get('cancelamentos', 'N/A')}

> **AVISO:** Texto placeholder. Nao e mensagem final formatada.
> Nenhum envio real sera feito.
"""

    with open(path, "w") as f:
        f.write(content)
    return str(path)


def gen_layer07_qa(package, run_dir, recipient_name, blocked, block_reason, data_readiness_status):
    """Layer 7: QA Gate (JSON)."""
    path = run_dir / recipient_name / "07-qa.json"

    if blocked:
        data = {
            "layer": "07-qa",
            "recipient": recipient_name,
            "date": package.get("date"),
            "verdict": "BLOCKED",
            "checks_passed": 0,
            "checks_total": 1,
            "blockers": [block_reason],
            "remarks": [
                "Pipeline bloqueada por Data Readiness NOT_READY.",
                "Artefatos gerados como placeholders deterministicos.",
            ],
            "send_allowed": False,
            "send_real_allowed": False,
            "fallback": True,
            "llm_used": False,
        }
    else:
        remarks = [
            "Artefatos gerados por fallback deterministico (sem LLM).",
            "Dados extraidos diretamente do data package v1.0.",
            f"Data Readiness: {data_readiness_status}.",
        ]
        data = {
            "layer": "07-qa",
            "recipient": recipient_name,
            "date": package.get("date"),
            "verdict": "APPROVED_WITH_REMARKS",
            "checks_passed": 1,
            "checks_total": 1,
            "blockers": [],
            "remarks": remarks,
            "send_allowed": False,
            "send_real_allowed": False,
            "fallback": True,
            "llm_used": False,
        }

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return str(path)


# --- Main Runner ---

def run(date_str, mode, recipients, config, package_path=None, prompt_version=None):
    print(f"=== Daily Sales Analyst Runner ===")
    print(f"Date: {date_str} | Mode: {mode}")
    print(f"Recipients: {', '.join(recipients)}")
    print()

    # Validate config
    if not config.get("enabled", False):
        print("ABORT: Config enabled=false. Pipeline disabled.")
        sys.exit(1)

    if not config.get("layer0_required", True):
        print("ABORT: layer0_required=false inconsistent with Phase 4.")
        sys.exit(1)

    pv = prompt_version or config.get("pinned_prompt_version") or config.get("prompt_version", "v3.0")
    dbv = config.get("data_builder_version", "v1.0")

    # Load package
    package, pkg_path = load_package(date_str, package_path)
    if package is None:
        print(f"FATAL: Package not found at {pkg_path}", file=sys.stderr)
        sys.exit(1)
    print(f"Package loaded: {pkg_path}")

    # Data Readiness
    dr = package.get("data_readiness", {})
    dr_status = dr.get("status", "NOT_READY")
    dr_quality = dr.get("data_quality", "not_ready")
    failed_checks = get_failed_checks(dr)

    print(f"Data Readiness: {dr_status} (quality: {dr_quality})")
    if failed_checks:
        for fc in failed_checks:
            print(f"  FAIL: {fc['check']} — {fc.get('detail', '')}")

    is_blocked = dr_status == "NOT_READY"
    block_reason = ""
    if is_blocked:
        reasons = [f"{fc['check']}: {fc.get('detail', '')}" for fc in failed_checks]
        block_reason = f"Data Readiness NOT_READY. Checks failed: {'; '.join(reasons)}"
        print(f"\nPipeline BLOCKED: {block_reason}\n")
    print()

    # Create run dir
    run_dir = RUNS_DIR / date_str
    run_dir.mkdir(parents=True, exist_ok=True)

    # Filter recipients by config
    active_recipients = []
    for r in recipients:
        key = f"{r}_enabled"
        if config.get(key, True):
            active_recipients.append(r)
        else:
            print(f"SKIP: {r} disabled in config.")

    # Generate artifacts per recipient
    recipient_results = {}
    artifact_paths = {}

    for r in active_recipients:
        print(f"--- Processing: {r} ---")
        paths = {}

        paths["00-data-package"] = gen_layer00_data_package(package, run_dir, r)
        paths["01-estrategica"] = gen_layer01_estrategica(package, run_dir, r, is_blocked, block_reason)
        paths["02-tatica"] = gen_layer02_tatica(package, run_dir, r, is_blocked, block_reason)
        paths["03-operacional"] = gen_layer03_operacional(package, run_dir, r, is_blocked, block_reason)
        paths["04-granular"] = gen_layer04_granular(package, run_dir, r, is_blocked, block_reason)
        paths["05-condensadora"] = gen_layer05_condensadora(package, run_dir, r, is_blocked, block_reason)
        paths["06-slack-preview"] = gen_layer06_slack_preview(package, run_dir, r, is_blocked, block_reason)
        paths["07-qa"] = gen_layer07_qa(package, run_dir, r, is_blocked, block_reason, dr_status)

        artifact_paths[r] = paths

        if is_blocked:
            status = "BLOCKED"
            qa_verdict = "BLOCKED"
            blockers = [block_reason]
            warnings = ["Artefatos placeholder deterministicos gerados para auditoria."]
        else:
            status = "APPROVED_WITH_REMARKS"
            qa_verdict = "APPROVED_WITH_REMARKS"
            blockers = []
            warnings = ["Fallback deterministico: sem analise LLM profunda."]

        recipient_results[r] = {
            "platform": RECIPIENT_PLATFORM.get(r, "unknown"),
            "status": status,
            "send_allowed": False,
            "slack_payload": None,
            "layers": {
                "layer0_data_package": paths["00-data-package"],
                "layer1_estrategica": paths["01-estrategica"],
                "layer2_tatica": paths["02-tatica"],
                "layer3_operacional": paths["03-operacional"],
                "layer4_granular": paths["04-granular"],
                "layer5_condensadora": paths["05-condensadora"],
                "layer6_slack_writer": paths["06-slack-preview"],
                "layer7_qa_gate": paths["07-qa"],
            },
            "qa": {
                "verdict": qa_verdict,
                "checks_passed": 0 if is_blocked else 1,
                "checks_total": 1,
                "blockers": blockers,
                "remarks": warnings,
            },
            "blockers": blockers,
            "warnings": warnings,
        }
        print(f"  Status: {status} | Artifacts: {len(paths)} files")

    # Global status
    statuses = [r["status"] for r in recipient_results.values()]
    if all(s == "BLOCKED" for s in statuses):
        global_status = "BLOCKED"
    elif all(s in ("APPROVED", "APPROVED_WITH_REMARKS") for s in statuses):
        global_status = "APPROVED_WITH_REMARKS" if "APPROVED_WITH_REMARKS" in statuses else "APPROVED"
    else:
        global_status = "PARTIAL"

    global_failure = "layer0" if is_blocked else False

    # Build manifest
    manifest = {
        "schema_version": "daily-sales-analyst-run/v1.0",
        "date": date_str,
        "generated_at_utc": now_utc(),
        "mode": VALID_MODES.get(mode, mode.upper()),
        "send_real_allowed": False,
        "global_status": global_status,
        "global_failure": global_failure,
        "prompt_version": pv,
        "data_builder_version": dbv,
        "package_path": pkg_path,
        "data_readiness": {
            "status": dr_status,
            "data_quality": dr_quality,
            "failed_checks": [c["check"] for c in failed_checks],
        },
        "recipients": recipient_results,
        "escalation": {
            "required": is_blocked,
            "reason": "Data Readiness NOT_READY — pipeline blocked" if is_blocked else None,
            "severity": "high" if is_blocked else None,
            "details": [block_reason] if is_blocked else None,
        },
        "audit_refs": {
            "run_dir": str(run_dir),
            "manifest_path": str(run_dir / "manifest.json"),
            "layer_artifacts": artifact_paths,
        },
        "memory_updates": {
            "suggested": [],
            "applied": [],
        },
        "runner_meta": {
            "fallback_mode": True,
            "llm_used": False,
            "limitations": [
                "Runner deterministico: sem chamadas LLM.",
                "Camadas 1-6 sao placeholders baseados no data package.",
                "QA reflete limitacao do fallback.",
            ],
        },
    }

    manifest_path = run_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n=== Run Complete ===")
    print(f"Global Status: {global_status}")
    print(f"Global Failure: {global_failure}")
    print(f"send_real_allowed: False")
    print(f"Manifest: {manifest_path}")
    print(f"Run Dir: {run_dir}")
    for r in active_recipients:
        print(f"  {r}: {recipient_results[r]['status']}")

    return manifest


def main():
    parser = argparse.ArgumentParser(description="Daily Sales Analyst Runner (Phase 4 — Dry-Run)")
    parser.add_argument("date", help="Date to analyze (YYYY-MM-DD)")

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--dry-run", action="store_const", const="dry-run", dest="mode")
    mode_group.add_argument("--shadow", action="store_const", const="shadow", dest="mode")
    mode_group.add_argument("--preview", action="store_const", const="preview", dest="mode")

    parser.add_argument("--recipients", type=str, default=None,
                        help="Comma-separated recipients (default: all)")
    parser.add_argument("--prompt-version", type=str, default=None,
                        help="Prompt version (default: from config)")
    parser.add_argument("--package", type=str, default=None,
                        help="Path to data package JSON")

    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"FATAL: Invalid date format: {args.date}. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # Parse recipients
    if args.recipients:
        recipients = [r.strip().lower() for r in args.recipients.split(",")]
        invalid = [r for r in recipients if r not in ALL_RECIPIENTS]
        if invalid:
            print(f"FATAL: Invalid recipients: {invalid}. Valid: {ALL_RECIPIENTS}", file=sys.stderr)
            sys.exit(1)
    else:
        recipients = list(ALL_RECIPIENTS)

    config = load_config()

    # Enforce send_real_allowed=false
    if config.get("send_real_enabled", False):
        print("WARNING: Config has send_real_enabled=true but Phase 4 enforces false.")

    manifest = run(args.date, args.mode, recipients, config,
                   package_path=args.package, prompt_version=args.prompt_version)

    # Final safety assertion
    assert manifest["send_real_allowed"] is False, "CRITICAL: send_real_allowed must be false!"


if __name__ == "__main__":
    main()

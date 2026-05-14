#!/usr/bin/env python3
"""Daily Sales Report v2.5 — runner preview das camadas.

Lê um package.json gerado por `daily-sales-v2-build-package.py` e produz artefatos
por destinatário para as camadas 3–7:
- Camada 3: operacional
- Camada 4: granular
- Camada 5: condensadora
- Camada 6: Slack Writer preview
- Camada 7: QA Gate preview

Garantias desta fase:
- NÃO mexe em cron.
- NÃO envia Slack.
- NÃO chama LLM.
- NÃO altera memória do Trader.
- Produz artefatos auditáveis para revisão antes de qualquer rollout.

Uso:
    python3 scripts/daily-sales-v2-layered-preview.py 2026-05-12
    python3 scripts/daily-sales-v2-layered-preview.py 2026-05-12 --package path/to/package.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parent.parent
PACKAGE_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "packages"
RUNS_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "runs"

PLATFORM_LABELS = {"shopee": "SHOPEE", "ml": "MERCADO LIVRE", "amazon": "AMAZON"}
FORBIDDEN_SECTIONS = ["📊 RESUMO GERAL", "🛒 VENDAS POR CANAL", "DESTAQUES DO DIA"]
REQUIRED_SECTIONS = ["📊 VISÃO", "🏆 TOP PRODUTOS", "🔍 ANÁLISE DA CONTA", "🎯 PRIORIDADES DO DIA"]


def brl(value: float | int | None) -> str:
    value = float(value or 0)
    s = f"R$ {value:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    return f"{float(value):+.1f}%".replace(".", ",")


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def product_name(product: dict[str, Any]) -> str:
    title = (product.get("title") or "").strip()
    if title:
        title = re.sub(r"\s+", " ", title)
        title = re.split(r"\s+-\s+Budamix\b", title, maxsplit=1)[0]
        title = re.sub(r"\s+Budamix\b.*$", "", title).strip()
        return title[:90].rstrip() + ("..." if len(title) > 90 else "")
    sku = (product.get("sku") or "").strip()
    if sku:
        return sku.replace("_", " ")
    return "Produto sem identidade confiável"


def collect_top_products(package: dict[str, Any], account_slugs: list[str]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for slug in account_slugs:
        account = package["accounts"][slug]
        for product in account["metrics"].get("top_products", []):
            name = product_name(product)
            key = name.lower()
            bucket = grouped.setdefault(key, {
                "name": name,
                "quantity": 0,
                "platform_item_ids": set(),
                "skus": set(),
            })
            bucket["quantity"] += int(product.get("quantity") or 0)
            if product.get("platform_item_id"):
                bucket["platform_item_ids"].add(str(product["platform_item_id"]))
            if product.get("sku"):
                bucket["skus"].add(str(product["sku"]))
    out = []
    for item in grouped.values():
        out.append({
            "name": item["name"],
            "quantity": item["quantity"],
            "platform_item_ids": sorted(item["platform_item_ids"]),
            "skus_internal": sorted(item["skus"]),
        })
    return sorted(out, key=lambda x: x["quantity"], reverse=True)[:10]


def account_line(account: dict[str, Any]) -> str:
    m = account["metrics"]
    h = account["historical"]["changes"]
    return (
        f"- {account['account_name']}: {m['pedidos_validos']} pedidos, {brl(m['gmv'])}, "
        f"ticket {brl(m['ticket_medio'])}, {m['cancelamentos']} cancelamentos; "
        f"vs 30d: pedidos {pct(h.get('orders_vs_30d_pct'))}, GMV {pct(h.get('gmv_vs_30d_pct'))}; "
        f"top3 {str(m.get('top3_concentration', 0)).replace('.', ',')}%."
    )


def build_operational(package: dict[str, Any], recipient: str) -> str:
    cfg = package["recipients"][recipient]
    platform_label = PLATFORM_LABELS[cfg["platform"]]
    lines = [
        f"# Camada 3 — Operacional — {recipient} / {platform_label}",
        "",
        f"Data analisada: {package['date']} — {package['brt_window']['display']}",
        "Fonte: Supabase `orders` em janela BRT, cancelados excluídos dos totais válidos.",
        "",
        "## Visão objetiva da plataforma",
        f"- Faturamento: {brl(cfg['totals']['gmv'])}",
        f"- Pedidos: {cfg['totals']['orders']}",
        f"- Ticket médio: {brl(cfg['totals']['ticket_medio'])}",
        f"- Cancelamentos: {cfg['totals']['cancelamentos']}",
        "",
        "## Raio-X por unidade operacional",
    ]
    for slug in cfg["accounts"]:
        lines.append(account_line(package["accounts"][slug]))
    lines.extend([
        "",
        "## O que precisa ser investigado pela Granular",
    ])
    for slug in cfg["accounts"]:
        acc = package["accounts"][slug]
        flags = acc.get("quality_flags", [])
        if flags:
            for flag in flags:
                lines.append(f"- {acc['account_name']}: validar `{flag['code']}` — {flag['message']}")
        h = acc["historical"]["changes"]
        if h.get("orders_vs_30d_pct") is not None and abs(h["orders_vs_30d_pct"]) >= 20:
            lines.append(f"- {acc['account_name']}: explicar variação forte de pedidos vs 30d ({pct(h['orders_vs_30d_pct'])}).")
        if acc["metrics"].get("top3_concentration", 0) >= 60:
            lines.append(f"- {acc['account_name']}: avaliar risco de concentração de mix/top produtos.")
    if lines[-1] == "## O que precisa ser investigado pela Granular":
        lines.append("- Sem investigação obrigatória crítica; granular deve apenas validar consistência e procurar conflito de evidência.")
    return "\n".join(lines) + "\n"


def build_granular(package: dict[str, Any], recipient: str) -> dict[str, Any]:
    cfg = package["recipients"][recipient]
    checks = []
    for slug in cfg["accounts"]:
        acc = package["accounts"][slug]
        rec = acc["reconciliation"]
        checks.append({
            "account": acc["account_name"],
            "question": "A fonte granular reconcilia com a fonte canônica BRT?",
            "status": "ok" if rec.get("ok") else "blocked",
            "confidence": "alta" if rec.get("ok") else "baixa",
            "evidence": rec,
            "slack_block": not bool(rec.get("ok")),
        })
        for flag in acc.get("quality_flags", []):
            checks.append({
                "account": acc["account_name"],
                "question": f"Flag de qualidade `{flag['code']}` impede interpretação?",
                "status": "blocked" if flag["level"] == "critical" else "warning",
                "confidence": "media" if flag["level"] != "critical" else "baixa",
                "evidence": flag,
                "slack_block": flag["level"] == "critical",
            })
    return {
        "layer": "camada-4-granular",
        "recipient": recipient,
        "platform": cfg["platform"],
        "date": package["date"],
        "checks": checks,
        "blocked_for_slack": any(c["slack_block"] for c in checks),
    }


def insight_for_account(account: dict[str, Any]) -> str:
    m = account["metrics"]
    h = account["historical"]["changes"]
    name = account["account_name"]
    orders_delta = h.get("orders_vs_30d_pct")
    gmv_delta = h.get("gmv_vs_30d_pct")
    conc = m.get("top3_concentration", 0)
    if orders_delta is not None and orders_delta <= -20:
        return f"{name} perdeu tração contra a média de 30 dias ({pct(orders_delta)} em pedidos e {pct(gmv_delta)} em GMV), então a leitura principal é queda de exposição/demanda antes de mexer em margem."
    if orders_delta is not None and orders_delta >= 20:
        return f"{name} rodou acima do patamar recente ({pct(orders_delta)} em pedidos e {pct(gmv_delta)} em GMV), mas precisa validar se o ganho veio de tráfego saudável ou concentração pontual de mix."
    if conc >= 65:
        return f"{name} está dependente dos produtos líderes: top 3 concentram {str(conc).replace('.', ',')}% das unidades, o que aumenta risco se anúncio, estoque ou ranking desses itens oscilar."
    ticket = brl(m.get("ticket_medio", 0))
    orders = m.get("pedidos_validos", 0)
    return f"{name} operou com {orders} pedidos e ticket {ticket}, sem desvio significativo contra a média recente; estrutura de mix e volume mantida."


def build_condenser(package: dict[str, Any], recipient: str, granular: dict[str, Any]) -> dict[str, Any]:
    cfg = package["recipients"][recipient]
    insights = []
    for slug in cfg["accounts"]:
        insights.append(insight_for_account(package["accounts"][slug]))
    # Shopee pode ter 3 contas; limitar forte a 3 insights finais.
    insights = insights[:3]
    priorities = []
    if granular["blocked_for_slack"]:
        priorities.append("Não enviar Slack real antes de resolver os bloqueios críticos apontados pela Granular/QA.")
    for slug in cfg["accounts"]:
        acc = package["accounts"][slug]
        h = acc["historical"]["changes"]
        if h.get("orders_vs_30d_pct") is not None and h["orders_vs_30d_pct"] <= -20:
            priorities.append(f"Investigar causa da queda de pedidos em {acc['account_name']} ({pct(h['orders_vs_30d_pct'])} vs 30d): verificar se houve perda de tráfego, ruptura de estoque ou mudança de ranking antes de qualquer ajuste de preço.")
        elif acc["metrics"].get("top3_concentration", 0) >= 65:
            priorities.append(f"Validar estoque, ranking e campanha dos produtos líderes em {acc['account_name']}; concentração alta vira risco operacional se um item cair.")
    if not priorities:
        priorities.append("Dia dentro da faixa operacional sem ruptura; sem ação estrutural necessária — foco em disponibilidade e execução.")
    return {
        "layer": "camada-5-condensadora",
        "recipient": recipient,
        "platform": cfg["platform"],
        "date": package["date"],
        "final_insights": insights[:3],
        "priorities": priorities[:3],
        "discarded": "Comparativos secos e métricas já cobertas na visão/top produtos foram mantidos fora da análise final.",
        "blocked_for_slack": granular["blocked_for_slack"],
    }


def build_slack_preview(package: dict[str, Any], recipient: str, condenser: dict[str, Any]) -> str:
    cfg = package["recipients"][recipient]
    platform_label = PLATFORM_LABELS[cfg["platform"]]
    top_products = collect_top_products(package, cfg["accounts"])
    lines = [
        f"DAILY SALES REPORT — {platform_label} — {datetime.strptime(package['date'], '%Y-%m-%d').strftime('%d/%m/%Y')} (Ontem)",
        "",
        f"📊 VISÃO {platform_label}",
        f"- Faturamento: {brl(cfg['totals']['gmv'])}",
        f"- Pedidos: {cfg['totals']['orders']}",
        f"- Ticket médio: {brl(cfg['totals']['ticket_medio'])}",
        f"- Cancelamentos: {cfg['totals']['cancelamentos']}",
        "",
        f"🏆 TOP PRODUTOS {platform_label}",
    ]
    for i, product in enumerate(top_products[:5], 1):
        lines.append(f"- {i}. {product['name']} — {product['quantity']} un.")
    if not top_products:
        lines.append("- Ranking bloqueado: nenhum produto com identidade confiável no pacote.")
    lines.extend([
        "",
        "🔍 ANÁLISE DA CONTA",
    ])
    for insight in condenser["final_insights"]:
        lines.append(f"- {insight}")
    lines.extend([
        "",
        "🎯 PRIORIDADES DO DIA",
    ])
    for priority in condenser["priorities"]:
        lines.append(f"- {priority}")
    lines.extend([
        "",
        f"Dia analisado: {datetime.strptime(package['date'], '%Y-%m-%d').strftime('%d/%m/%Y')} — 00:00–23:59 BRT",
    ])
    return "\n".join(lines) + "\n"


SHALLOW_PRIORITY_PATTERNS = [
    re.compile(r"\b(monitorar|acompanhar|observar)\b.*\b(amanhã|se repet[ei]|próximos dias)\b", re.IGNORECASE),
    re.compile(r"\bchecar (exposição|ADS|listing)\b(?!.*\b(porque|pois|dado que|evidência|sinal)\b)", re.IGNORECASE),
    re.compile(r"\bobservar se (o padrão )?se repete?\b", re.IGNORECASE),
    re.compile(r"\bmanter rotina\b.*\bobservar\b", re.IGNORECASE),
]

SHALLOW_INSIGHT_PATTERNS = [
    re.compile(r"\bprecisa validar\b(?!.*\b(porque|pois|dado que|evidência)\b)", re.IGNORECASE),
    re.compile(r"\bficou dentro de uma faixa operacional\b", re.IGNORECASE),
]

CONSOLIDATED_SECTION_PATTERNS = [
    re.compile(r"📊 RESUMO GERAL", re.IGNORECASE),
    re.compile(r"🛒 VENDAS POR CANAL", re.IGNORECASE),
    re.compile(r"DESTAQUES DO DIA", re.IGNORECASE),
    re.compile(r"VISÃO CONSOLIDADA", re.IGNORECASE),
    re.compile(r"RESUMO DO DIA", re.IGNORECASE),
]


def _check_shallow_content(text: str, patterns: list[re.Pattern], label: str) -> list[str]:
    """Check for shallow/generic phrases that lack evidence or falsifiable conditions."""
    issues = []
    for pattern in patterns:
        matches = pattern.findall(text)
        if matches:
            issues.append(f"{label} rasa/genérica detectada: padrão '{pattern.pattern}' encontrado sem condição ou evidência.")
    return issues


def qa_gate(slack_text: str, granular: dict[str, Any], condenser: dict[str, Any], package: dict[str, Any], recipient: str) -> dict[str, Any]:
    errors = []
    warnings = []

    # --- Structural checks ---
    for section in FORBIDDEN_SECTIONS:
        if section in slack_text:
            errors.append(f"Seção proibida encontrada: {section}")
    for section in REQUIRED_SECTIONS:
        if section not in slack_text:
            errors.append(f"Seção obrigatória ausente: {section}")

    # --- Product identity ---
    if "Produto não identificado" in slack_text or "Produto sem identidade confiável" in slack_text:
        errors.append("Produto sem identidade confiável apareceu no texto final.")

    # --- Raw SKU check ---
    raw_sku_pattern = re.compile(r"\b[A-Z0-9]{2,}_[A-Z0-9_]{2,}\b")
    raw_skus = raw_sku_pattern.findall(slack_text)
    if raw_skus:
        errors.append(f"SKU cru detectado no texto final: {', '.join(raw_skus[:3])}")

    # --- Granular block ---
    if granular["blocked_for_slack"]:
        errors.append("Granular marcou bloqueio para Slack.")

    # --- Insight count ---
    if len(condenser.get("final_insights", [])) > 3:
        errors.append("Condensadora passou de 3 insights finais.")

    # --- send_real_allowed ---
    if package["pipeline"].get("send_real_allowed") is not False:
        errors.append("Package preview não está explicitamente travado contra envio real.")

    # --- Priority count ---
    if len(condenser.get("priorities", [])) > 3:
        warnings.append("Mais de 3 prioridades detectadas; preview truncou para 3.")

    # --- HARDENED: Block shallow/generic priorities ---
    priorities_text = "\n".join(condenser.get("priorities", []))
    shallow_priority_issues = _check_shallow_content(priorities_text, SHALLOW_PRIORITY_PATTERNS, "Prioridade")
    for issue in shallow_priority_issues:
        warnings.append(issue)

    # --- HARDENED: Block shallow/generic insights ---
    insights_text = "\n".join(condenser.get("final_insights", []))
    shallow_insight_issues = _check_shallow_content(insights_text, SHALLOW_INSIGHT_PATTERNS, "Insight")
    for issue in shallow_insight_issues:
        warnings.append(issue)

    # --- HARDENED: Block metric repetition without thesis ---
    for insight in condenser.get("final_insights", []):
        # Check if insight just repeats metric numbers without interpretation
        numbers = re.findall(r"[+-]?\d+[.,]\d+%", insight)
        interpretive_words = re.findall(r"\b(porque|portanto|isso significa|o que indica|sugere que|então|logo)\b", insight, re.IGNORECASE)
        if len(numbers) >= 2 and not interpretive_words:
            warnings.append(f"Insight repete métricas sem tese interpretativa: '{insight[:80]}...'")

    # --- HARDENED: Block consolidated sections reintroduced by Slack Writer ---
    for pattern in CONSOLIDATED_SECTION_PATTERNS:
        if pattern.search(slack_text):
            errors.append(f"Seção consolidada proibida reintroduzida no Slack: padrão '{pattern.pattern}'")

    # --- Determine status ---
    # Shallow warnings become errors if 3+ accumulate (systemic shallow analysis)
    shallow_warning_count = len(shallow_priority_issues) + len(shallow_insight_issues)
    if shallow_warning_count >= 3:
        errors.append(f"Análise sistematicamente rasa: {shallow_warning_count} padrões genéricos detectados — bloqueio por acúmulo.")

    status = "BLOQUEADO" if errors else "APROVADO COM RESSALVA" if warnings else "APROVADO"
    return {
        "layer": "camada-7-qa-gate-preview",
        "recipient": recipient,
        "date": package["date"],
        "status": status,
        "send_real_allowed": False,
        "errors": errors,
        "warnings": warnings,
        "shallow_checks": {
            "priority_issues": shallow_priority_issues,
            "insight_issues": shallow_insight_issues,
            "systemic_block": shallow_warning_count >= 3,
        },
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def write_artifacts(package: dict[str, Any], recipient: str, out_dir: Path) -> dict[str, str]:
    rec_slug = slugify(recipient)
    rec_dir = out_dir / rec_slug
    rec_dir.mkdir(parents=True, exist_ok=True)
    operational = build_operational(package, recipient)
    granular = build_granular(package, recipient)
    condenser = build_condenser(package, recipient, granular)
    slack = build_slack_preview(package, recipient, condenser)
    qa = qa_gate(slack, granular, condenser, package, recipient)

    files = {
        "operational": rec_dir / "camada-3-operacional.md",
        "granular": rec_dir / "camada-4-granular.json",
        "condenser": rec_dir / "camada-5-condensadora.json",
        "slack_preview": rec_dir / "camada-6-slack-writer-preview.md",
        "qa_gate": rec_dir / "camada-7-qa-gate-preview.json",
    }
    files["operational"].write_text(operational, encoding="utf-8")
    files["granular"].write_text(json.dumps(granular, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    files["condenser"].write_text(json.dumps(condenser, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    files["slack_preview"].write_text(slack, encoding="utf-8")
    files["qa_gate"].write_text(json.dumps(qa, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return {k: str(v) for k, v in files.items()}


def run(date_str: str, package_path: Path | None = None) -> dict[str, Any]:
    package_path = package_path or (PACKAGE_BASE / date_str / "package.json")
    package = json.loads(package_path.read_text(encoding="utf-8"))
    out_dir = RUNS_BASE / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": "daily-sales-layered-preview-run/v1",
        "date": date_str,
        "package_path": str(package_path),
        "run_dir": str(out_dir),
        "send_real_allowed": False,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "recipients": {},
    }
    for recipient in sorted(package["recipients"]):
        manifest["recipients"][recipient] = write_artifacts(package, recipient, out_dir)
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Daily Sales v2.5 layered preview")
    parser.add_argument("date", help="Data analisada em YYYY-MM-DD (BRT)")
    parser.add_argument("--package", dest="package_path", help="Caminho opcional para package.json")
    args = parser.parse_args()
    datetime.strptime(args.date, "%Y-%m-%d")
    manifest = run(args.date, Path(args.package_path) if args.package_path else None)
    statuses = {}
    for recipient, files in manifest["recipients"].items():
        qa = json.loads(Path(files["qa_gate"]).read_text(encoding="utf-8"))
        statuses[recipient] = qa["status"]
    print(json.dumps({"run_dir": manifest["run_dir"], "statuses": statuses, "send_real_allowed": False}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

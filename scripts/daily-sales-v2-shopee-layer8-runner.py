#!/usr/bin/env python3
"""Daily Sales v2 — Camada 8 Shopee via LLM.

Roda depois das 7 camadas por conta. Para a Shopee, usa as três saídas da
Camada Condensadora (Budamix Store, Oficial e Shop) como input exclusivo da
síntese consolidada que alimenta o Slack Writer.

Nunca envia Slack. Apenas salva artefato auditável.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parent.parent
PACKAGE_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "packages"
RUNS_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "runs"
PROMPTS = WORKSPACE / "prompts" / "daily-sales"

SHOPEE_ACCOUNTS = [
    ("shopee-budamix-store", "Budamix Store", "Shopee 1"),
    ("shopee-budamix-oficial-2", "Budamix Oficial", "Shopee 2"),
    ("shopee-budamix-shop-3", "Budamix Shop", "Shopee 3"),
]

LAYER_PROMPTS = [
    (1, "estrategica", "camada-1-estrategica.md"),
    (2, "tatica", "camada-2-tatica.md"),
    (3, "operacional", "camada-3-operacional.md"),
    (4, "granular", "camada-4-granular.md"),
    (5, "condensadora", "camada-5-condensadora.md"),
]


def load_package(day: str) -> dict[str, Any]:
    path = PACKAGE_BASE / day / "package.json"
    if not path.exists():
        raise SystemExit(f"Pacote não encontrado: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def package_accounts(package: dict[str, Any]) -> dict[str, Any]:
    return package.get("accounts") or package.get("platforms") or {}


def call_openai(prompt: str, *, model: str) -> str:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise SystemExit("OPENAI_API_KEY ausente; Camada 8 LLM bloqueada.")
    payload = json.dumps({"model": model, "input": prompt}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
    if data.get("error"):
        raise RuntimeError(data["error"])
    text = data.get("output_text")
    if text:
        return text.strip()
    chunks: list[str] = []
    for item in data.get("output", []):
        for part in item.get("content", []):
            if part.get("type") in {"output_text", "text"} and part.get("text"):
                chunks.append(part["text"])
    if not chunks:
        raise RuntimeError("OpenAI response sem texto")
    return "\n".join(chunks).strip()


def compact_account_context(account: dict[str, Any]) -> dict[str, Any]:
    metrics = account.get("metrics", {})
    historical = account.get("historical", {})
    return {
        "account_name": account.get("account_name"),
        "metrics": {
            "pedidos_validos": metrics.get("pedidos_validos"),
            "gmv": metrics.get("gmv"),
            "ticket_medio": metrics.get("ticket_medio"),
            "cancelamentos": metrics.get("cancelamentos"),
            "top3_concentration": metrics.get("top3_concentration"),
            "top_products": metrics.get("top_products", [])[:8],
        },
        "historical_changes": historical.get("changes", {}),
        "quality_flags": account.get("quality_flags", []),
        "reconciliation": account.get("reconciliation", {}),
    }


def run_account_layers(package: dict[str, Any], slug: str, label: str, day: str, model: str, force: bool) -> dict[int, str]:
    accounts = package_accounts(package)
    account = accounts[slug]
    out_dir = RUNS_BASE / day / "accounts" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    previous = ""
    outputs: dict[int, str] = {}
    context = compact_account_context(account)
    for n, name, prompt_file in LAYER_PROMPTS:
        out_path = out_dir / f"camada-{n}-{name}.md"
        if out_path.exists() and not force:
            text = out_path.read_text(encoding="utf-8")
            outputs[n] = text
            previous = text
            continue
        system_prompt = (PROMPTS / prompt_file).read_text(encoding="utf-8")
        full_prompt = f"""{system_prompt}

# Contexto da conta
Destinatário: Lucas
Conta: {label}
Data: {package['date']}

Dados validados da conta:
{json.dumps(context, ensure_ascii=False, indent=2)}

Saída da camada anterior:
{previous or 'Primeira camada — sem saída anterior.'}

Responda em português brasileiro. Seja específico, denso e auditável. Não invente dado.
"""
        text = call_openai(full_prompt, model=model)
        out_path.write_text(text + "\n", encoding="utf-8")
        outputs[n] = text
        previous = text
    return outputs


def extract_json(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("Saída da Camada 8 não contém JSON")
    return json.loads(cleaned[start:end + 1])


def run_layer8(package: dict[str, Any], condensers: dict[str, str], day: str, model: str) -> dict[str, Any]:
    accounts = package_accounts(package)
    prompt = (PROMPTS / "camada-8-shopee-consolidada.md").read_text(encoding="utf-8")
    payload = {
        "date": package["date"],
        "recipient": "Lucas",
        "platform": "Shopee",
        "objective": "síntese consolidada das 3 contas Shopee para Slack",
        "account_condensers": {
            slug: {"label": label, "slot": slot, "camada_5_condensadora": condensers[slug]}
            for slug, label, slot in SHOPEE_ACCOUNTS
        },
        "metrics_reference_only": {
            slug: compact_account_context(accounts[slug]) for slug, _, _ in SHOPEE_ACCOUNTS
        },
    }
    full_prompt = f"""{prompt}

# Input da Camada 8
{json.dumps(payload, ensure_ascii=False, indent=2)}
"""
    raw = call_openai(full_prompt, model=model)
    parsed = extract_json(raw)
    required = ["analysis_lines", "priority_lines", "memory_for_tomorrow", "qa_flags"]
    missing = [k for k in required if k not in parsed]
    if missing:
        raise ValueError(f"Camada 8 sem campos obrigatórios: {missing}")
    out_dir = RUNS_BASE / day / "lucas"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "camada-8-shopee-consolidada.raw.md").write_text(raw + "\n", encoding="utf-8")
    (out_dir / "camada-8-shopee-consolidada.json").write_text(
        json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily Sales v2 — Camada 8 Shopee LLM")
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--model", default=os.environ.get("DAILY_SALES_OPENAI_MODEL", "gpt-4.1"))
    parser.add_argument("--force", action="store_true", help="Reexecuta camadas 1-5 mesmo se artefatos já existirem")
    args = parser.parse_args()

    package = load_package(args.date)
    condensers: dict[str, str] = {}
    for slug, label, _slot in SHOPEE_ACCOUNTS:
        outputs = run_account_layers(package, slug, label, args.date, args.model, args.force)
        condensers[slug] = outputs[5]
    parsed = run_layer8(package, condensers, args.date, args.model)
    print(json.dumps({"status": "OK", "analysis_lines": len(parsed["analysis_lines"]), "priority_lines": len(parsed["priority_lines"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

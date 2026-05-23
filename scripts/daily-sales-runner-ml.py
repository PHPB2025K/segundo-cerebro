#!/usr/bin/env python3
"""
Daily Sales Analyst Runner — Phase 7.1 (LLM Hardening)

Executes Layer 0 + 7 layers sequentially, generates auditable artifacts
per date/recipient, with kill switch, rollback, and LLM integration.

Usage:
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --dry-run
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe --llm
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe --llm --recipients lucas
    python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe --llm --recipients lucas --merge-existing

Modes:
    --dry-run          Generate artifacts, no send. Standard test mode.
    --shadow           Shadow mode: generate + compare, no send.
    --preview          Preview mode: generate artifacts for review.
    --preview-to-kobe  Generate artifacts + PREVIEW_TO_KOBE.md summary. No external send.
    --send-candidate   Mark as send candidate. Blocked if config/fallback/approval prevent send.
    --production-send  Real send. Blocked unless ALL protections are satisfied.

LLM:
    --llm              Enable LLM execution for layers 1-7 (requires config or flag).

Hardening (Phase 7.1):
    --merge-existing   Merge new recipient results into existing manifest (default: true when --recipients subset).
    --timeout SECS     Override LLM timeout per layer (default: from config or 180s).

Protections:
    - send_real_allowed=false enforced when config prevents it.
    - llm_layers_enabled=false blocks any real send.
    - require_kobe_approval_for_real_send=true blocks send without approval.
    - Kill switch via enabled=false aborts immediately.
    - Contamination detection: LLM output with meta-commentary (permission requests,
      file/tool references, overwrite language) is auto-rejected and falls back.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
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
PROMPTS_BASE = Path("/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/prompts/versions")
CONTEXT_DIR = Path("/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/memory/context")
ACCOUNTS_DIR = Path("/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/memory/accounts")

VALID_MODES = {
    "dry-run": "DRY_RUN",
    "shadow": "SHADOW",
    "preview": "PREVIEW",
    "preview-to-kobe": "PREVIEW_TO_KOBE",
    "send-candidate": "SEND_CANDIDATE",
    "production-send": "PRODUCTION_SEND",
}
# ═══════════════════════════════════════════════════════════════════
# RUNNER INDEPENDENTE — MERCADO LIVRE / YASMIN
# Não compartilha estado com Shopee/Amazon. Cada plataforma tem seu próprio runner.
# Prompts: v4.0/mercado-livre/ (versão dedicada com referências explícitas ao ml_snapshot)
# ═══════════════════════════════════════════════════════════════════
ALL_RECIPIENTS = ["yasmin"]

RECIPIENT_PLATFORM = {
    "yasmin": "mercado_livre",
}

RECIPIENT_ACCOUNTS = {
    "yasmin": ["mercado-livre"],
}

# Default prompt version pra esse runner. Pode ser overridado via --prompt-version.
DEFAULT_PROMPT_VERSION = "v4.0/mercado-livre"

# ML não usa L06B (Shopee Consolidator) — ela é exclusiva do pipeline Shopee
LAYER_DEFS = [
    {"num": "01", "name": "estrategica", "prompt_file": "01-estrategica.md", "output_ext": "md"},
    {"num": "02", "name": "tatica", "prompt_file": "02-tatica.md", "output_ext": "md"},
    {"num": "03", "name": "operacional", "prompt_file": "03-operacional.md", "output_ext": "md"},
    {"num": "04", "name": "granular", "prompt_file": "04-granular.md", "output_ext": "json"},
    {"num": "05", "name": "condensadora", "prompt_file": "05-condensadora.md", "output_ext": "json"},
    {"num": "06", "name": "slack-writer", "prompt_file": "06-slack-writer.md", "output_ext": "md", "output_name": "06-slack-preview"},
    {"num": "07", "name": "qa-gate", "prompt_file": "07-qa-gate.md", "output_ext": "json", "output_name": "07-qa"},
]

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

def product_display_name(product):
    """Only use Layer 0 short commercial name for visible product labels."""
    return (
        product.get("short_product_name")
        or product.get("display_name")
        or product.get("title")
        or "Produto não identificado"
    )


def validate_layer0_product_contract(package):
    """Fail closed if Layer 0 did not provide sellable variation + short name."""
    blockers = []
    if package.get("schema_version") != "daily-sales-data-package/v1.3":
        blockers.append("Layer 0 package schema antigo; exige daily-sales-data-package/v1.3")

    for slug, account in (package.get("platforms") or {}).items():
        for idx, product in enumerate(account.get("metrics", {}).get("top_products", [])[:10], 1):
            short_name = (product.get("short_product_name") or "").strip()
            mapped = (product.get("mapped_variation_sku") or "").strip()
            status = product.get("mapping_status")
            confidence = product.get("confidence")
            if not short_name or not mapped or status in {"ambiguous", "unmapped_title_only"} or confidence == "low":
                blockers.append(
                    f"{slug} top#{idx}: identidade insegura "
                    f"(raw_sku={product.get('raw_sku')!r}, mapped={mapped!r}, "
                    f"short={short_name!r}, status={status!r}, confidence={confidence!r})"
                )
    return blockers


def recipient_data(package, recipient_name):
    """Extract recipient-specific data from package."""
    key = recipient_name.capitalize()
    return package.get("recipients", {}).get(key, {})


def accounts_data(package, recipient_name):
    """Extract account-level data for a recipient."""
    slugs = RECIPIENT_ACCOUNTS.get(recipient_name, [])
    platforms = package.get("platforms", {})
    return {s: platforms[s] for s in slugs if s in platforms}


def check_send_real_allowed(config, mode):
    """Check all protections and return (allowed, blockers)."""
    blockers = []

    if not config.get("send_real_enabled", False):
        blockers.append("send_real_enabled=false in config")

    if not config.get("llm_layers_enabled", False):
        blockers.append("llm_layers_enabled=false — fallback deterministic active, real send blocked")

    if config.get("require_kobe_approval_for_real_send", True):
        blockers.append("require_kobe_approval_for_real_send=true — no approval document found")

    return len(blockers) == 0, blockers


def read_file_safe(path):
    """Read a file, return empty string if not found."""
    try:
        with open(path) as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return ""


def read_qa_verdict(path):
    """Normalize Layer 7 QA output into manifest status fields."""
    try:
        with open(path) as f:
            qa = json.load(f)
    except Exception:
        return None

    raw = (qa.get("resultado_qa") or qa.get("verdict") or "").upper()
    blockers = qa.get("blockers") or qa.get("bloqueios") or qa.get("correcoes_obrigatorias_antes_envio") or []
    problems = qa.get("problemas_encontrados") or []
    counts = qa.get("contagem_severidade") or {}
    remarks = qa.get("remarks") or qa.get("ressalvas_memoria_interna") or qa.get("ressalvas_auditoria_nao_bloqueante") or []

    if "BLOQUE" in raw or blockers:
        status = "BLOCKED"
    elif "RESSALVA" in raw or counts.get("maiores") or counts.get("menores") or problems or remarks:
        status = "APPROVED_WITH_REMARKS"
    elif "APROV" in raw or "APPROVED" in raw:
        status = "APPROVED"
    else:
        status = None

    return {
        "status": status,
        "verdict": status or raw or "APPROVED_WITH_REMARKS",
        "blockers": blockers if isinstance(blockers, list) else [str(blockers)],
        "remarks": remarks if isinstance(remarks, list) else [str(remarks)],
        "problems": problems if isinstance(problems, list) else [str(problems)],
    }


# --- LLM Backend ---

def load_context_files():
    """Load all shared context files."""
    context = {}
    for name in ["responsaveis", "contas-shopee", "himmel", "marketplace-rules", "slack-format", "qa-standards"]:
        path = CONTEXT_DIR / f"{name}.md"
        content = read_file_safe(path)
        if content:
            context[name] = content
    return context


def load_account_memory(recipient_name):
    """Load account memory files for a recipient's accounts."""
    memory = {}
    slugs = RECIPIENT_ACCOUNTS.get(recipient_name, [])
    for slug in slugs:
        acc_dir = ACCOUNTS_DIR / slug
        if acc_dir.is_dir():
            acc_mem = {}
            for fname in ["rules.md", "weekly.md", "monthly.md"]:
                content = read_file_safe(acc_dir / fname)
                if content.strip():
                    acc_mem[fname] = content
            if acc_mem:
                memory[slug] = acc_mem
    return memory


def build_llm_input(layer_def, package, recipient_name, prompt_content,
                    context_files, account_memory, previous_outputs):
    """Build the full input prompt for an LLM layer call."""
    rec = recipient_data(package, recipient_name)
    accs = accounts_data(package, recipient_name)
    platform = RECIPIENT_PLATFORM.get(recipient_name, "unknown")

    sections = []

    # Phase 7.1: Strong technical wrapper (prepended, not part of v3.0 prompts)
    sections.append(LLM_HARDENING_WRAPPER)

    # System instruction
    sections.append("# Contexto de Execucao — Daily Sales Analyst")
    sections.append(f"Data: {package.get('date', 'N/A')}")
    sections.append(f"Recipient: {recipient_name.capitalize()}")
    sections.append(f"Plataforma: {platform}")
    sections.append(f"Data Readiness: {package.get('data_readiness', {}).get('status', 'N/A')}")
    sections.append(f"Prompt Version: v3.0")
    sections.append(f"Camada: {layer_def['num']}-{layer_def['name']}")
    sections.append("")

    # Prompt (the versioned prompt itself)
    sections.append("---")
    sections.append("# PROMPT DA CAMADA")
    sections.append(prompt_content)
    sections.append("")

    # Data package (recipient-specific subset)
    sections.append("---")
    sections.append("# DADOS — Layer 0 Data Package")
    sections.append("")
    sections.append("## Recipient Data")
    sections.append(f"```json\n{json.dumps(rec, indent=2, ensure_ascii=False)}\n```")
    sections.append("")
    sections.append("## Accounts Data")
    sections.append(f"```json\n{json.dumps(accs, indent=2, ensure_ascii=False)}\n```")
    sections.append("")
    sections.append("## Data Readiness")
    sections.append(f"```json\n{json.dumps(package.get('data_readiness', {}), indent=2, ensure_ascii=False)}\n```")
    sections.append("")

    # Context files (relevant ones)
    relevant_context = {
        "01": ["responsaveis", "marketplace-rules"],
        "02": ["responsaveis", "marketplace-rules", "contas-shopee"],
        "03": ["responsaveis", "marketplace-rules", "contas-shopee"],
        "04": ["marketplace-rules", "contas-shopee"],
        "05": ["marketplace-rules", "qa-standards"],
        "06B": ["slack-format", "responsaveis", "contas-shopee", "qa-standards"],
        "06": ["slack-format", "responsaveis", "contas-shopee", "himmel"],
        "07": ["qa-standards", "slack-format", "responsaveis", "marketplace-rules"],
    }
    ctx_keys = relevant_context.get(layer_def["num"], list(context_files.keys()))
    for key in ctx_keys:
        if key in context_files:
            sections.append(f"---")
            sections.append(f"# CONTEXTO: {key}")
            sections.append(context_files[key])
            sections.append("")

    # Account memory
    if account_memory:
        sections.append("---")
        sections.append("# MEMORIA DAS CONTAS")
        for slug, mem_files in account_memory.items():
            sections.append(f"## {slug}")
            for fname, content in mem_files.items():
                sections.append(f"### {fname}")
                sections.append(content)
                sections.append("")

    # Shopee 6B receives the three account lenses explicitly before Slack Writer.
    if layer_def["num"] == "06B" and recipient_name == "lucas":
        sections.append("---")
        sections.append("# INPUT ESPECIFICO — CONSOLIDADORA SHOPEE 6B")
        sections.append("Voce deve produzir uma sintese consolidada das 3 contas Shopee usando as camadas anteriores e os dados das tres contas abaixo.")
        sections.append("Nao trate Shopee como conta unica. Gere exatamente: consolidado + Budamix Store + Budamix Oficial + Budamix Shop.")
        sections.append(f"```json\n{json.dumps(accs, indent=2, ensure_ascii=False)}\n```")
        sections.append("")

    # Previous layer outputs
    if previous_outputs:
        sections.append("---")
        sections.append("# OUTPUTS DAS CAMADAS ANTERIORES")
        for layer_key, output in previous_outputs.items():
            sections.append(f"## {layer_key}")
            sections.append(output)
            sections.append("")

    # Output format instruction
    if layer_def["output_ext"] == "json":
        sections.append("---")
        sections.append("# INSTRUCAO DE OUTPUT")
        sections.append("Responda EXCLUSIVAMENTE com JSON valido. Nenhum texto fora do JSON.")
        sections.append("Nao use blocos de codigo markdown (```). Apenas o JSON puro.")
        sections.append("")
    elif layer_def["num"] == "06":
        sections.append("---")
        sections.append("# INSTRUCAO DE OUTPUT")
        sections.append("Responda em Markdown exatamente com os blocos pedidos pelo prompt da Slack Writer: Mensagem Slack, Respeito de bloqueios e Decisoes de formatacao.")
        sections.append("A Mensagem Slack deve estar pronta para preview, mas send_real_allowed = false. Este e apenas um preview.")
        sections.append("")

    return "\n".join(sections)


def _is_openai_model(model: str) -> bool:
    """Detecta se o nome do modelo pertence à família OpenAI (codex CLI)."""
    m = (model or "").lower()
    return (
        m.startswith("gpt-")
        or m.startswith("o3")
        or m.startswith("o4")
        or m.startswith("openai")
    )


def _call_claude(prompt_text, model, timeout):
    """Invoca claude -p (Anthropic CLI). Retorna (stdout, stderr, returncode)."""
    result = subprocess.run(
        ["claude", "-p", "--model", model, "--allowedTools", ""],
        input=prompt_text,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return result.stdout, result.stderr, result.returncode


def _call_codex(prompt_text, model, timeout):
    """Invoca codex exec (OpenAI CLI). Lê resposta de --output-last-message."""
    out_file = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    out_file.close()
    try:
        result = subprocess.run(
            [
                "codex", "exec",
                "-m", model,
                "--skip-git-repo-check",
                "--ephemeral",
                "-s", "read-only",
                "--output-last-message", out_file.name,
            ],
            input=prompt_text,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        try:
            with open(out_file.name, "r", encoding="utf-8") as f:
                stdout = f.read()
        except Exception:
            stdout = ""
        return stdout, result.stderr, result.returncode
    finally:
        try:
            os.unlink(out_file.name)
        except Exception:
            pass


def _resolve_model_for_layer(config, layer_num):
    """Resolve modelo a usar para uma camada específica.

    Lê `llm_model_per_layer` no config (dict opcional `{"04": "claude-opus-4-7", ...}`).
    Se a camada tem override, retorna ele; senão devolve `llm_model` global.
    """
    default = config.get("llm_model", "sonnet")
    overrides = config.get("llm_model_per_layer") or {}
    if not isinstance(overrides, dict):
        return default
    if layer_num and layer_num in overrides:
        return overrides[layer_num]
    return default


def _resolve_timeout_for_layer(config, layer_num):
    """Resolve timeout. Opus pode precisar de mais tempo que Sonnet."""
    default = config.get("llm_timeout_seconds", 120)
    overrides = config.get("llm_timeout_seconds_per_layer") or {}
    if isinstance(overrides, dict) and layer_num and layer_num in overrides:
        return overrides[layer_num]
    return default


def call_llm(prompt_text, config, layer_num=None):
    """Roteia para a CLI correta baseado no nome do modelo.

    - Modelos `claude-*`, `sonnet`, `opus`  → `claude -p`
    - Modelos `gpt-*`, `o3-*`, `o4-*`       → `codex exec` (OpenAI)

    `layer_num` (opcional, ex.: "04", "05") permite override de modelo
    e timeout por camada via `llm_model_per_layer` no config.

    Retorna (output, model_used, error).
    """
    model = _resolve_model_for_layer(config, layer_num)
    timeout = _resolve_timeout_for_layer(config, layer_num)
    max_retries = config.get("llm_max_retries", 2)
    use_codex = _is_openai_model(model)

    for attempt in range(1, max_retries + 1):
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
                tmp.write(prompt_text)
                tmp_path = tmp.name

            if use_codex:
                stdout, stderr, rc = _call_codex(prompt_text, model, timeout)
            else:
                stdout, stderr, rc = _call_claude(prompt_text, model, timeout)

            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass

            if rc == 0 and (stdout or "").strip():
                return stdout.strip(), model, None
            else:
                err = (stderr or "").strip() or f"returncode={rc}, empty output"
                if attempt < max_retries:
                    print(f"    LLM attempt {attempt} failed: {err}. Retrying...")
                    continue
                return None, model, err

        except subprocess.TimeoutExpired:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass
            err = f"timeout ({timeout}s)"
            if attempt < max_retries:
                print(f"    LLM attempt {attempt} timed out. Retrying...")
                continue
            return None, model, err
        except Exception as e:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass
            return None, model, str(e)

    return None, model, "max retries exceeded"


def validate_json_output(text):
    """Try to parse JSON from LLM output, handling markdown code blocks."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        start = 1
        end = len(lines)
        for i in range(len(lines) - 1, 0, -1):
            if lines[i].strip() == "```":
                end = i
                break
        cleaned = "\n".join(lines[start:end]).strip()

    try:
        parsed = json.loads(cleaned)
        return parsed, None
    except json.JSONDecodeError as e:
        return None, str(e)


def repair_json_with_llm(raw_output, json_error, config, layer_num=None):
    """Repair invalid LLM JSON with another LLM pass; never falls back deterministically."""
    prompt = f"""
Voce e um reparador estrito de JSON.

O texto abaixo deveria ser JSON valido, mas falhou com este erro:
{json_error}

Regras:
- Responda somente com JSON valido.
- Nao adicione markdown, comentarios ou texto fora do JSON.
- Preserve o conteudo e a estrutura pretendida tanto quanto possivel.
- Corrija apenas sintaxe JSON: aspas, virgulas, escapes, chaves/colchetes.

TEXTO ORIGINAL:
{raw_output}
""".strip()

    repaired_text, model_used, call_error = call_llm(prompt, config, layer_num=layer_num)
    if call_error or not repaired_text:
        return None, model_used, call_error or "empty repair output"

    parsed, repaired_error = validate_json_output(repaired_text)
    if repaired_error:
        return None, model_used, repaired_error

    return parsed, model_used, None


def validate_slack_writer_output(text, package, recipient_name):
    """Mechanical guard for Slack Writer output before QA.

    The current Layer 0 package exposes product order counts, not validated
    product-level revenue. Top Produtos must not contain R$ values or estimated
    revenue unless the package explicitly starts providing product revenue fields.
    """
    errors = []
    in_top = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("🏆 TOP PRODUTOS"):
            in_top = True
            continue
        if in_top and (line.startswith("🔍 ") or line.startswith("🎯 ") or line.startswith("Dia analisado:")):
            in_top = False
        if in_top and line.startswith("-"):
            if re.search(r"\bR\$\s*\d", line) or re.search(r"(?i)\best\.?\b|estimad", line):
                errors.append(f"Top Produtos contém faturamento/estimativa não autorizada: {line}")
    if re.search(r"(?i)foi removid[oa]", text) and re.search(r"(?i)\best\.?\b|estimad", text):
        errors.append("Log declara remoção de estimativa, mas output ainda contém referência estimada.")
    return errors


def validate_condensadora_output(parsed, recipient_name):
    """Mechanical guard for Condensadora internal contradictions.

    If the Condensadora blocks assertions about internal listing/variation structure,
    it cannot also place those same assertions in insights/priorities/memory.
    """
    errors = []
    if not isinstance(parsed, dict):
        return errors
    blocked_text = " ".join(str(x) for x in parsed.get("o_que_nao_pode_ir_para_slack", [])).lower()
    blocks_internal_listing = any(term in blocked_text for term in [
        "sem afirmar estrutura interna",
        "não afirmar estrutura interna",
        "compartilham o mesmo listing",
        "hipótese de que",
    ])
    if not blocks_internal_listing:
        return errors
    fields = [
        "analise_final_condensada",
        "prioridades_condensadas",
        "prioridades_condensadas_para_slack",
        "memoria_para_amanha",
        "alertas_de_confianca",
    ]
    public_text = " ".join(json.dumps(parsed.get(field, ""), ensure_ascii=False) for field in fields).lower()
    forbidden_patterns = [
        r"abriga\s+duas\s+cores",
        r"compartilh\w*\s+o\s+mesmo\s+listing",
        r"mesmo\s+listing",
        r"duas\s+cores\s+sob\s+o\s+mesmo\s+an[úu]ncio",
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, public_text):
            errors.append(f"Condensadora contradiz bloqueio de estrutura interna de listing: {pattern}")
    return errors


# --- Contamination Detection (Phase 7.1) ---

CONTAMINATION_PATTERNS = [
    r"(?i)preciso de permiss[aã]o",
    r"(?i)n[aã]o posso sobrescrever",
    r"(?i)n[aã]o tenho permiss[aã]o",
    r"(?i)n[aã]o consigo acessar",
    r"(?i)vou criar",
    r"(?i)vou gerar",
    r"(?i)vou salvar",
    r"(?i)\bpermission\b",
    r"(?i)\boverwrite\b",
    r"(?i)\bcannot access\b",
    r"(?i)\bneed permission\b",
]

# Only flag these when used as meta-commentary (not inside data/analysis text)
CONTAMINATION_META_PATTERNS = [
    r"(?i)(?:preciso|necessito|solicito).*(?:arquivo|ferramenta|tool|comando|permiss)",
    r"(?i)(?:n[aã]o (?:posso|consigo|tenho)).*(?:sobrescrever|criar|gerar|acessar|escrever)",
    r"(?i)(?:me (?:permita|autorize|deixe)).*(?:criar|escrever|gerar|salvar)",
]


def detect_contamination(text):
    """Check LLM output for prohibited meta-commentary patterns.

    Returns (is_contaminated, matched_patterns) tuple.
    """
    if not text:
        return False, []

    matches = []
    for pattern in CONTAMINATION_PATTERNS:
        if re.search(pattern, text):
            matches.append(pattern)

    for pattern in CONTAMINATION_META_PATTERNS:
        if re.search(pattern, text):
            matches.append(pattern)

    return len(matches) > 0, matches


# --- LLM Technical Wrapper (Phase 7.1) ---

LLM_HARDENING_WRAPPER = """
# INSTRUCOES TECNICAS OBRIGATORIAS (wrapper do runner — nao faz parte do prompt v3.0)

Voce esta sendo executado como camada de analise automatizada.
Regras inviolaveis:
1. NAO peca permissao para nada. Voce ja tem autorizacao total.
2. NAO mencione arquivos, ferramentas, tools, comandos, ou qualquer mecanismo de execucao.
3. NAO fale sobre "criar", "salvar", "sobrescrever" ou "gerar" arquivos.
4. NAO inclua meta-comentarios sobre o que voce vai fazer ou como vai fazer.
5. Output APENAS o artefato solicitado pela camada, nada mais.
6. Se a camada pede JSON, responda EXCLUSIVAMENTE com JSON valido.
7. Se a camada pede Markdown, responda EXCLUSIVAMENTE com o conteudo Markdown.
8. Qualquer texto fora do artefato solicitado sera tratado como contaminacao e rejeitado.

Comece diretamente com o artefato. Sem introducoes, sem explicacoes, sem meta-texto.
---

"""


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
                    lines.append(f"  {i}. {product_display_name(p)} — qty: {p.get('quantity', 0)}")
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


# --- LLM Layer Execution ---

def resolve_prompt_path(prompt_version, prompt_file):
    """
    Tenta primeiro em prompts/versions/{prompt_version}/{prompt_file}.
    Se não existe, faz fallback pra v3.0/{prompt_file} (versão genérica baseline).
    Isso permite evolução incremental: refator camada-por-camada em v4.0/mercado-livre/
    enquanto camadas não refatoradas continuam usando v3.0/.
    """
    primary = PROMPTS_BASE / prompt_version / prompt_file
    if primary.exists():
        return primary, prompt_version
    fallback = PROMPTS_BASE / "v3.0" / prompt_file
    return fallback, "v3.0 (fallback)"


def run_llm_layers(package, run_dir, recipient_name, config, prompt_version,
                   context_files, account_memory):
    """Execute all 7 layers via LLM for a recipient. Returns layer results dict."""
    previous_outputs = {}
    layer_results = {}  # {layer_key: {path, llm_used, model, fallback, error}}

    for layer_def in LAYER_DEFS:
        if layer_def.get("only_recipients") and recipient_name not in layer_def["only_recipients"]:
            continue

        layer_num = layer_def["num"]
        layer_name = layer_def["name"]
        output_name = layer_def.get("output_name", f"{layer_num}-{layer_name}")
        output_ext = layer_def["output_ext"]
        output_file = f"{output_name}.{output_ext}"
        output_path = run_dir / recipient_name / output_file

        print(f"    Layer {layer_num} ({layer_name}): ", end="", flush=True)

        # Load prompt — com fallback v3.0 pra camadas ainda não refatoradas
        prompt_path, prompt_source = resolve_prompt_path(prompt_version, layer_def["prompt_file"])
        prompt_content = read_file_safe(prompt_path)
        if not prompt_content:
            print(f"SKIP (prompt not found: {prompt_path})")
            layer_results[output_name] = {
                "path": str(output_path),
                "llm_used": False,
                "model": None,
                "fallback": True,
                "error": f"Prompt file not found: {prompt_path}",
            }
            continue

        # Build input
        llm_input = build_llm_input(
            layer_def, package, recipient_name, prompt_content,
            context_files, account_memory, previous_outputs
        )

        # Persist EXACT input sent to LLM (pra Mission Control mostrar em tempo real)
        input_path = output_path.with_suffix(output_path.suffix + ".input.txt") \
            if not str(output_path).endswith(".input.txt") else output_path
        # Mais simples: salva como {output_basename}.input.txt
        input_persist_path = output_path.parent / f"{layer_num}-{layer_name}.input.txt"
        try:
            with open(input_persist_path, "w", encoding="utf-8") as f:
                f.write(llm_input)
        except Exception as e:
            print(f"    ⚠ falha ao persistir input: {e}")

        # Call LLM (passa layer_num pra permitir override de modelo via config.llm_model_per_layer)
        output, model_used, error = call_llm(llm_input, config, layer_num=layer_num)

        if error or not output:
            print(f"FALLBACK (error: {error})")
            layer_results[output_name] = {
                "path": str(output_path),
                "llm_used": False,
                "model": model_used,
                "fallback": True,
                "error": error,
            }
            # Store empty previous output so next layers know
            previous_outputs[output_name] = f"[FALLBACK - camada {layer_num} usou fallback deterministico]"
            continue

        # Phase 7.1: Contamination detection
        is_contaminated, contamination_matches = detect_contamination(output)
        if is_contaminated:
            contam_err = f"CONTAMINATED: output contains prohibited meta-commentary ({len(contamination_matches)} patterns matched)"
            print(f"FALLBACK ({contam_err})")
            layer_results[output_name] = {
                "path": str(output_path),
                "llm_used": False,
                "model": model_used,
                "fallback": True,
                "error": contam_err,
            }
            previous_outputs[output_name] = f"[FALLBACK - camada {layer_num} contaminada, usou fallback deterministico]"
            continue

        # Validate JSON layers
        if output_ext == "json":
            parsed, json_err = validate_json_output(output)
            repaired_by_llm = False
            if json_err:
                print(f"REPAIR_JSON (invalid JSON: {json_err})", end=" ", flush=True)
                repaired, repair_model, repair_err = repair_json_with_llm(output, json_err, config, layer_num=layer_num)
                if repair_err:
                    print(f"FALLBACK (repair failed: {repair_err})")
                    layer_results[output_name] = {
                        "path": str(output_path),
                        "llm_used": False,
                        "model": model_used,
                        "fallback": True,
                        "error": f"Invalid JSON from LLM: {json_err}; repair failed: {repair_err}",
                    }
                    previous_outputs[output_name] = f"[FALLBACK - JSON invalido na camada {layer_num}]"
                    continue
                parsed = repaired
                repaired_by_llm = True
                print(f"OK (repair={repair_model})")

            if output_name == "05-condensadora":
                condensadora_errors = validate_condensadora_output(parsed, recipient_name)
                if condensadora_errors:
                    err = "; ".join(condensadora_errors[:3])
                    print(f"FALLBACK (condensadora guard: {err})")
                    layer_results[output_name] = {
                        "path": str(output_path),
                        "llm_used": False,
                        "model": model_used,
                        "fallback": True,
                        "error": f"Condensadora guard failed: {err}",
                    }
                    previous_outputs[output_name] = f"[FALLBACK - Condensadora contradisse bloqueios: {err}]"
                    continue

            # Enrich JSON with metadata
            if isinstance(parsed, dict):
                parsed["llm_used"] = True
                parsed["model"] = model_used
                parsed["fallback"] = False
                if repaired_by_llm:
                    parsed["json_repaired"] = True

            with open(output_path, "w") as f:
                json.dump(parsed, f, indent=2, ensure_ascii=False)

            previous_outputs[output_name] = json.dumps(parsed, indent=2, ensure_ascii=False)
        else:
            if output_name == "06-slack-preview":
                slack_errors = validate_slack_writer_output(output, package, recipient_name)
                if slack_errors:
                    err = "; ".join(slack_errors[:3])
                    print(f"FALLBACK (slack writer guard: {err})")
                    layer_results[output_name] = {
                        "path": str(output_path),
                        "llm_used": False,
                        "model": model_used,
                        "fallback": True,
                        "error": f"Slack Writer guard failed: {err}",
                    }
                    previous_outputs[output_name] = f"[FALLBACK - Slack Writer violou contrato: {err}]"
                    continue

            # Markdown layers — add metadata header
            header = f"<!-- llm_used=true model={model_used} fallback=false -->\n"
            full_output = header + output
            with open(output_path, "w") as f:
                f.write(full_output)

            previous_outputs[output_name] = output

        print(f"OK (llm={model_used})")
        layer_results[output_name] = {
            "path": str(output_path),
            "llm_used": True,
            "model": model_used,
            "fallback": False,
            "error": None,
        }

    return layer_results


# --- Preview to Kobe ---

def gen_preview_to_kobe(date_str, run_dir, config, recipient_results, manifest):
    """Generate PREVIEW_TO_KOBE.md consolidating all recipients."""
    path = run_dir / "PREVIEW_TO_KOBE.md"
    send_allowed, send_blockers = check_send_real_allowed(config, "preview-to-kobe")

    lines = [
        f"# Preview para Kobe — {date_str}",
        f"**Gerado em:** {now_utc()}",
        f"**Modo:** PREVIEW_TO_KOBE",
        f"**send_real_allowed:** false",
        f"**Global Status:** {manifest['global_status']}",
        f"**Prompt Version:** {manifest['prompt_version']}",
        f"**Data Builder Version:** {manifest['data_builder_version']}",
        f"**LLM Used:** {manifest['runner_meta']['llm_used']}",
        "",
        "## Protecoes Ativas",
    ]

    for b in send_blockers:
        lines.append(f"- {b}")
    lines.append("")

    lines.append("## Resumo por Recipient")
    lines.append("")

    for r_name, r_data in recipient_results.items():
        lines.append(f"### {r_name.capitalize()} ({r_data['platform']})")
        lines.append(f"- **Status:** {r_data['status']}")
        lines.append(f"- **send_allowed:** {r_data['send_allowed']}")
        lines.append(f"- **llm_used:** {r_data.get('llm_used', False)}")
        if r_data.get("llm_layers_detail"):
            for lk, ld in r_data["llm_layers_detail"].items():
                status = "LLM" if ld.get("llm_used") else "FALLBACK"
                lines.append(f"  - {lk}: {status}")
        if r_data.get("warnings"):
            for w in r_data["warnings"]:
                lines.append(f"- **Aviso:** {w}")
        lines.append("")
        lines.append("**Artefatos:**")
        for layer_name, layer_path in r_data.get("layers", {}).items():
            lines.append(f"  - `{layer_name}`: `{layer_path}`")
        lines.append("")

    lines.extend([
        "## Acao Requerida",
        "",
        "Kobe/Pedro: revisar artefatos acima e decidir:",
        "- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate",
        "- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar",
        "",
        "---",
        "*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*",
    ])

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return str(path)


# --- Main Runner ---

def run(date_str, mode, recipients, config, package_path=None,
        prompt_version=None, use_llm=False, merge_existing=False,
        timeout_override=None):
    print(f"=== Daily Sales Analyst Runner (Phase 7.1 — LLM Hardening) ===")
    print(f"Date: {date_str} | Mode: {mode} | LLM: {use_llm} | Merge: {merge_existing}")
    print(f"Recipients: {', '.join(recipients)}")
    print()

    # --- Kill Switch ---
    if not config.get("enabled", False):
        print("ABORT: Config enabled=false. Pipeline disabled (kill switch).")
        sys.exit(1)

    if not config.get("layer0_required", True):
        print("ABORT: layer0_required=false inconsistent with pipeline requirements.")
        sys.exit(1)

    # --- LLM eligibility ---
    llm_active = False
    if use_llm:
        if config.get("llm_layers_enabled", False):
            llm_active = True
            print("LLM: Enabled via config llm_layers_enabled=true")
        elif config.get("allow_llm_in_shadow", False):
            llm_active = True
            print("LLM: Enabled via allow_llm_in_shadow=true (shadow/test mode)")
        else:
            print("WARNING: --llm flag passed but neither llm_layers_enabled nor allow_llm_in_shadow is true.")
            print("         Falling back to deterministic mode.")

    # --- Send real protection check ---
    send_real_allowed, send_blockers = check_send_real_allowed(config, mode)

    if mode in ("send-candidate", "production-send"):
        print("=== Send Protection Check ===")
        if not send_real_allowed:
            print("BLOCKED: Real send is NOT allowed. Reasons:")
            for b in send_blockers:
                print(f"  - {b}")
            print()
            if mode == "production-send":
                print("ABORT: --production-send blocked by protections.")
                print("No artifacts generated. No external send attempted.")
                print("Resolve blockers above before attempting production send.")
                sys.exit(2)
            else:
                print("INFO: --send-candidate will generate artifacts but mark send as BLOCKED.")
                print()

    # --- Preview to Kobe check ---
    if mode == "preview-to-kobe" and not config.get("preview_to_kobe_enabled", True):
        print("ABORT: preview_to_kobe_enabled=false in config.")
        sys.exit(1)

    pv = prompt_version or config.get("pinned_prompt_version") or config.get("prompt_version", "v3.0")
    dbv = config.get("data_builder_version", "v1.0")

    # Handle rollback versions
    if config.get("rollback_to_version"):
        pv = config["rollback_to_version"]
        print(f"ROLLBACK: Using prompt version {pv} (rollback active)")
    if config.get("rollback_data_builder_version"):
        dbv = config["rollback_data_builder_version"]
        print(f"ROLLBACK: Using data builder version {dbv} (rollback active)")

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

    contract_blockers = validate_layer0_product_contract(package)
    if contract_blockers:
        print("Layer 0 product contract: FAIL")
        for b in contract_blockers[:10]:
            print(f"  FAIL: {b}")
    else:
        print("Layer 0 product contract: OK")

    is_blocked = dr_status == "NOT_READY" or bool(contract_blockers)
    block_reason = ""
    if is_blocked:
        reasons = [f"{fc['check']}: {fc.get('detail', '')}" for fc in failed_checks]
        if contract_blockers:
            reasons.extend([f"product_identity_contract: {b}" for b in contract_blockers[:10]])
        block_reason = f"Layer 0/Data Readiness blocked. Checks failed: {'; '.join(reasons)}"
        print(f"\nPipeline BLOCKED: {block_reason}\n")
    print()

    # Phase 7.1: Apply timeout override
    if timeout_override is not None:
        config = dict(config)  # shallow copy to avoid mutating original
        config["llm_timeout_seconds"] = timeout_override
        print(f"Timeout override: {timeout_override}s")

    # Load context and memory (for LLM mode)
    context_files = {}
    if llm_active:
        context_files = load_context_files()
        print(f"Context files loaded: {list(context_files.keys())}")

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
    any_llm_used = False

    for r in active_recipients:
        print(f"\n--- Processing: {r} ---")
        paths = {}

        paths["00-data-package"] = gen_layer00_data_package(package, run_dir, r)

        recipient_llm_used = False
        llm_layers_detail = {}
        llm_strict_failure = False
        llm_strict_blockers = []

        if llm_active and not is_blocked:
            # LLM execution path
            print(f"  LLM mode: executing 7 layers via LLM...")
            account_memory = load_account_memory(r)
            llm_results = run_llm_layers(
                package, run_dir, r, config, pv,
                context_files, account_memory
            )

            # Map results to paths
            fallback_layers = []
            for layer_def in LAYER_DEFS:
                if layer_def.get("only_recipients") and r not in layer_def["only_recipients"]:
                    continue
                output_name = layer_def.get("output_name", f"{layer_def['num']}-{layer_def['name']}")
                lr = llm_results.get(output_name, {})
                paths[output_name] = lr.get("path", "")
                llm_layers_detail[output_name] = lr
                if lr.get("llm_used"):
                    recipient_llm_used = True
                    any_llm_used = True
                elif lr.get("fallback"):
                    fallback_layers.append(output_name)

            if fallback_layers:
                print(f"  Fallback layers: {', '.join(fallback_layers)}")
                if not config.get("fallback_deterministic_allowed", True):
                    llm_strict_failure = True
                    llm_strict_blockers = [
                        f"LLM layer failed and deterministic fallback is disabled: {', '.join(fallback_layers)}"
                    ]
                    print("  BLOCKED: deterministic fallback disabled; recipient not approved.")
                else:
                    # Generate fallback for layers that failed LLM
                    for layer_def in LAYER_DEFS:
                        if layer_def.get("only_recipients") and r not in layer_def["only_recipients"]:
                            continue
                        output_name = layer_def.get("output_name", f"{layer_def['num']}-{layer_def['name']}")
                        lr = llm_results.get(output_name, {})
                        if lr.get("fallback") and not Path(lr.get("path", "")).exists():
                            # Generate deterministic fallback
                            if layer_def["num"] == "01":
                                paths["01-estrategica"] = gen_layer01_estrategica(package, run_dir, r, False, "")
                            elif layer_def["num"] == "02":
                                paths["02-tatica"] = gen_layer02_tatica(package, run_dir, r, False, "")
                            elif layer_def["num"] == "03":
                                paths["03-operacional"] = gen_layer03_operacional(package, run_dir, r, False, "")
                            elif layer_def["num"] == "04":
                                paths["04-granular"] = gen_layer04_granular(package, run_dir, r, False, "")
                            elif layer_def["num"] == "05":
                                paths["05-condensadora"] = gen_layer05_condensadora(package, run_dir, r, False, "")
                            elif layer_def["num"] == "06":
                                paths["06-slack-preview"] = gen_layer06_slack_preview(package, run_dir, r, False, "")
                            elif layer_def["num"] == "07":
                                paths["07-qa"] = gen_layer07_qa(package, run_dir, r, False, "", dr_status)

        else:
            # Deterministic fallback path
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
        elif llm_strict_failure:
            status = "BLOCKED"
            qa_verdict = "BLOCKED"
            blockers = llm_strict_blockers
            warnings = ["LLM obrigatório: fallback determinístico não é caminho aprovado."]
        else:
            qa_summary = read_qa_verdict(paths.get("07-qa", ""))
            if qa_summary and qa_summary.get("status"):
                status = qa_summary["status"]
                qa_verdict = qa_summary["verdict"]
                blockers = qa_summary.get("blockers", [])
                warnings = qa_summary.get("remarks", [])
                if status == "APPROVED_WITH_REMARKS" and not warnings:
                    warnings = qa_summary.get("problems", []) or ["QA aprovou com ressalvas; revisar artefato 07-qa.json."]
            else:
                status = "APPROVED_WITH_REMARKS"
                qa_verdict = "APPROVED_WITH_REMARKS"
                blockers = []
                if recipient_llm_used:
                    warnings = ["Analise LLM executada. Verificar artefatos para qualidade."]
                else:
                    warnings = ["Fallback deterministico: sem analise LLM profunda."]

        recipient_results[r] = {
            "platform": RECIPIENT_PLATFORM.get(r, "unknown"),
            "status": status,
            "send_allowed": False,
            "slack_payload": None,
            "llm_used": recipient_llm_used,
            "llm_layers_detail": llm_layers_detail,
            "layers": {
                "layer0_data_package": paths.get("00-data-package", ""),
                "layer1_estrategica": paths.get("01-estrategica", ""),
                "layer2_tatica": paths.get("02-tatica", ""),
                "layer3_operacional": paths.get("03-operacional", ""),
                "layer4_granular": paths.get("04-granular", ""),
                "layer5_condensadora": paths.get("05-condensadora", ""),
                "layer6b_shopee_consolidator": paths.get("06b-shopee-consolidator", ""),
                "layer6_slack_writer": paths.get("06-slack-preview", ""),
                "layer7_qa_gate": paths.get("07-qa", ""),
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
        llm_label = " (LLM)" if recipient_llm_used else " (fallback)"
        print(f"  Status: {status} | Artifacts: {len(paths)} files{llm_label}")

    # Global status
    statuses = [r["status"] for r in recipient_results.values()]
    if all(s == "BLOCKED" for s in statuses):
        global_status = "BLOCKED"
    elif all(s in ("APPROVED", "APPROVED_WITH_REMARKS") for s in statuses):
        global_status = "APPROVED_WITH_REMARKS" if "APPROVED_WITH_REMARKS" in statuses else "APPROVED"
    else:
        global_status = "PARTIAL"

    global_failure = "layer0" if is_blocked else False

    # Phase 7.1: Auto-enable merge when running subset of recipients
    is_subset = set(active_recipients) != set(ALL_RECIPIENTS)
    should_merge = merge_existing or is_subset
    existing_manifest = None
    if should_merge:
        existing_manifest_path = run_dir / "manifest.json"
        if existing_manifest_path.exists():
            try:
                with open(existing_manifest_path) as f:
                    existing_manifest = json.load(f)
                print(f"\nMerge mode: loaded existing manifest with {len(existing_manifest.get('recipients', {}))} recipients")
            except (json.JSONDecodeError, KeyError) as e:
                print(f"WARNING: Could not load existing manifest for merge: {e}")
                existing_manifest = None

    # Build manifest
    manifest = {
        "schema_version": "daily-sales-analyst-run/v3.0",
        "date": date_str,
        "generated_at_utc": now_utc(),
        "mode": VALID_MODES.get(mode, mode.upper()),
        "send_real_allowed": False,
        "send_real_blockers": send_blockers,
        "global_status": global_status,
        "global_failure": global_failure,
        "prompt_version": pv,
        "data_builder_version": dbv,
        "package_path": pkg_path,
        "config_snapshot": {
            "enabled": config.get("enabled"),
            "send_real_enabled": config.get("send_real_enabled"),
            "llm_layers_enabled": config.get("llm_layers_enabled"),
            "allow_llm_in_shadow": config.get("allow_llm_in_shadow"),
            "llm_model": config.get("llm_model"),
            "fallback_deterministic_allowed": config.get("fallback_deterministic_allowed"),
            "require_kobe_approval_for_real_send": config.get("require_kobe_approval_for_real_send"),
            "preview_to_kobe_enabled": config.get("preview_to_kobe_enabled"),
        },
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
            "phase": 7,
            "fallback_mode": not any_llm_used,
            "llm_used": any_llm_used,
            "llm_flag_passed": use_llm,
            "llm_active": llm_active,
            "llm_model": config.get("llm_model", "sonnet"),
            "limitations": [
                "send_real_allowed=false enforced.",
            ] + (
                ["Camadas executadas via LLM com fallback deterministico quando necessario."]
                if any_llm_used else
                [
                    "Runner deterministico: sem chamadas LLM.",
                    "Camadas 1-6 sao placeholders baseados no data package.",
                    "QA reflete limitacao do fallback.",
                ]
            ),
        },
    }

    # Phase 7.1: Merge with existing manifest
    if existing_manifest and should_merge:
        # Preserve recipients from existing manifest that we didn't re-run
        for r_name, r_data in existing_manifest.get("recipients", {}).items():
            if r_name not in recipient_results:
                recipient_results[r_name] = r_data
                artifact_paths[r_name] = existing_manifest.get("audit_refs", {}).get("layer_artifacts", {}).get(r_name, {})
                print(f"  Merged existing recipient: {r_name}")

        # Recalculate global status after merge
        manifest["recipients"] = recipient_results
        manifest["audit_refs"]["layer_artifacts"] = artifact_paths
        statuses = [r["status"] for r in recipient_results.values()]
        if all(s == "BLOCKED" for s in statuses):
            manifest["global_status"] = "BLOCKED"
        elif all(s in ("APPROVED", "APPROVED_WITH_REMARKS") for s in statuses):
            manifest["global_status"] = "APPROVED_WITH_REMARKS" if "APPROVED_WITH_REMARKS" in statuses else "APPROVED"
        else:
            manifest["global_status"] = "PARTIAL"
        global_status = manifest["global_status"]

    manifest_path = run_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Generate PREVIEW_TO_KOBE.md if mode is preview-to-kobe
    preview_path = None
    if mode == "preview-to-kobe":
        preview_path = gen_preview_to_kobe(date_str, run_dir, config, recipient_results, manifest)
        print(f"\nPREVIEW_TO_KOBE.md generated: {preview_path}")

    print(f"\n=== Run Complete ===")
    print(f"Mode: {mode}")
    print(f"LLM Used: {any_llm_used}")
    print(f"Global Status: {global_status}")
    print(f"Global Failure: {global_failure}")
    print(f"send_real_allowed: False")
    print(f"Recipients in manifest: {list(recipient_results.keys())} ({len(recipient_results)}/{len(ALL_RECIPIENTS)})")
    if send_blockers:
        print(f"Send blockers: {len(send_blockers)}")
        for b in send_blockers:
            print(f"  - {b}")
    print(f"Manifest: {manifest_path}")
    print(f"Run Dir: {run_dir}")
    for r_name in sorted(recipient_results.keys()):
        llm_label = " (LLM)" if recipient_results[r_name].get("llm_used") else " (fallback)"
        print(f"  {r_name}: {recipient_results[r_name]['status']}{llm_label}")
    if preview_path:
        print(f"Preview: {preview_path}")

    return manifest


def main():
    parser = argparse.ArgumentParser(
        description="Daily Sales Analyst Runner — Pipeline MERCADO LIVRE (Yasmin)"
    )
    parser.add_argument("date", help="Date to analyze (YYYY-MM-DD)")

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--dry-run", action="store_const", const="dry-run", dest="mode")
    mode_group.add_argument("--shadow", action="store_const", const="shadow", dest="mode")
    mode_group.add_argument("--preview", action="store_const", const="preview", dest="mode")
    mode_group.add_argument("--preview-to-kobe", action="store_const", const="preview-to-kobe", dest="mode")
    mode_group.add_argument("--send-candidate", action="store_const", const="send-candidate", dest="mode")
    mode_group.add_argument("--production-send", action="store_const", const="production-send", dest="mode")

    parser.add_argument("--llm", action="store_true", default=False,
                        help="Enable LLM execution for layers 1-7")
    parser.add_argument("--recipients", type=str, default=None,
                        help="Comma-separated recipients (default: all)")
    parser.add_argument("--prompt-version", type=str, default=DEFAULT_PROMPT_VERSION,
                        help=f"Prompt version (default: {DEFAULT_PROMPT_VERSION})")
    parser.add_argument("--package", type=str, default=None,
                        help="Path to data package JSON")
    parser.add_argument("--merge-existing", action="store_true", default=False,
                        help="Merge new results into existing manifest (default: auto when --recipients subset)")
    parser.add_argument("--timeout", type=int, default=None,
                        help="Override LLM timeout per layer in seconds")

    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"FATAL: Invalid date format: {args.date}. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # Runner ML é hardcoded pra yasmin. Mantemos --recipients pra retrocompat,
    # mas qualquer valor diferente de "yasmin" é rejeitado.
    if args.recipients:
        recipients = [r.strip().lower() for r in args.recipients.split(",")]
        if recipients != ["yasmin"]:
            print(f"FATAL: Este runner é exclusivo do ML/Yasmin. Recipients válidos: ['yasmin']. Recebido: {recipients}", file=sys.stderr)
            sys.exit(1)
    else:
        recipients = ["yasmin"]

    config = load_config()

    # Enforce send_real_allowed=false
    if config.get("send_real_enabled", False):
        print("WARNING: Config has send_real_enabled=true — Phase 7 protections will still enforce checks.")

    manifest = run(args.date, args.mode, recipients, config,
                   package_path=args.package, prompt_version=args.prompt_version,
                   use_llm=args.llm, merge_existing=args.merge_existing,
                   timeout_override=args.timeout)

    # Final safety assertion
    assert manifest["send_real_allowed"] is False, "CRITICAL: send_real_allowed must be false!"


if __name__ == "__main__":
    main()

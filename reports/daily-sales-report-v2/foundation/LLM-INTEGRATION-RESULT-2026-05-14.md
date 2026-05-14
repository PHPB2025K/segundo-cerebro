# LLM Integration Result — Daily Sales Analyst — 2026-05-14

## O que foi implementado

Integração LLM profunda das camadas 1–7 no runner do Daily Sales Analyst (Phase 7), usando os prompts definitivos v3.0 versionados.

### Alterações:

1. **`scripts/daily-sales-analyst-runner.py`** — Reescrito de Phase 6 para Phase 7:
   - Flag `--llm` para ativar execução LLM por camada
   - Backend LLM via `claude -p --model sonnet` (CLI disponível no ambiente)
   - Construção de input completo por camada: prompt v3.0 + data package + contexto + memória de contas + outputs anteriores
   - Validação de JSON para camadas 04, 05, 07
   - Fallback determinístico automático quando LLM falha (timeout, erro, JSON inválido)
   - Metadata em cada artefato: `llm_used`, `model`, `fallback`
   - Manifest v3.0 com detalhamento por camada LLM/fallback
   - PREVIEW_TO_KOBE.md com status LLM por recipient/camada

2. **`shared/daily-sales-analyst/config/daily-sales-analyst.json`** — Novos campos:
   - `allow_llm_in_shadow`: true (permite LLM em modo teste sem ativar `llm_layers_enabled`)
   - `llm_model`: "sonnet"
   - `llm_timeout_seconds`: 180
   - `llm_max_retries`: 2

### Proteções mantidas:
- `send_real_enabled=false` — inalterado
- `llm_layers_enabled=false` — inalterado (LLM ativado apenas via `allow_llm_in_shadow` + flag `--llm`)
- `require_kobe_approval_for_real_send=true` — inalterado
- Nenhum cron alterado
- Nenhuma API Slack/Telegram chamada

## Backend LLM

- **Ferramenta:** `claude -p --model sonnet --allowedTools ""`
- **Execução:** Subprocess Python, sem acesso a ferramentas (tools desabilitadas via `--allowedTools ""`)
- **Sem credenciais expostas:** O runner não manuseia API keys diretamente; o CLI gerencia auth
- **Timeout:** 180s por camada, 2 retries
- **Fallback:** Determinístico automático em caso de falha

## Arquivos alterados

| Arquivo | Tipo de alteração |
|---------|-------------------|
| `scripts/daily-sales-analyst-runner.py` | Reescrito (Phase 6 → Phase 7, +LLM) |
| `shared/daily-sales-analyst/config/daily-sales-analyst.json` | Campos adicionados |

## Comandos de teste

```bash
# Sem LLM (fallback determinístico, como antes)
python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe

# Com LLM (layers 1-7 via Claude Sonnet)
python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe --llm

# Com LLM, recipient específico
python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --preview-to-kobe --llm --recipients lucas

# Dry-run com LLM
python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --dry-run --llm
```

## Status por recipient (2026-05-13)

| Recipient | Plataforma | LLM Layers OK | Fallback Layers | Status |
|-----------|-----------|---------------|-----------------|--------|
| Lucas | Shopee | 01,02,03,05,06 (5/7) | 04,07 (timeout 120s) | APPROVED_WITH_REMARKS |
| Yasmin | Mercado Livre | 01,02,03,04,05,06 (6/7) | 07 (timeout 180s) | APPROVED_WITH_REMARKS |
| Leonardo | Amazon | 01,02,03,04,05,06,07 (7/7) | nenhum | APPROVED_WITH_REMARKS |

**Nota:** Lucas rodou com timeout de 120s (primeiro teste), depois aumentado para 180s. Yasmin e Leonardo rodaram com 180s.

## Qualidade observada

### Pontos positivos:
- **Camada Estratégica (01):** Análise temporal profunda, identifica tendências de 7/30/60d, classifica estado da conta (não apenas "como foi ontem")
- **Camada Tática (02):** Mapeia decisões concretas, conecta com responsáveis corretos
- **Camada Operacional (03):** Ray-X detalhado de produtos, concentração, fulfillment
- **Camada Granular (04):** Investigação forense com nível de confiança por achado
- **Camada Condensadora (05):** Filtragem editorial eficaz, descarta ruído, mantém insights acionáveis
- **Camada Slack Writer (06):** Mensagem estruturada conforme template obrigatório, com seções corretas
- **Camada QA Gate (07):** Validação rigorosa com gates e severidades

### Pontos de atenção:
- Camada 07 (QA Gate) tende a timeout por produzir output JSON longo com 11 gates
- Camada 04 (Granular) pode timeout quando o prompt + dados + outputs anteriores excedem contexto grande
- Memória de contas (weekly/monthly) está vazia — LLM opera sem histórico qualitativo acumulado

## Limitações

1. **Timeout em camadas pesadas:** Camadas 04 e 07 podem exceder 180s dependendo da complexidade
2. **Memória de contas vazia:** As análises são feitas sem histórico qualitativo acumulado (rules.md, weekly.md, monthly.md estão com templates vazios)
3. **LLM via CLI:** Cada camada inicia um novo processo `claude`, sem session state entre camadas (outputs são passados via texto)
4. **Custo:** 7 camadas × 3 recipients = 21 chamadas LLM por execução diária
5. **`llm_layers_enabled` permanece false:** LLM só funciona com flag `--llm` + `allow_llm_in_shadow=true`

## Confirmação de segurança

- [x] `send_real_allowed=false` em todos os artefatos e manifests
- [x] `send_real_enabled=false` no config — inalterado
- [x] Nenhuma API Slack chamada
- [x] Nenhuma API Telegram chamada
- [x] Nenhum cron alterado
- [x] Nenhum token/credencial exposto no código ou artefatos
- [x] JSON válido em todas as camadas 04, 05, 07
- [x] Preview local criado (PREVIEW_TO_KOBE.md)
- [x] Fallback determinístico funcional quando LLM desabilitado ou falha

## Recomendação de checkpoint Kobe

**APROVADO_COM_RESSALVA**

Ressalvas:
1. Camada 07 (QA Gate) precisa de timeout maior ou otimização de prompt para consistência
2. Memória de contas precisa ser populada para análises mais ricas
3. Recomendado rodar 3-5 dias em shadow mode antes de considerar `llm_layers_enabled=true`
4. Lucas precisa re-rodar com timeout de 180s para cobrir camadas 04 e 07 via LLM

---
*Gerado em 2026-05-14. Nenhum envio externo realizado.*

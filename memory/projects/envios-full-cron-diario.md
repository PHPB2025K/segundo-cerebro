---
title: "Cron Diário ENVIOS FULL — Baixa Automática de Estoque"
created: 2026-05-29
type: project-spec
status: producao
project: estoque-gb-fase2
tags:
  - estoque
  - cron
  - envios-full
  - automacao
  - producao
---

# Cron Diário ENVIOS FULL — Baixa Automática

> Implementado e ativo desde 29/05/2026.

## Resumo executivo

Todo dia às **06h BRT (09 UTC)** o sistema:

1. Baixa o XLSX oficial `1zfll5bvkIUqY56y0YcJ-ZP1GoMupcj_f` do Drive via `gog drive download`
2. Faz parse das 5 abas (FBA AMAZON, FULL ML, FULL SHOPEE 1/2/3) com regras corrigidas do `lib/envios-full.ts`
3. Identifica shipments NOVOS via `envios_full_baseline_shipments` (917 shipments pré-existentes ignorados)
4. Envia eventos novos em batches de 50 para `/api/stock-movements/ingest-safe-outbound` com `apply=true`
5. Marca shipments processados na baseline (não reaparecem em runs futuros)
6. Registra run completo em `envios_full_cron_runs` (auditoria)
7. Envia relatório ao Telegram tópico Estoque (`thread 11932`)

## Arquivos / Localizações

| Item | Path |
|---|---|
| Script | `/var/www/mission-control/scripts/envios-full-daily-cron.py` |
| Log | `/var/www/mission-control/data/envios-full-daily-cron.log` |
| Lockfile | `/var/run/envios-full-daily-cron.lock` (fcntl LOCK_EX non-blocking) |
| Cron entry | `0 9 * * *` no root crontab |
| XLSX cache | `/tmp/envios-full-cron.xlsx` |

## Tabelas Supabase

| Tabela | Função |
|---|---|
| `envios_full_baseline_shipments` | (sheet, shipment_id) UNIQUE — shipments que NÃO devem ser processados. Populado em 29/05 com 917 shipments existentes na planilha; cron adiciona novos após processá-los. |
| `envios_full_cron_runs` | Auditoria histórica por run: shipments_detected, events_sent, applied, divergent, errored, elapsed_seconds, shipments_processed (jsonb) |

## Como o cron decide o que processar

**Filtro:** `shipments_no_xlsx EXCEPT baseline_shipments`

Resultado: só processa shipments **criados após a primeira ativação do cron**. Não toca em histórico.

Exceção: se um shipment ficar com status BLOCKED (cancelado/finalizado) ou status não-mapeado, o cron NÃO aplica baixa, mas marca como "processed" na baseline (não tenta de novo). Esses casos viram divergentes auditáveis.

## Idempotência em camadas

1. **Lockfile fcntl** — duas instâncias simultâneas não rodam
2. **Baseline tabela** — shipments processados pulam no run seguinte
3. **`external_event_id` UNIQUE** em `stock_movements` — motor TS descarta duplicatas mesmo se um evento bater 2x

## Telegram

- Chat: Kobe Hub `-1003730816228`
- Tópico: **Estoque** (thread `11932`)
- Mensagem padrão: shipments novos detectados / aplicados / divergentes / erros + envios processados + top SKUs divergentes
- Se 0 envios novos: mensagem curta "Sem envios novos hoje ✅"

## Variáveis de ambiente / config

Tudo lido de `/var/www/mission-control/.env.local`:
- `SUPABASE_SERVICE_ROLE_KEY`
- Token Telegram via `/root/.openclaw/openclaw.json` → `channels.telegram.botToken`
- `GOG_KEYRING_PASSWORD` via `/root/.openclaw/.gog-keyring-pass`

Sobrescrita opcional via env:
- `CRON_BATCH_SIZE` (default 50)
- `CRON_HTTP_TIMEOUT` (default 180s)
- `CRON_TG_TOPIC_ID` (default 11932)

## Smoke test em produção

29/05/2026 13:46 BRT — primeira execução real:
- 3200 eventos parseados / 40 skipped (bloqueados/desconhecidos)
- 917 shipments na baseline
- 0 envios novos a processar (baseline acabou de ser criada com tudo do XLSX atual)
- Concluído em 4.2s
- Telegram enviado OK

## Próxima execução automática

**Amanhã 30/05/2026 06h BRT (09 UTC)** — vai pegar shipments criados pelos analistas após hoje 13:00 BRT.

## Riscos conhecidos

- Se XLSX no Drive sumir/quebrar, cron erra mas não para o motor (operação manual via UI continua).
- Se Drive API ficar fora do ar, `gog drive download` falha — cron loga e sai sem aplicar nada.
- Se motor (PM2 estoque-budamix) estiver offline, todos os batches HTTP falham. Mitigação: erro registrado no Telegram.
- Shipments antigos que mudam de status (BLOCKED → SAFE) hoje **não são reprocessados** porque já estão na baseline. Pra reprocessar: `DELETE FROM envios_full_baseline_shipments WHERE shipment_id = 'X'`.

## Cobertura final do "Cron diário ENVIOS FULL"

✅ **100% implementado e em produção**.

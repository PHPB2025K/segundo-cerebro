---
title: "Cron VPS — Stock Sync (Planilha → Supabase)"
type: workflow
created: 2026-04-17
updated: 2026-04-17
status: active
tags:
  - automacao
  - cron
  - vps
  - estoque
  - supabase
---

# Cron VPS — Stock Sync (Planilha → Supabase)

| Campo | Valor |
|-------|-------|
| **Host** | VPS 187.77.237.231 (Hostinger) |
| **Script** | `/opt/budamix-stock-sync/sync.py` (perms 0700, root-only) |
| **Log** | `/var/log/budamix-stock-sync.log` (0640) |
| **Cron** | `*/5 * * * * /usr/bin/python3 /opt/budamix-stock-sync/sync.py` |
| **Fonte** | [Planilha ESTOQUE](https://docs.google.com/spreadsheets/d/1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI/) |
| **Destino** | `product_variants.stock` no Supabase do [[projects/budamix-ecommerce|Budamix E-commerce]] |
| **Credencial** | `op://OpenClaw/uv6ngw5erk6ynksnr2pyzjfmlu/credential` (service_role, plaintext no arquivo) |
| **Status** | ✅ Ativo (primeiro run 17/04: 25 variants, 0 erros) |

## O que faz

Baixa a planilha de estoque como CSV (endpoint `gviz/tq?tqx=out:csv&sheet=ESTOQUE`), pula as 3 linhas de header, lê coluna A (ESTOQUE) e coluna B (SKU BASE), e faz PATCH em `product_variants?sku=eq.{sku}` com `{"stock": N}` via REST do Supabase.

Conversão de qty:
- Vazio ou texto não-numérico → `0`
- Formato BR (`1.234,56`) → inteiro (`1234`)
- Negativo → `0`
- Decimal → `floor`

## Substitui

Apps Script real-time em [scripts/google-apps-script-stock-sync.js](~/Documents/05-Projetos-Codigo/budamix-ecommerce/scripts/google-apps-script-stock-sync.js) — nunca foi instalado na planilha. Cron VPS ganha em não precisar de setup manual; perde em latência (5 min vs ~1-2s).

## Código-fonte local

- [scripts/stock-sync-cron.py](~/Documents/05-Projetos-Codigo/budamix-ecommerce/scripts/stock-sync-cron.py) — versão principal
- [scripts/stock-sync-cron.sh](~/Documents/05-Projetos-Codigo/budamix-ecommerce/scripts/stock-sync-cron.sh) — alternativa bash

Repo: `budamix-ecommerce`, commit `a915064`.

## Operações

| O que | Como |
|-------|------|
| Rodar manual | `ssh root@187.77.237.231 "python3 /opt/budamix-stock-sync/sync.py"` |
| Ver log | `ssh root@187.77.237.231 "tail -50 /var/log/budamix-stock-sync.log"` |
| Atualizar código | Editar localmente → `scp sync.py root@vps:/opt/budamix-stock-sync/` (re-substituir key) |
| Rotacionar key | `op read ... > /tmp/k && ssh vps "sed -i \"s|OLD_KEY|\$(cat /tmp/k)|\" /opt/..."` + `rm /tmp/k` |
| Desativar | `ssh root@vps "crontab -l | grep -v budamix-stock-sync | crontab -"` |

## Ver também

- [[projects/budamix-ecommerce]] — consumidor do `product_variants.stock`
- [[automacoes/workflows/estoque-pdf-parser]] — fluxo complementar (entrada de NF-e)

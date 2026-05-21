---
title: "MOC — Pedidos de Venda Atacado"
created: 2026-05-21
type: moc
status: active
tags:
  - moc
  - atacado
  - whatsapp
  - bling
  - fisco
---

# MOC — Pedidos de Venda Atacado

> Hub do pipeline ponta-a-ponta que recebe pedido de atacado via WhatsApp, interpreta com LLM, valida via Fisco e cria no Bling Matriz com PDF oficial.
> Pipeline cross-area envolvendo briefing, workflow N8N, agente Fisco, endpoint Mission Control e API v3 do Bling.

---

## Pipeline de ponta a ponta

```
Grupo WhatsApp (mensagem)
   ↓ Evolution API webhook
Workflow N8N (pedidos-venda-gb-bling)
   ↓ POST /api/fisco/pedidos-venda-gb
Mission Control (rota Fisco)
   ↓ X-Fisco-Secret + payload canônico
Agente Fisco
   ↓ LLM + alias map SKU + validação determinística + idempotência
Bling API v3 (Matriz)
   ↓ POST pedido + GET PDF oficial
Grupo WhatsApp (PDF + confirmação)
```

## Documentos canônicos

| Documento | Tipo | Status |
|---|---|---|
| [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.4]] | Briefing canônico | draft-for-approval |
| [[automacoes/workflows/pedidos-venda-gb-bling]] | Workflow N8N (T7WT4vGaRuWd0N0Q) | inativo até liberação |

> Versões anteriores do briefing (v, v2, v2.1, v2.2, v2.3) foram arquivadas em [[automacoes/workflows/_archive/README|_archive]] em 2026-05-20 (todas marcadas `status: superseded`).

## Atores

| Camada | Componente | Função |
|---|---|---|
| Captura | Evolution API (`trottingtuna-n8n.cloudfy.live`) | Webhook MESSAGES_UPSERT do grupo Kobe |
| Orquestração | N8N | Normaliza evento + monta payload canônico |
| Endpoint | [[projects/mission-control]] / [[memory/projects/mission-control]] | Rota `/api/fisco/pedidos-venda-gb` com `X-Fisco-Secret` |
| Inteligência | [[openclaw/agents/fisco/IDENTITY|Fisco]] | LLM + alias map SKU + idempotência persistente |
| Sistema fiscal | [[projects/financeflow|FinanceFlow]] | Integração Bling API v3 (OAuth Matriz/Filial) |
| ERP | Bling v3 Matriz (`58.151.616/0001-43`) | Criação do pedido + PDF oficial |

## Regras de ouro

1. **PDF enviado no grupo precisa ser obrigatoriamente o PDF oficial gerado pelo Bling.** Fallback interno só serve para debug — nunca para envio ao cliente/grupo (decisão v2.4).
2. **N8N não é autoridade fiscal nem de SKU.** Toda interpretação fica na rota Fisco/LLM.
3. **Idempotência persistente fica no Fisco**, não no N8N.
4. **Workflow segue inativo até decisão explícita** — ativar pode criar pedidos reais.

## Aprendizados técnicos relevantes

- [[knowledge/concepts/bling-api-v3-aprendizados]] — comportamentos não-óbvios da API v3 (PUT não aceita patch parcial, CFOP/tributos ignorados no payload, query `codigo` vs `pesquisa`, rate limit 3 req/s)

## Conexão com regra fiscal

- [[business/importacao/estrategia-fiscal-gb]] — modelo 90/10 v2.1 (LC 204/2023 + RIPI art. 43 X). Atacado Matriz pode usar TTD 409 quando aplicável.

## Política de retry do PDF oficial

| Tentativa | Quando |
|---:|---|
| 1 | imediato |
| 2 | +10s |
| 3 | +30s |
| 4 | +2 min |
| 5 | +10 min |
| 6 | +30 min |
| Falha | `failed_permanent_pdf_official` → DLQ → alerta privado para Pedro |

## Próximos passos rastreáveis

Lista vive no documento canônico [[automacoes/workflows/pedidos-venda-gb-bling#Próximos passos]]:

1. Pedro decidir criação real do pedido 953
2. Ativar workflow + rodar teste controlado sem `dry_run`
3. Ampliar `sku-aliases.json`
4. Ajustar resposta para bloqueios Fisco
5. Liberação contínua após N pedidos sem erro

## MOCs relacionados

- [[meta/mocs/MOC - Token Management]] — OAuth Bling Matriz/Filial (refresh 5h)
- [[meta/mocs/MOC - Governanca OpenClaw]] — leveling do Fisco (L1) e protocolos de revisão

---

*Criado: 2026-05-21 — Fase 4 de densificação do vault.*

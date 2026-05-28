---
title: "Operação GB Tempo Real — Seed inicial (grupos, DMs, mapeamento)"
created: 2026-05-28
type: project-data
status: pronto-para-implantacao
project: operacao-tempo-real
tags:
  - openclaw
  - kobe
  - whatsapp
  - slack
  - seed
---

# Operação GB — Seed inicial para `operation_groups`

> Captura confirmada via instância **WHATSAPP PRÓPRIO KOBE** em 2026-05-28 19:15 BRT.
> 8 de 9 grupos resolvidos automaticamente. Decisões Pedro de 28/05 incorporadas.

## 1. Tópico Telegram do briefing matinal

- **Daily Briefing** = thread `2` do Kobe Hub (`telegram:-1003730816228`).
- Já existe e é onde os briefings matinais 07h BRT são enviados desde 03/2026.

## 2. Grupos WhatsApp da operação

| # | Grupo | JID | Área | Agente owner | Auto-response | Observação |
|---|---|---|---|---|---|---|
| 1 | **Estoque - GB Importadora** | `120363407096324740@g.us` | estoque | **kobe** | ✅ ligar (confirmar recebimento, listar saldo, etc) | 4 participantes |
| 2 | **Devoluções - GB Importadora** | `120363411628970089@g.us` | devolucoes | **kobe** | ✅ ligar (confirmar recebimento, status devolução) | 4 participantes |
| 3 | **Contas a Receber - GB Importadora** | `120363321268883488@g.us` | contas_receber | **vault** | ❌ não | 6 participantes — adicionado 28/05 19:25 BRT |
| 4 | **Vendas atacado - GB Importadora** | `120363401241177278@g.us` | atacado | **scout** | ✅ já ativo (pipeline `novo_pedido` do wholesale-poller) | 4 participantes — JÁ EM PRODUÇÃO |
| 5 | **Compras - GB Importadora** | `120363409020629957@g.us` | compras | **scout** | ❌ não | 4 participantes |
| 6 | **Expedição - GB Importadora** | `120363242132245729@g.us` | expedicao | **kobe** | ❌ não | 13 participantes |
| 7 | **Sócios - GB Importadora** | `120363270687689452@g.us` | socios | **kobe** | ❌ não (sensível) | 4 participantes |
| 8 | **Financeiro - GB Importadora** | `120363428248073679@g.us` | financeiro | **vault** | ❌ não | 4 participantes |
| 9 | **Contas a Pagar - GB Importadora** | `120363409385839582@g.us` | contas_pagar | **vault** | ❌ não | 3 participantes |

## 3. Slack DMs com colaboradores

| Funcionário | Função | Slack user_id | Área | Agente owner | Privacidade |
|---|---|---|---|---|---|
| **Lucas Gabriel** | Analista Shopee | a resolver via `users.lookupByEmail` ou `users.list` | trader_shopee | **trader** | só kobe + rh (temas sensíveis) |
| **Leonardo Basseto** | Analista Amazon | a resolver | trader_amazon | **trader** | só kobe + rh |
| **Yasmin Oscarlino** | Analista Mercado Livre | a resolver | trader_ml | **trader** | só kobe + rh |

**Próximo passo Slack:** usar `python3 scripts/slack-read.py list --type im --limit 200` na VPS pra mapear cada user_id pelo nome, depois INSERT em `operation_groups` com `source='slack_dm'`.

## 4. Decisões Pedro 28/05 incorporadas

| Decisão | Valor |
|---|---|
| Tom briefing matinal | Conversacional, sem se estender muito |
| Slack — escopo | Só DMs com colaboradores (Lucas, Leonardo, Yasmin). Sem canais públicos. |
| Privacidade Slack | Só Kobe + agente RH veem DMs sensíveis |
| Estoque/Devoluções auto-response | Kobe responde coisas simples (confirmar recebimento, listar saldo) |
| Tópico do briefing | "📋 Daily Briefing" (thread 2 do Kobe Hub) |

## 5. Agentes do mapeamento — status hoje

| Agente | Status | Áreas que vai monitorar |
|---|---|---|
| **kobe** | ✅ ativo | TUDO (cérebro central) + Estoque + Devoluções + Expedição + Sócios |
| **vault** | ✅ ativo (CFO) | Financeiro + Contas a Pagar + Contas a Receber |
| **scout** | 🟡 fundação criada | Compras + Vendas atacado (já em produção) |
| **trader** | ✅ ativo (Daily Sales) | Slack DMs Lucas + Leonardo + Yasmin |
| **rh** | ✅ ativo | (mantém DMs funcionários WhatsApp — escopo separado) |
| **fisco** | 🔴 em construção | nada nesta fase |
| **spark** | ✅ ativo (ADS) | nada nesta fase |
| **builder** | ✅ ativo | nada nesta fase (dev, não operação) |

## 6. Status implementação

✅ **9/9 grupos resolvidos.** Pronto para Fase 0 (schema).

Próximos passos:
1. Fase 0: aplicar schema (`operation_groups`, `operation_messages`, `agent_message_memory`) no Supabase Budamix Central
2. Fase 1: INSERT seed (9 grupos + 3 DMs Slack)
3. Fase 2: generalizar `wholesale-evolution-poller` → `whatsapp-operacao-poller`
4. Fase 3: `slack-dm-poller`
5. Fase 4: dispatcher + memória layered
6. Fase 5: cron digest 22h + briefing 07h no tópico Daily Briefing (thread 2)

## 7. Inviolabilidades reforçadas

- Captura sempre ligada; auto-response só onde marcado ✅ acima.
- Grupo **Sócios** = leitura passiva apenas. Kobe nunca posta lá sem comando explícito.
- DMs Slack com colaboradores não saem do escopo Kobe + RH.
- Mídia (fotos NF, áudios) baixada localmente, OCR/Whisper só sob demanda.

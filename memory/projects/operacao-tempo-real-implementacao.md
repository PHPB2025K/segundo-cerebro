---
title: "Operação GB em Tempo Real — Implementação 100% concluída"
created: 2026-05-28
type: project-status
status: producao
project: operacao-tempo-real
tags:
  - openclaw
  - kobe
  - whatsapp
  - slack
  - producao
  - tempo-real
---

# Operação GB em Tempo Real — 100% implementado e em produção

> 5 fases entregues em 28/05/2026 numa única sessão. Tudo rodando em PM2 + cron na VPS.

## Camadas em produção

### Fase 0 — Schema Supabase Budamix Central
- `public.operation_groups` (12 canais cadastrados)
- `public.operation_messages` (fila idempotente via fingerprint UNIQUE)
- `public.agent_message_memory` (layered L0/L1/L2 com TTL)
- `public.daily_digests` (snapshot diário por agente)
- Realtime publication ativa em `operation_messages`

### Fase 1 — Seed (12 canais)
**9 grupos WhatsApp GB Importadora** (instância `WHATSAPP PRÓPRIO KOBE`):

| Grupo | JID | Agente | Auto-response |
|---|---|---|---|
| Estoque | `120363407096324740@g.us` | kobe | ✅ confirmar_recebimento, listar_saldo, consultar_movimento |
| Devoluções | `120363411628970089@g.us` | kobe | ✅ confirmar_recebimento, consultar_devolucao |
| Contas a Receber | `120363321268883488@g.us` | vault | ❌ |
| Vendas atacado | `120363401241177278@g.us` | scout | ✅ novo_pedido (em wholesale-poller atual) |
| Compras | `120363409020629957@g.us` | scout | ❌ |
| Expedição | `120363242132245729@g.us` | kobe | ❌ |
| Sócios | `120363270687689452@g.us` | kobe | ❌ (inviolável: nunca posta sem comando) |
| Financeiro | `120363428248073679@g.us` | vault | ❌ |
| Contas a Pagar | `120363409385839582@g.us` | vault | ❌ |

**3 DMs Slack com analistas** (workspace GB Importadora T03V1KHCPN1):

| Funcionário | Slack channel | user_id | Agente |
|---|---|---|---|
| Lucas Gabriel | `D08TCL5S4TT` | U08TCL5A8U9 (lsimon) | trader |
| Leonardo Basseto | `D0AUUQ3S8FJ` | U0AUUQ5MP6C (leonardoctparticular) | trader |
| Yasmin Oscarlino | `D09AX9TCMC7` | U09AX9SETDM (yasminoscarlino7) | trader |

Privacidade: DMs Slack só Kobe + RH veem.

### Fase 2 — `whatsapp-operacao-poller` (PM2)
- Script: `/var/www/mission-control/scripts/whatsapp-operacao-poller.py`
- PM2 name: `whatsapp-operacao-poller`
- Polling: 30s
- State: `/var/www/mission-control/data/whatsapp-operacao-poller-state.json`
- Substitui `wholesale-evolution-poller` (que segue rodando pro grupo Atacado por segurança; migrar quando estabilizar)

### Fase 3 — `slack-dm-poller` (PM2)
- Script: `/var/www/mission-control/scripts/slack-dm-poller.py`
- PM2 name: `slack-dm-poller`
- Polling: 60s
- Token via `slack-read.py` (1Password "Slack Pedro Read Only")
- Bug do Slack API tratado: `oldest` precisa de exatamente 6 casas decimais

### Fase 4 — `operacao-dispatcher` (PM2)
- Script: `/var/www/mission-control/scripts/operacao-dispatcher.py`
- PM2 name: `operacao-dispatcher`
- Polling: 10s sobre `operation_messages WHERE status='recebido'`
- Para cada msg: insere em `agent_message_memory` para Kobe (sempre) + agent_owner do canal
- L0 TTL 24h
- Detecta `intent_preview` (7 padrões: novo_pedido, confirmar_recebimento, consultar_saldo, devolucao, doc_financeiro, reclamacao, logistica)
- Detecta `contains_action_required` (regex com palavras-chave)

### Fase 5 — Digest 22h + Briefing 07h (v3 via Codex CLI — zero custo de API)
- Script digest: `/var/www/mission-control/scripts/digest-por-agente.py` (rola 22h, popula `daily_digests` — histórico/auditoria)
- Script briefing **v3**: `/var/www/mission-control/scripts/briefing-matinal.py`
  - **LLM via `codex exec` CLI** — usa a assinatura GPT Pro do Pedro (OAuth `pehpbroglio@gmail.com`), modelo gpt-5.5 default. **Zero cobrança de API.** Decisão Pedro 29/05.
  - Puxa mensagens REAIS das 24h anteriores
  - 2 seções: **📩 SLACK** (DMs analistas) e **📱 WHATSAPP** (grupos da operação)
  - Para cada seção, Kobe (via codex CLI) lê as conversas, entende contexto, narra:
    - Slack: 1 subseção por DM (Lucas/Leonardo/Yasmin) + "Olhada geral"
    - WhatsApp: 1 subseção por grupo + "Pontos pra você olhar hoje"
  - Resolve user_ids em nomes amigáveis (Pedro/Lucas/Leonardo/Yasmin/Pedro@lid)
  - Envia em Markdown ao Telegram tópico `2` (📋 Daily Briefing) do Kobe Hub
  - Split automático se > 4000 chars
- Cron 22h BRT (01 UTC): digest por agente (legado/auditoria)
- Cron 07h BRT (10 UTC): briefing matinal v3 com codex CLI
- Tom: conversacional, sem se estender.
- **Tempo médio:** ~30s por briefing (Slack 16s + WhatsApp 11s LLM via codex).
- **Notas:**
  - codex CLI binário em `/usr/bin/codex`. Auth OAuth persistente.
  - Flags usadas: `--sandbox read-only --skip-git-repo-check --ephemeral --color never --output-last-message`
  - Bug histórico: gpt-5-mini reasoning model gastava tokens pensando; resolvido ao mudar pra codex CLI (gpt-5.5 chat puro).

## Serviços PM2 ativos

```
whatsapp-operacao-poller   (Python, polling Evolution 30s, N grupos)
slack-dm-poller            (Python, polling Slack 60s, N DMs)
operacao-dispatcher        (Python, processa fila 10s)
wholesale-evolution-poller (legado, grupo Atacado, mantido por segurança)
```

## Crons Linux ativos

```
0  1 * * *  digest-por-agente.py       # 22h BRT
0 10 * * *  briefing-matinal.py        # 07h BRT
```

## Captura inicial (28/05 22:30 BRT)

- 27 mensagens WhatsApp dos 8 grupos ativos
- 300 mensagens Slack das 3 DMs (limite página 100 cada, paginação automática)
- 1078 mensagens roteadas para Kobe e Trader em `agent_message_memory`
- 169 action items detectados

## Inviolabilidades reforçadas

1. Captura sempre ON; resposta automática só onde `auto_response_intents` está preenchido.
2. Grupo **Sócios** = leitura passiva apenas (Kobe nunca posta sem comando explícito).
3. DMs Slack com colaboradores não saem do escopo Kobe + RH.
4. Token Slack/Evolution nunca em log/chat.
5. PM2 service `wholesale-evolution-poller` segue rodando até decisão explícita de migrar (não regredir Atacado).

## Próximos passos / refinamentos pendentes

- Migrar grupo Atacado do `wholesale-evolution-poller` para o novo pipeline (após validação 1-2 dias)
- Substituir sumarização programática do digest por LLM (qualidade do briefing)
- Adicionar mais user aliases conforme novos colaboradores aparecerem
- Aposentar `wholesale-evolution-poller` quando Atacado estiver migrado
- RLS pendente nas tabelas novas (advisor crítico) — tratar quando criar dashboard web

---
title: "Operação GB em Tempo Real — Blueprint de Monitoramento Unificado"
created: 2026-05-28
type: blueprint
status: draft-aprovacao
project: openclaw-operacao
tags:
  - openclaw
  - kobe
  - whatsapp
  - slack
  - operacao
  - tempo-real
---

# Operação GB em Tempo Real — Blueprint de Monitoramento Unificado

## 1. Objetivo

Capturar **em tempo real**, **de forma automatizada**, **toda a comunicação operacional** da GB Importadora (WhatsApp + Slack) e distribuir o contexto entre:

- **Kobe** (cérebro central — visibilidade total)
- **Agentes especialistas** (cada um vê o que é da sua área)
- **Pedro** (briefings agregados sob demanda + automáticos)

Sem dependência de polls diários, sem ação manual do Pedro, com latência típica < 1 minuto entre evento e disponibilidade na memória dos agentes.

---

## 2. Princípios fundamentais

1. **Captura é sempre ON, resposta nunca é automática** sem autorização explícita ou agente com escopo dedicado. O risco de auto-reply indevido (incidente 25/03 Alexandre Novaes) está documentado e é inviolável.
2. **Kobe é o cérebro central.** Toda mensagem capturada vai pro contexto do Kobe, sempre. Especialistas têm subset por área.
3. **Tempo real via Postgres Realtime** (Supabase channels), não cron periódico. Cron entra só pra digest/resumo, não pra captura.
4. **Memória layered L0/L1/L2** (padrão já validado no processor RH v3) — replicar para todos os agentes.
5. **Privacidade por escopo.** Dados RH/financeiro não vazam entre agentes sem necessidade. Cada agente vê só o que precisa para sua função.
6. **Idempotência por design.** Mesma mensagem nunca processada 2 vezes. Fingerprint baseado em `(instance, group_jid, message_id)`.
7. **Configuração declarativa.** Pedro adiciona um grupo novo editando JSON, não código. Mesmo padrão para grupos WhatsApp, canais Slack e DMs.

---

## 3. Arquitetura em camadas

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1 — CAPTURA (Pollers + Webhooks)                        │
│  • whatsapp-operacao-poller (daemon, 1 por instância Evolution)│
│  • slack-dm-poller (daemon, 1 por workspace)                   │
│  • webhook-evolution + webhook-slack (push complementar)       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2 — NORMALIZAÇÃO + FILA (Supabase)                      │
│  • Tabela operation_messages (raw, idempotente)                │
│  • Trigger: enriquece com area, agent_owner, intent_preview    │
│  • Realtime channel: operation_messages_inserts                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3 — ROTEAMENTO POR ÁREA                                 │
│  • config/operacao-routing.json (declarativo)                  │
│  • dispatcher daemon: lê realtime → enfileira por agente       │
│  • RPC notify_agent(agent_id, message_id)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────┬─────────────────────────────────────────┐
│  LAYER 4a — KOBE       │  LAYER 4b — AGENTES ESPECIALISTAS      │
│  Memória central       │  RH / Trader / Scout / Vault / Fisco   │
│  (todas mensagens)     │  (subset por área)                     │
└────────────────────────┴─────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 5 — DIGEST + BRIEFING                                   │
│  • Cron 22h BRT: cada agente resume sua área do dia            │
│  • Cron 07h BRT: Kobe consolida em briefing matinal pro Pedro  │
│  • Sob demanda: Pedro pergunta no Telegram, Kobe responde      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Schema de dados (Supabase Budamix Central)

### 4.1 `operation_groups` — registro dos canais monitorados

```sql
CREATE TABLE operation_groups (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  source text NOT NULL CHECK (source IN ('whatsapp_group','whatsapp_dm','slack_channel','slack_dm','telegram_topic')),
  external_id text NOT NULL,                -- group_jid, channel_id, etc
  display_name text NOT NULL,               -- nome legível ("Estoque - GB Importadora")
  area text NOT NULL,                       -- estoque | devolucoes | atacado | financeiro | rh | trader_shopee...
  agent_owner text NOT NULL,                -- kobe | rh | trader | scout | vault | fisco
  instance text,                            -- nome da instância Evolution (NULL pra Slack)
  poll_enabled boolean DEFAULT true,
  poll_interval_seconds int DEFAULT 30,
  notify_on_message boolean DEFAULT true,
  capture_only boolean DEFAULT true,        -- captura sem habilitar resposta
  members jsonb,                            -- [{number, name, role}]
  notes text,
  active boolean DEFAULT true,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  UNIQUE (source, external_id)
);
```

### 4.2 `operation_messages` — toda mensagem ingerida

```sql
CREATE TABLE operation_messages (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  group_id uuid REFERENCES operation_groups(id),
  -- Fingerprint idempotência
  fingerprint text UNIQUE NOT NULL,         -- "{source}:{external_id}:{msg_id}"
  -- Mensagem
  message_external_id text NOT NULL,
  sender_id text NOT NULL,                  -- número/user_id
  sender_name text,
  content_text text,
  content_media_url text,
  content_media_type text,                  -- image | audio | video | pdf | location
  reply_to_message_id text,
  timestamp_message timestamptz NOT NULL,   -- timestamp do evento original
  timestamp_ingested timestamptz DEFAULT now(),
  -- Enriquecimento
  area text,                                -- copiado de operation_groups
  agent_owner text,                         -- copiado de operation_groups
  intent_preview text,                      -- classificação rápida (regex/LLM-light)
  contains_action_required boolean DEFAULT false,
  -- Pipeline status
  status text DEFAULT 'recebido' CHECK (status IN (
    'recebido','enriquecido','roteado','memorizado','respondido','arquivado','erro'
  )),
  routed_to_agents text[],                  -- ['kobe','trader'] etc
  error_reason text,
  raw_payload jsonb
);

CREATE INDEX ON operation_messages (group_id, timestamp_message DESC);
CREATE INDEX ON operation_messages (agent_owner, status) WHERE status != 'arquivado';
CREATE INDEX ON operation_messages (area, timestamp_message DESC);
```

### 4.3 `agent_message_memory` — quem viu o quê (layered)

```sql
CREATE TABLE agent_message_memory (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id text NOT NULL,                   -- kobe | rh | trader | ...
  message_id uuid REFERENCES operation_messages(id),
  layer text NOT NULL CHECK (layer IN ('L0_session','L1_recent','L2_consolidated')),
  summary text,                             -- resumo do agente (não cópia bruta)
  importance numeric DEFAULT 0.5,           -- 0-1, decide retenção
  created_at timestamptz DEFAULT now(),
  expires_at timestamptz                    -- L0 expira em 24h, L1 em 7d
);

CREATE INDEX ON agent_message_memory (agent_id, layer, created_at DESC);
```

### 4.4 Realtime channel

```sql
-- Habilitar Realtime na tabela
ALTER PUBLICATION supabase_realtime ADD TABLE operation_messages;
```

Cada agente (ou o dispatcher central) subscreve ao channel `operation_messages` filtrando por `agent_owner = 'kobe'` etc.

---

## 5. Componentes a construir

### 5.1 Pollers (Layer 1)

**A) `whatsapp-operacao-poller` (daemon Python, PM2)**

Generaliza o `wholesale-evolution-poller` atual:

- Lê `operation_groups WHERE source='whatsapp_group' AND active=true`
- Para cada `instance` distinta, abre conexão Evolution e faz `findMessages` no JID
- Polling 30s padrão (configurável por grupo)
- Inserts em `operation_messages` com `ON CONFLICT (fingerprint) DO NOTHING`
- State persistente em disco (timestamp do último msg visto por grupo) — mesmo padrão do RH-poller

**Substitui:** o `wholesale-evolution-poller` atual (1 grupo hardcoded). O wholesale fica como caso particular dessa tabela.

**B) `slack-dm-poller` (daemon Python, PM2)**

Novo:

- Lê `operation_groups WHERE source IN ('slack_dm','slack_channel') AND active=true`
- Polling 60s (Slack tem rate limits mais agressivos)
- Usa `conversations.history` com cursor de `oldest` salvo em state
- Mesmo padrão de idempotência via fingerprint

**C) Webhook complementar (opcional, futuro)**

- Evolution webhook → endpoint `/webhook/evolution/operation` → fila direta em `operation_messages`
- Slack Events API → endpoint `/webhook/slack/operation`
- Latência ~instantânea, polling vira fallback

### 5.2 Dispatcher (Layer 3)

**`operacao-dispatcher` (daemon Node/Python, PM2)**

- Subscreve realtime channel `operation_messages`
- Em cada INSERT:
  1. Roteia: insere em `agent_message_memory` para Kobe + agente da área
  2. Se `contains_action_required = true`: dispara notificação Telegram pro agente owner
  3. Se for resposta automática habilitada (RH apenas hoje): aciona pipeline existente
- Latência típica < 1s do INSERT à entrada na memória

### 5.3 Memória layered (Layer 4)

Reutilizar `agent_memory_layered` que o **processor RH v3** já implementa:

- **L0 session:** últimas 50 mensagens não-resumidas, contexto imediato
- **L1 recent:** últimos 7 dias agregados por dia + temas
- **L2 consolidated:** snapshots semanais/mensais de decisões e padrões

Cron diário 23h BRT migra L0 → L1, semanal L1 → L2.

### 5.4 Digest + Briefing (Layer 5)

**Cron 22h BRT — Digest por agente:**

Cada agente lê suas mensagens do dia (`agent_message_memory WHERE layer='L0' AND created_at::date = today`) e produz:

- Resumo executivo (5-10 bullets)
- Ações pendentes detectadas
- SKUs/processos mencionados
- Pessoas-chave

Salvo em `daily_digests`.

**Cron 07h BRT — Briefing matinal Kobe → Pedro:**

Kobe lê:
- Todos os digests dos agentes especialistas
- Suas próprias mensagens não-digeridas
- `memory/context/pendencias.md` e `deadlines.md`

Produz briefing único enviado pro Pedro via Telegram (tópico geral do Kobe Hub).

---

## 6. Roteamento por área — config declarativa

Arquivo `/root/.openclaw/config/operacao-routing.json`:

```json
{
  "areas": {
    "estoque": {
      "agent_owner": "kobe",
      "telegram_topic": 11932,
      "auto_response": false
    },
    "devolucoes": {
      "agent_owner": "kobe",
      "telegram_topic": 11937,
      "auto_response": false
    },
    "atacado": {
      "agent_owner": "scout",
      "telegram_topic": 10494,
      "auto_response": true,
      "auto_response_intents": ["novo_pedido"]
    },
    "financeiro": {
      "agent_owner": "vault",
      "auto_response": false
    },
    "rh": {
      "agent_owner": "rh",
      "auto_response": true,
      "auto_response_intents": ["all_after_greeting"]
    },
    "trader_shopee": {
      "agent_owner": "trader",
      "auto_response": false
    }
  }
}
```

Pedro adiciona área nova só editando esse arquivo + INSERT em `operation_groups`.

---

## 7. Como Pedro alimenta o sistema (UX do cadastro)

### 7.1 Fluxo manual (primeiro lote)

Pedro me passa lista no formato:

```
Grupo: "Estoque - GB Importadora"
  → área: estoque
  → agente: kobe
  → instância: WHATSAPP PRÓPRIO KOBE
  → integrantes: Lucas, Yasmin, almoxarifado
```

Eu (Claude Code ou Kobe) faço:
1. Resolve o JID via `findChats` da Evolution
2. INSERT em `operation_groups`
3. Confirma com Pedro

### 7.2 Fluxo automático (futuro)

Telegram bot do Kobe Hub aceita comando:
```
/registrar_grupo "Estoque - GB Importadora" area=estoque agente=kobe
```

Kobe lista grupos pendentes que ele tá vendo passivamente e Pedro escolhe.

---

## 8. Memória compartilhada e contexto do Kobe

### 8.1 Kobe sempre tem TUDO

Toda mensagem em `operation_messages` gera `agent_message_memory` para `agent_id='kobe'`. Não importa a área.

### 8.2 Especialistas têm subset

Trader vê só `area IN ('trader_shopee','trader_ml','trader_amazon')`. RH só vê `area='rh'`. Vault só `financeiro`. Etc.

### 8.3 Briefing matinal Kobe agrega tudo

Estrutura do briefing 07h BRT:

```
=== BRIEFING OPERAÇÃO — 2026-05-29 07:00 BRT ===

ESTOQUE (3 mensagens ontem)
- Lucas pediu reposição YW1520RC...
- Almoxarifado reportou entrada container...

DEVOLUÇÕES (1 mensagem)
- Cliente João reportou caneca quebrada...

ATACADO (5 pedidos)
- 3 novos pedidos consolidados...

FINANCEIRO (2 mensagens)
- Bancos solicitaram extrato mensal...

RH (4 conversas em andamento)
- Sandra perguntou férias...

PENDÊNCIAS CRÍTICAS (cross-área)
- ...

DECISÕES ESPERADAS HOJE
- ...
```

### 8.4 Consulta sob demanda

Pedro pergunta no Telegram: "O que rolou no estoque essa semana?"

Kobe roda: `SELECT summary FROM agent_message_memory WHERE agent_id='kobe' AND area='estoque' AND created_at > now()-interval '7 days'` + agrega.

---

## 9. Plano de implementação por fases

### Fase 0 — Schema + tabela (1h trabalho)
- [ ] Migration: `operation_groups`, `operation_messages`, `agent_message_memory`
- [ ] Habilitar Realtime
- [ ] Seed: cadastrar os grupos que **já estão pollados** (Atacado, RH DMs) com tipo correto

### Fase 1 — Cadastro dos grupos da operação (Pedro + Claude/Kobe)
- [ ] Pedro me passa lista completa de grupos WhatsApp da operação
- [ ] Para cada: resolver JID, capturar nome, integrantes, mapear área + agente owner
- [ ] INSERT em `operation_groups` (ainda com `poll_enabled=false`)

### Fase 2 — Migração do wholesale-poller (2-3h)
- [ ] Generalizar `wholesale-evolution-poller` para ler de `operation_groups`
- [ ] Renomear → `whatsapp-operacao-poller`
- [ ] Validar com o grupo Atacado ativo (não regressão)
- [ ] Ativar `poll_enabled=true` nos grupos novos da operação um por um

### Fase 3 — Slack DM poller (3-4h)
- [ ] Implementar `slack-dm-poller` análogo ao WhatsApp
- [ ] Subir como PM2 service
- [ ] Cadastrar DMs com analistas (Lucas, Yasmin, Leonardo) em `operation_groups`
- [ ] Validar idempotência

### Fase 4 — Dispatcher + Memória layered (4-5h)
- [ ] Daemon `operacao-dispatcher` (Realtime → memory)
- [ ] Reutilizar lógica de memória layered do processor RH v3
- [ ] Smoke: enviar mensagem teste em grupo cadastrado, ver Kobe receber

### Fase 5 — Briefing matinal + Digest (3-4h)
- [ ] Cron 22h BRT: digest por agente
- [ ] Cron 07h BRT: briefing Kobe → Pedro via Telegram tópico 1
- [ ] Iterar prompt do briefing por 1 semana até calibrar

### Fase 6 — Webhook push (opcional, futuro)
- [ ] Endpoint `/webhook/evolution/operation` no Mission Control
- [ ] Reduz latência de 30s para ~1s
- [ ] Polling vira fallback

### Fase 7 — Comando de cadastro via Telegram (futuro)
- [ ] `/registrar_grupo` no Kobe Hub
- [ ] Pedro adiciona novos grupos sem mexer em arquivo

**Tempo total estimado: 15-20h de implementação distribuídas em 1-2 semanas.**

---

## 10. Riscos e segurança

### 10.1 Risco de auto-reply indevido
- **Mitigação:** `capture_only=true` por padrão. Auto-reply só habilita via `auto_response_intents` explícito por área. Allowlist do `groupPolicy` do Evolution permanece "allowlist", não "open".

### 10.2 Vazamento de dados entre agentes
- **Mitigação:** policy de leitura por agente em `agent_message_memory` (RLS quando ativarmos). Kobe é o único com escopo global.

### 10.3 Volume + custo LLM
- **Mitigação:** `intent_preview` é classificador leve (regex/keyword). LLM caro só roda em mensagens com `contains_action_required=true` ou em digests.

### 10.4 Mensagens com mídia (foto da nota fiscal, áudio do colaborador)
- **Mitigação:** Layer 1 baixa e armazena em `/root/.openclaw/media/operacao/{date}/` + Storage Supabase. OCR/Whisper só sob demanda.

### 10.5 Compliance LGPD
- **Mitigação:** dados pessoais identificáveis (CPF, endereço) detectados via regex no enriquecimento → flag `pii_redacted`. Retenção em L0/L1/L2 com TTL.

### 10.6 Inviolável (já documentado em decisões)
- OpenClaw/Baileys NUNCA com `dmPolicy=open`.
- Resposta automática só em áreas com escopo + autorização Pedro.
- Token Slack User OAuth nunca em log/chat.

---

## 11. Métricas de sucesso

| Métrica | Meta |
|---|---|
| Latência mensagem → memória Kobe | < 60s em 95% dos casos |
| Cobertura de grupos cadastrados | 100% dos grupos operacionais |
| Mensagens perdidas (duplicadas / esquecidas) | 0 (idempotência valida) |
| Tempo Pedro gasta consultando WhatsApp/Slack | -50% em 30 dias |
| Briefing matinal entregue às 07:00 BRT | 7/7 dias |
| Falsos positivos em "action_required" | < 20% |

---

## 12. Próximos passos imediatos (esta semana)

1. **Pedro:** lista de grupos WhatsApp operacionais (nome + área + integrantes principais). Não precisa de IDs `@g.us` — o sistema resolve.
2. **Pedro:** lista de funcionários cujas DMs do Slack devem entrar no monitoramento.
3. **Eu/Claude:** aplicar schema (Fase 0) + cadastrar lote inicial (Fase 1) com `poll_enabled=false`.
4. **Kobe ou eu:** generalizar wholesale-poller (Fase 2).
5. Após validação dos pontos 1-4, plugar Slack (Fase 3) e dispatcher (Fase 4).

---

## 13. Decisões pendentes para discussão

- **Dono do briefing matinal:** Kobe envia direto ao Pedro, ou roda numa thread Telegram específica?
- **Tom do briefing:** seco-direto ou conversacional? (alinhar com preferência Pedro de "direto")
- **Slack — captura DMs ou também canais públicos?** Canais públicos da empresa podem ter ruído (memes, etc).
- **Privacidade Slack DMs:** Pedro fala com funcionários sobre temas sensíveis. Quem além do Kobe pode ver? Recomendação: só Kobe + RH para DMs com colaboradores.
- **Resposta automática Estoque/Devoluções:** começamos só captura (`capture_only=true`), ou ativamos Kobe pra responder coisas simples (confirmar recebimento, etc)?

---

*Blueprint sujeito a revisão após primeira lista de grupos do Pedro.*

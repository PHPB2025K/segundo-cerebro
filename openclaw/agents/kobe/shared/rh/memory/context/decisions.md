---
title: "decisions"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Decisões de RH

_Registro permanente. Nunca contradizer._

## 2026-03-30
- Agente RH criado como 5º membro do time Kobe
- Modelo: GPT 5.4 (migrado 2026-04-06)
- Fase 1: Monitor de Ponto + Alertas básicos
- Relatórios de ponto → Pedro via Telegram (tópico RH). Comunicação com funcionários → WhatsApp do Kobe
- Ponto Certo é fonte de verdade — sem cópias na memória
- Irregularidades detectadas → contatar funcionário via WhatsApp do Kobe antes de qualquer correção
- Tom com funcionários: colaborativo, nunca punitivo. Objetivo = registros corretos, não fiscalização
- Fluxo: detectar → WhatsApp funcionário → aguardar confirmação → corrigir. Sem resposta 48h → escalar Pedro
- Registros só podem ser corrigidos COM confirmação do funcionário (nunca unilateral)

## Regra Universal — Horários em Brasília (2026-04-01)
TODOS os horários apresentados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de exibir. Vale para relatórios, alertas, logs, timestamps — qualquer comunicação.


## 2026-04-30 — Defesa em profundidade Evolution + polling

- Canal RH oficial: instância Evolution `RECURSOS HUMANOS GB` (+55 19 99299-7273).
- Webhook Evolution pode falhar silenciosamente; solução de maio é manter Evolution e adicionar polling 30s (`rh-poller`) + detector de mensagens presas (`rh-stuck-detector`).
- Migrar para Baileys só se webhook falhar mais que 2x em maio.

## 2026-04-30 — Banco de horas acumulado inviolável

- Saldo acumulado nunca decrementa por saldo mensal negativo.
- Saldo mensal positivo soma ao acumulado; negativo é ignorado no acumulado.
- Única redução do acumulado: funcionário usa horas como folga compensatória por ação explícita.

## 2026-04-30 — Conversas RH no admin

- Admin Ponto Certo terá módulo Conversas RH para supervisão em tempo real.
- Bottom nav mobile prioriza Conversas RH no lugar de Histórico/Ponto.
- Telegram deixa de receber spam de mensagem normal; só escalonamentos e erros.


## 2026-05-04 — WhatsApp RH

- Em 04/05, não enviar mensagens proativas/alinhamentos para funcionários sem aprovação explícita do Pedro.
- O agente RH deve continuar em produção para responder mensagens inbound espontâneas.
- Wrapper `send-whatsapp.py --instance rh` bloqueia proativo por padrão durante o guard; respostas receptivas usam exceção explícita `--allow-rh-reply`.
- Mensagens RH devem ser texto puro com `linkPreview:false`; evitar listas, polls, interativos e previews/rich render.

---
title: "telegram-map"
created: 2026-04-26
type: memory-integration
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - integration
---
# Mapa de Tópicos — Telegram Hub

## Grupo
- **Nome:** Tobias Hub
- **ID:** -1003730816228
- **Tipo:** Supergroup (Forum/Tópicos)

## Tópicos

| Thread ID | Tópico | Uso |
|---|---|---|
| 2 | 📋 Daily Briefing | Briefing matinal, agenda, clima, pendências |
| 3 | 🛒 Marketplaces | ML, Amazon, Shopee — vendas, pedidos, relatórios |
| 4 | 🚢 Importação | Skiway, Open Trade, embarques, documentos |
| 6 | 💻 Projetos SaaS | Bidspark, SimulImport, Canguu, Atlas Finance |
| 7 | 💰 Financeiro | Extratos, contas a pagar/receber, fluxo de caixa |
| 8 | 🚨 Urgente | Alertas críticos realmente urgentes, incidentes imediatos, pedidos em atraso graves |
| 9 | 📣 Marketing | Instagram, conteúdo, campanhas, redes sociais |
| 10 | 👥 RH | Equipe, analistas, contratações |
| 11 | 🛍️ Compras | Regra fixa: qualquer assunto relacionado a compras deve ficar aqui, incluindo fornecedores, cotações, pedidos de compra, planejamento/projeção de compras e reposição de canecas |
| 12 | 📦 Estoque & Expedição | Níveis de estoque, envios, logística nacional |
| 13 | ⚙️ Operacional & Sistema | Crons, integrações, VPS, backups, skills |
| 10204 | 🚨 Alertas | Todo conteúdo relacionado a alertas: watchdogs, guards, audits, monitores, failure alerts, resumos técnicos e avisos de risco/problema |
| 10222 | Daily Sales Report - SLACK | Desenvolvimento, previews, alertas, QA, avisos e qualquer comunicação sobre o Daily Sales Report dos funcionários no Slack |
| 10469 | Gestão de Funcionários | Assuntos de gestão específica de funcionários da empresa e rotina semanal `✅ Rotina semanal de Gestão de Funcionários` |
| 10494 | Pedidos Atacado Automação | Assunto exclusivo da automação do WhatsApp **Pedidos de Venda - GB** / pedidos de atacado: desenho, testes, N8N, Bling Matriz, PDF oficial do pedido, parser, validação, webhook, bloqueios e alertas dessa rotina |
| 11259 | Amazon ADS | Assunto exclusivo para qualquer comunicação relacionada a ADS da Amazon: análises semanais, grupos de anúncio, BidSpark, ações, D+7, auditorias, alertas e decisões operacionais de Amazon Ads |
| 11932 | Estoque | Desenvolvimento do sistema de estoque, alertas, divergências, decisões técnicas e comunicação com Pedro fora da operação diária. A fonte operacional real é o WhatsApp **Estoque - GB Importadora**. |
| 11937 | Devoluções | Desenvolvimento, alertas, divergências e decisões sobre devoluções. A fonte operacional real é o WhatsApp **Devoluções - GB Importadora**. |

## Formato de delivery para crons
```
channel: telegram
to: -1003730816228:topic:{thread_id}
```

## Mapa Cron → Tópico

| Cron | Thread ID | Tópico |
|---|---|---|
| Daily Briefing | 2 | 📋 Daily Briefing |
| Inbox Cleanup | silencioso | Consolidado no resumo diário de Alertas |
| GitHub Backup | silencioso | Consolidado no resumo diário de Alertas |
| Resumo Diário — Alertas Watchdogs | 10204 | 🚨 Alertas |
| Daily Sales Report — Slack Funcionários | 10222 | Daily Sales Report - SLACK |
| Daily Sales v2 — Marketplace Rules Watch Refresh | 10222 | Daily Sales Report - SLACK |
| Daily Sales v2 — Consolidação Semanal/Mensal Trader | 10222 | Daily Sales Report - SLACK |
| Daily Sales v2 — Himmel/Granola Context Sync | 10222 | Daily Sales Report - SLACK |
| Gestão Funcionários — atas semanais Slack | 10469 | Gestão de Funcionários |
| Automação Pedidos Atacado / Pedidos de Venda GB | 10494 | Pedidos Atacado Automação |
| Amazon Ads / BidSpark | 11259 | Amazon ADS |
| Estoque GB — sistema/movimentações/alertas | 11932 | Estoque |
| Devoluções GB — sistema/alertas/triagem | 11937 | Devoluções |

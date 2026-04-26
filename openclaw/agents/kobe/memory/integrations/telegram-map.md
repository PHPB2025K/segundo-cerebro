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
| 8 | 🚨 Urgente | Alertas críticos, pedidos em atraso, problemas |
| 9 | 📣 Marketing | Instagram, conteúdo, campanhas, redes sociais |
| 10 | 👥 RH | Equipe, analistas, contratações |
| 11 | 🛍️ Compras | Fornecedores, cotações, pedidos de compra |
| 12 | 📦 Estoque & Expedição | Níveis de estoque, envios, logística nacional |
| 13 | ⚙️ Operacional & Sistema | Crons, integrações, VPS, backups, skills |

## Formato de delivery para crons
```
channel: telegram
to: -1003730816228:topic:{thread_id}
```

## Mapa Cron → Tópico

| Cron | Thread ID | Tópico |
|---|---|---|
| Daily Briefing | 2 | 📋 Daily Briefing |
| Inbox Cleanup | 13 | ⚙️ Operacional & Sistema |
| GitHub Backup | 13 | ⚙️ Operacional & Sistema |

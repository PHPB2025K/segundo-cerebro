---
title: "Ponto Certo"
created: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/ponto-certo/"
tags:
  - project
  - dev
  - rh
---

# Ponto Certo

**Path:** `~/Documents/05-Projetos-Codigo/ponto-certo/`
**Branch:** main
**Stack:** Vite + React + TypeScript + Tailwind + shadcn/ui + Supabase
**Deploy:** VPS 187.77.237.231, PM2 (porta 3091), Traefik HTTPS
**URL:** https://ponto.budamix.com.br
**Supabase:** dgldsmhbeosjgfrbegyv
**GitHub:** https://github.com/PHPB2025K/ponto-certo.git

## O que é

Ponto eletrônico dos funcionários Budamix. Registro de entrada/saída/intervalo com validação GPS (raio do escritório), QR Code diário, banco de horas, atrasos, relatórios admin. Funcionários usam pelo celular (Android/iOS).

## Decisões-chave

- [15/04] Timer baseado em primitivo ms (não Date object) — evita race condition em Android
- [15/04] Deploy via SCP (token GitHub na VPS inválido)
- [30/04] Módulo Conversas RH no admin (`/admin/conversas-rh`) — ferramenta de supervisão das conversas do agente RH com funcionários em tempo real → [[memory/context/decisoes/2026-04#[30/04 noite] Módulo Conversas RH]]
- [30/04] Saldo acumulado de banco de horas é INVIOLÁVEL — função SQL `calcular_banco_horas_v2` corrigida pra ignorar saldo mensal negativo → [[memory/context/decisoes/2026-04#[30/04 noite] Saldo acumulado]]

## Módulos atuais

| Módulo | Path | Função |
|---|---|---|
| Dashboard | `/admin/dashboard` | KPIs e visão geral |
| Equipe | `/admin/equipe` | Funcionários ativos |
| Banco de Horas | `/admin/banco-horas` | Saldos individuais e teto |
| Ajustar Ponto | `/admin/historico-ponto` | Editar registros manualmente |
| Solicitações | `/admin/solicitacoes` | Aprovar/rejeitar ajustes e justificativas |
| **Conversas RH** | `/admin/conversas-rh` | Histórico de conversas agente RH ↔ funcionários (estilo WhatsApp Web, real-time) |
| Configurações | `/admin/ajustes` | Tolerâncias, jornadas, débito mensal |
| Relatórios | `/admin/relatorios` | Espelho de ponto, banco semestral |

## Stack RH (PM2 daemons na VPS)

| Process | Função |
|---|---|
| `webhook-rh` | Recebe webhooks Evolution → debounce |
| `debounce-rh` | Agrupa mensagens fragmentadas em 30s |
| `rh-processor` | Chama agente RH + envia resposta + persiste em `rh_conversation_history` |
| `rh-poller` | Vigia 30s — pega o que o webhook deixou cair (defesa em profundidade) |
| `rh-stuck-detector` | Alerta 3min — avisa Pedro se agente travou |

## Pendências

- [ ] Deploy do módulo Conversas RH em produção (build OK local, falta SCP/git pull na VPS + restart PM2)
- [ ] Reautenticar `gh auth` na VPS para restaurar `git pull`
- [ ] Validar timer Android com funcionário real
- [ ] Validar layout mobile estoque (equipe usa celular no armazém)

## Notas relacionadas

- [[openclaw/agents/rh/IDENTITY]] — Agente RH monitora ponto
- [[memory/context/people]] — Equipe de funcionários
- [[openclaw/agents/kobe/shared/rh/knowledge/faq-funcionarios|FAQ Funcionários]] — base de respostas do agente
- [[memory/context/decisoes/2026-04|Decisões abr/26]] — histórico de decisões

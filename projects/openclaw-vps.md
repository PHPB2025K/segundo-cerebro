---
title: "OpenClaw VPS"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/OpenClaw-VPS/"
tags:
  - project
  - dev
  - openclaw
  - infra
---

# OpenClaw VPS

**Path:** `~/Documents/05-Projetos-Codigo/OpenClaw-VPS/`
**Branch:** N/A (não é git repo)
**Stack:** Configs e scripts de deploy
**Deploy:** VPS Hostinger (187.77.237.231)
**CLAUDE.md:** sim

## O que é

Infraestrutura crítica. VPS Hostinger (Ubuntu 24.04) rodando OpenClaw (6 agentes, 12+ crons), estoque.budamix.com.br, import.budamix.com.br, e Budamix Central Live Sales. Acesso via SSH.

## Status Infraestrutura

| Recurso | Estado |
|---------|--------|
| Disco | 63.4% de 47GB — monitorar ⚠️ |
| Memória | 80% + swap 52% — processo zombie ⚠️ |
| OpenClaw | v2026.4.5, GPT 5.4 |
| Sync | Cron 06:45 BRT (git pull + rsync segundo-cerebro) |

## Serviços Rodando

- OpenClaw Gateway (127.0.0.1:18789) — 6 agentes
- estoque.budamix.com.br — Traefik + SSL
- import.budamix.com.br — Nginx + SSL
- Budamix Central backend / Live Sales

## Pendências

- [ ] VPS disco — limpeza de logs, backups, Chrome cache
- [ ] VPS memória — investigar processo zombie
- [ ] Porta 8084 (Evolution API?) aberta na UFW — verificar necessidade
- [ ] Tailscale/WireGuard não implementado (recomendado)
- [ ] 3 crons com timeout insuficiente (job-monitor, Contingency Guard, Organização Noturna)
- [ ] GitHub Backup timeout 120s → 300s

## Notas relacionadas

- [[openclaw/agents/kobe/IDENTITY]]
- [[openclaw/agents/kobe/AGENTS]]
- [[openclaw/agents/kobe/BOOT]]
- [[openclaw/system/user-briefing-openclaw-v1]]
- [[openclaw/system/user-briefing-openclaw-v2]]
- [[projects/openclaw-config]]
- [[meta/mocs/MOC - Governanca OpenClaw]]
- [[meta/mocs/MOC - Token Management]]
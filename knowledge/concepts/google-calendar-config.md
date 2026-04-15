---
title: "Google Calendar Config"
created: 2026-04-14
updated: 2026-04-15
type: reference
status: active
path: "~/Documents/05-Projetos-Codigo/google-calendar-config/"
tags:
  - knowledge
  - config
  - calendar
  - oauth
---

# Google Calendar Config

**Path:** `~/Documents/05-Projetos-Codigo/google-calendar-config/`
**Branch:** N/A (não é git repo)
**Stack:** OAuth config (JSON)
**Deploy:** nenhum — configuração estática

## O que é

Repositório de configuração OAuth para integração com Google Calendar. Contém apenas o arquivo `gcp-oauth.keys.json` com credenciais OAuth do projeto GCP. Usado pelo MCP Google Calendar no Claude Code e potencialmente pelo Kobe para consultar agenda.

**Conteúdo:**
- `gcp-oauth.keys.json` — credenciais OAuth do projeto GCP

> Não é um projeto de código — é um repositório de configuração. Considerar mover para `knowledge/concepts/` ou absorver no mapeamento de credenciais.

## Notas relacionadas

- [[knowledge/concepts/credenciais-map]] — mapeamento de credenciais
- [[openclaw/agents/kobe/IDENTITY]] — Kobe usa Calendar
- [[projects/openclaw-vps]] — integração VPS
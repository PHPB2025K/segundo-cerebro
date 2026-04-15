---
title: "Estoque Budamix"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/estoque-budamix/"
tags:
  - project
  - dev
  - estoque
---

# Estoque Budamix

**Path:** `~/Documents/05-Projetos-Codigo/estoque-budamix/`
**Branch:** main
**Stack:** Next.js + Supabase + N8N (PDF parser)
**Deploy:** VPS
**CLAUDE.md:** sim
**Último commit:** 22 hours ago — feat: initial commit

## O que é

Sistema de gestão de estoque para a Budamix. Next.js frontend, Supabase backend, N8N para parsing automático de PDFs de entrada de mercadoria. Deploy na VPS (estoque.budamix.com.br). Design system Budamix aplicado (3 iterações). URL: https://estoque.budamix.com.br

## Decisões-chave

- [13/04] Supabase em vez de SQLite para persistência
- [13/04] N8N para PDF parsing (workflow ID: WyxKDxwIkuuL8BdH)
- [13/04] Traefik reverse proxy (não Nginx direto)
- [13/04] Fix parseInt milhar brasileiro + fix col_brand — 4 operações reprocessadas, zero erros

## Pendências

- [ ] Validar layout mobile (equipe usa celular no armazém)
- [ ] Conectar com planilha real de estoque (Google Sheets)

## Notas relacionadas

- [[openclaw/agents/builder/memory/projects/canguu]]
- [[memory/projects/estoque-budamix]]
- [[openclaw/agents/builder/IDENTITY]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[openclaw/agents/fisco/IDENTITY]]
- [[business/empresa/_index]]
- [[meta/mocs/MOC - Supabase Ecosystem]]
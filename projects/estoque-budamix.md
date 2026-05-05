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
**Repo:** [PHPB2025K/estoque-budamix](https://github.com/PHPB2025K/estoque-budamix) (privado, criado 05/05/2026)
**Branch:** main
**Stack:** Next.js 16 + Supabase + N8N (PDF parser)
**Deploy:** VPS (estoque.budamix.com.br) — PM2 `estoque-budamix:3050`, Traefik reverse proxy
**CLAUDE.md:** sim (`@AGENTS.md`)

## O que é

Sistema de gestão de estoque para a Budamix. Next.js frontend, Supabase backend, N8N para parsing automático de PDFs de entrada de mercadoria. Deploy na VPS (estoque.budamix.com.br). Design system Budamix aplicado.

**Uso: desktop-only.** A equipe do almoxarifado opera só em computador — não otimizar pra mobile (confirmado por Pedro 05/05/2026 após inferência inicial errada). Pente fino mobile aplicado na PR2 fica como bonus (touch targets 44-48px, fontSize 16px), mas a partir da PR3 assume desktop-first/only.

## Decisões-chave

- [13/04] Supabase em vez de SQLite para persistência
- [13/04] N8N para PDF parsing (workflow ID: WyxKDxwIkuuL8BdH)
- [13/04] Traefik reverse proxy (não Nginx direto)
- [13/04] Fix parseInt milhar brasileiro + fix col_brand — 4 operações reprocessadas, zero erros
- [05/05] **PR1 — fix(stock): inventory drift bugs.** Devolução movida pra entrada (`devolucao_cliente`); race condition fechada via `readStockCell` + snapshot mutável local; regressão do parseInt milhar BR refixada via helper `parseStockValue`; validação `ALLOWED_SUBTYPES` na API. Commits `e3031db` (baseline rsync) + `42dbeec` (fix).
- [05/05] **PR2 — feat(stock): radio cards + SKU autocomplete.** Substituiu `<Select>` de motivo por radio cards com default Compra/Venda. Novo `SkuAutocomplete` com busca SKU+descrição e normalização NFD (acentos opcionais) — mata classe de bug onde nomes coloquiais ("914", "caneca bola", "anilao", "montado 800") não casavam com SKU canônico. Commit `eeab9c5`.

## Pendências

- [ ] **PR3 — bug #1 SKUs específicos remanescentes.** Validar com a planilha real (`1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`) se ainda há SKUs que escapam do match após PR2. Lista: série 914, caneca bola, anilão 800, montado 800.
- [ ] **PR4 — kits/BOM (bugs #5 e #6).** Sistema não decompõe kit em componentes na baixa; vendas de kit vs unitário não conciliam. Mudança estrutural — schema novo. Skill `planilha-precificacao` documenta sintaxe `BASE1/BASE2` em col B das abas marketplace; explorar BOM a partir daí.

## Notas relacionadas

- [[projects/canggu]]
- [[memory/projects/estoque-budamix]]
- [[openclaw/agents/builder/IDENTITY]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[openclaw/agents/fisco/IDENTITY]]
- [[business/empresa/_index]]
- [[meta/mocs/MOC - Supabase Ecosystem]]
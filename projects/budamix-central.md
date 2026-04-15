---
title: "Budamix Central (Canggu)"
created: 2026-04-15
type: project
status: active
path: "Lovable project (prj_wMl99f4aixldKCwBiJv9xDedL7AR)"
tags:
  - project
  - dev
  - dashboard
  - canggu
---

# Budamix Central (Canggu)

**URL:** https://central.budamix.com.br
**Branch:** main
**Stack:** React + Vite + shadcn/ui + Supabase + pgvector + Lovable
**Deploy:** Vercel (via Lovable)
**Supabase:** `sqbkoprcmnznmzbwdrmf`

## O que é

Dashboard interno da Budamix. Centraliza vendas em tempo real (Live Sales), gestão de produtos, chat WhatsApp com clientes (Ana/Giovana), e busca vetorial semântica via pgvector. Acesso role-based (admin/viewer).

## Módulos

| Módulo | Status | Descrição |
|--------|:------:|-----------|
| Live Sales | ✅ | Dashboard real-time: pedidos, faturamento, ranking SKU, gráfico dual axis |
| Produtos | ✅ | Gestão de 27 base_products, campos ricos (IA), embeddings vetoriais |
| Chat WhatsApp | ✅ | Integração Evolution API + N8N, pipeline vetorial Ana |
| Busca Vetorial | ✅ | pgvector + text-embedding-3-small (OpenAI), 384d |
| TV Mode | ✅ | Layout zero-scroll 1920×1080, flex-based, breakpoint lg: |
| Auth | ✅ | Supabase Auth, role-based (admin/viewer) |

## Acessos

| Usuário | Email | Role |
|---------|-------|------|
| Pedro | pehpbroglio@gmail.com | admin |
| Simone Peron | simoneperon@uol.com.br | viewer |

## Decisões-chave

- [13/04] Layout TV: flex-based com h-screen + overflow-hidden. Breakpoint lg: (≥1024px)
- [09/04] Role-based access implementado (admin/viewer, middleware + API)
- [09/04] Domínio migrado para central.budamix.com.br (SSL Let's Encrypt)
- [06/04] Reestruturação dados: 3 camadas (base_products → products → product_listings)
- [06/04] Pipeline vetorial Ana: embedding pergunta → busca vetorial → SQL → contexto

## Pendências

- [ ] Fase 4 cleanup: remover campos antigos (marketplace_links, available_kits, price_marketplace) + dropar tabela marketplace_product_mapping
- [ ] ~14 Session Extractors desabilitados (timeout 120s insuficiente, precisam 300s+)
- [ ] Analistas preenchendo campos ricos dos 44 produtos (Top 10 primeiro)
- [ ] Validar layout mobile (equipe usa celular no armazém)
- [ ] Domínio antigo `central.gbformulario.com` — considerar redirect

## Notas relacionadas

- [[openclaw/agents/builder/IDENTITY]] — Builder
- [[memory/context/people]] — equipe
- [[knowledge/concepts/stack-tecnico]] — stack
- [[meta/mocs/MOC - Supabase Ecosystem]] — Supabase

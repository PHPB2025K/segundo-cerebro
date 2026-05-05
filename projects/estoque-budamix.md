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
- [05/05] **PR3 modo investigação (sem código)** — auditoria da aba ESTOQUE da planilha de Precificação + Supabase histórico das últimas 500 ops. Achados: 484 OK / 16 erro (3,2%), dos 16 erros **12 são "Estoque insuficiente" = bug #5/#6 dominante**. PR2 cobre 3 dos 4 mismatches reais; **POT1BB único SKU duplicado em toda a aba** (L8 com Trava + L9 sem Trava, descrições diferentes — não é acidente). Termos coloquiais (caneca bola, anilão, montado) não existem nas descrições da planilha — necessário alias.
- [05/05] **PR3a — fix(autocomplete): match bidirecional pra sufixo a mais.** Adiciona reverse `query.includes(sku)` com guarda `query.length >= 4` AND `sku.length >= 4`. Cobre o caso `KIT4YW800SQ_T` (operador digita sufixo a mais que não existe). Validado com Playwright. Commit `9f980cc`.
- [05/05] **🔴 Descoberta crítica: nenhuma das 3 PRs chegou em produção.** Repo GitHub criado nesta sessão NÃO é a fonte do deploy. App é deployado via rsync histórico de 13/04 direto na VPS, sem ponte automática GitHub→VPS. Plano de remediação aprovado com 5 salvaguardas, execução iniciada e **pausada no Bloco 4 (`git fetch` 403)** aguardando decisão de credencial GitHub.

## Pendências

- [ ] **Retomar deploy em produção** (pause em 05/05 22h aguardando decisão de credencial GitHub na VPS). Estado: backup feito em `/var/www/estoque-budamix.backup-20260505-2143/`, `.env` preservado (hash `ec2bbf991d37033859c0af1e1ed9609f`), `.git/` inerte criado, remote `origin` configurado. Próximo passo: Pedro escolher entre Deploy Key SSH (recomendação), PAT, ou rsync from Mac. Depois refazer Bloco 4 → Bloco 5 (`reset --hard` com OK ativo) → Bloco 7 (build com OK ativo) → restart + smoke. Plano completo no Session Extract de [[memory/sessions/2026-05-05]] e memory local `estoque_budamix_deploy_checkpoint.md`.
- [ ] **POT1BB duplicado** na aba ESTOQUE da planilha (`1u74a...`): renomear L9 → `POT1BB_ST` (sem Trava). Aplicação aguardando OK Pedro pra rodar via gspread.
- [ ] **Lista de aliases** em `/tmp/pr3-cadastro-cleanup.md`: 5 famílias pra Pedro preencher os termos coloquiais reais (anilão? montado? caneca bola?) e devolver.
- [ ] **KFJ003** SKU não encontrado no histórico — Pedro consultar equipe se é fantasma ou cadastrar retroativo.
- [ ] **PR4 — kits/BOM (bugs #5 e #6).** Sistema não decompõe kit em componentes na baixa; vendas de kit vs unitário não conciliam. **Bug dominante** (75% dos erros reais). Mudança estrutural — schema novo. Skill `planilha-precificacao` documenta sintaxe `BASE1/BASE2` em col B das abas marketplace; explorar BOM a partir daí. Tocar só depois de fechar PR1+PR2+PR3a em produção + cleanup cadastro.

## Notas relacionadas

- [[projects/canggu]]
- [[memory/projects/estoque-budamix]]
- [[openclaw/agents/builder/IDENTITY]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[openclaw/agents/fisco/IDENTITY]]
- [[business/empresa/_index]]
- [[meta/mocs/MOC - Supabase Ecosystem]]
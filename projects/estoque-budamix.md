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
**Stack:** Next.js 16 + Supabase + pdf-parse v2 (parser local, substituiu N8N em 20/05/2026)
**Deploy:** VPS (estoque.budamix.com.br) — PM2 `estoque-budamix:3050`, Traefik reverse proxy
**CLAUDE.md:** sim (`@AGENTS.md`)

## O que é

Sistema de gestão de estoque para a Budamix. Next.js frontend, Supabase backend, N8N para parsing automático de PDFs de entrada de mercadoria. Deploy na VPS (estoque.budamix.com.br). Design system Budamix aplicado.

**Uso: desktop-only.** A equipe do almoxarifado opera só em computador — não otimizar pra mobile (confirmado por Pedro 05/05/2026 após inferência inicial errada). Pente fino mobile aplicado na PR2 fica como bonus (touch targets 44-48px, fontSize 16px), mas a partir da PR3 assume desktop-first/only.

## Decisões-chave

- [28/05] **Fase 2 mapeamento de SKUs deployada** (Claude Code direto, não Kobe). Camada de dados: `sku_aliases` (25) + `kit_bom` (16) + Postgres function `resolver_sku()` + views `vw_resolver_dashboard` e `vw_decisoes_pendentes_familias`. Catálogo `_catalog_estoque` (93 SKUs snapshot). Camada de código: `resolveSku()` em `lib/stock-movements.ts`, rotas `ingest-safe-outbound` e `sheets/update` refatoradas pra expandir `kit_bom` em N movimentos por componente. Build webpack OK, PM2 restart pid 2428590. Smoke test 5/5 cenários. Doc handoff em `docs/stock-movements-phase2-resolver.md`. Cobertura: 8% dos 2.119 divergentes aplicariam (142 mov, 36 SKUs finais, ~5.470 un).
- [28/05] **Clink descontinuado:** `CK4742_B` removido do catálogo, aliases (`CK4742_BB`, `CK4742`) e kit (`KIT2CK4742_B`) marcados `active=false`. Família `CK_jarra_clink` inteira (150 SKUs / 332 mov) considerada descontinuada.
- [28/05] **Planilha ENVIOS FULL oficial:** ID `1zfll5bvkIUqY56y0YcJ-ZP1GoMupcj_f`, só 5 abas (FBA AMAZON, FULL ML, SHOPEE 1/2/3). Código `lib/envios-full.ts` tem `AMAZON FULL` e `FULL MAGALU` sobrando que devem ser removidos. 53 movimentos `source_channel='amazon_full'` no banco vieram de planilha errada.
- [13/04] Supabase em vez de SQLite para persistência
- [13/04] N8N para PDF parsing (workflow ID: WyxKDxwIkuuL8BdH) — ⚠️ DESCONTINUADO em 20/05/2026, substituído por parser local Next (`/api/sheets/parse-pdf`)
- [13/04] Traefik reverse proxy (não Nginx direto)
- [13/04] Fix parseInt milhar brasileiro + fix col_brand — 4 operações reprocessadas, zero erros
- [05/05] **PR1 — fix(stock): inventory drift bugs.** Devolução movida pra entrada (`devolucao_cliente`); race condition fechada via `readStockCell` + snapshot mutável local; regressão do parseInt milhar BR refixada via helper `parseStockValue`; validação `ALLOWED_SUBTYPES` na API. Commits `e3031db` (baseline rsync) + `42dbeec` (fix).
- [05/05] **PR2 — feat(stock): radio cards + SKU autocomplete.** Substituiu `<Select>` de motivo por radio cards com default Compra/Venda. Novo `SkuAutocomplete` com busca SKU+descrição e normalização NFD (acentos opcionais) — mata classe de bug onde nomes coloquiais ("914", "caneca bola", "anilao", "montado 800") não casavam com SKU canônico. Commit `eeab9c5`.
- [05/05] **PR3 modo investigação (sem código)** — auditoria da aba ESTOQUE da planilha de Precificação + Supabase histórico das últimas 500 ops. Achados: 484 OK / 16 erro (3,2%), dos 16 erros **12 são "Estoque insuficiente" = bug #5/#6 dominante**. PR2 cobre 3 dos 4 mismatches reais; **POT1BB único SKU duplicado em toda a aba** (L8 com Trava + L9 sem Trava, descrições diferentes — não é acidente). Termos coloquiais (caneca bola, anilão, montado) não existem nas descrições da planilha — necessário alias.
- [05/05] **PR3a — fix(autocomplete): match bidirecional pra sufixo a mais.** Adiciona reverse `query.includes(sku)` com guarda `query.length >= 4` AND `sku.length >= 4`. Cobre o caso `KIT4YW800SQ_T` (operador digita sufixo a mais que não existe). Validado com Playwright. Commit `9f980cc`.
- [05/05] **🔴 Descoberta crítica: nenhuma das 3 PRs chegou em produção.** Repo GitHub criado nesta sessão NÃO é a fonte do deploy. App é deployado via rsync histórico de 13/04 direto na VPS, sem ponte automática GitHub→VPS. Plano de remediação aprovado com 5 salvaguardas, execução iniciada e **pausada no Bloco 4 (`git fetch` 403)** aguardando decisão de credencial GitHub.
- [20/05] **Deploy retomado e concluído via rsync direto** — checkpoint encerrado. Fluxo: build local → rsync excluindo `.env`/`node_modules` → `npm ci --omit=dev` → `pm2 restart`. Backup automático em `/root/.openclaw/backups/estoque-budamix-pre-<TS>.tar.gz`. Commits `42dbeec` + `eeab9c5` + `9f980cc` em prod desde 19:11 BRT. Build via `--webpack` (turbopack quebra externals).
- [20/05] **PR4 — feat(pdf): parser local substituindo webhook n8n.** Lucas reportou SKUs `_B` "sumindo". Causa raiz: workflow n8n quebrado (`{"error":"Nenhum item encontrado"}` pra tabela SKU+Qtd; parseava "Pedido 659" como SKU=PEDIDO qty=659 em PDFs Bling). Nova rota `/api/sheets/parse-pdf` com pdf-parse v2 (`PDFParse` class) + regex filtrando header/footer + dedup. `serverExternalPackages: ["pdf-parse","pdfjs-dist"]` no `next.config.ts`. Commit `2a38f57`.
- [20/05] **Validação end-to-end** com PDF real do Lucas: 7 SKUs `54171*_B` + `914C_B` extraídos OK → baixa real registrada na planilha Google Sheets → reversão equivalente → planilha voltou bit por bit ao estado original. Audit trail no Supabase: 14 ops `TESTE QA Claude%`.

## Pendências

- [ ] **Limpar operações de teste do banco** (opcional): `DELETE FROM estoque_operations WHERE operation_name LIKE 'TESTE QA Claude%';` — 14 linhas de validação 20/05.
- [ ] **Webhook n8n descontinuado** (`trottingtuna-n8n.cloudfy.live/webhook/estoque-upload`): não é mais usado pelo sistema, pode ser desativado no painel n8n sem impacto.
- [ ] **Regra simples pro Lucas (operacional)**: PDF de baixa/entrada precisa ter **exatamente 2 colunas — SKU e Quantidade**, nada mais. Não usar PDFs do Bling/ML/pedidos de venda (têm texto extra que confunde).
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
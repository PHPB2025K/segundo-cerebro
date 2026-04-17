---
title: "GB Import Hub"
created: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/gb-import-hub/"
tags:
  - project
  - dev
  - importacao
---

# GB Import Hub

**URL:** https://import.budamix.com.br
**Branch:** main
**Stack:** Next.js + React + Supabase + Edge Functions (Deno) + Terminal49 + Mapbox
**Deploy:** VPS 187.77.237.231 (Nginx + Traefik + SSL Let's Encrypt)
**Supabase:** `ocxvwwaaqqxecmzhfxhb`
**Repo:** `PHPB2025K/gb-import-hub`

## O que é

Sistema de gestão de importações da GB Importadora. Controla containers, documentos, tracking marítimo, pagamentos (numerário + 70% balanço), e conferências de custos. Central de controle para todas as operações de importação.

## Schema (12 tabelas)

| Tabela | O que guarda |
|--------|-------------|
| containers | Dados centrais do container (ID, status logístico/financeiro) |
| documents | Documentos de importação (PDF, storage) |
| finance_pagamentos | Pagamentos (numerário, 70% balanço) |
| finance_numerario_itens | Itens individuais por pagamento |
| conferencias_numerario | Conferências de numerário |
| conferencias_comunicacoes | Comunicações de conferência |
| referencias_mercado | Referências de mercado para precificação |
| referencias_ncm | Referências NCM/tributárias |
| vessel_tracking | Tracking de embarcações (Terminal49) |
| vessel_position_history | Histórico de posições |
| tracking_alerts | Alertas de tracking |
| container_milestones | Marcos/eventos do container |

## Edge Functions (17 deployadas)

Inclui: `extract-import-document`, `calculate-tax-references`, `fetch-vessel-position`, `get-mapbox-token`, entre outras.

## Containers Ativos

| Container | Status Logístico | Status Financeiro |
|-----------|:----------------:|:-----------------:|
| GB25007 | finished | A PREENCHER |
| GB25009 | finished | 🔴 70% R$72.232 vence 16/04 |
| GB25010 | **customs** (descarregado BRIOA 16/04) | 30% pago, **numerário R$64.136,40 vence 20/04**, 70% R$81.750 vence 10/05 |
| GB25011 | **road** (saindo SC→SP 20/04, Qualilog retira em Itajaí) | Numerário pago, 70% R$71.419 vence 24/05 |
| GB26001 | A PREENCHER | Sem datas/valores no sistema |
| GB26002 | A PREENCHER | Sem datas/valores no sistema |

## Decisões-chave

- [08/04] Migração completa de Lovable Cloud para Supabase externo: 12 tabelas, 4.530 rows, 17 Edge Functions, 27 docs, SSL
- [08/04] Dual cycle model: status logístico (production→maritime→customs→road→finished) ≠ status financeiro (pending/paid/overdue)
- [08/04] Supabase REST API: ANON_KEY para reads, SERVICE_ROLE_KEY para writes
- [17/04] GB25010 — PNI registrada: 22 itens em `finance_numerario_itens` somando R$64.136,40 (bate exato). `payment_numerario_value` atualizado de R$72.305,25 (estimativa) para R$64.136,40 (PNI oficial), USD $12.876,64 × câmbio 4,9806. Mapeamento de categorias: ISS→SERVICOS_TRADING, IPI/ICMS LP/LR→IMPOSTOS_FEDERAIS com observacao, frete marítimo→OUTROS_CUSTOS.
- [17/04] GB25010 — Status `maritime`→`customs` após poll Terminal49 confirmar: `vessel_arrived` 15/04 12:30 UTC + `vessel_discharged` 16/04 11:57 UTC em BRIOA (Itapoá).
- [17/04] Credencial 1Password — skill precisa atualizar comando: `--fields credential` (não `password`) para itens do tipo API Credential (ex: `gb-import-hub-supabase-service-role`).
- [17/04] GB25011 — 5 docs novos anexados (tabela `documents` + bucket Storage `container-documents`): **NF Transferência** NF-000649, **CC-e NF Transferência** 000649, **Nota Fiscal** NFS 580012 Open Trade, **Invoice** INVOICE&PL-GB25011.xls, **Packing List** PACKING LIST-GB25011.xlsx (13.7 MB). HBL já existia. Status container movido `maritime`→`road` para saída SC→SP segunda 20/04.

## Pendências

- [ ] Frontend Lovable ainda aponta pro Supabase antigo — atualizar env vars OU usar somente deploy VPS
- [ ] MarineTraffic API key não configurada (tracking funciona via Terminal49)
- [ ] Módulo Conferências (validação custos importação) — em construção
- [ ] Skill gb-import-hub v2 validada (14/15 testes OK, terminal49-fetch-shipment com bug HTTP 500)
- [ ] Edge Function `poll-terminal49` — não atualiza `vessel_tracking.pod_ata` quando chega milestone `vessel_arrived`, e não bumpa `last_api_call`. Milestones são gravados OK, só os campos derivados ficam stale. Cosmético mas pode confundir health checks/dashboards.
- [ ] Atualizar skill `skills/gb-import-hub/SKILL.md` — comando `op item get --fields password` está errado para itens do tipo API Credential. Usar `--fields credential`.

## Notas relacionadas

- [[business/importacao/_index]] — índice importação
- [[automacoes/sops/atualizar-pagamento-importacao]] — SOP pagamentos
- [[knowledge/concepts/credenciais-map]] — credenciais (7 items GB Import Hub)
- [[memory/context/deadlines]] — prazos financeiros

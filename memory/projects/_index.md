# Projetos — Índice Geral

> Fonte de verdade para status de todos os projetos.
> Detalhes em `memory/projects/{nome}.md`.
> Atualizar sempre que um projeto mudar de status.

---

## 🟢 Ativos

| Projeto | Status | Métrica-chave | Arquivo |
|---------|--------|---------------|---------|
| GB Importadora/Budamix | 🟢 Operação | 44 SKUs ativos, 4 canais | [[memory/context/business-context|business-context]] |
| OpenClaw/Kobe | 🟢 Produção | 6 agentes GPT 5.4, v2026.4.5, 22 crons | [[agents/kobe/AGENTS|Kobe AGENTS]] |
| Canggu | 🟢 Produção | Dashboard + busca vetorial + WhatsApp + roles | [[agents/builder/memory/projects/canguu|canggu]] |
| Jornal da Manhã | 🟢 Produção | Digest diário | — |

---

## 🔨 Em Construção

| Projeto | Status | Próximo Marco | Arquivo |
|---------|--------|---------------|---------|
| FinanceFlow | 🔨 Em construção | Automação Word→Excel 6 CNPJs | [[agents/fisco/IDENTITY|Fisco]] |
| SimulaImport | 🔨 Em construção | MicroSaaS MVP | [[agents/builder/memory/projects/simulimport|simulimport]] |
| Atlas Finance | 🔨 Em construção | DFC com Lovable/Supabase | [[agents/builder/memory/projects/atlas-finance|atlas-finance]] |
| Módulo Conferências | 🔨 Em construção | Validação custos importação | [[memory/projects/gb-import-hub-schema|gb-import-hub]] |

---

## ⏸️ Pausados

| Projeto | Motivo | Retomar quando | Arquivo |
|---------|--------|----------------|---------|
| TikTok Shop | Exploração, sem prioridade | Quando definir estratégia MCN | tiktok-shop.md |

---

## ✅ Concluídos / Arquivados

| Projeto | Resultado | Data |
|---------|-----------|------|
| Reestruturação Dados Canggu | 5 fases completas, busca vetorial ativa | 06/04/2026 |

---

## Mudanças Recentes

- [09/04] Budamix Central — Role-based access (admin/viewer), login Simone, domínio central.budamix.com.br
- [09/04] Zero Anthropic concluído — 43 refs removidas, fallback chain opção C, doctor warnings corrigidos → [[memory/context/decisoes/2026-04|decisões abril]]
- [09/04] RH v2 — Auditoria + deploy ([[agents/rh/SOUL|SOUL]], [[agents/rh/AGENTS|AGENTS]], [[agents/kobe/shared/rh/skills/comunicacao-funcionarios/SKILL|comunicacao skill]]) + cron semanal + tabela comunicacoes_rh
- [09/04] Amazon Request Review — Fix completo (batch, persistência, timing handling)
- [08/04] Budamix Central Live Sales — Redesign: gráfico dual axis, thumbnails, estoque, pulsante → [[agents/builder/IDENTITY|Builder]]
- [08/04] [[memory/projects/gb-import-hub-schema|GB Import Hub]] — Migração completa para Supabase externo + deploy VPS + SSL
- [08/04] Skill [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] criada (mapeamento 4 abas, proteção de 40 fórmulas)
- [08/04] PCM001 inserido na planilha de estoque, preço ajustado R$19,90, custo R$1,04
- [08/04] GB Import Hub — Schema extraído (12 tabelas, 17 Edge Functions, 27 migrations consolidadas)
- [07/04] Amazon BR — Listing PCM001 ACCEPTED via SP-API (DRINK_COASTER, FBA, ASIN pendente)
- [07/04] ML + Shopee — Anúncios criados para Kit Porta-Copos PCM001
- [07/04] Skills: [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]], [[skills/shopee-listing-creator/SKILL|shopee-listing-creator]]
- [07/04] [[agents/kobe/AGENTS|OpenClaw]] — Fix fallback cascata (anthropic/claude-haiku-4-5)
- [06/04] Canggu — Reestruturação + pipeline vetorial Ana + migração GPT 5.4

---

*Atualizado: 09/04/2026*

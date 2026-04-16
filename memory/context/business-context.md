---
title: "business context"
created: 2026-04-14
type: context
status: active
tags:
  - memory
  - context
---

# Contexto Geral — Pedro Broglio

> **CACHE COMPILADO** — visão panorâmica para boot rápido do /cerebro.
> Em caso de conflito, as fontes individuais prevalecem (ver PROPAGATION.md).
> Fontes: projects/_index.md (projetos), people.md (equipe), decisoes/ (decisões)
> Índices: [[business/importacao/_index|Importação]], [[business/marketplaces/_index|Marketplaces]], [[business/financeiro/_index|Financeiro]], [[business/empresa/_index|Empresa]], [[business/marketing/_index|Marketing]]
> Mapeamento local: [[memory/context/dev-projects-local]]
> Last updated by: /salve — 06/04/2026

---

## Sobre Mim

Pedro Broglio. Founder da GB Importadora, marca Budamix. Importo utensílios domésticos (vidro, cerâmica, porcelana) da China e vendo nos principais marketplaces do Brasil. Opero com AI em tudo: agente OpenClaw (Kobe) com 6 sub-agentes, automações de preço/estoque, IA de atendimento, e estou construindo MicroSaaS para o setor de importação.

---

## Empresa

| Dado | Valor |
|------|-------|
| Razão Social | GB Importadora |
| Marca | Budamix |
| CNPJs | 6 operacionais |
| Sede operacional | Pedreira-SP |
| Filial fiscal | Itajaí-SC (TTD 409, ICMS benefício) |
| Portos | Itajaí, Itapoá |
| Trading | Open Trade, ICMS 4% |
| Sourcing | Yiwu, China |
| Marca INPI | Registrada |

---

## Projetos / Negócios

> Ver índice completo: [[memory/projects/_index|Índice de Projetos]]

| Nome | Status | Métricas-chave |
|------|--------|----------------|
| GB Importadora/Budamix | 🟢 Ativo | 44 SKUs ativos, 4 canais de venda |
| [[openclaw/agents/kobe/AGENTS|OpenClaw/Kobe]] | 🟢 Ativo | 6 agentes, 22 crons, 16 integrações |
| [[projects/budamix-central|Canggu]] | 🟢 Ativo | Dashboard interno (Next.js 16, VPS pm2+Traefik), busca vetorial, 27 base_products |
| FinanceFlow | 🔨 Em construção | Automação fiscal 6 CNPJs |
| [[openclaw/agents/builder/memory/projects/simulimport|SimulaImport]] | 🔨 Em construção | MicroSaaS simulação importação |
| [[openclaw/agents/builder/memory/projects/atlas-finance|Atlas Finance]] | 🔨 Em construção | DFC com Lovable/Supabase |
| Jornal da Manhã | 🟢 Ativo | Digest diário Perplexity + Claude |

---

## Equipe

| Nome | Função | Notas |
|------|--------|-------|
| Pedro Broglio | CEO, dev, estratégia | Faz tudo |
| 2 analistas | Operação, cadastro, marketplaces | Preenchendo dados de produtos no Canggu → [[memory/context/people|detalhes]] |
| [[openclaw/agents/kobe/IDENTITY|Kobe]] (AI) | Agente principal OpenClaw | GPT 5.4, 6 sub-agentes: [[openclaw/agents/trader/IDENTITY|Trader]], [[openclaw/agents/spark/IDENTITY|Spark]], [[openclaw/agents/builder/IDENTITY|Builder]], [[openclaw/agents/fisco/IDENTITY|Fisco]], [[openclaw/agents/rh/IDENTITY|RH]] |
| Ana (AI) | Atendimento WhatsApp | IA conversacional via N8N + Evolution API |

---

## Foco Atual (Abril 2026)

1. Expansão de SKUs nos marketplaces (Kit Porta-Copos MDF publicado em ML + 3 lojas Shopee)
2. Enriquecimento de dados de produtos no Canggu (analistas preenchendo, embeddings vetoriais)
3. FinanceFlow — automação fiscal para 6 CNPJs
4. Estabilização do Canggu (WhatsApp, busca vetorial, context-builder)
5. Padronização de anúncios Shopee via skill shopee-listing-creator
6. Estoque Budamix — controle de entrada/saída armazém via Google Sheets (https://estoque.budamix.com.br)

---

## Canais de Venda

| Canal | Status | Integração |
|-------|--------|------------|
| Amazon BR | 🟢 FBA ativo | SP-API + Amazon Ads |
| Shopee | 🟢 Ativo | 3 contas OAuth, sync cada 2min |
| Mercado Livre | 🟢 Ativo | 3 apps, sync cada 2min |
| budamix.com.br | 🟢 Ativo | E-commerce próprio |
| Budamix Central | 🟢 Ativo | central.budamix.com.br (VPS pm2+Traefik, role-based: admin/viewer) |
| TikTok Shop | ⏸️ Exploração | Outreach MCN/afiliados |

---

## Infraestrutura AI

| Componente | Status | Detalhes |
|------------|--------|----------|
| [[openclaw/agents/kobe/AGENTS|OpenClaw/Kobe]] | 🟢 Produção | VPS Hostinger, v2026.4.5, GPT 5.4 (todos os agentes migrados) |
| Ana (atendimento) | 🟢 Produção | N8N + Evolution API + Supabase |
| Canggu | 🟢 Produção | Next.js 16 + Supabase + pgvector, VPS (pm2 porta 3000 + Traefik SSL), role-based access (admin/viewer) |
| Claude Code | 🟢 Uso diário | VS Code + MCPs |
| Segundo Cérebro | 🟢 Configurado | ~/segundo-cerebro |

---

## Resultados Recentes

- [15/04] Amazon Ads otimização cirúrgica: mapeamento 139 campanhas, 4 ações executadas (83 logadas), 48→39 ativas, ACOS 22,9%→meta 19%. Revisão 29/04 → [[memory/context/decisoes/2026-04|decisões]]
- [15/04] Auditoria completa de margens Shopee: 72 SKUs, 4 correções aplicadas direto no Google Sheets via API (comissão escalonada, afiliado real, margens unificadas) → [[memory/context/decisoes/2026-04|decisões]]
- [15/04] Google Sheets OAuth configurado: Claude Code agora edita planilha de precificação diretamente no Drive
- [15/04] Skill [[skills/planilha-precificacao/SKILL|planilha-precificacao]] criada + SOP upload Drive
- [15/04] E-commerce budamix.com.br redesign completo (5 agentes, identidade Budamix) → [[projects/budamix-ecommerce]]
- [14/04] Vault centralizado (5 fases), Knowledge Graph instalado, go-live e-commerce (Stripe→MP)
- [13/04] Amazon Request Review fix definitivo, Estoque Budamix criado, DPM002 no ML
- [09/04] Budamix Central: role-based access, domínio central.budamix.com.br
- [08/04] GB Import Hub migrado, skill spreadsheet-pricing criada

---

*Última atualização: 15/04/2026 — sessão 7*

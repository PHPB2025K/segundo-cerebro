# Contexto Geral — Pedro Broglio

> **CACHE COMPILADO** — visão panorâmica para boot rápido do /cerebro.
> Em caso de conflito, as fontes individuais prevalecem (ver PROPAGATION.md).
> Fontes: projects/_index.md (projetos), people.md (equipe), decisoes/ (decisões)
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

| Nome | Status | Métricas-chave |
|------|--------|----------------|
| GB Importadora/Budamix | 🟢 Ativo | 44 SKUs ativos, 4 canais de venda |
| OpenClaw/Kobe | 🟢 Ativo | 6 agentes, 22 crons, 16 integrações |
| Canggu | 🟢 Ativo | Dashboard interno, busca vetorial, 27 base_products |
| FinanceFlow | 🔨 Em construção | Automação fiscal 6 CNPJs |
| SimulaImport | 🔨 Em construção | MicroSaaS simulação importação |
| Atlas Finance | 🔨 Em construção | DFC com Lovable/Supabase |
| Jornal da Manhã | 🟢 Ativo | Digest diário Perplexity + Claude |

---

## Equipe

| Nome | Função | Notas |
|------|--------|-------|
| Pedro Broglio | CEO, dev, estratégia | Faz tudo |
| 2 analistas | Operação, cadastro, marketplaces | Preenchendo dados de produtos no Canggu |
| Kobe (AI) | Agente principal OpenClaw | GPT 5.4, 6 sub-agentes |
| Ana (AI) | Atendimento WhatsApp | IA conversacional via N8N + Evolution API |

---

## Foco Atual (Abril 2026)

1. Expansão de SKUs nos marketplaces (Kit Porta-Copos MDF publicado em ML + 3 lojas Shopee)
2. Enriquecimento de dados de produtos no Canggu (analistas preenchendo, embeddings vetoriais)
3. FinanceFlow — automação fiscal para 6 CNPJs
4. Estabilização do Canggu (WhatsApp, busca vetorial, context-builder)
5. Padronização de anúncios Shopee via skill shopee-listing-creator

---

## Canais de Venda

| Canal | Status | Integração |
|-------|--------|------------|
| Amazon BR | 🟢 FBA ativo | SP-API + Amazon Ads |
| Shopee | 🟢 Ativo | 3 contas OAuth, sync cada 2min |
| Mercado Livre | 🟢 Ativo | 3 apps, sync cada 2min |
| budamix.com.br | 🟢 Ativo | E-commerce próprio |
| TikTok Shop | ⏸️ Exploração | Outreach MCN/afiliados |

---

## Infraestrutura AI

| Componente | Status | Detalhes |
|------------|--------|----------|
| OpenClaw/Kobe | 🟢 Produção | VPS Hostinger, v2026.4.5, GPT 5.4 (todos os agentes migrados) |
| Ana (atendimento) | 🟢 Produção | N8N + Evolution API + Supabase |
| Canggu | 🟢 Produção | Lovable + Supabase + pgvector |
| Claude Code | 🟢 Uso diário | VS Code + MCPs |
| Segundo Cérebro | 🟢 Configurado | ~/segundo-cerebro |

---

## Resultados Recentes

- [08/04] GB Import Hub migrado para Supabase externo — online em https://import.budamix.com.br
- [08/04] Migração completa: 12 tabelas, 4.530 rows, 17 Edge Functions, 27 docs, SSL Let's Encrypt
- [08/04] Skill spreadsheet-pricing criada (mapeamento de 4 abas, 40 fórmulas protegidas)
- [08/04] PCM001 na planilha: preço R$19,90, custo R$1,04
- [07/04] PCM001 publicado em ML + Shopee (3 lojas) + Amazon BR (FBA, ASIN pendente)
- [07/04] Skills: shopee-listing-creator, amazon-listing-creator, spreadsheet-pricing
- [07/04] Fix OpenClaw: fallback cascata corrigido
- [06/04] Reestruturação Canggu + pipeline vetorial Ana + migração GPT 5.4

---

*Última atualização: 07/04/2026*

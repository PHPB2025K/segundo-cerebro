---
title: "MEMORY"
created: 2026-04-14
type: memory-config
agent: kobe
status: active
tags:
  - agent/kobe
---

# MEMORY.md — Índice Central de Memória

_Último update: 2026-04-29 23:30 BRT (Consolidação Diária)._

---

## Estrutura

```
memory/
├── context/
│   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   ├── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
│   ├── people.md          ← Contatos importantes
│   └── business-context.md ← Vocabulário, números de referência
├── projects/
│   ├── gb-importadora.md  ← Operação principal
│   ├── simulimport.md     ← MicroSaaS — simulador de importação
│   ├── bidspark.md        ← MicroSaaS — automação de ADS (Amazon + ML)
│   ├── canguu.md          ← MicroSaaS — agente IA atendimento
│   └── atlas-finance.md   ← Sistema financeiro GB (contas a pagar/receber)
├── sessions/
│   └── YYYY-MM-DD.md      ← Notas diárias (expira 30 dias após consolidação)
├── integrations/
│   ├── tools-map.md       ← Ferramentas, IDs, acessos
│   ├── telegram-map.md    ← Grupo Kobe Hub — tópicos e thread IDs
│   ├── github-repos.md    ← Mapeamento completo repos GitHub (23 ativos, 7 arquivados)
│   ├── whatsapp-integration.md  ← Status e regras do WhatsApp
│   ├── whatsapp-allowlist.md    ← Contatos/grupos autorizados (READ vs READ+SEND)
│   └── whatsapp-groups-full.md  ← Listagem completa dos 39 grupos
├── feedback/
│   ├── content.json       ← Rejeições de conteúdo/design
│   ├── tasks.json         ← Rejeições de tarefas/execução
│   ├── recommendations.json ← Rejeições de recomendações
│   └── digest.json        ← Rejeições de resumos/digestos
└── pending.md             ← Aguardando input do Pedro
```

## Carregamento por sessão

### Sempre carregado (automático via workspace context)
- `SOUL.md`, `USER.md`, `AGENTS.md`, `IDENTITY.md`
- `MEMORY.md` (este arquivo)

### Carregado no boot
- `memory/sessions/` de hoje + ontem
- `memory/pending.md`

### Sob demanda (memory_search → memory_get)
- `memory/context/*` — decisões, lições, pessoas
- `memory/projects/*` — projetos específicos
- `memory/integrations/*` — dados de ferramentas
- `memory/feedback/*` — consultar ANTES de fazer sugestões

## Integrações Ativas

| Ferramenta | Status | Credenciais |
|---|---|---|
| Telegram | ✅ Bot @TOBIAS_USER_BOT + Grupo Kobe Hub (11 tópicos) | Config OpenClaw |
| Brave Search | ✅ Pesquisa web | Config + 1Password |
| 1Password CLI | ✅ Service Account, vault "OpenClaw" | Systemd override |
| Google (gog) | ✅ Gmail + Calendar + Drive + Sheets (2 contas) | OAuth tokens |
| GitHub (gh) | ✅ CLI autenticado, PHPB2025K (23 ativos, 7 arquivados) | PAT no 1Password |
| OpenAI Whisper | ✅ Transcrição de áudio | API key no systemd |
| Instagram | ✅ Via RapidAPI (instagram120) | RapidAPI key |
| Mercado Livre | ✅ 3 apps (Vendas, Financeiro, Métricas) | Tokens em .ml-tokens*.json |
| Shopee OAuth Multi-Account | ✅ 3 contas gerenciadas automaticamente | Server porta 8901, auto-refresh 3h30 |
| Amazon Ads | ✅ Via Supabase do Bidspark | Refresh token no Supabase |
| Amazon SP-API | ✅ Integração completa. Endpoint NA, marketplace BR (A2Q3Y263D00KWC) | Tudo no 1Password |
| Stripe | ✅ Conectado (modo teste) | sk_test no 1Password + systemd |
| RapidAPI | ✅ Conta gb.ai.agent | Key no 1Password |
| AWS | ✅ IAM User sp-api-tobias + Role SpApiRole | Credentials em ~/.aws/ |
| Google Chrome | ✅ Headless no VPS | Config OpenClaw browser |
| Bright Data | ⚠️ Instável / billing suspende intermitentemente | API key no 1Password |
| Evolution API Cloudfy | ✅ WhatsApp Pedro + WhatsApp Kobe | API Key em 1Password |
| Bling ERP | ✅ Plano Mercúrio (Matriz + Filial) | OAuth tokens refresh automático |
| Supabase | ✅ Projeto Budamix Central + Budamix E-commerce | Service role key via env/credencial N8N |
| Slack | ✅ Read-only workspace GB Importadora | User token no 1Password |
| N8N Cloudfy | ✅ Workflows Blog Budamix; ⚠️ API key nova ainda não localizada no 1Password | Credentials internas no N8N + pendência de item `N8N Cloudfy API Key` |
| Perplexity API | ✅ Radar de pautas Blog Budamix | Credential N8N via 1Password |

## Skills

```
skills/
├── marketplace/
│   ├── marketplace-report/
│   ├── consolidado-financeiro/
│   ├── ml-competitor-analysis/
│   ├── ml-extrato/
│   ├── ml-ads/
│   ├── shopee-extrato/
│   ├── shopee-fees-rules/
│   ├── amazon-extrato/
│   ├── amazon-request-reviews/
│   └── inventory-management/
├── amazon-listing-creator/
├── shopee-listing-creator/
├── integracao/
│   └── instagram/
├── design/
│   ├── lovable-quality/
│   ├── superdesign/
│   ├── frontend-design-ultimate/
│   ├── shadcn-ui/
│   ├── report-design-system/
│   ├── excel-design-system/
│   └── excel-generation/
├── coaching-corrida/
└── financeiro/
    └── stripe-api/
```

## Agentes

| Agente | Especialidade | Workspace | Status |
|---|---|---|---|
| **main (Kobe)** | Orquestração, análise, memória | ~/.openclaw/workspace | ✅ L3 Estratégico |
| **Trader** | Marketplace — ML, Shopee, Amazon | shared/trader | ✅ Operacional |
| **Spark** | ADS — ML, Amazon, Meta | shared/spark | ✅ Operacional |
| **Builder** | Dev — MicroSaaS, APIs, UI | shared/builder | ✅ L2 Contributor |
| **Fisco** | Faturamento — NF-e, tributário | agents/fisco | ✅ Operacional |
| **RH** | Ponto, salários, compliance | agents/rh | ✅ Operacional |

## Status do Sistema (29/04/2026 23:30 BRT — Consolidação Diária)

### 🚨 Crítico
- **Fechamento março continua aberto:** ads spend real, consolidado novo e DRE semanal seguem pendentes.
- **Budamix Central Full:** analistas precisam cadastrar custos zerados em 30/04; depois rodar `sync-costs.py` e validar cobertura real.
- **Bling Filial** segue bloqueado/degradado; Matriz OK.
- **Google Ads OAuth do Spark** segue com `invalid_grant` e precisa novo refresh token.

### ⚠️ Importante
- **Social Studio** está em preview/branch `feat/social-studio-phase2` avançado até Fase 5; precisa QA autenticado e decisão de merge/deploy produção.
- **Blog Budamix Pipeline v2** está em produção; resta inspeção visual humana do post de teste e cleanup.
- **Budamix Central Full:** Etapa 2D `sku_mapping`, monitoramento Shopee e validação ML/Amazon seguem para 30/04.
- **Vercel Preview** precisa envs públicas Supabase configuradas no ambiente Preview ou passadas explicitamente pela CLI.
- **Vault-as-SSoT** segue em observação 48–72h após migração.

### ✅ Operacional
- **Vault como SSoT** validado: OpenClaw aponta para `/root/segundo-cerebro`, sync Mac↔GitHub↔VPS funcionando, workspace antigo deprecado.
- **Blog Budamix/Admin Pipeline v2** concluído em 7 fases e deployado em produção com `blog_pillars`, WF0/WF2/WF3/WF4 atualizados, LLM como diretor de arte criativo e Admin com pilares/pins manuais.
- **Budamix Central** agora tem repo GitHub privado e baseline/tag de rollback; módulo Full teve Shopee 3 contas restaurado e KPI Custo corrigido por filtro.
- **Social Studio** implementado em preview com persistência Supabase, UI real, geração de copy, editor manual e render PNG.

## Qualidade da Memória (Consolidação Diária 28/04)
- **sessions/2026-04-28.md:** consolidado com Vault-as-SSoT, Blog/Admin, N8N, Vercel, Social Studio e jobs Builder.
- **pending.md:** limpo; Supabase REST keys removida como pendência antiga após uso/validação REST controlada; novas pendências Blog/Social Studio/Vercel adicionadas; itens PCM001/SimulImport antigos movidos para Backlog Estagnado.
- **decisions.md:** atualizado com decisões de Vault SSoT, Blog assíncrono, Deploy Key, token Vercel `vcp_...`, Social Studio e Supabase migration controlada.
- **lessons.md:** atualizado com lições sobre HTTP síncrono, estado persistido, Vercel preview envs, Supabase migrations e secrets hardcoded no N8N.
- **shared/trader e shared/spark:** sessões 28/04 registradas como sem atividade delegada; pendências revalidadas.
- **shared/builder:** sessão 28/04 criada com entregas técnicas diretas no repo/N8N/Supabase e pendências atuais.
- **feedbacks:** registrados aprovações/rejeições de conteúdo/editorial/arquitetura do Blog e Social Studio.

## Timeline Recente
- **2026-04-29:** Blog Budamix Pipeline v2 fechado em produção (7 fases: `blog_pillars`, WF0 Perplexity, WF2 Sonnet 4.6 como diretor de arte, WF3 aspect ratio, WF4 validações, Admin com PillarSelect/AddPinManualDialog e validação E2E 6/6). Budamix Central ganhou baseline GitHub/tag rollback e refactor Full: Shopee 3 contas sincronizando, `sync-costs.py` corrigido, KPI Custo filtrável, Live Sales alinhado à Home por `v_daily_sales`. Social Studio seguiu em preview até render PNG, ainda sem merge produção.
- **2026-04-28:** Vault-as-SSoT validado 8/8 e workspace antigo deprecado; Blog Budamix/Admin corrigiu falso erro de geração, separou Em geração/Rascunhos, endureceu WF4 por estado real no Supabase e deployou via VPS/Vercel; Social Studio nasceu com SPEC, persistência Supabase, preview Vercel, geração de copy, editor manual, render PNG e wizard. Trader/Spark sem execução delegada; Builder sem RESULT.md novo.
- **2026-04-27:** Blog Budamix/Admin v2 virou a frente principal: WF4 Orchestrator, Admin Blog SPEC v2.0, WF0/WF2/WF4 corrigidos, fluxo final `gerando` → `em_edicao` → `preview` → `publicado`, UX de preview/editor, reset de pipeline, DNA editorial/visual/emocional aprovado, template de artigos encurtado e Amazon Request Review ajustado para 7–12 dias. GitHub do ecommerce destravado via PAT nas Observações do 1Password.
- **2026-04-26:** Integração Slack read-only criada, Google Sheets e WhatsApp histórico validados, e Blog Budamix avançou de placeholder para fundação no repo principal + N8N Draft Generator + WF0 Perplexity + Admin Blog Review em produção. No delta pós-consolidação, houve retrofit dos 3 artigos legados e SEO técnico deployado, com pendência de push GitHub/keys REST Supabase/N8N API key. Lições críticas registradas: Builder em repo privado precisa validar repo principal e deploy frontend exige smoke test renderizado amplo.
- **2026-04-25:** Pedro formalizou a diretriz de migração total para GPT-5.5 via ChatGPT Pro, com guardrails de backup, validação e rollback. Consolidação diária limpou o pending, reposicionou GPT-5.5 como prioridade atual e registrou ausência de atividade nova de Trader, Spark e Builder.
- **2026-04-23:** Consolidação diária silenciosa com revalidação integral do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção fiel do estado operacional do sistema.
- **2026-04-20:** Consolidação diária silenciosa com revalidação integral do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção do índice central sem mudanças estruturais artificiais.
- **2026-04-17:** Consolidação diária silenciosa com limpeza conservadora do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção do índice central sem mudanças estruturais artificiais.
- **2026-04-15:** Consolidação profunda quinzenal seguida de consolidação diária silenciosa. Pending principal foi limpo de forma conservadora, com itens antigos sem movimentação migrados para backlog estagnado. Trader, Spark e Builder fecharam o dia sem atividade nova e com sessões explícitas registradas.
- **2026-04-04:** Trader e Spark promovidos para GPT 5.4. Catálogo da Ana consolidado em CSV com 62 SKUs. Canggu conferido com 87/87 embeddings OK.
- **2026-04-06:** Planilha Excel de composição de kits entregue, arquivo `PRE PACKING LIST - GB25008.xlsx` recuperado do Gmail, base Ana avançada, seção Vibe incorporada ao SOUL e HIGH aplicado como default persistido para agentes/chats novos.
- **2026-04-07:** PCM001 lançado no Mercado Livre, nas 3 lojas Shopee e na Amazon BR com submission aceita e ASIN pendente. Playbook de restauração de contexto pós-troca de modelo reforçado. Kit de segundo cérebro avaliado como sólido para Claude Code local e incompleto para a camada OpenClaw/VPS.
- **2026-04-08:** Dia de baixa atividade operacional nova. Pending foi limpo de itens resolvidos já marcados, a skill `shopee-fees-rules` recebeu clarificações de abril/2026, e os alertas técnicos reais foram mantidos enxutos.
- **2026-04-09:** Dia de manutenção silenciosa. Sem execução nova relevante de Trader, Spark ou Builder. A consolidação reforçou o estado real das pendências e preservou a memória sem criar falsos avanços.
- **2026-04-14:** Nova manutenção silenciosa consolidada, com revalidação do pending principal, confirmação de ausência de atividade nova dos agentes especializados e permanência do bloqueio de autenticação GitHub para push/backup.

---

_Próximas ações: (1) fechar março com ads + consolidado + DRE semanal, (2) QA real Blog Budamix em produção, (3) QA/merge/deploy Social Studio, (4) remover service role hardcoded do WF4, (5) normalizar Google Ads OAuth e Bling Filial._

---
## Contexto
- [[openclaw/agents/kobe/memory/context/decisions|Decisões]]
- [[openclaw/agents/kobe/memory/context/lessons|Lições]]
- [[openclaw/agents/kobe/memory/context/people|Pessoas]]
- [[openclaw/agents/kobe/memory/context/business-context|Contexto do Negócio]]
- [[openclaw/agents/kobe/memory/projects/gb-importadora|GB Importadora]]
- [[openclaw/agents/kobe/memory/integrations/tools-map|Ferramentas e Integrações]]
- [[openclaw/agents/kobe/memory/integrations/telegram-map|Telegram — Kobe Hub]]
- [[openclaw/agents/kobe/memory/pending|Pendências]]

## Outputs dos Agentes
- [[openclaw/agents/kobe/shared/outputs/trader-platforms|Output Trader Platforms]]
- [[openclaw/agents/kobe/shared/outputs/trader-IDENTITY|Output Trader IDENTITY]]
- [[openclaw/agents/kobe/shared/outputs/trader-IDENTITY-v2|Output Trader IDENTITY v2]]
- [[openclaw/agents/kobe/shared/outputs/trader-SOUL|Output Trader SOUL]]
- [[openclaw/agents/kobe/shared/outputs/trader-AGENTS|Output Trader AGENTS]]
- [[openclaw/agents/kobe/shared/outputs/trader-MEMORY|Output Trader MEMORY]]
- [[openclaw/agents/kobe/shared/outputs/trader-decisions|Output Trader Decisions]]
- [[openclaw/agents/kobe/shared/outputs/trader-lessons|Output Trader Lessons]]
- [[openclaw/agents/kobe/shared/outputs/trader-pending|Output Trader Pending]]

## Workspaces dos Agentes
- [[openclaw/agents/kobe/shared/builder/MEMORY|Builder Workspace]]
- [[openclaw/agents/kobe/shared/fisco/MEMORY|Fisco Workspace]]
- [[openclaw/agents/kobe/shared/spark/MEMORY|Spark Workspace]]
- [[openclaw/agents/kobe/shared/rh/SOUL|RH Workspace]]
- [[openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao|Reforma Tributária (SimulImport)]]

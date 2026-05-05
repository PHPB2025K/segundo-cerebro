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

_Último update: 2026-05-04 23:30 BRT (consolidação diária)._

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

## Status do Sistema (04/05/2026 23:30 BRT — consolidação diária)

### 🚨 Crítico
- **Fechamento março continua aberto:** ads spend real, consolidado novo e DRE semanal seguem pendentes.
- **Budamix Central Estoque:** Fase 1.5 visual precisa validação do Pedro antes da Fase 2 de movimentações.
- **Marco 04/05 pós-refatoração:** pendências/inconformidades de abril removidas da fila ativa; Pedro vai regularizar abril diretamente. A partir daqui, só entram pendências novas ou recorrências materializadas após 04/05.
- **Google Ads OAuth do Spark** segue com `invalid_grant` e precisa novo refresh token.

### ⚠️ Importante
- **Amazon Ads:** após reset de 04/05, acompanhar apenas novos sinais/experimentos materializados de maio; abril fica como baseline histórico, não pendência ativa.
- **Social Studio Carrossel** Fase 1 está em produção com pipeline E2E validado; próxima decisão é Fase 4 publish IG ou Fase 5 hardening.
- **Blog Budamix Pipeline v2** está em produção; resta inspeção visual humana do post de teste e cleanup.
- **Budamix Central Full:** fechado com `zero_cost=0`; restam monitoramento Shopee 1E e validação defensiva ML/Amazon.
- **Vercel Preview** precisa envs públicas Supabase configuradas no ambiente Preview ou passadas explicitamente pela CLI.
- **Social Studio Carrossel:** 96 templates Paper viraram base do módulo; Fase 1 fechada em produção com custo real ~$0,31/carrossel.

### ✅ Operacional
- **Vault como SSoT** validado: OpenClaw aponta para `/root/segundo-cerebro`, sync Mac↔GitHub↔VPS funcionando, workspace antigo deprecado.
- **Blog Budamix/Admin Pipeline v2** concluído em 7 fases e deployado em produção com `blog_pillars`, WF0/WF2/WF3/WF4 atualizados, LLM como diretor de arte criativo e Admin com pilares/pins manuais.
- **Budamix Central** tem Full com custo 100% coberto e módulo Estoque dedicado (Full/Físico/Consolidado) deployado; capital total de estoque em torno de R$ 709k.
- **Social Studio** tem preview antigo funcional até render PNG, mas o novo módulo de Carrossel vira frente canônica após os templates Paper oficiais.

## Qualidade da Memória (Consolidação Diária 30/04)
- **sessions/2026-04-30.md:** consolidado com Budamix Central Full/Estoque, Canggu, RH/Ponto Certo, GitHub→Vercel e pendências finais.
- **pending.md:** limpo; removidas pendências resolvidas de cadastro de SKU base/2D; adicionadas Estoque Fase 2-4, Canggu, RH e validações reais.
- **decisões:** já registradas em `memory/context/decisoes/2026-04.md` para RH, Canggu, Ponto Certo, Vercel, Full/Estoque.
- **lessons.md:** atualizado com fonte canônica, guardrails determinísticos, mensagens interativas Evolution/Baileys, parser BR e SSoT de repo.
- **shared/trader/spark/builder/rh:** sessões 30/04 criadas; Builder/RH receberam decisões/lições e pendências atualizadas.
- **feedbacks:** registrada rejeição parcial de design do Estoque Fase 1 funcional porém abaixo do padrão visual.

## Timeline Recente
- **2026-05-04:** Dia de reset operacional pós-refatoração: Pedro mandou limpar pendências/inconformidades de abril da fila ativa; DRE abril corrigida para devolução estrita pós-recebimento (0,62%, ou 0,70% conservador com retorno em trânsito); Ponto Certo teve rota Traefik corrigida para `ponto.budamix.com.br` e ficou bloqueado apenas por DNS; RH WhatsApp foi bloqueado para proativos, reativado para inbound com guard `--allow-rh-reply`, `linkPreview:false` e reenvios autorizados para Yasmin/Leonardo; Budamix Live Sales mudou meta para R$15k; Social Studio Carrossel fechou Fase 1 em produção com pipeline E2E, export PNG/PDF e custo ~$0,31/carrossel.
- **2026-05-03:** Amazon Ads fechou a cobertura dos grupos finais de abril: Kits Microfibra executado com criação de Exact `pano microfibra` e escala de Auto; Abraçadeiras Nylon virou experimento de tração após confirmação de 24 un FBA no ASIN ativo; Redinha Frutas e Kit Jardinagem ficaram sem bid por falta de entrega/estrutura. Pedro consolidou o framework obrigatório de 3 blocos para Ads. No CC local, templates Budamix no Paper.design foram concluídos em 96 artboards (5 famílias × 3 paletas), com decisões de CLARA teal/fundo areia e limitação de shaders via MCP registrada.
- **2026-05-02:** Budamix Central/Live Sales teve meta diária alterada para R$20k em produção. Amazon Ads virou frente principal do dia: abril fechado usado como baseline, com cortes/harvesting/escala em 9 grupos (Potes Vidro, Canequinhas, Bambu, Canelada, Tulipa, Paris, Suporte Gamer, Jarra Medidora e Potes Redondos), D+7 pendente e Kits Microfibra aguardando aprovação. CC local instalou `epic-paper` e `video-use`, primeiro carrossel Profundo Budamix ficou 5/7 cards, e Guarani Sistemas teve estratégia de contestação/distrato com teto técnico R$7.002,30 sem reconhecimento de dívida.
- **2026-05-01:** Fechamento financeiro abril revisado: faturamento comercial R$405,8k separado de settlement R$355,0k; Ads reais validados (ML R$5.441,44, Shopee R$9.460, Amazon R$2.478,95) e DRE profissional clássica definida como padrão obrigatório. Fisco emitiu NFs internas abril Filial→Simples 000031–000033 (R$77.065,09) após reconciliação fiscal por SKU/componente, exclusão CK4742/Jarra Clink e validação IPI; PDFs/XMLs enviados à FOUR e financeiro. NFs de transferência 000649/000653 também enviadas à FOUR com ressalva sobre orientação Suellen v2.1.
- **2026-04-30:** Budamix Central Full fechado com `zero_cost=0` após planilha oficial, matching multi-fonte e filtro de fantasmas Amazon; módulo Estoque criado/refinado com capital total ~R$709k; Canggu consolidado em repo único/edge pipeline + mídia visível + guard ML; RH entrou em operação com mensagens inaugurais, polling anti-webhook-fail e Conversas RH; GitHub→Vercel auto-deploy ativado.
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

_Próximas ações: (1) operar a partir do marco 04/05 sem carregar abril como pendência ativa, (2) retomar Social Studio Carrossel Fase 0 com Paper MCP, (3) fechar março com ads + consolidado + DRE semanal, (4) QA real Blog Budamix e normalizar autenticações/rotas que ainda quebrarem após 04/05._

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

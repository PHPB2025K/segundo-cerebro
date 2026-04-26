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

_Último update: 2026-04-25 23:30 BRT (Consolidação Diária). Não duplica conteúdo — aponta pra onde está cada coisa._

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
| Supabase | ✅ Projeto Budamix Central | Service role key via env |

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

## Status do Sistema (25/04/2026 23:30 BRT — Consolidação Diária)

### 🚨 Crítico
- **Migração GPT-5.5 formalizada por Pedro:** agora é prioridade de infraestrutura, não backlog. Exige backup, autenticação Codex CLI, provider `openai-via-codex`, migração de todos os agentes/crons, validação completa e rollback se qualquer etapa falhar.
- **GitHub backup/push do workspace segue bloqueado por autenticação:** commit local pode funcionar, mas push remoto continua degradado até corrigir credencial.
- **Google `gog` degradado:** Sheets, Calendar e Gmail seguem com falhas de autenticação/token, afetando sync-costs, briefing e inbox cleanup.
- **Fechamento março continua aberto:** seguem pendentes ads spend, consolidado novo e mapeamento semanal do DRE.

### ⚠️ Importante
- **Monitor Ponto Semanal** continua degradado por timeout.
- **RH Monitor Ponto Saída** precisa correção de fallback/modelo.
- **Bling Token Refresh** continua exigindo validação operacional da Filial.
- **Links Amazon da base Ana** e pendências finais do PCM001 seguem abertas.

### ✅ Operacional
- O dia 25/04 teve manutenção noturna, criação da sessão diária e consolidação da diretriz GPT-5.5.
- Não houve atividade operacional relevante nova de Trader, Spark ou Builder no recorte do dia.
- Não houve job novo do Builder nem `RESULT.md` novo para consolidar em 25/04.
- `pending.md` principal foi relido integralmente e limpo: itens concluídos foram removidos, e a migração GPT-5.5 foi reposicionada como prioridade atual.
- Decisão GPT-5.5 e lição sobre não inferir áudio falho estão registradas nos arquivos core de memória.

## Qualidade da Memória (Consolidação Diária 25/04)
- **sessions/2026-04-25.md:** registra manutenção noturna, diretriz GPT-5.5, pendências abertas e consolidação diária final.
- **pending.md:** relido por completo, limpo de itens concluídos e corrigido para manter GPT-5.5 em prioridade imediata.
- **decisions.md:** decisão de migração total para GPT-5.5 já registrada com condição de rollback.
- **lessons.md:** lição tática registrada para não inferir conteúdo de áudio falho nem afirmar incidente/configuração sem validação real.
- **shared/trader, shared/spark e shared/builder:** sessões de 25/04 criadas explicitamente e pendings revalidados com timestamp novo.
- **feedbacks:** sem novo feedback formal a registrar em `memory/feedback/`.

## Timeline Recente
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

_Próximas ações: (1) executar migração GPT-5.5 com guardrails, (2) normalizar auth do GitHub e `gog`, (3) fechar março com ads + consolidado + DRE semanal, (4) fechar links Amazon da base Ana, (5) fechar pendentes finais do PCM001._

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

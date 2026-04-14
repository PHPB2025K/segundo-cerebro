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

_Último update: 2026-04-09 23:30 BRT (Consolidação Diária). Não duplica conteúdo — aponta pra onde está cada coisa._

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
|--------|--------------|-----------|--------|
| **main (Kobe)** | Orquestração, análise, memória | ~/.openclaw/workspace | ✅ L3 Estratégico |
| **Trader** | Marketplace — ML, Shopee, Amazon | shared/trader | ✅ Operacional |
| **Spark** | ADS — ML, Amazon, Meta | shared/spark | ✅ Operacional |
| **Builder** | Dev — MicroSaaS, APIs, UI | shared/builder | ✅ L2 Contributor |
| **Fisco** | Faturamento — NF-e, tributário | agents/fisco | ✅ Operacional |
| **RH** | Ponto, salários, compliance | agents/rh | ✅ Operacional |

## Status do Sistema (09/04/2026 23:30 BRT — Consolidação Diária)

### 🚨 Crítico
- **Fechamento março continua aberto:** faltam ads spend, consolidado novo e mapeamento semanal do DRE.
- **Validação ponta a ponta de zero Anthropic segue pendente:** a migração/limpeza avançou, mas a checagem final ainda está aberta no pending.
- **Links Amazon da base Ana seguem em aberto:** continuam como prioridade crítica do catálogo.

### ⚠️ Importante
- **Claude Contingency Guard** e **RH Monitor Ponto Saída** permanecem como os dois alertas técnicos reais mais relevantes.
- **Bling Token Refresh** continua com falha operacional da Filial e precisa validação real no Bling.
- **PCM001** continua dependendo de ASIN, peso final embalado, foto 9 e custos refinados para fechar o ciclo.

### ✅ Operacional
- O dia foi majoritariamente silencioso em execução nova dos agentes.
- Consolidação do dia reafirmou ausência de atividade operacional nova de Trader, Spark e Builder.
- Não houve job novo do Builder, nem nova sessão autônoma relevante dos agentes especializados.

## Qualidade da Memória (Consolidação Diária 09/04)
- **sessions/2026-04-09.md:** agora registra explicitamente a manutenção silenciosa do dia e a ausência de atividade nova dos agentes.
- **pending.md:** mantido fiel ao estado real, com timestamp novo e sem reabrir item já resolvido artificialmente.
- **shared/trader, shared/spark e shared/builder:** receberam sessões de 09/04 e pending atualizado para refletir dia sem operação nova.
- **decisions.md / lessons.md:** sem nova decisão permanente ou lição crítica adicional no dia.
- **feedbacks:** sem novo registro relevante do Pedro no dia.

## Timeline Recente
- **2026-04-04:** Trader e Spark promovidos para GPT 5.4. Catálogo da Ana consolidado em CSV com 62 SKUs. Canggu conferido com 87/87 embeddings OK.
- **2026-04-06:** Planilha Excel de composição de kits entregue, arquivo `PRE PACKING LIST - GB25008.xlsx` recuperado do Gmail, base Ana avançada, seção Vibe incorporada ao SOUL e HIGH aplicado como default persistido para agentes/chats novos.
- **2026-04-07:** PCM001 lançado no Mercado Livre, nas 3 lojas Shopee e na Amazon BR com submission aceita e ASIN pendente. Playbook de restauração de contexto pós-troca de modelo reforçado. Kit de segundo cérebro avaliado como sólido para Claude Code local e incompleto para a camada OpenClaw/VPS.
- **2026-04-08:** Dia de baixa atividade operacional nova. Pending foi limpo de itens resolvidos já marcados, a skill `shopee-fees-rules` recebeu clarificações de abril/2026, e os alertas técnicos reais foram mantidos enxutos.
- **2026-04-09:** Dia de manutenção silenciosa. Sem execução nova relevante de Trader, Spark ou Builder. A consolidação reforçou o estado real das pendências e preservou a memória sem criar falsos avanços.

---

_Próximas ações: (1) fechar março com ads + consolidado + DRE semanal, (2) validar zero Anthropic de ponta a ponta, (3) fechar links Amazon da base Ana, (4) destravar os pendentes finais do PCM001._

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

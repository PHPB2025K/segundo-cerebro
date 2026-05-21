---
title: "Fase 2 — Mapa de Conexões Propostas (densificação transversal)"
created: 2026-05-21
type: audit
status: proposal
tags:
  - audit
  - meta
  - knowledge-graph
  - densificacao
scope: 29 notas problemáticas (órfãs + ilhas) do LOTE A pós-limpeza
---

# Fase 2 — Mapa de Conexões Propostas

> **Modo:** proposta. Nenhum link aplicado ainda. Pedro revisa e marca quais aceita antes da Fase 3.
> **Princípio:** cada conexão sugerida cruza áreas DIFERENTES do vault (business ↔ projects ↔ skills ↔ memory ↔ automacoes). Sem inventar — só linkar quando há relação genuína.
> **Notação:** `tipo de conexão` segue convenção: **ref** (referência operacional), **pai/filho** (hierarquia), **autoridade** (fonte canônica), **dependência** (consome/usa), **executor** (quem executa), **tema** (mesmo conceito).

---

## Sumário

- **29 notas-fonte** analisadas
- **~110 conexões propostas** (média 3.8 por nota)
- Todas para notas **existentes** no vault (validei contra `notes_index.json`)
- Conexões reversas (in-link via "Notas relacionadas" do destino) **não** propostas aqui — fase 3 decide se vale duplicar

---

## ✅ Como aprovar

Para cada bloco, basta dizer:
- `aprovo` — aplica todas as conexões da nota
- `aprovo 1,3,4` — só as numeradas
- `reprovo` — pula a nota inteira
- `aprovo + adicionar X → Y` — eu aplico + adendo

---

## 📦 BLOCO A — automacoes/sops/ (4 notas)

### A1. [[automacoes/sops/abrir-nova-importacao]]
> SOP de abertura de container no GB Import Hub.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/gb-import-hub]] | **executor** | SOP opera diretamente sobre o sistema descrito na ficha (containers, finance_pagamentos, documents, vessel_tracking) |
| 2 | [[business/importacao/estrategia-fiscal-gb]] | **autoridade** | Documentos e NF gerados pela importação devem seguir a regra fiscal v2.1 (90/10, sem destaque ICMS, IPI suspenso) |
| 3 | [[skills/gb-import-hub/SKILL]] | **dependência** | Skill operacional que executa o SOP via API do Hub |
| 4 | [[knowledge/concepts/credenciais-map]] | **ref** | SERVICE_ROLE_KEY do Supabase `ocxvwwaaqqxecmzhfxhb` está mapeada lá |
| 5 | [[meta/mocs/MOC - Supabase Ecosystem]] | **tema** | Projeto Supabase do Import Hub aparece no MOC |

### A2. [[automacoes/sops/configurar-novo-agente-openclaw]]
> SOP de criação de novo agente OpenClaw com IDENTITY/SOUL/AGENTS.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[meta/mocs/MOC - Governanca OpenClaw]] | **autoridade** | MOC define leveling (L1/L2/L3/L4), heartbeats e protocolos — SOP segue essas regras |
| 2 | [[memory/context/business-context]] | **ref** | Visão panorâmica do business que o novo agente precisa absorver |
| 3 | [[knowledge/concepts/credenciais-map]] | **ref** | Credenciais 1Password vault OpenClaw que o agente vai usar |
| 4 | [[memory/context/people]] | **tema** | Agentes existentes listados na seção "Agentes AI" |

### A3. [[automacoes/sops/criar-listing-shopee]]
> SOP de criação de anúncio Shopee via API v2.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketplaces/_index]] | **pai** | Índice marketplaces inclui Shopee como canal e referencia EXPERT-SHOPEE knowledge file |
| 2 | [[meta/mocs/MOC - Taxas e Precificacao]] | **autoridade** | Tabela de faixas Shopee + armadilha R$80 documentada como regra de ouro |
| 3 | [[skills/shopee-listing-creator/SKILL]] | **dependência** | Skill citada no próprio SOP como entrypoint |
| 4 | [[openclaw/agents/trader/IDENTITY]] | **executor** | Trader é o agente responsável por marketplaces Shopee |
| 5 | [[memory/context/people]] | **ref** | Lucas é focal point Shopee (validações operacionais) |

### A4. [[automacoes/sops/deploy-ecommerce]]
> SOP de deploy budamix.com.br via Vercel CLI + 1Password.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/budamix-ecommerce]] | **executor** | SOP é o how-to da ficha do projeto |
| 2 | [[knowledge/concepts/credenciais-map]] | **ref** | Vercel Token + Supabase keys no 1Password vault OpenClaw |
| 3 | [[knowledge/concepts/stack-tecnico]] | **tema** | Vercel + Supabase + Mercado Pago aparecem na stack canônica |

---

## 📦 BLOCO B — automacoes/workflows/ (6 notas)

### B1. [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.4]]
> Briefing canônico (v2.4) — PDF oficial do Bling obrigatório.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[automacoes/workflows/pedidos-venda-gb-bling]] | **filho** | Workflow N8N que implementa o briefing (rota /api/fisco/pedidos-venda-gb) |
| 2 | [[projects/financeflow]] | **dependência** | FinanceFlow agente Fisco é quem cria o pedido no Bling Matriz |
| 3 | [[openclaw/agents/fisco/IDENTITY]] | **executor** | Fisco interpreta a mensagem com LLM + alias map e emite o pedido |
| 4 | [[knowledge/concepts/bling-api-v3-aprendizados]] | **tema** | API v3 do Bling tem comportamentos não-óbvios que afetam a obtenção do PDF |
| 5 | [[projects/mission-control]] | **ref** | Rota `/api/fisco/pedidos-venda-gb` está hospedada no Mission Control |

### B2. [[automacoes/workflows/budamix-whatsapp-ana]]
> Workflow N8N do agente Ana (Budamix AI Agent).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/canggu/canggu]] | **pai** | Canggu = o produto Ana; workflow N8N é uma das 16 nodes do pipeline |
| 2 | [[knowledge/concepts/stack-tecnico]] | **ref** | Evolution API + Claude AI + Supabase aparecem na stack |
| 3 | [[knowledge/concepts/credenciais-map]] | **ref** | Anthropic API key + Evolution API mapeadas |

### B3. [[automacoes/workflows/gmail-agente-inbox]]
> Workflow N8N de classificação automática de emails.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/gmail-organizer]] | **pai** | Ficha do projeto Gmail Organizer descreve este workflow |
| 2 | [[projects/n8n-builder]] | **ref** | Infraestrutura N8N que hospeda o workflow |
| 3 | [[knowledge/concepts/credenciais-map]] | **ref** | Anthropic API + Gmail OAuth mapeados |

### B4. [[automacoes/workflows/pedidos-venda-gb-bling]]
> Workflow N8N (T7WT4vGaRuWd0N0Q) — pedidos atacado via WhatsApp.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.4]] | **pai** | Briefing canônico que originou este workflow |
| 2 | [[projects/financeflow]] | **dependência** | FinanceFlow/Fisco é quem cria pedido real no Bling |
| 3 | [[openclaw/agents/fisco/IDENTITY]] | **executor** | Fisco interpreta + valida + cria |
| 4 | [[projects/mission-control]] | **ref** | Endpoint `mission.budamix.com.br/api/fisco/pedidos-venda-gb` |
| 5 | [[knowledge/concepts/bling-api-v3-aprendizados]] | **tema** | Aprendizados Bling aplicam ao endpoint de pedidos |

### B5. [[automacoes/workflows/running-coach-nova-atividade]]
> Workflow N8N do coach AI "Antonieta" (corrida).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/running-coach-ai]] | **pai** | Ficha do projeto descreve este pipeline de 24 nodes |
| 2 | [[projects/n8n-builder]] | **ref** | Infraestrutura N8N |
| 3 | [[knowledge/concepts/credenciais-map]] | **ref** | Strava OAuth + Claude API |

### B6. [[automacoes/workflows/vault-sync-mac-launchd]]
> launchd Mac que auto-pulla o vault a cada 60s.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[meta/mocs/MOC - Governanca OpenClaw]] | **tema** | Vault SSoT é parte da governança Kobe ↔ Mac |
| 2 | [[knowledge/concepts/stack-tecnico]] | **ref** | safe-write.sh sync + lockfile aparecem como parte da stack de devops |

---

## 📦 BLOCO C — business/ (5 notas)

### C1. [[business/financeiro/dre-abril-2026-u15-u44-v4]]
> DRE fechado abril/2026 (U15 + U44 v4).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/financeiro/_index]] | **pai** | Índice financeiro tem seção "DRE contínuo no vault" — esta nota se encaixa lá |
| 2 | [[skills/financeiro/dre-profissional-marketplace/SKILL]] | **dependência** | Skill que gera DREs profissionais multi-marketplace |
| 3 | [[meta/mocs/MOC - Taxas e Precificacao]] | **tema** | U44 (taxas marketplace) é o conceito central do MOC |
| 4 | [[business/marketplaces/_index]] | **ref** | Bases ML/Shopee/Amazon vêm dos canais listados |

### C2. [[business/marketing/marca/calendario-semana-04-a-10-maio-2026]]
> Calendário semanal de conteúdo Instagram (04-10/05).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **pai** | Índice da pasta marca já lista esta nota — mas não tem in-link reverso |
| 2 | [[business/marketing/marca/mapa-editorial]] | **autoridade** | Framework Schwartz aplicado vem do mapa editorial |
| 3 | [[business/marketing/marca/proposta-de-valor]] | **autoridade** | Inimigo comum "Improvisação Herdada" definido na proposta |
| 4 | [[projects/social-studio-reborn]] | **executor** | Publicador Instagram que vai distribuir os posts do calendário |

### C3. [[business/marketing/marca/mapa-editorial]]
> Framework Schwartz + Inimigo Comum aplicado ao calendário Budamix.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **pai** | Listado no índice mas sem in-link reverso |
| 2 | [[business/marketing/marca/proposta-de-valor]] | **autoridade** | Inimigo comum + avatar + posicionamento vêm da proposta |
| 3 | [[business/marketing/marca/calendario-semana-04-a-10-maio-2026]] | **filho** | Calendário concreto que aplica o framework |
| 4 | [[meta/mocs/MOC - Design Systems Budamix]] | **tema** | DNA visual aplicado por nível de consciência |

### C4. [[business/marketing/marca/planejamento-comunidade-vip]]
> Calendário do grupo WhatsApp Budamix VIP — Maio 2026.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **pai** | Listado no índice mas sem in-link reverso |
| 2 | [[business/marketing/marca/proposta-de-valor]] | **autoridade** | Posicionamento e inimigo comum fundamentam o tom da comunidade |
| 3 | [[memory/context/business-context]] | **ref** | Canal WhatsApp Budamix VIP aparece no contexto geral |

### C5. [[business/marketing/marca/proposta-de-valor]]
> Documento mestre — valor único, inimigo comum, mecanismo único.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **pai** | Listado no índice como "documento mestre" mas sem in-link reverso |
| 2 | [[business/marketing/marca/mapa-editorial]] | **filho** | Mapa editorial deriva da proposta |
| 3 | [[memory/context/business-context]] | **tema** | Empresa/marca/público compartilhados com o contexto geral |
| 4 | [[projects/budamix-ecommerce]] | **ref** | Loja própria é a expressão direta do posicionamento Budamix |

### C6. [[business/marketing/marca/recomendacao-stories]]
> SIMON — análise dos 6 formatos de stories aplicados à Budamix.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **pai** | Listado no índice mas sem in-link reverso |
| 2 | [[business/marketing/marca/proposta-de-valor]] | **autoridade** | Linhas editoriais (Bastidores Reais, etc.) vêm da proposta |
| 3 | [[projects/social-studio-reborn]] | **executor** | Stories publicados via Social Studio Reborn |

---

## 📦 BLOCO D — knowledge/concepts/ (3 notas)

### D1. [[knowledge/concepts/bling-api-v3-aprendizados]]
> Comportamentos não-óbvios da API v3 do Bling (NF transferência GB25010).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/financeflow]] | **dependência** | FinanceFlow consome Bling API v3 — aprendizados aplicam diretamente |
| 2 | [[openclaw/agents/fisco/IDENTITY]] | **executor** | Fisco é o agente que executa Bling — referenciado na nota |
| 3 | [[meta/mocs/MOC - Token Management]] | **tema** | OAuth Bling Matriz/Filial + refresh cron 5h |
| 4 | [[business/importacao/estrategia-fiscal-gb]] | **tema** | NF de transferência segue regras de transferência sem ICMS |
| 5 | [[knowledge/concepts/credenciais-map]] | **ref** | Bling API - Matriz/Filial mapeados no 1Password |

### D2. [[knowledge/concepts/cloudflare-urllib-user-agent]]
> Cloudflare bloqueia urllib do Python sem User-Agent custom.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[knowledge/concepts/stack-tecnico]] | **ref** | Python aparece na stack como linguagem para scripts |
| 2 | [[automacoes/workflows/budamix-whatsapp-ana]] | **ref** | Evolution Cloudfy (citada na nota) é a infra do workflow Ana |

### D3. [[knowledge/concepts/nano-banana-mcp-setup]]
> Setup do MCP Nano Banana (Gemini gpt-image).

> Nota: já linka pra credenciais-map, stack-tecnico, MOC Token Management. Falta uma conexão temática transversal:

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[skills/marketing/image-prompt-generator/SKILL]] | **tema** | Skill irmã de geração de imagens — Pedro usa em paralelo (Gemini vs gpt-image-2) |
| 2 | [[business/marketing/marca/_index]] | **ref** | Geração de imagens da marca Budamix passa por essas ferramentas |

---

## 📦 BLOCO E — memory/ (4 notas)

### E1. [[memory/context/writing-as-pedro]]
> Regra de tom para Kobe escrever em nome do Pedro.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[memory/context/business-context]] | **tema** | Regra de comunicação faz parte do contexto operacional |
| 2 | [[memory/context/people]] | **ref** | Pedro descrito como CEO; regra define o tom dele |
| 3 | [[openclaw/agents/kobe/IDENTITY]] | **executor** | Kobe é quem aplica essa regra |
| 4 | [[projects/canggu/canggu]] | **tema** | Ana também redige em nome do Pedro/marca — mesmo princípio |

### E2. [[memory/projects/compras-canecas]]
> Projeto de reposição de canecas Budamix (Yasmin/Lucas/Leonardo).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[memory/context/people]] | **ref** | 3 focal points (Yasmin/ML, Lucas/Shopee, Leonardo/Amazon) descritos no people |
| 2 | [[openclaw/agents/trader/IDENTITY]] | **executor** | Trader cruza dados marketplace para validar projeções da equipe |
| 3 | [[projects/budamix-central]] | **ref** | Estoque consolidado FULL+FÍSICO+TOTAL na home do Central |
| 4 | [[business/marketplaces/_index]] | **tema** | 3 canais ML/Shopee/Amazon mapeados como contexto |
| 5 | [[memory/projects/gestao-funcionarios]] | **tema** | Mesma equipe (Yasmin/Lucas/Leonardo) acompanhada semanalmente |

### E3. [[memory/projects/gestao-funcionarios]]
> Acompanhamento semanal Yasmin/Lucas/Leonardo via atas Slack.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[memory/context/people]] | **ref** | 3 focal points descritos no people |
| 2 | [[projects/ponto-certo]] | **complementar** | Separação clara: gestão de pessoas ≠ RH/Ponto Certo (explicitada na nota) |
| 3 | [[openclaw/agents/rh/IDENTITY]] | **complementar** | RH cobre ponto/jornada; esta frente cobre performance |
| 4 | [[memory/projects/compras-canecas]] | **tema** | Mesma equipe e mesmo canal Slack |

### E4. [[memory/projects/mission-control]]
> Memória do projeto Mission Control (painel OpenClaw).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/mission-control]] | **pai** | Ficha completa do projeto (frontend, PRDs, módulos) |
| 2 | [[meta/mocs/MOC - Governanca OpenClaw]] | **tema** | Painel visual da governança OpenClaw |
| 3 | [[automacoes/workflows/pedidos-venda-gb-bling]] | **filho** | Consome a rota `/api/fisco/pedidos-venda-gb` que vive no Mission |

---

## 📦 BLOCO F — projects/ (1 nota — outras já têm in-links)

### F1. [[projects/canggu/frontend]]
> Frontend de Canggu (Vite + React 19 + Zustand) — auditoria forense 22/04.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[projects/canggu/canggu]] | **pai** | Ficha-pai do projeto |
| 2 | [[knowledge/concepts/stack-tecnico]] | **tema** | Vite/React/Zustand/Tailwind aparecem na stack canônica |
| 3 | [[projects/canggu/debitos-tecnicos]] | **ref** | Bug #14 citado na própria nota |

---

## 📦 BLOCO G — skills/*/SKILL.md (3 notas)

### G1. [[skills/design/epic-paper/SKILL]]
> Skill para criar designs no Paper.design via MCP.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **dependência** | Skill é usada para criar carrosséis Budamix conforme DNA visual |
| 2 | [[meta/mocs/MOC - Design Systems Budamix]] | **autoridade** | Paleta v2.1 Floresta com Faísca + tokens Budamix são input da skill |
| 3 | [[business/marketing/marca/templates-carrossel-paper]] | **filho** | Templates concretos criados no Paper que esta skill manipula |

### G2. [[skills/financeiro/dre-profissional-marketplace/SKILL]]
> Skill para gerar DRE gerencial multi-marketplace.

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/financeiro/_index]] | **pai** | DRE pertence ao domínio financeiro |
| 2 | [[business/financeiro/dre-abril-2026-u15-u44-v4]] | **filho** | Output concreto gerado pela skill |
| 3 | [[meta/mocs/MOC - Taxas e Precificacao]] | **autoridade** | Taxas e fees por marketplace são input para U44 |
| 4 | [[openclaw/agents/trader/IDENTITY]] | **executor** | Trader é o agente que aplica esta skill |

### G3. [[skills/marketing/image-prompt-generator/SKILL]]
> Skill geradora de prompts gpt-image-2 (OpenAI).

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[business/marketing/marca/_index]] | **dependência** | Geração de imagens Budamix segue paleta+DNA da marca |
| 2 | [[meta/mocs/MOC - Design Systems Budamix]] | **autoridade** | Tokens visuais aplicáveis aos prompts |
| 3 | [[knowledge/concepts/nano-banana-mcp-setup]] | **tema** | Ferramenta irmã (Gemini); decisão entre os dois é caso-a-caso |
| 4 | [[knowledge/concepts/credenciais-map]] | **ref** | OpenAI API key mapeada |
| 5 | [[projects/social-studio-reborn]] | **consumidor** | Publicador Instagram pode usar prompts gerados para criar assets |

---

## 📦 BLOCO H — meta/audits/ (1 nota)

### H1. [[meta/audits/auditoria-vault-2026-05-20]]
> Este relatório de auditoria (criado nesta sessão).

> Já tem 65+ out-links (lista todas as órfãs). Falta um in-link de hub:

| # | Conectar a | Tipo | Justificativa |
|---|---|---|---|
| 1 | [[meta/audits/auditoria-conexoes-2026-04-10]] | **predecessor** | Auditoria anterior do vault (10/04) — esta é a sucessora |
| 2 | [[meta/mocs/MOC - Governanca OpenClaw]] | **tema** | Governança do vault entra na governança operacional |

---

## 🚫 Excluído desta proposta

- **[[projects/budamix-central-estoque-modulo/sync-physical-inventory-v3-with-items.py.patch]]** — é um patch de código sem yaml, já archived. Não vale densificar.

---

## 📊 Resumo numérico

| Bloco | Notas-fonte | Conexões propostas |
|---|---:|---:|
| A — automacoes/sops | 4 | 17 |
| B — automacoes/workflows | 6 | 22 |
| C — business | 6 | 22 |
| D — knowledge | 3 | 10 |
| E — memory | 4 | 16 |
| F — projects | 1 | 3 |
| G — skills | 3 | 12 |
| H — meta/audits | 1 | 2 |
| **TOTAL** | **28** | **104** |

---

## ⚖️ Princípios respeitados

- ✅ Nenhuma conexão para nota inexistente (validado contra `notes_index.json`)
- ✅ Toda conexão entre áreas DIFERENTES do vault (não densifico dentro da mesma pasta sem razão)
- ✅ Toda conexão tem justificativa específica — não há "estes conceitos podem se relacionar"
- ✅ Não proponho aplicar em pasta arquivada (`_archive/`, status: archived)
- ✅ Não toco em notas do GRUPO 2 (skill-internal/autogerado/openclaw agents)

---

_Gerado em 2026-05-21 pela Fase 2 da skill obsidian-vault-manager._

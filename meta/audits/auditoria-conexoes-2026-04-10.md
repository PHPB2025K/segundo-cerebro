---
title: "auditoria conexoes 2026 04 10"
created: 2026-04-14
type: audit
status: active
tags:
  - meta/audit
---

# Auditoria de Conexões do Vault — 10/04/2026

> Auditoria exaustiva de 347 notas do segundo cérebro.
> Todas as 4 áreas lidas e analisadas semanticamente.
> Conexões baseadas exclusivamente no conteúdo escrito nas notas.

---

## 1. Estatísticas Gerais

| Métrica | Valor |
|---------|-------|
| Total de notas | 347 |
| Wikilinks existentes | ~397 |
| Alvos únicos de link | 61 |
| Notas órfãs (nunca linkadas) | 306 (88%) |
| Tags semânticas | ~15 (maioria são hex colors de CSS) |
| Notas vazias | 1 (`Sem título.md`) |

### Distribuição por área

| Área | Notas | % |
|------|-------|---|
| Skills | 151 | 43% |
| Agents/kobe/shared | ~117 | 34% |
| Agents core (kobe+trader+spark+builder+fisco+rh) | 51 | 15% |
| Memory (context+sessions+projects) | 15 | 4% |
| Root (CLAUDE, PROPAGATION, Sem título) | 3 | 1% |
| .claude | 1 | <1% |

### Estado de conectividade

O vault é **altamente desconectado**. Apenas 41 notas recebem algum link. Os hubs são:
- openclaw/agents/kobe/IDENTITY` (57 links recebidos)
- openclaw/agents/builder/IDENTITY` (49)
- openclaw/agents/trader/IDENTITY` (40)
- openclaw/agents/spark/IDENTITY` (40)
- openclaw/agents/fisco/IDENTITY` (22)
- openclaw/agents/rh/IDENTITY` (14)
- `skills/spreadsheet-pricing/SKILL` (13)

A vasta maioria das 151 skills e ~80 arquivos de memória/sessão dos agentes não tem NENHUM link apontando para elas.

---

## 2. Nota vazia / candidata a exclusão

| Nota | Status | Ação sugerida |
|------|--------|---------------|
| `Sem título.md` (raiz) | Arquivo vazio, 1 linha em branco | Excluir |

---

## 3. Inconsistências detectadas

| Local A | Local B | Inconsistência |
|---------|---------|----------------|
| openclaw/agents/fisco/USER` | openclaw/agents/fisco/SOUL` | USER diz "Simples Nacional"; SOUL detalha Lucro Presumido para Matriz/Filial |
| openclaw/agents/rh/USER` | openclaw/agents/rh/IDENTITY` | USER diz "~4 funcionários CLT"; IDENTITY lista 8 ativos |
| openclaw/agents/trader/TOOLS` | `skills/spreadsheet-pricing/SKILL` | TOOLS referencia planilha antiga (`1u74aCdH...`); skill deveria usar nova (`1dUoZtrv...`) |
| `skills/operations/inventory-management/SKILL` | `skills/spreadsheet-pricing/SKILL` | inventory-management referencia planilha antiga; spreadsheet-pricing deveria ter novo SSID |
| `memory/context/deadlines` | `memory/context/pendencias` | Deadlines NÃO lista GB25009 (16/04, R$72k) nem GB25011 (11/04, R$60k) — ambos críticos em pendências |
| openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo` | Frontend Ponto Certo | TOLERANCE_MINUTE=40 no frontend vs 10 no backend (bug pendente) |
| `skills/spreadsheet-pricing/rules/format-rules` | `skills/amazon-listing-creator/rules/field-formats` | NCM com pontos na planilha (4411.12.10) vs sem pontos na Amazon (44111210) — risco de erro |

---

## 4. Conexões descobertas por tipo

### 4.1 TEMÁTICA DIRETA — notas do mesmo assunto sem link

| # | Nota A | Nota B | Conexão |
|---|--------|--------|---------|
| T1 | `memory/projects/gb-import-hub-schema` | `memory/projects/gb-import-hub-edge-functions-map` | Mesmo projeto GB Import Hub: schema define tabelas, edge-functions-map define as 17 funções que operam sobre elas |
| T2 | `memory/projects/gb-import-hub-schema` | `memory/projects/gb-import-hub-reconnection-plan` | Reconnection-plan depende do schema para saber quais hooks acessam quais tabelas; RLS de conferencias_numerario exige migração de auth |
| T3 | `memory/projects/gb-import-hub-edge-functions-map` | `memory/projects/gb-import-hub-reconnection-plan` | Os dois formam o blueprint completo para reconectar frontend ao Supabase externo |
| T4 | `skills/marketplace/amazon-extrato/SKILL` | `skills/marketplace/ml-extrato/SKILL` | Formato unificado de 23 colunas; nomenclatura cross-plataforma padronizada |
| T5 | `skills/marketplace/amazon-extrato/SKILL` | `skills/marketplace/shopee-extrato/SKILL` | Idem — 23 colunas padronizadas para consolidação |
| T6 | `skills/marketplace/ml-extrato/SKILL` | `skills/marketplace/shopee-extrato/SKILL` | Idem |
| T7 | `skills/marketplace/amazon-fees-rules/SKILL` | `skills/marketplace/ml-fees-rules/SKILL` | Ambos têm cron "Fees Monitor" toda quarta 10h SP; base para precificação |
| T8 | `skills/marketplace/amazon-fees-rules/SKILL` | `skills/marketplace/shopee-fees-rules/SKILL` | Idem |
| T9 | `skills/marketplace/ml-fees-rules/SKILL` | `skills/marketplace/shopee-fees-rules/SKILL` | Idem |
| T10 | `skills/design/animated-financial-display/SKILL` | `skills/design/financial-design-systems/SKILL` | Complementares: animated-display (números animados) + financial-viz (charts); ambos usam mesma paleta (green=gains, red=losses) |
| T11 | `skills/design/excel-design-system` | `skills/excel-generation/SKILL` | Design system fornece paleta/fontes; excel-generation implementa com openpyxl |
| T12 | `skills/design/shadcn-ui/SKILL` | `skills/design/frontend-design-ultimate/SKILL` | Ambos cobrem shadcn/ui + Tailwind; frontend-design-ultimate é mais prescritivo (anti-slop) |
| T13 | `skills/design/shadcn-ui/SKILL` | `skills/design/lovable-quality/SKILL` | Lovable-quality exige design system first com shadcn/ui tokens; shadcn-ui é o guia de uso |
| T14 | openclaw/agents/fisco/HEARTBEAT` | openclaw/agents/rh/HEARTBEAT` | Ambos vazios — únicos agentes sem heartbeat configurado apesar de terem crons críticos |
| T15 | openclaw/agents/kobe/shared/trader/memory/context/marketplace-algorithms` | `skills/marketplace/marketplace-optimization/SKILL` | Mesmo conhecimento (ranking ML/Amazon/Shopee) em dois locais: memória do Trader vs skill operacional |

### 4.2 CONCEITUAL / ANALÓGICA — domínios diferentes, mesmo padrão

| # | Nota A | Nota B | Padrão compartilhado |
|---|--------|--------|---------------------|
| C1 | openclaw/agents/kobe/shared/builder/SOUL` (regra: "design system first") | openclaw/agents/kobe/shared/rh/SOUL` (regra: "chunks ≤3 linhas, tom casual") | **Linguagem de output como pré-requisito** — Builder exige design tokens antes de código, RH exige formato de comunicação antes de mensagem. Dois agentes completamente distintos com a mesma preocupação: COMO comunicar, não só O QUE |
| C2 | openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-30` (crash OOM 4 jobs) | openclaw/agents/kobe/HEARTBEAT` (monitorar VPS disco/memória) | **Limite físico como regra de governança** — 3.8GB RAM virou regra "max 2 jobs"; HEARTBEAT monitora o mesmo recurso de forma preventiva |
| C3 | `skills/superpowers/systematic-debugging/SKILL` (Iron Law: no fixes without root cause) | `skills/superpowers/verification-before-completion/SKILL` (Iron Law: no claims without evidence) | **Disciplina anti-atalho** — ambos resistem à mesma tentação (pular etapa sob pressão); ambos usam linguagem imperativa para prevenir racionalização |
| C4 | `skills/superpowers/test-driven-development/SKILL` (Red-Green-Refactor para código) | `skills/superpowers/writing-skills/SKILL` (Red-Green-Refactor para documentação de skills) | **TDD como padrão universal** — TDD aplicado a código E a documentação; mesma estrutura transferida entre domínios |
| C5 | openclaw/agents/kobe/shared/rh/SOUL` (modo supervisão: toda msg → notificação Pedro) | openclaw/agents/kobe/shared/TEAM` (L1-L4: nenhum agente fala direto com Pedro) | **Governança com exceção humana** — RH é o único agente com canal direto a Pedro (TIPO D), justificado pelo impacto humano; exceção à hierarquia padrão |
| C6 | `skills/marketplace/shopee-fees-rules/SKILL` (armadilha de fronteira R$79,99→R$80) | `skills/marketplace/ml-fees-rules/SKILL` (tabela variável 232 combinações peso×preço) | **Descontinuidades de preço como armadilha** — ambas plataformas têm pontos de inflexão onde +R$0,01 no preço causa salto desproporcional no custo |

### 4.3 CAUSAL — Nota A descreve causa, Nota B descreve efeito

| # | Causa (Nota A) | Efeito (Nota B) | Relação |
|---|---------------|-----------------|---------|
| CA1 | `memory/sessions/2026-04-06` (migração GPT 5.4, fallback = mesmo provider) | `memory/sessions/2026-04-07` (fix fallback cascata, FallbackSummaryError horas) | Migração criou o bug → sessão seguinte diagnosticou e corrigiu |
| CA2 | openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-30` (OOM: 4 jobs simultâneos) | openclaw/agents/kobe/shared/builder/SOUL` (regra inviolável: max 2 jobs) | Crash físico → virou regra de governança permanente |
| CA3 | openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-24` (Spark Ads v1 sem design system = amador) | openclaw/agents/kobe/shared/builder/memory/context/lessons` (lição: design system first) | Entrega ruim → lição estratégica permanente |
| CA4 | openclaw/agents/kobe/AGENTS` (incidente 25/03: Kobe respondeu WhatsApp sem autorização) | openclaw/agents/kobe/SOUL` (regra INVIOLÁVEL: dmPolicy "open" JAMAIS) | Incidente com cliente Alexandre Novaes → regra de segurança mais forte do sistema |
| CA5 | openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-03` (relatório março com Shopee parcial) | openclaw/agents/kobe/shared/trader/memory/context/decisions` (5 regras QA financeiro) | Entrega com dados incompletos → 5 regras de validação |

### 4.4 COMPLEMENTAR — Nota A tem a pergunta, Nota B tem a resposta

| # | Pergunta (Nota A) | Resposta (Nota B) | Relação |
|---|-------------------|-------------------|---------|
| CO1 | `memory/context/pendencias` ("22 SKUs MELI com margem negativa — revisar preços") | `skills/marketplace/ml-fees-rules/SKILL` (tabela completa de taxas ML 2026) | Pendência pede revisão → skill tem as regras exatas para recalcular |
| CO2 | `memory/context/pendencias` ("Custos Full pendentes de integração Col N") | `memory/context/decisoes/2026-04` (decisão 10/04: custos Full via Mercado Pago shp_fulfillment) | Pendência pede dados → decisão documenta como obtê-los |
| CO3 | openclaw/agents/kobe/shared/simulimport/sprint2-roadmap` ("reforma tributária no simulador") | openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao` (fórmulas Python exatas CBS/IBS) | Roadmap pede feature → documento técnico tem as fórmulas prontas |
| CO4 | openclaw/agents/builder/memory/pending` ("Atlas Finance relatórios quebrados") | openclaw/agents/kobe/shared/fisco/SOUL` (modelo fiscal completo com distribuição 90/10) | Builder precisa de regras fiscais → Fisco tem o modelo completo |
| CO5 | openclaw/agents/spark/memory/pending` ("Google Ads Developer Token pendente") | `skills/marketing/google-ads/SKILL` (skill completa aguardando token) | Pendência bloqueia → skill inteira já construída, só falta o token |

### 4.5 ENTIDADE COMPARTILHADA — mesma entidade em notas desconectadas

| # | Entidade | Notas que a mencionam sem se linkar |
|---|----------|-------------------------------------|
| E1 | **Planilha de estoque (Google Sheets)** | `skills/spreadsheet-pricing/SKILL`, `skills/operations/inventory-management/SKILL`, `skills/update-ml-return-rates/SKILL`, openclaw/agents/kobe/shared/outputs/trader-platforms`, openclaw/agents/trader/TOOLS` |
| E2 | **Supabase** (como infra cross-agent) | openclaw/agents/kobe/shared/builder/memory/context/stack`, openclaw/agents/kobe/shared/fisco/skills/bling-nfe/SKILL`, openclaw/agents/kobe/shared/trader/memory/context/platforms`, openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-24`, openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo` |
| E3 | **Evolution API** | openclaw/agents/kobe/shared/rh/SOUL`, openclaw/agents/kobe/shared/rh/memory/context/lessons`, openclaw/agents/kobe/shared/spark/SOUL`, `skills/whatsapp-ultimate/SKILL`, openclaw/agents/kobe/TOOLS` |
| E4 | **Bright Data** | `skills/marketplace/ml-competitor-analysis/SKILL`, openclaw/agents/kobe/shared/trader/memory/context/platforms`, `memory/context/pendencias` |
| E5 | **1Password vault "OpenClaw"** | openclaw/agents/kobe/AGENTS`, openclaw/agents/trader/TOOLS`, openclaw/agents/spark/TOOLS`, `skills/marketplace/ml-competitor-analysis/SKILL`, `skills/financeiro/stripe-api/SKILL`, `skills/marketing/meta-ads/SKILL` |
| E6 | **Bidspark** | openclaw/agents/builder/memory/projects/bidspark`, openclaw/agents/spark/SOUL`, openclaw/agents/spark/memory/context/decisions`, openclaw/agents/builder/SOUL`, openclaw/agents/builder/memory/context/lessons` |
| E7 | **TTD 409 SC** | openclaw/agents/kobe/shared/fisco/SOUL`, openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao`, openclaw/agents/fisco/SOUL`, openclaw/agents/kobe/shared/fisco/skills/distribution/SKILL` |
| E8 | **NCM** | `skills/amazon-listing-creator/reference/known-product-types`, openclaw/agents/kobe/shared/simulimport/ncm-database-spec`, `skills/gb-import-hub/SKILL`, `skills/spreadsheet-pricing/rules/format-rules` |
| E9 | **CNPJ × Marketplace mapping** | openclaw/agents/kobe/shared/trader/memory/context/decisions`, openclaw/agents/kobe/shared/fisco/SOUL`, openclaw/agents/kobe/shared/fisco/skills/distribution/SKILL` |
| E10 | **Ponto Certo** | openclaw/agents/rh/IDENTITY`, openclaw/agents/rh/SOUL`, openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo`, openclaw/agents/kobe/shared/builder/memory/projects/ponto-certo` |

### 4.6 METODOLÓGICA — mesmo framework/processo

| # | Nota A | Nota B | Framework compartilhado |
|---|--------|--------|------------------------|
| M1 | openclaw/agents/trader/AGENTS` (checklist pré-entrega 9 itens) | openclaw/agents/spark/AGENTS` (checklist pré-entrega) | Mesmo protocolo de QA adaptado para domínios diferentes (marketplace vs ads) |
| M2 | openclaw/agents/kobe/shared/builder/AGENTS` (BRIEFING-TEMPLATE.md 9 seções) | openclaw/agents/kobe/shared/fisco/AGENTS` (spawn com briefing) | Mesmo padrão de briefing para spawn de sessões de agentes |
| M3 | `skills/superpowers/brainstorming/SKILL` → `skills/superpowers/writing-plans/SKILL` → `skills/superpowers/subagent-driven-development/SKILL` → `skills/superpowers/requesting-code-review/SKILL` → `skills/superpowers/finishing-a-development-branch/SKILL` | Pipeline completo de desenvolvimento | 5 skills que formam um pipeline linear mas NÃO se linkam via wikilinks |
| M4 | openclaw/agents/kobe/HEARTBEAT` | openclaw/agents/trader/HEARTBEAT` | Mesmo formato HEARTBEAT (verificações + regra urgente/importante/nada) |
| M5 | openclaw/agents/trader/memory/context/decisions` + openclaw/agents/spark/memory/context/decisions` + openclaw/agents/builder/memory/context/decisions` | Três arquivos de decisões permanentes | Padrão idêntico de decisions.md — auditoria conjunta garantiria coerência |

### 4.7 META-PADRÃO — temas recorrentes em 3+ notas que merecem MOC

| # | Meta-padrão | Notas onde aparece | Sugestão |
|---|-------------|-------------------|----------|
| MP1 | **Gestão de tokens OAuth como fragilidade sistêmica** | openclaw/agents/kobe/shared/fisco/memory/context/lessons` (bug redirect_uri, dual-sync), openclaw/agents/kobe/shared/trader/memory/context/lessons` (validar tokens antes de relatório), openclaw/agents/kobe/shared/spark/memory/context/lessons` (Meta token 60d), openclaw/agents/trader/HEARTBEAT` (verificar validade), openclaw/agents/spark/HEARTBEAT` (token Meta expirando) | Criar MOC: `Token Management` — centralizar protocolo de gestão de tokens cross-agent |
| MP2 | **Formato unificado 23 colunas (extratos financeiros)** | `skills/marketplace/amazon-extrato/SKILL`, `skills/marketplace/ml-extrato/SKILL`, `skills/marketplace/shopee-extrato/SKILL`, `skills/marketplace/consolidado-financeiro/SKILL`, nomenclaturas unificadas (3 arquivos) | Criar MOC: `Extratos Financeiros` — hub linkando os 3 extratos + consolidado + nomenclatura unificada |
| MP3 | **Pipeline de desenvolvimento Superpowers** | `skills/superpowers/brainstorming/SKILL`, `writing-plans`, `subagent-driven-development`, `executing-plans`, `requesting-code-review`, `receiving-code-review`, `finishing-a-development-branch`, `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `dispatching-parallel-agents`, `using-superpowers`, `writing-skills` | Criar MOC: `Superpowers Pipeline` — mapa de como as 14 skills se conectam em sequência |
| MP4 | **Regras de taxas por marketplace** | `skills/marketplace/amazon-fees-rules/SKILL`, `skills/marketplace/ml-fees-rules/SKILL`, `skills/marketplace/shopee-fees-rules/SKILL`, `skills/spreadsheet-pricing/SKILL`, `skills/marketplace/marketplace-optimization/SKILL` | Criar MOC: `Taxas e Precificação` — hub comparativo das 3 plataformas + planilha |
| MP5 | **Design systems (3 flavors)** | `skills/design/report-design-system/SKILL` (HTML dark mode), `skills/design/excel-design-system` (Excel dark mode), `skills/design/lovable-quality/SKILL` (frontend tokens), `skills/design/financial-design-systems/SKILL` (charts), `skills/design/animated-financial-display/SKILL` (números), `skills/design/frontend-design-ultimate/SKILL` (anti-slop) | Criar MOC: `Design Systems Budamix` — hub unificando os 3 design systems (HTML, Excel, Frontend) |
| MP6 | **Supabase como infraestrutura convergente** | Usado por Builder (stack), Fisco (tokens), Trader (cache marketplace), Spark (sync-ads), RH (Ponto Certo), Ana (embeddings), GB Import Hub, Budamix Central | Criar MOC: `Supabase Ecosystem` — mapa de todos os projetos Supabase e quem usa o quê |
| MP7 | **Leveling e governança de agentes AI** | openclaw/agents/kobe/shared/TEAM`, openclaw/agents/kobe/shared/lessons/reviews/builder-2026-03-26`, `trader-2026-03-26`, `spark-2026-03-26`, todos os AGENTS.md (6), todos os HEARTBEAT.md (6) | Criar MOC: `Governança OpenClaw` — hub de leveling, reviews, heartbeats e protocolos |
| MP8 | **Criação de listings por marketplace** | `skills/amazon-listing-creator/SKILL`, `skills/shopee-listing-creator/SKILL`, `skills/marketplace/marketplace-optimization/SKILL`, `skills/spreadsheet-pricing/SKILL` | Criar MOC: `Listing Pipeline` — hub do fluxo: pesquisa → criação → planilha → monitoramento |

---

## 5. Ranking das conexões mais valiosas

Ordenadas por impacto potencial no vault:

| Rank | Conexão | Tipo | Impacto |
|------|---------|------|---------|
| 1 | **Pipeline Superpowers** (14 skills sem links entre si) | Metodológica (MP3) | Altíssimo — pipeline completo de desenvolvimento invisível no graph |
| 2 | **Extratos financeiros 23 colunas** (3 extratos + consolidado) | Meta-padrão (MP2) | Alto — fluxo financeiro central da operação sem conexão visual |
| 3 | **Taxas × Precificação** (3 fees-rules + spreadsheet-pricing) | Meta-padrão (MP4) | Alto — base de toda decisão de preço, desconectada |
| 4 | **deadlines.md vs pendencias.md** (GB25009/GB25011 ausentes) | Inconsistência | Alto — prazos financeiros críticos não aparecem em deadlines |
| 5 | **Bidspark ↔ Spark** (projeto + agente visam eliminar R$9k/mês) | Entidade (E6) | Alto — conexão estratégica central invisível |
| 6 | **GB Import Hub** (3 docs do mesmo projeto sem links) | Temática (T1-T3) | Médio — blueprints complementares desconectados |
| 7 | **Trader algorithms ↔ marketplace-optimization** (conhecimento duplicado) | Temática (T15) | Médio — mesmo conteúdo em dois locais sem referência cruzada |
| 8 | **Token OAuth cross-agent** (3 agentes com o mesmo problema) | Meta-padrão (MP1) | Médio — fragilidade sistêmica não visível no graph |
| 9 | **CNPJ × Marketplace** (Trader + Fisco operam sobre mesma estrutura) | Entidade (E9) | Médio — dependência fiscal-comercial invisível |
| 10 | **SimulImport ↔ Reforma Tributária ↔ Fisco** | Complementar (CO3) | Médio — conhecimento fiscal do Fisco deveria alimentar SimulImport |

---

## 6. Notas órfãs com sugestões de link

### Alta prioridade (notas importantes sem nenhum link recebido)

| Nota órfã | Deveria ser linkada por | Razão |
|-----------|------------------------|-------|
| `memory/context/pendencias` | `memory/context/decisoes/2026-04`, `memory/projects/_index` | Fonte de verdade de pendências — decisões resolvem pendências, projetos geram pendências |
| `memory/context/deadlines` | `memory/context/pendencias`, `memory/context/business-context` | Prazos deveriam ser referenciados pelas pendências e pelo contexto geral |
| `memory/sessions/2026-04-09` | `memory/context/decisoes/2026-04` | Sessão gerou 8 decisões registradas |
| `memory/sessions/2026-04-10` | `memory/context/decisoes/2026-04` | Sessão gerou 6 decisões registradas |
| `memory/projects/shopee-porta-copos-analise` | `memory/context/pendencias`, `skills/shopee-listing-creator/SKILL` | Análise estratégica de mercado que fundamenta pendências Shopee |
| `PROPAGATION` | `CLAUDE` | Protocolo de propagação referenciado pelo CLAUDE como sistema operacional |
| openclaw/agents/kobe/CHANGELOG` | openclaw/agents/kobe/IDENTITY`, openclaw/agents/kobe/MEMORY` | Histórico cronológico do sistema — deveria ser linkado pela identidade e memória |

### Média prioridade (documentação técnica)

| Nota órfã | Deveria ser linkada por |
|-----------|------------------------|
| `memory/projects/gb-import-hub-edge-functions-map` | `memory/projects/gb-import-hub-schema` |
| `memory/projects/gb-import-hub-reconnection-plan` | `memory/projects/gb-import-hub-schema` |
| openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao` | openclaw/agents/kobe/shared/simulimport/sprint2-roadmap` |
| openclaw/agents/kobe/shared/simulimport/ncm-database-spec` | openclaw/agents/kobe/shared/builder/memory/projects/simulaimport` |
| openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo` | openclaw/agents/kobe/shared/builder/memory/projects/ponto-certo`, openclaw/agents/rh/SOUL` |

---

## 7. Conexões estratégicas cross-domínio (as mais valiosas)

### 7.1 TTD 409 como fio condutor fiscal → reforma → SimulImport

```
agents/kobe/shared/fisco/SOUL (TTD 409, 36 meses, ICMS 2.6%)
  ↕ causa/efeito
agents/kobe/shared/fisco/skills/distribution/SKILL (modelo 90/10 maximiza TTD)
  ↕ temporal/futuro
agents/kobe/shared/simulimport/reforma-tributaria-importacao (TTD extinto 2029-2033)
  ↕ complementar
agents/kobe/shared/simulimport/sprint2-roadmap (feature: calcular custo sem TTD)
```

**Insight:** A estrutura societária inteira da GB depende de um benefício fiscal temporário. O SimulImport eventualmente precisará simular custos pós-2033 sem esse benefício — e o Fisco tem todo o conhecimento para alimentar essas fórmulas.

### 7.2 Bidspark como convergência Builder × Spark

```
agents/builder/memory/projects/bidspark (~90% pronto, zero testes)
  ↕ constrói
agents/spark/IDENTITY (gestão de ads, 4 skills)
  ↕ opera
agents/spark/memory/context/decisions (ROAS 10x, R$9k/mês em agências)
  ↕ justifica
agents/builder/SOUL (Bidspark nasceu de dor própria com agências)
```

**Insight:** Bidspark é o único projeto onde dois agentes convergem para o mesmo objetivo (eliminar R$9k/mês em agências). Spark opera manualmente hoje o que Bidspark automatizará.

### 7.3 Fisco alimentando Atlas Finance

```
agents/kobe/shared/fisco/SOUL (modelo fiscal completo, 5 CNPJs, distribuição)
  ↕ dados
agents/builder/memory/projects/atlas-finance (DRE/fluxo de caixa quebrados)
  ↕ precisa
agents/kobe/shared/fisco/memory/nfe-log (NFs reais: R$29.355,85 em março)
```

**Insight:** Atlas Finance precisa de regras fiscais para calcular DRE e fluxo de caixa corretamente. O Fisco tem essas regras mas nunca foi conectado ao Atlas Finance.

---

## 8. Ações recomendadas

### Links bidirecionais a inserir (aguardando aprovação)

**Grupo A — Extratos Financeiros (6 links)**
- `amazon-extrato/SKILL` ↔ `ml-extrato/SKILL` ↔ `shopee-extrato/SKILL`
- Todos ↔ `consolidado-financeiro/SKILL`

**Grupo B — Fees Rules (6 links)**
- `amazon-fees-rules/SKILL` ↔ `ml-fees-rules/SKILL` ↔ `shopee-fees-rules/SKILL`
- Todos ↔ `spreadsheet-pricing/SKILL`

**Grupo C — Listing Creators (4 links)**
- `amazon-listing-creator/SKILL` ↔ `shopee-listing-creator/SKILL`
- Ambos ↔ `spreadsheet-pricing/SKILL`

**Grupo D — Pipeline Superpowers (13 links sequenciais)**
- Cadeia: `brainstorming` → `writing-plans` → `subagent-driven-development`/`executing-plans` → `requesting-code-review` → `receiving-code-review` → `finishing-a-development-branch`
- Laterais: `systematic-debugging` ↔ `verification-before-completion`, `dispatching-parallel-agents` ↔ `subagent-driven-development`

**Grupo E — GB Import Hub (3 links)**
- `gb-import-hub-schema` ↔ `gb-import-hub-edge-functions-map` ↔ `gb-import-hub-reconnection-plan`

**Grupo F — SimulImport × Fisco (3 links)**
- `reforma-tributaria-importacao` ↔ `fisco/SOUL`
- `ncm-database-spec` ↔ `builder/memory/projects/simulaimport`
- `sprint2-roadmap` ↔ `reforma-tributaria-importacao`

**Grupo G — Design Systems (4 links)**
- `report-design-system` ↔ `consolidado-financeiro/SKILL`
- `excel-design-system` ↔ `excel-generation/SKILL`
- `animated-financial-display` ↔ `financial-design-systems`
- `frontend-design-ultimate` ↔ `lovable-quality`

**Grupo H — Agentes × Projetos (5 links)**
- openclaw/agents/spark` ↔ `builder/memory/projects/bidspark`
- openclaw/agents/rh/SOUL` ↔ `builder/memory/projects/ponto-certo`
- openclaw/agents/fisco/SOUL` ↔ `builder/memory/projects/atlas-finance`
- `kobe/CHANGELOG` ↔ `kobe/IDENTITY`
- `PROPAGATION` ↔ `CLAUDE`

**Grupo I — Memory cross-links (4 links)**
- `pendencias` ↔ `deadlines`
- `pendencias` ↔ `decisoes/2026-04`
- `sessions/2026-04-09` ↔ `decisoes/2026-04`
- `sessions/2026-04-10` ↔ `decisoes/2026-04`

### MOCs a criar (8 sugeridos)

1. `Token Management` — gestão centralizada de OAuth cross-agent
2. `Extratos Financeiros` — hub dos 3 extratos + consolidado
3. `Superpowers Pipeline` — mapa das 14 skills de desenvolvimento
4. `Taxas e Precificação` — hub comparativo 3 plataformas + planilha
5. `Design Systems Budamix` — hub dos 3 design systems
6. `Supabase Ecosystem` — mapa de todos os projetos e agentes
7. `Governança OpenClaw` — leveling, reviews, heartbeats
8. `Listing Pipeline` — fluxo pesquisa → criação → planilha → monitoramento

---

*Auditoria realizada em 10/04/2026 via Claude Code*
*347 notas lidas | 4 agentes paralelos | ~50 conexões descobertas*

---

## MOCs criados nesta auditoria

- [[meta/mocs/MOC - Token Management|Token Management]]
- [[meta/mocs/MOC - Extratos Financeiros|Extratos Financeiros]]
- [[meta/mocs/MOC - Superpowers Pipeline|Superpowers Pipeline]]
- [[meta/mocs/MOC - Taxas e Precificacao|Taxas e Precificação]]
- [[meta/mocs/MOC - Design Systems Budamix|Design Systems]]
- [[meta/mocs/MOC - Supabase Ecosystem|Supabase Ecosystem]]
- [[meta/mocs/MOC - Governanca OpenClaw|Governança OpenClaw]]
- [[meta/mocs/MOC - Listing Pipeline|Listing Pipeline]]

## Skills de manutenção do vault

- [[skills/obsidian-vault-manager/SKILL|Obsidian Vault Manager]]

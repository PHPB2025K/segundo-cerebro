# SKILL: Análise Semanal Amazon Ads — Budamix (BidSpark)

**Versão:** 3.0
**Atualizada:** 10/Abr/2026
**Modo:** Otimização MANUAL via Claude Code (análise automática multi-agente pausada)

---

## 1. OBJETIVO

Otimizar semanalmente TODAS as campanhas Amazon Ads Sponsored Products da Budamix, maximizando vendas com ACoS dentro do target definido por grupo, utilizando a estratégia de 4 campanhas complementares (funil).

### Fonte Única de Metas
Tabela `amazon_ads_product_groups` no Supabase. SEMPRE consultar antes de analisar — nunca usar valores de memória.

### Multiplicadores por Tipo de Campanha
| Tipo | Multiplicador | Papel |
|------|:-:|---|
| DESCOBERTA | ×1.5 | Mineração — aceita custo maior para descobrir termos novos |
| ALCANCE | ×1.2 | Broad/Phrase — captura variações de termos conhecidos |
| PERFORMANCE | ×0.72 | Exact — motor de lucro, deve performar MELHOR que target |
| DEFESA | ×0.5 | Marca própria — competição mínima, bid baixo |

**Exemplo com target 20%:** Desc 30% | Alc 24% | Perf 14.4% | Def 10%

---

## 2. ESTRATÉGIA: FUNIL DE 4 CAMPANHAS

Cada grupo de anúncios é composto por 4 campanhas que funcionam como um **funil integrado**. Nenhuma campanha opera isolada — cada uma tem um papel específico e alimenta a próxima. Antes de analisar qualquer métrica individual, é preciso entender como o tráfego flui entre as 4 campanhas.

### Como o funil funciona

A **DESCOBERTA** (campanha automática) minera termos novos que ninguém pensou. A Amazon testa automaticamente diferentes search terms e product targetings. Quando um termo gera 2 ou mais vendas, ele é "promovido" para a **PERFORMANCE** como keyword exact match. Para evitar que a Descoberta e a Performance disputem o mesmo tráfego, adicionamos uma negativa EXACT na Descoberta — isso **roteia** a busca exata para a Performance, enquanto variações do termo continuam sendo descobertas.

O **ALCANCE** (broad/phrase) faz o mesmo papel da Descoberta, mas com keywords manuais que capturam variações. Por exemplo, "pote hermético vidro grande" no Alcance BROAD captura variações como "pote hermético vidro grande 1 litro". Winners do Alcance também migram para a Performance com negativa EXACT correspondente.

A **PERFORMANCE** (exact match) concentra os winners comprovados com bids otimizados individualmente e o maior budget do grupo (~50%). É o motor de lucro — deve ter o menor ACoS de todas as campanhas.

A **DEFESA** protege buscas de marca ("budamix" + variações) contra concorrentes. Budget mínimo, quase sem tráfego, e está tudo bem assim — ela só ativa quando alguém busca pela marca.

### Regras do Funil (INVIOLÁVEIS)
- **NEGATIVE_EXACT = roteamento** (direciona tráfego exact de uma campanha para outra)
- **NEGATIVE_PHRASE = filtro** (bloqueia material/contexto irrelevante, como "inox" para produto de porcelana)
- NUNCA usar NEGATIVE_PHRASE em termos core do produto (substantivos como caneca, jarra, pote, xícara)
- Todo termo da Performance DEVE ter NEGATIVE_EXACT correspondente nas origens (Descoberta + Alcance)
- ASINs dos produtos devem estar em TODAS as 4 campanhas do grupo

### Fluxo de exemplo
```
Cliente busca "pote hermético vidro tampa bambu 500ml"
  → Performance EXACT "pote hermético vidro tampa bambu" NÃO captura (não é exact match)
  → Alcance BROAD "pote hermético bambu" CAPTURA ✅ (variação matchada)
  → Se converter: migrar para Performance como EXACT + negativar EXACT no Alcance

Cliente busca "pote hermético vidro tampa bambu"
  → Performance EXACT captura ✅ (match exato)
  → Alcance bloqueado por NEGATIVE_EXACT ✅ (roteamento funciona)
  → Descoberta bloqueado por NEGATIVE_EXACT ✅

Cliente busca "pote plástico hermetico"
  → BLOQUEADO por NEGATIVE_PHRASE "plástico" em todas as campanhas ✅ (filtro de material)
```

---

## 3. REGRAS DE SEGURANÇA — 8 GUARDRAILS

Estas regras existem porque em Fev/Mar 2026, o sistema antigo negativou termos core como "caneca" na campanha de Canecas, causando queda de 99% nas impressões e perda de ~R$1.270/semana. NUNCA violar estas regras.

### G1: TERMOS PROTEGIDOS
- Tabela `amazon_ads_protected_terms` contém 257 termos extraídos do catálogo
- ANTES de negativar qualquer termo: consultar esta tabela
- Se o termo consta como protegido — NÃO NEGATIVAR sem aprovação explícita do Pedro

### G2: NEGATIVE_EXACT COMO DEFAULT
- Toda negativação deve usar NEGATIVE_EXACT, a menos que haja razão explícita para PHRASE
- NEGATIVE_PHRASE só para filtrar MATERIAIS ou CONTEXTOS claramente irrelevantes
- NUNCA usar NEGATIVE_PHRASE em substantivos do produto

### G3: LIMITE CUMULATIVO DE BID
- Redução máxima por ciclo: 30% do bid atual
- Redução máxima acumulada em 28 dias: 50% do bid original
- Bid mínimo absoluto: R$0.30 (keywords) / R$0.15 (targeting groups Descoberta)
- ANTES de reduzir bid: consultar histórico de reduções no `actions_log`

### G4: LIMITE DE NEGATIVAÇÕES POR CAMPANHA
| Tipo | Máximo |
|------|:-:|
| DESCOBERTA | 30 |
| ALCANCE | 40 |
| PERFORMANCE | 15 |
| DEFESA | 5 |

### G5: NUNCA NEGATIVAR TERMOS COM VENDAS
- Se o search term teve QUALQUER venda nos últimos 30 dias — NÃO negativar
- Se tem 0 vendas mas é termo core do produto — NÃO negativar (problema é listing, não ads)
- Exceção única: ASIN de concorrente com vendas (pode negativar)

### G6: DADOS MÍNIMOS PARA AGIR
| Ação | Dados mínimos |
|------|--------------|
| Reduzir bid | 20+ cliques |
| Aumentar bid | 15+ cliques + 1 venda |
| Negativar IRRELEVANTE | 10+ cliques, R$3+ spend, 0 vendas |
| Negativar RELEVANTE | 20+ cliques, R$8+ spend, 0 vendas, 14+ dias |
| Migrar para Performance | 2+ vendas |
| Pausar keyword | 20+ cliques, 0 vendas 30d, 2 reduções prévias |

### G7: PARES DE MIGRAÇÃO OBRIGATÓRIOS
- Toda migração para Performance DEVE ter NEGATIVE_EXACT correspondente na origem
- NUNCA negativar na origem SEM criar a keyword no destino primeiro

### G8: NUNCA MIGRAR ASINs
- Regex: `^[bB]0[a-zA-Z0-9]{8,}$`
- ASINs de concorrentes NUNCA devem ser migrados para Performance
- ASINs podem ser negativados (é legítimo bloquear tráfego de concorrente)

---

## 4. METODOLOGIA — 4 FASES SEQUENCIAIS

### Conceito Fundamental
Antes de qualquer opinião, coletamos TUDO. Não analisamos de cabeça — analisamos dados. Depois analisamos em 6 dimensões. Depois apresentamos recomendações POR CAMPANHA e PARAMOS para aprovação. Só executamos o que for aprovado, e registramos TUDO no banco.

### Ordem de Análise dos Grupos
1. **🔴 Críticos** primeiro — ACoS >2x target ou gastando sem vender
2. **🟡 Atenção** — ACoS acima do target mas com vendas
3. **🟢 Saudáveis** — verificação rápida de oportunidades
4. **⚪ Inativos** — só reportar status

Dentro de cada grupo, a análise é sempre **POR CAMPANHA** (Performance → Alcance → Descoberta → Defesa), considerando o papel de cada uma no funil.

---

### FASE 1 — COLETA (executar automaticamente, sem perguntar)

Para CADA grupo de produto, coletar todos os dados necessários. A coleta usa duas fontes:

**Fonte primária: Supabase** (dados já coletados diariamente pelo ciclo N8N)

```sql
-- Metas do grupo (SEMPRE consultar, nunca usar de memória)
SELECT * FROM amazon_ads_product_groups WHERE id = '{group_id}';

-- Campanhas com métricas em 3 JANELAS TEMPORAIS (7d, 15d, 30d)
-- Isso evita decisões baseadas em flutuação de curto prazo
SELECT * FROM amazon_ads_campaigns
WHERE campaign_id IN (SELECT campaign_id FROM amazon_ads_campaign_roles WHERE product_group_id = '{group_id}')
AND report_date >= CURRENT_DATE - INTERVAL '30 days';

-- Keywords ativas com métricas de performance
SELECT * FROM amazon_ads_keywords
WHERE campaign_id IN (...)
AND report_date >= CURRENT_DATE - INTERVAL '14 days';

-- Search terms — cada termo que gerou cliques, quanto gastou, se converteu
SELECT * FROM amazon_ads_search_terms
WHERE campaign_id IN (...)
AND report_date >= CURRENT_DATE - INTERVAL '14 days';

-- Ações anteriores e seus resultados — evita repetir o que não funcionou
SELECT * FROM amazon_ads_actions_log
WHERE product_group_id = '{group_id}'
AND status IN ('EXECUTED', 'FAILED')
ORDER BY executed_at DESC LIMIT 30;

-- Termos protegidos do grupo (guardrail G1)
SELECT term FROM amazon_ads_protected_terms WHERE product_group_id = '{group_id}';

-- Keywords ATUAIS com bids (snapshot diário)
-- NOTA: tabela alimentada diariamente desde 10/Abr/2026
-- Se snapshot_date < 30 dias de histórico → complementar com API Amazon ao vivo
SELECT * FROM amazon_ads_keyword_snapshots
WHERE campaign_id IN (...)
AND snapshot_date = (SELECT MAX(snapshot_date) FROM amazon_ads_keyword_snapshots);

-- Negativas ATUAIS por campanha (snapshot diário)
-- NOTA: tabela alimentada diariamente desde 10/Abr/2026
-- Se snapshot_date < 30 dias de histórico → complementar com API Amazon ao vivo
SELECT * FROM amazon_ads_negative_snapshots
WHERE campaign_id IN (...)
AND snapshot_date = (SELECT MAX(snapshot_date) FROM amazon_ads_negative_snapshots);

-- Produtos por campanha (ASINs vinculados)
SELECT * FROM amazon_ads_product_ads WHERE campaign_id IN (...);
```

**Fonte secundária: API Amazon ao vivo** (usar ENQUANTO snapshots não têm 30 dias de histórico)

Até ~10/Mai/2026, as tabelas `keyword_snapshots` e `negative_snapshots` terão menos de 30 dias de dados. Nesse período, COMPLEMENTAR com chamadas API live para:
- Keywords atuais por campanha (bids, match type, estado) via `KeywordsV3.list_keywords()`
- Negativas atuais por campanha via `CampaignNegativeKeywordsV3.list_campaign_negative_keywords()`

**A partir de ~10/Mai/2026**, quando os snapshots tiverem 30+ dias de histórico, a Fase 1 será 100% Supabase — zero chamadas API ao vivo.

**Métricas obrigatórias em CADA JANELA (7d, 15d, 30d):**
- Impressões, Cliques, CTR, CPC médio
- Spend, Sales, ACoS, ROAS
- Pedidos (conversões)
- Budget utilization por campanha (spend/budget %)
- Histórico de ações executadas no período e seus resultados

---

### FASE 2 — ANÁLISE (executar automaticamente, sem perguntar)

Para cada grupo, analisar em **6 dimensões**, sempre considerando o funil completo:

**2.1 — Integridade do funil**
Verificar se as 4 campanhas estão trabalhando juntas corretamente:
- Todo termo da Performance tem NEGATIVE_EXACT nas origens? Se não, há "furos" — tráfego exact que deveria ir para Performance está sendo capturado pelo Alcance a custo maior.
- Há NEGATIVE_PHRASE destrutivas bloqueando termos core do produto? (verificar contra `protected_terms`)
- Produtos (ASINs) estão em todas as 4 campanhas?
- Há competição interna? (mesmo termo EXACT no Alcance e Performance sem negativa)
- Bids estão invertidos? (Alcance com bid MAIOR que Performance para o mesmo termo)

**2.2 — Métricas vs target**
Cada campanha tem seu próprio target de ACoS (baseado no multiplicador). Comparar:
- ACoS 7d de cada campanha vs seu target específico (não vs o target geral)
- ROAS, CTR, CPC médio por campanha
- Budget utilization por campanha (>90% = limitando vendas, <30% = sobrando)
- Validar vendas zero: se uma campanha mostra 0 vendas, CONFIRMAR cruzando com search terms e dados diários. Dados de `sales_7d` da Amazon flutuam por 48-72h.

**2.3 — Search terms**
Separar em categorias e quantificar:
- **Winners:** termos com vendas — candidatos a migração se não estão na Performance
- **Waste:** termos com spend > R$3 e 0 vendas — candidatos a negativação
- **ASINs:** separar ASINs de concorrentes (negativar) de product targeting (avaliar)
- Calcular % do spend total que é waste
- Para cada winner: está na campanha certa? (se está no Alcance mas deveria estar na Performance)

**2.4 — Tendência**
Comparar as 3 janelas para entender a direção:
- 7d vs 15d vs 30d: ACoS está melhorando ou piorando?
- Identificar o ponto de inflexão — quando exatamente algo mudou
- Cruzar ponto de inflexão com data de ações nossas — foi algo que fizemos?

**2.5 — Resultado das ações anteriores**
O feedback loop mais importante — aprender com o que fizemos:
- Consultar `result_after_7d` das ações executadas há 7+ dias (calculado automaticamente pelo compute-results diário)
- Para cada ação: MELHOROU, NEUTRO ou PIOROU?
- Se uma ação PIOROU: NÃO repetir a mesma abordagem — tentar diferente
- Se uma negativação causou queda >50% impressões E >30% vendas — considerar reverter
- Se uma ação MELHOROU: considerar escalar (mais do mesmo)

**2.6 — Diagnóstico de conversão**
Se o tráfego é alto mas vendas são zero, o problema pode NÃO ser de ads:
- Tráfego alto + 0 vendas → possível problema de listing/preço/Buy Box/estoque (NÃO negativar termos core)
- Impressões caíram de repente → verificar se alguma ação nossa causou
- ACoS subiu gradualmente → identificar quais termos/campanhas específicas estão piorando

---

### FASE 3 — RECOMENDAÇÕES (PARAR AQUI E ESPERAR APROVAÇÃO)

Apresentar o relatório **1 grupo de cada vez**, e dentro de cada grupo, **por campanha**. Cada campanha recebe seu próprio diagnóstico e recomendações, sempre explicando como a ação afeta o funil.

**Formato obrigatório:**

```
🔴/🟡/🟢 [NOME DO GRUPO]
ACoS 7d: X% | 15d: Y% | 30d: Z% (target: W%)
Spend 7d: R$X | Sales 7d: R$X | Ped: X | Tendência: ↑/↓/→

INTEGRIDADE DO FUNIL: ✅ OK / ⚠️ X furos / 🔴 problemas estruturais

RESULTADO DAS AÇÕES ANTERIORES:
- [ação] em [data] → [MELHOROU/NEUTRO/PIOROU] — [dados concretos]

POR CAMPANHA:

  PERFORMANCE (target X%):
    Métricas 7d/15d/30d: [tabela]
    Diagnóstico: [o que está acontecendo nesta campanha]
    Ações: [lista com dados e classificação ✅/⚠️/🔴]

  ALCANCE (target X%):
    [mesma estrutura]

  DESCOBERTA (target X%):
    [mesma estrutura]

  DEFESA (target X%):
    [mesma estrutura]

GUARDRAILS VERIFICADOS: ✅ G1-G8 / ⚠️ atenção em GX
RISCO: [se executar / se NÃO executar]
```

**Classificação de risco das ações:**
- ✅ SEGURA: negativar ASIN concorrente, negativar termo claramente irrelevante, migrar winner comprovado
- ⚠️ REVISAR: reduzir bid >20%, negativar termo com alguma relação ao produto, ajustar budget
- 🔴 DECISÃO: pausar keyword com vendas históricas, negativar termo core, mudança estrutural

**NUNCA executar sem aprovação explícita do Pedro.**

Após apresentar, perguntar: "Quais ações você aprova? Pode ser por grupo ou por ação individual."

---

### FASE 4 — EXECUÇÃO (SOMENTE após aprovação)

Para cada ação aprovada:

1. **Verificar guardrails G1-G8** uma última vez ANTES de executar
2. **Executar via SDK Amazon Ads** (`python-amazon-ad-api`)
3. **Registrar no `amazon_ads_actions_log`** com TODOS os campos:
   - action_type, entity_name, campaign_name, campaign_id
   - old_value, new_value
   - reason (com dados concretos — spend, clicks, vendas que justificam a ação)
   - product_group_id, product_group_name
   - status = 'EXECUTED'
   - executed_at = NOW()
4. **Reportar resultado** (sucesso/erro + IDs da Amazon)
5. **Definir efeito esperado** para cada ação — o que monitorar na próxima semana

O registro no `actions_log` é obrigatório porque:
- O compute-results diário vai calcular `result_after_7d` automaticamente
- Na próxima análise semanal, podemos medir o impacto real de cada ação
- Sem registro, não há aprendizado

---

## 5. INFRAESTRUTURA DE DADOS

### Pipeline de Coleta Diária (N8N, 6h BRT)

O ciclo diário alimenta o Supabase com todos os dados necessários para a análise semanal:

```
Schedule 6h BRT
  → Health Check
  → Collect Campaigns (relatório D-2)      → amazon_ads_campaigns
  → Collect Targeting (relatório D-2)       → amazon_ads_keywords
  → Collect Search Terms (relatório D-2)    → amazon_ads_search_terms
  → Daily Health Check                      → alertas WhatsApp
  → Rolling Collection (D-4, D-9, D-16, D-30) → reapuração de dados
  → Sync Catalog                            → amazon_ads_catalog
  → Collect Product Ads                     → amazon_ads_product_ads
  → Compute Action Results                  → amazon_ads_actions_log.result_after_7d
  → Keyword Snapshots                       → amazon_ads_keyword_snapshots
  → Negative Snapshots                      → amazon_ads_negative_snapshots
  → Format Summary + Send WhatsApp
```

### Tabelas do Supabase — Mapa Completo

| Tabela | Tipo | Frequência | Dados |
|--------|------|:----------:|-------|
| `amazon_ads_campaigns` | Relatório | Diário D-2 | Métricas campanhas (imp, clicks, spend, sales) |
| `amazon_ads_keywords` | Relatório | Diário D-2 | Métricas keywords (imp, clicks, spend, sales, bid) |
| `amazon_ads_search_terms` | Relatório | Diário D-2 | Search terms com métricas |
| `amazon_ads_keyword_snapshots` | API live | Diário | Bids ATUAIS, state de toda keyword ENABLED |
| `amazon_ads_negative_snapshots` | API live | Diário | Negativas ativas por campanha |
| `amazon_ads_product_ads` | API live | Diário | ASINs por campanha com state |
| `amazon_ads_catalog` | API Metadata | Diário | Título, preço, BSR, categoria |
| `amazon_ads_product_groups` | Estático | Manual | Metas (acos_target, margin, budget) |
| `amazon_ads_campaign_roles` | Estático | Manual | Mapeamento campanha→grupo→role |
| `amazon_ads_protected_terms` | Estático | Manual | 257 termos que nunca negativar |
| `amazon_ads_actions_log` | Evento | Por ação | Histórico de ações + result_after_7d |
| `amazon_ads_config` | Estático | Manual | 4 configs globais |

---

## 6. GRUPOS ATIVOS

SEMPRE consultar `amazon_ads_product_groups` para a lista e metas atualizadas:

```sql
SELECT group_name, acos_target, margin_pct, total_daily_budget, active
FROM amazon_ads_product_groups ORDER BY group_name;
```

Não confiar em listas hardcoded — grupos, metas e budgets mudam.

---

## 7. LIÇÕES APRENDIDAS (CRÍTICAS)

### Incidente Fev/Mar 2026 — Negativações PHRASE Destrutivas
**O que aconteceu:** Sistema antigo negativou "caneca", "microfibra", "jarra de vidro" como NEGATIVE_PHRASE em nível de campanha. Resultado: queda de 99% nas impressões, perda estimada de R$1.270/semana.
**Lição:** NUNCA usar NEGATIVE_PHRASE em substantivos do produto. Consultar `amazon_ads_protected_terms` ANTES de toda negativação.

### Incidente Mar 2026 — Migração de ASINs
**O que aconteceu:** ASINs de concorrentes foram migrados como keywords Exact para Performance. Gastou dinheiro biddando em produtos alheios.
**Lição:** ASINs (regex `^[bB]0[a-zA-Z0-9]{8,}$`) NUNCA devem ser migrados. Podem ser negativados.

### Incidente Mar 2026 — Bid Crushing
**O que aconteceu:** Mesma keyword recebeu -30% por 3 ciclos seguidos. Total -66%. Keyword morreu.
**Lição:** Verificar histórico de reduções nos últimos 28 dias. Limite acumulado: 50%.

---

## 8. LOGGING DE AÇÕES MANUAIS

Quando executar ações manualmente via SDK, SEMPRE registrar no actions_log:

```sql
INSERT INTO amazon_ads_actions_log (
  action_type, entity_type, entity_id, entity_name,
  campaign_name, campaign_id,
  old_value, new_value, reason, status,
  product_group_id, product_group_name,
  urgency, confidence, approved_by,
  executed_at, recommended_at, created_at
) VALUES (
  '{tipo}', '{entity_type}', '', '{termo}',
  '{campanha}', '{campaign_id}',
  '{valor_antigo}', '{valor_novo}', '{justificativa com dados}', 'EXECUTED',
  '{group_id}', '{group_name}',
  'ALTA', 'ALTA', 'pedro',
  NOW(), NOW(), NOW()
);
```

---

## 9. CHECKLIST PRÉ-ANÁLISE

Antes de começar cada análise semanal:
- [ ] Consultar metas atuais no Supabase (NÃO usar de memória)
- [ ] Verificar última data com dados coletados (coleta D-2 diária 6h BRT)
- [ ] Verificar se snapshots de keywords e negativas foram coletados
- [ ] Verificar se compute-results rodou (result_after_7d preenchido)
- [ ] Verificar se há ações PENDING no actions_log
- [ ] Consultar termos protegidos do grupo (`amazon_ads_protected_terms`)
- [ ] Confirmar quais grupos analisar (todos ou específicos)

---

## 10. REFERÊNCIA RÁPIDA

### Match Types de Negativação
| Tipo | Efeito | Quando usar |
|------|--------|-------------|
| NEGATIVE_EXACT | Bloqueia apenas a busca exata | Roteamento (migração), ASINs |
| NEGATIVE_PHRASE | Bloqueia qualquer busca que contenha o termo | Filtro de material/contexto irrelevante |

### Fórmulas
```
ACoS = (Spend / Sales) × 100
ROAS = Sales / Spend
CPC = Spend / Clicks
CTR = (Clicks / Impressions) × 100
Budget Utilization = (Avg Daily Spend / Daily Budget) × 100
```

### Prioridade de Ações (por impacto em R$)
1. Migrar winners para Performance (gera receita)
2. Corrigir furos no funil — negativações EXACT faltantes (evita desperdício estrutural)
3. Negativar waste com alto spend (economia direta)
4. Ajustar bids de keywords com ACoS >2x target (economia)
5. Escalar winners com ACoS <0.5x target (mais receita)
6. Ajustar budgets (rebalanceamento)

---

## 11. HISTÓRICO DE SESSÕES

### Sessão 28/Mar/2026 — Auditoria Geral
- 8 grupos auditados, 170+ NEGATIVE_PHRASE destrutivas removidas
- Roteamento NEGATIVE_EXACT criado em todos os grupos
- 3 campanhas Performance criadas, 3 Defesa criadas

### Sessão 28-29/Mar/2026 — Novos Grupos + Metas
- 4 grupos novos criados (Tampa Bambu, Jardinagem, Redinha, Canelada)
- Metas ACoS Fase 1 aplicadas (25%→20%, 30%→25%)
- Multiplicadores atualizados (Desc ×2.0→×1.5, Def ×0.6→×0.5)

### Sessão 02/Abr/2026 — Fixes pontuais
- Suporte Gamer: negativas 14→6, bids aumentados → resultado: +1000% vendas
- Redinha Frutas: negativas 8→2, bids aumentados → resultado: ainda sem tráfego

### Sessão 04/Abr/2026 — Canequinhas + Xícaras
- SPARK055/SPARK056
- Canequinhas: budget redistribuído, genéricos negativados
- Xícaras: "com pires" negativado PHRASE

### Sessão 10/Abr/2026 — Análise semanal COMPLETA (178 ações, 9 grupos)

**Infraestrutura adicionada:**
- 3 novos endpoints: keyword-snapshots (2.160 kws), negative-snapshots (798 negs), compute-results
- N8N workflow: 31 nodes (3 novos no ciclo diário)

**Resultados por grupo:**

| Grupo | Ações | Achados principais |
|-------|:-----:|-------------------|
| Canecas Tulipa | 9 | Inversão bids Alcance corrigida, waste eliminado |
| Kit Xícaras Paris | 8 | Bids + negativas legacy removidas |
| Kit Jardinagem | 4 | PAUSADO — 0 vendas, sem demanda |
| Canequinhas Café | 35 | 29 bids inversão Alcance, 6 dup Descoberta G4 |
| **Jarra Medidora** | **52** | **3 PHRASE na Perf bloqueavam TOP keywords (40+ pu/mês)**. Limpeza Desc 76→35 |
| Potes Vidro | 6 | Saudável — pausar marcas concorrentes, otimização fina |
| Tampa Bambu | 4 | Grupo novo (12d) — ações conservadoras. Genéricos convertem melhor que bambu-específicos |
| Suporte Gamer | 14 | Escalar "suporte headset" +30%. Negativar "suporte para headset" (intent headset-only). 8 dup Desc |
| **Microfibra Carro** | **50** | **Performance MORTA — 44 PHRASE bloqueavam TODOS 26 keywords (0 cliques em 24d). Ressuscitada** |

**Padrão encontrado**: NEGATIVE_PHRASE legacy do sistema pré-guardrails (Fev-Mar) ainda presente em 2 grupos (Jarra Medidora + Microfibra). Problema idêntico ao incidente de negativações catastróficas de Fev/Mar. Guardrails G1/G2 previnem recorrência mas não limparam o legado.

**Lições aprendidas:**
1. Sempre cross-validar Performance negatives vs keywords ANTES de qualquer análise
2. "waste" em Performance pode ser enganoso — close variants (plural, preposições) podem vender
3. Grupos novos (<15 dias) requerem abordagem conservadora — dados insuficientes para decisões agressivas
4. Alcance com ACoS melhor que Performance indica inversão de bids ou Performance bloqueada
5. Budget utilization <30% indica bids muito baixos, não falta de budget

**Revisão geral: 17/Abr/2026** — verificar result_after_7d de todas 178 ações

---

## 12. CHANGELOG

| Data | Versão | Mudança |
|------|--------|---------|
| 09/Abr/2026 | 1.0 | Criação inicial |
| 09/Abr/2026 | 2.0 | Guardrails, lições aprendidas, logging, queries SQL |
| 10/Abr/2026 | 2.1 | Sessão Tulipa logada, formato análise por campanha |
| 10/Abr/2026 | 3.0 | Metodologia descritiva completa, infraestrutura de dados documentada, 3 novas coletas, pipeline N8N expandido |
| 10/Abr/2026 | 3.1 | Análise semanal completa (9 grupos, 178 ações). Padrão PHRASE legacy documentado. 5 lições aprendidas |
| 10/Abr/2026 | 3.2 | Novo grupo "Potes Redondos Vidro" criado (4 campanhas, 45 keywords). Correção material vidro vs plástico. Total 13 grupos (12 ativos) |

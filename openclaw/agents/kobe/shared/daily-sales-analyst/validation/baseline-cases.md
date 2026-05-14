# Baseline Cases — Daily Sales Analyst Phase 5

**Criado em:** 2026-05-14
**Objetivo:** Definir baseline objetiva para avaliacao de qualidade das analises.

---

## Caso 1 — Dia Bom Claro

| Campo | Valor |
|-------|-------|
| **Data** | 2026-05-11 |
| **Plataforma/Destinatario** | Shopee → Lucas |
| **Tipo de caso** | dia_bom_claro |
| **Data Readiness** | DADOS_OK |
| **Metricas** | 135 pedidos, R$ 6.506,57 GMV, ticket R$ 48,20 |
| **Decisao esperada** | baseline_candidate |

### O que uma analise boa deveria perceber
- Volume solido (135 pedidos) com ticket acima da media
- 3 contas Shopee bem separadas (store=72, oficial-2=36, shop-3=27)
- 21 cancelamentos e alto — investigar se concentrado em conta/produto
- Comparar vs mesma weekday (domingo) para context

### O que seria erro critico
- Misturar dados entre as 3 contas Shopee
- Ignorar os 21 cancelamentos (15.6% do total)
- Reportar SKU cru sem nome do produto
- Atribuir dados de ML ou Amazon ao Lucas

### Criterios binarios
- [ ] Contas Shopee separadas corretamente
- [ ] Cancelamentos mencionados
- [ ] Nenhum SKU cru exposto
- [ ] Plataforma correta (Shopee)
- [ ] Dados fidedignos ao package

### Scores esperados
- Profundidade: **2/5** (fallback deterministico — dados crus sem insight)
- Utilidade: **2/5** (mostra numeros mas sem contexto acionavel)

### Limitacao de label
`baseline_candidate` — Nao ha label humano de referencia para esta data. Metricas verificaveis contra package, mas qualidade analitica nao tem ground truth.

---

## Caso 2 — Dia Ruim Claro

| Campo | Valor |
|-------|-------|
| **Data** | 2026-05-13 |
| **Plataforma/Destinatario** | Shopee → Lucas |
| **Tipo de caso** | dia_ruim_claro |
| **Data Readiness** | NOT_READY |
| **Metricas** | Bloqueado — shopee-oficial-2 -60%, amazon +68.5% |
| **Decisao esperada** | rejeitado |

### O que uma analise boa deveria perceber
- Pipeline deve ser BLOQUEADA — dados nao confiaveis
- shopee-budamix-oficial-2 com volume -60% vs media 30d (possivel falha de sync)
- Amazon com +68.5% vs media (anomalia positiva ou duplicacao)
- Nao deve gerar recomendacoes sobre dados potencialmente incorretos

### O que seria erro critico
- Gerar analise como se os dados fossem confiaveis
- Ignorar os alertas de volume band
- Recomendar acoes baseadas em dados suspeitos
- Enviar Slack com dados NOT_READY

### Criterios binarios
- [ ] Pipeline bloqueada corretamente
- [ ] Motivo do bloqueio documentado
- [ ] send_real_allowed = false
- [ ] Artefatos marcados como BLOCKED

### Scores esperados
- Profundidade: **1/5** (bloqueio correto, sem analise)
- Utilidade: **3/5** (bloqueio e util — evita desinformacao)

### Limitacao de label
Ground truth: bloqueio correto por design. Verificavel objetivamente.

---

## Caso 3 — Dia Ambiguo

| Campo | Valor |
|-------|-------|
| **Data** | 2026-05-12 |
| **Plataforma/Destinatario** | Shopee → Lucas |
| **Tipo de caso** | dia_ambiguo |
| **Data Readiness** | DADOS_OK |
| **Metricas** | 118 pedidos, R$ 5.378,44 GMV, ticket R$ 45,58, 13 cancelamentos |
| **Decisao esperada** | baseline_candidate |

### O que uma analise boa deveria perceber
- Volume ok mas shopee-oficial-2 com -37% e shop-3 com -36.2% vs media 30d
- Essas quedas passaram no volume_band (dentro da tolerancia) mas merecem comentario
- Cancelamentos moderados (11%)
- Segunda-feira — comparar com segunda anterior

### O que seria erro critico
- Ignorar quedas nas contas menores
- Tratar como "dia bom" sem caveats
- Misturar plataformas

### Criterios binarios
- [ ] Variacao por conta mencionada
- [ ] Cancelamentos contextualizados
- [ ] Nenhum dado de outra plataforma
- [ ] Contas separadas

### Scores esperados
- Profundidade: **2/5** (fallback — mostra dados mas sem interpretacao)
- Utilidade: **2/5** (numeros disponiveis mas sem nuance analitica)

### Limitacao de label
`baseline_candidate` — Sem label humano. A ambiguidade deste caso so pode ser avaliada por analise LLM futura.

---

## Caso 4 — Risco de Produto Errado

| Campo | Valor |
|-------|-------|
| **Data** | 2026-05-11 |
| **Plataforma/Destinatario** | Amazon → Leonardo |
| **Tipo de caso** | risco_produto_errado |
| **Data Readiness** | DADOS_OK |
| **Metricas** | 30 pedidos, R$ 1.152,80 GMV, FBA: 30/30 |
| **Decisao esperada** | baseline_candidate |

### O que uma analise boa deveria perceber
- Amazon: ASIN e titulo real do produto devem aparecer (nao SKU interno)
- 100% FBA — comentar impacto logistico
- 8 cancelamentos em 30 pedidos (26.7%) — muito alto, pedir investigacao
- Top products com titulo real, nao codigo

### O que seria erro critico
- Mostrar ASIN B0xxxxx sem titulo legivel
- Ignorar taxa de cancelamento de 26.7%
- Confundir produtos FBA com FBM
- Misturar dados de Shopee/ML

### Criterios binarios
- [ ] ASIN com titulo real (nao SKU cru)
- [ ] Taxa de cancelamento alta destacada
- [ ] Dados exclusivamente Amazon
- [ ] FBA/FBM correto

### Scores esperados
- Profundidade: **2/5** (fallback lista top products mas sem contexto ASIN)
- Utilidade: **2/5** (dados disponiveis mas sem inteligencia sobre produto)

### Limitacao de label
`baseline_candidate` — Verificacao de ASIN/titulo depende de LLM layer. Fallback deterministico nao resolve nomes de produto.

---

## Caso 5 — Shopee Mascarando Conta

| Campo | Valor |
|-------|-------|
| **Data** | 2026-05-12 |
| **Plataforma/Destinatario** | Shopee → Lucas |
| **Tipo de caso** | shopee_mascara_conta |
| **Data Readiness** | DADOS_OK |
| **Metricas** | store=76, oficial-2=23, shop-3=19 |
| **Decisao esperada** | baseline_candidate |

### O que uma analise boa deveria perceber
- 3 contas Shopee devem ser SEMPRE separadas por shop_id
- oficial-2 e shop-3 com queda significativa (-37% e -36.2%) mas dentro da banda
- Se contas forem somadas sem discriminacao, Lucas perde visibilidade
- Cada conta tem dinamica propria — store e dominante

### O que seria erro critico
- Somar as 3 contas em "Shopee total" sem discriminar
- Apresentar dados de uma conta como se fossem de outra
- Ignorar a queda simultanea de oficial-2 e shop-3

### Criterios binarios
- [ ] 3 contas separadas no artefato
- [ ] shop_id correto para cada conta
- [ ] Nenhuma agregacao que mascare conta individual
- [ ] Queda por conta visivel

### Scores esperados
- Profundidade: **2/5** (fallback separa por conta no layer 02-tatica)
- Utilidade: **2/5** (dados separados mas sem analise de causa)

### Limitacao de label
`baseline_candidate` — Separacao verificavel no package. Analise de causa requer LLM.

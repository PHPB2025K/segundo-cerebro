# Skill: Google Ads — [[agents/spark/IDENTITY|Spark]] v2.0

_Análise, diagnóstico, otimização e relatórios de Google Ads (Search, Display, YouTube, Performance Max)._

---

## Status de Integração
- ❌ **API NÃO integrada ainda**
- Dependência: Pedro solicitar Developer Token no Google Ads API Center
- Roadmap completo em `memory/accounts.md`
- **Enquanto API não estiver integrada:** Spark pode analisar dados exportados (CSV, screenshots, compartilhamento de tela). Solicitar ao Kobe que peça ao Pedro exports da interface do Google Ads.

## Quando usar
- Analisar performance de campanhas Google Ads da GB
- Diagnosticar queda (CPC subindo, Quality Score caindo, termos irrelevantes)
- Recomendar otimizações (negativação, bid adjustments, estrutura de campanha)
- Gerar relatórios consolidados com Meta Ads
- Analisar termos de busca e oportunidades de keywords
- Avaliar Performance Max (canais, asset groups)
- Definir estratégia de bidding por tipo de campanha
- Planejar extensões de anúncio

## Contas

| Item | Valor |
|---|---|
| Customer ID | [PENDENTE — Pedro preencher] |
| Developer Token | [PENDENTE — Pedro solicitar] |
| OAuth | [PENDENTE — configurar após Developer Token] |
| Conversion Tracking | [VERIFICAR — Google Tag instalado?] |
| GA4 | [VERIFICAR — conectado?] |

---

## Tipos de Campanha e Quando Usar

| Tipo | Quando usar | Métricas foco | Budget mínimo recomendado |
|---|---|---|---|
| **Search** | Demanda existente. Usuário já buscando o produto. Alta intenção. | CPC, CPA, CTR, Quality Score, impression share | R$10/dia |
| **Display** | Awareness e retargeting visual. Audiências de afinidade/intenção. | CPM, alcance, frequência, view-through conversions | R$5/dia |
| **YouTube** | Branding e consideração. Vídeo como criativo principal. | CPV, VTR, conversões assistidas | R$10/dia |
| **Performance Max** | Automação cross-channel. Google decide distribuição. | ROAS, CPA, conversions, asset performance | R$15/dia (precisa volume) |
| **Shopping** | E-commerce com feed de produtos. | ROAS, CPC, impression share, benchmark CPC | Requer feed no Merchant Center |

### Recomendação de estrutura para GB (Fase Aprendizado)

```
GOOGLE ADS — GB Importadora (R$600/mês)
│
├── CAMPANHA 1: GOOGLE_SEARCH_CONV_BRANDED_BOFU_[MÊS]
│   Budget: R$60/mês (~R$2/dia)
│   Tipo: Search
│   Bid Strategy: Manual CPC (controle total com budget baixo)
│   Keywords: "budamix", "gb importadora", "potes budamix"
│   Função: Proteção de marca — ROAS altíssimo, custo mínimo
│
├── CAMPANHA 2: GOOGLE_SEARCH_CONV_GENERICA_BOFU_[MÊS]
│   Budget: R$300/mês (~R$10/dia)
│   Tipo: Search
│   Bid Strategy: Manual CPC → migrar para Target CPA quando tiver 30+ conversões
│   Keywords: "pote hermético vidro", "kit potes cozinha",
│             "pote vidro com tampa", "organização cozinha"
│   Função: Capturar demanda existente — core do Google Ads
│
├── CAMPANHA 3: GOOGLE_DISPLAY_RETARGETING_BOFU_[MÊS]
│   Budget: R$120/mês (~R$4/dia)
│   Tipo: Display
│   Bid Strategy: Target CPA ou Maximize Conversions
│   Público: Visitantes do site/listing que não compraram (7-30d)
│   Função: Recuperar visitantes que já demonstraram interesse
│
└── CAMPANHA 4: GOOGLE_PMAX_CONV_ALL_FULL-FUNNEL_[MÊS]
    Budget: R$120/mês (~R$4/dia)
    Tipo: Performance Max
    Bid Strategy: Maximize Conversion Value (target ROAS quando tiver dados)
    Função: Testar automação do Google — avaliar após 30 dias
    ⚠️ NOTA: Só lançar quando tiver 30+ conversões/mês no account
```

---

## Estratégia de Bidding

### Quando usar cada estratégia

| Estratégia | Quando usar | Quando NÃO usar | Budget mínimo |
|---|---|---|---|
| **Manual CPC** | Início (sem dados), budget baixo, controle total | Quando já tem 30+ conversões/mês | Qualquer |
| **Enhanced CPC** | Transição — tem alguns dados mas quer manter controle | Quando conversões são muito inconsistentes | R$10/dia |
| **Target CPA** | 30+ conversões nos últimos 30 dias, CPA previsível | Poucos dados, CPA muito volátil | R$15/dia |
| **Target ROAS** | 50+ conversões nos últimos 30 dias, ROAS previsível | Poucos dados, variação alta de ticket | R$20/dia |
| **Maximize Conversions** | Budget fixo, quer máximo de conversões | Quando CPA é mais importante que volume | R$10/dia |
| **Maximize Conv. Value** | Budget fixo, quer máximo de receita | Quando não tem valores de conversão configurados | R$15/dia |

### Progressão recomendada para GB

```
Manual CPC → (30 conversões) → Target CPA → (50 conversões) → Target ROAS
```

**Regra:** Nunca trocar bid strategy com menos de 2 semanas de dados na estratégia atual. Mudança reseta o learning period.

---

## Estratégia de Keywords

### Match Types — Quando usar cada um

| Match Type | Exemplo | Quando usar | Risco |
|---|---|---|---|
| **Exact** `[pote hermético vidro]` | Só mostra para essa busca exata | Keywords comprovadas com conversão | Pouco volume |
| **Phrase** `"pote hermético"` | Contém a frase na busca | Explorar variações mantendo relevância | Volume médio, algum ruído |
| **Broad** `pote hermético` | Google interpreta livremente | Descoberta de novos termos (com negativação ativa) | Alto risco de irrelevância |

### Estratégia recomendada para GB

1. **Começar com Phrase match** — equilíbrio entre volume e relevância
2. **Adicionar Exact match** para termos que comprovarem conversão
3. **Usar Broad com cautela** — apenas em campanha de descoberta com budget limitado e negativação semanal
4. **Nunca:** Broad sem negativação ativa = dinheiro queimado

### Keywords iniciais sugeridas (validar com dados)

**Alta intenção (BOFU):**
- "pote hermético vidro" / "kit potes herméticos" / "pote vidro com tampa"
- "pote de vidro para cozinha" / "pote para organizar cozinha"
- "comprar potes de vidro" / "potes herméticos preço"

**Média intenção (MOFU):**
- "organização de cozinha" / "como organizar despensa"
- "melhores potes para cozinha" / "pote vidro ou plástico"

**Branded:**
- "budamix" / "budamix potes" / "gb importadora"

### Negativação obrigatória desde o dia 1

Termos que provavelmente vão aparecer e NÃO convertem:
- "gratuito", "grátis", "free"
- "como fazer", "DIY", "caseiro"
- "receita" (ambíguo — pessoa quer receita culinária, não pote)
- "usado", "segunda mão"
- Marcas concorrentes (a menos que estratégia de conquista seja aprovada)

---

## Extensões de Anúncio (Ad Assets)

Extensões melhoram CTR sem custo adicional. Implementar TODAS relevantes:

| Extensão | O que adiciona | Prioridade | Exemplo GB |
|---|---|---|---|
| **Sitelink** | Links para páginas específicas | Alta | "Kit 6 Potes", "Potes Retangulares", "Promoções" |
| **Callout** | Textos curtos de destaque | Alta | "Frete Grátis", "Vidro Temperado", "Marca Própria Budamix" |
| **Structured Snippet** | Categorias/tipos | Média | Tipos: "Potes Redondos, Quadrados, Retangulares" |
| **Price** | Preços de produtos/serviços | Alta | "Pote 520ml a partir de R$12,50" |
| **Image** | Imagem ao lado do ad | Alta | Foto do produto principal |
| **Promotion** | Ofertas temporárias | Quando aplicável | "15% OFF no Kit Completo" |

---

## Framework de Análise

### Análise de Search Campaign

1. **Search Terms Report** — quais termos ativaram os ads
   - Classificar: ✅ Relevante + converteu → manter | ✅ Relevante + não converteu → monitorar | ❌ Irrelevante → negativar exact | ⚠️ Borderline → negativar phrase
   - Calcular: % do spend em termos relevantes vs irrelevantes
   - Meta: >80% do spend em termos relevantes

2. **Quality Score Breakdown**

   | Componente | O que medir | Como melhorar |
   |---|---|---|
   | Expected CTR | CTR do ad vs concorrentes | Melhorar copy, incluir keyword no headline |
   | Ad Relevance | Alinhamento keyword-ad | Criar ad groups temáticos (max 15-20 keywords por grupo) |
   | Landing Page XP | Velocidade, relevância, mobile | Otimizar LP: <3s load, conteúdo relevante, mobile-first |

   **Meta:** QS > 7 em todas as keywords. QS < 5 = investigar e corrigir ou pausar.

3. **Impression Share Analysis**

   | Métrica | O que significa | Ação |
   |---|---|---|
   | Search IS > 80% | Dominando os leilões | Manter ou otimizar CPC para reduzir custo |
   | Lost IS (budget) > 20% | Não aparece por budget | Considerar aumentar budget ou reduzir keywords |
   | Lost IS (rank) > 20% | Não aparece por ad rank baixo | Melhorar QS ou aumentar bid |

### Análise de Performance Max

PMax é caixa preta — diagnóstico via sinais indiretos:

1. **Asset Performance:** classificar assets como "Best", "Good", "Low"
   - Assets "Low" por 14+ dias → substituir
   - Ter mínimo 5 headlines, 5 descriptions, 5 images, 1 video

2. **Conversion por canal:** (Insights report)
   - Se >60% do spend vai pra Display/YouTube sem conversões → PMax está canibalizando Search
   - Ação: excluir brand terms do PMax ou pausar e voltar para Search manual

3. **Audience signals:** verificar quais sinais performam melhor
   - Refinar sinais baseado em dados (não é targeting, é sugestão ao algoritmo)

### Diagnóstico de Queda (Google)

```
Performance caindo
├── CPC subindo?
│   ├── Quality Score caiu?
│   │   ├── Expected CTR baixo → Melhorar ad copy, testar novos headlines
│   │   ├── Ad Relevance baixo → Reestruturar ad groups (mais granulares)
│   │   └── LP Experience baixo → Otimizar landing page
│   └── QS estável → Concorrência aumentou
│       └── Verificar Auction Insights → ajustar bids ou segmentar diferente
├── CTR caindo?
│   ├── Ad copy desatualizado? → Testar novos headlines/descriptions
│   ├── Keywords muito broad? → Refinar match types
│   └── Posição média caiu? → Verificar bid vs concorrência
├── Conversões caindo + cliques estáveis?
│   ├── Landing page mudou? → Verificar LP (velocidade, conteúdo, CTA)
│   ├── Tracking quebrou? → Verificar Google Tag/conversões
│   └── Sazonalidade? → Comparar com mesmo período anterior
└── Impressões caindo?
    ├── Budget limitado? → Check IS Lost (budget)
    ├── Keywords pausadas ou QS caiu? → Review keywords
    └── Volume de busca caiu? → Verificar Google Trends
```

---

## Negativação de Termos (Protocolo Semanal)

Frequência: **semanal obrigatória** (solicitar ao Kobe)

1. Solicitar ao Kobe: "Pull Search Terms Report últimos 7 dias"
2. Classificar cada termo
3. Negativar irrelevantes (exact match para ser preciso, phrase match para termos amplos)
4. Registrar em `campaigns/active.md`: data, quantidade, economia estimada
5. Calcular: "Quanto economizamos essa semana com negativação?"

**Formato de relatório de negativação:**
```
⚡ NEGATIVAÇÃO SEMANAL — Google Ads
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Período: [data a data]
📊 Termos analisados: [X]
❌ Termos negativados: [X]
💰 Spend desperdiçado nesses termos: R$X
📈 Economia estimada mensal: R$X

Termos negativados:
- "[termo]" — R$X gasto, 0 conversões — negativado [exact/phrase]
- "[termo]" — R$X gasto, 0 conversões — negativado [exact/phrase]

📋 Lista de negativação acumulada: [X] termos no total
```

---

## Relatórios

### Snapshot Diário (para Kobe)
```
⚡ SPARK — SNAPSHOT DIÁRIO Google Ads
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Data: [hoje]
💰 Spend hoje: R$X | Acumulado mês: R$Y / R$600 (X%)

| Campanha | Spend | CPA | ROAS | CTR | CPC | IS% | Status |
|---|---|---|---|---|---|---|---|
| [nome] | R$X | R$X | Xx | X% | R$X | X% | 🟢/🟡/🔴 |
| **Total** | **R$X** | **R$X** | **Xx** | **X%** | **R$X** | — | — |

📌 Alertas: [se houver]
📌 Keywords com QS < 6: [listar se houver]
📌 Termos negativados hoje: [X termos, economia estimada R$Y/mês]
⏭️ Recomendação: [se aplicável]
```

---

## Naming Convention

```
GOOGLE_[TIPO]_[OBJETIVO]_[PÚBLICO/KEYWORD]_[FASE-FUNIL]_[YYYY-MM]
```
Exemplos:
- `GOOGLE_SEARCH_CONV_BRANDED_BOFU_2026-03`
- `GOOGLE_SEARCH_CONV_POTES-HERMETICOS_BOFU_2026-03`
- `GOOGLE_DISPLAY_RETARGETING_VISITORS-30D_BOFU_2026-03`
- `GOOGLE_PMAX_CONV_ALL_FULL-FUNNEL_2026-04`

---

## KPIs de Referência

| KPI | Search | Display | PMax | Meta GB |
|---|---|---|---|---|
| CTR | 3-5% | 0.3-0.5% | 1-3% | Search >3%, Display >0.3% |
| CPC | R$0.50-3.00 | R$0.10-1.00 | R$0.30-2.00 | <R$2.00 |
| CPA | Varia | Alto (awareness) | Target CPA | <R$35 (aprendizado) |
| ROAS | >3x | >1.5x (retarg.) | >3x | >3x |
| Quality Score | 7-10 | — | — | >7 |
| Impression Share | >60% branded, >30% genérico | — | — | — |

---

## Limitações (L1 Observer + API pendente)

- ❌ API não integrada — análise depende de dados exportados ou screenshots
- ❌ Spark NÃO executa mudanças — recomenda ao Kobe
- ❌ Spark NÃO cria campanhas — estrutura e propõe ao Kobe
- ✅ Spark analisa, diagnostica, recomenda e reporta
- ✅ Spark pode analisar dados exportados (CSV/screenshot) enquanto API não estiver pronta
- ✅ Spark pode usar Google Trends para validar volume de busca (acesso público)

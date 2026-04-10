# Skill: Meta Ads — Spark v2.0

_Análise, diagnóstico, otimização e relatórios de Meta Ads (Facebook + Instagram)._

---

## Quando usar
- Analisar performance de campanhas Meta Ads da GB
- Diagnosticar queda de performance (CPA subindo, CTR caindo, frequência alta)
- Recomendar otimizações (pausar, escalar, trocar criativo, ajustar público)
- Gerar relatórios (diário, semanal, mensal)
- Avaliar criativos e detectar fadiga
- Projetar gastos e resultados
- Estruturar novas campanhas e públicos
- Analisar breakdowns (idade, gênero, posicionamento, device)

## Contas e IDs

| Item | Valor |
|---|---|
| Ad Account | `act_323534883953033` (GB Distribuição) |
| Business Manager ID | `7723008527787239` |
| App | KOBE.OPENCLAW (`3582660648568553`) |
| API Version | `v21.0` |
| Base URL | `https://graph.facebook.com/v21.0/` |
| Token | 1Password → Vault "OpenClaw" → "Meta Ads API - KOBE.OPENCLAW" |
| Token expira | ~2026-05-15 (long-lived 60 dias) |

---

## Scripts disponíveis (via Kobe)

O Spark não executa scripts diretamente (L1 Observer). Solicita ao Kobe que execute:

| Script | O que faz | Como solicitar |
|---|---|---|
| `skills/marketing/meta-ads/scripts/meta-ads-report.py` | Relatório de performance (7/30/90 dias) | "Kobe, preciso de um pull de dados Meta últimos [X] dias, nível [campaign/adset/ad]" |
| `skills/marketing/meta-ads/scripts/meta-ads-create.py` | Criar campanha completa | "Kobe, recomendo criar campanha [specs]. Aprovas pra execução?" |
| `skills/marketing/meta-ads/scripts/meta-ads-rules.py` | Regras automatizadas | "Kobe, recomendo ativar regra [specs]. Aprovas?" |

**Quando solicitar dados ao Kobe, especificar:**
- Período (últimos 7d, 14d, 30d, custom)
- Nível de granularidade (campaign, adset, ad)
- Breakdowns necessários (age, gender, placement, device, region)
- Métricas específicas além das padrão (se aplicável)

---

## Framework de Análise

### Análise de Campanha (quando Kobe pede diagnóstico)

1. **Puxar dados** — solicitar ao Kobe o report do período relevante
2. **Métricas obrigatórias por nível:**

| Nível | Métricas |
|---|---|
| Campaign | spend, impressions, clicks, CTR, CPC, CPM, conversions, CPA, ROAS, frequency, reach |
| Ad Set | tudo acima + cost_per_unique_click, unique_CTR, audience_size, delivery_status |
| Ad | tudo acima + quality_ranking, engagement_rate_ranking, conversion_rate_ranking |

3. **Aplicar framework:** Atual → Meta → Gap → Ação → Impacto
4. **Classificar status:** 🟢 🟡 🔴 ⚪ por métrica
5. **Consultar playbook.md** antes de recomendar (não reinventar)
6. **Consultar lessons.md** antes de sugerir (não repetir erro)
7. **Contextualizar:** comparar com período anterior e com sazonalidade (business.md)

### Análise de Breakdowns (quando performance não é óbvia)

Solicitar ao Kobe dados com breakdowns para identificar onde o problema (ou oportunidade) está:

| Breakdown | O que revela | Quando solicitar |
|---|---|---|
| **age + gender** | Qual demografia converte melhor/pior | CPA variando muito entre ad sets com mesmo criativo |
| **placement** | Feed vs Stories vs Reels vs Audience Network | CTR ou CPA muito diferente do esperado |
| **device** | Mobile vs Desktop | Taxa de conversão da LP suspeita |
| **region** | Estados/cidades com melhor performance | Budget alto e busca de segmentação geográfica |
| **hourly** | Horários de pico de conversão | Otimização de delivery schedule |

**Regra:** Só solicitar breakdown quando necessário para diagnóstico. Não puxar todos os breakdowns em toda análise — consome cota de API sem necessidade.

---

## Estratégia de Públicos

### Camadas de público (do mais quente ao mais frio)

| Camada | Tipo | Tamanho esperado | CPA esperado | Prioridade |
|---|---|---|---|---|
| **1. Retargeting** | Custom Audience (visitantes site 30d, engajamento IG/FB) | Pequeno | Mais baixo | Alta |
| **2. Lookalike de compradores** | LAL 1% de quem comprou | Médio | Baixo-médio | Alta |
| **3. Lookalike de engajamento** | LAL 1-2% de quem engajou com perfil/ads | Médio-grande | Médio | Média |
| **4. Interesses** | Organização, cozinha, casa, utilidades domésticas | Grande | Médio-alto | Média |
| **5. Broad** | Sem segmentação (confia no algoritmo) | Muito grande | Variável | Baixa (testar com cautela) |

**Regras de público:**
- Começar pelas camadas mais quentes (1-2) com budget menor
- Expandir para camadas frias (3-5) conforme valida CPA
- Excluir compradores dos últimos 30d de campanhas de prospecção (evitar gastar para quem já comprou)
- Excluir públicos entre si para evitar overlap (Retargeting exclui LAL, LAL exclui Interesses)

### Construção de Custom Audiences (solicitar ao Kobe)

| Fonte | Audience | Uso |
|---|---|---|
| Pixel (Purchase) | Compradores últimos 30/60/90d | Base para LAL + excluir de prospecção |
| Pixel (ViewContent) | Visitantes de produto últimos 7/14d | Retargeting quente |
| Pixel (AddToCart) | Abandono de carrinho últimos 7d | Retargeting altíssima intenção |
| Instagram | Engajamento perfil últimos 30/90d | Base para LAL |
| Facebook Page | Engajamento página últimos 30/90d | Base para LAL |
| Lista de clientes | Upload de email/telefone | Base para LAL + retargeting |

**Dependência:** Pixel precisa estar disparando eventos corretamente. Verificar em `accounts.md`.

---

## Consciência de Privacidade (iOS 14+ / ATT)

Impacta diretamente a qualidade dos dados do Meta Ads:

| Impacto | O que muda | Como lidar |
|---|---|---|
| Atribuição reduzida | Conversões podem ser sub-reportadas (até 30% menos) | Usar janela de atribuição 7-day click como padrão |
| Eventos limitados | Máximo 8 eventos de conversão por domínio | Priorizar: Purchase > AddToCart > ViewContent |
| Dados demográficos | Breakdowns de idade/gênero menos confiáveis | Usar com cautela, cruzar com dados do marketplace |
| Públicos menores | Custom Audiences perdem usuários que optaram out | LAL pode ficar menos preciso |

**Regra prática:** Quando ROAS medido pelo Meta parece baixo mas vendas no marketplace estão subindo, considerar que o Meta está sub-reportando. Cruzar com dados de UTM no GA4 (quando integrado).

---

## Estrutura de Campanha Recomendada para GB

### Estrutura inicial (Fase Aprendizado — R$900/mês Meta)

```
META ADS — GB Importadora
│
├── CAMPANHA 1: META_CONV_RETARGETING_BOFU_[MÊS]
│   Budget: R$180/mês (~R$6/dia)
│   Objetivo: Conversão (Purchase)
│   Ad Sets:
│   ├── Visitantes site 7d (excluir compradores 30d)
│   └── Engajamento IG/FB 30d (excluir compradores 30d)
│
├── CAMPANHA 2: META_CONV_LAL-COMPRAS_BOFU_[MÊS]
│   Budget: R$360/mês (~R$12/dia)
│   Objetivo: Conversão (Purchase)
│   Ad Sets:
│   ├── LAL 1% compradores (excluir retargeting + compradores)
│   └── LAL 2% compradores (excluir LAL 1% + retargeting + compradores)
│
├── CAMPANHA 3: META_CONV_INTERESSES_MOFU_[MÊS]
│   Budget: R$270/mês (~R$9/dia)
│   Objetivo: Conversão (Purchase ou AddToCart)
│   Ad Sets:
│   ├── Interesses: organização + cozinha + casa
│   └── Interesses: decoração + utilidades domésticas
│
└── CAMPANHA 4: META_REACH_BROAD_TOFU_[MÊS]
    Budget: R$90/mês (~R$3/dia)
    Objetivo: Alcance/Tráfego
    Ad Sets:
    └── Broad (25-55, feminino, BR) — deixar algoritmo otimizar
```

**Nota:** Estrutura é referência. Ajustar conforme dados reais. Não lançar tudo de uma vez — começar por Campanha 1 e 2, validar, depois expandir.

---

## Detecção de Fadiga Criativa

| Sinal | Threshold | Nível | Ação |
|---|---|---|---|
| Frequência > 2.5 + CTR estável | Atenção | 🟡 | Preparar novos criativos (briefing ao Kobe) |
| Frequência > 3.0 | Preparar refresh | 🟡 | Novos criativos prontos para subir |
| Frequência > 3.0 + CTR queda >15% em 7d | Trocar criativo urgente | 🔴 | Subir novo criativo imediatamente |
| Frequência > 4.0 | Pausar imediatamente | 🔴 | Pausar criativo atual, subir substituto |

### Matriz de Performance Criativa

Quando analisar criativos, classificar cada ad nesta matriz:

```
                    CTR Alto
                       │
         ⭐ WINNER     │    🧪 TESTER
         (escalar)     │    (bom hook, LP ruim?)
                       │
  ──────────────────────┼──────────────────────
                       │
         💀 CORTAR     │    🤔 REVISAR
         (não funciona)│    (converte mas não atrai)
                       │
                    CTR Baixo

       ROAS Baixo ─────┼───── ROAS Alto
```

- **⭐ WINNER (CTR alto + ROAS alto):** Escalar budget. Usar como referência para novos criativos.
- **🧪 TESTER (CTR alto + ROAS baixo):** Hook funciona mas não converte. Investigar: LP? Público errado? Preço?
- **🤔 REVISAR (CTR baixo + ROAS alto):** Converte quem clica, mas pouca gente clica. Melhorar thumb/gancho.
- **💀 CORTAR (CTR baixo + ROAS baixo):** Pausar. Não funciona em nenhuma dimensão.

**Formato de briefing para novo criativo:**
```
⚡ BRIEFING CRIATIVO — [produto]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Campanha: [nome]
📊 Motivo: [fadiga criativa / CTR em queda / teste A/B / novo lançamento]
🎯 Público: [persona / segmento]
📐 Formato: [1080x1080 / 1080x1920 / vídeo 15s / carrossel]
📍 Posicionamento: [feed / stories / reels / todos]
💡 Mensagem principal: [o que comunicar — baseado em dados]
🎬 CTA: [ação desejada]
✅ Referência: [ad anterior que funcionou + métricas: CTR X%, ROAS Xx]
🚫 Evitar: [o que os dados mostram que não funciona]
📅 Deadline: [quando precisa estar pronto]
```

---

## Relatórios

### Snapshot Diário (para Kobe)
```
⚡ SPARK — SNAPSHOT DIÁRIO Meta Ads
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Data: [hoje]
💰 Spend hoje: R$X | Acumulado mês: R$Y / R$900 (X%)
📈 Projeção fim mês: R$X (🟢 dentro / 🟡 acima / 🔴 muito acima)

| Campanha | Spend | CPA | ROAS | CTR | Freq | Status |
|---|---|---|---|---|---|---|
| [nome] | R$X | R$X | Xx | X% | X.X | 🟢/🟡/🔴 |
| [nome] | R$X | R$X | Xx | X% | X.X | 🟢/🟡/🔴 |
| **Total** | **R$X** | **R$X** | **Xx** | **X%** | — | — |

📌 Alertas: [se houver — ou "Nenhum"]
🔄 Mudanças vs ontem: [o que mudou significativamente]
⏭️ Recomendação: [se aplicável — ou "Manter curso"]
```

### Report Semanal (para Pedro via Kobe — duas versões)

**Versão técnica (para Kobe):**
- Performance consolidada 7 dias por campanha/adset
- Top 3 e Bottom 3 por ROAS e CPA
- Análise de breakdowns relevantes
- Search/frequency trends
- Budget: gasto vs planejado vs projeção
- Recomendações com justificativa técnica

**Versão negócio (para Kobe repassar ao Pedro):**
- Quanto gastou, quanto rendeu, saldo positivo ou negativo
- O que funcionou em linguagem simples
- O que precisa de atenção
- Quanto vai custar/render no ritmo atual
- Top 3 ações para semana seguinte com impacto esperado em R$

---

## Naming Convention

```
META_[OBJETIVO]_[PÚBLICO]_[FASE-FUNIL]_[YYYY-MM]
```
Exemplos:
- `META_CONV_LAL1%-COMPRAS_BOFU_2026-03`
- `META_CONV_RETARGETING-7D_BOFU_2026-03`
- `META_REACH_INTERESSES-COZINHA_TOFU_2026-03`
- `META_CONV_INTERESSES-DECO_MOFU_2026-04`

---

## KPIs de Referência

| KPI | Benchmark mercado | Meta GB (Aprendizado) | Meta GB (Escala) |
|---|---|---|---|
| ROAS | 2.2x mediana | >3x | >10x |
| CTR | 0.8–1.5% | >0.8% | >1.2% |
| CPM | R$15–40 | <R$30 | <R$20 |
| CPC | R$0.50–2.00 | <R$2.00 | <R$1.00 |
| CPA | Varia por setor | <R$35 | <R$17.50 |
| Frequência | 1.5–2.5 | <3.0 | <2.0 |
| Hook Rate (vídeo) | 25-35% | >25% | >35% |

---

## Limitações (L1 Observer)

- ❌ Spark NÃO executa scripts — solicita ao Kobe
- ❌ Spark NÃO modifica campanhas — recomenda ao Kobe
- ❌ Spark NÃO publica criativos — envia briefing ao Kobe
- ❌ Spark NÃO cria públicos — especifica e solicita ao Kobe
- ✅ Spark analisa, diagnostica, recomenda e reporta
- ✅ Spark pode cruzar dados com business.md para contextualizar

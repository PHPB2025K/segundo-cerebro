---
title: "campaign-guide"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/meta-ads
---
# Guia de Criação de Campanhas — Meta Ads
**Conta:** act_323534883953033 (GB Distribuição)

---

## Estrutura Hierárquica

```
Business Manager (7723008527787239)
└── Ad Account (act_323534883953033)
    └── Campaign (objetivo, budget CBO, bid strategy)
        └── Ad Set (público, budget ABO, placement, schedule)
            └── Ad (criativo + copy + CTA)
                └── Ad Creative (imagem/vídeo + texto)
```

**Regra de ouro:** Cada nível depende do anterior. Sempre criar de cima para baixo.

---

## Objetivos ODAX — Quando usar cada um

### OUTCOME_SALES (mais usado para GB)
- **O que otimiza:** Compras, conversões no site
- **Evento ideal:** Purchase via Pixel
- **Quando usar:** Produto já tem demanda, Pixel instalado, >30 compras/mês
- **Estrutura típica:** CBO + Broad + evento Purchase
- **KPI:** ROAS > 3x, CPP < 30% do ticket

### OUTCOME_TRAFFIC
- **O que otimiza:** Visitas ao site, Landing Page Views
- **Quando usar:** Lançamento sem histórico de Pixel, produto novo, awareness com CTA
- **Evento:** Landing Page Views (melhor que Link Clicks — filtra bots)
- **KPI:** CPC < R$1.50, CTR > 1%

### OUTCOME_AWARENESS
- **O que otimiza:** Alcance, Ad Recall Lift
- **Quando usar:** Branding da Budamix, lançamento de nova linha
- **KPI:** CPM < R$25, Frequência 2–4x
- **Nota:** Não medir por ROAS — é investimento de marca

### OUTCOME_ENGAGEMENT
- **O que otimiza:** Curtidas, comentários, compartilhamentos, mensagens
- **Quando usar:** Construir social proof antes de escalar conversão
- **KPI:** Custo por Engajamento, % de positivos

### OUTCOME_LEADS
- **O que otimiza:** Preenchimento de formulário
- **Quando usar:** Captar contatos B2B, newsletters
- **KPI:** CPL < R$30 (depende do ticket)

---

## Checklist Antes de Criar

- [ ] Pixel instalado e disparando Purchase events?
- [ ] Page do Facebook ativa e sem restrições?
- [ ] Conta de anúncios sem policy violations?
- [ ] Método de pagamento válido na conta?
- [ ] Criativos prontos (imagem/vídeo + copy)?
- [ ] Naming convention definido?
- [ ] Budget aprovado?

---

## Templates de Campanha — GB Importadora

### Template 1: Campanha de Vendas CBO (principal)
```
Campaign: BUDAMIX_SALES_POTES-HERMETICOS_CBO_[Mês][Ano]
├── Objetivo: OUTCOME_SALES
├── Budget: R$150–500/dia (CBO)
├── Bid Strategy: LOWEST_COST_WITHOUT_CAP
│
├── Ad Set 1: POTES_BR_25-55_BROAD_PURCHASE
│   ├── Targeting: Brasil, 25–55 anos, sem interesses (broad)
│   ├── Optimization: OFFSITE_CONVERSIONS → Purchase
│   ├── Placement: Automatic (Advantage+ Placements)
│   └── Status: PAUSED (ativar após revisão)
│
├── Ad Set 2: POTES_BR_25-55_LAL1PCT_PURCHASE
│   ├── Targeting: Lookalike 1% de compradores
│   ├── Optimization: OFFSITE_CONVERSIONS → Purchase
│   └── Status: PAUSED
│
└── Ad Set 3: POTES_BR_25-55_RETARGETING_PURCHASE
    ├── Targeting: Custom Audience - Visitantes 30d - excluir compradores
    ├── Optimization: OFFSITE_CONVERSIONS → Purchase
    └── Status: PAUSED
```

### Template 2: Campanha de Testes ABO
```
Campaign: BUDAMIX_TEST_POTES_ABO_[Mês][Ano]
├── Objetivo: OUTCOME_SALES
├── Budget: SEM budget na campanha (ABO)
│
├── Ad Set A: POTES_BROAD_VARIACAO-A (R$50/dia)
├── Ad Set B: POTES_INTERESSES-COZINHA_VARIACAO-A (R$50/dia)
└── Ad Set C: POTES_LAL1PCT_VARIACAO-A (R$50/dia)
```

### Template 3: Campanha de Awareness Budamix
```
Campaign: BUDAMIX_AWARENESS_BRAND_[Mês][Ano]
├── Objetivo: OUTCOME_AWARENESS
├── Budget: R$50–100/dia
│
└── Ad Set: BRAND_BR_25-45_BROAD_REACH
    ├── Targeting: Brasil, 25–45 anos
    ├── Optimization: REACH
    └── Placement: Feed + Instagram + Reels
```

---

## Placements (Posicionamentos)

### Advantage+ Placements (recomendado)
Meta escolhe automaticamente os melhores placements. Geralmente melhor ROAS que seleção manual.

```json
"destination_type": "WEBSITE"
// Não especificar publisher_platforms — Meta decide
```

### Manual (quando usar)
- Testar performance por placement
- Criativos específicos para Stories/Reels (9:16)
- Excluir Audience Network (menor qualidade)

```json
{
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed", "marketplace"],
  "instagram_positions": ["stream", "reels"]
}
```

### Benchmarks por Placement (BR, e-commerce)
| Placement | CPM | CTR | Notas |
|---|---|---|---|
| Facebook Feed | R$18–35 | 1.0–2.0% | Alto intent, desktop+mobile |
| Instagram Feed | R$20–40 | 0.8–1.5% | Mais visual, mobile |
| Reels | R$12–25 | 0.5–1.2% | Crescendo, nativo vertical |
| Stories | R$15–30 | 0.3–0.8% | Swipe up, vertical |
| Marketplace | R$10–20 | 1.5–3.0% | Alta intent de compra |
| Audience Network | R$5–15 | 0.2–0.5% | Qualidade menor |

---

## Buying Type: Auction vs Reach & Frequency

### Auction (padrão — usar sempre para performance)
- Leilão em tempo real
- Flexibilidade total de budget
- Escala e pausa quando quiser
- **Usar para:** Sales, Traffic, Leads, Engagement

### Reach & Frequency
- CPM fixo, alcance garantido
- Requer commitment antecipado ($10k+)
- Controle de frequência preciso
- **Usar para:** Lançamento de produto, campanhas de Awareness com budget garantido

---

## Fases de uma Campanha

### Fase 1: Learning (dias 1–14)
- Status: "Learning" no Ads Manager
- Performance instável — CPA pode ser alto
- **NÃO MEXER EM NADA**
- Objetivo: 50 eventos de otimização por Ad Set/semana

### Fase 2: Estabilização (dias 15–30)
- Status: sai do "Learning"
- Performance começa a se estabilizar
- Pode fazer ajustes conservadores (máx 20% de budget)
- Avaliar criativos: quais têm melhor CTR/ROAS?

### Fase 3: Escala (dia 30+)
- Aumentar budget 20% a cada 3–5 dias
- Testar novos criativos mantendo os vencedores
- Lançar novos Ad Sets com variações de targeting
- Monitorar frequência → >3 = renovar criativos

### Fase 4: Fadiga
- CTR cai progressivamente
- Frequência > 4–5
- ROAS começa a cair
- Ação: Renovar criativos, ampliar audiência, pausar Ad Sets fracos

---

## Decisões Comuns

### CBO ou ABO?
- **Teste inicial:** ABO — controle igual por variação, saiba o que gastou em cada
- **Escala:** CBO — Meta otimiza distribuição, mais eficiente
- **Híbrido:** CBO com budget mínimo por Ad Set

### Broad vs. Interesses?
- **Conta com histórico (>50 compras/mês):** Broad — Meta tem dados suficientes
- **Conta nova / produto novo:** Interesses — guiar o algoritmo inicialmente
- **Budget baixo (<R$100/dia):** Interesses — menos desperdício explorando

### Quantos criativos por Ad Set?
- **Mínimo:** 2–3 (Meta precisa de variação para testar)
- **Ideal:** 3–5 (variar formatos: imagem + vídeo + carrossel)
- **Máximo útil:** 10 (mais que isso não costuma acrescentar)

---

## Naming Convention — GB Importadora

```
Campaign:   [MARCA]_[OBJETIVO-CURTO]_[PRODUTO]_[TIPO]_[MêsAno]
AdSet:      [PRODUTO]_[REGIÃO]_[FAIXA-ETÁRIA]_[PÚBLICO]_[EVENTO]
Ad:         [PRODUTO]_[FORMATO]_[VARIAÇÃO]_[MêsAno]

MARCA:    BUDAMIX | GB
OBJETIVO: SALES | TRAFFIC | AWARENESS | LEADS
PRODUTO:  POTES | KITS | VIDROS | COMBO
TIPO:     CBO | ABO | TEST | RETARG
MêsAno:   Mar2026, Abr2026...
PÚBLICO:  BROAD | LAL1PCT | LAL3PCT | RETARG | INTEREST
EVENTO:   PURCHASE | ADDTOCART | LPV | REACH
FORMATO:  IMG | VID | CAR (carrossel)

Exemplos:
  BUDAMIX_SALES_POTES_CBO_Mar2026
  BUDAMIX_TEST_KITS_ABO_Abr2026
  POTES_BR_25-55_BROAD_PURCHASE
  POTES_BR_25-55_LAL1PCT_PURCHASE
  POTES_BR_30-50_RETARG-CART_PURCHASE
  POTES_IMG_OFERTA-LANCAMENTO_Mar2026
  KITS_VID_UNBOXING-01_Mar2026
```

**Por que naming convention importa:**
- Filtrar relatórios por produto/tipo sem abrir cada campanha
- Identificar onde está cada budget no relatório exportado
- Comunicar com agências e analistas sem ambiguidade
- Auditoria histórica: o que foi testado, quando, com qual objetivo

---

## Flags de Atenção

⚠️ **special_ad_categories:** Deve ser `[]` para produtos normais. Para imóveis, crédito, emprego ou questões sociais, usar categorias específicas ou será rejeitado.

⚠️ **promoted_object:** Obrigatório para OUTCOME_SALES com Pixel. Sem isso, sem otimização por conversão.

⚠️ **Status PAUSED por padrão:** Sempre criar pausado. Ativar somente após revisão completa.

⚠️ **Orçamento em centavos:** API usa centavos. R$150/dia = 15000 na API.


## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — agente proprietário desta skill
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis do agente
- [[openclaw/agents/kobe/AGENTS]] — orquestração com sub-agentes
- [[meta/mocs/MOC - Governanca OpenClaw]] — governança da plataforma

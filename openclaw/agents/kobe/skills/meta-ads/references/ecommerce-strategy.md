---
title: "ecommerce-strategy"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/meta-ads
---
# Meta Ads para E-commerce — Estratégia GB Importadora
**Contexto:** GB Importadora, marca Budamix, marketplace-first (ML + Shopee + Amazon)

---

## ⚠️ Problema Fundamental: Meta Ads → Marketplace

**NÃO apontar Meta Ads direto para listings do Mercado Livre (e Shopee/Amazon).**

### Por que não funciona
1. **Sem Pixel:** ML/Shopee/Amazon não permitem Pixel externo nos listings. Zero rastreamento de conversão.
2. **Sem ROAS mensurável:** Sem conversão = algoritmo otimiza por clique, não por venda.
3. **Concorrência interna:** Usuário chega no seu listing e vê produtos do concorrente em destaque. Você pagou para ele ir comprar do outro.
4. **Algoritmo ML não beneficia:** Tráfego externo tem peso diferente no ranking orgânico do ML.
5. **CPP invisível:** Você nunca saberá o custo real por compra.

### Quando PODE fazer sentido (exceções)
- **Lançamento estratégico:** Produto novo precisando de volume inicial de vendas/reviews para ranquear. Custo é investimento de branding (aceitar sem ROI mensurável).
- **Produto super nichado:** Audiência muito específica que quase não existe organicamente no marketplace.
- **Volume de vendas em prova:** Boost temporário para sair do zero (produto novo sem reviews).

---

## Estratégia Recomendada por Prazo

### Curto Prazo (sem loja própria)
Prioridade: plataformas nativas de anúncio dos marketplaces.

```
Mercado Livre → Mercado Ads (Product Ads)
   → ACOS, CTR, ROAS mensuráveis nativamente
   → Tráfego interno já comprador
   
Shopee → Shopee Ads
   → Tem integração parcial com Pixel Meta
   → Nativo da plataforma

Amazon → Sponsored Products / Sponsored Brands
   → Amazon Attribution para tráfego externo (tracking parcial)
   → Mais robusto que ML para anúncios externos
```

### Médio Prazo (com loja própria Budamix)
Criar landing page / loja própria com:
- **Pixel Meta** completo (+ CAPI para iOS 14)
- **Analytics** configurado
- **Checkout** integrado

Então usar Meta Ads com funil completo:
```
Meta Ads → Loja Budamix → Conversão rastreável → ROAS real
```

### Longo Prazo (escala omnichannel)
```
Meta Ads para branding + loja própria (ROAS mensurável)
     ↓
Audiência Budamix engajada (Custom Audiences)
     ↓
ML/Shopee como canal de volume + conveniência
     ↓
Brand loyalty → Lower CAC ao longo do tempo
```

---

## Estrutura de Funil — Quando tiver Loja Própria

### Topo: Prospecção (40–50% budget)
- **Targeting:** Broad (25–55, BR) + LAL 3–5% compradores
- **Objetivo:** Sales ou Traffic
- **Criativo:** Conteúdo que apresenta Budamix, benefícios dos potes
- **Evento:** Purchase (se volume) ou Add to Cart

### Meio: Consideração (20–30% budget)
- **Targeting:** Visitantes site 30–60 dias (excluindo compradores)
- **Objetivo:** Sales
- **Criativo:** Mostrar produto em uso, depoimentos, comparativo
- **ROAS esperado:** 3–5x

### Fundo: Conversão (20–30% budget)
- **Targeting:** Add to Cart 14 dias, Initiate Checkout 7 dias
- **Objetivo:** Sales
- **Criativo:** Urgência, oferta, frete grátis, social proof
- **ROAS esperado:** 5–8x

---

## Métricas sem Loja Própria (Proxy Metrics)

Quando apontando para marketplace (aceito o risco), usar:

```bash
# Adicionar UTMs em todos os links
# https://produto.mercadolivre.com.br/MLB-XXX?utm_source=meta&utm_medium=cpc&utm_campaign=potes-BUDAMIX&utm_content=IMG01

# Monitorar no GA4 (se tiver) ou via ML Analytics:
# - Sessions por source=meta
# - Comparar vendas no período da campanha vs. período anterior
# - Share of Sales antes/depois

# KPIs aproximados para ML sem Pixel
CPC → menor que R$1.50 (eficiência de clique)
CTR → maior que 1% (criativo relevante)
```

---

## Dynamic Product Ads (DPA) — Para Catálogo

Útil quando tiver loja própria com catálogo de produtos.

### Requisitos
- Catálogo de produtos no Meta (Business Manager)
- Pixel disparando ViewContent, AddToCart, Purchase com `content_ids`
- Produto com imagens de qualidade e preço atualizado

### Criação
```bash
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/token")
AC="act_323534883953033"

# Criar campanha DPA
curl -X POST "https://graph.facebook.com/v21.0/$AC/campaigns" \
  -d "name=BUDAMIX_DPA_CATALOGO_Mar2026" \
  -d "objective=OUTCOME_SALES" \
  -d "promoted_object={\"product_catalog_id\":\"{CATALOG_ID}\"}" \
  -d "status=PAUSED" \
  -d "access_token=$TOKEN"
```

### Estratégias DPA
| Estratégia | Targeting | Objetivo |
|---|---|---|
| Broad DPA | Sem Custom Audience | Prospecção via catálogo |
| Retargeting DPA | ViewContent/AddToCart | Mostrar produto exato que o usuário viu |
| Cross-sell DPA | Compradores | Produtos complementares |
| ASC com DPA | Advantage+ | Automação total |

---

## Advantage+ Shopping Campaigns (ASC)

Modo mais automatizado para e-commerce. Meta controla tudo: targeting, placements, criativos.

### Quando usar ASC
✅ Pixel maduro (>30 compras/mês)
✅ Catálogo de produtos estruturado
✅ Criativos variados disponíveis (mín. 3–5)
✅ Quer simplicidade e confiar no algoritmo

### Limitações ASC
- Menos controle sobre onde o budget vai
- Harder para atribuir performance a variação específica
- Requer dados de qualidade (Pixel + CAPI)

### Estrutura ASC (API unificada 2025)
```json
{
  "objective": "OUTCOME_SALES",
  "campaign_type": "SHOPPING",
  "buying_type": "AUCTION",
  "daily_budget": 50000,
  "promoted_object": {
    "pixel_id": "{PIXEL_ID}",
    "custom_event_type": "PURCHASE"
  },
  "special_ad_categories": []
}
```

> **Nota:** API unificada desde maio 2025. Legacy ASC/AAC APIs serão depreciadas Q1 2026 (MAPI v25.0).

---

## Amazon Attribution (Alternativa para Amazon)

A Amazon oferece tracking parcial de tráfego externo.

### Setup
1. Acessar **Amazon Attribution Console** (Seller Central → Brand Analytics → Amazon Attribution)
2. Criar campanha de atribuição
3. Gerar link rastreado para usar no Meta Ads
4. Ver dados no painel da Amazon

### Limitações
- Tracking só de cliques e compras no Amazon (sem checkout abandonado, sem add to cart)
- Dados com delay de 48–72h
- Menos granular que Pixel próprio

### Quando usar
- Produto com ticket alto (>R$150) onde tráfego externo pode fazer sentido
- Construção de brand recognition no Amazon (reviews)
- Complementar Sponsored Products da Amazon

---

## Sazonalidade — Datas para GB Importadora

| Período | Oportunidade | Budget |
|---|---|---|
| **Dia das Mães (maio)** | Kits presente, produtos cozinha | +50–100% |
| **Dia dos Namorados (jun)** | Kits, combos especiais | +30% |
| **Black Friday (nov)** | Liquidação estoque, combos | +100–200% |
| **Natal/Ano Novo (dez)** | Presentes, renovação da cozinha | +80–150% |
| **Dia das Mulheres (mar)** | Organização doméstica, cozinha | +30% |
| **Janeiro** | Reorganização pós-festas, novo ano | Oportunidade subexplorada |

**Estratégia sazonalidade:**
1. Aumentar budget 2–3 semanas antes (Meta precisa de learning time)
2. Criativos temáticos prontos com antecedência
3. Custom Audiences de compradores do ano anterior para retargeting

---

## ROI Estimado — Sem Loja Própria

Para tomada de decisão antes de ter loja própria:

```
Premissas (estimar):
  - CPC Meta: R$1.00
  - Taxa de conversão ML: 1.5% (do clique externo para compra)
  - Ticket médio: R$100
  - Margem bruta: 40%

Cálculo:
  R$1.00 CPC
  → 100 cliques = R$100 gasto
  → 1.5 compras × R$100 = R$150 receita
  → ROAS estimado = 1.5x
  → Margem bruta = R$60
  → Resultado: R$60 receita - R$100 custo ADS = -R$40 (negativo)

Conclusão: Não faz sentido ROI sem loja própria.
Exceção: aceitar como custo de branding/lançamento.
```

---

## Roadmap de Implementação

### Fase 1: Preparação (sem Meta Ads ainda)
- [ ] Criar Page do Facebook para Budamix
- [ ] Criar conta de anúncios verificada
- [ ] Focar em ML Ads e Shopee Ads nativos
- [ ] Documentar métricas baseline dos marketplaces

### Fase 2: Com landing page simples
- [ ] Criar landing page básica (Budamix.com.br ou subdomain)
- [ ] Instalar Pixel Meta
- [ ] Instalar CAPI (server-side)
- [ ] Configurar eventos: PageView, ViewContent, Purchase
- [ ] Criar Custom Audiences iniciais
- [ ] Lançar campanha Traffic para acumular dados do Pixel

### Fase 3: Escala com dados
- [ ] >50 eventos Purchase/mês → ativar otimização por Purchase
- [ ] Criar Lookalike Audiences de compradores
- [ ] Lançar campanha Sales CBO com Broad
- [ ] Configurar regras automáticas (meta-ads-rules.py)
- [ ] Reportar semanalmente (meta-ads-report.py)

### Fase 4: Funil completo
- [ ] Loja própria completa com checkout
- [ ] DPA com catálogo de produtos
- [ ] ASC para automação máxima
- [ ] Integração CRM → Custom Audiences
- [ ] Dashboard de atribuição (Meta vs. GA vs. vendas reais)

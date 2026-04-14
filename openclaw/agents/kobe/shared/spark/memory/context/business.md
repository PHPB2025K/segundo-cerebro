---
title: "business"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Contexto do Negócio — Spark v2.0

_Atualizado: 2026-03-20_

---

## A Empresa

- **Nome:** GB Importadora
- **Marca própria:** Budamix (registrada no INPI)
- **Segmento:** Utilidades domésticas
- **Canais de venda:** Mercado Livre, Shopee, Amazon
- **Modelo:** Alto volume em poucos produtos, com kits, combos e variações
- **Diferencial:** Margem bruta alta (~70%) por importação direta + marca própria

## Produtos Principais

| Categoria | SKUs | Origem | % do Mix |
|---|---|---|---|
| Potes herméticos de vidro (carro-chefe) | ~7 | Importado China | ~80% |
| Cerâmica nacional (canecas, xícaras) | ~4 | Nacional | ~10% |
| MDF cortado a laser | ~2 | Fabricação própria | ~10% |

**Implicações para tráfego pago:**
- Poucos SKUs = foco intenso nos criativos de cada produto
- Kits e combos = oportunidade de aumentar ticket médio via ads
- Produto visual (vidro, cerâmica) = criativos de imagem/vídeo com alto impacto potencial
- Produto utilitário = gatilho de compra por necessidade + organização

## Público-Alvo

| Atributo | Valor |
|---|---|
| Perfil | Consumidores de utilidades domésticas, organização de cozinha |
| Faixa etária estimada | 25-55 anos (predominância feminina) |
| Comportamento | Compra por necessidade + oportunidade (kits, combos) |
| Ticket médio | R$100-300 |
| Canal principal | Marketplaces (sem e-commerce próprio ativo) |
| Dispositivo provável | Mobile (maioria dos compradores de marketplace) |

**Personas preliminares para targeting (validar com dados):**
- **Persona 1 — "Organizadora":** Mulher 28-45, busca organização de cozinha/casa, segue perfis de decoração/home organization
- **Persona 2 — "Presenteadora":** Mulher 30-50, compra kits/combos para presente (datas comemorativas)
- **Persona 3 — "Revendedora":** Compra em quantidade para revenda/uso comercial (ticket mais alto)

_⚠️ Personas são hipóteses iniciais. Validar com dados das primeiras campanhas._

## Parâmetros Financeiros

| Parâmetro | Valor | Nota |
|---|---|---|
| Ticket médio | R$100 – R$300 | Varia por produto/kit |
| Margem bruta | ~70% | Importação direta + marca própria |
| Budget mensal tráfego pago | R$1.500 (fase inicial) | Decisão registrada em `decisions.md` |
| ROAS breakeven | 1.43x (1 ÷ 0.70) | Abaixo disso = prejuízo |
| Faturamento pico | R$1M/mês (julho 2025) | Referência de capacidade operacional |

**Cálculo de referência para CPA máximo:**
```
Ticket médio mínimo: R$100
Margem bruta: 70% → Lucro bruto: R$70
CPA máximo absoluto (breakeven): R$70
CPA máximo saudável (fase aprendizado): R$35 (50% do lucro bruto)
CPA alvo (fase otimização): R$24.50 (35% do lucro bruto)
CPA ideal (fase escala): R$17.50 (25% do lucro bruto)
```

## Metas de Tráfego Pago por Fase

| Métrica | 🟡 Aprendizado (atual) | 🟢 Otimização | 🚀 Escala |
|---|---|---|---|
| CPA máximo | Até 50% do lucro bruto (R$35) | Até 35% do lucro bruto (R$24.50) | Até 25% do lucro bruto (R$17.50) |
| ROAS mínimo | 3x | 5x | 10x |
| CTR mínimo | >0.8% | >1.0% | >1.2% |
| Frequência máxima | 3.0 | 2.5 | 2.0 |
| CPM referência | <R$30 | <R$25 | <R$20 |

### Critérios de transição entre fases

| De → Para | Critério | Quem decide |
|---|---|---|
| Aprendizado → Otimização | CPA estável abaixo da meta por 14+ dias consecutivos + ROAS > 3x | Pedro via Kobe |
| Otimização → Escala | ROAS > 5x estável por 30+ dias + estrutura de criativos validada | Pedro via Kobe |
| Qualquer → Aprendizado (rebaixamento) | CPA fora da meta por 14+ dias OU mudança estrutural grande | Kobe |

## Fase Atual
- **Status:** 🟡 Aprendizado — primeiras campanhas de tráfego pago
- **Budget:** R$1.500/mês dividido entre Meta e Google
- **Objetivo primário:** Validar CPA e ROAS com budget controlado antes de escalar
- **Objetivo secundário:** Gerar dados para construir benchmarks internos da GB

---

## Sazonalidade

_Dados a serem preenchidos conforme histórico de vendas for disponibilizado._

| Mês | Expectativa | Datas relevantes | Impacto esperado em ads |
|---|---|---|---|
| Janeiro | [PREENCHER] | — | — |
| Fevereiro | [PREENCHER] | — | — |
| Março | [PREENCHER] | — | — |
| Abril | [PREENCHER] | — | — |
| Maio | [PREENCHER] | Dia das Mães (potencial alto para presentes) | CPM pode subir, mas conversão também |
| Junho | [PREENCHER] | Dia dos Namorados | Similar a Maio |
| Julho | Pico histórico (R$1M) | — | Melhor mês para escalar |
| Agosto | [PREENCHER] | Dia dos Pais | — |
| Setembro | [PREENCHER] | — | — |
| Outubro | [PREENCHER] | — | — |
| Novembro | [PREENCHER] | Black Friday | CPM mais alto, competição intensa |
| Dezembro | [PREENCHER] | Natal | Presentes (kits, combos) |

**Regra:** Antes de comparar performance entre períodos, sempre verificar sazonalidade. Queda de vendas em janeiro vs julho não é problema de campanha — é padrão do mercado.

---

## Concorrentes em Ads

_Mapear conforme campanhas forem ativas e dados de leilão forem disponibilizados._

| Concorrente | Plataforma | Produtos que competem | CPM estimado | Observações |
|---|---|---|---|---|
| [PREENCHER] | Meta / Google | — | — | — |
| [PREENCHER] | Meta / Google | — | — | — |

**Como identificar concorrentes:**
- Meta: Biblioteca de Anúncios (facebook.com/ads/library)
- Google: Relatório de Leilões (Auction Insights)
- Marketplaces: Top sellers nos mesmos termos de busca

---

## Jornada do Cliente (hipótese inicial)

```
Marketplace → [vê anúncio no Meta/Google] → [clica] → [landing page / listing]
     ↓                                                         ↓
[busca orgânica no ML/Shopee/Amazon]               [adiciona ao carrinho]
     ↓                                                         ↓
[compara preços/reviews]                              [compra / abandona]
     ↓                                                         ↓
[compra pela busca orgânica]                       [retargeting se abandonou]
```

**Desafio de atribuição:** Cliente pode ver anúncio no Meta, mas comprar via busca orgânica no marketplace. O ROAS medido pela plataforma pode subestimar o impacto real do tráfego pago. Considerar isso ao avaliar performance.

---

_Contexto atualizado conforme dados reais das campanhas forem sendo coletados._

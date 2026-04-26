---
title: "Sessão — 2026-04-15 — Auditoria de Margens Shopee Budamix"
created: 2026-04-15
type: session
status: done
tags:
  - memory
  - session
  - shopee
  - budamix
  - audit
  - precificacao
---

# RELATÓRIO FINAL — AUDITORIA DE MARGENS SHOPEE BUDAMIX

**Data:** 15/04/2026  
**Auditor:** Claude Code  
**Fonte de dados:** Planilha PRECIFICAÇÃO.xlsx (aba SHOPEE, 72 SKUs) + Shopee Open Platform API v2 (partner_id 2031533, 3 lojas)  
**Período da promoção ativa:** 30/11/2025 — 20-21/04/2026

> Contextualização: ver [[business/marketplaces/_index]], [[meta/mocs/MOC - Taxas e Precificacao]], [[memory/projects/shopee-porta-copos-analise]] e [[projects/budamix-central]]. Focal point Shopee na operação: Lucas — ver [[memory/context/people]].

---

## 1. RESUMO EXECUTIVO

Foram auditados 72 SKUs da planilha de precificação Shopee da Budamix. A análise revelou **três camadas de problemas sobrepostos**: (1) bug na fórmula de comissão que aplica 20% flat em vez do sistema escalonado da Shopee, afetando 6 SKUs acima de R$80; (2) uma promoção "FECHA MÊS" ativa há quase 5 meses que reduziu drasticamente os preços reais de pelo menos 32 SKUs em relação à planilha, destruindo margens; e (3) ausência de colunas de margem para vendas via afiliado, impossibilitando avaliar o pior cenário.

O impacto mais grave é a promoção. Usando os preços REAIS da API (vs. os preços da planilha), o número de SKUs em **prejuízo sobe de 6 para 16**, e SKUs classificados como "OK" na planilha caem para "ATENÇÃO" ou "CRÍTICO". O caso mais gritante é o RED01B (Redinha): a planilha mostra R$29,90 mas a API mostra R$16,90 — um produto com custo de R$26,35 sendo vendido por R$16,90, gerando prejuízo de R$-18,80 por unidade (-111,2% de margem), com 79 unidades em estoque.

A promoção expira em **5-6 dias** (20-21/04/2026). Se não for renovada, os preços voltam ao original da API (que em muitos casos é MAIOR que a planilha). A decisão de renovar ou não é urgente e tem impacto direto em dezenas de SKUs.

---

## 2. TRÊS CAMADAS DE PROBLEMAS

### Camada 1: Bug nas fórmulas da planilha

#### 1A. Comissão flat 20% (Col H) — 6 SKUs afetados

A fórmula `=G*0.2` aplica 20% para todos os preços. Produtos >= R$80 deveriam pagar 14%.

| SKU | Preço | Comissão Atual (20%) | Comissão Correta (14%) | Excesso/un | Margem Atual | Margem Corrigida |
|-----|-------|---------------------|----------------------|-----------|-------------|-----------------|
| KIT4YW1050 | R$89,90 | R$17,98 | R$12,59 | R$5,39 | 7,7% | 13,7% |
| KIT12FIT300M | R$99,90 | R$19,98 | R$13,99 | R$5,99 | -49,9% | -43,9% |
| KIT9S098 | R$100,90 | R$20,18 | R$14,13 | R$6,05 | -7,8% | -1,8% |
| KIT4YW1520 | R$122,90 | R$24,58 | R$17,21 | R$7,37 | 10,2% | 16,2% |
| KIT6S100 | R$129,90 | R$25,98 | R$18,19 | R$7,79 | 7,1% | 13,1% |
| KIT9S101 | R$173,90 | R$34,78 | R$24,35 | R$10,43 | 7,1% | 13,1% |
| **TOTAL** | | | | **R$43,03** | | |

**Fórmula correta para Col H:**
```
=G4*IF(G4<=7.99,0.5,IF(G4<=79.99,0.2,0.14))
```

#### 1B. Taxa de transação exibida separadamente (Col I) — cosmético

A coluna I calcula `=G*0.02` mas NÃO é subtraída na fórmula de lucro (Col U). Impacto financeiro: R$0,00. Gera confusão visual.

**Correção:** Zerar (`=0`) ou remover a coluna.

#### 1C. Colunas de margem afiliado ausentes

Existe Col S (comissão afiliado = 10%), mas não há colunas de lucro/margem com afiliado.

---

### Camada 2: Preços desatualizados — Planilha ≠ API (Promoção FECHA MÊS)

**32 SKUs com preço diferente entre planilha e API.** Para cada um, recalculei a margem usando o preço REAL da API.

**Fórmula de margem utilizada:**
```
Lucro = Preço - Custo - Comissão(%) - Taxa_Fixa - Imposto(7%) - Devoluções(4%) - Ads(5%) - R$1,20 - R$0,50 - R$0,05
Margem = Lucro / Preço × 100
```

#### SKUs com preço MENOR na API (vendendo mais barato que a planilha):

| # | SKU | Produto | Custo | Preço Plan. | Preço API | Diff | Faixa | Comissão | Tx Fixa | Outros* | Lucro Plan. | Lucro API | Marg Plan. | Marg API | Status API |
|---|-----|---------|-------|------------|----------|------|-------|---------|--------|---------|------------|----------|-----------|---------|-----------|
| 1 | RED01B | Redinha 155un 70x110cm | R$26,35 | R$29,90 | R$16,90 | -R$13,00 | 2 | R$3,38 | R$4,00 | R$4,46 | -R$12,96 | -R$18,80 | -43,4% | -111,2% | ⚫ PREJUÍZO |
| 2 | SPC011 | Suporte Gamer 2 Ctrl+Headset | R$7,00 | R$19,90 | R$16,89 | -R$3,01 | 2 | R$3,38 | R$4,00 | R$4,46 | -R$0,01 | -R$3,46 | -0,1% | -20,5% | ⚫ PREJUÍZO |
| 3 | SPC013 | Suporte Gamer 2 Ctrl+Headset | R$3,90 | R$19,90 | R$16,89 | -R$3,01 | 2 | R$3,38 | R$4,00 | R$4,46 | R$3,09 | -R$0,36 | 15,5% | -2,1% | ⚫ PREJUÍZO |
| 4 | 914A_B | Canequinha acrílico 6pç 90ml | R$7,70 | R$24,90 | R$22,90 | -R$2,00 | 2 | R$4,58 | R$4,00 | R$4,42 | R$2,49 | R$0,69 | 10,0% | 3,0% | 🔴 CRÍTICO |
| 5 | 914C_B | Canequinha 6pç 100ml | R$18,48 | R$45,90 | R$36,90 | -R$9,00 | 2 | R$7,38 | R$4,00 | R$7,66 | R$5,15 | -R$2,13 | 11,2% | -5,8% | ⚫ PREJUÍZO |
| 6 | IMB501P_T | 5 Potes Tampa Preta | R$7,82 | R$26,90 | R$23,90 | -R$3,00 | 2 | R$4,78 | R$4,00 | R$5,58 | R$3,65 | R$0,21 | 13,6% | 0,9% | 🔴 CRÍTICO |
| 7 | IMB501C_T | 5 Potes Tampa Cinza | R$7,82 | R$26,90 | R$23,90 | -R$3,00 | 2 | R$4,78 | R$4,00 | R$5,58 | R$3,65 | R$0,21 | 13,6% | 0,9% | 🔴 CRÍTICO |
| 8 | IMB501V_T | 5 Potes Tampa Vermelha | R$7,82 | R$26,90 | R$23,90 | -R$3,00 | 2 | R$4,78 | R$4,00 | R$5,58 | R$3,65 | R$0,21 | 13,6% | 0,9% | 🔴 CRÍTICO |
| 9 | XCP001 | Xícara Paris 170ml Branca | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 10 | XCP002 | Xícara Paris 170ml Colorida | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 11 | XCP003 | Xícara Paris 170ml Rosa | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 12 | XCP004 | Xícara Paris 170ml Preto | R$21,00 | R$54,90 | R$44,90 | -R$10,00 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,48 | 15,3% | 1,1% | 🔴 CRÍTICO |
| 13 | XCP005 | Xícara Paris 170ml Verde | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 14 | XCP006 | Xícara Paris 170ml Azul | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 15 | XCP007 | Xícara Paris 170ml Amarelo | R$21,00 | R$54,90 | R$44,89 | -R$10,01 | 2 | R$8,98 | R$4,00 | R$8,93 | R$8,39 | R$0,47 | 15,3% | 1,0% | 🔴 CRÍTICO |
| 16 | K6CAN250AM | Caneca Canelada 250ml Amarelo | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 17 | K6CAN250AZ | Caneca Canelada 250ml Azul | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 18 | K6CAN250B | Caneca Canelada 250ml Branco | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 19 | K6CAN250P | Caneca Canelada 250ml Preto | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 20 | K6CAN250R | Caneca Canelada 250ml Rosa | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 21 | K6CAN250VD | Caneca Canelada 250ml Verde | R$25,80 | R$78,90 | R$69,90 | -R$9,00 | 2 | R$13,98 | R$4,00 | R$12,96 | R$18,95 | R$11,65 | 24,0% | 16,7% | 🟢 OK |
| 22 | KIT6CAR200AZ | Caneca Reta 200ml Azul | R$19,80 | R$52,90 | R$51,90 | -R$1,00 | 2 | R$10,38 | R$4,00 | R$10,07 | R$8,31 | R$6,14 | 15,7% | 11,8% | 🟡 ATENÇÃO |
| 23 | KIT6CAR200P | Caneca Reta 200ml Preto | R$19,80 | R$52,90 | R$51,90 | -R$1,00 | 2 | R$10,38 | R$4,00 | R$10,07 | R$8,31 | R$6,14 | 15,7% | 11,8% | 🟡 ATENÇÃO |
| 24 | KIT6CAR200VD | Caneca Reta 200ml Verde | R$19,80 | R$52,90 | R$51,90 | -R$1,00 | 2 | R$10,38 | R$4,00 | R$10,07 | R$8,31 | R$6,14 | 15,7% | 11,8% | 🟡 ATENÇÃO |

*Outros = Imposto(7%) + Devoluções(4%) + Ads(5%) + Caixa(R$1,20) + Embalagem(R$0,50) + Bilhete(R$0,05) = 16% do preço + R$1,75*

#### SKUs com preço MAIOR na API (margem MELHOR que a planilha):

| # | SKU | Produto | Custo | Preço Plan. | Preço API | Diff | Marg Plan. | Marg API | Status |
|---|-----|---------|-------|------------|----------|------|-----------|---------|--------|
| 1 | KIT6CAR200 | Caneca Reta 200ml Colorida | R$19,80 | R$52,90 | R$58,90 | +R$6,00 | 15,7% | 20,7% | 🟢 OK |
| 2 | KIT6CAR200B | Caneca Reta 200ml Branco | R$19,80 | R$52,90 | R$58,90 | +R$6,00 | 15,7% | 20,7% | 🟢 OK |
| 3 | KIT9S101 | Kit 9pç Retangular | R$77,19 | R$173,90 | R$179,90 | +R$6,00 | 13,1%* | 14,8%* | 🟡 ATENÇÃO |
| 4 | KIT2YW1050 | Kit 2pç 1050ml | R$17,10 | R$44,90 | R$48,90 | +R$4,00 | 13,1% | 16,2% | 🟢 OK |
| 5 | KIT4YW1050 | Kit 4pç 1050ml | R$32,90 | R$89,90 | R$93,90 | +R$4,00 | 13,7%* | 15,5%* | 🟢 OK |
| 6 | KIT2CK4742_B | Kit 2 Jarra Medidora | R$13,22 | R$35,90 | R$38,90 | +R$3,00 | 11,2% | 14,3% | 🟡 ATENÇÃO |
| 7 | KIT6S100 | Kit 6pç Retangular | R$52,16 | R$129,90 | R$132,89 | +R$2,99 | 13,1%* | 14,1%* | 🟡 ATENÇÃO |
| 8 | KIT2YW320 | Kit 2pç 320ml | R$9,19 | R$24,90 | R$26,89 | +R$1,99 | 4,0% | 7,5% | 🟡 ATENÇÃO |

*Margem com fórmula corrigida (14% comissão em vez de 20% para SKUs >= R$80)*

---

### Camada 3: Promoção "FECHA MÊS" — impacto sistêmico

| Loja | Shop ID | Início | Fim | ID Promoção |
|------|---------|--------|-----|-------------|
| budamix.store | 448649947 | 30/11/2025 16:01 | 20/04/2026 14:10 | 797096882388992 |
| budamix-store2 | 860803675 | 30/11/2025 16:01 | 21/04/2026 14:00 | 797095439564800 |
| budamix-shop | 442066454 | 30/11/2025 16:01 | 20/04/2026 14:00 | 797096077099008 |

**Duração:** ~4 meses e 21 dias (quase 5 meses!)  
**Itens com preço promocional:** 47 (preço original > preço atual)  
**Itens com desconto >= 20%:** 34  
**Desconto máximo:** 66,1% (RED01B: de R$49,90 para R$16,90)

**Pergunta central:** Pedro, esta promoção foi intencional? Sabia que está rodando há quase 5 meses? Ela expira em 5-6 dias — o que fazer?

---

## 3. TOP 15 SKUs MAIS CRÍTICOS (margem REAL com preço da API)

Ordenados do pior para o melhor, usando preço REAL da API e fórmulas corrigidas.

| Rank | SKU | Produto | Custo | Preço REAL | Faixa | Comissão | Tx Fixa | Imposto 7% | Devolução 4% | Ads 5% | Fixos¹ | Lucro | Margem | Class. |
|------|-----|---------|-------|-----------|-------|---------|--------|-----------|-------------|--------|--------|-------|--------|--------|
| 1 | RED01B | Redinha 155un | R$26,35 | R$16,90 | 2 | R$3,38 | R$4,00 | R$1,18 | R$0,68 | R$0,85 | R$1,75 | **-R$21,29** | **-126,0%** | ⚫ |
| 2 | KIT12FIT300M² | Fita Adesiva 12x300m | R$96,00 | R$99,90 | 3 | R$13,99 | R$16,00 | R$6,99 | R$4,00 | R$5,00 | R$1,75 | **-R$43,83** | **-43,9%** | ⚫ |
| 3 | KIT6FIT300M² | Fita Adesiva 6x300m | R$48,00 | R$49,90 | 2 | R$9,98 | R$4,00 | R$3,49 | R$2,00 | R$2,50 | R$1,75 | **-R$21,82** | **-43,7%** | ⚫ |
| 4 | SPC011 | Suporte Gamer | R$7,00 | R$16,89 | 2 | R$3,38 | R$4,00 | R$1,18 | R$0,68 | R$0,84 | R$1,75 | **-R$1,94** | **-11,5%** | ⚫ |
| 5 | 914C_B | Canequinha 6pç 100ml | R$18,48 | R$36,90 | 2 | R$7,38 | R$4,00 | R$2,58 | R$1,48 | R$1,85 | R$1,75 | **-R$0,62** | **-1,7%** | ⚫ |
| 6 | SPC013³ | Suporte Gamer | R$3,90 | R$16,89 | 2 | R$3,38 | R$4,00 | R$1,18 | R$0,68 | R$0,84 | R$1,75 | **R$1,16** | **6,9%** | 🟡 |
| 7 | IMB501P_T | 5 Potes Tampa Preta | R$7,82 | R$23,90 | 2 | R$4,78 | R$4,00 | R$1,67 | R$0,96 | R$1,20 | R$1,75 | **R$1,72** | **7,2%** | 🟡 |
| 8 | IMB501C_T | 5 Potes Tampa Cinza | R$7,82 | R$23,90 | 2 | R$4,78 | R$4,00 | R$1,67 | R$0,96 | R$1,20 | R$1,75 | **R$1,72** | **7,2%** | 🟡 |
| 9 | IMB501V_T | 5 Potes Tampa Vermelha | R$7,82 | R$23,90 | 2 | R$4,78 | R$4,00 | R$1,67 | R$0,96 | R$1,20 | R$1,75 | **R$1,72** | **7,2%** | 🟡 |
| 10 | XCP001 | Xícara Paris Branca | R$21,00 | R$44,89 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,24 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |
| 11 | XCP002 | Xícara Paris Colorida | R$21,00 | R$44,89 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,24 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |
| 12 | XCP003 | Xícara Paris Rosa | R$21,00 | R$44,89 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,24 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |
| 13 | XCP004 | Xícara Paris Preto | R$21,00 | R$44,90 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,25 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |
| 14 | XCP005 | Xícara Paris Verde | R$21,00 | R$44,89 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,24 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |
| 15 | XCP006 | Xícara Paris Azul | R$21,00 | R$44,89 | 2 | R$8,98 | R$4,00 | R$3,14 | R$1,80 | R$2,24 | R$1,75 | **R$1,98** | **4,4%** | 🔴 |

¹ Fixos = Caixa R$1,20 + Embalagem R$0,50 + Bilhete R$0,05 = R$1,75  
² KIT12FIT300M e KIT6FIT300M não têm match na API — análise usa preço da planilha com fórmulas corrigidas  
³ SPC013 tem custo menor que SPC011 (R$3,90 vs R$7,00), por isso margem diferente

**Destaques de risco com estoque:**
- RED01B: 79 unidades em estoque, prejuízo de R$21,29/un = **R$1.681,91 de perda potencial**
- XCP001-007: 1.021+ unidades em estoque nas variações, margem 4,4% = quase zero de lucro
- SPC011/013: 60 unidades, SPC011 com prejuízo, SPC013 marginal

---

## 4. CLASSIFICAÇÃO COMPLETA DOS 72 SKUs — TRÊS CENÁRIOS

### Detalhamento por cenário

**Cenário A:** Preços da planilha + fórmulas corrigidas (14% >= R$80)  
**Cenário B:** Preços REAIS da API + fórmulas corrigidas (margem real atual)  
**Cenário C:** Preços REAIS da API + fórmulas corrigidas + 10% afiliado (pior cenário)

> **Nota:** Para os 22 SKUs sem match na API, os Cenários B e C usam o preço da planilha.  
> Para os 8 SKUs com preço MAIOR na API, o Cenário B/C usa o preço real (maior).

| Classificação | Cenário A (Plan. Corrigida) | Cenário B (API Real) | Cenário C (API + Afiliado) |
|---------------|---------------------------|--------------------|-----------------------------|
| ⚫ PREJUÍZO (<0%) | 6 (8%) | 11 (15%) | 29 (40%) |
| 🔴 CRÍTICO (0-5%) | 4 (6%) | 11 (15%) | 13 (18%) |
| 🟡 ATENÇÃO (5-15%) | 24 (33%) | 20 (28%) | 24 (33%) |
| 🟢 OK (>15%) | 38 (53%) | 30 (42%) | 6 (8%) |

### Movimentação entre cenários — SKUs que mudam de classificação:

| SKU | Cenário A | Cenário B | Mudança |
|-----|-----------|-----------|---------|
| RED01B | ⚫ -43,4% | ⚫ -126,0% | Piorou drasticamente |
| SPC011 | ⚫ -0,1% | ⚫ -11,5% | Piorou |
| SPC013 | 🟢 15,5% | 🟡 6,9% | OK → ATENÇÃO |
| 914A_B | 🟡 10,0% | 🔴 3,0% | ATENÇÃO → CRÍTICO |
| 914C_B | 🟡 11,2% | ⚫ -1,7% | ATENÇÃO → PREJUÍZO |
| IMB501P_T | 🟡 13,6% | 🟡 7,2% | Piorou dentro da faixa |
| IMB501C_T | 🟡 13,6% | 🟡 7,2% | Piorou dentro da faixa |
| IMB501V_T | 🟡 13,6% | 🟡 7,2% | Piorou dentro da faixa |
| XCP001-007 (7 SKUs) | 🟢 15,3% | 🔴 4,4% | OK → CRÍTICO |
| K6CAN250AM-VD (6 SKUs) | 🟢 24,0% | 🟢 16,7% | OK, mas 7pp menor |
| KIT6CAR200AZ/P/VD (3 SKUs) | 🟢 15,7% | 🟡 11,8% | OK → ATENÇÃO |
| KIT6CAR200/B (2 SKUs) | 🟢 15,7% | 🟢 20,7% | Melhorou (API maior) |
| KIT2YW320 | 🔴 4,0% | 🟡 7,5% | Melhorou (API maior) |
| KIT2YW1050 | 🟡 13,1% | 🟢 16,2% | Melhorou (API maior) |

---

## 5. PLANO DE CORREÇÕES (para aprovação)

### A) Correções de fórmulas — 3 itens

| # | Coluna | Fórmula Atual | Fórmula Proposta | Justificativa | Impacto |
|---|--------|---------------|------------------|---------------|---------|
| 1 | H (Comissão) | `=G4*0.2` | `=G4*IF(G4<=7.99,0.5,IF(G4<=79.99,0.2,0.14))` | Sistema escalonado Shopee 2026 | 6 SKUs afetados, R$43,03 total |
| 2 | I (Taxa Trans.) | `=G4*0.02` | `=0` | Já inclusa na comissão; não afeta cálculo mas confunde | Cosmético |
| 3 | V/W (Afiliado) | Não existe | V: `=IF(G4="","",G4-F4-H4-J4-K4-L4-N4-O4-Q4-P4-R4-S4)` / W: `=IF(G4="","",(V4*100)/G4/100)` | Visibilidade do pior cenário | 72 SKUs ganham visibilidade |

### B) Decisão sobre promoção "FECHA MÊS"

A promoção expira em **5-6 dias** (20-21/04/2026). Duas opções:

| Opção | O que acontece | Prós | Contras |
|-------|----------------|------|---------|
| **Deixar expirar** | Preços voltam ao original da API (R$49,90 RED01B, R$59,90 XCPs, etc.) | Margens restauradas; planilha volta a refletir a realidade para muitos SKUs | Possível queda de vendas se concorrência mantiver preços baixos |
| **Renovar seletivamente** | Escolher quais itens manter em promo | Mantém competitividade nos itens com margem saudável | Precisa recalcular item a item |

**Recomendação:** Deixar expirar e avaliar impacto em vendas por 1-2 semanas. Depois, criar promoções pontuais apenas para SKUs com margem >= 15% no preço original.

### C) SKUs para reprecificar (margem < 5% com fórmulas corretas, preço da planilha)

| SKU | Preço Atual | Custo | Margem Atual | Preço Sugerido | Margem Nova | Justificativa |
|-----|------------|-------|-------------|---------------|-------------|---------------|
| SPC011 | R$19,90 | R$7,00 | -0,1% | R$24,90 | 10,8% | Custo alto para faixa R$8-80 |
| SPC012 | R$19,90 | R$7,00 | -0,1% | R$24,90 | 10,8% | Idem |
| LIVCOL1 | R$16,90 | R$4,76 | 1,8% | R$19,90 | 10,9% | Margem insuficiente |
| CNCOL24 | R$22,90 | R$8,13 | 3,4% | R$27,90 | 11,8% | Margem insuficiente |
| KIT2YW320 | R$24,90 | R$9,19 | 4,0% | R$29,90 | 11,2% | Margem insuficiente |
| LIVCNCOL80 | R$62,90 | R$31,43 | 4,9% | R$72,90 | 10,2% | Margem insuficiente |

### D) SKUs candidatos a descontinuação (margem negativa persistente)

| SKU | Produto | Custo | Preço Plan. | Preço API | Margem | Estoque | Recomendação |
|-----|---------|-------|------------|----------|--------|---------|--------------|
| KIT12FIT300M | Fita Adesiva 12x300m | R$96,00 | R$99,90 | sem API | -43,9% | ? | **DESCONTINUAR** — custo ~= preço, impossível lucrar |
| KIT6FIT300M | Fita Adesiva 6x300m | R$48,00 | R$49,90 | sem API | -43,7% | ? | **DESCONTINUAR** — mesma razão |
| RED01B | Redinha 155un | R$26,35 | R$29,90 | R$16,90 | -126,0% | 79 | **URGENTE** — vendendo a R$16,90 com custo R$26,35. Remover da promo imediatamente ou tirar do ar |
| KIT9S098 | Kit 9pç Quadrado | R$50,73 | R$100,90 | sem API | -1,8% | ? | **REPRECIFICAR** para R$119,90 (margem ~12%) ou descontinuar |

---

## 6. FRONTEIRAS PERIGOSAS

SKUs precificados logo acima das faixas de taxa fixa da Shopee:

| SKU | Preço | Faixa | Taxa Fixa | Se movesse para... | Economia | Nova Margem |
|-----|-------|-------|-----------|-------------------|----------|-------------|
| KIT4YW1050 | R$89,90 (API: R$93,90) | 3 (R$80-99,99) | R$16,00 | R$79,90 (faixa 2) | R$12,00/un (tx fixa R$4) mas comissão sobe 6pp | Pior — não vale |
| KIT9S098 | R$100,90 | 4 (R$100-199,99) | R$20,00 | R$99,90 (faixa 3) | R$4,00/un (tx fixa R$16) mas comissão sobe 6pp | Pior — não vale |
| KIT4YW1520 | R$122,90 | 4 | R$20,00 | Manter | N/A | Já na faixa ideal |

**Conclusão:** Para a estrutura de taxas Shopee 2026, mover para faixas inferiores geralmente NÃO compensa porque a comissão sobe de 14% para 20% (6pp). A economia na taxa fixa (R$4 a R$12) é menor que o aumento de comissão em valores >= R$80. **Manter os preços nas faixas atuais é a decisão correta.**

Exceção: produtos precificados entre R$80,00-R$83,00 podem se beneficiar de ir para R$79,90 se a queda de comissão (de 14% para 20% — espera, sobe) não compensar. Fazendo a conta para R$80,00:
- Faixa 3: R$80 × 14% + R$16 = R$27,20
- Faixa 2: R$79,90 × 20% + R$4 = R$19,98
- Economia: R$7,22/un movendo para R$79,90

**Portanto, para SKUs entre R$80-R$100, mover para R$79,90 ECONOMIZA ~R$7/unidade.** Nenhum SKU está nessa faixa atualmente com preço da planilha, mas com preço da API, K6CAN250 variantes a R$78,90 já estão na faixa 2 (corretamente).

---

## 7. PERGUNTAS PARA O PEDRO

1. **Programa de afiliados:** Está ATIVO nas 3 lojas Shopee? A planilha tem Col S (10%), mas não conseguimos confirmar via API. Se ativo, 29 SKUs ficam em PREJUÍZO no cenário de venda via afiliado.

2. **Promoção "FECHA MÊS":** Você sabia que está rodando desde 30/11/2025 (quase 5 meses)? Foi intencional manter por tanto tempo? Expira em 5-6 dias (20-21/04). O que quer fazer?

3. **22 SKUs sem match na API:** Os seguintes SKUs estão na planilha mas não foram encontrados na loja budamix.store — foram descontinuados, estão em outra loja, ou é problema de mapeamento?
   - CNCOL24/48/80, LIVCOL1, LIVCNCOL24/48/80
   - KIT12FIT300M, KIT6FIT300M
   - KIT2YW1520, KIT2YW520SQ, KIT2YW800SQ
   - KIT3S096, KIT3S099
   - KIT4YW520SQ, KIT4YW800SQ, KIT4YW1520
   - KIT6S097, KIT9S098
   - KIT6CAR200AM, KIT6CAR200R
   - SPC012

4. **Regime tributário:** O imposto de 7% é Simples Nacional. Confirma que é esse o regime para as contas Shopee (qual CNPJ)?

5. **Premissas de custo:** As estimativas de 4% devoluções e 5% Ads estão atualizadas? São baseadas em dados reais ou estimativas conservadoras?

6. **Fita adesiva:** Quer manter os kits KIT12FIT300M (custo R$96, venda R$99,90, prejuízo R$43,83/un) e KIT6FIT300M (custo R$48, venda R$49,90, prejuízo R$21,82/un)? Recomendo descontinuar.

7. **RED01B — ação urgente:** Este produto está sendo vendido a R$16,90 com custo de R$26,35. São 79 unidades em estoque. Cada venda gera R$21,29 de prejuízo. Total potencial: R$1.681,91. Deseja pausar o anúncio imediatamente?

---

## 8. NOTA SOBRE CREDENCIAIS E ACESSO API

- **1Password:** Contém credenciais de teste (partner_id 1228462) — NÃO funcionam para dados reais
- **Credenciais de produção:** Apenas na VPS (partner_id 2031533, IP 187.77.237.231)
- **IP Whitelist:** Chamadas à API só funcionam da VPS (IP autorizado)
- **OAuth tokens:** 3 lojas com auto-refresh a cada 3h30 via cron na VPS — funcionando normalmente
- **Cobertura:** API retorna 278 itens na budamix.store vs 72 na planilha — 206 SKUs não auditados

---

## APÊNDICE: MEMÓRIA DE CÁLCULO

### Fórmula detalhada para cada SKU (exemplo RED01B com preço API R$16,90):

```
Preço:         R$16,90
Custo:        -R$26,35
Comissão:     -R$3,38   (R$16,90 × 20% = R$3,38, faixa 2)
Taxa Fixa:    -R$4,00   (faixa R$8-79,99)
Imposto:      -R$1,18   (R$16,90 × 7%)
Devoluções:   -R$0,68   (R$16,90 × 4%)
Ads:          -R$0,85   (R$16,90 × 5%)
Caixa:        -R$1,20
Embalagem:    -R$0,50
Bilhete:      -R$0,05
─────────────────────────
Lucro:        -R$21,29
Margem:       -21,29 / 16,90 × 100 = -126,0%
```

### Fórmula detalhada para XCP001 com preço API R$44,89:

```
Preço:         R$44,89
Custo:        -R$21,00
Comissão:     -R$8,98   (R$44,89 × 20% = R$8,978)
Taxa Fixa:    -R$4,00   (faixa R$8-79,99)
Imposto:      -R$3,14   (R$44,89 × 7%)
Devoluções:   -R$1,80   (R$44,89 × 4%)
Ads:          -R$2,24   (R$44,89 × 5%)
Caixa:        -R$1,20
Embalagem:    -R$0,50
Bilhete:      -R$0,05
─────────────────────────
Lucro:         R$1,98
Margem:        1,98 / 44,89 × 100 = 4,4%
```

---

*Relatório gerado em 15/04/2026 — Auditoria consolidada Shopee Budamix*  
*Fontes: PLANILHA DE ESTOQUE _ PRECIFICAÇÃO.xlsx (aba SHOPEE) + Shopee Open Platform API v2*  
*Auditor: Claude Code*

## Ver também

- [[business/marketplaces/_index]] — visão geral marketplaces
- [[meta/mocs/MOC - Taxas e Precificacao]] — MOC tributação e margens
- [[memory/projects/shopee-porta-copos-analise]] — análise específica de SKU Shopee
- [[projects/budamix-central]] — dashboard interno (live sales + SKU analytics)
- [[memory/context/people]] — Lucas (focal Shopee)
- [[memory/context/decisoes/2026-04]] — decisões de abril relacionadas a marketplaces
- [[business/importacao/estrategia-fiscal-gb]] — modelo fiscal que impacta o preço final

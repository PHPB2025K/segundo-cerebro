---
name: amazon-fees-rules
description: Regras completas de comissões, taxas, FBA, frete e custos da Amazon Brasil 2026 para vendedores CNPJ. Base para precificação e estratégia de anúncios. Consultar SEMPRE antes de qualquer cálculo de margem, recomendação de pricing, simulação de lucro ou análise de custo na Amazon. Também ativar quando o usuário mencionar "quanto custa vender na Amazon", "comissão amazon", "taxa amazon", "calcular margem amazon", "precificação amazon", "FBA amazon", "fulfillment amazon", "frete amazon", "buy box", "oferta em destaque", "amazon ads", "sponsored products", "DBA amazon", "FBA onsite", "prime seller", "tarifa logística amazon", ou qualquer variação relacionada a custos e taxas da Amazon Brasil.
triggers:
  - "quanto custa vender na Amazon"
  - "comissão amazon"
  - "taxa amazon"
  - "calcular margem amazon"
  - "precificação amazon"
  - "FBA amazon"
  - "fulfillment amazon"
  - "frete amazon"
  - "buy box"
  - "oferta em destaque"
  - "amazon ads"
  - "sponsored products"
  - "DBA amazon"
  - "tarifa logística amazon"
  - "armazenagem amazon"
  - "prime seller"
metadata:
  openclaw:
    emoji: 📦
    last_updated: "2026-04-10"
    next_review: "2026-04-16"
    cron: "Amazon Fees Monitor — quarta 10h SP"
    sources:
      - url: "https://venda.amazon.com.br/precos"
        status: "✅ Oficial — custos gerais e comissões"
      - url: "https://venda.amazon.com.br/cresca/fba"
        status: "✅ Oficial — FBA tarifas e logística"
      - url: "https://venda.amazon.com.br/cresca/fba/fba-gratis"
        status: "✅ Oficial — promoção FBA Grátis"
      - url: "https://venda.amazon.com.br/cresca/dba"
        status: "✅ Oficial — DBA"
      - url: "https://venda.amazon.com.br/cresca/fba-onsite"
        status: "✅ Oficial — FBA Onsite"
      - url: "https://venda.amazon.com.br/publicidade"
        status: "✅ Oficial — Amazon Ads"
      - url: "https://gosmarter.com.br/taxas-amazon-brasil-2026/"
        status: "✅ Confiável — tabela consolidada"
      - url: "https://gefersonalencar.com.br/2026/02/20/taxas-amazon-brasil-seller-voce/"
        status: "✅ Confiável — análise detalhada"
      - url: "https://ecommercenapratica.com/blog/comissao-amazon/"
        status: "✅ Confiável — comissões"
      - url: "https://www.koncili.com/blog/amazon-altera-tabela-de-tarifas-2/"
        status: "✅ Confiável — tarifas"
---

# Regras de Comissões, Taxas e Custos — Amazon Brasil 2026 (CNPJ)

> ⚠️ **Última atualização:** 10/04/2026
> **Comissões:** sem alteração desde 20/01/2025 (quando 17 categorias tiveram redução de até 3 p.p.)
> **FBA:** promoção agressiva vigente (fev–jul/2026) — tarifa zero para produtos ≥R$100
> **Parcelamento:** desde 16/03/2026, taxa de 1,5% expandida para faixa R$40–100
> **Nenhuma mudança adicional de comissões entre janeiro e abril de 2026.**
> **Cron de verificação:** Quarta-feira 10h SP (Amazon Fees Monitor)
> **Escopo:** Vendedores CNPJ com Plano Profissional.

---

## 1. PLANO DE VENDA

| Característica | Individual | Profissional |
|---|---|---|
| **Mensalidade** | R$ 0 | **R$ 19/mês** (1º ano grátis) |
| **Taxa por item vendido** | **R$ 2,00/item** | R$ 0 |
| Ponto de equilíbrio | — | **10 vendas/mês** |
| FBA | ❌ | ✅ |
| Amazon Ads | ❌ | ✅ |
| Buy Box (Oferta em Destaque) | ❌ | ✅ |
| Upload em massa | ❌ | ✅ |
| Relatórios avançados | ❌ | ✅ |
| Promoções e ofertas | ❌ | ✅ |

> **Para GB Importadora:** Plano Profissional é obrigatório. Sem ele não há FBA, Ads nem Buy Box.
> **R$ 19/mês rateado:** com 100 vendas/mês = R$ 0,19/venda. Desprezível acima de 50 vendas.

---

## 2. COMISSÃO POR CATEGORIA (Referral Fee)

Comissão incide sobre **preço total da venda** (produto + frete + embalagem paga pelo comprador). Mínimo: **R$ 1,00/item** (exceto Indústria: R$ 2,00). Tabela vigente desde 20/01/2025, **sem alteração em 2026**.

### Categorias relevantes para GB Importadora ⭐

| Categoria | Comissão |
|---|---|
| **Casa** ⭐ | **12%** |
| **Cozinha** ⭐ | **12%** |
| **Jardim e Piscina** | 12% |
| **Brinquedos e Jogos** | 12% |
| **Produtos para Bebês** | 12% |
| **Produtos para Animais** | 12% |
| **Esportes, Aventura e Lazer** | 12% |

### Tabela completa

| Categoria | Comissão | Mín. |
|---|---|---|
| Comidas e Bebidas | 10% | R$ 1 |
| Pneus e Rodas | 10% | R$ 1 |
| TV, Áudio e Cinema em Casa | 10% | R$ 1 |
| Bebidas Alcoólicas | 11% | R$ 1 |
| Câmera e Fotografia | 11% | R$ 1 |
| Celulares | 11% | R$ 1 |
| Eletrodomésticos Linha Branca | 11% | R$ 1 |
| Ferramentas e Construção | 11% | R$ 1 |
| Videogames e Consoles | 11% | R$ 1 |
| Casa | 12% | R$ 1 |
| Cozinha | 12% | R$ 1 |
| Eletroportáteis Cuidado Pessoal | 12% | R$ 1 |
| Esportes, Aventura e Lazer | 12% | R$ 1 |
| Instrumentos Musicais | 12% | R$ 1 |
| Jardim e Piscina | 12% | R$ 1 |
| PC (Computadores) | 12% | R$ 1 |
| Peças e Acessórios Automotivos | 12% | R$ 1 |
| Produtos para Animais | 12% | R$ 1 |
| Produtos para Bebês | 12% | R$ 1 |
| Saúde e Cuidados Pessoais | 12% | R$ 1 |
| Brinquedos e Jogos | 12% | R$ 1 |
| Indústria e Ciência | 12% | **R$ 2** |
| Beleza | 13% | R$ 1 |
| Eletrônicos Portáteis | 13% | R$ 1 |
| Papelaria e Escritório | 13% | R$ 1 |
| Relógios | 13% | R$ 1 |
| Bagagem e Acessórios de Viagem | 14% | R$ 1 |
| Beleza de Luxo | 14% | R$ 1 |
| Calçados, Bolsas e Óculos | 14% | R$ 1 |
| Joias | 14% | R$ 1 |
| Roupas e Acessórios | 14% | R$ 1 |
| Livros | 15% | R$ 1 |
| Música (CDs, LPs) | 15% | R$ 1 |
| Vídeo e DVD | 15% | R$ 1 |
| Artesanato (Handmade) | 16% | R$ 1 |
| Demais Categorias | 15% | R$ 1 |

### Categorias com comissão escalonada

| Categoria | Até R$ 100/200 | Acima |
|---|---|---|
| **Acessórios Eletrônicos/PC** | 15% (até R$ 100) | 10% sobre excedente |
| **Móveis** | 15% (até R$ 200) | 10% sobre excedente |

Exemplo Móveis: produto R$ 500 → R$ 30 (15% de R$ 200) + R$ 30 (10% de R$ 300) = **R$ 60** (efetiva 12%).

### Incentivo novos produtos Prime
Comissão reduzida a **5%** nos primeiros 100 itens padrão (ou 50 extragrandes) durante até 120 dias para produtos novos no catálogo com entrega Prime (FBA/FBA Onsite).

---

## 3. TAXAS ADICIONAIS POR VENDA

### 3.1 Taxa de Parcelamento Sem Juros
- **1,5%** sobre o valor total da venda para produtos ≥ R$ 40
- Desde **16/03/2026**: faixa R$ 40–100 passou a pagar (antes isenta)
- Programa **opcional** — vendedor pode desativar por ASIN no Seller Central
- ⚠️ Incluir SEMPRE no cálculo se o parcelamento estiver ativo

### 3.2 Taxa de Administração de Reembolso
- Quando o vendedor faz reembolso, Amazon devolve a comissão mas retém **20% da comissão original**, com teto de **R$ 10,00**
- Exemplo: produto R$ 100 com 12% comissão (R$ 12) → taxa retida = R$ 2,40
- Provisionar ~2-3% do faturamento para devoluções/reembolsos

### 3.3 Taxas que NÃO existem no Brasil
- ❌ Closing fee (taxa de fechamento de mídia)
- ❌ Taxa de armazenagem de itens perigosos
- ❌ Taxa de listagem de alto volume
- ❌ Taxa de processamento de devoluções por categoria
- **Estrutura brasileira é significativamente mais simples que a Amazon EUA/Europa**

---

## 4. MODELOS LOGÍSTICOS (4 opções)

### 4.1 FBA (Fulfillment by Amazon) — Recomendado ⭐
- Estoque nos CDs da Amazon. Amazon separa, embala, envia e atende pós-venda
- **Selo Prime automático** — frete grátis para membros Prime sem custo extra ao vendedor
- Frete de saída (CD → cliente) **incluído na tarifa FBA** — não paga frete separado
- Entrega em 1 dia em 50+ cidades, 2 dias em 100+ cidades
- Amazon reporta que sellers FBA multiplicam vendas em média **5×**
- Requisitos: CNPJ com IE em SP, MG, PR, RJ, SC, RS, CE, DF ou PE

### 4.2 DBA (Delivery by Amazon) — Padrão para novos sellers
- Vendedor armazena e embala; transportadoras Amazon fazem entrega
- **Sem selo Prime**
- Frete grátis ao consumidor: ≥R$ 19 (mesma região) e ≥R$ 79 (inter-regional)
- Comissão incide **apenas sobre preço do produto** (não inclui frete) — vantagem vs FBM
- Tarifas DBA (exemplos SP): R$ 4,50 (<R$ 30), R$ 6,50 (R$ 30–49,99), R$ 6,75 (R$ 50–78,99)

### 4.3 FBA Onsite — Por convite
- Estoque fica no armazém do vendedor, Amazon gerencia logística
- **Selo Prime**
- Peso máx. 30 kg, dimensões máx. 100×100×100 cm
- Tarifas não publicadas (disponíveis no Seller Central)

### 4.4 FBM (Fulfilled by Merchant) — Logística própria
- Vendedor cuida de tudo: armazém, embalagem, envio, devoluções
- **Sem selo Prime** (SFP não existe no Brasil)
- Vendedor configura tabela de frete nas 53 zonas
- Comissão incide sobre preço **+ frete** (encarece a operação)

### Comparativo rápido

| Critério | FBA | DBA | FBA Onsite | FBM |
|---|---|---|---|---|
| Selo Prime | ✅ | ❌ | ✅ | ❌ |
| Frete incluído | ✅ | Parcial | ✅ | ❌ |
| Quem envia | Amazon | Amazon | Amazon | Vendedor |
| Quem armazena | Amazon | Vendedor | Vendedor | Vendedor |
| Buy Box vantagem | Máxima | Moderada | Alta | Baixa |
| Custo operacional | Tarifa FBA | Tarifa DBA | Convite | Frete próprio |

---

## 5. FBA — TARIFAS COMPLETAS

### 5.1 Tarifa de Logística FBA (R$/unidade, vigente desde 01/08/2025)

Peso = real ou cubado (C×L×A ÷ 6.000 + 20g embalagem), o maior. Limite: 22 kg e 105×105×105 cm.

**Produtos ≥ R$ 79:**

| Peso | R$79–99 | R$100–119 | R$120–149 | R$150–199 | ≥R$200 |
|---|---|---|---|---|---|
| 0–100g | 10,05 | 12,05 | 14,05 | 15,05 | 15,55 |
| 100–200g | 10,45 | 12,45 | 14,45 | 15,45 | 16,05 |
| 200–300g | 10,95 | 12,95 | 14,95 | 15,95 | 16,55 |
| 300–400g | 11,45 | 13,45 | 15,45 | 16,95 | 17,15 |
| 400–500g | 11,95 | 13,95 | 15,95 | 17,05 | 17,85 |
| 500–750g | 12,05 | 14,05 | 16,05 | 18,45 | 18,55 |
| 750g–1kg | 12,45 | 14,45 | 16,45 | 19,05 | 19,25 |
| 1–1,5kg | 12,95 | 14,95 | 16,95 | 19,45 | 20,35 |
| 1,5–2kg | 13,05 | 15,05 | 17,05 | 19,95 | 21,35 |
| 2–3kg | 14,05 | 16,05 | 18,05 | 20,05 | 22,35 |
| 3–4kg | 15,05 | 17,05 | 19,05 | 21,95 | 23,35 |
| 4–5kg | 16,05 | 18,05 | 20,05 | 22,95 | 24,35 |
| 5–6kg | 24,05 | 27,05 | 29,05 | 30,05 | 30,35 |
| 6–7kg | 25,05 | 28,05 | 30,05 | 31,05 | 33,35 |
| 7–8kg | 26,05 | 29,05 | 31,05 | 32,05 | 35,35 |
| 8–9kg | 27,05 | 30,05 | 32,05 | 33,05 | 37,35 |
| 9–10kg | 35,05 | 40,05 | 46,05 | 51,05 | 51,35 |
| Kg adicional (>10) | 3,05 | 3,05 | 3,05 | 3,50 | 3,50 |

**Produtos < R$ 79 (fora de promoção):**

| Peso | < R$ 79 |
|---|---|
| 0–100g | 12,95 |
| 100–200g | 13,45 |
| 200–300g | 13,95 |
| 300–400g | 14,45 |
| 400–500g | 14,95 |
| 500–750g | 15,45 |
| 750g–1kg | 15,95 |
| 1–1,5kg | 16,95 |
| 1,5–2kg | 17,95 |
| 2–3kg | 18,95 |
| 3–4kg | 19,95 |
| 4–5kg | 20,95 |
| 5–6kg | 25,95 |
| Kg adicional | 3,05 |

### 5.2 ⚡ Promoção FBA Grátis (fev–jul 2026, ATIVA em abril 2026)

Campanha **"Experimente FBA+"**:

| Perfil | Tarifa Logística | Armazenagem | Coleta |
|---|---|---|---|
| **Novo no FBA** (30 dias) | **R$ 0** | **R$ 0** | **R$ 0** |
| **FBA existente** (c/ 3,5% Ads) | **R$ 0** (≥R$ 100) / **R$ 5** (<R$ 100) | **R$ 0** | **R$ 0** |
| **FBA existente** (s/ Ads) | Tarifa padrão | Tarifa padrão | Tarifa padrão |

> ⚠️ **Condição:** manter investimento de **3,5% do faturamento elegível em Amazon Ads** mensalmente
> ⚠️ **Promoção temporária:** tratar como benefício transitório na precificação. Skill deve permitir alternar entre tarifas promocionais e standard.
> **Vigência:** 01/02/2026 a 31/07/2026

### 5.3 Armazenagem Mensal

| Volume do produto | Tarifa/m³/mês |
|---|---|
| < 10.000 cm³ | **R$ 75,00** |
| ≥ 10.000 cm³ | **R$ 37,50** |

- **Sem variação sazonal** (diferente da Amazon EUA — não tem sobretaxa out-dez)
- Cobrada no mês seguinte ao uso

**Exemplo prático (nossos potes — kit médio ~3.000 cm³):**
- Volume: 0,003 m³ × R$ 75 = **R$ 0,23/mês por unidade**
- Se ficar 30 dias: R$ 0,23. Se ficar 90 dias: R$ 0,68. Custo irrelevante.

### 5.4 Armazenagem de Longa Duração
- **> 365 dias** no CD: adicional de **R$ 525,00/m³/mês** (sobre a tarifa regular)
- NÃO existe cobrança intermediária aos 180 dias (diferente dos EUA)
- **Regra:** girar estoque em até 6 meses. Acima de 12 meses, custo fica proibitivo.

### 5.5 Remoção de Inventário

| Peso | Tarifa/unidade |
|---|---|
| 0–250g | R$ 0,99 |
| 250–500g | R$ 1,04 |
| 500g–1kg | R$ 1,12 |
| 1–2kg | R$ 1,26 |
| 2–3kg | R$ 1,76 |
| 3–4kg | R$ 1,90 |
| 4–5kg | R$ 2,00 |
| 5–10kg | R$ 2,20–R$ 3,60 |
| Kg adicional | R$ 0,17 |

Prazo: ~14 dias úteis (30+ em picos). Itens "não vendáveis" não removidos em 30 dias = descartados.

### 5.6 Tarifa de Coleta (inbound — opcional)
Serviço de coleta Amazon no armazém do vendedor. Varia por peso e estado de origem.
- Exemplo SP: **R$ 0,93 a R$ 9,81 por caixa** (até 30 kg)
- Gratuita na promoção FBA+ vigente

---

## 6. FRETE — QUEM PAGA O QUÊ

| Cenário | Quem paga | Custo para vendedor |
|---|---|---|
| FBA — cliente Prime | **Amazon absorve** | R$ 0 (embutido na tarifa FBA) |
| FBA — cliente não-Prime (≥R$ 129) | Amazon (frete grátis) | R$ 0 |
| FBA — cliente não-Prime (<R$ 129) | Cliente paga frete | R$ 0 |
| DBA — cliente (≥R$ 19 mesmo estado) | Frete grátis | Tarifa DBA |
| DBA — cliente (≥R$ 79 interestadual) | Frete grátis | Tarifa DBA |
| FBM — cliente | Cliente paga (vendedor define) | Frete próprio |

> **Diferença crucial vs ML/Shopee:** No FBA, o vendedor **NÃO paga frete separado**. O custo do frete ao consumidor (incluindo Prime grátis) está incluído na tarifa de logística FBA. Isso simplifica enormemente a precificação.

---

## 7. BUY BOX (Oferta em Destaque)

**~80-90% das vendas na Amazon passam pelo Buy Box.** Sem Buy Box, o produto fica relegado ao link "Outras ofertas" — quase invisível no mobile.

### Critérios de elegibilidade
- Plano Profissional (Individual NÃO pode)
- Produto novo e em estoque
- Métricas em conformidade (ODR < 1%)
- Conta em situação regular

### Critérios de classificação (ordem de importância)
1. **Preço total competitivo** (produto + frete) — não precisa ser o menor
2. **Método de fulfillment** — FBA tem vantagem significativa sobre FBM
3. **Velocidade de entrega** — prazo mais curto ganha prioridade
4. **Métricas de desempenho** — ODR, entrega pontual, cancelamentos
5. **Disponibilidade de estoque** e histórico da conta

> **Regra prática:** FBA + preço competitivo + métricas verdes = Buy Box na maior parte do tempo (~95% de rotação).
> **Sponsored Products exige Buy Box** — se perder elegibilidade, os anúncios param automaticamente.

---

## 8. AMAZON ADS

### 8.1 Sponsored Products (formato principal)
- **Modelo:** CPC via leilão de segundo preço
- **Requisito:** Plano Profissional + elegibilidade ao Buy Box
- **Segmentação:** automática ou manual por palavras-chave
- **Sem investimento mínimo** — vendedor define orçamento diário (recomendação: R$ 50/dia para resultados)
- **Não exige Brand Registry**
- CPC médio Brasil (estimativa): **R$ 0,75–R$ 7,50**

### 8.2 Sponsored Brands
- Banner com logo + headline + até 3 produtos no topo dos resultados
- **Exige Amazon Brand Registry** (marca INPI)
- Formatos: coleção, destaque da loja, vídeo
- CPC médio: **R$ 5,00–R$ 12,50**
- Formato vídeo: CPCs mais baixos, conversão 1,5× maior

### 8.3 Sponsored Display
- Anúncios em páginas de produto, avaliações e fora da Amazon (Twitch, Prime Video)
- Modelos CPC e vCPM
- **Exige Brand Registry** para funcionalidades completas
- CPC médio: **R$ 1,50–R$ 10,00**

### 8.4 Benchmarks de referência

| Métrica | Faixa típica |
|---|---|
| ACOS fase de lançamento | 30%–70% |
| ACOS produto maduro | **10%–20%** |
| ACOS médio geral | ~30% |
| CTR médio | 0,3%–0,6% |
| Taxa de conversão | 8%–15% |

> ⚠️ **Promoção FBA+ exige 3,5% em Ads.** Isso torna Ads praticamente obrigatório para quem quer FBA com tarifa reduzida. Incluir no cálculo de margem.
> **Créditos disponíveis:** até **R$ 5.300 em créditos de Ads** para novos sellers elegíveis.

---

## 9. SAÚDE DA CONTA (Account Health)

### 9.1 Account Health Rating (AHR)
- Pontuação de **0 a 1.000** pontos
- Contas novas: **200 pontos**
- Acima de 200 = saudável. Abaixo de 200 = em risco
- +4 pontos a cada 200 pedidos bem-sucedidos (180 dias)
- -2 a -8 pontos por violação (reincidência dobra)

### 9.2 Métricas obrigatórias

| Métrica | Limite | Janela | Aplica-se a |
|---|---|---|---|
| **ODR (Taxa de Defeito)** | **< 1%** | 60 dias | Todos |
| **Taxa Cancelamento Pré-envio** | **< 2,5%** | 7 dias | FBM/DBA |
| **Taxa Envio Atrasado** | **< 4%** (geral) / **< 2,5%** (DBA) | 30 dias | FBM |
| **Taxa Rastreamento Válido** | **> 95%** | 30 dias | FBM |
| **Entrega Pontual** | **> 97%** (recomendado) | 30 dias | FBM |
| **Insatisfação Devoluções** | **< 10%** | Contínuo | Todos |

> **FBA exclui** métricas de envio (cancelamento, atraso, VTR) — Amazon é responsável.
> **AHR < 100** = suspensão da conta + retenção de fundos por 90 dias.
> **Account Health Assurance:** sellers com AHR ≥ 250 por 6+ meses ganham aviso de 72h antes de desativação.

---

## 10. RECEBIMENTO

### 10.1 Ciclo de pagamento
- Repasse a cada **14 dias** (quinzenal)
- Após entrega confirmada: fundos retidos por **7 dias** (reserva DD+7)
- Transferência bancária: **2–5 dias úteis**
- **Prazo total estimado: 20–28 dias** da venda ao recebimento

### 10.2 Reserva de saldo
- Amazon retém parcela variável para cobrir devoluções/chargebacks
- Percentual não divulgado — varia conforme histórico da conta
- Contas novas: primeiro repasse pode levar **até 30 dias**

### 10.3 Requisitos
- Conta corrente em banco brasileiro, no nome do CNPJ
- Cartão de crédito válido (Visa, MasterCard, Diners)
- Pix/TED: não documentado como opção de saque
- **Antecipação:** referenciada como disponível, mas não documentada publicamente

---

## 11. PROGRAMAS ESPECIAIS (disponíveis no Brasil)

| Programa | Custo | Requisito | Uso |
|---|---|---|---|
| **Amazon Vine** | Grátis (até 2 un.) / R$ 200 (3–10) / R$ 500 (11–30) | Brand Registry + FBA | Reviews de qualidade |
| **Programe e Poupe** | Desconto de até 10% ao consumidor | FBA | Vendas recorrentes |
| **Lightning Deals** | Variável (~US$ 150/deal) | Profissional + ≥3,5 estrelas | Promoções relâmpago |
| **Handmade** | Comissão 16% | Cadastro artesão | Artesanato |
| **Programa de Recompensas** | Grátis | Novo seller + marca | R$ 100–500/produto + créditos |

---

## 12. FÓRMULA DE PRECIFICAÇÃO

### Custo total por venda (FBA, sem promoção, sem Ads)

```
Custo Amazon = Comissão (%) × Preço total
             + Tarifa FBA (lookup: peso × preço)
             + Armazenagem (volume × dias ÷ 30 × tarifa/m³)
             + Taxa parcelamento (1,5% se ≥R$ 40)
             + Mensalidade rateada (R$ 19 ÷ vendas/mês)
```

### Fórmula de preço mínimo

```
Preço mín. = (CMV + Impostos + Tarifa FBA + Armazenagem + Margem)
           / (1 - Comissão% - Parcelamento%)
```

### Exemplo: Kit 5 Potes Vidro — R$ 89,90 (Casa 12%, ~1kg, FBA, sem promo)

| Item | Valor |
|---|---|
| Preço de venda | R$ 89,90 |
| Comissão (12%) | −R$ 10,79 |
| Tarifa FBA (750g–1kg, R$79–99) | −R$ 12,45 |
| Armazenagem (~25 dias, médio) | −R$ 0,19 |
| Taxa parcelamento (1,5%) | −R$ 1,35 |
| Mensalidade rateada (~100 vendas) | −R$ 0,19 |
| **Total custos Amazon** | **R$ 24,97** |
| **% retido pela Amazon** | **27,8%** |
| **Sobra para CMV + lucro** | **R$ 64,93** |

### Mesmo produto com FBA promoção (≥R$ 100, tarifa zero)

Se precificar a R$ 100:

| Item | Valor |
|---|---|
| Comissão (12%) | −R$ 12,00 |
| Tarifa FBA (promo ≥R$ 100) | **R$ 0** |
| Armazenagem (promo) | **R$ 0** |
| Taxa parcelamento (1,5%) | −R$ 1,50 |
| **Total custos Amazon** | **R$ 13,69** |
| **% retido** | **13,7%** |

### Checklist de verificação
1. [ ] Categoria e comissão corretas?
2. [ ] Peso real ou cubado (o maior)?
3. [ ] Incluiu taxa de parcelamento (1,5%) se ≥R$ 40?
4. [ ] Usando tarifa FBA padrão ou promocional?
5. [ ] Incluiu armazenagem (volume × tempo estimado)?
6. [ ] Se usando Ads: incluiu custo de Ads (ACOS 10–30%)?
7. [ ] Se promoção FBA: incluiu 3,5% obrigatório em Ads?
8. [ ] Mensalidade rateada (R$ 19/mês)?

---

## 13. COMPARATIVO AMAZON vs [[skills/marketplace/ml-fees-rules/SKILL|ML]] vs [[skills/marketplace/shopee-fees-rules/SKILL|SHOPEE]] (abril 2026)

| Aspecto | Amazon Brasil | Mercado Livre | Shopee |
|---|---|---|---|
| **Comissão** | 10%–15% | 10%–19% (Clássico/Premium) | 14%–20% |
| **Taxa fixa por venda** | R$ 0 (Profissional) | R$ 5,65–R$ 261 (variável) | R$ 0–R$ 26 (escalonado) |
| **Mensalidade** | R$ 19/mês (1º ano grátis) | R$ 0 | R$ 0 |
| **Fulfillment** | FBA com promoções agressivas | Full (custos em alta) | SFS (em expansão) |
| **Frete grátis** | Prime absorve (vendedor R$ 0) | Custo do vendedor | Subsidiado pela Shopee |
| **Parcelamento** | 1,5% (≥R$ 40) | Embutido no Premium | Não oferece s/juros |
| **Pagamento** | 14 dias + DD+7 | D+2 a D+28 | Após entrega |
| **Tendência custos 2026** | ⬇️ Reduzindo | ⬆️ Aumentando | ⬆️ Aumentando |
| **Visitas mensais** | ~80–100 milhões | ~350 milhões | ~180–240 milhões |
| **Ticket médio** | Mais alto | Alto | Baixo |
| **Buy Box** | Sim (obrigatório) | Não | Não |

> **Regra prática para GB Importadora:**
> - **Produtos <R$ 79:** Amazon é a mais barata (sem taxa fixa)
> - **Produtos R$ 80–199:** Amazon e ML Clássico empatam (~12%)
> - **Produtos ≥R$ 200:** Todos convergem, mas Amazon com FBA promo = menor custo
> - **Volume e visibilidade:** ML ainda é o maior em audiência (350M vs 100M)
> - **Recomendação:** operar nos 3 com precificação diferenciada por canal

---

## 14. MUDANÇAS RECENTES 2026

| Data | Mudança |
|---|---|
| Jan/2026 | Reforma Tributária: campos CBS/IBS obrigatórios na NF-e. FBA calcula automaticamente |
| Fev/2026 | Campanha FBA Grátis: tarifa R$ 0 (≥R$ 100) / R$ 5 (<R$ 100), válida até jul/2026 |
| Fev/2026 | Campanha SP: comissão ZERO por até 5 meses (limite R$ 60.000) para CNPJ com coleta em SP |
| Mar/2026 | Parcelamento sem juros: taxa 1,5% expandida para faixa R$ 40–100 |
| Abr/2026 | Amazon EUA: sobretaxa 3,5% combustível no FBA — NÃO afeta Amazon Brasil doméstico |

---

## 15. URLs DE MONITORAMENTO (Cron Semanal)

| # | Fonte | Status | Nota |
|---|---|---|---|
| 1 | [Amazon Oficial — Preços](https://venda.amazon.com.br/precos) | ✅ Oficial | Comissões e planos |
| 2 | [Amazon Oficial — FBA](https://venda.amazon.com.br/cresca/fba) | ✅ Oficial | Tarifas fulfillment |
| 3 | [Amazon Oficial — FBA Grátis](https://venda.amazon.com.br/cresca/fba/fba-gratis) | ✅ Oficial | Promoção vigente |
| 4 | [Amazon Oficial — DBA](https://venda.amazon.com.br/cresca/dba) | ✅ Oficial | Tarifas DBA |
| 5 | [Amazon Oficial — Ads](https://venda.amazon.com.br/publicidade) | ✅ Oficial | Publicidade |
| 6 | [GoSmarter — Taxas Amazon](https://gosmarter.com.br/taxas-amazon-brasil-2026/) | ✅ Confiável | Consolidado |
| 7 | [Seller Central — Fórum](https://sellercentral.amazon.com.br/seller-forums) | ✅ Oficial | Mudanças anunciadas |

### Protocolo de verificação:
1. Acessar fontes oficiais Amazon (1–5) → comparar com dados desta skill
2. Cruzar com fontes secundárias (6–7)
3. Se divergência → fonte oficial Amazon prevalece
4. Se confirmada mudança → atualizar skill + notificar Pedro no tópico 📊 Marketplaces
5. **Atenção especial:** verificar status da promoção FBA+ (expira jul/2026)

---

## CHANGELOG

| Data | Alteração |
|---|---|
| 10/04/2026 | v1.0 — Criação da skill do zero. Tabela completa de comissões (35+ categorias). 4 modelos logísticos (FBA/DBA/FBA Onsite/FBM). Tarifas FBA completas (peso × preço). Promoção FBA+ vigente. Armazenagem e remoção. Amazon Ads (3 formatos + benchmarks). Buy Box (critérios e importância). Saúde da conta (AHR + métricas). Recebimento (ciclo 14 dias). Programas especiais (Vine, Programe e Poupe, Lightning Deals). Fórmula de precificação com exemplos. Comparativo Amazon vs ML vs Shopee. Mudanças 2026. |

---

## Notas relacionadas

- [[skills/marketplace/ml-fees-rules/SKILL|Taxas ML]]
- [[skills/marketplace/shopee-fees-rules/SKILL|Taxas Shopee]]
- [[skills/spreadsheet-pricing/SKILL|Planilha de Precificação]]

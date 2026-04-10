---
name: ml-fees-rules
description: Regras completas de comissões, taxas, frete e custos do Mercado Livre Brasil 2026 para vendedores CNPJ. Base para precificação e estratégia de anúncios. Consultar SEMPRE antes de qualquer cálculo de margem, recomendação de pricing, simulação de lucro ou análise de custo no ML. Também ativar quando o usuário mencionar "quanto custa vender no ML", "comissão mercado livre", "taxa mercado livre", "calcular margem ML", "precificação mercado livre", "custo frete ML", "custo full ML", "mercado envios full", "mercadolíder", "tabela de frete ML", "custo de envio ML", "reputação mercado livre", "mercado ads", "anúncio clássico", "anúncio premium", ou qualquer variação relacionada a custos e taxas do Mercado Livre Brasil.
triggers:
  - "quanto custa vender no ML"
  - "comissão mercado livre"
  - "taxa mercado livre"
  - "calcular margem ML"
  - "precificação mercado livre"
  - "custo frete ML"
  - "custo full ML"
  - "mercado envios full"
  - "mercadolíder"
  - "tabela frete ML"
  - "anúncio clássico ML"
  - "anúncio premium ML"
  - "mercado ads"
  - "reputação mercado livre"
metadata:
  openclaw:
    emoji: 💰
    last_updated: "2026-04-10"
    next_review: "2026-04-16"
    cron: "ML Fees Monitor — quarta 10h SP"
    sources:
      - url: "https://www.mercadolivre.com.br/ajuda/quanto-custa-vender-um-produto_1338"
        status: "✅ Oficial — custos gerais"
      - url: "https://www.mercadolivre.com.br/ajuda/custos-envio-reputacao-verde-mercado-lider_40538"
        status: "✅ Oficial — tabela frete verde/ML/sem reputação"
      - url: "https://www.mercadolivre.com.br/ajuda/custos-frete-gratis-sem-reputacao-ou-amarela_40545"
        status: "✅ Oficial — tabela frete amarela"
      - url: "https://www.mercadolivre.com.br/ajuda/tarifas-e-faturamento_1472"
        status: "✅ Oficial — tarifas"
      - url: "https://www.mercadolivre.com.br/ajuda/Custos-de-frete-gratis-pelo-Mercado-Envios_3362"
        status: "✅ Oficial — custos envio"
      - url: "https://gosmarter.com.br/taxas-mercado-livre/"
        status: "✅ Confiável — tabela completa + calculadora"
      - url: "https://gosmarter.com.br/mercado-envios-full-vale-a-pena-2026/"
        status: "✅ Confiável — Full"
      - url: "https://ecommercenapratica.com/blog/comissao-mercado-livre/"
        status: "✅ Confiável — comissões"
      - url: "https://www.koncili.com/blog/categorias-do-mercado-livre/"
        status: "✅ Confiável — categorias"
      - url: "https://conteudos.xpi.com.br/acoes/relatorios/mercado-livre-meli34-entenda-o-aumento-de-custos-para-os-sellers-anunciado-hoje/"
        status: "✅ XP Investimentos — análise de impacto"
---

# Regras de Comissões, Taxas e Custos — Mercado Livre 2026 (CNPJ)

> ⚠️ **Última atualização:** 10/04/2026
> **Mudança estrutural em 02/03/2026:** ML substituiu taxa fixa por tabela variável de 232 combinações (peso × preço), encerrou subsídio de frete grátis, reajustou Full, criou tabelas de frete por reputação.
> **Nenhuma mudança adicional entre março e abril de 2026.**
> **Cron de verificação:** Quarta-feira 10h SP (ML Fees Monitor)

---

## 1. TIPOS DE ANÚNCIO

### Resumo comparativo

| Critério | Grátis | Clássico | Premium |
|---|---|---|---|
| Comissão | 0% | 10–14% | 15–19% |
| Exposição | Baixa | Alta | Máxima |
| Duração | 60 dias | Ilimitada | Ilimitada |
| Parcelas s/juros | Não | Não | Até 12× (até 18× em valores altos) |
| Limite vendas | 5 novos / 20 usados por ano | Sem limite | Sem limite |
| Anúncios simultâneos | Máx. 10 (1 un. cada) | Sem limite | Sem limite |
| Uso ideal | Teste de demanda | Margem apertada | Escala / alto giro |

### Notas:
- **Grátis:** Indisponível para MercadoLíder ou Profissional do Mercado Pago. Apenas para teste.
- **Clássico:** Não oferece parcelamento sem juros. Defesa de rentabilidade.
- **Premium:** Prioridade no algoritmo + parcelamento. A diferença vs Clássico é sempre **5 pontos percentuais** em qualquer categoria.
- **Regra prática:** Premium custa ~R$ 2–3 a mais por venda na faixa R$ 25–50. Se parcelamento + exposição gerarem ≥1 venda extra a cada 10, compensa.

---

## 2. COMISSÃO POR CATEGORIA (tabela completa)

Comissões percentuais **não foram alteradas** na reestruturação de março/2026.

| Categoria | Clássico | Premium |
|---|---|---|
| **Alimentos e Bebidas** | 14% | 19% |
| **Bebês** | 14% | 19% |
| **Beleza e Cuidado Pessoal** | 14% | 19% |
| **Calçados, Roupas e Bolsas** | 14% | 19% |
| **Esportes e Fitness** | 14% | 19% |
| **Eletrônicos, Áudio e Vídeo** | 13% | 18% |
| **Games** | 13% | 18% |
| **Pet Shop** | 12,5% | 17,5% |
| **Joias e Relógios** | 12,5% | 17,5% |
| **Acessórios para Veículos** | 12% | 17% |
| **Livros, Revistas e Comics** | 12% | 17% |
| **Saúde** | 12% | 17% |
| **Indústria e Comércio** | 12% | 17% |
| **Casa, Móveis e Decoração** ⭐ | 11,5% | 16,5% |
| **Brinquedos e Hobbies** | 11,5% | 16,5% |
| **Agro** | 11,5% | 16,5% |
| **Arte, Papelaria e Armarinho** | 11,5% | 16,5% |
| **Construção** | 11,5% | 16,5% |
| **Instrumentos Musicais** | 11,5% | 16,5% |
| **Eletrodomésticos** | 11% | 16% |
| **Informática / Celulares / Notebooks** | 11% | 16% |
| **Câmeras e Acessórios** | 11% | 16% |

> **Nota:** Subcategorias podem variar pontualmente. Sempre confirmar no Seller Center.
> Fonte: Koncili, GoSmarter, Ecommerce na Prática — dados idênticos entre as três.

---

## 3. CUSTO OPERACIONAL / ENVIO (novo modelo março/2026)

### ⚠️ MUDANÇA CRÍTICA: "Taxa fixa" NÃO EXISTE MAIS

Desde 02/03/2026, a antiga taxa fixa (R$ 6,25 / R$ 6,50 / R$ 6,75) foi **abolida** e substituída por uma **tabela variável de 232 combinações** (29 faixas de peso × 8 faixas de preço). Esse custo já incorpora o frete grátis oferecido ao comprador — o ML não subsidia mais.

### 3.1 Como funciona o novo modelo

O custo depende de 3 variáveis: **preço do produto**, **peso** (real ou cubado, o que for maior) e **nível de reputação** do vendedor.

**Faixas de preço:** R$ 0–18,99 | R$ 19–48,99 | R$ 49–78,99 | R$ 79–99,99 | R$ 100–119,99 | R$ 120–149,99 | R$ 150–199,99 | R$ 200+

**Regras de frete por faixa:**
- **Abaixo de R$ 19:** custo máximo = 50% do preço. Frete grátis não se aplica automaticamente.
- **R$ 19 a R$ 78,99:** Frete grátis **padrão** (prazo normal) ao comprador. Vendedor paga tarifa menor.
- **R$ 79+:** Frete grátis **rápido** obrigatório. Vendedor paga tarifa maior.

### 3.2 Tabela de custos de envio — MercadoLíder / Reputação Verde / Sem Reputação

Fonte: Página oficial ML (`ajuda/40538`). Válido para Full, Coleta e Agências. **Desconto de até 70% já embutido.**

| Peso | R$0-18,99 | R$19-48,99 | R$49-78,99 | R$79-99,99 | R$100-119,99 | R$120-149,99 | R$150-199,99 | R$200+ |
|---|---|---|---|---|---|---|---|---|
| Até 0,3kg | R$5,65 | R$6,55 | R$7,75 | R$12,35 | R$14,35 | R$16,45 | R$18,45 | R$20,95 |
| 0,3-0,5kg | R$5,95 | R$6,65 | R$7,85 | R$13,25 | R$15,45 | R$17,65 | R$19,85 | R$22,55 |
| 0,5-1kg | R$6,05 | R$6,75 | R$7,95 | R$13,85 | R$16,15 | R$18,45 | R$20,75 | R$23,65 |
| 1-1,5kg | R$6,15 | R$6,85 | R$8,05 | R$14,15 | R$16,45 | R$18,85 | R$21,15 | R$24,65 |
| 1,5-2kg | R$6,25 | R$6,95 | R$8,15 | R$14,45 | R$16,85 | R$19,25 | R$21,65 | R$24,65 |
| 2-3kg | R$6,35 | R$7,95 | R$8,55 | R$15,75 | R$18,35 | R$21,05 | R$23,65 | R$26,25 |
| 3-4kg | R$6,45 | R$8,15 | R$8,95 | R$17,05 | R$19,85 | R$22,65 | R$25,55 | R$28,35 |
| 4-5kg | R$6,55 | R$8,35 | R$9,75 | R$18,45 | R$21,55 | R$24,65 | R$27,75 | R$30,75 |
| 5-6kg | R$6,65 | R$8,55 | R$9,95 | R$25,45 | R$28,55 | R$32,65 | R$35,75 | R$39,75 |

> **Tabela completa:** 29 faixas de peso (até 150kg+). Dados acima cobrem ~90% dos nossos produtos.
> Para tabela completa: https://www.mercadolivre.com.br/ajuda/40538

### 3.3 Impacto da reputação no custo de frete

Desde março/2026, existem **tabelas diferenciadas por reputação**:

| Reputação | Desconto embutido | Faixa de custo (total) | Tabela oficial |
|---|---|---|---|
| Verde / ML / Sem reputação | Até 70% | R$ 5,65 — R$ 261,95 | `ajuda/40538` |
| Amarela | ~60% | R$ 6,46 — R$ 314,34 | `ajuda/40545` |
| Laranja / Vermelha | 0% | **R$ 8,07 — R$ 523,90** | — |

**⚠️ Reputação ruim pode DOBRAR o custo de frete. Manter verde é questão de sobrevivência financeira.**

### 3.4 Frete grátis rápido opcional (produtos abaixo de R$ 79)

Vendedor pode **optar** por oferecer frete grátis rápido em produtos de R$ 0 a R$ 78,99 (custo maior):

| Peso | Custo (R$0-78,99) |
|---|---|
| Até 0,3kg | R$12,35 |
| 0,3-0,5kg | R$13,25 |
| 0,5-1kg | R$13,85 |
| 1-1,5kg | R$14,15 |
| 1,5-2kg | R$14,45 |
| 2-3kg | R$15,75 |

> Regra: Produtos abaixo de R$ 19 pagam no máximo 50% do preço.

### 3.5 Envios Flex — Exceção (mantém custo fixo)

O Envios Flex é a **única modalidade que mantém custo fixo** por unidade:

| Faixa de preço | Custo fixo Flex |
|---|---|
| Até R$ 18,99 | R$ 6,25 |
| R$ 19–48,99 | R$ 6,65 |
| R$ 49–78,99 | R$ 7,75 |

Livros via Flex: R$ 3,00 a R$ 4,50.

### 3.6 Referência histórica — tabela antiga (até fev/2026)

Para comparação com dados antigos:

| Faixa de preço (antigo) | Custo fixo antigo |
|---|---|
| Abaixo de R$ 12,50 | 50% do preço |
| R$ 12,50 a R$ 29,00 | R$ 6,25 |
| R$ 29,00 a R$ 50,00 | R$ 6,50 |
| R$ 50,00 a R$ 79,00 | R$ 6,75 |
| Acima de R$ 79,00 | Sem custo fixo |

---

## 4. MERCADO ENVIOS FULL (Fulfillment)

### 4.1 Armazenagem diária (por unidade) — reajustada em março/2026

| Tamanho | Critério | Custo/dia/un. |
|---|---|---|
| **Pequeno** | Até 12×15×25cm, ≤18kg | **R$ 0,007** |
| **Médio** | Até 28×36×51cm, ≤18kg | **R$ 0,015** |
| **Grande** | Até 60×60×70cm, ≤18kg | **R$ 0,050** |
| **Extragrande** | >60×60×70cm ou >18kg | **R$ 0,107** |

**Exemplo prático (nossos potes):**
- Kit 5 potes vidro = tamanho **Médio**
- 30 dias: R$ 0,015 × 30 = **R$ 0,45/un.**
- 80 dias: R$ 0,015 × 80 = **R$ 1,20/un.** (margem começa a doer)
- 120+ dias: custos adicionais a partir de **R$ 2/mês por unidade**

### 4.2 Full Super (categoria Supermercado)

| Tamanho | Custo/dia/un. |
|---|---|
| Pequeno | **R$ 0,000** (grátis!) |
| Médio | **R$ 0,000** (grátis!) |
| Grande | R$ 0,014 |
| Extragrande | R$ 0,025 |

Preço mínimo de R$ 8 por produto. Custo fixo entre R$ 1 e R$ 6 conforme faixa.

### 4.3 Reajustes aplicados em março/2026

| Componente | Reajuste |
|---|---|
| Armazenagem diária (médios/grandes) | **+7,6%** |
| Retirada de estoque | **+5%** (R$ 95/item) |
| Custos de coleta | **+5% a +10%** |
| Estoque >6 meses | **+6,4%** adicional |
| Estoque >120 dias | A partir de R$ 2/mês por unidade |

### 4.4 Cashback de frete (benefício ML/Loja Oficial)

Vendedores Full com selo **MercadoLíder ou Loja Oficial** que têm **>50% dos envios via Full** recebem **cashback de 40%** dos gastos com frete grátis no fim do mês. Benefício significativo — considerar no cálculo de margem.

### 4.5 Penalidades por não conformidade

| Situação | Custo |
|---|---|
| Divergência de inventário <100% | R$ 3/unidade |
| Divergência ≥100% | R$ 9/unidade excedente |
| Embalagem/etiquetagem fora do padrão | Cobranças por inconformidade |

### 4.6 Quando usar Full

✅ Alto giro + margem saudável + dimensões pequenas/médias + meta ML
❌ Baixo giro + pesado/volumoso + margem apertada + estoque >90 dias

---

## 5. MERCADO ADS (Publicidade)

### 5.1 Product Ads (formato principal)

- **Modelo:** CPC (Custo por Clique) via leilão de segundo preço
- **Como funciona:** CPC cobrado = Ad-rank do concorrente abaixo ÷ seu Ad-score + R$ 0,01. Anúncios mais relevantes pagam menos.
- **Requisitos:** conta ativa 7–15 dias, mínimo **20 vendas**, reputação **amarela ou superior**
- **Sem investimento mínimo obrigatório** — vendedor define orçamento diário (pausa quando esgota)
- **ACOS operacional típico:** 5% a 15% (vendedores otimizados)
- **Posicionamento:** resultados de busca + páginas de produtos concorrentes

### 5.2 Display Ads (branding)

- Formato para marcas maiores (vídeos na home, Audience Deals, Brand Lift)
- Modelo CPM (Custo por Mil Impressões)
- Não relevante para operação GB Importadora no momento

### 5.3 Central de Promoções

- Campanhas sazonais (Black Friday, Liquidação, 3.3, Dia das Mães)
- Descontos progressivos por quantidade, cupons, promoções relâmpago
- ML pode oferecer descontos nas tarifas de frete/comissão em troca de redução de preço
- Tudo gerido pelo Seller Center

### 5.4 Impacto no cálculo

Ads é custo **adicional** à comissão + custo de envio:
```
Custo total por venda = Comissão (%) × Preço
                      + Custo de envio (tabela peso × preço)
                      + Ads (CPC acumulado por venda)
                      + Armazenagem Full (se aplicável)
```

**Regra:** definir ACOS máximo por SKU. Se ACOS > margem disponível → prejuízo.

---

## 6. REPUTAÇÃO E MercadoLíder

### 6.1 Termômetro de reputação

Ativado após **10 vendas** nos últimos 365 dias. Avaliado nos últimos 60 dias (alto volume) ou 365 dias (<60 vendas).

**Limites para manter verde:**
- Reclamações: < 2–3%
- Cancelamentos: < 2–2,5%
- Envios atrasados: < 3–6%
- Meta operacional: **97% de entregas no prazo**

### 6.2 Requisitos MercadoLíder (últimos 60 dias)

| Nível | Vendas mínimas | Faturamento mínimo |
|---|---|---|
| **MercadoLíder (Prata)** | ≥ 230 | ≥ R$ 37.000 |
| **MercadoLíder Gold** | ≥ 575 | ≥ R$ 118.400 |
| **MercadoLíder Platinum** | ≥ 1.725 | ≥ R$ 296.000 |

Todos exigem: cadastro ≥4 meses, termômetro verde-escuro, <1% reclamações, <0,5% mediações ML, <6% atrasos.

### 6.3 Como reputação afeta custos e visibilidade

| Dimensão | Impacto |
|---|---|
| **Comissões (%)** | NÃO variam por reputação — apenas por categoria e tipo |
| **Custo de frete** | Tabelas diferenciadas: até 70% desconto (verde) vs 0% (laranja/vermelha) |
| **Visibilidade** | Verde-escuro/ML nas primeiras posições. Vermelho praticamente invisível |
| **Prazo recebimento** | 2 dias (boa reputação) vs até 28 dias (sem reputação) |
| **Benefício especial** | Full + ML + Premium em itens >R$ 250: comissão Clássico (11% vs 16%) |

---

## 7. RECEBIMENTO VIA MERCADO PAGO

### 7.1 Prazos de liberação

| Situação | Prazo |
|---|---|
| Com reputação + produtos novos | ~5 dias após entrega |
| Sem reputação ou produtos usados | ~9 dias |
| Sem confirmação do comprador | Até 28 dias |
| MercadoLíderes | 2–11 dias conforme nível |
| Comprador confirma recebimento | **Imediato** |

### 7.2 Saques e transferências

- **Pix/TED para conta bancária:** sem custo (NÃO é saque)
- **Pix Saque/Pix Troco:** 8 gratuitos/mês. A partir do 9º: R$ 5,90
- **Banco24Horas:** R$ 5,90/operação (não conta como saque gratuito)
- **Antecipação de recebíveis:** disponível sob demanda, taxa dinâmica que diminui com faturamento

---

## 8. FÓRMULA DE PRECIFICAÇÃO

### Custo total por venda (sem Ads)

```
Custo ML = Comissão (%) × Preço de venda
         + Custo de envio (lookup: peso × preço × reputação)
         + Armazenagem Full (se aplicável)
```

### Fórmula de preço mínimo

```
Preço mínimo = (CMV + Impostos + Margem desejada + Custo envio + Armazenagem)
             / (1 - Comissão%)
```

> ⚠️ O custo de envio agora depende do **peso e preço**, criando circularidade na fórmula (preço define faixa de frete, que define custo, que define preço mínimo). Na prática: calcular iterativamente ou usar o Simulador de Custos oficial.

### Checklist de verificação:
1. [ ] Peso e dimensões do produto estão corretos? (peso real vs cubado)
2. [ ] Usou a tabela de frete da reputação correta?
3. [ ] Comissão é da categoria E tipo de anúncio corretos?
4. [ ] Incluiu custo de armazenagem Full (se aplicável)?
5. [ ] Considerou cenário com e sem Ads (ACOS 5–15%)?
6. [ ] Produto está em kit? (custo de envio cobrado 1× por kit)
7. [ ] Verificou se tem cashback de 40% do frete (ML + Full >50%)?

---

## 9. EXEMPLOS DE CÁLCULO

### Exemplo 1: Kit 5 Potes Vidro — R$ 24,90 (Premium 16,5%, ~1kg, Full)

| Item | Valor |
|---|---|
| Preço de venda | R$ 24,90 |
| Comissão Premium (16,5%) | −R$ 4,11 |
| Custo de envio (0,5-1kg, faixa R$19-48,99) | −R$ 6,75 |
| Armazenagem Full (~25 dias, médio) | −R$ 0,38 |
| **Total custos ML** | **R$ 11,24** |
| **% retido pelo ML** | **45,1%** |
| **Sobra para CMV + imposto + lucro** | **R$ 13,66** |

### Exemplo 2: Mesmo produto a R$ 39,90 (Premium 16,5%, ~1kg, Full)

| Item | Valor |
|---|---|
| Preço de venda | R$ 39,90 |
| Comissão Premium (16,5%) | −R$ 6,58 |
| Custo de envio (0,5-1kg, faixa R$19-48,99) | −R$ 6,75 |
| Armazenagem Full (~20 dias, médio) | −R$ 0,30 |
| **Total custos ML** | **R$ 13,63** |
| **% retido pelo ML** | **34,2%** |
| **Sobra para CMV + imposto + lucro** | **R$ 26,27** |

### Exemplo 3: Kit 2 Potes 1520ml — R$ 55,90 (Premium 16,5%, ~2kg, Full)

| Item | Valor |
|---|---|
| Preço de venda | R$ 55,90 |
| Comissão Premium (16,5%) | −R$ 9,22 |
| Custo de envio (1,5-2kg, faixa R$49-78,99) | −R$ 8,15 |
| Armazenagem Full (~25 dias, médio) | −R$ 0,38 |
| **Total custos ML** | **R$ 17,75** |
| **% retido pelo ML** | **31,8%** |
| **Sobra para CMV + imposto + lucro** | **R$ 38,15** |

### Exemplo 4: Clássico vs Premium (R$ 39,90)

| | Clássico (11,5%) | Premium (16,5%) |
|---|---|---|
| Comissão | R$ 4,59 | R$ 6,58 |
| Custo envio | R$ 6,75 | R$ 6,75 |
| **Total custos ML** | **R$ 11,34** | **R$ 13,33** |
| **Diferença** | — | **+R$ 1,99/venda** |
| **Em troca de** | Sem parcelamento, exposição alta | Até 12× s/juros, exposição máxima |

---

## 10. MUDANÇAS OPERACIONAIS 2026

### 10.1 Monitoramento de preços em concorrentes
Desde outubro/2025 (reforçado em 2026), o ML monitora preços em plataformas concorrentes. Vendedor com preço menor em outra plataforma recebe notificação e tem **3 dias para ajustar**, sob pena de **perda de visibilidade**.

### 10.2 Mercado Shops → Minha Página
Mercado Shops descontinuado em 31/12/2025. Substituído por "Minha Página" a **R$ 99/mês**.

### 10.3 Loja Oficial simplificada
Regras simplificadas: apenas registro INPI ativo + Minha Página.

### 10.4 Funcionalidade UP (User Products)
Preço independente por variação de produto (expansão em 2026). Permite precificar cada variação (cor, tamanho) separadamente.

### 10.5 API — parâmetros novos
Desde 02/03/2026, o cálculo correto de `fixed_fee` via API exige os parâmetros: `logistic_type`, `shipping_mode` e `billable_weight`.

### 10.6 NCM e dados fiscais
Exigência reforçada de NCM e dados fiscais corretos em todos os anúncios.

---

## 11. PONTOS CRÍTICOS PARA PRECIFICAÇÃO

1. **Cadastro correto de peso e dimensões é CRÍTICO.** O novo modelo cobra por peso/tamanho — erro aqui = margem errada.

2. **Produtos abaixo de R$ 79 são os mais caros proporcionalmente.** A R$ 24,90 o ML retém ~45%. A R$ 79+ o custo fixo desaparece e o % cai.

3. **A tabela de frete tem 232 combinações.** Não dá pra precificar "de cabeça" — usar planilha, ferramenta ou Simulador de Custos oficial.

4. **Kits diluem o custo de envio.** Kit de 5 potes = 1 envio = 1 custo. 5 vendas avulsas = 5 custos.

5. **Full compensa se girar rápido.** Até 30 dias: custo irrelevante (R$ 0,45). Acima de 120 dias: começa a pesar forte.

6. **Reputação é custo direto.** Amarela paga ~20% mais frete. Laranja/vermelha paga **até o dobro**.

7. **Cashback de 40% no frete** para ML + Full >50% dos envios. Incluir no cálculo.

8. **Premium nem sempre compensa.** Para ticket baixo (<R$ 30), avaliar caso a caso.

9. **Monitoramento de preços:** ML penaliza se você vende mais barato em outra plataforma.

10. **Simulador oficial é a fonte de verdade:** https://www.mercadolivre.com.br/simulador-de-custos

---

## 12. COMPARATIVO ML vs SHOPEE (abril 2026)

Ambos reestruturaram custos em março/2026, encerrando a "guerra de frete grátis" de 2025.

| Aspecto | Mercado Livre | Shopee |
|---|---|---|
| Comissão (ticket baixo <R$79) | 11–19% + tarifa variável por peso | 20% + R$ 4,00 fixo |
| Comissão (ticket médio R$80–199) | 11–19% + frete variável | 14% + R$ 16–20 fixo |
| Comissão (ticket alto >R$200) | 11–19% + frete variável | 14% + R$ 26 fixo (sem teto) |
| Frete grátis | Obrigatório ≥R$ 79 (padrão ≥R$ 19) | Obrigatório para todos (subsidiado) |
| Subsídio de frete | Acabou (custo do vendedor) | Shopee subsidia até R$ 20–40 |
| Fulfillment | Maduro e consolidado (Full) | Em expansão (SFS) |
| Prazo recebimento | 2–5 dias (boa reputação) | 5–15 dias úteis |
| Ads | Robusto, dados analíticos completos | 5 formatos, Shopee Live |
| Visitas mensais | ~350 milhões | ~180–240 milhões |
| Perfil público | Classes B/C, compra planejada | Classes C/D, impulso |

**Regra prática:** ML é superior para ticket médio/alto, logística robusta e recebimento rápido. Shopee compete em ticket baixo com frete subsidiado. Para a GB Importadora, **operar nos dois** com precificação diferenciada é o ideal.

---

## 13. URLs DE MONITORAMENTO (Cron Semanal)

| # | Fonte | Status | Nota |
|---|---|---|---|
| 1 | [ML Oficial — Custos gerais](https://www.mercadolivre.com.br/ajuda/quanto-custa-vender-um-produto_1338) | ✅ Oficial | Base |
| 2 | [ML Oficial — Frete verde/ML](https://www.mercadolivre.com.br/ajuda/custos-envio-reputacao-verde-mercado-lider_40538) | ✅ Oficial | Tabela 232 combinações |
| 3 | [ML Oficial — Frete amarela](https://www.mercadolivre.com.br/ajuda/custos-frete-gratis-sem-reputacao-ou-amarela_40545) | ✅ Oficial | Tabela reputação amarela |
| 4 | [ML Oficial — Tarifas](https://www.mercadolivre.com.br/ajuda/tarifas-e-faturamento_1472) | ✅ Oficial | Tarifas gerais |
| 5 | [ML Oficial — Custos envio](https://www.mercadolivre.com.br/ajuda/Custos-de-frete-gratis-pelo-Mercado-Envios_3362) | ✅ Oficial | Envios |
| 6 | [GoSmarter — Taxas ML](https://gosmarter.com.br/taxas-mercado-livre/) | ✅ Confiável | Calculadora + tabela |
| 7 | [GoSmarter — Full](https://gosmarter.com.br/mercado-envios-full-vale-a-pena-2026/) | ✅ Confiável | Full detalhado |
| 8 | [Ecommerce na Prática](https://ecommercenapratica.com/blog/comissao-mercado-livre/) | ✅ Confiável | Comissões |
| 9 | [Koncili — Categorias](https://www.koncili.com/blog/categorias-do-mercado-livre/) | ✅ Confiável | Categorias |

### Protocolo de verificação:
1. Acessar fontes oficiais ML (1–5) → comparar com dados desta skill
2. Cruzar com fontes secundárias (6–9)
3. Se divergência → fonte oficial ML prevalece
4. Se confirmada mudança → atualizar skill + notificar Pedro no tópico 📊 Marketplaces

---

## CHANGELOG

| Data | Alteração |
|---|---|
| 10/04/2026 | v2.0 — Reformulação completa: taxa fixa abolida → tabela variável 232 combinações como seção principal. Tabelas de frete por reputação (verde/amarela/laranja). Tabela de categorias expandida (10→22). Parcelas Premium corrigido (12×, não 10×). Full: reajustes +7,6%, cashback 40%, penalidades detalhadas, estoque >120 dias. Ads: modelo leilão 2º preço, requisitos, ACOS 5–15%. Recebimento: prazos detalhados por nível, Pix/TED sem custo. Mudanças operacionais 2026 (monitoramento preços, Minha Página, Loja Oficial, UP, API). Requisitos MercadoLíder adicionados. Comparativo ML vs Shopee atualizado. Fontes oficiais ML adicionadas (ajuda/40538, 40545). |
| 18/03/2026 | v1.0 — Criação da skill |

---
title: "ml ranking"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Mercado Livre — Algoritmo, Fatores e Estratégias

## SUMÁRIO
1. [Como funciona o algoritmo](#como-funciona)
2. [Hierarquia de exibição](#hierarquia)
3. [Catálogo — o fator mais crítico](#catalogo)
4. [Os 12 fatores de ranking](#fatores)
5. [Penalizações](#penalizacoes)
6. [Títulos e exemplos para potes herméticos](#titulos)
7. [Checklist completo ML](#checklist)

---

## Como funciona o algoritmo {#como-funciona}

Objetivo do ML: **maximizar probabilidade de conversão**. Mostrar o produto com maior chance de ser comprado.

**Duas etapas:**
1. Filtragem por relevância (palavras-chave devem estar no anúncio)
2. Ranking por score (combinação de fatores de desempenho)

O algoritmo **não é** cronológico (quem anunciou primeiro), não é só preço baixo, e não é aleatório.

---

## Hierarquia de exibição {#hierarquia}

```
1º → Anúncios do Catálogo (sempre primeiros)
2º → Product Ads / Patrocinados (tag "Patrocinado")
3º → Anúncios orgânicos (ordenados pelo score)
```

**Implicação crítica:** Sem catálogo e sem ADS, você só aparece na 3ª posição hierárquica.

---

## Catálogo — o fator mais crítico {#catalogo}

### O que é:
Anúncios do catálogo aparecem ANTES de todos os orgânicos. Dentro do catálogo, vendedores competem pelo mesmo produto — quem vence fica como "destaque" (botão "Comprar agora"). Os outros ficam em "Outras opções de compra".

### Status no catálogo:
| Status | Significado | Ação |
|--------|-------------|------|
| **Ganhando** | Você é a primeira opção de compra | Manter condições, monitorar |
| **Compartilhando** | Condições semelhantes a concorrentes | Melhorar preço/frete para se destacar |
| **Perdendo (laranja)** | Outros têm melhores condições | Você aparece em "outras opções" |
| **Perdendo (cinza)** | Não é possível competir | Investigar bloqueio (reputação? preço?) |

### Critérios para ganhar destaque no catálogo:
1. Preço mais competitivo (produto + frete total)
2. Reputação **mínimo verde** (laranja/vermelho = bloqueado do catálogo)
3. Estoque disponível
4. Mercado Envios Full (vantagem significativa)
5. Velocidade de envio
6. Avaliações do produto

### Para GB/Budamix:
- Verificar se potes herméticos de vidro têm catálogo disponível
- Entrar ativamente e monitorar status (ganhando/compartilhando/perdendo)
- Full ML é o maior diferencial para ganhar destaque no catálogo

**O QUE FAZER:** Acessar Central de Anúncios → Catálogo → verificar quais SKUs têm catálogo disponível e qual é o status atual de cada um.

---

## Os 12 fatores de ranking {#fatores}

### 1. Vendas Recentes ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)
- Velocidade de vendas (por semana) é mais importante que volume histórico total
- Janelas analisadas: últimos 7, 30, 60 dias
- Queda de vendas → menos visibilidade → menos vendas (espiral negativa)
- Campanhas que geram picos de venda melhoram o ranking orgânico depois

**O QUE FAZER:** Usar promoções da Central de Promoções para gerar spikes. Nunca deixar anúncios principais sem estoque — interrompe o momentum.

### 2. Catálogo ⭐⭐⭐⭐⭐ (Peso: CRÍTICO)
Ver seção completa acima.

### 3. Reputação do Vendedor ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)

**Thresholds exatos para manter reputação verde:**
| Métrica | Limite para verde |
|---------|-------------------|
| Taxa de reclamações | **< 3%** das vendas (últimos 60 dias) |
| Taxa de cancelamento | **< 2,5%** das vendas |
| Atrasos no envio | **< 15%** dos envios atrasados |

**Impactos por cor:**
- Verde escuro → máxima visibilidade
- Verde → boa visibilidade
- Amarelo → visibilidade reduzida
- Laranja/Vermelho → severamente penalizado + **bloqueado do catálogo**

**O QUE FAZER:** Monitorar termômetro semanalmente. Se aproximando do limite: cancelar pedidos apenas quando absolutamente necessário, enviar no prazo, resolver reclamações antes de virar caso.

### 4. MercadoLíder ⭐⭐⭐⭐ (Peso: ALTO)

**Requisitos 2025:**
| Nível | Vendas (últimos 60 dias) | Faturamento |
|-------|--------------------------|-------------|
| MercadoLíder | ~30 vendas | R$ ~6.000 |
| MercadoLíder Gold | ~200 vendas | R$ ~55.000 |
| MercadoLíder Platinum | 1.725+ vendas | R$ 296.000+ |

**Benefícios de ranking:** Maior visibilidade, mais recursos de catálogo, tarifas diferenciadas, destaque visual.

**Para GB:** Com faturamento histórico de pico de R$1M/mês, Platinum é o target natural. Manter métricas para não perder o status.

### 5. Mercado Envios Full ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)
- ML controla estoque e entrega → "confia mais" no anúncio → prioridade algorítmica
- Prazo de entrega mais curto → mais competitivo no catálogo
- Menos cancelamentos → melhor reputação
- Frete grátis mais acessível (descontos de até 50% em alguns envios)
- Elegibilidade para "Entrega Garantida" e "Entrega no mesmo dia"

**Restrições:** limite de dimensão/peso; regras para produtos com validade; não disponível para todos os produtos.

**O QUE FAZER:** Verificar se potes herméticos de vidro são elegíveis (atenção ao peso — vidro é pesado). Calcular custo de armazenagem vs. benefício de posicionamento. Ativar nos top 3 SKUs primeiro.

### 6. Qualidade do Anúncio ⭐⭐⭐⭐ (Peso: ALTO)

**Título:**
- Máximo 60 chars visíveis (ML corta o resto)
- Palavra-chave principal no início
- Sem maiúsculas excessivas, repetições, preço, símbolos
- Fórmula: `[Produto] [Marca] [Variação] [Atributo principal]`

**Fotos:**
- Mínimo 1, recomendado 6-7
- Principal: fundo branco, produto centralizado, sem marca d'água
- Adicionais: detalhes, lifestyle, dimensões, uso, kit completo
- Resolução mínima: 500x500px | Recomendado: 1200x1200px

**Ficha técnica:**
- Preencher 100% dos campos (material, dimensões, capacidade, cor, marca, modelo)
- Algoritmo favorece completude
- Campos vazios = menos visibilidade em filtros específicos

**O QUE FAZER:** Auditar cada anúncio de pote hermético. Para cada um: título segue a fórmula? Ficha técnica 100%? 6+ fotos?

### 7. Preço Competitivo ⭐⭐⭐⭐ (Peso: ALTO)
- ML compara preços de produtos similares na mesma busca
- Preço muito alto = menos conversão = queda no ranking
- Para catálogo: preço é critério central para ganhar destaque
- ML oferece ajuste automático de preço (defina min/max)

**Para kits e combos:** Verificar concorrentes de kit vs. produto unitário. Kits têm menos concorrência e permitem melhor margem percebida.

### 8. Frete Grátis ⭐⭐⭐⭐ (Peso: ALTO)
- Tag de frete grátis = destaque visual + preferência do algoritmo
- Filtro "Frete grátis" muito usado — sem ele, some do tráfego filtrado
- Kits acima de R$79 ativam frete grátis padrão do ML automaticamente

**Modalidades de envio:**
- Full: frete grátis automático acima do threshold
- Coleta: ML busca no depósito do seller
- ME2 (agência): seller leva em agência parceira
- Flex: entrega própria (mesma cidade)

### 9. Taxa de Conversão ⭐⭐⭐⭐ (Peso: ALTO)
- Razão visitas/compras — anúncio que converte bem = algoritmo aprende que é desejável
- Para potes herméticos, as dúvidas críticas são: capacidade (ml/L), material exato, compatibilidade com micro-ondas/freezer, vedação, unitário ou conjunto
- Responder essas dúvidas NA DESCRIÇÃO reduz abandono antes da pergunta

**O QUE FAZER:** Verificar as perguntas mais feitas nos anúncios de potes. Incluir respostas antecipadas na descrição.

### 10. Mercado Ads / Product Ads ⭐⭐⭐⭐ (Peso: MODERADO-ALTO)
- Sistema de leilão com ROAS Objetivo (ML migrou de ACOS para ROAS em 2024)
- Efeito Halo: ADS → mais vendas → melhora ranking orgânico
- TACOS = gasto ADS / faturamento total (orgânico + pago) — métrica mais honesta

**Estratégia:**
1. Começar com campanha automática para identificar keywords com conversão
2. Migrar keywords boas para campanha manual
3. Usar ADS em anúncios que já convertem — não para salvar anúncios ruins
4. ROAS objetivo mínimo: 5x (R$1 gasto → R$5 de retorno)
5. Cauda longa: 30% menos concorrência, até 2x mais conversão

**Exemplo de cauda longa para GB:**
- Curta (alta concorrência): `pote hermético`
- Longa (menor concorrência): `pote hermético vidro 700ml tampa bambu`

### 11. Histórico e Longevidade ⭐⭐⭐ (Peso: MODERADO)
- Anúncios antigos com bom histórico têm vantagem acumulada
- Pausar e reativar pode causar reset parcial ou total do histórico
- Mudar título de anúncio com histórico forte é um risco

**O QUE FAZER:** Nunca pausar anúncios de bom desempenho. Ajustes sempre com anúncio ativo.

### 12. Variações e Kits ⭐⭐⭐ (Peso: MODERADO)
- Variações concentram todo o histórico de vendas em um anúncio → mais força de ranking
- Ex: Kit 3 potes (500ml, 700ml, 1L) em variação = histórico unificado
- Kits têm menos concorrência que produtos unitários
- Kits ultrapassam R$79 mais facilmente (threshold de frete grátis)
- Kits com composição única = sem concorrência direta

---

## Penalizações {#penalizacoes}

| Ação | Impacto |
|------|---------|
| Cancelamento pelo vendedor > 2,5% | Reputação cai |
| Atrasos no envio > 15% | Reputação cai |
| Reclamações > 3% | Reputação cai |
| Estoque zerado com anúncio ativo | Pausa automática + prejudica histórico |
| Pausar e reativar anúncio | Possível reset parcial do histórico |
| Mudança brusca de preço (muito alto) | Perde competitividade no catálogo |
| Fotos sem qualidade | Menos visibilidade nas primeiras posições |
| Ficha técnica incompleta | Invisível em filtros específicos |
| Perguntas sem resposta | Reduz conversão → queda no ranking |
| Categoria errada | Invisível para buscas corretas |

---

## Títulos e exemplos para potes herméticos {#titulos}

**Fórmula:**
```
Pote Hermético Vidro [capacidade] [atributo] Budamix [conjunto/kit]
```

**Exemplos testados:**
```
Pote Hermético Vidro 700ml Tampa Bambu Budamix Conjunto 3 Peças
Pote Hermético Vidro 1L Mantimento Budamix Kit 6 Unidades
Conjunto Potes Herméticos Vidro Budamix 500ml 700ml 1L Tampa Bambu
Kit Potes Herméticos Vidro Organização Despensa Budamix 3 Tamanhos
```

**Keywords essenciais ML:**
- `pote hermético vidro` (principal)
- `pote vidro tampa bambu`
- `conjunto potes herméticos`
- `kit potes mantimentos`
- `pote vidro organização`
- `recipiente hermético vidro`
- `vasilha vidro hermética`
- `pote vidro com tampa`

---

## Checklist completo ML {#checklist}

- [ ] Verificar status no catálogo (ganhando/compartilhando/perdendo)
- [ ] Preencher 100% da ficha técnica em todos os anúncios
- [ ] 6+ fotos de qualidade (fundo branco + detalhes + lifestyle + infográfico)
- [ ] Título com keyword principal no início (máx 60 chars)
- [ ] Preço competitivo vs. top 5 da categoria
- [ ] Ativar Full ML nos top 3 SKUs
- [ ] Reputação verde: < 3% reclamações, < 2,5% cancelamentos, < 15% atrasos
- [ ] Responder perguntas em < 1 hora
- [ ] Participar da Central de Promoções (Ofertas do dia, Relâmpago)
- [ ] Ativar Product Ads com campanha automática inicial
- [ ] ROAS objetivo ≥ 5x
- [ ] Criar variações para concentrar histórico (tamanhos, quantidades)
- [ ] Criar kits para subir ticket médio e fugir da concorrência direta
- [ ] Nunca pausar anúncios de bom desempenho
- [ ] Monitorar MercadoLíder — manter status ou avançar de nível

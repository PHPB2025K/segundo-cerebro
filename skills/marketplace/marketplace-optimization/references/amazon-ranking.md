---
title: "amazon ranking"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Amazon Brasil — Algoritmo A10, Buy Box e Estratégias

## SUMÁRIO
1. [Algoritmo A10 vs. A9 — o que mudou](`#a10`)
2. [Buy Box — conceito crítico](#buybox)
3. [Os 8 fatores de ranking](#fatores)
4. [Penalizações e riscos](#penalizacoes)
5. [Estrutura de listing otimizado](#listing)
6. [Checklist completo Amazon](#checklist)

---

## Algoritmo A10 vs. A9 — o que mudou {#a10}

### A9 (modelo anterior):
- Foco em velocidade de vendas
- PPC tinha impacto direto no ranking orgânico
- Palavras-chave no título e bullets
- CTR e conversão importavam

### A10 (modelo atual) — diferenças críticas:
| Mudança | Impacto prático |
|---------|-----------------|
| **Tráfego externo importa** | Google, Instagram, TikTok com link Amazon = boost no ranking |
| **Vendas orgânicas > PPC para ranking** | PPC gera vendas mas impacta menos o orgânico que antes |
| **Autoridade do seller ganhou peso** | Histórico, feedback e métricas têm mais influência |
| **Engajamento com o listing** | Tempo na página, interações, FAQ respondidas |
| **Conteúdo de qualidade** | A+ Content, vídeos, imagens ricas têm mais peso |

### Dados do Estudo Lett/Neogrid (out/2024 a mar/2025):
- **86% das vendas** estão concentradas nos **10 primeiros resultados**
- Posição média nos últimos 5 dias é uma das variáveis mais determinantes
- Estabilidade de posição → permanência no ranking
- Rating ideal: **4.9 estrelas** (não 5.0 — "imperfeição" aumenta autenticidade)
- Avaliações entre 1 e 3.2 estrelas: queda de performance
- Avaliações > 4.7 estrelas: ganhos de ranking
- Preço muito baixo ou muito alto prejudica — faixa moderada e competitiva é ideal

---

## Buy Box — conceito crítico {#buybox}

### O que é:
Botão "Adicionar ao carrinho" / "Comprar agora" em destaque na página do produto. Apenas **um vendedor** ocupa a Buy Box por vez. A maioria esmagadora das vendas acontece pela Buy Box.

### Para GB/Budamix (marca própria):
Por ser **marca exclusiva e única vendedora**, a Buy Box deve ser automática **se** atender critérios de elegibilidade.

**Condição para elegibilidade automática:**
- Conta Prime Seller ou FBA ativo
- Estoque disponível
- Métricas de seller em dia (ODR < 1%, cancelamentos < 2,5%, LSR < 4%)

### Critérios de Buy Box (relevante quando há múltiplos sellers):
1. Preço competitivo total (produto + frete)
2. Método de envio: FBA ou SFP têm vantagem enorme sobre FBM
3. Disponibilidade de estoque (sem estoque = fora da Buy Box)
4. Métricas do seller: ODR, cancelamentos, pontualidade
5. Avaliação do seller
6. Tempo de envio (mais rápido = melhor)

**Alerta de paridade de preço:** Amazon verifica se o produto está sendo vendido mais barato em outros canais (ML, Shopee). Preço mais baixo em outro canal → Amazon pode suprimir a Buy Box.

---

## Os 8 fatores de ranking {#fatores}

### 1. Relevância de Keywords ⭐⭐⭐⭐⭐ (Peso: CRÍTICO)

**Hierarquia de indexação:**
| Local | Peso | Limite |
|-------|------|--------|
| Título — primeiros 80 chars | Máximo | 200 chars total (recomendar até 150) |
| Bullet Points | Alto | 5 bullets × 500 chars |
| Descrição | Médio | Sem limite prático |
| Backend Keywords | Médio | **249 bytes** (sem repetir título/bullets) |
| A+ Content | Baixo/indireto | Melhora conversão mais que ranking |

**Fórmula de título Amazon:**
```
Marca + Produto + Característica Principal + Material + Tamanho/Capacidade + Cor + Quantidade
```

**Exemplo para GB:**
```
Budamix Pote Hermético de Vidro com Tampa de Bambu 700ml | Conjunto 3 Potes para Mantimentos e Organização da Cozinha
```

**Backend keywords — o que incluir:**
- Variações de grafia: `pote hermético`, `pote hermetico` (sem acento)
- Sinônimos: `frasco vidro`, `recipiente vidro`, `vasilha vidro`
- Uso: `organizar despensa`, `guardar café`, `conservar alimentos`
- Inglês que brasileiro digita: `glass jar`, `hermetic container`
- Não repetir palavras já no título — desperdício de bytes

**Estrutura de bullets otimizados:**
```
Bullet 1: PRINCIPAL BENEFÍCIO
"VIDRO DE QUALIDADE: Material 100% vidro borossilicato, livre de BPA, seguro para alimentos..."

Bullet 2: FUNCIONALIDADE
"VEDAÇÃO HERMÉTICA: Tampa com borracha de silicone garante hermeticidade total, preservando sabor e aroma..."

Bullet 3: VERSATILIDADE
"MÚLTIPLOS USOS: Ideal para grãos, café, chá, especiarias, açúcar, farinha — organiza sua despensa..."

Bullet 4: KIT COMPLETO
"KIT COM 3 POTES: Conjunto com capacidades 500ml, 700ml e 1L para diferentes necessidades..."

Bullet 5: GARANTIA/MARCA
"MARCA BUDAMIX: Garantia de 12 meses, suporte ao cliente dedicado — qualidade comprovada..."
```

**O QUE FAZER:** Auditar título de cada produto. Primeiros 80 chars contêm as keywords mais importantes? Backend keywords usa todos os 249 bytes disponíveis?

### 2. Sales Velocity / BSR ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)
- BSR (Best Seller Rank) = ranking dentro da categoria
- Menor número = melhor posição (BSR #1 = melhor vendedor da categoria)
- Calculado em tempo real, com peso maior para vendas recentes
- Subir no BSR → mais visibilidade → mais vendas (efeito bola de neve)

**Ciclo virtuoso:**
```
PPC → mais vendas → BSR sobe → ranking orgânico melhora → mais vendas orgânicas → BSR continua subindo
```

**Monitoramento:** BSR é público, atualizado hourly. Monitorar diariamente nos top SKUs.

### 3. Avaliações ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)

**Métricas:**
- Quantidade: volume de reviews importa tanto quanto nota
- Qualidade: reviews com fotos/vídeos têm mais peso
- Nota ideal: **4.9 estrelas** (estudo Neogrid/Lett)
- Threshold crítico: < 4.7 → perde ranking

**Como conseguir reviews na Amazon:**
- **Amazon Vine Program**: Amazon envia amostras para Vine Voices; requer convite; ideal para lançamentos
- **Follow-up via Seller Central**: Solicitação de feedback limitada — policy proíbe pedir review diretamente
- **Produto de qualidade**: Review orgânico natural é o mais sustentável

**O QUE FAZER:** Para novos SKUs, solicitar acesso ao Vine Program. Para SKUs existentes, monitorar média e responder reviews negativos com solução visível.

### 4. FBA — Fulfillment by Amazon ⭐⭐⭐⭐⭐ (Peso: MUITO ALTO)
- FBA = produto elegível ao Amazon Prime
- Prime = frete grátis em 1-2 dias = conversão muito maior
- Vantagem na Buy Box sobre FBM (Fulfilled by Merchant)
- Amazon "confia" mais em produtos FBA (ela controla a logística)

**Custos FBA Brasil 2026 (aproximado):**
- Taxa de armazenagem: por m³/mês (varia por categoria e temporada)
- Taxa de fulfillment: por unidade enviada (varia por peso/dimensão)
- Taxa de referência (comissão): 11-15% do preço de venda (varia por categoria)

**Para potes herméticos de vidro:**
- Atenção ao peso — vidro é pesado → custo FBA pode ser significativo
- Calcular viabilidade por SKU: kits maiores diluem custo fixo de FBA
- Verificar categoria "Cozinha e Jantar" para restrições de embalagem de vidro
- Possível exigência de embalagem adicional (bubble wrap, caixa reforçada)

**O QUE FAZER:** Calcular break-even de FBA por SKU antes de ativar. Comparar: custo FBA vs. custo de perder Prime badge. Para potes de maior capacidade (1L, kit 3 potes), prioridade para FBA.

### 5. A+ Content ⭐⭐⭐ (Peso: MODERADO — impacto em conversão)
- Conteúdo enriquecido abaixo da descrição: imagens, tabelas, textos formatados
- Requer **Brand Registry** da Amazon (usa registro no INPI)
- Impacto direto: melhora conversão (+5-15% típico)
- Impacto indireto: mais conversão → mais vendas → melhor ranking

**GB/Budamix tem direito ao Brand Registry:** Com marca registrada no INPI, basta ativar o Brand Registry na Amazon. Isso dá acesso a:
- A+ Content
- Sponsored Brands (banners com logo)
- Brand Store (página da marca)
- Proteção contra counterfeit

**A+ Content ideal para potes herméticos:**
- Comparativo visual de capacidades (500ml vs. 700ml vs. 1L)
- Benefícios do vidro vs. plástico (segurança, durabilidade, estética)
- Cuidados de conservação e limpeza
- Visual da coleção Budamix
- Tabela de usos por tamanho (café → 500ml, farinha → 1L, etc.)

**O QUE FAZER:** Verificar se Brand Registry está ativo. Criar A+ Content para os top 3 SKUs primeiro.

### 6. CTR (Click-Through Rate) ⭐⭐⭐⭐ (Peso: ALTO)
- Taxa de cliques no resultado de busca
- Produto que aparece mas ninguém clica = sinal negativo para o algoritmo
- Impacta CTR: foto principal, preço, estrelas, badge Prime, título

**Para melhorar CTR:**
- Foto principal: produto visivelmente atrativo, fundo branco, ocupando 85%+ do frame
- Preço: competitivo (não precisa ser o menor, mas deve estar na faixa)
- Prime badge: FBA = Prime automático = mais cliques imediatos
- Amazon Choice / Best Seller badge: concedidos automaticamente por performance

### 7. Tráfego Externo ⭐⭐⭐⭐ (Peso: ALTO — diferencial único do A10)
- Único dos 3 marketplaces que recompensa explicitamente tráfego externo
- Google indexa listings Amazon → produto bem posicionado no Google = tráfego extra gratuito
- Instagram/TikTok com link → sinal positivo para o algoritmo A10

**Estratégias para GB:**
- Instagram/TikTok: vídeos de organização de despensa com potes Budamix + link Amazon na bio
- Blog/artigos: "melhores potes para organização" + link direto para Amazon
- Parcerias com criadores de conteúdo de organização de casa (home organizer)
- Pinterest: pins de organização de despensa com link Amazon

**O QUE FAZER:** Estratégia de médio prazo (2-3 meses). Criar conta Instagram @budamix focada em organização de casa. Primeiros posts: antes/depois de organização de despensa.

### 8. Amazon PPC — Sponsored Products ⭐⭐⭐⭐ (Peso: MODERADO-ALTO)
- No A10: PPC ainda gera vendas, mas impacto no orgânico é menor que no A9
- Fundamental para novos produtos (zero histórico = zero ranking orgânico)

**Flywheel Effect:**
```
PPC → Vendas → Reviews → Ranking Orgânico sobe → Mais vendas orgânicas → Menos dependência de PPC
```

**Tipos de campanha:**
| Tipo | Quando usar |
|------|-------------|
| Sponsored Products | Produto individual nos resultados — base para qualquer estratégia |
| Sponsored Brands | Banner com logo + múltiplos produtos — requer Brand Registry |
| Sponsored Display | Retargeting em outras páginas e sites — avançado |

**Estratégia de PPC para novos SKUs:**
1. Auto campaign por 2-4 semanas (descoberta de keywords)
2. Identificar top keywords com conversão
3. Criar manual campaign com keywords identificadas
4. Pausar keywords com alto ACOS e baixa conversão
5. Reduzir dependência de PPC à medida que orgânico sobe

---

## Penalizações e riscos {#penalizacoes}

| Problema | Consequência |
|----------|--------------|
| **Stockout** | Perda de Buy Box + queda no BSR + semanas/meses para recuperar |
| ODR alto (Order Defect Rate > 1%) | **Suspensão de conta** |
| Late Shipment Rate > 4% | Advertência + potencial suspensão |
| Cancelamentos > 2,5% | Afeta elegibilidade para Buy Box |
| Reviews negativos (< 3.5 média) | Queda abrupta no ranking |
| Keyword stuffing no título/bullets | Amazon remove ou penaliza listing |
| Imagem principal não no fundo branco | Amazon pode suprimir o listing |
| Violação de políticas | Remoção do listing ou suspensão |
| Preço muito diferente de outros canais | Supressão da Buy Box |

**Stockout é o maior risco na Amazon:**
Uma semana sem estoque pode levar meses para recuperar o ranking. FBA ajuda — Amazon alerta antes de zerar e gestiona reposição.

**O QUE FAZER:** Manter buffer de estoque mínimo de 45 dias. Para FBA, monitorar nível de inventário no Seller Central e repor antes de atingir nível crítico.

---

## Estrutura de listing otimizado {#listing}

### Exemplo completo para potes herméticos:

**Título:**
```
Budamix Pote Hermético de Vidro com Tampa de Bambu 700ml | Conjunto 3 Potes para Mantimentos e Organização da Cozinha
```
(120 chars — dentro do limite visual de 150 recomendado)

**5 Bullets:**
```
✓ VIDRO DE QUALIDADE SUPERIOR: Vidro borossilicato livre de BPA, seguro para alimentos e fácil de limpar

✓ VEDAÇÃO HERMÉTICA TOTAL: Tampa de bambu com anel de silicone garante hermeticidade — preserva frescor por mais tempo

✓ MÚLTIPLOS USOS NA COZINHA: Perfeito para café, chá, açúcar, farinha, grãos, especiarias e qualquer mantimento seco

✓ KIT COM 3 POTES 700ml: Conjunto completo para organizar sua despensa — quantidade ideal para uma cozinha organizada

✓ MARCA BUDAMIX COM GARANTIA: 12 meses de garantia, suporte dedicado ao cliente — produto testado e aprovado por milhares de lares
```

**Backend keywords (249 bytes):**
```
pote hermetico vidro vasilha vidro frasco vidro recipiente vidro glass jar hermetic container organizar despensa guardar cafe conservar alimentos organizacao cozinha pote tampa bambu mantimentos secos
```

---

## Checklist completo Amazon {#checklist}

- [ ] Brand Registry Amazon ativo (usa INPI BR — Budamix)
- [ ] Título: Marca + Produto + Característica + Capacidade + Quantidade (até 150 chars visíveis)
- [ ] 5 bullet points com keywords em maiúsculo no início de cada um
- [ ] Backend keywords: 249 bytes, sem repetir título/bullets
- [ ] A+ Content criado (comparativo capacidades, benefícios vidro, lifestyle)
- [ ] 7-9 imagens: principal fundo branco + detalhes + lifestyle + infográfico + kit
- [ ] Vídeo do produto (demonstração de uso e vedação, 30-60s)
- [ ] FBA ativo (calcular viabilidade de custo por SKU para vidro pesado)
- [ ] Preço competitivo — verificar paridade com ML e Shopee
- [ ] PPC Sponsored Products ativo (auto campaign inicialmente)
- [ ] Monitorar BSR diariamente nos top SKUs
- [ ] Parent-child listing para variações de tamanho/quantidade
- [ ] Estoque buffer mínimo de 45 dias (stockout = pior penalização)
- [ ] Solicitar Amazon Vine para SKUs novos
- [ ] ODR monitorado — manter abaixo de 1% (risco de suspensão acima disso)
- [ ] Estratégia de tráfego externo: Instagram/TikTok com link Amazon

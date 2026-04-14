---
title: "marketplace algorithms"
created: 2026-04-14
type: agent
agent: trader
status: active
tags:
  - agent/trader
---

# Algoritmos de Ranking — Mercado Livre, Shopee e Amazon BR
**Pesquisa para GB Importadora (Budamix) | Março 2026**
> Documento de conhecimento core para otimização de potes herméticos de vidro e utilidades domésticas nas 3 plataformas.

---

## SUMÁRIO
1. [Mercado Livre — Algoritmo e Ranking](#1-mercado-livre)
2. [Shopee — Algoritmo e Ranking](#2-shopee)
3. [Amazon Brasil — Algoritmo A10](#3-amazon-brasil)
4. [Análise Cruzada e Matriz Comparativa](#4-análise-cruzada)
5. [Recomendações para a GB Importadora](#5-gb-importadora-recomendações)

---

# 1. MERCADO LIVRE

## 1.1 Como funciona o Algoritmo

O algoritmo do Mercado Livre é um sistema automatizado que determina qual produto aparece primeiro nos resultados de busca. A lógica central: **maximizar a probabilidade de conversão** para o comprador, ou seja, o ML quer mostrar o produto que tem maior chance de ser comprado.

O sistema opera em dois momentos:
1. **Filtragem por relevância**: Só aparecem anúncios com as palavras-chave buscadas pelo comprador
2. **Ranking por score**: Dentre os relevantes, ordena por uma combinação de fatores de desempenho

### Hierarquia de exibição nos resultados:
1. **Anúncios do Catálogo** — sempre aparecem primeiro
2. **Product Ads (patrocinados)** — aparecem nas primeiras posições com tag "Patrocinado"
3. **Anúncios orgânicos** — ordenados pelo algoritmo

### O que o algoritmo NÃO é:
- Não é aleatório
- Não é cronológico (quem anunciou primeiro não aparece primeiro)
- Não é só sobre preço baixo

---

## 1.2 Fatores de Ranking — Análise Profunda

### 🏆 FATOR 1: Vendas Recentes (Peso: MUITO ALTO)
**Como funciona:**
- O volume de vendas recentes é o fator mais poderoso no ML
- O algoritmo prioriza **velocidade** (quantas vendas por dia/semana) mais do que histórico total
- Anúncios com muitas vendas recentes têm "momentum" — continuam sendo exibidos mais
- O ML analisa janelas de tempo recentes (últimos 7, 30, 60 dias)

**Implicações práticas:**
- Um anúncio novo pode superar um antigo se gerar mais vendas por unidade de tempo
- Queda de vendas → queda no ranking → menos visibilidade → menos vendas (espiral negativa)
- Promoções e campanhas que geram pico de vendas ajudam o ranking orgânico depois

**Para potes herméticos:** Criar campanhas de oferta que gerem spikes de venda melhora ranking subsequente.

---

### 🏆 FATOR 2: Catálogo — Posição Privilegiada (Peso: CRÍTICO)
**Como funciona:**
- Anúncios no Catálogo do ML **sempre aparecem primeiro** nos resultados de busca
- No catálogo, vários vendedores competem pelo mesmo produto — quem vence aparece como "destaque"
- O vendedor em destaque é a primeira opção de compra (botão "Comprar agora")
- Outros vendedores ficam em "Outras opções de compra"

**Critérios para ganhar destaque no Catálogo:**
- Preço mais competitivo (produto + frete)
- Reputação verde (mínimo — laranja/vermelho não pode ganhar)
- Disponibilidade de estoque
- Uso do Mercado Envios Full (vantagem significativa)
- Velocidade de envio
- Avaliações do produto

**Status de concorrência no catálogo:**
- **Ganhando**: Você é a primeira opção de compra — maximize condições para aparecer mais
- **Compartilhando**: Condições semelhantes a concorrentes — melhore para se destacar
- **Perdendo (laranja)**: Outros oferecem condições melhores — você aparece em "outras opções"
- **Perdendo (cinza)**: Não é possível competir no momento — verifique o que pode melhorar

**Para GB:** Verificar se potes herméticos de vidro têm catálogo disponível e entrar ativamente.

---

### 🏆 FATOR 3: Reputação do Vendedor (Peso: MUITO ALTO)
**Como funciona:**
- Representada pelo termômetro de cores: verde escuro > verde > amarelo > laranja > vermelho
- Afeta diretamente o posicionamento — vendedores com reputação ruim têm "exposição reduzida"
- Vendedores laranjas/vermelhos NÃO PODEM ganhar o catálogo

**Métricas que compõem a reputação (com thresholds exatos):**
| Métrica | Limite para verde |
|---------|-------------------|
| Taxa de reclamações | < 3% das vendas (últimos 60 dias) |
| Taxa de cancelamento | < 2,5% das vendas |
| Atrasos no envio | < 15% dos envios atrasados |

**Impacto no ranking:**
- Verde escuro = máxima visibilidade
- Verde = boa visibilidade
- Amarelo = visibilidade reduzida
- Laranja/Vermelho = severamente penalizado

**Nota:** A reputação só é calculada quando há vendas suficientes. Novos vendedores sem histórico ficam em estado neutro.

---

### 🏆 FATOR 4: MercadoLíder — Boost de Status (Peso: ALTO)
**Como funciona:**
- Programa de reconhecimento para vendedores de alto desempenho
- Cria um círculo virtuoso: status → mais visibilidade → mais vendas → mais status

**Requisitos 2025:**
| Nível | Vendas (últimos 60 dias) | Faturamento |
|-------|--------------------------|-------------|
| MercadoLíder | ~30 vendas | R$ ~6.000 |
| MercadoLíder Gold | ~200 vendas | R$ ~55.000 |
| MercadoLíder Platinum | 1.725+ vendas | R$ 296.000+ |

**Benefícios que impactam ranking:**
- Maior visibilidade nos resultados
- Elegibilidade para mais recursos de catálogo
- Acesso a tarifas diferenciadas
- Destaque visual nos resultados

---

### 🏆 FATOR 5: Mercado Envios Full (Peso: MUITO ALTO)
**Como funciona:**
- Full = Fulfillment do ML: o seller manda estoque para centro de distribuição ML
- ML cuida de tudo: armazenagem, separação, embalagem, envio
- Anúncios Full têm vantagem algorítmica confirmada pela plataforma

**Benefícios diretos no ranking:**
- O ML "confia mais" em anúncios Full (controla estoque e entrega)
- Prazo de entrega mais curto = mais competitivo no catálogo
- Menos cancelamentos = melhor reputação
- Frete grátis mais acessível para o vendedor (descontos de até 50% em alguns envios)
- Elegibilidade para "Entrega Garantida" e "Entrega no mesmo dia" em regiões específicas

**Para GB:** Full é provavelmente a alavanca de maior impacto isolado para potes herméticos. Verificar se categoria e peso dos potes são elegíveis.

**Restrições do Full:**
- Limite de dimensão e peso por produto
- Regras especiais para produtos com validade
- Não disponível para todos os produtos

---

### 🏆 FATOR 6: Qualidade do Anúncio (Peso: ALTO)
**Inclui:**
- **Título**: Principal gatilho para o algoritmo encontrar o anúncio nas buscas
- **Fotos**: Qualidade, quantidade, aderência às guidelines
- **Ficha técnica**: Preenchimento de todos os campos obrigatórios e atributos
- **Descrição**: Completa e informativa
- **Categorização correta**: Anunciar na categoria errada penaliza visibilidade

**Estrutura de título recomendada pelo ML:**
```
[Nome do produto] [Marca] [Modelo/Variação] [Atributo principal]
```
Exemplo para GB: `Pote Hermético Vidro Budamix 700ml Tampa Bambu Conjunto 3 Peças`

**Regras de título:**
- Máximo 60 caracteres visíveis (o ML corta)
- Sem maiúsculas excessivas, sem repetições
- Palavra-chave principal no início
- Sem preço, sem condições no título
- Sem símbolos especiais

**Fotos:**
- Mínimo: 1 foto (mas o algoritmo penaliza anúncios com poucas fotos)
- Recomendado: 5-7 fotos
- Principal: fundo branco, produto centralizado, sem marcas d'água
- Adicionais: detalhes, lifestyle, dimensões, uso, kit completo
- Qualidade: mínimo 500x500px, recomendado 1200x1200px

**Ficha técnica:**
- Preencher 100% dos campos (algoritmo favorece completude)
- Material, dimensões, capacidade, cor, marca, modelo
- Atributos extras quando disponíveis

---

### 🏆 FATOR 7: Preço Competitivo (Peso: ALTO)
**Como funciona:**
- O ML compara preços de produtos similares na mesma busca
- Preço muito alto = menos conversão = queda no ranking
- Preço muito baixo = pode sinalizar problema de qualidade (mas menos impacto que muito alto)
- O ML oferece ajuste automático de preço (você define min/max)

**Estratégia:**
- Para catálogo: o preço é um dos principais critérios de quem ganha destaque
- Para orgânico: preço competitivo melhora CTR e conversão, que por sua vez melhoram ranking
- Incluir custo de frete na precificação para oferecer frete grátis sem prejudicar margem

**Para kits e combos:** Analisar concorrentes de kit vs. produto unitário. Kits podem ter menos concorrência e melhor margem.

---

### 🏆 FATOR 8: Frete Grátis (Peso: ALTO)
**Como funciona:**
- Produtos com frete grátis têm destaque visual (tag) e preferência do algoritmo
- O filtro "Frete grátis" é muito usado pelos compradores — sem ele, você some para parte do tráfego
- Mercado Envios: estrutura de frete com subsidio do ML para vendedores com bom desempenho

**Modalidades:**
- **Full**: Frete grátis automático para pedidos acima do threshold
- **Coleta**: ML busca no depósito do seller
- **ME2 (agência)**: Seller leva em agência parceira
- **Flex**: Entrega própria (mesma cidade)

---

### 🏆 FATOR 9: Taxa de Conversão (Peso: ALTO)
**Como funciona:**
- Razão entre visitas no anúncio e compras efetivadas
- Anúncio com alta conversão = o algoritmo "aprende" que é um produto desejável
- Taxa de conversão baixa (muitas visitas, poucas vendas) = sinal negativo

**O que afeta a conversão:**
- Preço
- Qualidade das fotos
- Completude das informações (se o comprador não tem a informação que precisa, sai sem comprar)
- Perguntas respondidas (dúvidas não respondidas = carrinho abandonado)
- Avaliações positivas

**Para GB:** Em utilidades domésticas, as principais dúvidas são: capacidade (ml/L), material exato, compatibilidade com micro-ondas/freezer, vedação, conjunto ou unitário. Responder isso antecipadamente na descrição é essencial.

---

### 🏆 FATOR 10: Mercado Ads / Product Ads (Peso: MODERADO-ALTO)
**Como funciona:**
- Product Ads colocam o produto nas primeiras posições com tag "Patrocinado"
- O ML usa sistema de leilão (Ad Rank) que combina ROAS Objetivo e relevância
- **Efeito Halo**: Ads → mais vendas → melhora ranking orgânico (ciclo virtuoso)

**Mudança importante 2024:**
- ML migrou de ACOS (%) para ROAS (retorno sobre investimento)
- ROAS ideal varia por categoria e margem
- TACOS = gasto com ADS / faturamento total (orgânico + pago) — métrica mais honesta

**Estratégia de ADS no ML:**
- Começar com campanha automática para identificar palavras-chave com conversão
- Migrar keywords boas para campanha manual
- Usar ADS para anúncios que já convertem bem (não para salvar anúncios ruins)
- ADS complementa orgânico — não substitui qualidade do anúncio

**Palavras-chave de cauda longa:**
- Dados do ML Ads: 30% menos concorrência e até 2x mais conversão
- Ex: "pote hermético vidro 700ml tampa bambu" vs. apenas "pote hermético"

---

### 🏆 FATOR 11: Histórico e Longevidade do Anúncio (Peso: MODERADO)
**Como funciona:**
- Anúncios mais antigos com bom histórico têm vantagem acumulada
- Parar/pausar um anúncio e reativar pode causar reset parcial ou total do histórico
- Mudar o título de um anúncio com histórico é um dilema — pode afetar o posicionamento

**Implicação:** Nunca pausar anúncios de bom desempenho. Se precisar ajustar, ajuste sem pausar.

---

### 🏆 FATOR 12: Variações e Kits (Peso: MODERADO)
**Variações:**
- Um anúncio com variações (tamanhos, cores) concentra todo o histórico de vendas em um lugar
- Melhor do que ter N anúncios separados para cada variação
- Ex: Kit 3 potes (500ml, 700ml, 1L) em variação = histórico unificado = mais força de ranking

**Kits e Combos:**
- Kits geralmente têm menos concorrência que produtos unitários
- Ticket médio maior = mais faturamento por venda (favorece MercadoLíder)
- Kits ultrapassam o threshold de R$79 mais facilmente (ativa frete grátis padrão do ML)
- Podem ser precificados com margem melhor (comprador percebe valor agregado)
- Estratégia: criar kits "exclusivos" que não têm concorrência direta

---

## 1.3 Penalizações — O que Faz Cair

| Ação | Impacto |
|------|---------|
| Cancelamento pelo vendedor > 2,5% | Reputação cai |
| Atrasos no envio > 15% | Reputação cai |
| Reclamações > 3% | Reputação cai |
| Estoque zerado com anúncio ativo | Pode pausar automaticamente + prejudica histórico |
| Pausar e reativar anúncio | Possível reset parcial do histórico |
| Mudança brusca de preço (muito alto) | Perde competitividade no catálogo |
| Fotos sem qualidade | Pode não aparecer nas primeiras posições |
| Anúncio sem ficha técnica completa | Menos visibilidade em filtros e buscas específicas |
| Muitas perguntas sem resposta | Reduz conversão = queda no ranking |
| Categoria errada | Invisível para quem pesquisa corretamente |

---

## 1.4 Estratégias de Otimização — ML

### Título ideal para potes herméticos:
```
Pote Hermético Vidro [capacidade] [atributo] Budamix [conjunto/kit]
```
Exemplos:
- `Pote Hermético Vidro 700ml Tampa Bambu Budamix Conjunto 3 Peças`
- `Pote Hermético Vidro 1L Herméticos Mantimento Budamix Kit 6 Unidades`
- `Conjunto Potes Herméticos Vidro Budamix 500ml 700ml 1L Tampa Bambu`

### Checklist de otimização ML:
- [ ] Entrar no catálogo do produto (se disponível)
- [ ] Preencher 100% da ficha técnica
- [ ] 6+ fotos de qualidade (fundo branco + detalhes + lifestyle + infográfico)
- [ ] Título com palavra-chave principal no início
- [ ] Preço competitivo vs. top 5 da categoria
- [ ] Ativar Full (ou coleta) para prazo de entrega rápido
- [ ] Manter reputação verde: < 3% reclamações, < 2,5% cancelamentos, < 15% atrasos
- [ ] Responder perguntas em < 1 hora
- [ ] Participar da Central de Promoções (Ofertas do dia, Relâmpago)
- [ ] Ativar Product Ads com ROAS objetivo realista
- [ ] Criar variações para concentrar histórico
- [ ] Criar kits para subir ticket médio e fugir da concorrência direta

---

# 2. SHOPEE

## 2.1 Como funciona o Algoritmo

O algoritmo da Shopee é fundamentado em **quatro pilares principais**:

1. **Relevância do Anúncio** — Correspondência de palavras-chave (título, descrição, categorias), densidade e posição dos termos
2. **Desempenho da Loja** — Taxa de resposta no chat, tempo de envio, avaliações, taxa de cancelamento
3. **Engajamento do Comprador** — CTR (taxa de cliques nos resultados) e taxa de conversão na página do produto
4. **Central de Marketing** — Participação em campanhas, uso de ferramentas promocionais da Shopee

**Diferença fundamental vs. ML:**
- Shopee dá muito mais peso para o **engajamento social** (Shopee Live, vídeos, curtidas)
- Sistema de **pontos de penalidade** mais estruturado e transparente
- Keywords têm peso alto tanto no título quanto na descrição
- Frete patrocinado é praticamente obrigatório para competir

---

## 2.2 Fatores de Ranking — Shopee

### 🏆 FATOR 1: Relevância de Keywords (Peso: MUITO ALTO)
**Como funciona:**
- O algoritmo analisa correspondência entre o que o comprador buscou e o conteúdo do anúncio
- Título tem mais peso que descrição
- Também analisa: categorias, atributos, tags do produto

**Estrutura de título ideal na Shopee:**
```
Marca + Nome do Produto/Modelo + Principal Característica + Palavra-Chave Relevante
```
- Limite: **120 caracteres**
- Começar com a keyword mais importante
- Evitar keyword stuffing (penaliza)

Exemplo para GB:
`Budamix Pote Hermético Vidro 700ml Tampa Bambu Organizador Mantimentos`

**Tags de produto (Shopee):**
- Diferente do ML, Shopee tem campo específico de "tags"
- Usar até 20 tags relevantes
- Tags em singular e plural
- Tags longtail: "pote vidro com tampa", "organizador mantimentos vidro"

---

### 🏆 FATOR 2: Vendas Recentes (Peso: MUITO ALTO)
**Como funciona:**
- Igual ao ML — volume recente de vendas impacta diretamente o ranking
- Velocidade de vendas importa mais que volume total histórico
- Participar de Flash Sale gera spikes de venda que impulsionam orgânico posterior

---

### 🏆 FATOR 3: Avaliações e Rating (Peso: MUITO ALTO)
**Como funciona:**
- Estrelas e comentários têm peso alto no algoritmo Shopee (maior que no ML)
- Avaliações com foto/vídeo têm mais peso
- Média ideal: entre 4.7 e 4.9 (5.0 perfeito pode parecer artificial)
- Volume de avaliações importa tanto quanto a nota

**Como incentivar avaliações:**
- Mensagem automática pós-entrega pedindo review
- Programa "Moedas por Avaliação" da Shopee (incentiva review com foto/vídeo)
- Qualidade da embalagem e do produto = reviews positivos naturais

**Ponto crítico:** Avaliações abaixo de 3.2 estrelas penalizam severamente o ranking.

---

### 🏆 FATOR 4: Performance de Entrega (Peso: MUITO ALTO)
**Como funciona:**
- Taxa de não envio (pedidos não enviados no prazo)
- Tempo médio de envio desde a venda
- Histórico de atrasos e não entregas

**Thresholds críticos Shopee 2025:**
- Taxa de não envio acima de 40% em uma semana = 1 ponto de penalidade extra
- Taxa de não cumprimento de envio > 12% na semana = queda de desempenho
- Qualquer atraso pode gerar penalidade dependendo do contexto

**Full Shopee (lançado set/2024):**
- Fulfillment da Shopee — centro de distribuição em Franco da Rocha/SP
- Melhora tempo de entrega e elimina risco de penalidade por atraso
- Ainda com elegibilidade restrita (categorias selecionadas, operação em São Paulo)
- Para utilidades domésticas: verificar elegibilidade — pode ser uma vantagem enorme

---

### 🏆 FATOR 5: Taxa de Resposta no Chat (Peso: ALTO)
**Como funciona:**
- Shopee mede taxa de resposta no chat em tempo real
- Meta: responder 100% das mensagens em < 12 horas
- Chat responsivo influencia diretamente o status de Star Seller
- Respostas rápidas = melhor experiência = mais conversão = melhor ranking

---

### 🏆 FATOR 6: Star Seller (Peso: ALTO)
**Como funciona:**
- Programa de reconhecimento da Shopee para lojas de excelência
- Boost de visibilidade confirmado para lojas Star Seller
- Requisitos (aproximados): rating alto, taxa de cancelamento baixa, envio no prazo, chat responsivo

**Benefícios:**
- Badge visual na loja = mais cliques
- Melhor posicionamento nos resultados
- Elegibilidade para campanhas exclusivas
- Programa de Frete Grátis com mais benefícios

---

### 🏆 FATOR 7: Frete Grátis / Frete Patrocinado (Peso: MUITO ALTO)
**Como funciona:**
- Programa de Frete Grátis da Shopee é quase mandatório para competir
- Produtos com frete grátis aparecem em destaque e têm filtro específico muito usado
- Dois tipos: frete grátis pago pelo vendedor vs. frete patrocinado pela Shopee

**Frete Patrocinado Shopee:**
- A Shopee subsidia parte do frete para o seller
- Requer elegibilidade (bom histórico, produtos elegíveis)
- Adicionar o custo de frete embutido no preço é estratégia comum

---

### 🏆 FATOR 8: Shopee Ads (Peso: MODERADO-ALTO)
**Tipos:**
- **Search Ads**: Produto aparece nas primeiras posições de busca com tag "Patrocinado"
- **Discovery Ads**: Produto aparece em outros contextos (página inicial, recomendações)

**Sistema de lances:**
- CPC (custo por clique)
- ACOS = valor gasto em ADS / receita gerada por ADS
- Métrica de ranking de anúncio: "Classificação média" = posição média do anúncio nos resultados pagos

**Estratégia avançada:**
1. Começar com palavras-chave broad para descobrir o que converte
2. Identificar keywords de alta conversão
3. Mover para correspondência exata com lance maior
4. Pausar keywords com alto CPC e baixa conversão
5. Reduzir ACOS gradualmente sem perder posição

---

### 🏆 FATOR 9: Participação em Campanhas (Peso: ALTO)
**Como funciona:**
- Flash Sale, Shopee Live, campanhas temáticas dão exposição extra massiva
- Participar de campanhas gera spikes de venda que impulsionam ranking orgânico
- Shopee Live: transmissão ao vivo com demonstração de produto = conversão muito alta
- Lojas com pontos de penalidade são excluídas das campanhas (perda dupla: sem campanha + penalidade)

**Para GB:** Shopee Live com demonstração de potes herméticos (organizando despensa, mostrando vedação) pode ser altamente eficaz. Utilidades domésticas têm apelo visual forte em lives.

---

### 🏆 FATOR 10: Vídeo no Listing (Peso: MODERADO)
**Como funciona:**
- Produtos com vídeo têm maior taxa de conversão (relatório: +25% em algumas categorias)
- Algoritmo favorece listings com vídeo
- Vídeo ideal: 30-60 segundos mostrando uso, vedação, qualidade do produto

---

### 🏆 FATOR 11: Variações de Produto (Peso: MODERADO)
**Como funciona:**
- Similar ao ML: variações concentram histórico de vendas
- Criar variações de capacidade (500ml, 700ml, 1L) em um mesmo listing maximiza força

---

## 2.3 Sistema de Penalizações — Shopee (Detalhado)

A Shopee tem um dos sistemas de penalização mais estruturados dos 3 marketplaces.

### Sistema de Pontos de Penalidade (atualizado jan/2025):
- **0 pontos**: Tudo normal, todos os benefícios
- **1-2 pontos**: Alerta, sem perda de benefícios ainda
- **3+ pontos**: Começa a perder visibilidade e pode sair de campanhas promocionais
- **Faixas altas (18, 21, 24 pontos)**: Conta pode ser congelada temporariamente

**Ciclos de avaliação:**
- Trimestral (jan-mar, abr-jun, jul-set, out-dez)
- Pontos são zerados no início de cada trimestre, mas punições em andamento continuam

### Motivos de penalidade:
| Infração | Pontos |
|----------|--------|
| Atraso no envio | 1 ponto por ocorrência |
| Taxa de não envio > 40% na semana | 1 ponto extra |
| Cancelamento pelo vendedor | 1 ponto |
| Anúncio de produto proibido | 1-2 pontos |
| Spam/duplicação de anúncios | 1-2 pontos |
| Violação de propriedade intelectual | 2 pontos |
| Nome de loja impróprio | 2 pontos |

**Consequências práticas:**
- Perda de visibilidade proporcional nos últimos 30 dias
- Exclusão de Flash Sales e campanhas
- Perda de status Star Seller
- Perda de elegibilidade para frete patrocinado

### Período crítico: Finais de semana
- A maioria das penalizações ocorre por atrasos em pedidos de sexta/sábado
- Estratégia: enviar antes da sexta, organizar operação para envio no sábado

---

## 2.4 Estratégias de Otimização — Shopee

### Checklist de otimização Shopee:
- [ ] Título: 120 chars, keyword principal no início, estrutura: Marca + Produto + Característica + KW
- [ ] 9+ fotos de qualidade (min 500x500, ideal 2000x2000, fundo branco na principal)
- [ ] Vídeo de produto (30-60 segundos demonstrando uso)
- [ ] Descrição detalhada com keywords naturais (responder: material, capacidade, vedação, cuidados)
- [ ] 20 tags relevantes (singular + plural + longtail)
- [ ] Participar do Frete Grátis / Frete Patrocinado
- [ ] Taxa de resposta no chat: 100% em < 12h
- [ ] Zero pontos de penalidade — ops de envio no prazo
- [ ] Participar de Flash Sales mensais
- [ ] Ativar Shopee Ads (Search Ads) nas principais keywords
- [ ] Criar variações para concentrar histórico
- [ ] Solicitar avaliações via mensagem pós-entrega + "Moedas por Avaliação"
- [ ] Planejar Shopee Live para demonstração de produto

---

# 3. AMAZON BRASIL

## 3.1 O Algoritmo A10 — Evolução do A9

### A9 vs A10: O que mudou
**Algoritmo A9 (modelo anterior):**
- Foco principal em velocidade de vendas (mais vendas = melhor ranking)
- Palavras-chave no título e bullets
- PPC (Sponsored Products) tinha impacto direto no ranking orgânico
- CTR e conversão importavam
- Preço competitivo fundamental

**Algoritmo A10 (modelo atual):**
- **Tráfego externo importa** — Amazon agora recompensa produtos que trazem tráfego de Google, redes sociais, influenciadores
- **Vendas orgânicas > vendas por PPC** para ranking — PPC ainda gera vendas mas impacta menos o orgânico que antes
- **Autoridade do seller** ganhou peso — histórico, feedback, métricas de performance
- **Engajamento com o listing** — tempo na página, interações, FAQ respondidas
- **Conteúdo de qualidade** — A+ Content, vídeos, imagens ricas

**Estudo Lett/Neogrid (out/2024 a mar/2025):**
- 86% das vendas estão concentradas nos **10 primeiros resultados**
- Posição média nos últimos 5 dias é uma das variáveis mais determinantes
- Produtos com estabilidade de posição tendem a permanecer bem ranqueados
- Rating ideal: **4.9 estrelas** (não 5.0 — "imperfeição" aumenta autenticidade)
- Avaliações entre 1 e 3.2 estrelas: queda de performance
- Avaliações > 4.7 estrelas: ganhos de ranking
- Preço muito baixo ou muito alto prejudicam — faixa competitiva moderada é ideal

---

## 3.2 Buy Box — Conceito Crítico

### O que é:
- Botão "Adicionar ao carrinho" / "Comprar agora" em destaque na página de produto
- Apenas UM vendedor ocupa a Buy Box por vez (quando há múltiplos vendedores do mesmo produto)
- A maioria esmagadora das vendas acontece pela Buy Box
- Para marcas próprias (ex: Budamix) que são os únicos vendedores: Buy Box é automática se elegível

### Critérios para ganhar a Buy Box:
1. **Preço competitivo total** (produto + frete)
2. **Método de envio** — FBA ou Seller Fulfilled Prime (SFP) têm vantagem enorme
3. **Disponibilidade de estoque** — sem estoque = não compete
4. **Métricas do seller** — ODR (Order Defect Rate), cancelamentos, pontualidade
5. **Avaliação do seller**
6. **Tempo de envio** — quanto mais rápido, melhor

**Para GB (marca própria Budamix):**
- Por ser marca exclusiva e única vendedora, Buy Box deve ser automática se atender critérios de elegibilidade (prime seller account, estoque disponível, métricas em dia)

---

## 3.3 Fatores de Ranking — Amazon

### 🏆 FATOR 1: Relevância de Keywords (Peso: CRÍTICO)
**Onde o algoritmo indexa keywords:**
1. **Título** — peso máximo, primeiros 80 chars são os mais importantes
2. **Bullet Points** — peso alto
3. **Descrição** — peso médio
4. **Backend Keywords** — peso médio (não visíveis para comprador)
5. **A+ Content** — peso baixo/indireto (melhora conversão mais que ranking direto)

**Estrutura de título Amazon (fórmula padrão):**
```
Marca + Produto + Característica Principal + Material + Tamanho/Capacidade + Cor + Quantidade
```
Exemplo para GB:
`Budamix Pote Hermético de Vidro com Tampa de Bambu 700ml | Conjunto 3 Potes para Mantimentos e Organização da Cozinha`

**Limites:**
- Título: 200 caracteres (recomendado até 150 para não truncar)
- Bullets: 5 bullets, 500 caracteres cada (Amazon processa até 1000 mas menos é mais)
- Backend keywords: 249 bytes (sem repetir palavras que já estão no título)

**Backend keywords — o que incluir:**
- Variações de grafia (pote hermético, pote hermetico)
- Sinônimos (frasco vidro, recipiente vidro, vasilha vidro)
- Uso (organizar despensa, guardar café, conservar alimentos)
- Palavras em inglês que o brasileiro digita (glass jar, hermetic container)

---

### 🏆 FATOR 2: Sales Velocity / BSR (Peso: MUITO ALTO)
**Como funciona:**
- BSR (Best Seller Rank) = ranking dentro da categoria
- Quanto mais se vende, menor o número do BSR (melhor)
- BSR é calculado em tempo real, mas com peso maior para vendas recentes
- Subir no BSR = mais visibilidade = mais vendas (efeito bola de neve)

**Ciclo virtuoso:**
PPC → mais vendas → BSR sobe → ranking orgânico melhora → mais vendas orgânicas → BSR continua subindo

---

### 🏆 FATOR 3: Avaliações (Peso: MUITO ALTO)
**Métricas:**
- **Quantidade**: Volume de reviews importa tanto quanto a nota
- **Qualidade**: Reviews com fotos/vídeos têm mais peso
- **Nota ideal**: 4.9 estrelas (estudo Neogrid/Lett)
- **Threshold crítico**: Abaixo de 4.7 começa a perder ranking

**Como conseguir reviews na Amazon:**
- Amazon Vine Program (por convite, para novos produtos) — a Amazon envia amostras para Vine Voices
- Follow-up por email via Seller Central (limitado — não pode pedir review diretamente, só solicitar feedback)
- Produto de qualidade = review orgânico natural

---

### 🏆 FATOR 4: FBA — Fulfillment by Amazon (Peso: MUITO ALTO)
**Por que importa:**
- FBA = produtos elegíveis ao Amazon Prime
- Prime = frete grátis em 1-2 dias = conversão muito maior
- FBA tem vantagem na Buy Box sobre FBM (Fulfilled by Merchant)
- A Amazon "confia" mais em produtos FBA (ela controla a logística)

**Custos FBA Brasil 2026 (aproximado):**
- Taxa de armazenagem: por m³/mês (varia por categoria e temporada)
- Taxa de fulfillment: por unidade enviada (varia por peso/dimensão)
- Taxa de referência (comissão): 11-15% do preço de venda dependendo da categoria

**Para potes herméticos de vidro:**
- Atenção ao peso e fragilidade — FBA pode ter custo mais alto por ser vidro pesado
- Calcular viabilidade por SKU — kits maiores podem diluir custo fixo de FBA
- Verificar se categoria "Cozinha e Jantar" tem restrições de embalagem para vidro

---

### 🏆 FATOR 5: A+ Content (Peso: MODERADO — impacto em conversão)
**O que é:**
- Conteúdo enriquecido abaixo da descrição (imagens, tabelas comparativas, textos formatados)
- Disponível para marcas registradas (Brand Registry)
- Impacto direto: melhora conversão (não indexação de keywords)
- Impacto indireto: mais conversão = mais vendas = melhor ranking

**Para GB/Budamix:**
- Com marca registrada no INPI, a GB tem direito ao Brand Registry da Amazon
- Brand Registry = acesso ao A+ Content, Sponsored Brands, Brand Store
- A+ Content deve mostrar: comparativo de capacidades, benefícios do vidro vs. plástico, cuidados de conservação, visual da coleção Budamix

---

### 🏆 FATOR 6: CTR (Click-Through Rate) (Peso: ALTO)
**Como funciona:**
- Taxa de cliques no resultado de busca
- Produto que aparece nos resultados mas ninguém clica = sinal negativo
- O que impacta CTR: foto principal, preço, estrelas, badge Prime, título

**Para melhorar CTR:**
- Foto principal: produto visivelmente atrativo, fundo branco, occupando 85%+ do frame
- Preço: competitivo (não precisa ser o menor)
- Prime badge: FBA = Prime automático = mais cliques
- Amazon Choice / Best Seller badge: automaticamente concedidos quando o produto performa bem

---

### 🏆 FATOR 7: Tráfego Externo (Peso: ALTO — diferencial do A10)
**Como funciona:**
- Amazon A10 recompensa produtos que trazem tráfego de fora da plataforma
- Google indexa listagens Amazon — produto bem posicionado no Google = tráfego extra
- Influenciadores com link direto para Amazon = sinal positivo para o algoritmo
- Pinterest, Instagram, YouTube com links = tráfego de qualidade

**Para GB:**
- Instagram/TikTok mostrando organização de despensa com potes Budamix + link Amazon
- Artigos de blog "melhores potes para organização" com link Amazon
- Parcerias com criadores de conteúdo de organização de casa

---

### 🏆 FATOR 8: Amazon PPC — Sponsored Products (Peso: MODERADO-ALTO)
**Como funciona:**
- Sponsored Products = anúncios pagos que aparecem nos resultados de busca
- No A10: PPC ainda gera vendas, mas impacto no orgânico é menor que no A9
- PPC é fundamental para novos produtos (zero histórico = zero ranking orgânico)

**Flywheel Effect:**
```
PPC → Vendas → Reviews → Ranking Orgânico sobe → Mais vendas orgânicas → Menos dependência de PPC
```

**Tipos de campanha Amazon:**
- **Sponsored Products**: produto individual nos resultados de busca
- **Sponsored Brands**: banner com logo e múltiplos produtos (requer Brand Registry)
- **Sponsored Display**: display em outras páginas e sites (retargeting)

---

## 3.3 Penalizações — Amazon

| Problema | Consequência |
|----------|--------------|
| Stockouts (estoque zerado) | Perda de Buy Box + queda no BSR + difícil recuperar posição |
| ODR alto (Order Defect Rate > 1%) | Suspensão de conta |
| Late Shipment Rate > 4% | Advertência + potencial suspensão |
| Cancelamentos > 2.5% | Afeta elegibilidade para Buy Box |
| Reviews negativos (< 3.5 média) | Queda abrupta no ranking |
| Keyword stuffing no título/bullets | Amazon remove ou penaliza listing |
| Imagem principal não no fundo branco | Amazon pode suprimir o listing |
| Violação de políticas | Remoção do listing ou suspensão |
| Preço muito diferente da concorrência | Supressão da Buy Box |

**Stockout é o maior risco para Amazon:**
- Uma semana sem estoque pode levar meses para recuperar o ranking
- FBA ajuda — Amazon gerencia reposição e alerta antes de zerar

---

## 3.4 Estratégias de Otimização — Amazon

### Estrutura de bullets otimizados (5 bullets):
```
Bullet 1: PRINCIPAL BENEFÍCIO — ex: "VIDRO DE QUALIDADE: Material 100% vidro borossilicato, livre de BPA..."
Bullet 2: FUNCIONALIDADE — ex: "VEDAÇÃO HERMÉTICA: Tampa com borracha de silicone garante..."
Bullet 3: VERSATILIDADE — ex: "MÚLTIPLOS USOS: Ideal para grãos, café, chá, especiarias..."
Bullet 4: KIT COMPLETO — ex: "KIT COM 3 POTES: Conjunto com capacidades 500ml, 700ml e 1L..."
Bullet 5: GARANTIA/MARCA — ex: "MARCA BUDAMIX: Garantia de 12 meses, suporte ao cliente..."
```

### Checklist de otimização Amazon:
- [ ] Registrar marca no Brand Registry da Amazon (usa INPI BR)
- [ ] Título: Marca + Produto + Característica + Capacidade + Quantidade (até 150 chars)
- [ ] 5 bullet points otimizados com keywords naturais
- [ ] Backend keywords: 249 bytes sem repetir título/bullets
- [ ] A+ Content criado (infográfico, comparativo de capacidades, lifestyle)
- [ ] 7-9 imagens: principal fundo branco + detalhes + lifestyle + infográfico + kit
- [ ] Vídeo do produto (demonstração de uso e vedação)
- [ ] FBA ativo (verificar viabilidade de custo para vidro pesado)
- [ ] Preço competitivo na faixa da categoria
- [ ] PPC: Sponsored Products com keywords automáticas inicialmente
- [ ] Monitorar BSR diariamente
- [ ] Programa de revisão de avaliações (nenhum incentivo direto — policy)
- [ ] Parent-child listing para variações de tamanho

---

# 4. ANÁLISE CRUZADA

## 4.1 Matriz Comparativa — Fatores de Ranking

| Fator | Mercado Livre | Shopee | Amazon BR |
|-------|--------------|--------|-----------|
| **Palavras-chave no título** | ⭐⭐⭐⭐⭐ Crítico | ⭐⭐⭐⭐⭐ Crítico | ⭐⭐⭐⭐⭐ Crítico |
| **Vendas recentes** | ⭐⭐⭐⭐⭐ Principal | ⭐⭐⭐⭐⭐ Principal | ⭐⭐⭐⭐ Muito alto |
| **Reputação/Rating do seller** | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alto (ODR) |
| **Avaliações (reviews)** | ⭐⭐⭐ Moderado | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐⭐⭐⭐ Muito alto |
| **Frete grátis/rápido** | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐⭐⭐ Alto (Prime) |
| **Fulfillment próprio** | ⭐⭐⭐⭐⭐ ML Full | ⭐⭐⭐⭐ Full Shopee | ⭐⭐⭐⭐⭐ FBA |
| **Preço competitivo** | ⭐⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alto |
| **Taxa de conversão** | ⭐⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alto | ⭐⭐⭐⭐ Alto |
| **Ads pagos** | ⭐⭐⭐⭐ Alto | ⭐⭐⭐ Moderado | ⭐⭐⭐⭐ Alto |
| **Conteúdo (descrição/A+)** | ⭐⭐⭐ Moderado | ⭐⭐⭐ Moderado | ⭐⭐⭐⭐ Alto |
| **Tempo de resposta (chat)** | ⭐⭐⭐ Moderado | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐ Baixo |
| **Participação em campanhas** | ⭐⭐⭐ Moderado | ⭐⭐⭐⭐⭐ Muito alto | ⭐⭐ Baixo |
| **Catálogo/ASIN compartilhado** | ⭐⭐⭐⭐⭐ Crítico (catálogo ML) | N/A | ⭐⭐⭐ Parent-child |
| **Vídeo no listing** | ⭐⭐ Baixo | ⭐⭐⭐⭐ Alto | ⭐⭐⭐ Moderado |
| **Tráfego externo** | ⭐ Pouco relevante | ⭐ Pouco relevante | ⭐⭐⭐⭐ Alto (A10) |
| **Engajamento social/lives** | ⭐ Mínimo | ⭐⭐⭐⭐ Alto | ⭐ Mínimo |
| **Conteúdo enriquecido (A+)** | ⭐ Não tem | ⭐ Limitado | ⭐⭐⭐⭐ Alto |
| **Variações/kits** | ⭐⭐⭐⭐ Concentra histórico | ⭐⭐⭐⭐ Concentra histórico | ⭐⭐⭐⭐ Parent-child |
| **Status especial** | ⭐⭐⭐⭐ MercadoLíder | ⭐⭐⭐ Star Seller | ⭐⭐ Não tem equivalente |

---

## 4.2 Similaridades — O que é Universal

**Funcionam nas 3 plataformas sem exceção:**

1. **Keywords no título**: Palavra-chave principal no início do título é lei nas 3 plataformas
2. **Vendas recentes dominam**: Volume recente de vendas é o fator mais poderoso nas 3
3. **Preço competitivo**: Não precisa ser o menor, mas precisa estar na faixa
4. **Frete grátis/rápido**: Essencial para competir — comprador quer entrega rápida e barata
5. **Zero cancelamentos/atrasos**: Penaliza nas 3 plataformas
6. **Fotos de qualidade**: Critério de admissão mínima + impacto em CTR
7. **Taxa de conversão**: Quanto mais visitas viram venda, melhor o ranking
8. **Variações concentram poder**: Unificar SKUs variantes em um listing/anúncio é vantagem
9. **Ads aceleram o orgânico**: PPC gera vendas que melhoram o ranking natural
10. **Estoque zerado é catastrófico**: Nas 3 plataformas, zerar estoque prejudica fortemente

---

## 4.3 Diferenças Críticas

### Onde cada plataforma diverge:

**Mercado Livre — Único(s):**
- **Catálogo**: Nenhuma outra plataforma tem a hierarquia de catálogo vs. individual do ML. Se você não está no catálogo, está atrás de todos que estão.
- **Reputação como gatekeeper**: Reputação laranja/vermelha bloqueia acesso ao catálogo. Nas outras, reputação impacta mas não exclui.
- **MercadoLíder**: Status com impacto direto em visibilidade — equivalente não existe na Shopee/Amazon.
- **ROAS como métrica de ADS**: ML agora usa ROAS (não ACOS) — diferente da Amazon que ainda usa ACOS.

**Shopee — Único(s):**
- **Chat como fator de ranking**: Nenhuma outra plataforma penaliza tanto por taxa de resposta no chat.
- **Sistema de Pontos de Penalidade**: O mais estruturado e transparente dos 3 — você sabe exatamente onde está.
- **Lives e engajamento social**: Shopee Live tem impacto real em ranking — ML e Amazon não têm equivalente relevante.
- **Campanhas como gatilho de visibilidade**: Participar de Flash Sale é mais impactante na Shopee do que promoções equivalentes no ML.
- **Tags de produto**: Campo específico de tags para indexação — ML e Amazon não têm exatamente isso.

**Amazon — Único(s):**
- **Tráfego externo**: A10 recompensa explicitamente quem traz tráfego de fora — único dos 3 que faz isso.
- **A+ Content / Brand Registry**: Conteúdo enriquecido com impacto real — ML tem recursos menores, Shopee ainda incipiente.
- **Backend keywords**: Campo oculto de keywords — permite indexar termos sem poluir o título. ML e Shopee não têm equivalente.
- **Buy Box como conceito**: O mais desenvolvido dos 3 — relevante principalmente quando há múltiplos sellers do mesmo produto.
- **BSR**: Métrica pública de ranking por categoria — transparência que ML e Shopee não oferecem.

---

## 4.4 Armadilhas de Estratégia Cruzada

**Erros comuns ao aplicar estratégia de uma plataforma em outra:**

1. **Título longo do ML no Amazon**: ML aceita até 60 chars visíveis. Amazon permite 200. No ML, enxugar. Na Amazon, aproveitar todos os caracteres com keywords.

2. **Focar em ADS e esquecer o orgânico**: No A9 da Amazon, ADS tinham impacto forte no orgânico. No A10, menos. No ML, ADS ajudam mas não substituem qualidade do anúncio. Na Shopee, ADS sem boas métricas de loja não resolvem.

3. **Ignorar o Chat na Shopee**: Vendedor acostumado com ML/Amazon (onde chat tem peso menor) pode deixar chat da Shopee demorado e ser penalizado.

4. **Não entrar no Catálogo do ML**: Seller que migra da Shopee/Amazon para ML e não percebe que o catálogo é a posição mais valiosa — fica sem entender por que não sobe de ranking.

5. **Stockout na Amazon é pior**: Uma semana sem estoque na Amazon pode levar meses para recuperar o BSR. No ML e Shopee, o impacto é alto mas a recuperação pode ser mais rápida.

6. **Reviews na Shopee são mais críticos que no ML**: No ML, reviews importam mas são menos determinantes. Na Shopee, média abaixo de 4.7 é sinal vermelho para o algoritmo.

7. **Tráfego externo para ML/Shopee**: Estratégia de trazer tráfego externo (Google Ads, Instagram) funciona muito bem para Amazon (A10 recompensa). Para ML e Shopee, o impacto é bem menor — melhor focar em otimização interna.

---

# 5. GB IMPORTADORA — RECOMENDAÇÕES

## 5.1 Recomendações para Potes Herméticos de Vidro

### Palavras-chave essenciais por plataforma

**Mercado Livre — Keywords para título:**
- `pote hermético vidro` (principal)
- `pote vidro tampa bambu`
- `conjunto potes herméticos`
- `kit potes mantimentos`
- `pote vidro organização`
- `recipiente hermético vidro`
- `vasilha vidro hermética`
- `pote vidro com tampa`

**Shopee — Keywords + Tags:**
- Título principal: `pote hermético vidro tampa bambu` (início)
- Tags: pote vidro, pote hermético, organizador mantimentos, vasilha vidro, kit potes, pote com tampa, frasco vidro, organização despensa
- Longtail: `pote de vidro com tampa hermética para mantimentos`

**Amazon — Keywords (título + backend):**
- Título: `Budamix Pote Hermético de Vidro + Tampa de Bambu`
- Backend keywords: pote hermetico vidro, vasilha vidro, frasco vidro, glass jar, hermetic container, organização cozinha, mantimentos, café açúcar

---

## 5.2 Estratégia de Kits e Combos por Plataforma

### Mercado Livre:
- **Kit unitário por capacidade** (ex: Kit 3 potes 700ml): Ideal para quem compra para substituir
- **Kit multi-capacidade** (ex: 500ml + 700ml + 1L): Para quem quer sortir a despensa — ticket maior, menos concorrência
- **Combo organizador** (potes + bandeja + identificadores): Se a GB tiver produtos MDF, criar combo cross-sell
- Estratégia: entrar no catálogo com produto unitário de maior venda e criar anúncios individuais de kit

### Shopee:
- Kits são mais valorizados — comprador Shopee adora "Kit X unidades"
- Flash Sale com kit especial (ex: "Kit Budamix Verão: 4 potes + brinde")
- Variações: colocar diferentes qtdes como variação no mesmo listing (Kit 3, Kit 6, Kit 9)
- Live demonstrando organização da despensa com múltiplos tamanhos

### Amazon:
- Parent-child listing: produto "pai" com filhos por capacidade
- Kit dedicado como ASIN separado (Amazon trata kits como produtos distintos)
- A+ Content mostrando comparativo visual de tamanhos e usos
- Bundle com outros itens de organização se possível (associação com outros sellers)

---

## 5.3 Precificação Cruzada — Como não Canibalizar

**Problema:** Se os preços são iguais nas 3 plataformas, o comprador vai para onde tem mais desconto. Se são muito diferentes, gera percepção de valor inconsistente.

**Estratégia recomendada:**

| Plataforma | Posicionamento | Justificativa |
|-----------|---------------|---------------|
| **Mercado Livre** | Preço referência (base) | Maior volume, maior concorrência, precisa ser competitivo |
| **Shopee** | Ligeiramente mais baixo (-5% a -10%) | Público mais sensível a preço, competição maior com produtos genéricos chineses |
| **Amazon** | Igual ou ligeiramente acima (+5%) | Público premium, Prime, dispostos a pagar por qualidade e prazo |

**Regra de ouro:** Nunca deixar Amazon com preço muito mais alto que ML/Shopee — a Amazon verifica paridade de preço e pode suprimir Buy Box se encontrar preço menor em outro canal.

**Kits como diferenciação:** Criar kits exclusivos por plataforma (Kit ML, Kit Amazon, Kit Shopee) com composições ligeiramente diferentes evita comparação direta de preço entre canais.

---

## 5.4 Onde Investir ADS Primeiro

**Prioridade recomendada:**

### 1º — Mercado Livre (Product Ads)
**Por quê:** ML é líder de mercado BR, maior volume de vendas, produto já com histórico.
- Start: campanha automática para descobrir keywords
- Orçamento mínimo: R$ 30-50/dia por produto principal
- Meta: ROAS ≥ 5x (para cada R$1 gasto, R$5 de retorno)
- Focar em: anúncios que já vendem organicamente — ADS amplifica, não cria demanda

### 2º — Shopee Ads (Search Ads)
**Por quê:** Shopee cresceu 100% em 2024, atingiu R$60bi — audiência enorme e crescente.
- Start: palavras-chave manual (não automático na Shopee pois você paga por clique sem controle)
- ACOS inicial pode ser alto — aceitar para acumular vendas e reviews
- Flash Sale: participar é tão importante quanto os ADS

### 3º — Amazon PPC (Sponsored Products)
**Por quê:** Amazon BR ainda em crescimento, mas CAC (custo por aquisição) tende a ser maior.
- Fundamental se a GB for usar FBA (produto elegível ao Prime)
- Estratégia de flywheel: PPC → BSR sobe → orgânico melhora → reduzir dependência de PPC

---

## 5.5 Quick Wins vs. Long Game

### Quick Wins (resultado em 2-4 semanas):
1. **Entrar no catálogo do ML** com o produto mais vendido e ser competitivo em preço/frete
2. **Ativar Full ML** para os top 3 SKUs (entrega rápida = vantagem imediata no catálogo)
3. **Revisar todos os títulos** com keywords principais no início (mudança simples, impacto rápido)
4. **Participar da próxima Flash Sale Shopee** (visibilidade massiva imediata)
5. **Preencher 100% da ficha técnica** no ML (imediato — mais visibilidade em filtros)
6. **Ativar frete patrocinado Shopee** se elegível
7. **Adicionar vídeo nos listings** Shopee (diferencial imediato vs. concorrentes)

### Long Game (resultado em 2-6 meses):
1. **Construir histórico de reviews** em todas as plataformas (processo lento mas determinante)
2. **Subir para MercadoLíder** (requer volume consistente de vendas)
3. **Conseguir Star Seller Shopee** (requer histórico consistente de excelência)
4. **Criar A+ Content Amazon** e registrar marca no Brand Registry
5. **Estratégia de tráfego externo para Amazon** (Instagram/TikTok → Amazon)
6. **Shopee Live** recorrente para construir base de seguidores da loja
7. **FBA Amazon** se a operação justificar (análise de custo-benefício por SKU)
8. **Kits exclusivos por plataforma** para diferenciação e fuga da guerra de preços

---

## 5.6 Framework de Implementação — Sequência Sugerida

### Mês 1 — Fundação:
- Auditar todos os títulos e fichas técnicas (ML + Shopee + Amazon)
- Verificar elegibilidade para Full ML e ativar nos top SKUs
- Ativar Product Ads ML com campanha automática
- Responder 100% das perguntas abertas nas 3 plataformas
- Criar variações de produto onde não existem

### Mês 2 — Aceleração:
- Entrar no catálogo ML com produtos elegíveis
- Participar de Flash Sale Shopee
- Ativar Shopee Ads (Search Ads) nas 5-10 keywords principais
- Gravar e publicar vídeo nos listings Shopee
- Otimizar campanhas ML com base em dados do mês 1

### Mês 3 — Expansão:
- Criar kits exclusivos por plataforma
- Solicitar Brand Registry Amazon (se ainda não tiver)
- Criar A+ Content Amazon para top SKUs
- Planejar primeira Shopee Live
- Ativar Amazon Sponsored Products para top SKUs
- Analisar viabilidade de FBA por SKU

### Mês 4-6 — Consolidação:
- Construir estratégia de reviews nas 3 plataformas
- Otimizar precificação cruzada
- Estratégia de conteúdo externo para Amazon (Instagram/blog)
- Monitorar BSR Amazon e ajustar PPC conforme ranking

---

## 5.7 KPIs para Monitorar (por Plataforma)

### Mercado Livre:
- Posição no catálogo (ganhando/perdendo)
- Taxa de conversão por anúncio
- ROAS das campanhas Product Ads
- Reputação (manter verde escuro)
- Posição nos resultados de busca (top 3 keywords)
- Visitas/mês por anúncio

### Shopee:
- Pontos de penalidade (manter em 0)
- Rating médio da loja (manter > 4.8)
- Taxa de resposta no chat (manter 100%)
- Taxa de envio no prazo (manter > 95%)
- ACOS dos Shopee Ads
- Classificação média (posição nos anúncios pagos)

### Amazon:
- BSR (Best Seller Rank) por categoria
- Unit Session Percentage (conversão = vendas/sessões)
- Total de reviews e média de estrelas
- Buy Box %
- ACOS do Sponsored Products
- Impressions orgânicas vs. pagas

---

*Pesquisa compilada em março de 2026 por Kobe para a GB Importadora (Budamix).*
*Fontes: documentação oficial ML (vendedores.mercadolivre.com.br), Shopee Seller Education, Seller Labs, AMZ Advisers, Nubimetrics, Arcos Scale, Bling Blog, Estudo Lett/Neogrid (out/2024-mar/2025), GoSmarter, e-Commerce Brasil.*

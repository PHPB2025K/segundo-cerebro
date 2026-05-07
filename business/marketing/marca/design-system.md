---
title: "Design System — Budamix v2.1"
created: 2026-04-29
modified: 2026-05-07
type: reference
domain: marketing
status: active
version: "v2.1"
tags:
  - business/marketing
  - marca
  - budamix
  - design-system
  - identidade-visual
  - branding
aliases:
  - Budamix Design System
  - Design System Budamix
  - BUDAMIX — DESIGN SYSTEM
---

# BUDAMIX — DESIGN SYSTEM

> **Versão:** v2.1 · Floresta com Faísca · DNA Editorial Playful Lapidado (07/05/2026)
> **Marca:** Budamix · GB Importadora
> **Site:** https://budamix.com.br
> **Mudança vs v2.0:** elementos do DNA visual lapidados com base em 6 referências reais de stories. Saíram elementos teóricos pouco recorrentes (selection markers, pixel pattern de quadrados, círculo cortado), entraram 8 elementos observados nas referências e validados como recorrentes (frame externo, pílula headline, hatch pattern, pontos em coluna, matriz de pontos, chevrons, asterisco, quadrados arredondados decorativos).
> **Mudança vs v1.2:** paleta refeita ("Floresta com Faísca"), stack tipográfica simplificada de 4 pra 3 fontes, logo atualizado, **DNA visual editorial playful** sistematizado.

---

## SUMÁRIO

1. [Sobre a marca](#1-sobre-a-marca)
2. [Personalidade visual](#2-personalidade-visual)
3. [Descrição da paleta](#3-descrição-da-paleta)
4. [Paleta de cores — Floresta com Faísca](#4-paleta-de-cores--floresta-com-faísca)
5. [Tipografia](#5-tipografia)
6. [DNA visual editorial playful](#6-dna-visual-editorial-playful)
7. [Spacing scale](#7-spacing-scale)
8. [Shadow scale](#8-shadow-scale)
9. [Border radius](#9-border-radius)
10. [Componentes — Button](#10-componentes--button)
11. [Componentes — Badge](#11-componentes--badge)
12. [Componentes — Pill (chip)](#12-componentes--pill-chip)
13. [Logotipo](#13-logotipo)
14. [Botão CTA — banners de marketing](#14-botão-cta--banners-de-marketing)
15. [Templates de carrossel Instagram](#15-templates-de-carrossel-instagram)
16. [Tratamento de fotos](#16-tratamento-de-fotos)
17. [Cores por marketplace](#17-cores-por-marketplace)
18. [Histórico de versões](#18-histórico-de-versões)
19. [Fontes](#19-fontes)

---

## 1. SOBRE A MARCA

**Budamix** é a marca registrada (INPI) da **GB Importadora** — empresa familiar de utensílios domésticos premium.

| Dado | Valor |
|------|-------|
| Categoria de produto | Utensílios domésticos: vidro, cerâmica, porcelana, MDF |
| Sourcing principal | Yiwu, China (importação direta) |
| Carro-chefe | Potes herméticos de vidro |
| Canais | Mercado Livre, Amazon, Shopee, e-commerce próprio (budamix.com.br) |
| Público | Mulheres e homens adultos que valorizam organização, bem-estar e qualidade de vida em casa |
| Posicionamento | Premium acessível — qualidade real sem cara de luxo inacessível |

---

## 2. PERSONALIDADE VISUAL

| Atributo | Descrição |
|----------|-----------|
| **Tom** | Sofisticado, confiável, doméstico, premium sem ser inacessível |
| **Estilo** | Editorial playful — limpo e elegante mas com personalidade visual ousada. Mistura calor humano com gestos gráficos. Nunca genérico, nunca poluído |
| **Atmosfera** | Casa brasileira contemporânea, lived-in mas curado. Pinterest-meets-magazine-zine |
| **Luz** | Natural, quente, suave nas fotos — gestos visuais coloridos como contraponto |
| **Materialidade** | Madeira clara, vidro, pedra, linho, cerâmica fosca + elementos vetoriais coloridos sobrepostos |
| **Personalidade da paleta** | Organizada sem rigidez, premium sem frieza, calorosa sem informalidade — universo de casa real, não de vitrine |
| **Atitude visual** | Não tem medo de ser ousada: pílulas que sobrepõem palavras, setas hero gigantes, italic dramático em acentos, círculos cortados nos cantos |

---

## 3. DESCRIÇÃO DA PALETA

> **Texto canônico — usar em apresentações, manual de marca, briefings de fornecedor.**

A paleta Budamix combina verdes profundos que transmitem solidez e calma, com Lima Sutil entrando como faísca moderna em palavras-chave e Burnt Terracotta reservada exclusivamente para botões de ação. Sobre uma base de tons quentes (Linen e Ivory Mist) que substituem o branco puro, o conjunto comunica organização sem rigidez, presença premium sem frieza, e calor humano sem informalidade — refletindo o universo da casa real, não da vitrine.

---

## 4. PALETA DE CORES — FLORESTA COM FAÍSCA

> Fonte canônica: `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/index.css`
> Mapeada em `tailwind.config.ts` via `hsl(var(--*))`.

### 4.1 Cores principais

| Token brand | Nome | Hex | HSL | CSS var | Tailwind | Função |
|-------------|------|-----|-----|---------|----------|--------|
| **Deep Teal** | Primary · Âncora | `#004D4D` | `180 100% 15%` | `--primary` | `bg-primary` | Cor âncora. Headlines, fundos premium, links principais, focus rings, ações primárias |
| **Forest Night** | Foreground · Texto | `#1B3A2D` | `144 38% 17%` | `--foreground` | `text-foreground` | Texto longo, fundos noturnos, body geral |
| **Fern Green** | Secondary · Apoio | `#4A7C59` | `137 25% 39%` | `--secondary` | `bg-secondary` | Eyebrow, badges de apoio, divisores, ícones secundários, traço horizontal antes do eyebrow |
| **Lima Sutil** | Destaque · Acento gráfico | `#B8D043` | `71 60% 54%` | `--lime` | `bg-lime` | Palavra-chave em headlines, KPIs, **setas hero**, **círculos cortados**, **pílulas inline**, **selection markers**, ícones gráficos centrais |
| **Burnt Terracotta** | Accent · CTA | `#C1553D` | `11 53% 50%` | `--accent` | `bg-accent` | **CTA exclusivo** + numeração de página em pílula + italic acento de palavra-chave |
| **Linen** | Suave · Cards | `#E8DFD4` | `32 32% 87%` | `--linen` | `bg-linen` | Fundo de cards, slides de fechamento, faixas de prova social, badges de marca |
| **Ivory Mist** | Background · Base | `#FAF7F2` | `36 36% 97%` | `--background` | `bg-background` | Fundo geral. Quote bubbles. Logo sobre fundo escuro |

### 4.2 Cores de superfície e suporte

| Token | Hex | HSL | CSS var | Uso |
|-------|-----|-----|---------|-----|
| Card | `#FFFFFF` | `0 0% 100%` | `--card` | Cards, modais, popovers (raro — preferir Linen/Ivory Mist) |
| Muted | `#EDE8E0` | `38 26% 90%` | `--muted` | Fundos sutis, disabled, skeleton loading |
| Muted foreground | — | `144 12% 35%` | `--muted-foreground` | Texto secundário sobre fundo claro, placeholders |
| Border | `#D6CFC2` | `38 18% 80%` | `--border` | Bordas padrão de cards, inputs, divisores |
| Border subtle | `#E5DED2` | `38 22% 86%` | `--border-subtle` | Bordas sutis (cards leves, inputs em descanso) |
| Ring | `#004D4D` | `180 100% 15%` | `--ring` | Focus ring (= primary) |
| Destructive | — | `0 72% 51%` | `--destructive` | Erros, exclusões, alerta crítico |
| Success | `#4A7C59` | `137 25% 39%` | `--success` | Confirmações, validação (= Fern Green) |

### 4.3 Hierarquia de uso (3 níveis)

**Nível 1 — Estruturais (alta frequência, uso livre)**
Deep Teal, Forest Night, Linen, Ivory Mist. Bases de qualquer peça, aparecem em todos contextos.

**Nível 2 — Suporte (uso médio, com regra de função)**
Fern Green sempre como apoio de hierarquia menor (eyebrows, divisores, ícones). Lima Sutil sempre como **destaque ou elemento gráfico decorativo** (palavra-chave, setas, círculos, ícones).

**Nível 3 — Acento (uso restrito, máxima atenção)**
Burnt Terracotta exclusivamente em CTA + pílula de numeração de página + italic de palavra-acento. Nunca em texto longo, nunca em fundo grande.

### 4.4 Regras de ouro

1. **Deep Teal é cor âncora** — aparece em quase toda peça (headlines, fundos premium, marca presente).
2. **Lima Sutil é faísca, não tinta** — usar em palavra única, número KPI, ícone decorativo, seta hero, círculo cortado, pílula inline. Nunca como fundo grande, nunca em parágrafo.
3. **Burnt Terracotta é CTA + assinatura de página** — botão de conversão, pílula `PAGE 01`, italic acento. Se aparecer em texto longo ou fundo, perde força.
4. **Lima Sutil + Fern Green não convivem perto** — os dois são tons de verde-amarelado e brigam visualmente. Se Lima aparece numa palavra de headline, Fern Green não deve aparecer no eyebrow da mesma peça (use Forest Night ou Deep Teal).
5. **Hierarquia obrigatória entre Deep Teal, Lima e Terracotta** — nunca usar as três com peso visual igual numa mesma composição. Uma manda, outra apoia, outra é detalhe.
6. **No feed Instagram, intercalar 1 fundo escuro a cada 3-4 posts** (Deep Teal ou Forest Night) pra criar ritmo visual.

### 4.5 Combinações testadas

| Fundo | Headline | Acento | Eyebrow | CTA | Decoração |
|-------|----------|--------|---------|-----|-----------|
| Ivory Mist | Deep Teal | Lima Sutil | Fern Green | Burnt Terracotta | Lima Sutil |
| Linen | Deep Teal | Lima Sutil | Fern Green | Burnt Terracotta | Lima Sutil |
| Deep Teal | Ivory Mist | Lima Sutil | Lima Sutil | Burnt Terracotta | Lima Sutil |
| Forest Night | Ivory Mist | Lima Sutil | Lima Sutil | Burnt Terracotta | Lima Sutil |

---

## 5. TIPOGRAFIA

> **3 fontes apenas.** Stack simplificada de 4 pra 3 na v2.0 (DM Sans removida — redundante com Plus Jakarta Sans).

### 5.1 Stack canônica

| Camada | Fonte | Variável Tailwind | Pesos | Função |
|--------|-------|-------------------|-------|--------|
| **Display** | **Bricolage Grotesque Variable** | `font-display` / `font-heading` | 700 / 800 | H1, H2, hero, capa de carrossel, números KPI grandes, palavras em pílula inline |
| **Body / UI** | **Plus Jakarta Sans Variable** | `font-body` / `font-sans` | 400 / 500 / 600 / 700 | H3 a H6, parágrafos, labels, eyebrows, badges, CTA, navegação. **Italic 700** pra acentos editoriais |
| **Mono** | **JetBrains Mono Variable** | `font-mono` | 400 / 500 / 700 | Preços, SKUs, códigos, especificações técnicas, URLs, labels de foto |

**Imports obrigatórios** (Google Fonts ou Fontsource via CDN):

```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700&family=JetBrains+Mono:wght@400;500;700&display=swap');
```

### 5.2 Quando usar cada uma

**Bricolage Grotesque** — exclusiva pra impacto visual. Headlines de peça-mãe (capa de carrossel, hero do site, banner promocional), nome do produto em embalagem, números grandes em estatísticas, palavras dentro de pílulas inline. **Sempre uppercase ou capitalize.** Letter-spacing levemente negativo (`-0.5px` a `-1px`) pra compactar e dar peso editorial. Usada para **gestos visuais grandes**.

**Plus Jakarta Sans** — voz textual única da marca. Tudo que não é display ou número técnico passa por aqui: subtítulos, parágrafos, labels de UI, navegação, eyebrows, badges, texto de botões, captions, quote bubbles. Usa peso 400 pra body, 500 pra labels, 600 pra eyebrows e CTAs, 700 pra subtítulos e **italic 700 pra acentos editoriais** (palavra dentro de headline em outra cor).

**JetBrains Mono** — números técnicos com cara de "dado". Preços em produto, SKUs, códigos de pedido, especificações (volume, medidas, peso), URLs em mockups, labels descritivas de foto (ex: "FOTO P&B · COZINHA REAL"), datas em mono pra dar sensação de timestamp.

### 5.3 Mistura tipográfica editorial — regra crítica

A v2.0 introduz **mistura tipográfica deliberada** dentro da mesma frase pra criar contraste visual editorial. Regra:

```
[Bricolage uppercase] + [Plus Jakarta italic] + [Bricolage uppercase]
"Por que isso *importa* na sua despensa"
   bricolage   italic Jakarta   bricolage
```

A palavra italic SEMPRE em **Plus Jakarta Sans 700 italic** + **Burnt Terracotta** + **font-style: italic** + texto-case normal (sem uppercase). Funciona como acento editorial e dá ritmo ao headline monolítico.

Não usar mais que 1 palavra italic por headline. Não usar italic em parágrafos longos.

### 5.4 Type scale (e-commerce)

| Token | Size | Uso |
|-------|------|-----|
| `text-xs` | 12px | Labels, tags, micro-disclaimers |
| `text-sm` | 14px | Body small, captions, eyebrow |
| `text-base` | 16px | Body padrão |
| `text-lg` | 18px | Lead, intro de seção |
| `text-xl` | 20px | H4 |
| `text-2xl` | 24px | H3, preços em destaque |
| `text-3xl` | 30px | H2 |
| `text-4xl` | 36px | H1 mobile |
| `text-5xl` | 48px | H1 desktop |
| `text-6xl` | 60px | Hero title |
| `text-7xl` | 72px | Números KPI gigantes |
| `text-8xl` | 96px | Números monumentais (capa de carrossel "5 ERROS") |

### 5.5 Tamanhos em banners e carrosséis

| Elemento | Fonte | Peso | Tamanho |
|----------|-------|------|---------|
| Headline capa | Bricolage Grotesque | 800 | 28–48px (escala conforme peça) |
| Headline slide interno | Bricolage Grotesque | 700/800 | 18–28px |
| Subtítulos / leads | Plus Jakarta Sans | 600/700 | 14–18px |
| Eyebrow | Plus Jakarta Sans | 500/600 | 8–12px (uppercase, letter-spacing 1.4–1.6px) |
| Body / parágrafo | Plus Jakarta Sans | 400 | 9–13px |
| Italic acento | Plus Jakarta Sans | 700 italic | igual ao tamanho do headline em volta |
| Logo na peça | Bricolage Grotesque | 800 | 11–18px (varia) |
| Números KPI gigantes | Bricolage Grotesque | 800 | 60–130px |
| Texto botão CTA | Plus Jakarta Sans | 600/700 | 9–14px (uppercase, letter-spacing 1.0–1.2px) |
| Pílula inline (palavra dentro de headline) | Bricolage Grotesque | 800 | mesmo do headline |
| Pílula numeração de página | Plus Jakarta Sans | 600 | 9px (uppercase) |
| Badge / chip | Plus Jakarta Sans | 600/700 | 8–11px |
| Preços | JetBrains Mono | 500/700 | 13–24px |
| Specs técnicas | JetBrains Mono | 400/500 | 7–11px |
| Quote text (em quote bubble) | Plus Jakarta Sans | 500 | 9–12px |
| Quote attribution | Bricolage Grotesque | 800 | 10–12px |
| URL / link em mono | JetBrains Mono | 400 | 8–10px |

### 5.6 Hierarquia de cor em texto

| Onde | Cor padrão | Sobre fundo escuro |
|------|------------|--------------------|
| Headline | Deep Teal `#004D4D` | Ivory Mist `#FAF7F2` |
| Palavra de destaque (Bricolage) | Lima Sutil `#B8D043` | Lima Sutil (igual) |
| Italic acento (Plus Jakarta) | Burnt Terracotta `#C1553D` | Lima Sutil (substitui pra contrastar) |
| Body | Forest Night `#1B3A2D` (opacidade 0.75–0.85) | Linen `#E8DFD4` (sem opacidade) |
| Eyebrow | Fern Green `#4A7C59` | Lima Sutil `#B8D043` |
| Caption / disclaimer | Forest Night opacidade 0.55–0.65 | Linen opacidade 0.75 |
| Logo `budamix°` | Forest Night | Ivory Mist |
| Logo — `°` (grau) | Lima Sutil sempre | Lima Sutil sempre |

---

## 6. DNA VISUAL EDITORIAL PLAYFUL

> **Sistema de elementos gráficos recorrentes** que constroem a identidade visual da Budamix. Lapidado a partir de 6 referências reais de stories de Instagram, validados como elementos efetivamente usados. Combiná-los corretamente gera coerência visual em qualquer canal.

> **14 elementos no total**, divididos em **3 categorias**:
> - **Estruturais** (3): frame externo, pílula headline, pílula numeração — aparecem em quase todo slide
> - **Decorativos** (8): hatch pattern, pontos em coluna, matriz de pontos, chevrons, asterisco, quadrados arredondados, setas hero, pílula inline — usados em rotação
> - **Especiais** (3): italic acento, quote bubble, pílula CTA — usados em momentos específicos

### 6.1 ESTRUTURAIS — uso em quase todo slide

#### 6.1.1 Elemento 1 — Frame externo + card interno

**O quê:** estrutura de página padrão Budamix. Margem colorida externa (Forest Night, Burnt Terracotta ou Deep Teal) + card cream interno (Ivory Mist ou Linen) com cantos arredondados, ocupando a maior parte do espaço.

**Quando usar:** **estrutura base** de todo story Instagram, post único e maioria dos slides de carrossel. É o layout fundamental da Budamix.

**Como aplicar:**
- Margem externa: 14–20px de espessura em todas as bordas
- Cor da margem: Forest Night `#1B3A2D` (padrão) · Burnt Terracotta `#C1553D` (alerta/urgência) · Deep Teal `#004D4D` (premium)
- Card interno: Ivory Mist `#FAF7F2` ou Linen `#E8DFD4`
- Border-radius do card: 12–18px (rounded-xl a rounded-2xl)
- Padding interno do card: 18–24px

**Variações:**
- Frame Forest Night + card Ivory Mist → padrão neutro premium
- Frame Burnt Terracotta + card Ivory Mist → alerta, urgência, novidade
- Frame Deep Teal + card Linen → conteúdo "premium silencioso"
- Frame Lima Sutil + card Ivory Mist → conteúdo "viral/trending" (uso raro)

#### 6.1.2 Elemento 2 — Pílula headline

**O quê:** bloco de cor escura com headline em uppercase, formato pílula com **canto cortado em curva** num dos lados. Não é retângulo nem círculo — é uma forma orgânica única que vira assinatura visual da Budamix.

**Quando usar:** **título principal** de stories, posts únicos e capas de carrossel. Substitui o headline-direto-no-fundo do v2.0.

**Como aplicar:**
- Background: Forest Night `#1B3A2D` (padrão) · Deep Teal `#004D4D` · Lima Sutil `#B8D043` (com texto Forest Night)
- Texto: Ivory Mist `#FAF7F2` (sobre fundos escuros) ou Forest Night (sobre Lima Sutil)
- Fonte: Bricolage Grotesque 800, 22–34px, uppercase
- Border-radius: assimétrico — 1 canto reto + 3 cantos arredondados (16–20px)
- O canto reto é o que se conecta visualmente ao próximo elemento da composição
- Padding: 10–16px vertical, 16–22px horizontal
- Pode ter "rabicho" curvado se conectando ao card de fundo (ver refs de stories)

#### 6.1.3 Elemento 3 — Pílula de numeração de página

**O quê:** pílula pequena em Burnt Terracotta posicionada no canto inferior direito de cada slide de carrossel, com texto `PAGE 01`, `PAGE 02` etc.

**Quando usar:** **obrigatório** em todo slide de carrossel Instagram. Não usar em post único nem story.

**Como aplicar:**
- Background: Burnt Terracotta `#C1553D`
- Texto: Ivory Mist `#FAF7F2`, Plus Jakarta Sans 600/700
- Tamanho: 9px, uppercase, letter-spacing 1.2px
- Padding: 4px 11px
- Border-radius: 999px (pílula completa)
- Posição: `bottom: 12px; right: 12px`
- Numeração: `PAGE 01`, `PAGE 02`... (não usar `01/06`, não usar `1`)

### 6.2 DECORATIVOS — usados em rotação

#### 6.2.1 Elemento 4 — Hatch pattern (listras diagonais)

**O quê:** quadrado preenchido com listras diagonais paralelas. Vira "assinatura geométrica" recorrente nos cantos dos cards.

**Quando usar:** decoração de canto. Aparece em 30–50% dos slides como elemento de detalhe. Posicionado em cantos opostos ao texto principal pra não competir.

**Como aplicar:**
- CSS: `background-image: repeating-linear-gradient(45deg, [cor] 0px, [cor] 3px, transparent 3px, transparent 7px);`
- Cor das listras: Forest Night `#1B3A2D` (sobre fundo claro) ou Lima Sutil `#B8D043` (sobre fundo escuro)
- Tamanho: 30–50px quadrado
- Posição: cantos do card interno (não do frame externo)
- Pode aparecer 1–2 vezes em cantos opostos
- Inclinação fixa em 45° (não variar)

#### 6.2.2 Elemento 5 — Pontos em coluna vertical

**O quê:** 3 (ou 4) círculos pequenos alinhados verticalmente, com espaçamento generoso entre eles.

**Quando usar:** decoração lateral (esquerda ou direita) do card. Aparece em ~40% dos slides como detalhe rítmico.

**Como aplicar:**
- Quantidade: 3 ou 4 círculos
- Cor: Lima Sutil `#B8D043` (padrão) · Ivory Mist (sobre fundos escuros)
- Tamanho de cada círculo: 5–8px de diâmetro
- Espaçamento entre círculos: 10–15px (gap generoso)
- Posição: 12–16px da borda lateral do card, a meia altura ou colado na borda superior
- Pode ter 2 grupos de 3 pontos em laterais opostas (raro)

#### 6.2.3 Elemento 6 — Matriz de pontos

**O quê:** grid denso de círculos pequenos (4×3 ou 5×4) ocupando uma área quadrada ou retangular. Substitui o "pixel pattern" de quadrados da v2.0.

**Quando usar:** decoração intermediária — área lateral próxima ao texto principal, sem dominar. Vira "ruído visual organizado" que adiciona personalidade.

**Como aplicar:**
- Grid: `display: grid; grid-template-columns: repeat(4, 5px); gap: 5px;` (variação de 4×3 a 5×4)
- Cada ponto: 4–6px de diâmetro, círculo perfeito
- Cor: Lima Sutil `#B8D043`
- Posição: lateral do card, próxima a algum elemento de texto sem sobreposição
- Aparecer 1 vez por slide (não usar 2 matrizes no mesmo slide)

#### 6.2.4 Elemento 7 — Chevrons em fileira

**O quê:** sequência de 3–4 chevrons (`>>>` ou `<<<`) flanqueando lateralmente um headline ou subtítulo, criando moldura visual lateral.

**Quando usar:** ao redor de headline de destaque ou label de seção (ex: `>>> TRENDING <<<`). Adiciona dinâmica e direcionalidade.

**Como aplicar:**
- Quantidade: 3–4 chevrons em cada lado (lado esquerdo: `>>>` apontando pra direita; lado direito: `<<<` apontando pra esquerda — apontam pro centro)
- Fonte: Bricolage Grotesque 800
- Cor: Lima Sutil `#B8D043`
- Tamanho: 14–22px
- Letter-spacing entre chevrons: -2px a -4px (mais apertado pra criar "fileira contínua")
- Espaçamento até o texto central: 8–12px

#### 6.2.5 Elemento 8 — Asterisco estilizado

**O quê:** símbolo de 6 ou 8 pontas em Lima Sutil, decorativo solto. Estilo "estrela editorial".

**Quando usar:** decoração solta em áreas vazias do slide, junto de outros elementos como cloud/forma orgânica. Aparece em 20–30% dos slides como detalhe pontual.

**Como aplicar:**
- Forma: 4 linhas atravessadas no centro (cruz + X) criando 8 pontas, OU 6 linhas radiais
- Cor: Lima Sutil `#B8D043`
- Tamanho: 20–40px
- Posição: solto em área vazia, raramente colado em borda
- Pode aparecer 1–2 vezes próximos um do outro (par)
- Espessura das linhas: 2–3px

#### 6.2.6 Elemento 9 — Quadrados arredondados decorativos

**O quê:** 2 ou 3 quadrados com cantos arredondados sobrepostos parcialmente, formando uma "constelação" geométrica em canto do slide.

**Quando usar:** decoração de canto em slides mais "limpos" que precisam de contraponto visual. Substitui o círculo cortado da v2.0.

**Como aplicar:**
- Quantidade: 2 ou 3 quadrados
- Cor: misturar Lima Sutil + Linen + Burnt Terracotta (3 cores distintas pra criar contraste interno)
- Tamanho de cada quadrado: 18–28px
- Border-radius: 6–8px
- Sobreposição: cada quadrado sobrepõe o anterior em ~30%
- Posição: canto inferior do card (esquerdo ou direito), parcialmente cortado pela borda

#### 6.2.7 Elemento 10 — Setas hero

**O quê:** seta `↘` ou `→` em escala gigante (50–100px), em Forest Night ou Lima Sutil, ocupando porção significativa do slide. **Elemento hero, não decoração.**

**Quando usar:** em slides de capa ou transição forte. Máximo 1 seta hero principal por slide (pode ter 1 seta secundária menor com opacidade reduzida pra criar efeito de "rastro").

**Como aplicar:**
- Fonte: Bricolage Grotesque 800
- Cor: Forest Night `#1B3A2D` (sobre fundos claros) · Lima Sutil `#B8D043` (sobre fundos escuros)
- Tamanho: 50–100px
- Rotação: 0° a 25°
- Posição: deslocada pra borda do slide
- Pode ter seta secundária 60% do tamanho com opacidade 0.5

#### 6.2.8 Elemento 11 — Pílula inline (palavra dentro de headline)

**O quê:** uma palavra do headline aparece dentro de pílula colorida sobreposta ao texto, criando destaque editorial.

**Quando usar:** em headlines de capa, CTA ou momentos de máxima ênfase. Máximo 1 pílula inline por slide.

**Como aplicar:**
- Background: Lima Sutil `#B8D043` (padrão) ou Deep Teal `#004D4D`
- Cor do texto: Deep Teal sobre Lima OU Ivory Mist sobre Teal
- Fonte: Bricolage Grotesque 800, mesmo tamanho do headline ao redor
- Padding: 0–4px vertical, 10–14px horizontal
- Border-radius: 999px

### 6.3 ESPECIAIS — uso em momentos específicos

#### 6.3.1 Elemento 12 — Italic acento

**O quê:** uma palavra em **Plus Jakarta Sans 700 italic + Burnt Terracotta + case normal** dentro de um headline em Bricolage uppercase.

**Quando usar:** em headlines de slides internos pra criar contraste tipográfico. Limite: 1 palavra italic por headline.

**Como aplicar:**
- Fonte: Plus Jakarta Sans 700 italic
- Cor: Burnt Terracotta `#C1553D` (em fundo claro) · Lima Sutil `#B8D043` (em fundo escuro)
- Case: normal (sem uppercase)
- Tamanho: igual ao do headline circundante
- Letter-spacing: -0.2px a -0.3px

#### 6.3.2 Elemento 13 — Quote bubble (em fotos de depoimento)

**O quê:** balão de fala em Ivory Mist sobre foto colorida, contendo depoimento curto.

**Quando usar:** em slides de prova social / depoimento. Sempre sobre uma foto da pessoa.

**Como aplicar:**
- Background: Ivory Mist `#FAF7F2`
- Border-radius: 6px
- Padding: 9px 11px
- Box-shadow leve: `0 3px 10px rgba(0,0,0,0.12)`
- Largura máx: 130–160px
- 3 pontinhos Lima Sutil no topo (simulando "menu de chat")
- Texto: Plus Jakarta Sans 500, 9–11px, Forest Night
- Palavra-chave dentro do quote em italic Burnt Terracotta

#### 6.3.3 Elemento 14 — Pílula CTA "Saiba mais"

**O quê:** botão em formato pílula com texto curto de ação. Variação do botão CTA mas em escala menor, dentro do card.

**Quando usar:** em stories e cards de informação que precisam de CTA secundário (não o CTA principal de conversão).

**Como aplicar:**
- Background: Burnt Terracotta `#C1553D` (CTA forte) ou Forest Night `#1B3A2D` (CTA neutro)
- Texto: Ivory Mist, Plus Jakarta Sans 600
- Tamanho: 11–13px
- Padding: 7–10px vertical, 16–22px horizontal
- Border-radius: 999px
- Copy curta: `Saiba mais`, `Read more`, `Quero ver`, `Ver mais`

### 6.4 Combinação de elementos — regra de saturação

**Não combinar mais que 5 elementos DNA num mesmo slide.** Saturação visual prejudica leitura.

| Tipo de slide | Elementos recomendados | Total |
|---------------|------------------------|-------|
| Story informativo | Frame externo + Pílula headline + Hatch pattern + Pontos em coluna + Pílula CTA | 5 |
| Story alerta (Weather/Breaking) | Frame Burnt Terracotta + Pílula headline + Hatch + Pontos coluna + Pílula CTA | 5 |
| Capa de carrossel | Frame externo + Pílula headline + Setas hero + Matriz de pontos + Pílula numeração | 5 |
| Slide interno carrossel (lista) | Frame externo + Italic acento + Pontos em coluna + Pílula numeração | 4 |
| Slide depoimento | Frame externo + Quote bubble + Quadrados arredondados + Pílula numeração | 4 |
| Slide CTA carrossel | Frame externo + Pílula inline + Quadrados arredondados + Pílula CTA + Pílula numeração | 5 |
| Story trending/viral | Frame externo + Pílula headline + Chevrons fileira + Asterisco + Pílula CTA | 5 |

---

## 7. SPACING SCALE

| Token | Value | Uso |
|-------|-------|-----|
| `space-1` | 4px | Micro gaps |
| `space-2` | 8px | Icon-label gap |
| `space-4` | 16px | Padding interno cards |
| `space-6` | 24px | Card padding |
| `space-8` | 32px | Section sub-gaps |
| `space-12` | 48px | Section gap mobile |
| `space-16` | 64px | Section padding mobile |
| `space-24` | 96px | Section padding desktop |

### Section spacing utility

```css
.section-budamix {
  padding-top: 4rem;
  padding-bottom: 4rem;
}
@media (min-width: 768px) {
  .section-budamix {
    padding-top: 6rem;
    padding-bottom: 6rem;
  }
}
```

---

## 8. SHADOW SCALE

| Token | Uso |
|-------|-----|
| `shadow-budamix-sm` | Cards em repouso, inputs |
| `shadow-budamix-md` | Cards em hover, dropdowns, quote bubbles |
| `shadow-budamix-lg` | Modais, sidebars, elementos flutuantes |

> Todos os shadows usam `hsl(var(--foreground))` (= Forest Night) com opacidade baixa pra integrar com fundos claros e escuros.

---

## 9. BORDER RADIUS

| Token | Value | Computed |
|-------|-------|----------|
| `--radius` | `0.5rem` | 8px (base) |
| `rounded-sm` | `calc(var(--radius) - 4px)` | 4px |
| `rounded-md` | `calc(var(--radius) - 2px)` | 6px |
| `rounded-lg` | `var(--radius)` | 8px |
| `rounded-xl` | — | 12px |
| `rounded-2xl` | — | 16px |
| `rounded-3xl` | — | 24px |
| `rounded-full` | — | 9999px (pills, avatars, CTAs banner, numeração de página) |

---

## 10. COMPONENTES — BUTTON

| Variant | Background | Foreground | Use case |
|---------|------------|------------|----------|
| `default` | `--primary` (Deep Teal) | Ivory Mist | CTA principal de UI (e-commerce, dashboards) |
| `accent` | `--accent` (Burnt Terracotta) | Ivory Mist | CTA de banners marketing e ações de conversão final |
| `secondary` | Linen | Forest Night | Ação secundária |
| `outline` | transparent + border Forest Night | Forest Night | Ação terciária |
| `ghost` | transparent | Forest Night | Nav, ações discretas, ícones de sidebar |
| `link` | transparent | Deep Teal | Links inline em texto longo |
| `lime` | Lima Sutil | Deep Teal (não Forest Night, pra contraste melhor) | Reservado pra ações especiais (raro — testar antes de usar) |

### Hierarquia de uso

1. **`accent` (Burnt Terracotta)** é o CTA de maior peso — usado em conversão final (comprar, finalizar pedido, salvar).
2. **`default` (Deep Teal)** é CTA primário de UI — ações dentro do app/dashboard que não são conversão final.
3. **`secondary` (Linen)** e **`outline`** são ações neutras de suporte.
4. **`ghost`** e **`link`** são quase invisíveis — pra navegação e ações discretas.

### Estilo do botão CTA banners (especial)

- Fonte: Plus Jakarta Sans 600/700, uppercase
- Letter-spacing: 1.0–1.2px
- Border-radius: 999px (pílula completa)
- Padding: 7–11px vertical, 14–22px horizontal
- Background: Burnt Terracotta `#C1553D`
- Texto: Ivory Mist `#FAF7F2`
- Ícone seta `→` à direita (espaço de 4–6px do texto)
- Sem sombra (a v2.0 abandona sombra suave do v1.2 pra estilo mais flat)

---

## 11. COMPONENTES — BADGE

| Variant | Background | Foreground | Use case |
|---------|------------|------------|----------|
| `default` | Linen | Forest Night | Status geral, categoria neutra |
| `secondary` | Fern Green | Ivory Mist | Tag de apoio |
| `accent` | Burnt Terracotta | Ivory Mist | Promoção, sale, "novo" |
| `lime` | Lima Sutil | Deep Teal | Premium, bestseller, rating, destaque |
| `outline` | transparent + border Fern Green | Fern Green | Tag discreta |
| `dark` | Deep Teal | Ivory Mist | Status sobre fundo claro |

### Diferença pra Pill (chip)

- **Badge:** indica status/categoria estática (não-clicável, geralmente). Pode ser quadrado ou com radius médio.
- **Pill:** sempre `rounded-full`. Pode ser clicável (filtro) ou estática (numeração de página, tag editorial). Geralmente maior padding horizontal que badge.

---

## 12. COMPONENTES — PILL (CHIP)

> **Nova categoria de componente na v2.0.** Pílulas são parte central do DNA editorial playful e merecem documentação dedicada.

### 12.1 Tipos de pílula

| Tipo | Uso | Background | Foreground | Tamanho |
|------|-----|------------|------------|---------|
| `pill-page` | Numeração de página em carrossel | Burnt Terracotta | Ivory Mist | 9px texto, 4px 11px padding |
| `pill-inline` | Palavra destacada dentro de headline | Lima Sutil | Deep Teal | igual ao headline em volta |
| `pill-soft` | "como uma" / "em" / textos de transição | Linen | Forest Night | 11px texto, 4px 10px padding |
| `pill-strong` | Palavra-conceito em destaque | Lima Sutil | Deep Teal | 12–14px Bricolage 800, 5px 13px padding |
| `pill-brand` | Badge de marca (ex: "DESPENSA", "DEFINA") | Linen ou Lima ou Deep Teal | varia conforme bg | 8px texto, 3px 8px padding |
| `pill-cta` | CTA em formato pílula | Burnt Terracotta | Ivory Mist | 9–11px texto, 7–14px padding |

### 12.2 Regras

- Border-radius: sempre 999px (pílula completa)
- Padding horizontal nunca menor que 8px (pílulas finas demais perdem identidade)
- Texto sempre em Plus Jakarta Sans 600/700 (ou Bricolage 800 em pílulas inline e strong)
- Letter-spacing: 0.4–1.4px em pílulas com texto uppercase
- Não combinar mais que 3 pílulas no mesmo slide (saturação visual)

---

## 13. LOGOTIPO

### 13.1 Logotipo principal (v2.0)

**Nome:** `budamix°`

- Caixa: minúscula (`budamix`) seguida do símbolo `°` (grau)
- Fonte: **Bricolage Grotesque 800**
- Letter-spacing: -0.3px a -0.5px (mais apertado)
- **Cor de `budamix`:** Forest Night `#1B3A2D` em fundo claro · Ivory Mist `#FAF7F2` em fundo escuro
- **Cor do `°` (grau):** Lima Sutil `#B8D043` sempre (em qualquer fundo) — assinatura visual da marca

### 13.2 Mudança vs v1.2

- v1.2: `BUDAMIX` (caixa alta) com "BUDA" branco + "MIX" dourado
- v2.0: `budamix°` (minúscula) com `°` em Lima Sutil

**Por que mudou:**
- Caixa baixa comunica acessibilidade contemporânea (vs caixa alta institucional)
- O `°` (grau) substitui o split de cor "BUDA + MIX" — virou assinatura visual mais sutil e memorável
- Lima Sutil no `°` reforça a faísca como marca, em vez do dourado

### 13.3 Aplicação

- **Posicionamento:** sempre canto superior esquerdo de qualquer peça (slide, banner, hero, embalagem)
- **Tamanho mínimo:** 11px de altura tipográfica (não usar menor — `°` perde legibilidade)
- **Nunca:** efeitos de gradiente, sombra, 3D, contorno
- **Nunca:** trocar a cor do `°` (sempre Lima Sutil)

### 13.4 Versão alternativa — em embalagem física

Em packaging físico (etiquetas, caixas, hangtags), o logo pode aparecer em sua versão estendida:

```
budamix°
Casa · Cozinha · Saúde
```

Tagline em Plus Jakarta Sans 500, 7px, Lima Sutil, uppercase, letter-spacing 1.5px.

---

## 14. BOTÃO CTA — BANNERS DE MARKETING

> **Mais detalhado que o componente Button** — esse é o CTA que aparece na peça de conversão final.

### Especificação

- **Fonte:** Plus Jakarta Sans 600/700, uppercase
- **Letter-spacing:** 1.0–1.2px
- **Border-radius:** 999px (pílula completa)
- **Padding:** 7px–11px vertical, 14px–22px horizontal
- **Background:** Burnt Terracotta `#C1553D`
- **Foreground:** Ivory Mist `#FAF7F2`
- **Ícone:** seta `→` à direita, espaço 4–6px do texto, mesma cor do texto
- **Sombra:** nenhuma (estilo flat na v2.0)

### Copy recomendada

Curta, direta, primeira pessoa ou imperativa:

- `Quero começar →`
- `Saiba mais →`
- `Comprar agora →`
- `Salvar carrossel →`
- `Ver coleção →`
- `Quero o meu →`

Não usar palavras frias como "Acessar" ou "Continuar" — a marca pede calor humano até no botão.

---

## 15. TEMPLATES DE CARROSSEL INSTAGRAM

> **Sistema de templates da v2.0** — combinações testadas dos elementos DNA pra cada tipo de conteúdo. Use como starting point, adapte conforme necessidade.

### 15.1 Formato padrão

- **Aspect ratio:** 4:5 vertical (1080×1350px) — formato preferencial
- **Aspect ratio alternativo:** 1:1 quadrado (1080×1080px) — usar quando carrossel for "feed-friendly" sobre 4:5
- **Margem segura interna:** 60px de cada borda
- **Numeração de página:** obrigatória em cada slide (canto inferior direito, pílula Burnt Terracotta)

### 15.2 Template T1 — Capa narrativa

Slide 1 de qualquer carrossel temático.

**Estrutura:**
- Logo budamix° canto superior esquerdo
- Badge brand canto superior direito ("CASA · COZINHA", "DESPENSA", "RECEITA" etc.)
- Setas hero Lima Sutil (1 grande + 1 secundária 60% do tamanho)
- Headline Bricolage 800 uppercase, 28–34px, quebrando em 2–3 linhas
- 2 pílulas inferiores: pill-soft (italic Plus Jakarta) + pill-strong (Bricolage Lima Sutil)
- Pílula PAGE 01

**Fundo recomendado:** Deep Teal (vibe premium) ou Ivory Mist (vibe leve)

### 15.3 Template T2 — Lista numerada

Cada slide apresenta um item da lista.

**Estrutura:**
- Logo budamix° + badge brand
- Número grande Bricolage 800, 90–130px, em Lima Sutil (ou Burnt Terracotta na capa T1 com lista)
- Eyebrow ao lado do número
- Headline curto Bricolage uppercase
- Pixel pattern 1–2 posições
- Pílula PAGE N

**Fundo recomendado:** Ivory Mist (clareza pra leitura rápida)

### 15.4 Template T3 — Foto + texto (depoimento)

Slide com prova social de cliente real.

**Estrutura:**
- Foto colorida da pessoa em cozinha (60% superior do slide)
- Quote bubble Ivory Mist DENTRO da foto (3 pontinhos Lima Sutil + texto + palavra italic)
- Bottom content (40% inferior): bot-h Bricolage com italic acento + bot-sub
- Círculo cortado Lima Sutil canto inferior esquerdo
- Pílula PAGE N

**Fundo recomendado:** Ivory Mist (foto se destaca melhor)

### 15.5 Template T4 — Ícone vetorial central

Slide explicativo de conceito ou atributo.

**Estrutura:**
- Logo budamix° + badge brand
- Ícone vetorial em SVG no centro (Lima Sutil), 60–80px
- Selection markers nos 4 cantos do ícone
- Headline Bricolage 800 abaixo do ícone
- Body Plus Jakarta abaixo do headline
- Seta deco rotacionada
- Pílula PAGE N

**Fundo recomendado:** Deep Teal (ícone Lima Sutil ganha contraste)

### 15.6 Template T5 — CTA final

Último slide do carrossel — chamada pra ação.

**Estrutura:**
- Logo budamix° + badge brand
- Headline Bricolage 800 com pílula inline (palavra dentro de pílula Lima Sutil)
- Sub Plus Jakarta com argumento curto
- CTA row: botão pílula Burnt Terracotta + URL JetBrains Mono
- Círculo cortado Lima Sutil canto
- Pílula PAGE N

**Fundo recomendado:** Ivory Mist (foco no CTA Burnt Terracotta)

### 15.7 Estrutura sugerida de carrossel completo (6–7 slides)

| Slide | Template | Função |
|-------|----------|--------|
| 1 | T1 | Capa narrativa — apresenta o tema |
| 2 | T2 ou T4 | Conceito ou primeira ideia da lista |
| 3 | T2 ou T3 | Continuação ou prova social |
| 4 | T2 ou T4 | Mais conceito ou ideia |
| 5 | T3 | Depoimento de cliente real |
| 6 | T5 | CTA final com URL e botão |
| 7 (opcional) | T1 simplificado | "Comente abaixo" / "Salve esse post" |

---

## 16. TRATAMENTO DE FOTOS

### 16.1 Foto P&B (preto e branco)

**Quando usar:** em slides de produto técnico, momento "antes/depois", ambientação editorial premium.

**Como aplicar:**
- Conversão completa pra grayscale
- Contraste levemente aumentado
- Sobreposição de elemento colorido (tampa do pote em Burnt Terracotta) pra criar foco visual

**Vibe:** premium editorial, marca atemporal.

### 16.2 Foto colorida natural

**Quando usar:** em depoimentos, lifestyle, contexto humano real.

**Como aplicar:**
- Cores naturais, com leve calibração pra harmonizar com paleta (warmth +5, saturação levemente reduzida)
- Sem filtros agressivos, sem black-and-white forçado
- Quote bubble Ivory Mist sobreposta (template T3)

**Vibe:** real, próxima, lived-in.

### 16.3 Mistura — slides de conteúdo

Carrossel pode (e deve) misturar foto P&B em alguns slides com foto colorida em outros. Cria ritmo visual e quebra monotonia.

**Regra:** se o carrossel tem 6 slides, recomendado 2–3 P&B + 3–4 coloridos. Não fazer "metade P&B / metade colorido" — deixa esquizofrênico.

### 16.4 Label técnica de foto

Em mockups de design system ou apresentações internas, fotos podem ter label JetBrains Mono no canto identificando o tipo:

```
foto P&B · cliente real
foto colorida · cozinha bancada
foto produto · vidro premium
```

7–9px, opacidade 0.55–0.65, cor da própria foto invertida (claro sobre escuro).

---

## 17. CORES POR MARKETPLACE

> Para dashboards, relatórios e visualizações cross-marketplace. Independente da paleta principal — esses tokens são utilitários internos.

| Plataforma | Cor | Uso |
|------------|-----|-----|
| **Shopee** | `#4CAF50` | Verde — gráficos, badges, headers de seção Shopee |
| **Mercado Livre** | `#42A5F5` | Azul — idem para ML |
| **Amazon** | `#AB47BC` | Roxo — idem para Amazon |

---

## 18. HISTÓRICO DE VERSÕES

### v2.1 (07/05/2026 · noite) — DNA visual lapidado pelas referências reais

**Mudanças vs v2.0:**

- **8 elementos do DNA visual lapidados** com base em 6 referências reais de stories Instagram. Saíram elementos teóricos pouco recorrentes; entraram elementos observados como recorrentes nas referências.

| Sai | Entra |
|-----|-------|
| Selection markers (4 pontos no canto de elemento) | Pontos em coluna vertical (3-4 dots laterais) |
| Pixel pattern (grid de quadrados) | Matriz de pontos (grid de círculos) |
| Círculo cortado de borda | Quadrados arredondados decorativos (3 quadrados sobrepostos) |
| Quadrante decorativo orgânico | Hatch pattern (listras diagonais em quadrado) |
| — | Frame externo + card interno (estrutura padrão) |
| — | Pílula headline com canto cortado |
| — | Chevrons em fileira (`>>>` `<<<`) |
| — | Asterisco estilizado (símbolo de 6-8 pontas) |

- **Total de elementos: 14** (3 estruturais + 8 decorativos + 3 especiais)
- **Frame externo** virou **estrutura base** de toda peça (story, post, slide) — mudança fundamental
- **Pílula headline** com canto cortado vira a forma padrão de apresentar título principal — substitui headline-direto-no-fundo da v2.0
- Limite de saturação subiu de 4 pra 5 elementos por slide

**Inconsistências da v2.0 resolvidas:**
- Selection markers eram conceito teórico que nunca apareceu em peças reais — removidos
- Pixel pattern de quadrados confundia com hatch pattern — substituído por matriz de pontos circulares (mais distintivo)

### v2.0 (07/05/2026) — Floresta com Faísca + DNA Editorial Playful

**Mudanças vs v1.2:**
- Paleta reescrita como "Floresta com Faísca": Forest Night substitui Graphite, Fern Green substitui Sage, Lima Sutil substitui Amber Gold, Burnt Terracotta substitui Terracotta atual, Linen substitui Porcelain, Ivory Mist substitui Areia. Deep Teal mantido como âncora.
- Stack tipográfica simplificada de 4 pra 3 fontes (DM Sans removida — redundante com Plus Jakarta Sans).
- Logo refeito: `BUDAMIX` (caixa alta, BUDA branco + MIX dourado) → `budamix°` (minúscula, com `°` em Lima Sutil como assinatura).
- **Novo DNA visual editorial playful** com 9 elementos sistematizados.
- Novo componente Pill (chip) como categoria dedicada.
- 5 templates de carrossel Instagram sistematizados (T1 a T5).
- Tratamento de fotos formalizado (P&B + colorida + label técnica).
- Mistura tipográfica deliberada (Bricolage uppercase + Plus Jakarta italic dentro do mesmo headline) virou regra crítica.

**Inconsistências da v1.2 resolvidas:**
- Teal primário: confirmado `#004D4D` em todos os contextos.
- Body font: agora unificado em Plus Jakarta Sans (e-commerce e banners).
- Heading font: unificado em Bricolage Grotesque (e-commerce e banners).
- Verde aprovação `#18794E`: substituído por Fern Green `#4A7C59` (mesmo papel, dentro da paleta canônica).

### v1.2 (28/04/2026) — Versão anterior

Documentação original consolidada de 8 fontes distintas. Paleta "Sage Premium" com Amber Gold como destaque, Terracotta como CTA. Stack de 4 fontes. Logo BUDAMIX caixa alta com split "BUDA + MIX" (branco + dourado). DNA visual focado em "premium silencioso" estilo Granado/Le Labo.

---

## 19. FONTES

Documentos consultados pra montar este consolidado:

| Fonte | Path | Conteúdo |
|-------|------|----------|
| **DESIGN-TOKENS.md** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/design/DESIGN-TOKENS.md` | Tokens HSL + Tailwind do e-commerce — atualizar pra v2.0 |
| **DNA Visual** | `~/Documents/07-Conteudo-Marketing/REELS-BUDAMIX/budamix-dna-visual.md` | Regras pra banners, reels e geração de conteúdo — atualizar pra v2.0 |
| **index.css** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/index.css` | CSS variables HSL canônicas — atualizar pra v2.0 |
| **tailwind.config.ts** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/tailwind.config.ts` | Mapeamento fonte/cor pra utilities — atualizar pra v2.0 |
| **MOC** | `~/segundo-cerebro/meta/mocs/MOC - Design Systems Budamix.md` | Hub de 3 design systems — atualizar índice |
| **Ficha do projeto** | `~/segundo-cerebro/projects/budamix-ecommerce.md` § Design System | Histórico de decisões |
| **Referências DNA visual** | 2 imagens fornecidas em 07/05/2026 — carrosséis "5 Carousel Branding" e "Personal Brand" | Inspiração editorial playful pra elementos novos do sistema |

---

## ANEXO A — CHEAT SHEET RÁPIDO

### Cores essenciais (decoradas)

```
Deep Teal       #004D4D    âncora — toda peça
Forest Night    #1B3A2D    texto longo
Fern Green      #4A7C59    eyebrow, apoio
Lima Sutil      #B8D043    faísca, decoração
Burnt Terracotta#C1553D    CTA + numeração página
Linen           #E8DFD4    cards, fundo suave
Ivory Mist      #FAF7F2    base de toda peça clara
```

### Stack (decorada)

```
Bricolage Grotesque 700/800     display
Plus Jakarta Sans 400/500/600/700+italic     body + voz
JetBrains Mono 400/500          números técnicos
```

### Mistura tipográfica regra

```
[BRICOLAGE UPPERCASE] + [Plus Jakarta italic] + [BRICOLAGE UPPERCASE]
"Por que isso *importa* na sua despensa"
   ↑ Deep Teal      ↑ Burnt Terracotta italic    ↑ Deep Teal
```

### Numeração de página

```
PAGE 01    Burnt Terracotta + Ivory Mist + Plus Jakarta 600 + uppercase
canto inferior direito · obrigatório em todo slide carrossel
```

### Logo

```
budamix°
   ↑ minúscula Bricolage 800 Forest Night · ° em Lima Sutil sempre
```

### Elementos do DNA visual v2.1 (3 estruturais + 8 decorativos + 3 especiais)

```
ESTRUTURAIS (uso em quase todo slide)
1. Frame externo + card interno — estrutura base de toda peça
2. Pílula headline — bloco escuro com canto cortado, título principal
3. Pílula numeração página — Burnt Terracotta canto inferior direito (carrossel only)

DECORATIVOS (uso em rotação)
4. Hatch pattern — listras diagonais em quadrado, decoração de canto
5. Pontos em coluna — 3-4 círculos verticais, decoração lateral
6. Matriz de pontos — grid 4x3 ou 5x4 de círculos
7. Chevrons fileira — >>> e <<< flanqueando texto
8. Asterisco — símbolo de 6-8 pontas, decoração solta
9. Quadrados arredondados — 3 quadrados sobrepostos em canto
10. Setas hero — ↘ ou → grandes (50-100px)
11. Pílula inline — palavra dentro de pílula colorida no headline

ESPECIAIS (uso em momentos específicos)
12. Italic acento — palavra em Plus Jakarta italic Burnt Terracotta
13. Quote bubble — balão de fala em fotos de depoimento
14. Pílula CTA — botão pílula "Saiba mais"
```

### Hierarquia de uso de Lima Sutil

```
1. palavra de destaque em headline (acento)
2. seta hero (gesto visual)
3. asterisco estilizado (decoração solta)
4. pontos em coluna (decoração lateral)
5. matriz de pontos (decoração intermediária)
6. chevrons fileira (moldura lateral de texto)
7. pílula inline em headline (caixa de destaque)
8. quadrados arredondados (decoração de canto)
```

### Hierarquia de uso de Burnt Terracotta

```
1. CTA (botão de conversão)
2. pílula de numeração de página
3. italic acento de palavra (em fundo claro)
4. frame externo de stories de alerta/urgência
```

### "Nunca"

```
× Lima Sutil em parágrafo longo
× Burnt Terracotta em fundo grande
× Lima Sutil + Fern Green próximos no mesmo slide
× Mais que 5 elementos DNA num mesmo slide
× Mais que 1 pílula inline por slide
× Mais que 1 italic acento por headline
× Mais que 1 matriz de pontos por slide
× Mais que 2 grupos de pontos em coluna por slide
× ALL CAPS em parágrafos (só em headlines Bricolage)
× Logo budamix° sem o ° em Lima Sutil
× CTA em formato retangular (sempre pílula 999px)
× Frame externo com card interno também colorido (cria competição)
```

---

*Documento consolidado em 07/05/2026 a partir das decisões de paleta, tipografia e DNA visual lapidado pelas referências reais de stories. Substitui integralmente a v1.2 e v2.0. Revisar trimestralmente conforme evolução da marca.*

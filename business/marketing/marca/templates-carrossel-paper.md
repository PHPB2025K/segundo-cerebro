---
title: "Templates de Carrossel Budamix — Paper.design"
created: 2026-05-03
type: design-asset
status: active
tags:
  - business/marketing
  - marca
  - design-system
  - templates
  - paper-design
related:
  - "[[design-system]]"
  - "[[recomendacao-carrosseis]]"
---

# Templates de Carrossel Budamix — Paper.design

Sistema completo de 5 templates-pai × 3 versões cromáticas (CLARA, NORMAL, ESCURA) = **96 artboards 1080×1080** prontos no Paper.design pra carrosséis Instagram, Reels covers, posts de feed, etc.

Construído em 02-03/05/2026 a partir do briefing v2 (5 templates agnósticos de cor + sistema cromático contextual).

---

## 🔗 Acesso

**Arquivo Paper.design:** https://app.paper.design/file/01KQMVPNGXW4ZWQPVE1KDPMBN3
*(nome interno: "Inventive castle")*

---

## 📐 Estrutura — 96 artboards organizados em 5 famílias verticais

| Template | Slides | Total artboards | Função |
|---|---|---|---|
| **T1 · Lançamento** | 6 (capa, revelação, contexto, 3 atributos, specs, CTA) | 18 | Apresentar algo novo (produto, linha, coleção) |
| **T2 · Lista Enumerada** | 7 (capa numérica, 5 itens, CTA) | 21 | "X motivos / X dicas / X erros" |
| **T3 · Tutorial** | 7 (capa promessa, 4 passos, resultado, CTA) | 21 | "Como fazer X" — sequência didática |
| **T4 · Storytelling** | 6 (capa, ANTES, virada, DEPOIS, reforço, CTA) | 18 | Mostrar transformação / antes-depois |
| **T5 · Credibilidade** | 6 (capa autoridade, evidência, 3 cards apoio, depoimento, atributos, CTA) | 18 | Social proof, autoridade, depoimentos |

**Layout no canvas:** cada família ocupa 3 linhas verticais (uma por versão cromática), na ordem CLARA → NORMAL → ESCURA. Famílias separadas por gap de 600px verticais.

---

## 🎨 3 Versões Cromáticas

### CLARA · Areia `#F7F4EF`
- **Atmosfera:** clean, aspiracional, lifestyle, Pinterest-inspired
- **Quando usar:** posts de produto em ambiente, organização, conteúdo aspiracional
- **Títulos:** verde teal `#004D4D` (decisão validada por Pedro — "ficou bem melhor que grafite")
- **Body/subheadline:** grafite muted `rgba(19,37,37,0.7)`
- **Eyebrow:** sage `#7EADAD`
- **Logo:** verde-teal transparente
- **Capa e CTA:** fundo areia (não overlay escuro)

### NORMAL · Teal `#004D4D`
- **Atmosfera:** marca pura, declarativo, autoridade institucional
- **Quando usar:** comunicação institucional, lançamentos âncora
- **Títulos:** branco `#FFFFFF`
- **Body/eyebrow:** porcelana `#D9E6E6`
- **Logo:** branco transparente

### ESCURA · Grafite `#132525`
- **Atmosfera:** dramática, premium, editorial, "noturno"
- **Quando usar:** lançamentos com peso, conteúdo premium, anúncios coleções, pré-lançamentos misteriosos
- **Títulos:** branco
- **Body:** porcelana
- **Eyebrow:** sage `#7EADAD`
- **Logo:** branco
- **Capa/CTA:** radial-gradient teal central + overlay denso

### Acentos constantes (não mudam entre versões)
- **Dourado:** `#C7A35A` — palavra-chave headline + selos + traço eyebrow
- **Terracota:** `#C56A4A` — EXCLUSIVO do botão CTA

---

## 🖼️ Logos (paths absolutos)

Logos cropados à proporção do conteúdo (~5.17:1, 1008×195 base):

- **Verde transparente** (CLARA): `/Users/pedrobroglio/Documents/05-Projetos-Codigo/planejamento-importacao-2026/assets-templates/BUDAMIX LOGO VERDE TRANSPARENTE-CROP.png`
- **Branco transparente** (NORMAL/ESCURA): `/Users/pedrobroglio/Documents/05-Projetos-Codigo/planejamento-importacao-2026/assets-templates/BUDAMIX LOGO BRANCA SEM FUNDO-CROP.png`

**Tamanhos canônicos no design:**
- Rodapé padrão: `width: 186px; height: 36px`
- Signature CTA (canto direito): `width: 258px; height: 50px`

**Originais antes do crop (não usar diretamente — têm fundo branco opaco no caso do verde):**
- Verde sobre fundo branco: `/Users/pedrobroglio/Downloads/Imagens/2025/Marketing-Design/BUDAMIX LOGO VERDE ESCURO.png`
- Branco transparente original: `/Users/pedrobroglio/Downloads/Imagens/2024/Marketing-Design/BUDAMIX LOGO BRANCA SEM FUNDO.png`

---

## 🔄 Como reusar (em outro projeto)

### Cenário 1: Usar um template direto
1. Abrir o arquivo Paper acima
2. Localizar a versão cromática que combina com o post (CLARA / NORMAL / ESCURA)
3. **Duplicar a linha inteira** da versão escolhida (ex: T3 NORMAL = 7 artboards horizontais)
4. Mover pra um arquivo novo ou área separada
5. Substituir os slots `{{...}}` por conteúdo real:
   - `{{HEADLINE}}` / `{{TÍTULO-ITEM 01}}` / etc → texto
   - Placeholders de imagem (retângulos com label `{{IMG · 4:5}}`) → arrastar imagens reais por cima

### Cenário 2: Spin-off do design system pra outro produto/marca
- O sistema é estrutural — pode ser portado mantendo só os tokens cromáticos
- Substituir paleta CLARA/NORMAL/ESCURA pelos tokens da nova marca
- Fontes (Plus Jakarta Sans + DM Sans) são gratuitas no Google Fonts
- Estrutura dos slots, hierarquia tipográfica e layouts permanecem

### Cenário 3: Criar versões 9:16 (Stories) ou 4:5 (feed otimizado)
Não estão prontas, mas o sistema é replicável:
- 9:16 (1080×1920) → adaptar T1/T5 capas full-bleed pra Stories
- 4:5 (1080×1350) → ajustar gaps verticais

---

## 📋 Slots padrão (copy-paste pra brief de conteúdo)

**Capa T1/T4/T5:** `{{EYEBROW}}` · `{{HEADLINE}}` · `{{PALAVRA-CHAVE em dourado}}`
**Capa T2:** `{{N}}` (número grande) · `{{HEADLINE-LISTA}}` · `{{PALAVRA-CHAVE}}`
**Capa T3:** `Como` (fixo) · `{{PALAVRA-CHAVE}}` · `{{COMPLEMENTO}}` + imagem teaser do resultado
**Slides internos:** dependem do template — cada um tem 3-7 slots numerados nas linhas
**CTA (todos):** `{{HEADLINE-CTA}}` · `{{COMPLEMENTO-DOURADO}}` · `{{TEXTO-CTA}}` (ex: VER COLEÇÃO, COMPRAR AGORA)

---

## ⚠️ Limitações conhecidas

1. **Paper Shaders (mesh gradient, grain, liquid metal) NÃO foram aplicados via MCP** — o Paper Shaders é uma lib React separada, não acessível via CSS/HTML. Se quiser elevar visualmente, aplicar manualmente na UI do Paper Desktop em capas escolhidas.
2. **Imagens são placeholders genéricos** — não foi colocada arte real. Quando usar, substituir os retângulos pelos visuais finais.
3. **Espelhamento ANTES/DEPOIS no T4** funciona via badge dourado vs sage/porcelana. Pra reforçar transformação, usar imagens dessaturadas no ANTES e quentes no DEPOIS.

---

## Histórico

- **02/05/2026** — Construção inicial dos 32 artboards (5 templates × NORMAL apenas) no arquivo "Budamix — Templates Carrossel v1"
- **02/05/2026** — Briefing v2 expandido pra 3 versões cromáticas, novo arquivo "Inventive castle" iniciado
- **02-03/05/2026** — 96 artboards completos (5 × 3 = 15 carrosséis); títulos CLARA validados em teal pelo Pedro; logos PNG aplicados via `paper-asset://`; bugs cromáticos T4-05 e T5-05 corrigidos; centralização vertical dos 3 atributos/benefícios aplicada

---

## Ver também

- [[design-system]] — paleta + tipografia oficial Budamix
- [[recomendacao-carrosseis]] — recomendações de conteúdo pra carrosséis
- [[recomendacao-legendas]] — copy + CTA por contexto

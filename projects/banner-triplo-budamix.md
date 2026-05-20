---
title: "Banner Triplo Budamix"
created: 2026-05-20
type: project
status: done
path: "~/Documents/05-Projetos-Codigo/banner-triplo-budamix/"
tags:
  - project
  - dev
  - marketing
  - design
---

# Banner Triplo Budamix

**Path:** `~/Documents/05-Projetos-Codigo/banner-triplo-budamix/`
**Status:** ✅ Entregue 20/05/2026
**Output:** `output/capa-01.png`, `capa-01-v2.png`, `capa-02.png`, `capa-03.png` (2000×2500 px) + `mockup-feed.png` (6040×2500)

## O que é

3 capas Instagram (formato 4:5 vertical, 2000×2500 px) que formam banner contínuo quando vistas lado a lado no feed. Paralelogramos Lima Sutil migram entre as capas criando ilusão de banner único de 3 dobras. Cada capa serve como primeiro slide do seu carrossel.

## Stack técnica

- **HTML + CSS puro** (sem framework)
- **Puppeteer** (headless Chrome) pra exportar PNG via `npm run render`
- **Google Fonts:** Antonio Bold (headlines) + Inter (corpo)
- 3 arquivos HTML self-contained + 1 script Node (`render.js`)

## Composição

| Slide | Tema | Estado |
|---|---|---|
| Capa 01 | "VIVA O MELHOR DA SUA CASA COM A BUDAMIX" | Versão v1 (4 linhas) e v2 (3 linhas) — Pedro escolhe |
| Capa 02 | "CONHEÇA NOSSOS PRODUTOS" | Placeholder retangular Deep Teal pra inserir foto dos potes no Canva |
| Capa 03 | "O QUE NOSSOS CLIENTES DIZEM?" | Placeholder circular pra foto da cliente Morgana |

## Tipografia (regra inviolável)

- **Antonio Bold 700 UPPERCASE** em TODOS os títulos
- **Inter** em textos secundários (eyebrow, caption, URL, footer)
- Palavra de acento (CASA, PRODUTOS, CLIENTES, BUDAMIX) em **Antonio Bold UPPERCASE** + cor Burnt Terracotta `#C1553D` — única diferença vs resto do título é a cor (sem italic, sem mudança de fonte, sem mudança de tamanho)

## Paleta usada

| Cor | Hex | Uso |
|---|---|---|
| Deep Teal | `#004D4D` | headlines, placeholders |
| Forest Night | `#1B3A2D` | logo, texto secundário |
| Fern Green | `#4A7C59` | URL, eyebrow, divisor |
| Lima Sutil | `#B8D043` | paralelogramos, ° do logo, seta hero, anel da foto cliente |
| Burnt Terracotta | `#C1553D` | palavras de acento, pílula PÁGINA, estrelas |
| Ivory Mist | `#FAF7F2` | fundo principal |

## Continuidade visual entre capas

Paralelogramos Lima com `transform: skewX(-22deg)` cruzam as bordas:
- Capa 01 (top-right) ↔ Capa 02 (top-left) — coordenada `top: 280px` idêntica
- Capa 02 (bottom-right) ↔ Capa 03 (bottom-left) — coordenada `top: 1450px` idêntica

## Pra usar

```bash
cd ~/Documents/05-Projetos-Codigo/banner-triplo-budamix
npm install   # primeira vez
npm run render
```

PNGs ficam em `output/` prontos pra importar no Canva, recortar como slides, e adicionar manualmente:
- Capa 1: pronta
- Capa 2: foto dos potes herméticos no retângulo placeholder
- Capa 3: foto circular da cliente Morgana no círculo placeholder

## Decisões

- [20/05] Antonio Bold como única fonte de display — substituiu cogitação inicial de Inter Italic 700 pra palavras de acento. Palavra de acento mantém Antonio Bold UPPERCASE, mudando apenas a cor pra Burnt Terracotta
- [20/05] Build com webpack porque turbopack quebrava externals (não aplica aqui — sem deps Next, mas regra registrada pro caso futuro)
- [20/05] 2 versões da Capa 01 entregues (4 linhas vs 3 linhas) — Pedro escolhe qual será final

## Em aberto

- [ ] Pedro escolher entre `capa-01.png` (4 linhas: `VIVA O MELHOR / DA SUA CASA / COM A / BUDAMIX`) vs `capa-01-v2.png` (3 linhas: `VIVA O MELHOR / DA SUA CASA / COM A BUDAMIX`)
- [ ] Inserir foto real dos potes (Capa 2) e foto da Morgana (Capa 3) no Canva
- [ ] Publicar no feed Instagram da Budamix

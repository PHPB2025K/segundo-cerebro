---
title: "Nano Banana / Gemini não gera PNG com alpha channel real"
created: 2026-04-20
type: concept
status: active
tags:
  - knowledge
  - ai
  - gemini
  - nano-banana
  - image-generation
  - limitations
---

# Nano Banana / Gemini não gera PNG com alpha channel real

## Limitação descoberta

Apesar de aceitar instruções explícitas como *"transparent background, PNG with alpha channel, no color fill"*, o Gemini image generation (aka Nano Banana) **sempre exporta em modo RGB sem canal alpha**. Em vez de gerar transparência real, ele **renderiza o padrão xadrez (checkerboard) de transparência como pixels sólidos** — cinza claro (~180,180,180) + branco (~255,255,255) alternados.

## Sintoma

Output visualmente parece ter fundo transparente no preview, mas ao analisar:

```python
from PIL import Image
img = Image.open('generated.png')
print(img.mode)  # RGB (não RGBA)
# Corner pixels sample:
# (183, 183, 185), (254, 255, 255)  ← cinza/branco do "checkerboard fake"
```

```bash
sips -g hasAlpha generated.png
# hasAlpha: no
```

## Workarounds

### 1. rembg (U2Net AI local)
```bash
pip3 install rembg onnxruntime
rembg i input.png output.png
```
~200MB de download no primeiro uso (modelo). Offline depois. Qualidade boa em fotos de produto.

### 2. remove.bg (manual, web)
Upload em https://remove.bg, download PNG com alpha real. 1 minuto. Não depende de código.

### 3. Gerar com fundo sólido conhecido e usar direto
Gemini gera bem qualquer cor sólida de fundo (`#132525`, `#C56A4A`, etc). Usa o fundo embutido no produto final em vez de tentar isolar. Menos flexível pra reuso da imagem.

### 4. Chroma-key via PIL (frágil)
Detectar pixels do checkerboard e setar alpha=0. Só funciona se a paleta do xadrez não colidir com cores do produto — não é o caso de fotos com áreas brancas/cinzas claras, onde vira um massacre.

## Outras limitações relacionadas do Gemini

- **Não corrige textos corrompidos**: se a imagem de referência tem typos ou texto ilegível (ex: arte gerada por outro modelo antes), Gemini preserva pixel-perfect os typos. Pode ser feature ou bug dependendo do caso.
- **Prior "fill the frame" forte**: em fotos de produto, tende a ocupar 75-90% do frame independente de prompt pedindo "more white space / zoom out / 15% padding on each side". 5 tentativas com prompt idêntico em [[memory/sessions/2026-04-20]] mostraram alternância entre logo nítido+padding apertado e padding bom+logo borrado.

## Aplicado em

- [[projects/budamix-ecommerce]] 2026-04-20 — tentativas de gerar foto dos potes de vidro com fundo transparente pro HeroBanner falharam (checkerboard sólido). Pedro acabou usando foto gerada no ChatGPT com fundo Graphite já embutido.
- Várias tentativas descartadas em `~/Documents/05-Projetos-Codigo/planejamento-importacao-2026/generated_imgs/edited-2026-04-20T*.png`.

## Ver também

- [[memory/sessions/2026-04-20]] — Sessão 3 (Budamix E-commerce)
- [Gemini image generation docs](https://ai.google.dev/) — oficial

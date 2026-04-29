---
title: "Design System — Budamix v1.2"
created: 2026-04-29
type: reference
domain: marketing
status: active
tags:
  - business/marketing
  - marca
  - budamix
  - design-system
  - identidade-visual
  - branding
---

# BUDAMIX — DESIGN SYSTEM

> **Versão:** v1.2 (consolidado em 28/04/2026)
> **Marca:** Budamix · GB Importadora
> **Site:** https://budamix.com.br

---

## SUMÁRIO

1. [Sobre a marca](#1-sobre-a-marca)
2. [Personalidade visual](#2-personalidade-visual)
3. [Paleta de cores](#3-paleta-de-cores-fonte-de-verdade)
4. [Tipografia](#4-tipografia)
5. [Spacing scale](#5-spacing-scale)
6. [Shadow scale](#6-shadow-scale)
7. [Border radius](#7-border-radius)
8. [Componentes — Button](#8-componentes--button)
9. [Componentes — Badge](#9-componentes--badge)
10. [Logotipo](#10-logotipo)
11. [Botão CTA — banners de marketing](#11-botão-cta--banners-de-marketing)
12. [DNA visual — banners e reels](#12-dna-visual--banners-e-reels)
13. [Cores por marketplace](#13-cores-por-marketplace)
14. [Inconsistências e divergências documentadas](#14-inconsistências-documentadas)
15. [Fontes deste documento](#15-fontes)

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
| **Estilo** | Limpo, elegante, com calor humano. Nunca genérico, nunca poluído |
| **Inspiração** | Granado + Great Jones (referências visuais) |
| **Atmosfera** | Casa brasileira Pinterest-inspired, lived-in mas curado |
| **Luz** | Natural, quente, suave — nunca dura ou clínica |
| **Materialidade** | Madeira clara, vidro, pedra, linho, cerâmica fosca |

---

## 3. PALETA DE CORES (FONTE DE VERDADE)

> Fonte canônica: `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/index.css`
> Mapeada em `tailwind.config.ts` via `hsl(var(--*))`.

### 3.1 Cores principais

| Token brand | Nome | Hex | HSL | CSS var | Tailwind utility | Uso |
|-------------|------|-----|-----|---------|------------------|-----|
| **Deep Teal** | Primary | `#004D4D` | `180 100% 15%` | `--primary` | `bg-primary text-primary-foreground` | CTA, links, ações principais. **Cor âncora da marca** |
| **Graphite** | Foreground | `#132525` | `180 32% 11%` | `--foreground` | `text-foreground` | Texto principal, fundo secundário |
| **Sage** | Secondary | `#7EADAD` | `180 24% 59%` | `--secondary` | `bg-secondary text-secondary-foreground` | Eyebrow, badges de apoio, bordas finas |
| **Terracotta** | Accent | `#C56A4A` | `17 52% 53%` | `--accent` | `bg-accent text-accent-foreground` | **CTA exclusivo de banners** + promoções/urgência (uso restrito) |
| **Amber Gold** | Gold | `#C7A35A` | `41 47% 57%` | `--gold` | `bg-gold text-gold-foreground` | Estrelas, premium, rating, destaque tipográfico |
| **Porcelain** | Porcelain | `#D9E6E6` | `180 25% 88%` | `--porcelain` | `bg-porcelain` | Texto secundário sobre fundo escuro, placeholder de imagem |
| **Areia** | Background | `#F7F4EF` | `40 27% 96%` | `--background` | `bg-background` | Fundo geral da página |

### 3.2 Cores de superfície e suporte

| Token | Hex | HSL | CSS var | Uso |
|-------|-----|-----|---------|-----|
| Card | `#FFFFFF` | `0 0% 100%` | `--card` | Cards, modais, popovers |
| Muted | `#EDE8E0` | `36 22% 90%` | `--muted` | Fundos sutis, disabled |
| Muted foreground | — | `180 20% 35%` | `--muted-foreground` | Texto secundário, placeholders |
| Border | `#C2D1D1` | `180 15% 80%` | `--border` | Bordas padrão |
| Border subtle | `#E5E0D8` | `40 15% 88%` | `--border-subtle` | Bordas sutis (cards, inputs) |
| Ring | `#004D4D` | `180 100% 15%` | `--ring` | Focus ring (= primary) |
| Destructive | — | `0 72% 51%` | `--destructive` | Erros, exclusões, alerta crítico |
| Success | — | `152 69% 31%` | `--success` | Confirmações, validação |

### 3.3 Cores de uso específico (banners marketing)

| Token | Hex | Uso |
|-------|-----|-----|
| Verde Aprovação | `#18794E` | Badges "BPA-free", "hermético", "aprovado" — exclusivo de banners marketing/reels (não tokenizado no e-commerce) |
| Branco | `#FFFFFF` | Texto principal sobre fundos escuros, vidro dos potes |

### 3.4 Regra de ouro da paleta

> **Teal é cor âncora.** Dourado é acento premium. Terracotta é reservado pro **único CTA**. Nunca usar as três com peso visual igual — hierarquia obrigatória.

---

## 4. TIPOGRAFIA

> Existem **2 sistemas tipográficos** por contexto, com ponto comum em **Plus Jakarta Sans**.

### 4.1 E-commerce (budamix.com.br)

Fonte canônica: `src/index.css` + `tailwind.config.ts` (via `@fontsource-variable`).

| Camada | Fonte | Variável Tailwind | Pesos | Uso |
|--------|-------|--------------------|-------|-----|
| Heading / Display | **Bricolage Grotesque Variable** | `font-heading` / `font-display` | 800 ExtraBold | H1–H6, títulos de seção |
| Body / UI | **Plus Jakarta Sans Variable** | `font-body` / `font-sans` | 400 / 500 / 600 | Parágrafos, UI labels, links |
| Monospace | **JetBrains Mono Variable** | `font-mono` | 700 Bold | Preços, códigos, SKUs |

### 4.2 Banners marketing / reels (DNA visual)

Fonte canônica: `~/Documents/07-Conteudo-Marketing/REELS-BUDAMIX/budamix-dna-visual.md`.

```css
body { font-family: 'DM Sans', system-ui, sans-serif; }
h1, h2, h3, h4, h5, h6 { font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }
```

Import obrigatório:
```
https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap
```

| Camada | Fonte | Peso | Cor | Função |
|--------|-------|------|-----|--------|
| **Eyebrow** | DM Sans | 500 Medium | Sage `#7EADAD`, uppercase, letter-spacing amplo | Contextualiza o banner. **Sempre precedido por traço horizontal curto (18–22px) dourado** |
| **Headline** | Plus Jakarta Sans | 800 ExtraBold | Branco com palavra-chave em **Dourado `#C7A35A`** | Promessa principal |
| **Subheadline** | DM Sans | 400 Regular | Porcelana `#D9E6E6` | Argumento curto |
| **CTA** | DM Sans | 600 SemiBold | Branco | Texto do botão (caixa alta, letter-spacing 0.12–0.16em) |

### 4.3 Type scale (e-commerce, Tailwind defaults)

| Token | Size | Uso |
|-------|------|-----|
| `text-xs` | 12px | Labels, tags |
| `text-sm` | 14px | Body small, captions |
| `text-base` | 16px | Body padrão |
| `text-lg` | 18px | Lead, intro |
| `text-xl` | 20px | H4 |
| `text-2xl` | 24px | H3, preços |
| `text-3xl` | 30px | H2 |
| `text-4xl` | 36px | H1 mobile |
| `text-5xl` | 48px | H1 desktop |
| `text-6xl` | 60px | Hero title |

### 4.4 Tamanhos de banners (referência)

| Elemento | Peso | Tamanho |
|----------|------|---------|
| Headline principal | Plus Jakarta 800 ExtraBold | 30px+ (escala conforme banner) |
| Headline secundária | Plus Jakarta 700 Bold | 24px |
| Subtítulos | Plus Jakarta 600 SemiBold | 20px |
| Eyebrow / chamada superior | DM Sans 500 / Plus Jakarta 600 | 13–18px |
| Logo da marca | Plus Jakarta 700 Bold | — |
| Números e KPIs em destaque | Plus Jakarta 700 Bold | 28px |
| Subheadline / parágrafos | DM Sans 400 Regular | 14–16px |
| Texto do botão CTA | DM Sans 600 SemiBold | 14px |
| Badges e selos informativos | DM Sans 500 Medium | 12px |
| Rodapé / disclaimers | DM Sans 400 Regular | 12px |

---

## 5. SPACING SCALE

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
  padding-top: 4rem;    /* py-16 mobile */
  padding-bottom: 4rem;
}
@media (min-width: 768px) {
  .section-budamix {
    padding-top: 6rem;  /* py-24 desktop */
    padding-bottom: 6rem;
  }
}
```

---

## 6. SHADOW SCALE

| Token | Uso |
|-------|-----|
| `shadow-budamix-sm` | Cards em repouso, inputs |
| `shadow-budamix-md` | Cards em hover, dropdowns |
| `shadow-budamix-lg` | Modais, sidebars, elementos flutuantes |

> Todos os shadows usam `hsl(var(--foreground))` com opacidade baixa pra integração com modo escuro.

---

## 7. BORDER RADIUS

| Token | Value | Computed |
|-------|-------|----------|
| `--radius` | `0.5rem` | 8px (base) |
| `rounded-sm` | `calc(var(--radius) - 4px)` | 4px |
| `rounded-md` | `calc(var(--radius) - 2px)` | 6px |
| `rounded-lg` | `var(--radius)` | 8px |
| `rounded-xl` | — | 12px |
| `rounded-2xl` | — | 16px |
| `rounded-3xl` | — | 24px |
| `rounded-full` | — | 9999px (pills, avatars, CTAs banner) |

---

## 8. COMPONENTES — BUTTON

| Variant | Background | Foreground | Use case |
|---------|------------|------------|----------|
| `default` | primary | white | CTA principal |
| `secondary` | secondary | grafite | Ação secundária |
| `accent` | accent | white | Promoções, urgência |
| `outline` | transparent | foreground | Ação terciária |
| `ghost` | transparent | foreground | Nav, ações discretas |
| `link` | transparent | primary | Links inline |

---

## 9. COMPONENTES — BADGE

| Variant | Use case |
|---------|----------|
| `default` | Status geral |
| `secondary` | Categoria, tag |
| `accent` | Promoção, sale |
| `gold` | Premium, bestseller, rating |
| `outline` | Tag discreta |

---

## 10. LOGOTIPO

- Nome **BUDAMIX** em caixa alta
- Fonte: Plus Jakarta Sans 700 Bold
- Letter-spacing: amplo
- **"BUDA"** em branco `#FFFFFF` + **"MIX"** em dourado `#C7A35A`
- (em fundo claro, inverter: BUDA em grafite + MIX em dourado)
- Acompanha ícone simples de pote à esquerda — fundo dourado, bordas arredondadas, silhueta do pote em grafite
- Posicionado sempre no canto superior esquerdo ou superior central do bloco de copy
- **Nunca** com efeitos de gradiente/sombra/3D no símbolo

---

## 11. BOTÃO CTA — BANNERS DE MARKETING

- Fonte: DM Sans 600 SemiBold, caixa alta
- Letter-spacing: 0.12–0.16em (médio-amplo)
- Formato: pílula (border-radius total, ~100px)
- Fundo: **Terracotta `#C56A4A`** com sombra suave em terracota embaixo
- Ícone de seta à direita dentro de círculo semitransparente branco
- Exemplos de copy: `VER COLEÇÃO` / `COMPRAR AGORA` / `CONFERIR` / `QUERO O MEU`

---

## 12. DNA VISUAL — BANNERS E REELS

### 12.1 Regras de produto (potes de vidro)

- **Protagonistas visuais** do banner — sempre em destaque
- Aparecem com efeito de **vidro translúcido** (reflexos sutis, não fosco)
- **Tampas em teal escuro `#004D4D`** com aro em sage `#7EADAD`
- Podem conter conteúdo interno visível: grãos, especiarias, ervas, cereais, frutas secas
- Mostrar **variação de tamanhos** (pequeno + médio + grande) quando possível
- Pote central/maior levemente **elevado ou em maior escala**
- Sombra suave abaixo dos potes para ancorar no espaço

### 12.2 Variáveis de layout (intercambiáveis)

**1. Divisão do espaço**
- 40% copy / 60% produto (mais produto)
- 50% / 50% (equilíbrio)
- 60% copy / 40% produto (storytelling)
- Copy centralizado com produto em overlay (full-width)
- Produto centro + copy em faixa inferior (square / vertical)

**2. Posição do produto**
- Agrupados lado a lado, frontal
- Pote grande centralizado + dois menores apoiando
- Close-up na tampa (detalhe de qualidade)
- Vista aérea / flatlay sobre superfície clean
- Em mão de pessoa (lifestyle real)
- Sobre bancada de mármore/madeira clara com ingredientes

**3. Fundo**
- Grafite escuro `#132525` com gradiente radial teal central (noturno)
- Areia clara `#F7F4EF` (diurno e leve)
- Teal escuro `#004D4D` uniforme
- Porcelana `#D9E6E6` (suave/delicado)
- Foto real de ambiente (cozinha clean, despensa, bancada de pedra)

**4. Decoração (sutil — nunca compete com produto)**
- Anéis concêntricos finos semitransparentes (dourado/sage)
- Grade de pontos dourado
- Formas orgânicas abstratas (pétalas, arcos)
- Linhas paralelas diagonais finas
- Arcos cortados pelas bordas (sensação de abundância)
- Nenhum (versão minimalista)

**5. Badges e selos flutuantes**
- "100% Hermético" em dourado com ponto verde
- "+3× mais durabilidade"
- "Livre de BPA" em verde `#18794E`
- Ícone de vedação com check verde
- Nenhum (versão clean)

**6. Conteúdo dentro dos potes**
- Cereais e granola (dourado quente)
- Ervas e especiarias (verde)
- Grãos coloridos: feijão, lentilha (terroso)
- Frutas secas e nuts (marrom âmbar)
- Vazio / transparente (foco no design do vidro)
- Café em grãos (marrom escuro premium)
- Doces e confeitos coloridos (alegre)

**7. Ângulos emocionais de copy**

| Ângulo | Exemplo de Headline |
|--------|---------------------|
| Organização | "A casa organizada começa **pelo que você guarda**" |
| Preservação | "Feito para durar — **e para impressionar**" |
| Qualidade | "Vidro que **eleva qualquer cozinha**" |
| Praticidade | "Guardar nunca foi **tão bonito assim**" |
| Presente / Gifting | "O presente que toda **casa merece receber**" |
| Sustentabilidade | "Menos descartável. **Mais inteligente.**" |
| Bem-estar | "Cuide do que você come — **com vidro que respeita**" |
| Lançamento | "Chegou a coleção que **sua despensa esperava**" |

### 12.3 Prompt base para IA generativa de banners

```
Crie um banner horizontal de produto para a marca Budamix,
especializada em potes herméticos de vidro premium.

LAYOUT: [Variável 1]
PRODUTO: [Variável 2]
FUNDO: [Variável 3]
DECORAÇÃO: [Variável 4]
BADGES: [Variável 5]
CONTEÚDO DO POTE: [Variável 6]

PALETA OBRIGATÓRIA:
- Teal #004D4D → fundo dominante e tampas
- Grafite #132525 → fundo secundário
- Dourado #C7A35A → destaque tipográfico e badges
- Terracota #C56A4A → botão CTA exclusivamente
- Sage #7EADAD → textos de apoio e bordas
- Porcelana #D9E6E6 → texto secundário

TIPOGRAFIA:
- Títulos: Plus Jakarta Sans (800 ExtraBold para headline,
  600 SemiBold para eyebrow)
- Corpo e CTA: DM Sans (400 Regular para subheadline,
  600 SemiBold para botão)
- Eyebrow em DM Sans 500 Medium, cor sage #7EADAD,
  caixa alta, letter-spacing amplo, precedido por traço
  horizontal dourado curto (18–22px)
- Palavra de destaque da headline em Plus Jakarta Sans
  800 ExtraBold, cor dourada #C7A35A

COPY:
- Eyebrow: "[insira]"
- Headline: "[insira — destaque a palavra mais emocional
   em dourado #C7A35A]"
- Subheadline: "[insira]"
- CTA: botão pílula terracota #C56A4A com texto "[insira]"

LOGO: "BUDAMIX" em Plus Jakarta Sans 700 Bold, caixa alta,
letter-spacing amplo. "BUDA" em branco + "MIX" em dourado
#C7A35A. Ícone de pote simples à esquerda com fundo dourado
arredondado.

ÂNGULO EMOCIONAL: [Variável 7]

ESTILO GERAL: elegante, premium, clean, organizado.
Sem poluição visual. Hierarquia clara entre copy e produto.
Produto é sempre o protagonista do bloco de produto.
```

---

## 13. CORES POR MARKETPLACE

> Para dashboards, relatórios e visualizações cross-marketplace. Consistente em todos os relatórios HTML/Excel internos.

| Plataforma | Cor | Uso |
|------------|-----|-----|
| **Shopee** | `#4CAF50` | Verde — gráficos, badges, headers de seção Shopee |
| **Mercado Livre** | `#42A5F5` | Azul — idem para ML |
| **Amazon** | `#AB47BC` | Roxo — idem para Amazon |

---

## 14. INCONSISTÊNCIAS DOCUMENTADAS

> Pontos onde a marca tem variações conhecidas — registrar pra reconciliar futuramente.

| # | Tema | Divergência | Status |
|---|------|-------------|--------|
| 1 | **Teal** primário | Brand oficial = `#004D4D` · `skills/marketplace/.../paleta-cores.md` (relatórios ML) usa `#174C4C` | Marcado como "⚠️ paleta provisória" no doc do relatório — confirmar com Pedro pra alinhar. Brand fica `#004D4D` |
| 2 | **Body font** | E-commerce = Plus Jakarta Sans · Banners DNA = DM Sans | Ambos válidos por contexto: e-commerce evoluiu pra Plus Jakarta em 16/04/2026 (decisão); banners mantêm DM Sans pelo DNA original |
| 3 | **Heading font** | E-commerce = Bricolage Grotesque · Banners DNA = Plus Jakarta Sans | Mesma lógica do #2 |
| 4 | **Verde aprovação** `#18794E` | Existe no DNA banners, **não tokenizado** no DESIGN-TOKENS do e-commerce | Adicionar como `--success` customizado se for usar em badges do site (hoje `--success` é genérico HSL) |

---

## 15. FONTES

Documentos consultados pra montar este consolidado:

| Fonte | Path | Conteúdo |
|-------|------|----------|
| **DESIGN-TOKENS.md v1.1** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/design/DESIGN-TOKENS.md` | Tokens HSL + Tailwind do e-commerce (16/04/2026) |
| **DNA Visual** | `~/Documents/07-Conteudo-Marketing/REELS-BUDAMIX/budamix-dna-visual.md` | Regras pra banners, reels e geração de conteúdo |
| **index.css** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/src/index.css` | CSS variables HSL canônicas |
| **tailwind.config.ts** | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/tailwind.config.ts` | Mapeamento fonte/cor pra utilities |
| **MOC** | `~/segundo-cerebro/meta/mocs/MOC - Design Systems Budamix.md` | Hub de 3 design systems (Report HTML, Excel, Frontend) + skills de visualização |
| **Ficha do projeto** | `~/segundo-cerebro/projects/budamix-ecommerce.md` § Design System | Histórico de decisões |
| **PDF módulo identidade** | `~/Documents/07-Conteudo-Marketing/REELS-BUDAMIX/modulo-03-identidade.pdf` | Identidade visual original (não consumido neste doc) |
| **Paleta institucional** | `~/Documents/04-Empresa/Paleta de cores e Descrição.docx` | Referência institucional (não consumido neste doc) |

---

*Documento consolidado em 28/04/2026 a partir de 8 fontes distintas. Revisar trimestralmente conforme evolução da marca.*

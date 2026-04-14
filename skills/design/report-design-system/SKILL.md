# Design System — Relatórios OpenClaw (Curso)

> Usado por [[openclaw/agents/trader/IDENTITY|Trader]]

> Extraído minuciosamente dos materiais: Módulo 4 (Memória) e Módulo 5 (Web Search)
> Para uso como referência na geração de relatórios HTML pelo agente Tobias.

---

## 1. FUNDAÇÃO VISUAL

### Filosofia
Dark mode editorial. Estética de dashboard premium, não de blog. Cada seção é um "card" ou bloco visual distinto. O fundo escuro faz os destaques de cor brilharem. A informação é hierarquizada visualmente — o olho sabe para onde ir.

### Tema de Cores (Tokens)

```css
:root {
  /* ── Backgrounds ── */
  --bg-page:          #0a0b10;       /* fundo principal da página */
  --bg-card:          #12131a;       /* fundo dos cards/seções */
  --bg-card-elevated: #1a1b25;       /* cards com hover ou destaque */
  --bg-code:          #0d0e14;       /* blocos de código */
  --bg-hero:          linear-gradient(135deg, #0a0b10 0%, #151628 50%, #0a0b10 100%);

  /* ── Bordas ── */
  --border-default:   #1e2030;       /* bordas sutis de cards */
  --border-accent:    #2a2d45;       /* bordas com mais presença */

  /* ── Texto ── */
  --text-primary:     #e8e9ed;       /* texto principal (quase branco) */
  --text-secondary:   #8b8d9e;       /* texto secundário / labels */
  --text-muted:       #5a5c6e;       /* texto terciário / metadata */

  /* ── Cores de Acento ── */
  --accent-purple:    #8b5cf6;       /* CTA principal, títulos hero, badges */
  --accent-purple-dim:#6d42d4;       /* hover state do purple */
  --accent-cyan:      #22d3ee;       /* bordas de destaque, tags, links técnicos */
  --accent-cyan-dim:  #0ea5c7;       /* hover state do cyan */
  --accent-green:     #22c55e;       /* status positivo, checkmarks ✅ */
  --accent-yellow:    #eab308;       /* warnings, atenção ⚠️ */
  --accent-red:       #ef4444;       /* erro, negativo ❌ */
  --accent-orange:    #f97316;       /* destaque quente, CTAs secundários */
  --accent-pink:      #ec4899;       /* badges especiais, bônus */

  /* ── Cores dos Section Numbers (círculos numerados) ── */
  --section-1:        #22c55e;       /* verde */
  --section-2:        #3b82f6;       /* azul */
  --section-3:        #f97316;       /* laranja */
  --section-4:        #ef4444;       /* vermelho */
  --section-5:        #8b5cf6;       /* roxo */

  /* ── Gradientes Especiais ── */
  --gradient-card-border-top-cyan:    linear-gradient(90deg, #22d3ee 0%, #0ea5c7 100%);
  --gradient-card-border-top-orange:  linear-gradient(90deg, #f97316 0%, #ef4444 100%);
  --gradient-card-border-top-green:   linear-gradient(90deg, #22c55e 0%, #3b82f6 100%);
  --gradient-card-border-top-purple:  linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%);
  --gradient-card-border-top-rainbow: linear-gradient(90deg, #22c55e, #3b82f6, #8b5cf6, #ec4899, #f97316);
}
```

### Tipografia

```css
/* Fonte principal — sans-serif limpa e moderna */
body {
  font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 16px;
  line-height: 1.7;
  color: var(--text-primary);
  -webkit-font-smoothing: antialiased;
}

/* Títulos — peso forte, tracking apertado */
h1 {
  font-size: 2.75rem;    /* ~44px — hero title */
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.02em;
}

h2 {
  font-size: 1.75rem;    /* ~28px — section title */
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

h3 {
  font-size: 1.25rem;    /* ~20px — subsection */
  font-weight: 600;
  line-height: 1.4;
}

/* Labels / Overlines (ex: "CASO DE USO #1", "GRÁTIS · NATIVO") */
.overline {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-secondary);
}

/* Código inline */
code {
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
  font-size: 0.875rem;
  background: var(--bg-code);
  padding: 2px 8px;
  border-radius: 4px;
  color: var(--accent-cyan);
}

/* Blocos de código */
pre {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.85rem;
  line-height: 1.6;
  background: var(--bg-code);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 24px;
  overflow-x: auto;
}
```

---

## 2. COMPONENTES

### 2.1 — Hero Section (topo da página)

Fundo com gradiente sutil escuro. Contém:
1. **Badges** no topo (tags coloridas): ex: `🧶 CURSO OPENCLAW` | `🌐 MÓDULO 5 · INTEGRAÇÕES` | `✅ NATIVO + AVANÇADO`
2. **Título grande** (h1, 2.75rem, bold 800) — parte do título pode ser colorida em `--accent-purple`
3. **Subtítulo** descritivo (text-secondary, 1.1rem)
4. **Stats row** — 3-4 números grandes com labels pequenos embaixo

```css
.hero {
  background: var(--bg-hero);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: 48px 40px;
  margin-bottom: 48px;
}

.hero-badges {
  display: flex;
  gap: 12px;
  margin-bottom: 32px;
}

.badge {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 20px;
  border: 1px solid var(--border-accent);
  background: rgba(139, 92, 246, 0.1);  /* varia por cor */
}

.hero h1 span.highlight {
  color: var(--accent-purple);
}

.stats-row {
  display: flex;
  gap: 48px;
  margin-top: 32px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--accent-cyan);  /* ou green, purple — varia */
}

.stat-label {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-muted);
}
```

### 2.2 — Section Headers (divisores de seção)

Cada seção tem:
1. **Número em círculo colorido** (40px, cor cheia, texto branco, bold)
2. **Título em caps** com tracking largo ao lado do número
3. **Linha horizontal** sutil (`--border-default`) que se estende até o final

```css
.section-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 56px 0 32px;
}

.section-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.1rem;
  color: white;
  flex-shrink: 0;
  /* background varia: --section-1 a --section-5 */
}

.section-title {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-secondary);
  white-space: nowrap;
}

.section-line {
  flex: 1;
  height: 1px;
  background: var(--border-default);
}
```

### 2.3 — Cards Padrão

Cards com fundo `--bg-card`, borda sutil, border-radius grande. Padding generoso.

```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 24px;
}
```

### 2.4 — Cards com Borda Colorida no Topo

Usados para "Caso de uso", features lado a lado. Borda de 3px no topo com gradiente.

```css
.card-top-accent {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: 32px;
  position: relative;
  overflow: hidden;
}

.card-top-accent::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-card-border-top-cyan); /* varia */
}
```

### 2.5 — Cards com Borda Esquerda (callouts de destaque)

Usados para dicas, informações, avisos. Borda left de 3-4px colorida.

```css
/* Variante: Info/Dica (cyan/verde) */
.callout-info {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-left: 4px solid var(--accent-cyan);
  border-radius: 12px;
  padding: 24px 28px;
}

/* Variante: Warning (amarelo) */
.callout-warning {
  border-left-color: var(--accent-yellow);
}

/* Variante: Error/Importante (vermelho) */
.callout-danger {
  border-left-color: var(--accent-red);
}

/* Variante: Success (verde) */
.callout-success {
  border-left-color: var(--accent-green);
}
```

### 2.6 — Alert Boxes (com ícone + título bold)

Blocos tipo "⚠️ Problema real", "💡 Sem configurar nada", "✅ Fix de Março 2026", "🚨 O maior erro dos iniciantes".

```css
.alert-box {
  background: var(--bg-card-elevated);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 24px 28px;
}

.alert-box .alert-title {
  font-weight: 700;
  font-size: 1.05rem;
  margin-bottom: 8px;
  /* cor do título varia: */
  /* ⚠️ warning → --accent-yellow */
  /* 💡 dica → --accent-green */
  /* ✅ success → --accent-green */
  /* 🚨 danger → --accent-red */
}

.alert-box .alert-body {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.7;
}
```

### 2.7 — Tabelas Comparativas

Fundo escuro, header mais escuro, células com cores de destaque nos valores.

```css
table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  overflow: hidden;
}

thead {
  background: rgba(0, 0, 0, 0.3);
}

th {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-muted);
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid var(--border-default);
}

td {
  padding: 16px 20px;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border-default);
  font-size: 0.95rem;
}

tr:last-child td {
  border-bottom: none;
}

/* Valores destacados nas tabelas (ex: "2.000/mês grátis", "Completo") */
td.highlight-cyan   { color: var(--accent-cyan); font-weight: 600; }
td.highlight-green   { color: var(--accent-green); font-weight: 600; }
td.highlight-purple  { color: var(--accent-purple); font-weight: 600; }
td.highlight-yellow  { color: var(--accent-yellow); font-weight: 600; }
```

### 2.8 — Feature Cards Side-by-Side

Dois cards lado a lado com ícone, tag overline, nome da feature, descrição e bullets de checkmarks.

```css
.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.feature-card {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: 32px;
  position: relative;
  overflow: hidden;
}

/* A borda top pode ser cyan para um, orange para outro */
.feature-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
}

.feature-card .icon {
  font-size: 2rem;
  margin-bottom: 16px;
}

.feature-card .tag {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 12px;
}

/* Tags coloridas */
.tag-red    { background: rgba(239,68,68,0.15); color: var(--accent-red); border: 1px solid rgba(239,68,68,0.3); }
.tag-cyan   { background: rgba(34,211,238,0.1); color: var(--accent-cyan); border: 1px solid rgba(34,211,238,0.3); }
.tag-green  { background: rgba(34,197,94,0.1); color: var(--accent-green); border: 1px solid rgba(34,197,94,0.3); }
.tag-purple { background: rgba(139,92,246,0.1); color: var(--accent-purple); border: 1px solid rgba(139,92,246,0.3); }

.feature-card .name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  padding: 2px 8px;
  background: rgba(139,92,246,0.15);  /* highlight sutil */
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 12px;
}

.feature-card .check-list {
  list-style: none;
  padding: 0;
}

.feature-card .check-list li::before {
  content: '✅ ';
}
```

### 2.9 — Steps (Passos Numerados)

Círculos menores com número + título bold + descrição.

```css
.step {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  padding: 24px 0;
  border-bottom: 1px solid var(--border-default);
}

.step:last-child {
  border-bottom: none;
}

.step-number {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--accent-purple);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1rem;
  flex-shrink: 0;
}

.step-title {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.step-body {
  color: var(--text-secondary);
  font-size: 0.95rem;
}
```

### 2.10 — Stat Cards / Big Numbers

Número grande + label pequeno embaixo. Usado na hero e em seções de destaque como preço do Perplexity.

```css
.big-stat {
  text-align: left;
}

.big-stat .number {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1;
  color: var(--accent-purple);  /* ou cyan, green — varia */
}

.big-stat .label {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-top: 4px;
}
```

### 2.11 — Do/Don't Cards (lado a lado)

Card vermelho (❌ NÃO FUNCIONA) e card verde (✅ FUNCIONA) lado a lado. Fundo do card levemente tintado.

```css
.dont-card {
  background: rgba(239, 68, 68, 0.06);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 12px;
  padding: 24px;
}

.do-card {
  background: rgba(34, 197, 94, 0.06);
  border: 1px solid rgba(34, 197, 94, 0.2);
  border-radius: 12px;
  padding: 24px;
}

.dont-card .label {
  color: var(--accent-red);
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.do-card .label {
  color: var(--accent-green);
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 16px;
}
```

### 2.12 — Code Snippets Inline

Nomes técnicos como `web_search`, `web_fetch`, `memory_search` aparecem com highlight:

```css
code.tool-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  background: rgba(139, 92, 246, 0.15);  /* fundo roxo sutil */
  color: var(--accent-cyan);
  padding: 3px 10px;
  border-radius: 4px;
  font-weight: 600;
}
```

### 2.13 — Resumo Final (grid de conceitos)

Grid 2x3 com conceitos-chave. Cada item tem título colorido e descrição curta.

```css
.summary-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: 40px;
}

.summary-item .title {
  font-weight: 700;
  color: var(--accent-purple);  /* ou cyan */
  margin-bottom: 8px;
}

.summary-item .desc {
  color: var(--text-secondary);
  font-size: 0.95rem;
}
```

### 2.14 — Footer

```css
.footer {
  text-align: center;
  padding: 48px 0;
  border-top: 1px solid var(--border-default);
  margin-top: 64px;
}

.footer .brand {
  font-weight: 700;
  color: var(--text-primary);
}

.footer .sub {
  color: var(--text-muted);
  font-size: 0.85rem;
}
```

### 2.15 — Bônus / Destaque Especial

Card com fundo diferenciado (gradiente mais quente), badge "🎁 BÔNUS EXCLUSIVO", título grande com parte colorida.

```css
.bonus-section {
  background: linear-gradient(135deg, #1a1020 0%, #12131a 100%);
  border: 1px solid rgba(236, 72, 153, 0.2);
  border-radius: 16px;
  padding: 48px 40px;
}

.bonus-badge {
  display: inline-block;
  background: rgba(236, 72, 153, 0.15);
  border: 1px solid rgba(236, 72, 153, 0.3);
  color: var(--accent-pink);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 20px;
  margin-bottom: 24px;
}
```

---

## 3. PADRÕES DE LAYOUT

### Largura e Espaçamento

```css
.page-container {
  max-width: 860px;       /* conteúdo estreito, editorial */
  margin: 0 auto;
  padding: 40px 24px;
}

/* Espaçamento entre seções */
section + section {
  margin-top: 64px;
}

/* Espaçamento entre cards */
.card + .card {
  margin-top: 24px;
}

/* Grid 2 colunas para feature cards / comparações */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
```

### Hierarquia Visual (ordem de leitura)

1. **Hero** — título + subtítulo + stats
2. **Seção** — número + título + linha
3. **Corpo** — parágrafo ou callout explicativo
4. **Cards** — componentes visuais (features, steps, tabelas)
5. **Alert** — dicas ou warnings dentro de seção
6. **Footer** — rodapé com créditos

---

## 4. ÍCONES E EMOJIS (USO CONSISTENTE)

| Contexto | Emoji |
|----------|-------|
| Busca/pesquisa | 🔍 |
| Documento/arquivo | 📄 |
| Dica/insight | 💡 |
| Warning/atenção | ⚠️ |
| Erro/perigo | 🚨 |
| Sucesso/ok | ✅ |
| Negativo/errado | ❌ |
| Parcial/incompleto | ⚠️ (amarelo) |
| Cérebro/IA | 🧠 |
| Dinheiro/custo | 💰 |
| Foguete/dica pro | 🚀 |
| Presente/bônus | 🎁 |
| Exercício/alvo | 🎯 |
| Estrela/destaque | ⭐ |
| Livro/curso | 📚 |
| Engrenagem/config | ⚙️ |
| Raio/rápido | ⚡ |
| Gráfico/dados | 📊 |
| Notícia | 📰 |
| Pasta/arquivo | 🗂 |
| Espião/monitorar | 🕵 |

---

## 5. REGRAS DE COMPOSIÇÃO

1. **Nunca texto solto direto na página** — sempre dentro de um card, callout ou seção demarcada
2. **Títulos hero sempre têm uma palavra/frase em cor** — destaca o conceito-chave
3. **Tabelas sempre dentro de cards** — nunca flutuando
4. **Máximo 2 colunas** — nunca 3+ (exceto stats row no hero)
5. **Code inline sempre em monospace com highlight** — nunca texto normal
6. **Cada seção tem cor de número diferente** — rota pelas 5 cores
7. **Cards lado a lado sempre com borda-top colorida** — diferencia visualmente
8. **Alerts nunca empilhados** — máximo 1 por sub-seção
9. **Blocos de código sempre com border-radius 12px** — cantos arredondados
10. **Border-radius padrão: 16px para cards, 12px para elementos menores, 20px para badges**

---

## 6. TEMPLATE HTML COMPLETO (ESQUELETO)

Abaixo, o esqueleto que o Tobias deve seguir para gerar qualquer relatório:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[TÍTULO DO RELATÓRIO] | OpenClaw</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    /* Colar aqui todas as CSS variables e estilos do design system */
    /* ... (usar tokens acima) ... */
  </style>
</head>
<body>
  <div class="page-container">

    <!-- HERO -->
    <section class="hero">
      <div class="hero-badges">
        <span class="badge badge-purple">🧶 CURSO OPENCLAW</span>
        <span class="badge badge-cyan">🌐 MÓDULO X · NOME</span>
        <span class="badge badge-green">✅ STATUS</span>
      </div>
      <h1>Título Principal:<br><span class="highlight">Parte Destacada</span></h1>
      <p class="subtitle">Subtítulo descritivo da aula/relatório.</p>
      <div class="stats-row">
        <div class="stat"><span class="stat-number">Valor</span><span class="stat-label">LABEL</span></div>
        <!-- repetir -->
      </div>
    </section>

    <!-- SEÇÃO N -->
    <div class="section-header">
      <div class="section-number" style="background: var(--section-1)">1</div>
      <span class="section-title">TÍTULO DA SEÇÃO</span>
      <div class="section-line"></div>
    </div>

    <section>
      <div class="card">
        <!-- conteúdo -->
      </div>
    </section>

    <!-- ALERT -->
    <div class="alert-box">
      <div class="alert-title" style="color: var(--accent-green)">💡 Título do Alert</div>
      <div class="alert-body">Corpo do alert com informação complementar.</div>
    </div>

    <!-- TABELA -->
    <div class="card">
      <table>
        <thead><tr><th>COL 1</th><th>COL 2</th><th>COL 3</th></tr></thead>
        <tbody>
          <tr><td>valor</td><td class="highlight-cyan">destaque</td><td>valor</td></tr>
        </tbody>
      </table>
    </div>

    <!-- GRID 2 COLUNAS -->
    <div class="two-col">
      <div class="card-top-accent" style="--accent: var(--gradient-card-border-top-cyan)">
        <!-- card 1 -->
      </div>
      <div class="card-top-accent" style="--accent: var(--gradient-card-border-top-orange)">
        <!-- card 2 -->
      </div>
    </div>

    <!-- STEPS -->
    <div class="card">
      <div class="step">
        <div class="step-number">1</div>
        <div>
          <div class="step-title">Título do Passo</div>
          <div class="step-body">Descrição do passo.</div>
        </div>
      </div>
    </div>

    <!-- BÔNUS -->
    <section class="bonus-section">
      <span class="bonus-badge">🎁 BÔNUS EXCLUSIVO</span>
      <h2>Título do <span style="color: var(--accent-green)">Bônus</span></h2>
      <p>Descrição do bônus.</p>
    </section>

    <!-- RESUMO -->
    <div class="section-header">
      <span class="section-title">RESUMO</span>
      <div class="section-line"></div>
    </div>
    <div class="summary-grid">
      <div class="summary-item">
        <div class="title">Conceito 1</div>
        <div class="desc">Descrição curta.</div>
      </div>
      <!-- repetir -->
    </div>

    <!-- FOOTER -->
    <footer class="footer">
      <p><span class="brand">🧶 Curso OpenClaw</span> · Módulo X — Nome</p>
      <p class="sub">Material produzido para founders de Micro-SaaS</p>
    </footer>

  </div>
</body>
</html>
```

---

## 7. CHECKLIST PARA O TOBIAS

Antes de entregar qualquer relatório HTML, verificar:

- [ ] Fundo da página é `#0a0b10` (escuro)
- [ ] Todos os cards têm `border-radius: 16px`
- [ ] Fonte Inter carregada via Google Fonts
- [ ] Código usa JetBrains Mono
- [ ] Cada seção tem número em círculo colorido
- [ ] Hero tem badges, título com highlight, stats
- [ ] Tabelas estão dentro de cards
- [ ] Alerts têm ícone + título bold + corpo secondary
- [ ] Nenhum texto solto fora de componente
- [ ] Max-width do container: ~860px
- [ ] Todas as cores seguem os tokens definidos
- [ ] Border-top colorido nos cards de feature
- [ ] Code inline com fundo sutil e cor cyan
- [ ] Footer com créditos centralizados

---

## Ver também

- [[skills/marketplace/consolidado-financeiro/SKILL|Consolidado Financeiro — Skill]]

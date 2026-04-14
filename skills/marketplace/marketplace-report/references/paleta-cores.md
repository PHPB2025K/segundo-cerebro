---
title: "paleta cores"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Paleta de Cores — Budamix / GB Importadora

Identidade visual do relatório ML. Baseada na assinatura visual da GB Importadora.

> ⚠️ Paleta provisória — Pedro vai confirmar antes de consolidar.

---

## Cores Principais

| Nome | Hex | Uso |
|---|---|---|
| **Primária** | `#174C4C` | Header, títulos de seção, borders de destaque |
| **Secundária** | `#1A6B6B` | Sub-headers, gradientes, hover states |

## Cores de Acento

| Nome | Hex | Uso |
|---|---|---|
| **Positivo** | `#2E7D32` | KPIs em alta, métricas boas, badges verdes |
| **Negativo** | `#C62828` | KPIs em queda, alertas críticos, badges vermelhos |
| **Alerta** | `#F57F17` | Atenção moderada, warnings, badges amarelos |
| **Destaque** | `#0277BD` | Informações neutras, links, badges azuis |

## Neutros

| Nome | Hex | Uso |
|---|---|---|
| **Fundo cards** | `#F5F5F5` | Background de cards KPI |
| **Fundo zebra** | `#FAFAFA` | Linhas pares de tabela |
| **Texto primário** | `#212121` | Corpo de texto principal |
| **Texto secundário** | `#757575` | Labels, legendas, texto de suporte |
| **Borda** | `#E0E0E0` | Bordas de cards e tabelas |
| **Branco** | `#FFFFFF` | Fundo geral, texto em fundos escuros |

---

## Uso por Componente

### Cards KPI
```css
background: #F5F5F5;
border-left: 4px solid #174C4C;
/* Variações por tipo:
   positivo: border-left-color: #2E7D32
   negativo: border-left-color: #C62828
   alerta:   border-left-color: #F57F17
*/
```

### Header de Seção
```css
background: #174C4C;
color: #FFFFFF;
```

### Tabelas
```css
/* Header */
background: #174C4C;
color: #FFFFFF;

/* Linha ímpar */
background: #FFFFFF;

/* Linha par (zebra) */
background: #FAFAFA;
```

### Boxes de Insight
```css
/* Positivo */
background: #E8F5E9;
border-left: 4px solid #2E7D32;

/* Atenção */
background: #FFF8E1;
border-left: 4px solid #F57F17;

/* Alerta */
background: #FFEBEE;
border-left: 4px solid #C62828;

/* Info */
background: #E3F2FD;
border-left: 4px solid #0277BD;
```

### Rodapé
```css
color: #757575;
border-top: 1px solid #E0E0E0;
font-size: 10px;
```

---

## Gráficos Matplotlib

Paleta de cores para séries em gráficos:

```python
CHART_COLORS = [
    '#174C4C',  # primária
    '#1A6B6B',  # secundária
    '#0277BD',  # azul destaque
    '#2E7D32',  # verde positivo
    '#F57F17',  # laranja alerta
    '#C62828',  # vermelho
    '#6A1B9A',  # roxo (extra)
    '#00838F',  # ciano (extra)
]
```

Fundo dos gráficos: transparente (`alpha=0.0`)
Grid: muito sutil (`#EEEEEE`, alpha=0.5)
Fonte: `DejaVu Sans` (padrão matplotlib) ou `sans-serif`

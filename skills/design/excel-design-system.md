---
title: "excel design system"
created: 2026-04-14
type: skill
domain: design
status: active
tags:
  - skill/design
---

# Excel Design System — GB Importadora

_Padrão visual obrigatório para todos os relatórios e extratos Excel._

## Paleta de Cores (Dark Mode)

| Elemento | Hex | Uso |
|---|---|---|
| Background principal | #1B2838 | Fundo de todas as células |
| Background alt (zebra light) | #1E2D3D | Linhas pares |
| Background alt (zebra dark) | #162435 | Linhas ímpares |
| Cabeçalho/Título | #174C4C | Headers de tabela, barra de título |
| Seções | #0D1B2A | Background de títulos de seção |
| Texto principal | #FFFFFF | Dados, labels |
| Texto secundário | #B0BEC5 | Subtítulos, descrições |
| Accent verde | #4CAF50 | Valores positivos, lucro, Shopee |
| Accent vermelho | #EF5350 | Valores negativos, taxas, perdas |
| Accent azul | #42A5F5 | Títulos de seção, destaques, ML |
| Accent amarelo | #FFC107 | Percentuais, rankings |
| Accent roxo | #AB47BC | Amazon |
| Borda | #2C3E50 | Bordas sutis entre linhas |

## Fontes

| Elemento | Font | Tamanho | Estilo | Cor |
|---|---|---|---|---|
| Título principal | Calibri | 16pt | Bold | #FFFFFF |
| Subtítulo | Calibri | 10pt | Normal | #B0BEC5 |
| Título de seção | Calibri | 13pt | Bold | #42A5F5 |
| Header de tabela | Calibri | 10pt | Bold | #FFFFFF sobre #174C4C |
| Dados normais | Calibri | 10pt | Normal | #FFFFFF |
| Percentuais | Calibri | 10pt | Normal | #FFC107 |
| Valores negativos | Calibri | 10pt | Normal | #EF5350 |
| Valores positivos destacados | Calibri | 10pt | Bold | #4CAF50 |
| Rankings/posição | Calibri | 10pt | Bold | #FFC107 |

## Formatos Numéricos

| Tipo | Formato |
|---|---|
| Monetário | #,##0.00 |
| Percentual | 0.0% |
| Inteiro | #,##0 |
| Data | DD/MM/YYYY HH:MM |

## Regras de Layout

1. **TODAS as células devem ter background dark** — nenhuma célula branca/sem preenchimento
2. **Zebra striping** nas linhas de dados (alternando #1E2D3D e #162435)
3. **Merge cells** para títulos de seção (span full width)
4. **Column widths generosos** — nunca truncar texto
5. **Row heights** adequados para legibilidade (mínimo 20px para dados, 30px para seções, 40px para títulos)
6. **Bordas sutis** — thin, cor #2C3E50, apenas na parte inferior das linhas

## Ícones (Emoji nas células)

Usar emojis como identificadores visuais:
- 📊 📈 📋 🏪 → abas
- 💰 → valores monetários, bruto
- 📦 → pedidos, volume
- 🏷️ → taxas, comissões
- ✅ → valores líquidos, positivos
- ❌ → cancelamentos, negativos
- 🚚 → frete
- 📊 → percentuais
- 🎯 → ticket médio, metas
- 🏆 → rankings, top produtos
- 💳 → métodos de pagamento

## Gráficos (openpyxl.chart)

- **Cores por plataforma:** Shopee #4CAF50, ML #42A5F5, Amazon #AB47BC
- **Background:** transparente
- **Títulos:** branco quando possível
- **Tipos preferidos:** BarChart (comparativos), PieChart (participação %), LineChart (tendências)

## Aplicação

Este design system se aplica a:
- Extratos financeiros (ML, Shopee, Amazon)
- Relatórios consolidados
- Análises comparativas
- Qualquer Excel gerado pelas skills de marketplace

## Referência rápida openpyxl

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Paleta
BG_MAIN = PatternFill(start_color="1B2838", end_color="1B2838", fill_type="solid")
BG_ZEBRA_LIGHT = PatternFill(start_color="1E2D3D", end_color="1E2D3D", fill_type="solid")
BG_ZEBRA_DARK = PatternFill(start_color="162435", end_color="162435", fill_type="solid")
BG_HEADER = PatternFill(start_color="174C4C", end_color="174C4C", fill_type="solid")
BG_SECTION = PatternFill(start_color="0D1B2A", end_color="0D1B2A", fill_type="solid")

# Fonts
FONT_TITLE = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
FONT_SUBTITLE = Font(name="Calibri", size=10, color="B0BEC5")
FONT_SECTION = Font(name="Calibri", size=13, bold=True, color="42A5F5")
FONT_HEADER = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
FONT_DATA = Font(name="Calibri", size=10, color="FFFFFF")
FONT_PCT = Font(name="Calibri", size=10, color="FFC107")
FONT_NEGATIVE = Font(name="Calibri", size=10, color="EF5350")
FONT_POSITIVE = Font(name="Calibri", size=10, bold=True, color="4CAF50")
FONT_RANK = Font(name="Calibri", size=10, bold=True, color="FFC107")

# Border
BORDER_BOTTOM = Border(bottom=Side(style="thin", color="2C3E50"))

---

## Ver também

- [[skills/excel-generation/SKILL|Excel Generation — Skill]]
```

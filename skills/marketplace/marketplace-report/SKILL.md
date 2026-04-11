---
name: marketplace-report
description: Gerar relatórios profissionais de performance de marketplace com visual premium. Suporta Mercado Livre, Amazon e Shopee — individual ou unificado. Use quando Pedro pedir relatório de qualquer marketplace, análise de performance, métricas de vendas, conversão, reputação, ads ou comparativo entre plataformas. Suporta relatório completo (9 páginas), focado (seções específicas) e comparativo (entre períodos ou plataformas).
---

# Relatório de Performance — Marketplaces

> Usado por [[agents/trader/IDENTITY|Trader]]

Gera relatórios PDF profissionais para Mercado Livre, Amazon e Shopee.
Arquitetura modular: seções genéricas + connectors por plataforma.

## Uso

```bash
# Relatório ML completo
python3 {baseDir}/scripts/report-engine.py --plataforma ml --inicio 2026-03-01 --fim 2026-03-15

# Relatório Amazon
python3 {baseDir}/scripts/report-engine.py --plataforma amazon --inicio 2026-03-01 --fim 2026-03-15

# Seções específicas
python3 {baseDir}/scripts/report-engine.py --plataforma ml --inicio 2026-03-01 --fim 2026-03-15 --secoes 1,2,6

# Relatório unificado (todas as plataformas)
python3 {baseDir}/scripts/report-engine.py --plataforma all --inicio 2026-03-01 --fim 2026-03-15
```

## Parâmetros

| Param | Obrigatório | Default | Descrição |
|---|---|---|---|
| `--plataforma` | Sim | — | `ml`, `amazon`, `shopee` ou `all` |
| `--inicio` | Sim | — | Data inicial (YYYY-MM-DD) |
| `--fim` | Sim | — | Data final (YYYY-MM-DD) |
| `--secoes` | Não | `all` | Seções: `1,2,3` ou `all` |
| `--output` | Não | auto | Caminho do PDF |
| `--debug` | Não | false | Modo debug |

## Arquitetura

```
scripts/
├── report-engine.py          ← Orquestrador universal
├── charts.py                 ← Gráficos matplotlib (Budamix palette)
├── connectors/               ← Um por plataforma
│   ├── mercadolivre.py       ← API ML/MP → formato padrão
│   ├── amazon.py             ← API Amazon → formato padrão
│   └── shopee.py             ← API Shopee → formato padrão
└── sections/                 ← Seções genéricas (agnósticas de plataforma)
    ├── helpers.py            ← Formatação, badges, constantes
    ├── s01_capa.py
    ├── s02_faturamento.py
    ├── ...
    └── s09_estrategia.py
```

### Fluxo
1. Engine recebe `--plataforma` e `--secoes`
2. Carrega o connector da plataforma (ou todos se `all`)
3. Connector busca dados e retorna formato padrão
4. Seções recebem dados padronizados e geram HTML
5. Engine combina HTML → PDF

### Formato padrão de dados (todos os connectors retornam isso)
```python
{
    "platform": "mercadolivre",          # identificador
    "platform_display": "Mercado Livre", # nome pra exibição
    "orders": [...],                     # pedidos pagos
    "payments": [...],                   # pagamentos com taxas
    "seller_info": {...},                # reputação, nível
    "items": [...],                      # anúncios ativos
    "items_total": int,                  # total de anúncios
}
```

## Seções

| # | Seção | Dados necessários |
|---|---|---|
| 1 | Capa & Resumo Executivo | orders, payments, seller_info, items_total |
| 2 | Faturamento & Receita | orders, payments |
| 3 | Volume & Conversão | orders |
| 4 | Tráfego & Visibilidade | (placeholder) |
| 5 | Publicidade / Ads | (placeholder) |
| 6 | Reputação & Saúde | seller_info |
| 7 | Logística & Envios | orders |
| 8 | Catálogo & Anúncios | items, items_total |
| 9 | Insights & Plano de Ação | orders, payments, seller_info |

## Identidade visual

Ver `references/paleta-cores.md` para paleta Budamix completa.

## Connectors disponíveis

| Plataforma | Status | Tokens |
|---|---|---|
| Mercado Livre | ✅ Ativo | .ml-tokens*.json |
| Amazon | 🔜 Futuro | — |
| Shopee | 🔜 Futuro | — |

## Aprendizados Incorporados

<!-- MELHORIA 2026-03-16 -->
### CSS: wkhtmltopdf não suporta CSS Grid
Usar `display: table` + `table-cell` + `table-row` para layouts lado a lado.
CSS Grid (`grid-template-columns`) é ignorado pelo wkhtmltopdf.
<!-- /MELHORIA -->

<!-- MELHORIA 2026-03-16 -->
### Ícones: Não usar emojis em PDFs
wkhtmltopdf não renderiza emojis mesmo com fonts-noto-color-emoji.
Usar SVGs inline (módulo `sections/icons.py`) com stroke na cor da paleta.
Emojis são aceitáveis apenas em textos de insight/estratégia (renderizam como texto).
<!-- /MELHORIA -->

<!-- MELHORIA 2026-03-16 -->
### Cards KPI: Layout premium
- Ícone com badge (fundo arredondado) à ESQUERDA do valor
- Valor em fonte 12pt bold 800, white-space: nowrap (nunca quebrar linha)
- Label em 6.5pt uppercase com letter-spacing 0.8px
- Card primário: gradiente teal, ícone dourado
- Box-shadow sutil para profundidade
<!-- /MELHORIA -->

<!-- MELHORIA 2026-03-16 -->
### Gráficos: Visual premium
- Linhas suavizadas com scipy.interpolate (spline)
- Área preenchida com gradiente transparente (12% opacidade)
- Pontos com borda branca (scatter + edgecolors white)
- Pico destacado com callout dourado
- Barras do pico em cor dourada diferenciada
<!-- /MELHORIA -->

<!-- MELHORIA 2026-03-18 -->
### Output: HTML puro (sem wkhtmltopdf)
- report-engine.py refatorado: output direto em HTML, removida dependência de wkhtmltopdf
- CSS agora vem do template `templates/report-base.html` (não inline no Python)
- Design system dark mode (purple/cyan/green sobre fundo #0a0b10)
- Fontes: Inter (texto) + JetBrains Mono (código/dados)
- Se Pedro precisar de PDF, converte pelo browser (Ctrl+P)
- CSS antigo (light theme teal/areia) removido do engine — vive apenas no git history
<!-- /MELHORIA -->

---
## Referências
- [[skills/marketplace/marketplace-report/references/estrutura-relatorio|Estrutura do Relatório]]
- [[skills/marketplace/marketplace-report/references/paleta-cores|Paleta de Cores]]

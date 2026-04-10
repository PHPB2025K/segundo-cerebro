---
name: consolidado-financeiro
description: Gerar relatório consolidado financeiro de todos os marketplaces (Shopee + ML + Amazon) em HTML profissional + Excel. Use quando o Pedro pedir consolidado, extrato geral, visão unificada, comparativo financeiro entre plataformas ou relatório mensal dos marketplaces.
---

# Consolidado Financeiro — Marketplaces

Gera relatório HTML profissional (dark mode) + Excel consolidando dados financeiros de Shopee, Mercado Livre e Amazon.

## Uso

### Passo 1: Gerar extratos individuais
```bash
# Shopee (3 contas)
python3 skills/marketplace/shopee-extrato/scripts/shopee-extrato.py --inicio YYYY-MM-DD --fim YYYY-MM-DD --conta todas

# Mercado Livre
bash skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh finance
python3 skills/marketplace/ml-extrato/scripts/ml-extrato.py --inicio YYYY-MM-DD --fim YYYY-MM-DD

# Amazon
python3 skills/marketplace/amazon-extrato/scripts/amazon-extrato.py --inicio YYYY-MM-DD --fim YYYY-MM-DD
```

### Passo 2: Consolidar
Após gerar os 3 extratos, consolidar os dados e gerar:
1. **Excel** — `reports/consolidado-marketplaces-YYYY-MM.xlsx` (source of truth)
2. **HTML** — `reports/consolidado-marketplaces-YYYY-MM.html` (versão de consumo/apresentação)

## Estrutura do HTML (padrão aprovado)

### Design System
Usar obrigatoriamente: `templates/report-base.html` (CSS) + `skills/design/report-design-system/SKILL.md`
- Dark mode editorial, max-width: 1120px
- Fonte: Inter + JetBrains Mono (Google Fonts)
- Paleta: --bg-page #0a0b10, --bg-card #12131a, accents green/yellow/red/purple/cyan

### Seções (nesta ordem):

1. **Hero / Header**
   - Título: "Consolidado Financeiro — Marketplaces"
   - Subtítulo: "GB Importadora / Budamix • {Mês} {Ano} (DD/MM a DD/MM)"
   - 5 KPI cards: Faturamento Bruto, Receita Líquida, Total Pedidos, Margem Média, Total Taxas

2. **Comparativo Geral**
   - Tabela: Plataforma | Vendas | Bruto | Taxas | Líquido | Margem | % Taxas
   - Badges coloridos: Shopee (verde), ML (azul), Amazon (roxo)
   - Barras de progresso visuais (participação %)
   - Linha TOTAL em destaque

3. **Análise de Taxas**
   - Tabela comparativa por tipo de taxa (comissão, frete, FBA, etc.)
   - Highlight: qual plataforma cobra mais/menos por categoria

4. **Shopee — Detalhamento**
   - Sub-tabela: 3 contas lado a lado (Budamix Store, Oficial, Shop)
   - Métodos de pagamento com barras visuais

5. **Mercado Livre — Detalhamento**
   - Breakdown: vendas, fretes, reembolsos, disputas
   - Status de liquidação

6. **Amazon — Detalhamento**
   - Breakdown de fees (FBA vs Comissão)
   - Vendas, devoluções, ajustes

7. **Curva ABC — Operação Consolidada**
   - KPI cards: Classe A (x SKUs, 80%), Classe B, Classe C
   - Tabela Classe A com: #, Produto, SKU, Qtd, Bruto, %, Acum., Plataformas
   - Tabela Classe B resumida
   - Card Classe C com métricas resumidas
   - Insight card com análise do produto campeão

8. **Insights & Recomendações**
   - Cards com ícones e análise por plataforma
   - Recomendações acionáveis

### Formatação de Tabelas
- overflow-x: auto nos containers
- Font compacta (0.82rem) em tabelas densas
- Zebra striping via CSS
- white-space: nowrap em colunas numéricas
- Badges inline para plataformas (verde=Shopee, azul=ML, roxo=Amazon)

## Estrutura do Excel

### 4 abas:
1. **📊 Dashboard** — KPIs + tabela comparativa + gráficos (openpyxl.chart)
2. **📈 Análise de Taxas** — breakdown por plataforma
3. **🏪 Shopee Detalhado** — 3 contas + métodos + top produtos
4. **📋 Resumo Executivo** — insights + recomendações

### Formatação
Seguir `skills/design/excel-design-system.md` (dark mode)

## Curva ABC — Como calcular

1. Coletar produtos vendidos de Shopee (via order details) e Amazon (via metadata dos extratos)
2. Agrupar por SKU, somar qty e bruto
3. Ordenar por bruto decrescente
4. Calcular % individual e % acumulado
5. Classificar: A (≤80%), B (80-95%), C (>95%)

**Nota:** ML não tem dados de produto no extrato financeiro (payment-level). Usar apenas Shopee + Amazon para curva ABC.

## Entrega

Quando Pedro pedir "consolidado" ou "relatório dos marketplaces":
1. Rodar os 3 extratos individuais
2. Gerar Excel + HTML consolidados
3. Enviar o **HTML** como arquivo principal
4. Enviar o **Excel** como complemento
5. Incluir resumo no chat com tabela comparativa

<!-- MELHORIA 2026-03-22 -->
## v2.x — Evoluções implementadas (21/03)

### Margem por produto (v2.0+)
- Cruzamento Curva ABC × planilha de precificação (Google Sheets)
- Margem vem da **planilha**, NUNCA calculada por script
- Cada aba (SHOPEE, MELI, AMAZON) já considera todos os custos
- Margem final = **média ponderada por volume** em cada plataforma
- SKUs sem custo na planilha: marcar N/D e alertar

### Fluxo de caixa (v2.0+)
- Timeline semanal de liquidação por plataforma
- Mostra quando o dinheiro realmente cai na conta

### Alertas automáticos (v2.0+)
- Margem < 15% → 🔴 Crítico
- Margem 15-25% → 🟡 Atenção
- Zero alertas → card verde

### Tabelas compactas (v2.1)
- Remover coluna "Custo Total" (redundante)
- Nomes de produtos encurtados
- Badges compactas (SH, AMZ, ML)
- Font 0.76rem em tabelas densas
- Container expandido para 1280px

### Nomenclatura (v2.3)
- "Classe A/B/C" → "Curva A/B/C" em todo o relatório

### Script de enhancement
- `skills/marketplace/consolidado-financeiro/scripts/enhance-consolidado.py`
- Adiciona margem por produto, fluxo de caixa e alertas ao HTML base
<!-- /MELHORIA 2026-03-22 -->

## Referência
- Relatório modelo: `reports/consolidado-marketplaces-2026-03-v2.html`
- Excel modelo: `reports/consolidado-marketplaces-2026-03.xlsx`

---
title: "decisions"
created: 2026-04-14
type: agent
agent: trader
status: active
tags:
  - agent/trader
---

# Decisões — Trader

_Registro de decisões permanentes. NUNCA contradizer._

## Plataformas

### SKUs — Padronização (2026-03-21)
- **Shopee:** SKUs atualizados via API (budamix-store2 + budamix-shop). budamix-store pendente (token expirado na época)
- **Mercado Livre:** 14 anúncios com seller_custom_field atribuído (antes vazio). 5 kits não encontrados ativos
- **Amazon:** SKU é imutável — NÃO tentar renomear (perde histórico/ranking). Usar Apelido do SKU no Upseller
- **Upseller:** SKU do armazém é imutável — usar campo "Apelido do SKU" nos Produtos do Armazém

### Amazon Ads — Endpoint (2026-03-16)
- Brasil usa endpoint NA: `advertising-api.amazon.com` (endpoint SA não existe)

## Relatórios

### Design System (2026-03-16)
- Output de relatórios é HTML (não mais PDF)
- Sempre ler skill report-design-system antes de gerar relatório
- CSS nunca fica inline no Python — sempre no template
- Paleta: dark theme (purple/cyan/green sobre fundo `#0a0`10)

### Excel Design System (2026-03-20)
- Planilhas Excel seguem paleta dark mode definida em `skills/design/excel-design-system.md`

### Separação Financeiro vs Performance (2026-03-20)
- **Financeiro** = dinheiro (receita, custos, margens, fluxo de caixa) → skill consolidado-financeiro
- **Performance** = operação (vendas, conversão, ranking, ads, reputação) → skill marketplace-report
- Complementares, sem sobreposição
- Divergência de datas: financeiro usa data de liquidação, performance usa data de venda

### Formato de entrega (2026-03-20)
- Consolidado financeiro: SEMPRE gerar HTML + Excel juntos
- HTML para visualização rápida, Excel para análise detalhada
- Container HTML: 1120px (não 860px) para tabelas caberem
- Tabelas: font 0.76rem, compactas (v2.1+)

### Consolidado — Margem (2026-03-20)
- Cada aba (SHOPEE, MELI, AMAZON) já considera TODOS os custos individuais
- Margem consolidada = média ponderada por VOLUME de venda
- Se não tem dado de volume, usar plataforma indicada no relatório como 100%

### Curva ABC (2026-03-20)
- Remover Top 10 Shopee do consolidado
- Substituir por Curva ABC consolidada (3 plataformas)
- Posicionar após detalhamento das 3 plataformas, antes de Insights

## Operacional

### Team Agents (2026-03-19)
- Trader é agente especializado ML/Shopee/Amazon
- Coordenado pelo Kobe — nunca fala direto com Pedro
- Resultados sempre entregues ao Kobe para validação

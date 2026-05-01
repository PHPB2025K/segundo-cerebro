---
name: dre-profissional-marketplace
description: Gerar DRE gerencial profissional para marketplaces da GB Importadora/Budamix, consolidado e por marketplace, com margem bruta, operacional e líquida, CMV, Ads, taxas, premissas, Excel executivo e HTML moderno. Use SEMPRE que Pedro/Kobe pedir DRE, demonstrativo de resultado, P&L, resultado operacional, margem por canal, fechamento mensal financeiro, relatório financeiro executivo ou comparação de rentabilidade ML/Shopee/Amazon.
---

# DRE Profissional Marketplace — GB Importadora

> Usado pelo Trader para transformar dados financeiros corretos em entregável executivo de verdade.

## Regra de ativação

Use esta skill para qualquer DRE/fechamento financeiro mensal. Não basta gerar uma planilha de apuração; a entrega precisa parecer um relatório executivo profissional.

## Skills obrigatórias de apoio

Antes de gerar o output final, consultar/aplicar:

1. `skills/marketplace/consolidado-financeiro/SKILL.md` — coleta/conciliação ML + Shopee + Amazon.
2. `skills/excel-generation/SKILL.md` — formatação Excel corporativa, number formats, tabelas, gráficos.
3. `skills/design/report-design-system/SKILL.md` — HTML dark premium e hierarquia visual.
4. `skills/design/financial-design-systems/SKILL.md` — paleta/visual financeiro dark quando houver gráficos/cards.
5. `skills/design/data-visualization-2/SKILL.md` — seleção correta de gráficos e storytelling com dados.

Se o contexto estiver apertado, leia primeiro esta skill + `excel-generation`; carregue as demais conforme o output exigir.

## Estrutura mínima da DRE

### Estrutura clássica obrigatória

A DRE precisa seguir estrutura profissional completa, mesmo quando parte dos dados estiver indisponível. Não pular seções; marcar lacunas explicitamente.

Obrigatório conter, nesta ordem:

1. **Receita Operacional Bruta**
   - Vendas de Marketplace
   - Vendas de Atacado, se houver
   - Outras Receitas Operacionais
   - Total Receita Bruta
2. **Deduções da Receita Bruta**
   - Impostos sobre vendas
   - Devoluções e cancelamentos
   - Descontos concedidos
   - Total Deduções
3. **Receita Operacional Líquida**
4. **CMV — Custo das Mercadorias Vendidas**
   - Custo das Mercadorias
   - Custo de Importação
   - Fretes e Seguros
   - Outros Custos Diretos
   - Total CMV
5. **Lucro Bruto**
6. **Margem Bruta (%)**
7. **Despesas Operacionais**
   - Despesas Administrativas
   - Despesas Comerciais
   - Total Despesas Operacionais
8. **EBITDA**
9. **Margem EBITDA (%)**
10. **Depreciação e Amortização**
11. **Lucro Operacional (EBIT)**
12. **Margem Operacional (%)**
13. **Resultado Financeiro**
   - Receitas Financeiras
   - Despesas Financeiras
   - Resultado Financeiro Líquido
14. **LAIR — Lucro Antes do IR/CSLL**
15. **Provisões Tributárias**
16. **Lucro Líquido**
17. **Margem Líquida (%)**

### Reconciliação marketplace obrigatória

Além da estrutura clássica, incluir a visão de marketplace:

- Receita comercial válida
- Receita liquidada em extrato / settlement — somente como reconciliação, não como faturamento
- Diferença comercial × settlement
- Taxas/fees marketplace
- Ads reais
- Gestão/agência Ads, se aplicável

### Por marketplace

Obrigatório para Mercado Livre, Shopee e Amazon:

- pedidos válidos
- faturamento comercial válido
- share do faturamento
- settlement/reconciliação
- CMV alocado ou real
- lucro bruto
- margem bruta
- taxas marketplace e % sobre receita
- Ads e % sobre receita
- gestão/agência alocada
- resultado operacional
- margem operacional
- resultado líquido gerencial
- margem líquida gerencial

## Premissas e limitações obrigatórias

Nunca esconder premissa. Sempre explicitar:

- Fonte do faturamento comercial.
- Fonte do settlement.
- Fonte do CMV.
- Se CMV por marketplace for alocado proporcionalmente, declarar isso em destaque.
- Se impostos, despesas financeiras, folha, aluguel, pró-labore ou overhead administrativo não estiverem na base, declarar que margem líquida é **gerencial/conhecida**, não contábil final.
- Ads Shopee: se vier manual da plataforma, usar como oficial e Wallet API apenas como conciliação.
- SETTLEMENT nunca deve ser chamado de faturamento bruto sem qualificador.

## Output obrigatório

Gerar pelo menos:

1. `.xlsx` executivo
   - Aba 00 Capa / Resumo executivo
   - Aba 01 DRE Consolidada
   - Aba 02 DRE Marketplace
   - Aba 03 Fontes e Premissas
   - Aba 04 Gráficos / Visual
2. `.html` executivo
3. `summary.json` técnico com números, fontes e premissas

## Padrão visual

### Excel

- Sem gridlines.
- Freeze panes nos headers.
- Moeda como `R$ #,##0.00`; percentuais como `0.00%`; pedidos como inteiro.
- Nunca formatar valor monetário como percentual.
- Totais/lucro/margens em destaque.
- Títulos claros, análise vertical e colunas de comentário.
- Notas/premissas com largura suficiente e wrap text.

### HTML

- Dark premium, cards KPI, tabela legível e notas metodológicas.
- Título executivo: insight + período.
- Não usar visual “só dark”; hierarquia, espaçamento e storytelling são obrigatórios.

## Checklist de validação antes de entregar

- [ ] Soma por marketplace bate com consolidado.
- [ ] Receita, CMV, taxas, Ads e resultado batem com o summary.
- [ ] Margem bruta = lucro bruto / receita comercial.
- [ ] Margem operacional = resultado operacional / receita comercial.
- [ ] Margem líquida gerencial = resultado líquido gerencial / receita comercial.
- [ ] Não há dinheiro formatado como percentual.
- [ ] Premissas e limitações estão explícitas.
- [ ] DRE parece relatório executivo, não planilha de apuração.

## Referência de qualidade

Pedro rejeitou DRE v3 em 2026-05-01 por estar correto nos dados, mas incompleto e pouco profissional. O padrão mínimo aceito a partir disso é v4+: consolidado + marketplace + margens + premissas + Excel/HTML executivo.


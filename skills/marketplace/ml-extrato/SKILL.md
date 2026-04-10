---
name: ml-extrato
description: Gerar extratos financeiros completos do Mercado Livre/Mercado Pago com detalhamento de vendas, taxas, comissões, fretes, devoluções e disputas. Use quando o Pedro pedir extrato, relatório financeiro, movimentações, faturamento ou qualquer análise financeira do Mercado Livre. Também usar quando precisar de dados financeiros do ML para outros relatórios ou análises.
---

# Extrato Financeiro — Mercado Livre / Mercado Pago

Gera extratos financeiros completos a partir da API do Mercado Pago, no formato padrão aprovado pelo Pedro.

## Autenticação

Tokens armazenados em `/root/.openclaw/.ml-tokens-finance.json`. Refresh automático via script.

Antes de qualquer chamada, executar o refresh do token:
```bash
{baseDir}/scripts/ml-refresh-token.sh finance
```

## Gerar extrato

```bash
{baseDir}/scripts/ml-extrato.py --inicio 2026-03-08 --fim 2026-03-14
```

O script gera o Excel no formato padrão em `~/workspace/reports/`.

### Parâmetros

| Param | Obrigatório | Descrição |
|---|---|---|
| `--inicio` | Sim | Data inicial (YYYY-MM-DD) |
| `--fim` | Sim | Data final (YYYY-MM-DD) |
| `--output` | Não | Caminho de saída (default: `~/workspace/reports/extrato-ml-{inicio}-{fim}.xlsx`) |

## Formato padrão do extrato

### Cabeçalho
- Linha 1: Título com período
- Linha 2: GB Importadora / Budamix • User ID • Período

### Colunas (23)
Ver `references/colunas.md` para descrição detalhada de cada coluna.

### Classificações de transação

| Técnico | Exibição | Descrição |
|---|---|---|
| SETTLEMENT | Venda Concluída | Venda paga e liberada pelo ML |
| SETTLEMENT_SHIPPING | Repasse de Frete | Frete cobrado do comprador, repassado à transportadora |
| REFUND | Devolução / Reembolso | Valor devolvido ao comprador |
| REFUND_SHIPPING | Estorno de Frete | Frete estornado em venda cancelada |
| DISPUTE | Reclamação / Disputa | Valor retido ou devolvido por reclamação |

### Status de liquidação

| Status | Significado |
|---|---|
| Recebido | Já caiu na conta do Mercado Pago |
| Pendente | Em processamento |
| Cancelado | Não será liquidado |

### Resumo financeiro (final da planilha)

Inclui totais por classificação, quantidades, taxas, e saldo líquido final.
Cada linha tem: valor absoluto + porcentagem do bruto total + descrição explicativa.

Cores do resumo:
- 🟢 Verde (#E8F5E9): entradas positivas (vendas, recebido)
- 🔴 Vermelho (#FFEBEE): saídas (devoluções, disputas, taxas)
- 🟡 Amarelo (#FFF8E1): neutro/parcial (frete, pendente)
- 🔵 Azul (#E3F2FD): saldo líquido final

## Apps e credenciais

| App | ID | Uso | Tokens |
|---|---|---|---|
| Vendas | 8869805792970343 | Pedidos, anúncios, itens | .ml-tokens.json |
| Financeiro | 8100349388872095 | Pagamentos, taxas, extrato | .ml-tokens-finance.json |
| Métricas | 7970005349031308 | Reputação, métricas | .ml-tokens-metrics.json |

Credenciais completas no 1Password (vault OpenClaw).

## Regras

- Usar SEMPRE termos em português no resumo (nunca jargão técnico na apresentação)
- Termos técnicos apenas internamente para cálculos
- Cor da marca GB no cabeçalho: #174C4C
- Porcentagem do bruto ao lado de cada valor do resumo
- Status de liquidação obrigatório em cada linha

## Critérios de Qualidade

- Extrato deve conter TODAS as movimentações do período sem exceção
- Classificação correta: cada transação no tipo certo (SETTLEMENT, REFUND, DISPUTE, etc)
- Taxas calculadas corretamente: bruto - líquido = taxa
- Status de liquidação preciso: Recebido / Pendente / Cancelado
- Resumo no final com totais, quantidades e porcentagens
- Termos em português no resumo (nunca jargão técnico na apresentação)
- Formato Excel com cabeçalho GB Importadora, cor #174C4C, zebra-striping
- Porcentagem do bruto ao lado de cada valor do resumo

## Aprendizados Incorporados

<!-- MELHORIA 2026-03-16 -->
### Formato padrão aprovado pelo Pedro
- 23 colunas incluindo Classificação em português e Status Liquidação
- Resumo com totais + porcentagem do bruto + descrição explicativa
- Cores: verde (entradas), vermelho (saídas), amarelo (neutro), azul (saldo)
- Termos técnicos (SETTLEMENT, REFUND) apenas internos — exibição sempre em português
<!-- /MELHORIA -->

<!-- MELHORIA 2026-03-16 -->
### Refresh de token obrigatório antes de cada extração
- Tokens ML expiram em 6h — sempre rodar ml-refresh-token.sh antes
- Se refresh falhar, abortar e informar (não tentar com token vencido)
<!-- /MELHORIA -->

## Formatação Visual

Seguir obrigatoriamente o design system: `skills/design/excel-design-system.md`

Padrão: Dark mode profissional com:
- Background #1B2838, zebra striping
- Cabeçalho #174C4C (GB green)
- Accent colors: verde (#4CAF50), vermelho (#EF5350), azul (#42A5F5), amarelo (#FFC107)
- Emojis como identificadores visuais
- Gráficos quando aplicável (openpyxl.chart)
- Nenhuma célula branca — tudo dark

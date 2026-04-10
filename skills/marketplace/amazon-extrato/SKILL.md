---
name: amazon-extrato
description: Gerar extratos financeiros completos da Amazon BR via SP-API com detalhamento de vendas, taxas, comissões FBA, devoluções, disputas A-to-Z e ajustes. Use quando o Pedro pedir extrato, relatório financeiro, movimentações, faturamento ou qualquer análise financeira da Amazon. Também usar quando precisar de dados financeiros da Amazon para outros relatórios ou análises.
---

# Extrato Financeiro — Amazon BR (SP-API)

Gera extratos financeiros completos a partir da Amazon Selling Partner API (Finances), no formato padrão aprovado pelo Pedro (23 colunas).

## Autenticação

Credenciais SP-API armazenadas em `/root/.openclaw/workspace/integrations/amazon/.sp-api-credentials.json`.
Contém: refresh_token, lwa_app_id, lwa_client_secret, aws_access_key, aws_secret_key, role_arn.
Marketplace: BR (A2Q3Y263D00KWC).

Não precisa de refresh manual — a biblioteca `python-amazon-sp-api` gerencia o token automaticamente.

## Gerar extrato

```bash
python3 {baseDir}/scripts/amazon-extrato.py --inicio 2026-03-01 --fim 2026-03-20
```

O script gera o Excel no formato padrão em `~/workspace/reports/`.

### Parâmetros

| Param | Obrigatório | Descrição |
|---|---|---|
| `--inicio` | Sim | Data inicial (YYYY-MM-DD) |
| `--fim` | Sim | Data final (YYYY-MM-DD) |
| `--output` | Não | Caminho de saída (default: `~/workspace/reports/extrato-amazon-{inicio}-{fim}.xlsx`) |

### Comportamentos automáticos
- **Paginação**: segue NextToken automaticamente até esgotar
- **Rate limiting**: retry com backoff exponencial (2s, 4s, 8s, 16s, 30s)
- **PostedBefore**: ajustado automaticamente se data fim > agora - 3min (requisito da API)
- **Erros individuais**: logados e continuados (não aborta o extrato inteiro)

## Formato padrão do extrato

### Cabeçalho
- Linha 1: Título com período e marketplace
- Linha 2: GB Importadora / Budamix • Amazon BR • Período

### Colunas (23)
Ver `references/colunas.md` para descrição detalhada de cada coluna.

### Classificações de transação

| Lista de Eventos | Técnico | Exibição | Descrição |
|---|---|---|---|
| ShipmentEventList | SETTLEMENT | Venda Concluída | Venda processada com fees cobradas |
| RefundEventList | REFUND | Devolução / Reembolso | Valor devolvido ao comprador |
| GuaranteeClaimEventList | DISPUTE | Disputa A-to-Z | Garantia acionada pelo comprador |
| ServiceFeeEventList | SERVICE_FEE | Taxa de Serviço | Taxas avulsas (FBA Storage, etc.) |
| AdjustmentEventList | ADJUSTMENT | Ajuste | Ajustes automáticos (WAREHOUSE_DAMAGE, etc.) |

### Status de liquidação

| Status | Significado |
|---|---|
| Recebido | Settlement já creditado na conta |
| Pendente | Aguardando próximo ciclo de pagamento |

### Resumo financeiro (final da planilha)

Inclui:
- Totais por classificação com porcentagem do bruto
- Quantidades por tipo de evento
- Status de liquidação (Recebido / Pendente)
- Saldo líquido final
- Breakdown detalhado de fees (Commission, FBA fees, etc.)

Cores do resumo:
- 🟢 Verde (#E8F5E9): entradas positivas (vendas, recebido)
- 🔴 Vermelho (#FFEBEE): saídas (devoluções, disputas, taxas)
- 🟡 Amarelo (#FFF8E1): neutro/parcial (ajustes, cupons)
- 🔵 Azul (#E3F2FD): saldo líquido final

## Endpoints SP-API utilizados

| Endpoint | Uso |
|---|---|
| `Finances.list_financial_events()` | Eventos financeiros do período (principal) |
| `Finances.list_financial_event_groups()` | Status de liquidação dos grupos |

## Dependências

- `python-amazon-sp-api` (pip)
- `openpyxl` (pip)

## Regras

- Usar SEMPRE termos em português no resumo (nunca jargão técnico na apresentação)
- Cor da marca GB no cabeçalho: #174C4C
- Zebra striping nas linhas de dados
- Porcentagem do bruto ao lado de cada valor do resumo
- Metadata com breakdown completo em JSON (SKU, qty, charges, fees)

## Critérios de Qualidade

- Extrato deve conter TODAS as movimentações do período (paginação completa)
- Classificação correta: cada evento no tipo certo
- Fees calculadas corretamente: soma de ItemFeeList (valores negativos)
- Refunds com campos *AdjustmentList (não confundir com ItemChargeList)
- Resumo no final com totais, quantidades e porcentagens
- Breakdown de fees por tipo (Commission, FBA, etc.)
- Formato Excel padrão GB Importadora

## Formatação Visual

Seguir obrigatoriamente o design system: `skills/design/excel-design-system.md`

Padrão: Dark mode profissional com:
- Background #1B2838, zebra striping
- Cabeçalho #174C4C (GB green)
- Accent colors: verde (#4CAF50), vermelho (#EF5350), azul (#42A5F5), amarelo (#FFC107)
- Emojis como identificadores visuais
- Gráficos quando aplicável (openpyxl.chart)
- Nenhuma célula branca — tudo dark

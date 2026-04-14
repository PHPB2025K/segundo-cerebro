---
name: shopee-extrato
description: Gerar extratos financeiros completos da Shopee com detalhamento de vendas, taxas, comissões, fretes, devoluções e disputas. Suporta 3 contas (Budamix Store, Budamix Oficial, Budamix Shop) com extrato individual por conta e aba consolidada comparativa. Use quando o Pedro pedir extrato, relatório financeiro, movimentações, faturamento ou qualquer análise financeira da Shopee. Também usar quando precisar de dados financeiros da Shopee para outros relatórios ou análises.
---

# Extrato Financeiro — Shopee / Budamix (Multi-Conta)

> Usado por [[openclaw/agents/trader/IDENTITY|Trader]]

Gera extratos financeiros completos a partir da API Shopee v2, no formato padrão aprovado pelo Pedro (mesmo formato do extrato ML — 23 colunas). Suporta 3 contas com consolidação automática.

## Contas

| Alias | Loja | Shop ID | CNPJ | Username |
|---|---|---|---|---|
| budamix-store | Budamix Store | 448649947 | 07.194.128/0001-82 | budamix.store |
| budamix-store2 | Budamix Oficial | 860803675 | 45.200.547/0001-79 | budamix_store |
| budamix-shop | Budamix Shop | 442066454 | 63.922.116/0001-06 | budamix.shop |

Mapa de contas: `integrations/shopee/accounts.json`

## Autenticação

Tokens por conta em `integrations/shopee/`:
- `.shopee-tokens-budamix-store.json`
- `.shopee-tokens-budamix-store2.json`
- `.shopee-tokens-budamix-shop.json`

Credenciais compartilhadas em `integrations/shopee/.env`:
- SHOPEE_PARTNER_ID=2031533
- SHOPEE_PARTNER_KEY (Partner Key do app Openclaw Agent)

Refresh automático de tokens dentro do script (access_token expira em 4h, refresh_token em 30 dias).

## Gerar extrato

### Conta específica
```bash
python3 {baseDir}/scripts/shopee-extrato.py --inicio 2026-03-01 --fim 2026-03-20 --conta budamix-store
```

### Todas as contas (com consolidado)
```bash
python3 {baseDir}/scripts/shopee-extrato.py --inicio 2026-03-01 --fim 2026-03-20 --conta todas
```

### Parâmetros

| Param | Obrigatório | Default | Descrição |
|---|---|---|---|
| `--inicio` | Sim | — | Data inicial (YYYY-MM-DD) |
| `--fim` | Sim | — | Data final (YYYY-MM-DD) |
| `--conta` | Não | `todas` | Nome da conta ou `todas` para consolidado |
| `--output` | Não | auto | Caminho de saída |

### Output

- Conta única: `reports/extrato-shopee-{alias}-{inicio}-{fim}.xlsx`
- Todas: `reports/extrato-shopee-todas-{inicio}-{fim}.xlsx`

## Estrutura do Excel (modo `--conta todas`)

1. **Aba "Budamix Store"** — Extrato individual (23 colunas + resumo financeiro)
2. **Aba "Budamix Oficial"** — Extrato individual (23 colunas + resumo financeiro)
3. **Aba "Budamix Shop"** — Extrato individual (23 colunas + resumo financeiro)
4. **Aba "Consolidado"** — 3 seções:
   - 📋 Comparativo por conta (bruto, taxas, líquido, margem, ticket médio)
   - 💳 Breakdown por método de pagamento (consolidado)
   - 🏆 Top 10 produtos por volume vendido (consolidado)

## Formato padrão do extrato (por aba)

### Cabeçalho
- Linha 1: Título com nome da loja
- Linha 2: GB Importadora / Budamix • Shop ID • Período

### Colunas (23)
Ver `references/colunas.md` para descrição detalhada.

### Classificações de transação
Ver `references/classificacoes.md` para mapeamento completo.

| Status Shopee | Técnico | Exibição |
|---|---|---|
| COMPLETED | SETTLEMENT | Venda Concluída |
| CANCELLED | REFUND | Devolução/Cancelamento |
| IN_CANCEL | DISPUTE | Em Cancelamento/Disputa |
| SHIPPED/READY_TO_SHIP | PENDING | Em Trânsito/Aguardando |

### Resumo financeiro (final de cada aba)
- Totais por classificação + quantidades + porcentagens
- Breakdown por método de pagamento com valores bruto e líquido
- Cores: Verde (entradas), Vermelho (saídas), Amarelo (neutro), Azul (saldo)

## Nomenclatura Unificada ML ↔ Shopee

Ver `references/nomenclatura-unificada.md` para mapeamento completo.

Termos-chave:
- **Valor Bruto** = cost_of_goods_sold (Shopee) = transaction_amount (ML)
- **Valor Líquido** = escrow_amount (Shopee) = net_received_amount (ML)
- **Taxas** = commission + service + transaction + campaign + fbs fees

## Endpoints Shopee API v2

| Endpoint | Uso | Limite |
|---|---|---|
| GET /api/v2/order/get_order_list | Listar pedidos | Max 15 dias/request, 50/page |
| GET /api/v2/order/get_order_detail | Status, datas, items | Batch até 50 order_sn |
| GET /api/v2/payment/get_escrow_detail | Detalhes financeiros | 1 order_sn/request |
| GET /api/v2/payment/get_escrow_list | Escrows liberados | Paginado |
| POST /api/v2/auth/access_token/get | Refresh de token | — |

### Assinatura
```python
# Chamadas autenticadas (shop-level):
base_string = f"{partner_id}{api_path}{timestamp}{access_token}{shop_id}"
sign = hmac.new(partner_key.encode(), base_string.encode(), hashlib.sha256).hexdigest()

# Refresh de token (public-level):
base_string = f"{partner_id}{api_path}{timestamp}"
```

## Performance

- **3 contas / março 2026:** ~3.300 pedidos, ~13 min de execução
- **1 conta principal:** ~2.000 pedidos, ~7 min
- Rate limiting: max 10 req/s por conta, retry com backoff em 429
- Contas processadas sequencialmente (não paralelo)
- Erros em pedidos individuais são logados mas não abortam

## Regras

- Termos sempre em português no resumo
- Cor GB no cabeçalho: #174C4C
- Aba Consolidado: dark mode com ícones visuais
- % do bruto ao lado de cada valor
- Status de liquidação obrigatório em cada linha
- Token refresh automático (access_token 4h, refresh_token 30d)

## Critérios de Qualidade

- TODOS os pedidos do período, sem exceção
- Classificação correta por status do pedido
- Taxas = soma de todas as fees individuais
- Status de liquidação preciso (baseado em escrow_release_time)
- Resumo com totais, quantidades e porcentagens
- Excel formatado (cabeçalho GB, zebra-striping)
- Top 10 produtos com dados reais da API
- Erros logados sem abortar execução

## Formatação Visual

Seguir obrigatoriamente o design system: `skills/design/excel-design-system.md`

Padrão: Dark mode profissional com:
- Background #1B2838, zebra striping
- Cabeçalho #174C4C (GB green)
- Accent colors: verde (`#4CAF50`), vermelho (`#EF5350`), azul (`#42A5F5`), amarelo (`#FFC107`)
- Emojis como identificadores visuais
- Gráficos quando aplicável (openpyxl.chart)
- Nenhuma célula branca — tudo dark

---

## Notas relacionadas

- [[skills/marketplace/amazon-extrato/SKILL|Extrato Amazon]]
- [[skills/marketplace/ml-extrato/SKILL|Extrato ML]]
- [[skills/marketplace/consolidado-financeiro/SKILL|Consolidado Financeiro]]

---
## Referências
- [[skills/marketplace/shopee-extrato/references/classificacoes|Classificações]]
- [[skills/marketplace/shopee-extrato/references/colunas|Colunas]]
- [[skills/marketplace/shopee-extrato/references/nomenclatura-unificada|Nomenclatura Unificada]]

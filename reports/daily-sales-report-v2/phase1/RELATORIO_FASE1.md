# Relatório — Daily Sales Report v2 — Fase 1: Mapeamento de Dados

**Data:** 2026-05-12
**Autor:** Kobe (OpenClaw)
**Escopo:** Diagnóstico técnico dos dados disponíveis para separação por conta/plataforma

---

## 1. Sumário Executivo

**Veredito: PODE AVANÇAR**

O campo `shop_id` na tabela `orders` identifica de forma confiável as 3 contas Shopee. Mercado Livre e Amazon operam com conta única cada. Os últimos 60 dias estão completos para todas as 5 unidades operacionais, sem lacunas. A view `v_daily_sales` serve apenas para resumo por plataforma — para análise por conta Shopee, é necessário consultar `orders` diretamente.

---

## 2. Mapa de Dados por Plataforma/Conta

### Shopee — 3 contas separadas via `shop_id`

| Conta | shop_id | alias | username | CNPJ | Pedidos (60d) | Receita (60d) |
|-------|---------|-------|----------|------|---------------|---------------|
| Budamix Store | `448649947` | budamix-store | budamix.store | 07.194.128/0001-82 | 7.272 | R$ 266.411,15 |
| Budamix Oficial (Conta 2) | `860803675` | budamix-store2 | budamix_store | 45.200.547/0001-79 | 2.677 | R$ 141.132,68 |
| Budamix Shop (Conta 3) | `442066454` | budamix-shop | budamix.shop | 63.922.116/0001-06 | 2.372 | R$ 155.887,97 |

**Fonte de mapeamento:** `/root/.openclaw/workspace/integrations/shopee/accounts.json`

### Mercado Livre — conta única

- `platform = "ml"`, `shop_id = NULL`
- Seller ID: `532562281` (do .env)
- 60 dias: 5.122 pedidos

### Amazon — conta única

- `platform = "amazon"`, `shop_id = NULL`
- Marketplace ID: `A2Q3Y263D00KWC`
- 60 dias: 1.748 pedidos
- 100% FBA (`FulfillmentChannel = "AFN"` no raw_payload)

---

## 3. Campos Confiáveis

| Campo | Tabela | Uso | Confiabilidade |
|-------|--------|-----|----------------|
| `platform` | orders | Identifica plataforma (shopee/ml/amazon) | ✅ Alta |
| `shop_id` | orders | Separa contas Shopee | ✅ Alta (string) |
| `order_date` | orders | Data/hora do pedido em UTC | ✅ Alta — converter para BRT |
| `total_amount` | orders | Valor total do pedido | ✅ Alta |
| `status` | orders | Estado do pedido | ✅ Alta |
| `items` | orders | Array JSON com SKU, título, qty, unit_price | ✅ Alta |
| `items[].sku` | orders.items | SKU do produto | ✅ Alta |
| `items[].quantity` | orders.items | Quantidade | ✅ Alta |
| `items[].unit_price` | orders.items | Preço unitário | ✅ Alta |
| `raw_payload` | orders | Payload original da API da plataforma | ✅ Disponível |
| `raw_payload.shipping_carrier` | orders (shopee) | "Full" = Shopee Fulfillment | ✅ Confiável |
| `raw_payload.FulfillmentChannel` | orders (amazon) | "AFN" = FBA | ✅ Confiável |
| `fulfillment_inventory` | tabela separada | Estoque FBA/Full por SKU e shop_id | ✅ Disponível |

---

## 4. Campos Suspeitos / Não Confiáveis

| Campo | Problema |
|-------|----------|
| `shop_id` para ML/Amazon | Sempre `NULL` — não é problema pois há conta única, mas impede uso como chave universal |
| `unique_buyers` em v_daily_sales | Amazon sempre retorna 1 (provável limitação de API) — não usar para análise de clientes Amazon |
| `buyer_username` / `buyer_id` | Disponível mas não relevante para o report v2 |
| Dados de ADS | Indisponíveis nesta base — não há tabela de investimento em publicidade |
| Custo do produto | Não disponível em `orders` — `fulfillment_inventory.unit_price` é preço de venda, não custo |
| Descontos | Não há campo explícito de desconto em `orders` ou `items` — pode estar embutido no raw_payload da Shopee |

---

## 5. Validação de 60 Dias por Conta

### Cobertura

| Unidade | Dias com dados | Lacunas | Status |
|---------|---------------|---------|--------|
| v_daily_sales (geral) | 61/61 | 0 | ✅ |
| Shopee — Budamix Store | 61/61 | 0 | ✅ |
| Shopee — Budamix Oficial (C2) | 61/61 | 0 | ✅ |
| Shopee — Budamix Shop (C3) | 61/61 | 0 | ✅ |
| Mercado Livre | 61/61 | 0 | ✅ |
| Amazon | 61/61 | 0 | ✅ |

**Período validado:** 2026-03-13 a 2026-05-12 (inclui dia parcial de hoje).

### Amostra diária Shopee (últimos 7 dias)

| Data | Budamix Store | Budamix Oficial (C2) | Budamix Shop (C3) |
|------|---------------|----------------------|--------------------|
| 2026-05-06 | 87 / R$3.071 | 34 / R$2.248 | 26 / R$2.151 |
| 2026-05-07 | 80 / R$2.691 | 31 / R$1.771 | 29 / R$1.736 |
| 2026-05-08 | 84 / R$2.868 | 43 / R$2.336 | 20 / R$1.294 |
| 2026-05-09 | 51 / R$1.910 | 28 / R$1.498 | 18 / R$1.066 |
| 2026-05-10 | 65 / R$2.283 | 28 / R$1.605 | 36 / R$1.969 |
| 2026-05-11 | 85 / R$3.102 | 42 / R$2.156 | 29 / R$2.212 |
| 2026-05-12* | 12 / R$356 | 5 / R$343 | 6 / R$319 |

*Dia parcial (dados até ~13h BRT).

### Status de pedidos (amostra recente)

| Plataforma | Statuses |
|------------|----------|
| Shopee | delivered (maioria), cancelled, confirmed, shipped, to_confirm_receive, to_return |
| ML | paid (maioria), cancelled, partially_refunded |
| Amazon | shipped (maioria), cancelled, pending |

Cancelados estão claramente identificados pelo status `cancelled` em todas as plataformas.

---

## 6. Qualidade da View `v_daily_sales`

- **Separa por plataforma:** Sim (shopee, ml, amazon).
- **Separa por conta Shopee:** NÃO. Consolida as 3 contas em uma única linha "shopee".
- **Serve para resumo geral:** Sim — faturamento total, pedidos, ticket médio por plataforma/dia.
- **Serve para análise por conta:** NÃO — precisa consultar `orders` diretamente filtrando por `shop_id`.
- **Timezone:** A view usa `order_date` que está em UTC. Para relatório BRT (00:00–23:59), a consulta na `orders` precisa converter timezone. A view parece já fazer essa conversão internamente (as contagens batem com os dados da `orders` convertidos para BRT).

### Proposta para Fase 2

Criar consulta direta na `orders` para gerar métricas por conta Shopee:

```sql
SELECT
  shop_id,
  DATE(order_date AT TIME ZONE 'UTC' AT TIME ZONE 'America/Sao_Paulo') AS sale_date,
  COUNT(*) AS order_count,
  SUM(total_amount) AS total_revenue,
  AVG(total_amount) AS avg_order_value
FROM orders
WHERE platform = 'shopee'
  AND status != 'cancelled'
GROUP BY shop_id, sale_date
ORDER BY sale_date DESC, shop_id;
```

---

## 7. Riscos e Lacunas

| # | Risco | Severidade | Mitigação |
|---|-------|------------|-----------|
| 1 | `v_daily_sales` não separa Shopee por conta | Médio | Consultar `orders` direto com filtro `shop_id` — dados disponíveis |
| 2 | Dados de ADS/publicidade indisponíveis | Baixo (Fase 1) | Fora do escopo atual; pode ser adicionado em fase futura via APIs de Ads |
| 3 | Custo do produto não disponível em orders | Baixo | Margem/lucro ficam para fase futura; `fulfillment_inventory` tem preço de venda, não custo |
| 4 | Amazon `unique_buyers` sempre = 1 | Baixo | Não usar contagem de compradores únicos para Amazon |
| 5 | Descontos não explícitos em orders | Baixo | Podem ser extraídos do `raw_payload` se necessário na Fase 2 |
| 6 | Shopee `shop_id` é string, não int | Trivial | Basta comparar como string; mapeamento já documentado |
| 7 | Amazon FBA removal orders | Baixo | Todos os 200 pedidos recentes são `AFN` (FBA); status `cancelled` já filtra devoluções |
| 8 | SKUs não 100% padronizados cross-plataforma | Médio | Mapeamento CSV já existe (`sku_fiscal_map`); script atual já usa canonical_sku() |

**Nenhum bloqueio real identificado.**

---

## 8. Recomendações para Fase 2/3

### Fase 2 — Implementação do Report Personalizado
1. Criar função que consulta `orders` por `platform` + `shop_id` com range BRT.
2. Mapeamento de `shop_id` → nome da conta já documentado; usar `accounts.json` como fonte.
3. Para cada funcionário, gerar seção com métricas da(s) sua(s) conta(s):
   - Lucas: 3 seções Shopee (uma por shop_id)
   - Yasmin: 1 seção ML
   - Leonardo: 1 seção Amazon (com indicador FBA via `raw_payload.FulfillmentChannel`)
4. Manter resumo geral consolidado no início de cada mensagem.
5. Incluir sinais de fulfillment: Shopee Full (`shipping_carrier = "Full"`) e Amazon FBA (`FulfillmentChannel = "AFN"`).

### Fase 3 — Análise Profunda em Background
1. Análise de tendência por conta (comparação com média 30d por conta).
2. Top produtos por conta (não só consolidado).
3. Alertas automáticos: queda > 30% vs média, dias sem pedidos, etc.
4. Integração com dados de ADS quando disponíveis.
5. Possível criação de view `v_daily_sales_by_account` no Supabase para performance.

---

## Resposta à Pergunta-Chave

> "Conseguimos separar com confiança as 3 contas Shopee nos dados históricos dos últimos 60 dias?"

**SIM.** O campo `shop_id` na tabela `orders` identifica cada conta Shopee de forma confiável e consistente. As 3 contas têm dados todos os dias dos últimos 60 dias, sem lacunas. O mapeamento shop_id → nome da conta está documentado em `accounts.json`.

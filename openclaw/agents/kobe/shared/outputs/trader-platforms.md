# Plataformas — Contexto Operacional

_Status e detalhes de cada plataforma da GB Importadora._

## Mercado Livre

| Campo | Valor |
|---|---|
| **Status** | ✅ Principal — maior volume |
| **Seller ID** | Consultar via API |
| **API** | 3 apps (Vendas, Financeiro, Métricas) |
| **Tokens** | `/root/.openclaw/.ml-tokens*.json` |
| **Refresh** | `skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh` |
| **Ads** | 21 campanhas ativas (ROAS 8.76x em Mar/2026) |
| **Marca** | Budamix (registrada INPI) |
| **Mix** | ~80% importados China (potes herméticos carro-chefe, 7 SKUs) |

### Custos ML
- Comissão: varia por categoria (consultar skill ml-fees-rules)
- Frete grátis: absorvido pelo vendedor acima de certo valor
- Agência ADS ML: parte dos R$9k/mês

## Amazon BR

| Campo | Valor |
|---|---|
| **Status** | ✅ Ativa — crescendo |
| **Marketplace ID** | A2Q3Y263D00KWC |
| **SP-API** | Endpoint NA, credenciais no 1Password |
| **Ads API** | Via Supabase Bidspark, endpoint NA |
| **FBA** | Ativo (estoque no fulfillment NÃO aparece na planilha geral) |

### Custos Amazon
- Comissão: varia por categoria
- FBA fees: pick & pack + storage
- Agência ADS Amazon: parte dos R$9k/mês

## Shopee (3 contas)

| Campo | Valor |
|---|---|
| **Status** | ✅ Ativa — 3 contas conectadas |
| **Partner ID** | 2031533 |
| **API** | Open Platform v2 (OAuth aprovado Mar/2026) |
| **Contas** | budamix-store, budamix-store2, budamix-shop |
| **Auto-refresh** | Implementado |

### Observações Shopee
- Margens menores que ML (ex: CK4742_B — 9% Shopee vs 31% ML)
- SKUs atualizados via API em 2 de 3 contas (budamix-store pendente)
- API de anúncios limitada — aguardando evolução

## Dados Cruzados

### Produto-chave: Potes Herméticos de Vidro
- 7 SKUs (variações de tamanho)
- Carro-chefe da operação
- Kits e combos para melhor ranqueamento
- Importados via Skiway (China) → Open Trade (Itajaí) → Pedreira

### Estoque
- Fonte: Google Sheets `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`
- NÃO inclui estoque nos fulfillments (Amazon FBA, ML Full, Shopee)
- Skill: `skills/operations/inventory-management/SKILL.md`

### Faturamento Referência (Mar/2026)
- Bruto consolidado: ~R$197k/mês
- Líquido consolidado: ~R$131k/mês
- Margem média: ~66,7%
- Pico histórico: R$1M/mês (Jul/2025)

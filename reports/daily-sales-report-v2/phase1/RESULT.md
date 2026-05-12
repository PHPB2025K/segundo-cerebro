# RESULT — Daily Sales Report v2 — Fase 1

## 1. Resumo

A Fase 1 de diagnóstico está **concluída com sucesso**. Veredito: **PODE AVANÇAR**.

Principais achados:
- O campo `shop_id` na tabela `orders` separa as 3 contas Shopee de forma confiável:
  - `448649947` → Budamix Store
  - `860803675` → Budamix Oficial (Conta 2)
  - `442066454` → Budamix Shop (Conta 3)
- Mercado Livre e Amazon operam com conta única cada.
- 60 dias de dados completos para todas as 5 unidades, sem lacunas.
- A view `v_daily_sales` NÃO separa Shopee por conta — é necessário consultar `orders` diretamente.
- Campos de granularidade (faturamento, pedidos, ticket médio, SKU, quantidade, status, horário BRT) estão todos disponíveis.
- Sinais de fulfillment disponíveis: Shopee Full (`shipping_carrier`) e Amazon FBA (`FulfillmentChannel`).
- Nenhum bloqueio identificado.

## 2. Arquivos Criados

| Arquivo | Descrição |
|---------|-----------|
| `RELATORIO_FASE1.md` | Relatório completo com mapa de dados, campos confiáveis/suspeitos, validação 60 dias, riscos e recomendações |
| `diag_data_mapping.py` | Script diagnóstico read-only que valida separação por conta e integridade dos dados |
| `RESULT.md` | Este arquivo |

## 3. Como Rodar

### Script diagnóstico
```bash
cd /root/openclaw-jobs/active/daily-sales-report-v2-phase1-20260512-125159/workspace
python3 diag_data_mapping.py
```
O script é read-only — não altera dados, não envia mensagens, não mexe em credenciais.

### Relatório
Abrir `RELATORIO_FASE1.md` para o diagnóstico completo com tabelas, mapeamentos e recomendações.

## 4. Pendências

| # | Pendência | Prioridade | Fase |
|---|-----------|------------|------|
| 1 | Criar consulta/view por conta Shopee (shop_id) para substituir v_daily_sales no report personalizado | Alta | Fase 2 |
| 2 | Implementar mensagens individuais por funcionário com métricas da(s) sua(s) conta(s) | Alta | Fase 2 |
| 3 | Extrair descontos do raw_payload Shopee, se necessário | Baixa | Fase 2/3 |
| 4 | Integrar dados de ADS/publicidade (indisponíveis nesta base) | Média | Fase 3 |
| 5 | Incluir custo de produto e margem (dados não disponíveis em orders) | Média | Fase 3 |
| 6 | Considerar criação de view `v_daily_sales_by_account` no Supabase para performance | Média | Fase 2 |
| 7 | Validar que `unique_buyers` do Amazon não é confiável (sempre = 1) | Baixa | Fase 2 |

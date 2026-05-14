# Data Builder — Daily Sales Analyst (Layer 0)

Componente determinístico do pipeline do Daily Sales Analyst. Não usa LLM.

## Responsabilidade

Consultar, validar e empacotar os dados de vendas diárias antes de qualquer camada analítica interpretar algo. Produz um `package.json` auditável com status de Data Readiness.

## Uso

```bash
# Gerar e salvar package
python3 scripts/daily-sales-data-builder.py 2026-05-13 --write

# Imprimir no stdout (debug/preview)
python3 scripts/daily-sales-data-builder.py 2026-05-13 --stdout
```

## Output

O package é salvo em:
```
reports/daily-sales-report-v2/layered/packages/YYYY-MM-DD/package.json
```

## Schema

Ver `schema.json` neste diretório.

## Data Readiness

O Builder classifica cada execução como:

| Status | Significado | Pipeline |
|--------|-------------|----------|
| `DADOS_OK` | Todas as fontes disponíveis, volume normal, zero divergências críticas | Pode rodar normalmente |
| `DADOS_PARCIAIS` | Alguma limitação menor; dados suficientes com ressalva | Pode rodar com ressalva |
| `NOT_READY` | Fonte indisponível, divergência crítica ou falha sistêmica | Bloqueia execução |

Critérios detalhados em `readiness-rules.md`.

## Fonte de Dados

- **Fonte canônica:** tabela `orders` no Supabase (Budamix Central), agregada em janela BRT
- **Shopee:** separada por `shop_id` (3 contas)
- **Amazon:** identificação por ASIN/platform_item_id do pedido real
- **Mercado Livre:** filtro por `platform = ml`

## Versionamento

Versão atual: `v1.0`

Changelog em `CHANGELOG.md`.

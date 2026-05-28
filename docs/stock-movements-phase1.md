# Estoque GB — Fase 1: movimentos auditáveis

Esta fase adiciona um **livro de movimentações** para registrar eventos de estoque de forma auditável e segura.

## Garantias de segurança

- A nova rota `/api/stock-movements` **não escreve na Google Sheet**.
- Movimentos criados ficam, por padrão, em `recebido` ou `pendente_validacao`.
- Movimentos pendentes/divergentes **não alteram saldo**.
- O fluxo atual de entrada/saída manual via `/api/sheets/update` permanece separado.
- `stock_balances` foi deixada para Fase 2, porque a aba `ESTOQUE` continua sendo o saldo operacional nesta fase.

## Como aplicar a migração

1. Abra o Supabase SQL Editor do projeto.
2. Execute o arquivo:

```sql
migrations/202605281430_stock_movements_phase1.sql
```

Alternativamente, use a CLI/processo de deploy do Supabase se já existir no ambiente.

## Modelo criado

- `stock_movements`: ledger principal com status, origem, SKU, quantidade, locais e idempotência por `source_type + external_event_id`.
- `stock_movement_evidences`: evidências como foto, PDF, OCR, texto ou links ligados ao movimento.
- `sku_aliases`: aliases para normalização futura de SKU.
- `kit_bom`: composição de kits/combos para futuras baixas seguras.

## API

### `GET /api/stock-movements`

Parâmetros opcionais:

- `page` — padrão `1`
- `status` — filtra por status
- `sourceType` — filtra por origem
- `sku` — busca em `sku_raw`/`sku_resolved`

Retorna movimentos recentes, total e paginação. Se a migração ainda não foi aplicada, retorna lista vazia com `setupRequired: true`.

### `POST /api/stock-movements`

Cria um movimento sem aplicar saldo.

Campos mínimos:

```json
{
  "sourceType": "manual_app",
  "movementType": "entrada",
  "skuRaw": "SKU123",
  "quantity": 10,
  "unit": "un",
  "status": "pendente_validacao",
  "externalEventId": "opcional-idempotencia"
}
```

Se `externalEventId` for enviado e já existir para a mesma `sourceType`, a API retorna o registro existente como idempotente em vez de inserir duplicado.

## Fase 2 sugerida

1. Criar motor de validação/aplicação com transação e locks por SKU.
2. Adicionar `stock_balances`/snapshots e conciliação com a aba `ESTOQUE`.
3. Implementar normalização via `sku_aliases` e expansão de kits via `kit_bom`.
4. Ingerir WhatsApp Estoque/Devoluções como eventos brutos com evidências.
5. Só então liberar escrita controlada na planilha, com trilha de auditoria e rollback operacional.

---
title: "Sync Google Sheets → Supabase via Apps Script onEdit"
created: 2026-04-17
type: concept
status: active
tags:
  - knowledge
  - dev
  - automacao
---

# Sync Google Sheets → Supabase via Apps Script `onEdit`

Padrão pra manter Supabase em sincronia com uma planilha operacional, em tempo real, sem rodar servidor próprio. Latência ~1-2s por edição.

## Quando usar

- Pedro/operador edita uma planilha existente (inventário, precificação, status de pedido) e quer refletir no banco imediatamente.
- Volume baixo-médio (até ~1 edit por segundo). Apps Script tem quota de 20k requests/dia.
- SKU/ID da planilha já bate 1-pra-1 com uma coluna única no Supabase.

Quando **NÃO** usar:
- Edit em batch de centenas de linhas → use `syncAllStock()` manual ou export CSV + script Python.
- Sync bidirecional (Supabase → Sheets) → precisa de trigger na DB + webhook, não cabe no Apps Script simples.
- Dados sensíveis que não podem trafegar pela ACL da planilha (Apps Script assume quem edita tem permissão).

## Arquitetura

```
[Pedro edita planilha]
  ↓ Apps Script onEdit trigger (instalável, não o simples)
  ↓ UrlFetchApp.fetch(PATCH /rest/v1/{tabela}?{col}=eq.{valor}, {body})
  ↓ PostgREST com Prefer: return=representation
  ↓ Supabase responde 200 + array de linhas afetadas
  ↓ Array vazio = SKU sem match no banco (log WARN, sem side-effect)
```

## Pontos sutis aprendidos

### 1. Trigger instalável, não o simples

`function onEdit(e)` plain é "simple trigger" — não tem acesso a `UrlFetchApp`, roda em sandbox. Precisa registrar via `ScriptApp.newTrigger('onEdit').forSpreadsheet(ss).onEdit().create()` uma vez. Isso é um "installable trigger" que roda com as permissões do dono do script.

Padrão: ter uma função `installTrigger()` que roda manualmente 1x, remove triggers antigos (`ScriptApp.getProjectTriggers()`) e cria o novo. Primeira execução pede autorização — tem que clicar "permitir acesso" no diálogo.

### 2. Service role como constante no script (não commit)

Service role key fica inline na constante `SUPABASE_SERVICE_ROLE_KEY` no topo do script, que está dentro do Apps Script (Google-hosted) — nunca no git. O arquivo commitado (`scripts/google-apps-script-stock-sync.js` no repo) tem placeholder `COLE_A_SERVICE_ROLE_KEY_AQUI`.

Proteção efetiva: **ACL da planilha** (quem pode editar pode mudar stock). Se planilha tiver edit compartilhado amplo, considerar mover pra uma Edge Function que valide quem chamou.

### 3. Prefer: return=representation

Sem esse header, PostgREST retorna 204 No Content em UPDATE/PATCH — não dá pra diferenciar "atualizou" de "SKU não existe".

Com `return=representation`:
- SKU existe → 200 + array com linha(s) atualizada(s)
- SKU não existe → 200 + array vazio `[]`

Isso vira o guard "não cria variant nova se SKU estranho" + log de WARN no Apps Script.

### 4. Normalizar o valor antes do PATCH

Planilha aceita qualquer lixo na célula: texto, vazio, decimal, negativo. Função `toStock(value)` com guard:

```js
function toStock(value) {
  if (value === '' || value === null || value === undefined) return 0;
  const n = Number(value);
  if (isNaN(n)) return 0;
  return Math.max(0, Math.floor(n));
}
```

Regra operacional: vazio = 0. "Só tem estoque quem está declarado com qty numérica ≥ 0".

### 5. Filtrar por coluna + linha antes de disparar

O trigger dispara pra TODA edição na planilha inteira. Filtros obrigatórios:
- `sheet.getName() !== SHEET_NAME` → return (só aba específica)
- `editedCol !== QTY_COLUMN` → return (só coluna de qty)
- `editedRow <= HEADER_ROW` → return (só data rows abaixo do cabeçalho)

Sem isso, qualquer edição em qualquer aba chama o webhook e a quota acaba.

### 6. Rate limit no batch

`syncAllStock()` itera 100+ linhas. Sem throttle, bate o quota de `UrlFetchApp` (20k/dia mas com rate limiting por minuto). `Utilities.sleep(100)` entre requests resolve.

## Template mínimo

```js
const SUPABASE_URL = 'https://XXX.supabase.co';
const SUPABASE_SERVICE_ROLE_KEY = 'PLACEHOLDER';
const SHEET_NAME = 'ESTOQUE';
const KEY_COL = 2;    // coluna com SKU/ID
const VALUE_COL = 9;  // coluna com valor a sincronizar
const HEADER_ROW = 3;

function onEdit(e) {
  const sheet = e.source.getActiveSheet();
  if (sheet.getName() !== SHEET_NAME) return;
  if (e.range.getColumn() !== VALUE_COL || e.range.getRow() <= HEADER_ROW) return;

  const key = sheet.getRange(e.range.getRow(), KEY_COL).getValue();
  if (!key) return;

  patch(String(key).trim(), normalizeValue(e.range.getValue()));
}

function patch(key, value) {
  const url = SUPABASE_URL + '/rest/v1/TABELA?coluna_chave=eq.' + encodeURIComponent(key);
  const res = UrlFetchApp.fetch(url, {
    method: 'PATCH',
    headers: {
      apikey: SUPABASE_SERVICE_ROLE_KEY,
      Authorization: 'Bearer ' + SUPABASE_SERVICE_ROLE_KEY,
      'Content-Type': 'application/json',
      Prefer: 'return=representation',
    },
    payload: JSON.stringify({ coluna_valor: value }),
    muteHttpExceptions: true,
  });
  const rows = JSON.parse(res.getContentText() || '[]');
  Logger.log((rows.length ? 'OK ' : 'WARN ') + key + ' → ' + value);
}

function installTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'onEdit')
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('onEdit')
    .forSpreadsheet(SpreadsheetApp.getActiveSpreadsheet())
    .onEdit()
    .create();
}
```

## Caso real

Aplicado em [[projects/budamix-ecommerce]] em 2026-04-17 pra sync planilha ESTOQUE → `product_variants.stock`.

Arquivos:
- Script: `~/Documents/05-Projetos-Codigo/budamix-ecommerce/scripts/google-apps-script-stock-sync.js`
- Setup: `~/Documents/05-Projetos-Codigo/budamix-ecommerce/docs/SETUP-STOCK-SYNC.md`

Regras específicas Budamix:
- SKU vazio na planilha → skip
- Qty vazio → stock=0 (regra: "só tem estoque quem declarou na planilha")
- SKU que não existe no Supabase → log WARN, não cria variant novo (inclusão é manual pelo admin)

## Notas relacionadas

- [[projects/budamix-ecommerce]]
- [[memory/sessions/2026-04-17]]

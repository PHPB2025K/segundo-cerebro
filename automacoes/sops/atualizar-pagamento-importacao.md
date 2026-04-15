---
title: "SOP — Atualizar Pagamento Importação"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - sop
  - importacao
  - pagamento
  - gb-import-hub
---

# SOP — Atualizar Pagamento Importação (GB Import Hub)

> Como registrar e atualizar pagamentos de importação no GB Import Hub.

---

## Dados do Sistema

| Campo | Valor |
|-------|-------|
| Sistema | GB Import Hub |
| URL | https://import.budamix.com.br |
| Supabase | `ocxvwwaaqqxecmzhfxhb` |
| Credenciais | 1Password → "gb-import-hub-supabase-*" |

---

## Modelo de Pagamento

Cada importação tem 2 pagamentos independentes:

| Tipo | Momento | % do valor |
|------|---------|:----------:|
| **Numerário** | Na declaração de importação | ~30% |
| **70% Balanço** | Quando container está "finished" | ~70% |

Status possíveis: `pendente` → `pago` → `vencido`

---

## Tabelas Envolvidas

| Tabela | O que guarda |
|--------|-------------|
| `containers` | Dados do container (ID, status logístico, status financeiro) |
| `finance_pagamentos` | Registro de pagamentos (tipo, valor, vencimento, status) |
| `finance_numerario_itens` | Itens individuais de cada numerário |

---

## Passo a Passo

### 1. Verificar status do container

```sql
SELECT container_id, status, payment_status 
FROM containers 
WHERE container_id = 'GB25011';
```

- Status logístico: production → maritime → customs → road → finished
- Status financeiro: independente do logístico

### 2. Registrar pagamento

```sql
INSERT INTO finance_pagamentos (
  container_id, 
  tipo_pagamento, 
  valor_total, 
  data_vencimento, 
  data_pagamento, 
  moeda, 
  status
) VALUES (
  'GB25011',
  '70% balanço',       -- ou 'numerário'
  71419.15,
  '2026-05-24',
  NULL,                -- NULL se ainda não pago
  'BRL',
  'pendente'           -- ou 'pago'
);
```

### 3. Marcar como pago (quando efetuar)

```sql
UPDATE finance_pagamentos 
SET status = 'pago', 
    data_pagamento = '2026-04-11'
WHERE container_id = 'GB25011' 
  AND tipo_pagamento = 'numerário';
```

### 4. Atualizar status financeiro do container

```sql
UPDATE containers 
SET payment_status = 'pagamento_registrado'
WHERE container_id = 'GB25011';
```

### 5. Atualizar pendências e deadlines

- Marcar como ✅ em `memory/context/pendencias.md`
- Atualizar status em `memory/context/deadlines.md`

---

## Pagamentos Ativos (Abril 2026)

| Container | Tipo | Valor | Vencimento | Status |
|-----------|------|-------|------------|--------|
| GB25009 | 70% balanço | R$72.232 | 16/04 | 🔴 CRÍTICO |
| GB25011 | Numerário | R$60.000 | 11/04 | ✅ Pago |
| GB25011 | 70% balanço | R$71.419 | 24/05 | ⏳ Pendente |
| GB26001 | Sinal 30% | — | — | ✅ Pago (valor exato a confirmar) |
| GB26001 | Numerário | — | — | ⏳ Pendente |
| GB26001 | 70% balanço | — | — | ⏳ Pendente |
| GB26002 | Sinal 30% | — | — | ✅ Pago (valor exato a confirmar) |
| GB26002 | Numerário | — | — | ⏳ Pendente |
| GB26002 | 70% balanço | — | — | ⏳ Pendente |

> [!info] Valores pendentes
> Sinal 30% já foi pago para ambos. Valores exatos do sinal, numerário e balanço 70% serão preenchidos pelo Pedro quando disponíveis. Registrar no Supabase (`ocxvwwaaqqxecmzhfxhb`) tabela `finance_pagamentos`.

---

## Edge Functions Relacionadas

| Function | O que faz |
|----------|-----------|
| `extract-import-document` | Extrai NCM/impostos de documentos |
| `calculate-tax-references` | Calcula impacto tributário |

---

## Notas Relacionadas

- [[projects/gb-import-hub]] — ficha do projeto
- [[business/importacao/_index]] — índice importação
- [[knowledge/concepts/credenciais-map]] — credenciais
- [[memory/context/deadlines]] — prazos financeiros

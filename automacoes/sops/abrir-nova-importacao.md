---
title: "SOP — Abrir Nova Importação"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
estimated-time: "30 min"
tags:
  - sop
  - importacao
  - gb-import-hub
  - automacao
---

# SOP — Abrir Nova Importação (GB Import Hub)

## Objetivo

Registrar uma nova importação no GB Import Hub, desde o cadastro do container até a ativação do tracking marítimo.

## Pré-requisitos

- [ ] Acesso ao Import Hub (https://import.budamix.com.br)
- [ ] SERVICE_ROLE_KEY do Supabase (`ocxvwwaaqqxecmzhfxhb`) — ver 1Password: "gb-import-hub-supabase-service-role"
- [ ] Dados do fornecedor (nome, cidade, país)
- [ ] Bill of Lading (BL) ou booking number
- [ ] Valor da carga (BRL e USD)
- [ ] Data de embarque e ETA estimado

---

## Procedimento

### Passo 1 — Criar container no Supabase

Tabela: `containers`. Código segue padrão `GB` + 5 dígitos (ex: GB26003).

**Campos obrigatórios:**

| Campo | Tipo | Exemplo |
|-------|------|---------|
| `code` | TEXT UNIQUE | "GB26003" |
| `status` | TEXT | "production" (sempre começa aqui) |
| `supplier` | TEXT | "Skiway" |
| `country` | TEXT | "China" |
| `city` | TEXT | "Yiwu" |
| `port` | TEXT | "Ningbo" |
| `embark_date` | DATE | "2026-05-15" |
| `eta` | DATE | "2026-07-01" |
| `cargo_description` | TEXT | "Glass pots, ceramic bowls" |
| `cargo_value_usd` | DECIMAL | 10000.00 |

**Campos opcionais (preencher quando disponíveis):**
- `vessel_name`, `vessel_imo`, `vessel_mmsi`
- `bill_of_lading`, `scac_code`, `carrier_name`
- `booking_number`, `reference`, `observations`

Via frontend: https://import.budamix.com.br → Novo Container

### Passo 2 — Criar registro de pagamentos

Tabela: `finance_pagamentos`. Um registro por container (UNIQUE).

| Pagamento | Campo valor | Campo vencimento | Campo status | Quando preencher |
|-----------|-------------|-----------------|-------------|-----------------|
| **Sinal 30%** | `payment_30_signal_value` | `payment_30_signal_due_date` | `payment_30_signal_status` | Na abertura |
| **Numerário** | `payment_numerario_value` | `payment_numerario_due_date` | `payment_numerario_status` | Quando DI pronta |
| **70% Balanço** | `payment_70_balance_value` | `payment_70_balance_due_date` | `payment_70_balance_status` | Quando container finished |

Status: `pending` → `paid` → `overdue`

Inicialmente, setar sinal 30% com valor e data. Numerário e 70% ficam `pending` com valores `null` até disponíveis.

### Passo 3 — Upload de documentos

Tabela: `documents`. Storage bucket: `container-documents`.

**Tipos de documento (document_tag):**

| Tag | Obrigatório | Quando |
|-----|:-----------:|--------|
| Invoice | ✅ | Na abertura |
| Proforma Invoice | 🟡 | Se diferente da final |
| Packing List | ✅ | Na abertura |
| Bill of Lading | ✅ | Quando disponível |
| Declaracao de Importacao | ✅ | Na chegada (DI) |
| XML da DI | ✅ | Com a DI |
| PNI | ✅ | Para conferência de numerário |
| Inspection Report | ⚪ | Se houver inspeção |
| Sales Contract | ⚪ | Se houver contrato |

Processo: upload no bucket → registrar metadata na tabela `documents`.

### Passo 4 — Ativar tracking Terminal49

Quando o BL estiver disponível:

1. **Buscar** container no Terminal49 via Edge Function `terminal49-search` (BL + carrier)
2. **Associar** container via `terminal49-associate` (container UUID + T49 shipment ID)
3. **Registrar webhook** via `terminal49-register-webhook`

O webhook recebe updates automaticamente e cria registros em `container_milestones` e `tracking_alerts`.

### Passo 5 — Extrair dados fiscais (quando DI disponível)

Via Edge Function `extract-import-document`:
- Upload do PDF da DI
- Extração automática: NCM, alíquotas (II, IPI, PIS, COFINS), valores

Via `fetch-ncm-aliquotas` para consulta manual de NCM.

### Passo 6 — Registrar numerário (quando PNI disponível)

1. Atualizar `finance_pagamentos` com valor e vencimento do numerário
2. Registrar cada item na tabela `finance_numerario_itens`

**Categorias de numerário (ENUM):**
- IMPOSTOS_FEDERAIS, CREDITOS_FISCAIS, TAXAS_ADUANEIRAS
- ARMAZENAGEM, TRANSPORTE_RODOVIARIO, DESCONSOLIDACAO
- SERVICOS_DESPACHANTE, SERVICOS_TRADING, SEGURO_NACIONAL
- SERVICOS_PORTO, OUTROS_CUSTOS, RECEITAS

### Passo 7 — Acompanhar ciclo de vida

**Ciclo logístico** (atualizar `containers.status`):
```
production → maritime → customs → road → finished
```

**Ciclo financeiro** (independente do logístico):
```
Sinal 30% → Numerário → 70% Balanço (cada um: pending → paid)
```

---

## Verificação

- [ ] Container criado com código único (GB+5 dígitos)
- [ ] Status inicial = "production"
- [ ] Registro de pagamentos criado (sinal 30% com valor e data)
- [ ] Documentos iniciais uploadados (Invoice, Packing List)
- [ ] Tracking Terminal49 ativado (quando BL disponível)
- [ ] Pendências registradas no vault (`memory/context/pendencias.md`)
- [ ] Deadlines registrados (`memory/context/deadlines.md`)

## Troubleshooting

| Problema | Causa provável | Solução |
|----------|---------------|---------|
| Terminal49 não encontra container | BL incorreto ou carrier errado | Verificar BL com trading (Open Trade) |
| `terminal49-fetch-shipment` retorna HTTP 500 | Bug conhecido (skill v2) | Usar `poll-terminal49` como alternativa |
| Webhook não recebe updates | Webhook URL incorreta ou não registrada | Re-registrar via `terminal49-register-webhook` |
| DI extraction com confiança baixa | PDF mal formatado | Verificar manualmente e corrigir dados |

## Referências

- [[projects/gb-import-hub]] — ficha do projeto
- [[automacoes/sops/atualizar-pagamento-importacao]] — SOP pagamentos
- [[business/importacao/_index]] — índice importação
- [[knowledge/concepts/credenciais-map]] — credenciais (7 items GB Import Hub)
- [[memory/context/deadlines]] — prazos financeiros

---
name: gb-import-hub
description: "Skill para acessar, consultar e gerenciar o sistema GB Import Hub (controle de importacoes da GB Importadora/Budamix). Use SEMPRE que o Pedro mencionar: containers, embarques, importacoes, rastreio de navio, tracking, numerario, PNI, DI, conferencias de importacao, custos de desembaraco, pagamentos de container, Terminal49, status de container, GB25xxx, NCM, aliquotas, documentos de importacao, Bill of Lading, ETA de navio, ou qualquer assunto relacionado a operacoes de comercio exterior. Tambem ative quando Pedro pedir relatorios financeiros de importacao, status de pagamentos (sinal 30%, numerario, balanco 70%), tracking de vessel, ou analise de custos de nacionalizacao. Este skill da acesso de leitura e escrita as 12 tabelas do Supabase do Import Hub via API REST."
---

# GB Import Hub - Skill de Acesso ao Sistema de Importacoes

## CONEXAO

**Supabase Project**: `ocxvwwaaqqxecmzhfxhb`
**URL**: `https://ocxvwwaaqqxecmzhfxhb.supabase.co`
**Credenciais**: 1Password (vault OpenClaw)
  - `gb-import-hub-supabase-service-role` - SERVICE_ROLE_KEY (leitura + escrita, bypassa RLS)
  - `gb-import-hub-supabase-anon` - ANON_KEY (respeita RLS, usar quando possivel)

**Frontend**: `https://import.budamix.com.br`

### Como conectar

```bash
SERVICE_KEY=$(op item get "gb-import-hub-supabase-service-role" --vault "OpenClaw" --fields password --reveal)
ANON_KEY=$(op item get "gb-import-hub-supabase-anon" --vault "OpenClaw" --fields password --reveal)
URL="https://ocxvwwaaqqxecmzhfxhb.supabase.co"
```

### Regra de keys
- **Leitura de dados operacionais** (containers, documents, finance, tracking): ANON_KEY funciona
- **Leitura de referencias** (referencias_mercado, referencias_ncm): SERVICE_ROLE_KEY
- **Escrita em qualquer tabela**: SEMPRE usar SERVICE_ROLE_KEY
- **Conferencias** (conferencias_numerario, conferencias_comunicacoes): SERVICE_ROLE_KEY

---

## SCHEMA - 12 TABELAS

Ver `references/schema-tables.md` e `references/schema-relationships.md` para detalhes.

| Tabela | Funcao | Leitura | Escrita |
|--------|--------|---------|---------|
| containers | Entidade central - embarques | ANON | SERVICE |
| documents | Documentos por container | ANON | SERVICE |
| finance_pagamentos | Pagamentos 30%/numerario/70% | ANON | SERVICE |
| finance_numerario_itens | Breakdown do numerario (PNI) | ANON | SERVICE |
| conferencias_numerario | Conferencia custos (DI vs PNI vs Simulacao) | SERVICE | SERVICE |
| conferencias_comunicacoes | Historico comunicacao com trading | SERVICE | SERVICE |
| referencias_mercado | Referencia custos de mercado | SERVICE | SERVICE |
| referencias_ncm | Aliquotas por NCM | SERVICE | SERVICE |
| vessel_tracking | Rastreio de navios | ANON | SERVICE |
| vessel_position_history | Historico posicoes GPS | ANON | SERVICE |
| tracking_alerts | Alertas de mudanca de ETA | ANON | SERVICE |
| container_milestones | Marcos do container (Terminal49) | ANON | SERVICE |

### Entidade central: containers

Tudo gira em torno da tabela `containers`. Cada container tem um `code` unico (ex: GB25011) e um `status` que segue o fluxo:

```
production -> maritime -> customs -> road -> finished
```

Relacionamentos:
- 1:N -> documents
- 1:1 -> finance_pagamentos
- 1:1 -> vessel_tracking
- 1:N -> tracking_alerts
- 1:N -> container_milestones

---

## REGRAS DE NEGOCIO - CICLOS INDEPENDENTES

### Ciclo Logistico vs Ciclo Financeiro

Um container tem DOIS ciclos independentes que NAO se confundem:

| Ciclo | Campo | Valores | O que indica |
|-------|-------|---------|--------------|
| Logistico | containers.status | production->maritime->customs->road->finished | Onde a mercadoria esta fisicamente |
| Financeiro | finance_pagamentos.*_status | pending / paid / overdue | Se os pagamentos foram quitados |

**REGRA FUNDAMENTAL**: um container com status `finished` NAO significa processo encerrado. O processo so esta 100% concluido quando o status logistico e `finished` E os 3 pagamentos (30% sinal, numerario, 70% balanco) estao `paid`.

### Status Real do Processo (campo derivado)

O Import Hub nao tem um campo "status real" no banco. Derivar cruzando os dois ciclos:

| Status Logistico | Status Financeiro | -> Status Real |
|-----------------|-------------------|----------------|
| finished | 3/3 pagos | ENCERRADO |
| finished | 1+ pendentes | PENDENTE FINANCEIRO |
| production/maritime/customs/road | 3/3 pagos | PENDENTE LOGISTICO |
| production/maritime/customs/road | 1+ pendentes | EM ANDAMENTO |
| qualquer | 1+ overdue | ATENCAO - PAGAMENTO ATRASADO |

### Logica para derivar

```
Para cada container:
  logistico_finished = (containers.status == "finished")
  pagamentos = [30%_status, numerario_status, 70%_status]
  
  Pagamentos sem valor (NULL) = "nao aplicavel" (nao contam como pendentes)
  
  algum_atrasado = algum == "overdue"
  todos_pagos = todos com valor != null estao "paid"
  algum_pendente = algum com valor != null esta "pending"

  SE algum_atrasado -> "ATENCAO - PAGAMENTO ATRASADO"
  SE logistico_finished E todos_pagos -> "ENCERRADO"
  SE logistico_finished E algum_pendente -> "PENDENTE FINANCEIRO"
  SE NAO logistico_finished E todos_pagos -> "PENDENTE LOGISTICO"
  SENAO -> "EM ANDAMENTO"
```

### Alertas Financeiros Automaticos

Alertar proativamente quando:
1. Pagamento vence em 7 dias ou menos + status pending -> Thread 7 (Financeiro)
2. Container finished com pagamento pending -> Thread 7
3. Pagamento overdue -> Thread 8 (Urgente)
4. Numerario pendente + ETA em menos de 5 dias -> Thread 7

---

## OPERACOES COMUNS (15)

### 1. Listar containers
```bash
curl -s "$URL/rest/v1/containers?select=code,status,supplier,eta,vessel_name,tracking_status&order=eta.asc" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 2. Detalhes container
```bash
curl -s "$URL/rest/v1/containers?code=eq.GB25011&select=*" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 3. Pagamentos com join
```bash
curl -s "$URL/rest/v1/finance_pagamentos?select=*,containers(code,status)" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 4. Tracking de navio com join
```bash
curl -s "$URL/rest/v1/vessel_tracking?select=vessel_name,latitude,longitude,predicted_eta,pod_name,containers(code)" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 5. Alertas com join
```bash
curl -s "$URL/rest/v1/tracking_alerts?select=alert_type,severity,message,containers(code)&order=created_at.desc&limit=10" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 6. Documentos com join
```bash
curl -s "$URL/rest/v1/documents?select=file_name,document_tag,containers(code)&order=uploaded_at.desc" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 7. NCM aliquotas
```bash
curl -s "$URL/rest/v1/referencias_ncm?ncm=eq.7013.49.00&select=*" \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY"
```

### 8. Referencias de mercado
```bash
curl -s "$URL/rest/v1/referencias_mercado?ativo=eq.true&select=codigo,descricao,valor_minimo,valor_maximo,percentual" \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY"
```

### 9. Atualizar status container
```bash
curl -s "$URL/rest/v1/containers?code=eq.GB25011" -X PATCH \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY" \
  -H "Content-Type: application/json" -H "Prefer: return=representation" \
  -d '{"status": "customs"}'
```

### 10. Registrar pagamento como pago
```bash
curl -s "$URL/rest/v1/finance_pagamentos?container_id=eq.UUID" -X PATCH \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY" \
  -H "Content-Type: application/json" -H "Prefer: return=representation" \
  -d '{"payment_30_signal_status": "paid", "payment_30_signal_paid_date": "2026-04-08"}'
```

### 11. Inserir novo container
```bash
curl -s "$URL/rest/v1/containers" -X POST \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY" \
  -H "Content-Type: application/json" -H "Prefer: return=representation" \
  -d '{"code":"GB26003","status":"production","supplier":"Skiway","country":"China","city":"Yiwu","port":"Ningbo","embark_date":"2026-05-15","eta":"2026-07-01"}'
```

### 12. Milestones de container
```bash
curl -s "$URL/rest/v1/container_milestones?container_id=eq.UUID&select=milestone_type,location,vessel_name,timestamp&order=timestamp.desc&limit=10" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

### 13. Conferencias de numerario
```bash
curl -s "$URL/rest/v1/conferencias_numerario?select=numero_di,processo_interno,total_di,total_pni,total_excesso,status&order=created_at.desc" \
  -H "apikey: $SERVICE_KEY" -H "Authorization: Bearer $SERVICE_KEY"
```

### 14. Edge Functions
```bash
# Polling Terminal49
curl -s "$URL/functions/v1/poll-terminal49" \
  -H "Authorization: Bearer $SERVICE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"containerId": "UUID"}'

# NCM aliquotas
curl -s "$URL/functions/v1/fetch-ncm-aliquotas" \
  -H "Authorization: Bearer $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ncm": "7013.49.00"}'

# Mapbox token
curl -s "$URL/functions/v1/get-mapbox-token"
```

### 15. Status real do processo (ciclo logistico + financeiro)
```bash
curl -s "$URL/rest/v1/finance_pagamentos?select=payment_30_signal_status,payment_30_signal_value,payment_30_signal_due_date,payment_numerario_status,payment_numerario_value,payment_numerario_due_date,payment_70_balance_status,payment_70_balance_value,payment_70_balance_due_date,containers(code,status,eta)&order=containers(eta).asc" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"
```

Aplicar logica de derivacao da secao "REGRAS DE NEGOCIO" para classificar cada container.

---

## EDGE FUNCTIONS - 17

| Function | Metodo | JWT | Uso |
|----------|--------|-----|-----|
| extract-import-document | POST | sim | Extracao de dados de documentos (IA) |
| calculate-tax-references | POST | sim | Calculo referencias tributarias |
| fetch-ncm-aliquotas | POST | sim | Aliquotas por NCM |
| fetch-ncm-aliquotas-web | POST | sim | Aliquotas NCM via web |
| fetch-market-references | POST | sim | Referencias de custo de mercado |
| fetch-vessel-position | POST | sim | Posicao do navio |
| fetch-container-map | POST | nao | Dados para mapa |
| get-mapbox-token | GET | nao | Token do Mapbox |
| update-vessel-positions | POST | sim | Atualizar posicoes |
| terminal49-search | POST | sim | Buscar container no T49 |
| terminal49-associate | POST | sim | Associar container ao T49 |
| terminal49-fetch-shipment | POST | sim | Detalhes de shipment |
| terminal49-register-webhook | POST | sim | Registrar webhook |
| terminal49-webhook | POST | nao | Receptor webhook |
| poll-terminal49 | POST | sim | Polling manual |
| create-tracking-request | POST | sim | Criar request tracking |
| send-eta-alert | POST | sim | Alerta ETA por email |

---

## REGRAS DE SEGURANCA

1. NUNCA logar keys em arquivos, outputs ou mensagens
2. Preferir ANON_KEY para leitura quando RLS permitir
3. NUNCA deletar containers ou pagamentos sem aprovacao do Pedro
4. Validar antes de escrever: confirmar com Pedro antes de atualizar status/pagamento
5. Formato datas: ISO 8601 (YYYY-MM-DD)
6. Formato monetario: DECIMAL com ponto (Supabase usa ponto)
7. Status container validos: production, maritime, customs, road, finished
8. Status pagamento validos: pending, paid, overdue
9. Container code pattern: GB + 5 digitos (GB25011, GB26002)

---

## REPORTING - THREADS TELEGRAM

| Assunto | Thread |
|---------|--------|
| Containers, tracking, ETA | Thread 4 (Importacao) |
| Pagamentos, custos, numerario | Thread 7 (Financeiro) |
| Alertas urgentes | Thread 8 (Urgente) |
| Conferencias com trading | Thread 4 (Importacao) |

---

## CONTEXTO DE NEGOCIO

- Empresa: GB Importadora (marca Budamix)
- Sourcing: Yiwu, China (utensilios domesticos - vidro, ceramica, porcelana)
- Portos: Itajai e Itapoa (SC)
- Trading: Open Trade | ICMS 4%
- TTD: 409 (Itajai-SC, beneficio fiscal ICMS)
- Fluxo de pagamento: 30% sinal (antes embarque) -> Numerario (despesas nacionalizacao) -> 70% balanco (apos desembaraco)
- Ciclos independentes: logistico (production->finished) e financeiro (3 pagamentos pending->paid). Processo so encerra quando AMBOS completos.
- Containers ativos: GB25007 a GB26002 (7 no sistema)

---
## Referências
- [[skills/gb-import-hub/references/schema-tables|Schema de Tabelas]]

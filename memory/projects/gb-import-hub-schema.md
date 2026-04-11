# GB Import Hub — Schema Completo do Banco de Dados

> Extraido de: repo PHPB2025K/gb-import-hub (27 migrations + types.ts)
> Supabase Cloud (Lovable): project_id usfilmvbckfnbfnpvrph
> Data: 08/04/2026
> Objetivo: migrar para Supabase externo

---

## 1. TABELAS (10 tabelas)

### 1.1 containers (principal)

```sql
CREATE TABLE public.containers (
  id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL CHECK (status IN ('production', 'maritime', 'customs', 'road', 'finished')),
  supplier TEXT NOT NULL,
  country TEXT NOT NULL,
  city TEXT NOT NULL,
  port TEXT NOT NULL,
  embark_date DATE NOT NULL,
  eta DATE NOT NULL,
  registered_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  cargo_description TEXT,
  cargo_value TEXT,
  cargo_value_usd DECIMAL(15, 2),
  observations TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  -- Payment flags (legacy, replaced by finance_pagamentos)
  payment_30_signal BOOLEAN DEFAULT FALSE,
  payment_numerario BOOLEAN DEFAULT FALSE,
  payment_70_balance BOOLEAN DEFAULT FALSE,
  -- Vessel
  vessel_name VARCHAR(100),
  vessel_imo VARCHAR(20),
  vessel_mmsi VARCHAR(20),
  -- Terminal49 tracking
  bill_of_lading VARCHAR(50),
  scac_code VARCHAR(10),
  terminal49_shipment_id VARCHAR(100),
  tracking_status VARCHAR DEFAULT 'draft' CHECK (tracking_status IN ('draft', 'tracking_enabled', 'archived')),
  booking_number VARCHAR,
  carrier_name VARCHAR,
  reference VARCHAR
);
```

**Indexes:** idx_containers_status, idx_containers_code

### 1.2 documents

```sql
CREATE TABLE public.documents (
  id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  container_id UUID NOT NULL REFERENCES containers(id) ON DELETE CASCADE,
  file_name TEXT NOT NULL,
  file_size BIGINT NOT NULL,
  file_type TEXT NOT NULL,
  file_url TEXT NOT NULL,
  uploaded_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  document_tag TEXT NOT NULL DEFAULT 'Invoice'
  -- Tags validas: Invoice, Proforma Invoice, Packing List, Inspection Report,
  -- Sales Contract, Bill of Lading, Declaracao de Importacao, XML da DI
);
```

**Index:** idx_documents_container_id

### 1.3 finance_pagamentos

```sql
CREATE TABLE finance_pagamentos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  container_id UUID NOT NULL REFERENCES containers(id) ON DELETE CASCADE UNIQUE,
  -- Payment 1: 30% Signal
  payment_30_signal_value DECIMAL(15,2),
  payment_30_signal_due_date DATE,
  payment_30_signal_paid_date DATE,
  payment_30_signal_status TEXT DEFAULT 'pending' CHECK (... IN ('pending', 'paid', 'overdue')),
  payment_30_signal_receipt_url TEXT,
  payment_30_signal_usd_value NUMERIC(12,2),
  payment_30_signal_exchange_rate NUMERIC(10,4),
  payment_30_signal_manual_override BOOLEAN DEFAULT FALSE,
  -- Payment 2: Numerario
  payment_numerario_value DECIMAL(15,2),
  payment_numerario_due_date DATE,
  payment_numerario_paid_date DATE,
  payment_numerario_status TEXT DEFAULT 'pending',
  payment_numerario_receipt_url TEXT,
  payment_numerario_pni_url TEXT,
  payment_numerario_usd_value NUMERIC(12,2),
  payment_numerario_exchange_rate NUMERIC(10,4),
  payment_numerario_manual_override BOOLEAN DEFAULT FALSE,
  -- Payment 3: 70% Balance
  payment_70_balance_value DECIMAL(15,2),
  payment_70_balance_due_date DATE,
  payment_70_balance_paid_date DATE,
  payment_70_balance_status TEXT DEFAULT 'pending',
  payment_70_balance_receipt_url TEXT,
  payment_70_balance_usd_value NUMERIC(12,2),
  payment_70_balance_exchange_rate NUMERIC(10,4),
  payment_70_balance_manual_override BOOLEAN DEFAULT FALSE,
  -- Metadata
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Realtime:** Habilitado (ALTER PUBLICATION supabase_realtime ADD TABLE finance_pagamentos)
**Trigger:** update_finance_pagamentos_updated_at (BEFORE UPDATE)

### 1.4 finance_numerario_itens

```sql
CREATE TABLE finance_numerario_itens (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pagamento_id UUID NOT NULL REFERENCES finance_pagamentos(id) ON DELETE CASCADE,
  categoria finance_categoria_numerario NOT NULL,
  descricao TEXT NOT NULL,
  valor DECIMAL(15,2) NOT NULL,
  linha_numero INT,
  codigo_item TEXT,
  observacao TEXT,
  documento_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.5 conferencias_numerario

```sql
CREATE TABLE conferencias_numerario (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id),
  -- Identificacao
  numero_di VARCHAR(50) NOT NULL,
  numero_processo VARCHAR(100),
  trading_company VARCHAR(200),
  processo_interno VARCHAR(50),
  processo_trading VARCHAR(100),
  fornecedor VARCHAR(200),
  incoterm VARCHAR(10),
  porto_origem VARCHAR(100),
  porto_destino VARCHAR(100),
  tipo_container VARCHAR(5),
  -- Dados extraidos (JSON completo)
  dados_di JSONB NOT NULL,
  dados_pni JSONB NOT NULL,
  dados_simulacao JSONB,
  -- URLs
  arquivo_di_url TEXT,
  arquivo_pni_url TEXT,
  arquivo_simulacao_url TEXT,
  -- Metadados da extracao
  confianca_extracao_di DECIMAL(5,2),
  confianca_extracao_pni DECIMAL(5,2),
  confianca_extracao_simulacao DECIMAL(5,2),
  campos_editados_manualmente JSONB DEFAULT '[]',
  -- Resultados
  total_di DECIMAL(15,2),
  total_pni DECIMAL(15,2),
  total_simulado DECIMAL(15,2),
  total_excesso DECIMAL(15,2),
  percentual_excesso DECIMAL(5,2),
  quantidade_alertas INTEGER DEFAULT 0,
  alertas JSONB DEFAULT '[]',
  -- Etapas
  etapa_atual VARCHAR(20) DEFAULT 'pre',
  decisao_pre VARCHAR(20) DEFAULT 'pendente',
  decisao_intermediaria VARCHAR(20) DEFAULT 'pendente',
  decisao_pos VARCHAR(20) DEFAULT 'pendente',
  -- Financeiro
  economia_identificada DECIMAL(15,2) DEFAULT 0,
  economia_negociada DECIMAL(15,2) DEFAULT 0,
  -- Status e comunicacao
  status VARCHAR(30) DEFAULT 'pendente',
  email_enviado BOOLEAN DEFAULT FALSE,
  data_email TIMESTAMPTZ,
  resposta_trading TEXT,
  data_resposta TIMESTAMPTZ,
  -- Resolucao
  valor_credito_obtido DECIMAL(15,2),
  observacoes TEXT,
  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.6 conferencias_comunicacoes

```sql
CREATE TABLE conferencias_comunicacoes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conferencia_id UUID REFERENCES conferencias_numerario(id) ON DELETE CASCADE,
  etapa VARCHAR(20) NOT NULL,
  tipo VARCHAR(30) NOT NULL,
  conteudo TEXT,
  data_envio TIMESTAMPTZ,
  resposta TEXT,
  data_resposta TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.7 referencias_mercado

```sql
CREATE TABLE referencias_mercado (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  codigo VARCHAR(50) NOT NULL UNIQUE,
  descricao VARCHAR(300) NOT NULL,
  valor_minimo DECIMAL(10,2),
  valor_maximo DECIMAL(10,2),
  valor_fixo DECIMAL(10,2),
  percentual DECIMAL(5,2),
  tipo_container VARCHAR(10),
  base_calculo VARCHAR(50),
  formula TEXT,
  fonte VARCHAR(200),
  ultima_atualizacao DATE,
  ativo BOOLEAN DEFAULT TRUE,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Seed data:** 16 registros (liberacao_bl, thd_capatazia, desp_zp, desembaraco, armazenagem, pesagem, sindicato, afrmm, conta_ordem, demurrage, detention, frete_internacional, frete_nacional)

### 1.8 referencias_ncm

```sql
CREATE TABLE public.referencias_ncm (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ncm VARCHAR(10) NOT NULL UNIQUE,
  descricao VARCHAR(255),
  aliquota_ii DECIMAL,
  aliquota_ipi DECIMAL,
  aliquota_pis DECIMAL,
  aliquota_cofins DECIMAL,
  ex_tarifario VARCHAR(10),
  fonte VARCHAR(100),
  confianca TEXT DEFAULT 'media',
  requer_revisao BOOLEAN DEFAULT false,
  fonte_ii TEXT,
  fonte_ipi TEXT,
  data_atualizacao DATE,
  ativo BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### 1.9 vessel_tracking

```sql
CREATE TABLE vessel_tracking (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  container_id UUID NOT NULL REFERENCES containers(id) ON DELETE CASCADE UNIQUE,
  vessel_name VARCHAR(100),
  vessel_imo VARCHAR(20),
  vessel_mmsi VARCHAR(20),
  latitude DECIMAL(10,6),
  longitude DECIMAL(10,6),
  speed_knots DECIMAL(5,2),
  course DECIMAL(5,2),
  position_timestamp TIMESTAMPTZ,
  predicted_eta TIMESTAMPTZ,
  eta_confidence VARCHAR(20) DEFAULT 'medium',
  destination_port VARCHAR(100),
  last_api_call TIMESTAMPTZ DEFAULT NOW(),
  api_provider VARCHAR(50) DEFAULT 'marinetraffic',
  -- Terminal49
  terminal49_tracking_id VARCHAR(100),
  pod_eta TIMESTAMPTZ,
  pod_ata TIMESTAMPTZ,
  last_free_day DATE,
  available_for_pickup BOOLEAN DEFAULT FALSE,
  holds JSONB,
  -- Port coordinates
  pod_latitude NUMERIC,
  pod_longitude NUMERIC,
  pod_name VARCHAR,
  pol_latitude NUMERIC,
  pol_longitude NUMERIC,
  pol_name VARCHAR,
  -- Error tracking
  tracking_error VARCHAR,
  tracking_error_at TIMESTAMPTZ,
  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.10 vessel_position_history

```sql
CREATE TABLE vessel_position_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tracking_id UUID NOT NULL REFERENCES vessel_tracking(id) ON DELETE CASCADE,
  latitude DECIMAL(10,6) NOT NULL,
  longitude DECIMAL(10,6) NOT NULL,
  speed_knots DECIMAL(5,2),
  course DECIMAL(5,2),
  timestamp TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.11 tracking_alerts

```sql
CREATE TABLE tracking_alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  container_id UUID NOT NULL REFERENCES containers(id) ON DELETE CASCADE,
  alert_type VARCHAR(50) NOT NULL, -- 'eta_delay', 'eta_advance', 'arrival', 'departure'
  severity VARCHAR(20) NOT NULL DEFAULT 'info', -- 'info', 'warning', 'critical'
  message TEXT NOT NULL,
  previous_eta TIMESTAMPTZ,
  new_eta TIMESTAMPTZ,
  difference_hours INTEGER,
  is_read BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 1.12 container_milestones

```sql
CREATE TABLE container_milestones (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  container_id UUID NOT NULL REFERENCES containers(id) ON DELETE CASCADE,
  milestone_type VARCHAR(50) NOT NULL,
  location VARCHAR(200),
  vessel_name VARCHAR(100),
  voyage_number VARCHAR(50),
  timestamp TIMESTAMPTZ NOT NULL,
  raw_data JSONB,
  lat NUMERIC,
  lng NUMERIC,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 2. ENUM TYPES

```sql
CREATE TYPE finance_categoria_numerario AS ENUM (
  'IMPOSTOS_FEDERAIS', 'CREDITOS_FISCAIS', 'TAXAS_ADUANEIRAS',
  'ARMAZENAGEM', 'TRANSPORTE_RODOVIARIO', 'DESCONSOLIDACAO',
  'SERVICOS_DESPACHANTE', 'SERVICOS_TRADING', 'SEGURO_NACIONAL',
  'SERVICOS_PORTO', 'OUTROS_CUSTOS', 'RECEITAS'
);
```

---

## 3. RELACIONAMENTOS (Foreign Keys)

```
containers (1) ---> (N) documents
containers (1) ---> (1) finance_pagamentos
containers (1) ---> (1) vessel_tracking
containers (1) ---> (N) tracking_alerts
containers (1) ---> (N) container_milestones
finance_pagamentos (1) ---> (N) finance_numerario_itens
conferencias_numerario (1) ---> (N) conferencias_comunicacoes
vessel_tracking (1) ---> (N) vessel_position_history
conferencias_numerario (N) ---> (1) auth.users (user_id)
```

---

## 4. RLS POLICIES

| Tabela | Policy | Tipo |
|--------|--------|------|
| containers | Public access (all ops) | Permissiva |
| documents | Public access (all ops) | Permissiva |
| finance_pagamentos | Public access (all ops) | Permissiva |
| finance_numerario_itens | Public access (all ops) | Permissiva |
| vessel_tracking | Public access (all ops) | Permissiva |
| vessel_position_history | Public access (all ops) | Permissiva |
| tracking_alerts | Public access (all ops) | Permissiva |
| container_milestones | Public access (all ops) | Permissiva |
| conferencias_numerario | **Per-user (auth.uid() = user_id)** | Restritiva |
| conferencias_comunicacoes | **Herda do dono da conferencia** | Restritiva |
| referencias_mercado | **Read-only (authenticated)** | Restritiva |
| referencias_ncm | **Read-only (authenticated)** | Restritiva |

---

## 5. FUNCTIONS E TRIGGERS

```sql
-- Trigger function (reusada por varias tabelas)
CREATE FUNCTION update_finance_pagamentos_updated_at() RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = NOW(); RETURN NEW; END; $$ LANGUAGE plpgsql;

-- Triggers
finance_pagamentos -> trigger_finance_pagamentos_updated_at
conferencias_numerario -> update_conferencias_numerario_updated_at
referencias_mercado -> update_referencias_mercado_updated_at
vessel_tracking -> update_vessel_tracking_updated_at
```

---

## 6. EXTENSIONS

```sql
CREATE EXTENSION IF NOT EXISTS pg_cron WITH SCHEMA pg_catalog;
CREATE EXTENSION IF NOT EXISTS pg_net WITH SCHEMA public;
```

---

## 7. STORAGE BUCKETS

| Bucket | Publico | Policies |
|--------|---------|----------|
| container-documents | Sim | Read + Insert publico |

---

## 8. REALTIME

| Tabela | Status |
|--------|--------|
| finance_pagamentos | Habilitado |

---

## 9. EDGE FUNCTIONS (17 funcoes)

| Funcao | Proposito |
|--------|-----------|
| calculate-tax-references | Calculo de referencias tributarias |
| create-tracking-request | Criar request de tracking |
| extract-import-document | Extracao de dados de documentos (IA) |
| fetch-container-map | Mapa de containers |
| fetch-market-references | Referencias de mercado |
| fetch-ncm-aliquotas | Aliquotas por NCM |
| fetch-ncm-aliquotas-web | Aliquotas NCM via web |
| fetch-vessel-position | Posicao do navio |
| get-mapbox-token | Token do Mapbox |
| poll-terminal49 | Polling Terminal49 |
| send-eta-alert | Envio de alerta de ETA |
| terminal49-associate | Associar container ao Terminal49 |
| terminal49-fetch-shipment | Buscar shipment no Terminal49 |
| terminal49-register-webhook | Registrar webhook Terminal49 |
| terminal49-search | Busca no Terminal49 |
| terminal49-webhook | Receptor de webhook Terminal49 |
| update-vessel-positions | Atualizar posicoes dos navios |

---

## 10. SEED DATA

**referencias_mercado:** 16 registros padrao de custos de importacao (THD, capatazia, desembaraco, armazenagem, AFRMM, sindicato, frete, etc.)

---

## 11. ESTRUTURAL vs LOVABLE BOILERPLATE

### Estrutural (especifico do GB Import Hub — MANTER)
- **containers** — core do sistema, rastreio de embarques
- **documents** — documentos de importacao por container
- **finance_pagamentos** — pagamentos 30/70/numerario por container
- **finance_numerario_itens** — breakdown do numerario (PNI)
- **conferencias_numerario** — conferencia de custos (DI vs PNI vs Simulacao)
- **conferencias_comunicacoes** — historico de comunicacao com trading
- **referencias_mercado** — referencia de custos de mercado
- **referencias_ncm** — aliquotas por NCM
- **vessel_tracking** — rastreio de navios
- **vessel_position_history** — historico de posicoes GPS
- **tracking_alerts** — alertas de mudanca de ETA
- **container_milestones** — marcos do container (Terminal49)
- **Enum finance_categoria_numerario** — categorias de custos
- **Storage bucket container-documents** — armazenamento de documentos
- **Todas as 17 Edge Functions** — logica de negocio

### Lovable Boilerplate (pode ser descartado/recriado)
- `src/integrations/supabase/client.ts` — gerado automaticamente, recriar com novas credenciais
- `src/integrations/supabase/types.ts` — regenerar apos migration no novo Supabase

---

## 12. DADOS EM PRODUCAO A MIGRAR

Precisam ser migrados do Lovable Cloud para o Supabase externo:
- Containers cadastrados (GB25001 a GB25011+)
- Documentos uploadados (storage bucket)
- Pagamentos registrados
- Itens de numerario
- Conferencias com dados de DI/PNI
- Referencias de mercado (seed + atualizacoes)
- Referencias NCM
- Historico de tracking/posicoes
- Alertas e milestones

---

*Extraido em 08/04/2026 por Kobe via Claude Code*

---

## Ver também

- [[memory/projects/gb-import-hub-edge-functions-map|GB Import Hub — Edge Functions Map]]
- [[memory/projects/gb-import-hub-reconnection-plan|GB Import Hub — Plano de Reconexão do Frontend]]

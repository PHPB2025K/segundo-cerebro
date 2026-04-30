---
title: "Card de Inventário Total — Home Budamix Central"
created: 2026-04-30
type: plan
status: active
tags:
  - project
  - budamix-central
  - dashboard
  - inventory
  - plano
---

# Card de Inventário Total na Home

## Objetivo

Adicionar uma seção dedicada na home do Budamix Central, **logo abaixo de "Participação por canal"**, com 3 cards lado a lado mostrando em tempo real:

| Card | Conteúdo | Fonte |
|------|---------|-------|
| **Estoque FULL** | Custo, qty, SKUs únicos consolidados | `fulfillment_inventory` (Supabase) — soma dos 3 marketplaces |
| **Estoque FÍSICO** | Custo, qty, SKUs únicos do galpão | `physical_inventory_summary` (Supabase, snapshot da planilha) |
| **TOTAL** | Soma dos dois | Calculado |

Hoje (30/04): Custo Full = R$ 158.820. Custo Físico = a calcular via planilha.

## Decisões já alinhadas

- **Frequência sync físico:** 30 minutos (galpão tem fluxos discretos: recebimento de container 1-2x/mês, envio Full semanal)
- **Layout:** 3 cards lado a lado
- **Granularidade:** valor em R$ + quantidade de unidades + número de SKUs únicos

## Arquitetura

```
┌──────────────────────────────────────────────┐
│  Home Dashboard (Next.js)                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │   FULL   │ │  FÍSICO  │ │  TOTAL   │      │
│  └──────────┘ └──────────┘ └──────────┘      │
│             ↑ /api/inventory-summary         │
└──────────────────────────────────────────────┘
                    │
                    ▼
       ┌─────────────────────────────┐
       │  Supabase                   │
       │  ├ fulfillment_inventory    │ ← já existe (sync-costs/sync-inventory)
       │  └ physical_inventory_      │
       │    summary (NOVA, 1 row)    │
       └────────────┬────────────────┘
                    │
                    │ cron 0,30 * * * *
                    │ sync-physical-inventory.py
                    ▼
       ┌─────────────────────────────┐
       │  Planilha de Precificação   │
       │  `1u74a...` aba ESTOQUE     │
       │  col A (qty) × col D (custo)│
       │  = col H (custo total)      │
       └─────────────────────────────┘
```

## Fases de execução

### Fase A — Auditoria da Home (read-only, Kobe)

Antes de qualquer código, Kobe identifica:
- File da home: provavelmente `src/app/(dashboard)/page.tsx` ou similar
- Onde está renderizado "Participação por canal" — file:line
- Estrutura do componente (qual lib de cards usa, se shadcn)
- Onde encaixa a nova seção (depois de qual `<div>` ou componente)
- Cores/visual padrão da home pra o card seguir o estilo

Reporta no chat antes de patchar.

### Fase B — Schema Supabase

Migration nova `XXX_physical_inventory_summary.sql`:

```sql
CREATE TABLE IF NOT EXISTS physical_inventory_summary (
  id INTEGER PRIMARY KEY DEFAULT 1 CHECK (id = 1),
  total_qty INTEGER NOT NULL DEFAULT 0,
  total_cost NUMERIC(12,2) NOT NULL DEFAULT 0,
  sku_count INTEGER NOT NULL DEFAULT 0,
  last_synced TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO physical_inventory_summary (id, total_qty, total_cost, sku_count)
VALUES (1, 0, 0, 0)
ON CONFLICT (id) DO NOTHING;

-- Habilitar Realtime para que o frontend receba updates automáticos
ALTER PUBLICATION supabase_realtime ADD TABLE physical_inventory_summary;
```

Single-row pattern (id=1 forçado por CHECK) — sempre 1 registro com snapshot atual.

### Fase C — Backend cron sync (VPS)

**Novo script:** `/root/.openclaw/workspace/scripts/sync-physical-inventory.py`

- Lê aba ESTOQUE da planilha `1u74a...` no range A4:H500
- Para cada linha:
  - col A → qty atual no galpão (int)
  - col B → SKU base (texto, valida que existe)
  - col D → custo unitário (parse_cost helper)
  - col H → custo total da linha (parse_cost — pode ter `#ERROR!` ou vazio)
- Soma: `total_qty`, `total_cost`, conta SKUs únicos com qty > 0 (ou todos com SKU base válido — a definir)
- Upsert em `physical_inventory_summary` (id=1) com `last_synced = NOW()`

**Wrapper:** `/root/scripts/sync-physical-inventory-cron.sh`

```bash
#!/bin/bash
export GOG_KEYRING_PASSWORD=$(cat /root/.openclaw/.gog-keyring-pass)
export GOG_ACCOUNT=gb.ai.agent@gbimportadora.com
LOG_DIR=/var/log/budamix-sync
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/physical-inventory-$(date +%Y%m%d).log"
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting physical inventory sync" >> "$LOG_FILE"
timeout 60 python3 -u /root/.openclaw/workspace/scripts/sync-physical-inventory.py >> "$LOG_FILE" 2>&1
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Physical inventory exit=$?" >> "$LOG_FILE"
```

**Crontab:**
```cron
0,30 * * * * /root/scripts/sync-physical-inventory-cron.sh
```

### Fase D — Backend API route (Next.js)

**Novo arquivo:** `src/app/api/inventory-summary/route.ts`

```ts
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server"; // ou client correto do projeto

export async function GET() {
  const supabase = createClient();

  // FULL — agrega em tempo real do fulfillment_inventory
  const { data: fullRows } = await supabase
    .from("fulfillment_inventory")
    .select("sku, available_qty, cost_price");

  const full_cost = fullRows?.reduce(
    (s, r) => s + (r.available_qty || 0) * (Number(r.cost_price) || 0),
    0,
  ) ?? 0;
  const full_qty = fullRows?.reduce((s, r) => s + (r.available_qty || 0), 0) ?? 0;
  const full_skus = new Set(fullRows?.map((r) => r.sku) ?? []).size;

  // FÍSICO — snapshot da tabela
  const { data: physical } = await supabase
    .from("physical_inventory_summary")
    .select("*")
    .eq("id", 1)
    .single();

  return NextResponse.json({
    full: {
      cost: full_cost,
      qty: full_qty,
      sku_count: full_skus,
    },
    physical: {
      cost: Number(physical?.total_cost) || 0,
      qty: physical?.total_qty || 0,
      sku_count: physical?.sku_count || 0,
      last_synced: physical?.last_synced,
    },
    total: {
      cost: full_cost + (Number(physical?.total_cost) || 0),
      qty: full_qty + (physical?.total_qty || 0),
    },
  });
}
```

### Fase E — Frontend (Next.js)

**Hook:** `src/hooks/use-inventory-summary.ts`

```ts
import { useQuery } from "@tanstack/react-query";
import { useEffect } from "react";
import { createClient } from "@/lib/supabase/client";

export function useInventorySummary() {
  const supabase = createClient();
  const query = useQuery({
    queryKey: ["inventory-summary"],
    queryFn: async () => {
      const r = await fetch("/api/inventory-summary");
      if (!r.ok) throw new Error("Failed to fetch inventory summary");
      return r.json();
    },
    refetchInterval: 60_000, // 1 min
    staleTime: 30_000,
  });

  // Realtime: refetch quando o cron physical update
  useEffect(() => {
    const channel = supabase
      .channel("physical-inventory-summary-changes")
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "physical_inventory_summary" },
        () => query.refetch(),
      )
      .subscribe();
    return () => {
      supabase.removeChannel(channel);
    };
  }, [supabase, query]);

  return query;
}
```

**Componente:** `src/components/dashboard/inventory-value-cards.tsx`

3 cards lado a lado seguindo o padrão visual existente da home (provavelmente shadcn/ui Card). Cada card mostra:
- Título (Estoque FULL / Estoque FÍSICO / TOTAL)
- Valor em R$ formatado (`R$ 158.820,52`)
- Sub-info: `X.XXX un · XX SKUs`
- Card físico: `Atualizado há X min` (formatDistance do date-fns)

**Ícones sugestivos:**
- FULL: `Truck` (lucide) — em trânsito/marketplace
- FÍSICO: `Warehouse` (lucide) — galpão
- TOTAL: `Coins` (lucide) — capital total

**Wireframe de layout:**

```
┌────────────────────────────────────────────────────────────────┐
│ ESTOQUE FULL          │ ESTOQUE FÍSICO     │ TOTAL              │
│ R$ 158.820            │ R$ XXX.XXX          │ R$ YYY.YYY         │
│ 9.700 un · 95 SKUs    │ XX.XXX un · XX SKUs │ XX.XXX un · XX SKUs│
│ tempo real            │ atualizado há 12min │                    │
└────────────────────────────────────────────────────────────────┘
```

### Fase F — Integração na Home

Encontrar a home page e o componente "Participação por canal", inserir o novo `<InventoryValueCards />` logo abaixo. Manter spacing consistente com a página.

### Fase G — Build + Deploy

Branch dedicada `feat/home-inventory-cards`:
1. `pnpm typecheck` (se existir) + `pnpm build`
2. Smoke test local (curl `/api/inventory-summary` → 200 com payload)
3. Commit + push
4. Merge na main + tag `v-inventory-cards-20260430`
5. Deploy via `pm2 restart budamix-central`

### Fase H — Validação visual (Pedro)

- Abrir [`https://central.budamix.com.br`](https://central.budamix.com.br)
- Confirmar 3 cards visíveis abaixo de "Participação por canal"
- Custo FULL deve bater com `Estoque Full` (KPI Valor Custo): R$ 158.820,52
- Custo FÍSICO mostra valor real da planilha
- Total = soma exata
- Sem regressão em outras telas

## Critério de aceite

| Validação | Como medir |
|-----------|-----------|
| Migration aplicada | `physical_inventory_summary` existe + 1 row id=1 |
| Cron rodando | Log `physical-inventory-YYYYMMDD.log` mostra exit=0 a cada 30min |
| API funciona | `curl localhost:3000/api/inventory-summary` retorna 3 chaves |
| Custo FULL bate | API.full.cost ≈ R$ 158.820 (±R$ 5 arredondamento) |
| Custo FÍSICO bate | API.physical.cost == soma manual da col H da planilha (±R$ 1) |
| Total = soma | API.total.cost = full.cost + physical.cost |
| Frontend renderiza | 3 cards visíveis, números formatados em PT-BR |
| Realtime refresh | Quando rodar cron manual, card físico atualiza < 5s |
| Sem regressão | `/produtos`, `/estoque`, `/live` continuam OK |

## Rollback

- Frontend/Backend: branch dedicada permite `git revert` ou voltar pra tag anterior
- Migration: `DROP TABLE physical_inventory_summary` se precisar reverter (mas é additive, geralmente não precisa)
- Cron: comentar linha no crontab

## Riscos

- **Quota Google Sheets API:** sync 30min ainda dentro de quota grátis (60/min, 100/100s usuário). OK.
- **Realtime Supabase:** precisa habilitar replication na tabela (instrução na migration).
- **Soma da col H:** pode ter `#ERROR!` em algumas linhas, fórmulas defasadas. `parse_cost` do sync-costs já trata.
- **Single-row pattern:** se múltiplos crons rodarem ao mesmo tempo, upsert resolve (último vence). Lock não necessário.

## Próximo passo

Mensagem pro Kobe executar Fase A (auditoria home — read-only, sem patch).

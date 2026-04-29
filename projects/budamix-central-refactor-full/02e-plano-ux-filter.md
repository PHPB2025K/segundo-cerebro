---
title: "Budamix Central Refactor Full — 02E Plano UX Filtro KPI"
created: 2026-04-29
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - ux
  - frontend
---

# Etapa 2E — Bug UX: KPI não recalcula com filtro

## Bug confirmado

Mapeamento ([[projects/budamix-central-refactor-full/00-mapeamento|00-mapeamento.md]]) seção D mostrou:

- `InventoryOverview` filtra `items` localmente em `filtered` (linhas 76-89 aproximadamente)
- Mas passa `kpis` original para `InventoryKPICards` ([src/components/inventory/inventory-overview.tsx:100](src/components/inventory/inventory-overview.tsx#L100))
- KPI **Valor Custo** (entre outros) continua mostrando agregado dos 3 marketplaces mesmo quando usuário seleciona "Shopee" ou um shop_id específico

## Comportamento esperado

KPI segue os mesmos filtros que a tabela. Sem toggle. Simples e previsível.

Quando usuário:
- Seleciona "Shopee" → KPI mostra só Shopee (3 contas somadas)
- Seleciona "Shopee" + subtab `448649947` → KPI mostra só essa conta
- Aplica busca por SKU → KPI mostra só os SKUs filtrados
- Aplica filtro de status (zerado/baixo/saudável) → KPI mostra só esse status

## Solução

Recalcular `kpis` no client a partir de `filtered`. A função `computeInventoryKPIs` em [src/data/mock-inventory.ts:94](src/data/mock-inventory.ts#L94) já é pura — recebe array, retorna agregados. Reutilizar.

### Patch (estimado, confirmar formato no código real)

Em `src/components/inventory/inventory-overview.tsx`:

```tsx
// Adicionar import no topo
import { computeInventoryKPIs } from "@/data/mock-inventory";
import { useMemo } from "react"; // se já não importado

// Dentro do componente, após o cálculo de `filtered`:
const filteredKpis = useMemo(
  () => computeInventoryKPIs(filtered),
  [filtered]
);

// Substituir uso de kpis pelo filteredKpis:
<InventoryKPICards kpis={filteredKpis} ... />
```

Detalhes a validar no momento do patch:
- O nome real do array filtrado (`filtered` é hipótese do mapeamento)
- Se há KPIs que NÃO devem ser recalculados (ex: contagem total de marca, snapshot global)
- Se `computeInventoryKPIs` está exportada do módulo

## Sequência de execução

1. **Branch dedicada** — `git checkout -b fix/2e-kpi-filter` no `/var/www/budamix-central` (já versionado pela Fase -1)
2. **Auditoria read-only** — Kobe lê `inventory-overview.tsx` + `inventory-kpis.tsx` + `mock-inventory.ts` e confirma estrutura. Reporta:
   - Nome real do array filtrado
   - Lista de KPIs em `InventoryKPICards`
   - Assinatura de `computeInventoryKPIs`
3. **Aplicar patch** conforme acima, ajustado pelo que a auditoria revelou
4. **Validar build** — `pnpm build` em modo prod (ou `pnpm typecheck` no mínimo)
5. **Smoke test pre-deploy** — `pnpm dev` ou serve dist; abrir `/estoque`, trocar filtro, ver KPI mudar
6. **Commit + push branch** — mensagem clara, ex: `fix(estoque): KPI cards now respect active filters`
7. **Merge na main** (PR ou direto, depende do gate)
8. **Deploy prod** — `pm2 restart budamix-central` ou equivalente
9. **Validação visual em prod** — Pedro abre `https://central.budamix.com.br/estoque`, troca filtro Marketplace, confirma KPI mudando

## Critério de aceite

| Validação | Como medir |
|-----------|-----------|
| Build sem erro | `pnpm build` exit 0, sem TS errors |
| Filtro Marketplace = "ML Full" | KPI Valor Custo ≈ R$ 17.7k (não R$ 134k) |
| Filtro Marketplace = "Shopee Full" | KPI Valor Custo ≈ R$ 83.5k |
| Filtro Marketplace = "Amazon FBA" | KPI Valor Custo ≈ R$ 23.3k |
| Subtab Shopee `448649947` | KPI Valor Custo ≈ R$ 39.2k |
| Soma das partes ≈ total | `17.7 + 83.5 + 23.3 ≈ 124.5` (matches o "Todas") |
| Build do `/estoque` carrega | sem erro JS no console, KPIs renderizam |
| Outras telas funcionam | `/produtos`, `/live`, `/estoque/historico` sem regressão |

## Riscos

- **`computeInventoryKPIs` pode usar campos não presentes no payload de `/api/inventory`:** se a função foi escrita pra mocks com campos extras, recalcular client-side pode dar valores diferentes do server-side. Auditoria do Passo 2 deve confirmar.
- **Outros componentes podem depender do `kpis` original:** `RestockTab` ou `SalesHistoryTab` podem ter referência. Validar busca por uso.
- **Performance:** recalcular a cada filtro é O(n) em ~200 registros. Trivial. Sem risco.

## Rollback

Se algo quebrar:
```bash
cd /var/www/budamix-central
git checkout main
git reset --hard pre-refactor-full-20260429  # tag baseline da Fase -1
pnpm install && pnpm build && pm2 restart budamix-central
```

Ou simplesmente voltar pra commit anterior se branch ainda não foi mergeada.

## Próximo passo após 2E

Decidir entre:
- **2D — sku_mapping fallback** (cobre +21 registros zerados, mais R$ ~6-15k de custo coberto)
- **1E — Monitoramento Shopee** (defensivo, evita repetir o problema das contas paradas)

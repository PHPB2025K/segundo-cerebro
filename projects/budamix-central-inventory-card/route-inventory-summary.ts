// Path no repo: src/app/api/inventory-summary/route.ts
// Combina dados em tempo real do fulfillment_inventory (FULL) com snapshot
// do physical_inventory_summary (FÍSICO).
// Padrão: requireAuth + createClient async (igual /api/inventory).

import { NextResponse } from "next/server";
import { requireAuth } from "@/lib/auth/require-auth";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const authError = await requireAuth(request);
  if (authError) return authError;

  const supabase = await createClient();

  // FULL — agrega em tempo real do fulfillment_inventory
  const { data: fullRows, error: fullErr } = await supabase
    .from("fulfillment_inventory")
    .select("sku, available_qty, cost_price");

  if (fullErr) {
    return NextResponse.json(
      { error: "Failed to fetch fulfillment_inventory", detail: fullErr.message },
      { status: 500 },
    );
  }

  const full_cost = (fullRows ?? []).reduce(
    (s, r) => s + (r.available_qty ?? 0) * (Number(r.cost_price) || 0),
    0,
  );
  const full_qty = (fullRows ?? []).reduce(
    (s, r) => s + (r.available_qty ?? 0),
    0,
  );
  const full_skus = new Set((fullRows ?? []).map((r) => r.sku)).size;

  // FÍSICO — snapshot da tabela
  const { data: physical } = await supabase
    .from("physical_inventory_summary")
    .select("*")
    .eq("id", 1)
    .maybeSingle();

  const physical_cost = Number(physical?.total_cost) || 0;
  const physical_qty = physical?.total_qty || 0;
  const physical_skus = physical?.sku_count || 0;
  const physical_synced = physical?.last_synced ?? null;

  return NextResponse.json({
    full: {
      cost: full_cost,
      qty: full_qty,
      sku_count: full_skus,
    },
    physical: {
      cost: physical_cost,
      qty: physical_qty,
      sku_count: physical_skus,
      last_synced: physical_synced,
    },
    total: {
      cost: full_cost + physical_cost,
      qty: full_qty + physical_qty,
      sku_count: full_skus + physical_skus,
    },
  });
}

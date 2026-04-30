// Path no repo: src/hooks/use-inventory-summary.ts
// Padrão baseado em src/hooks/use-inventory.ts (Realtime + invalidação).
// Subscreve apenas em physical_inventory_summary (cron 30min).
// Mudanças no fulfillment_inventory são pegas via refetchInterval de 60s.

"use client";

import { useEffect } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createClient } from "@/lib/supabase/client";

export type InventorySummary = {
  full: { cost: number; qty: number; sku_count: number };
  physical: {
    cost: number;
    qty: number;
    sku_count: number;
    last_synced: string | null;
  };
  total: { cost: number; qty: number; sku_count: number };
};

const QUERY_KEY = ["inventory-summary"] as const;

async function fetchInventorySummary(): Promise<InventorySummary> {
  const res = await fetch("/api/inventory-summary", { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to fetch inventory summary: ${res.status}`);
  return res.json();
}

export function useInventorySummary() {
  const queryClient = useQueryClient();

  useEffect(() => {
    const supabase = createClient();
    const channel = supabase
      .channel("physical-inventory-summary-changes")
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "physical_inventory_summary",
        },
        () => {
          queryClient.invalidateQueries({ queryKey: QUERY_KEY });
        },
      )
      .subscribe();
    return () => {
      supabase.removeChannel(channel);
    };
  }, [queryClient]);

  return useQuery({
    queryKey: QUERY_KEY,
    queryFn: fetchInventorySummary,
    refetchInterval: 60_000,
    staleTime: 30_000,
  });
}

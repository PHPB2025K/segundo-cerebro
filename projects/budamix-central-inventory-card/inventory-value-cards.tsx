// Path no repo: src/components/dashboard/inventory-value-cards.tsx
// 3 cards lado a lado: ESTOQUE FULL | ESTOQUE FÍSICO | TOTAL
// Padrão visual baseado em kpi-cards.tsx (Card + hover glow + ícone em box var(--primary)/10).

"use client";

import { Card } from "@/components/ui/card";
import { Coins, Truck, Warehouse, type LucideIcon } from "lucide-react";
import { useInventorySummary } from "@/hooks/use-inventory-summary";
import { formatCurrency } from "@/lib/utils";

function timeAgo(iso: string | null | undefined) {
  if (!iso) return "—";
  const diff = Math.floor((Date.now() - new Date(iso).getTime()) / 60_000);
  if (diff < 1) return "agora mesmo";
  if (diff < 60) return `há ${diff} min`;
  const hours = Math.floor(diff / 60);
  if (hours < 24) return `há ${hours} h`;
  return `há ${Math.floor(hours / 24)} d`;
}

type CardConfig = {
  title: string;
  subtitle: string;
  icon: LucideIcon;
  value: number;
  qty: number;
  sku_count: number;
  footer: string;
};

export function InventoryValueCards() {
  const { data, isLoading } = useInventorySummary();

  if (isLoading || !data) return <InventoryValueCardsSkeleton />;

  const cards: CardConfig[] = [
    {
      title: "Estoque Full",
      subtitle: "ML + Shopee + Amazon",
      icon: Truck,
      value: data.full.cost,
      qty: data.full.qty,
      sku_count: data.full.sku_count,
      footer: "tempo real",
    },
    {
      title: "Estoque Físico",
      subtitle: "Galpão Pedreira-SP",
      icon: Warehouse,
      value: data.physical.cost,
      qty: data.physical.qty,
      sku_count: data.physical.sku_count,
      footer: `atualizado ${timeAgo(data.physical.last_synced)}`,
    },
    {
      title: "Total em Estoque",
      subtitle: "Capital total imobilizado",
      icon: Coins,
      value: data.total.cost,
      qty: data.total.qty,
      sku_count: data.total.sku_count,
      footer: "Full + Físico",
    },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
      {cards.map((c) => (
        <Card
          key={c.title}
          className="p-6 transition-shadow hover:shadow-[0_0_24px_-4px_var(--primary)]"
        >
          <div className="flex items-start gap-3 mb-4">
            <div className="rounded-lg bg-[var(--primary)]/10 text-[var(--primary)] p-2 shrink-0">
              <c.icon className="h-5 w-5" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium leading-tight">{c.title}</p>
              <p className="text-xs text-[var(--muted-foreground)] truncate">
                {c.subtitle}
              </p>
            </div>
          </div>
          <p className="text-3xl font-bold tracking-tight">
            {formatCurrency(c.value)}
          </p>
          <p className="text-xs text-[var(--muted-foreground)] mt-2">
            {c.qty.toLocaleString("pt-BR")} un · {c.sku_count} SKUs
          </p>
          <p className="text-xs text-[var(--muted-foreground)]/70 mt-1">
            {c.footer}
          </p>
        </Card>
      ))}
    </div>
  );
}

function InventoryValueCardsSkeleton() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
      {[0, 1, 2].map((i) => (
        <Card key={i} className="p-6 animate-pulse">
          <div className="flex items-start gap-3 mb-4">
            <div className="h-9 w-9 rounded-lg bg-[var(--muted)]/40" />
            <div className="flex-1 space-y-2">
              <div className="h-3 bg-[var(--muted)]/40 rounded w-2/3" />
              <div className="h-2 bg-[var(--muted)]/40 rounded w-1/2" />
            </div>
          </div>
          <div className="h-8 bg-[var(--muted)]/40 rounded w-3/4 mb-2" />
          <div className="h-3 bg-[var(--muted)]/40 rounded w-full" />
        </Card>
      ))}
    </div>
  );
}

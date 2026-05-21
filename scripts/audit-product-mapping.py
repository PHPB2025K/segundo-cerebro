#!/usr/bin/env python3
"""
audit-product-mapping.py — Detecta divergências entre o mapa estático
PRODUCT_DISPLAY_NAMES do data builder e o title real dos anúncios na API ML.

Roda 1×/semana via cron. Pega todos os platform_item_id que apareceram em
pedidos ML nos últimos N dias, busca o title real na API ML, e compara com
o display_name esperado pelo mapa estático.

Output: JSON com divergências detectadas.

Usage:
    python3 audit-product-mapping.py [--days 30] [--output /path]

Critério de divergência:
  - O SKU normalizado do pedido tem entrada em PRODUCT_DISPLAY_NAMES
  - O display_name do mapa difere "substancialmente" do title real do ML
  - "Substancialmente" = não compartilha palavras-chave principais do produto
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone, timedelta

# Reusa o connector ML existente
sys.path.insert(0, "/root/segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors")
import mercadolivre as ml_conn  # noqa: E402

# Importa o mapa estático e função de normalização do data builder
sys.path.insert(0, "/root/segundo-cerebro/scripts")
spec_path = "/root/segundo-cerebro/scripts/daily-sales-data-builder.py"
import importlib.util
spec = importlib.util.spec_from_file_location("data_builder", spec_path)
data_builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_builder)

PRODUCT_DISPLAY_NAMES = data_builder.PRODUCT_DISPLAY_NAMES
normalize_sku = data_builder.normalize_sku

# Config Supabase
SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxYmtvcHJjbW56bm16Yndkcm1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDM4MDQxNCwiZXhwIjoyMDg5OTU2NDE0fQ.-sTaIitEplNoBbW8U5nBHIjAlsIe20ImZ3SkLs17i6A"


def fetch_ml_items_from_orders(days):
    """Busca platform_item_id + sku dos pedidos ML dos últimos N dias."""
    since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    all_orders = []
    offset = 0
    page = 1000
    while True:
        params = [
            ("select", "items,platform_order_id"),
            ("platform", "eq.ml"),
            ("order_date", f"gte.{since}"),
            ("limit", str(page)),
            ("offset", str(offset)),
        ]
        url = f"{SUPABASE_URL}/rest/v1/orders?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        })
        resp = urllib.request.urlopen(req, timeout=60)
        batch = json.loads(resp.read())
        if not batch:
            break
        all_orders.extend(batch)
        if len(batch) < page:
            break
        offset += page
    return all_orders


def extract_item_sku_pairs(orders):
    """
    Retorna dict {platform_item_id: {sku_set, total_orders}}.
    Os items[] já têm 'sku' e 'title' por pedido — mas precisamos do
    platform_item_id que está dentro de cada item.
    """
    items_index = defaultdict(lambda: {"skus": set(), "raw_titles": set(), "orders": 0})
    for o in orders:
        for it in (o.get("items") or []):
            pid = it.get("platform_item_id")
            sku = it.get("sku")
            title = it.get("title")
            if pid:
                items_index[pid]["orders"] += 1
                if sku:
                    items_index[pid]["skus"].add(sku)
                if title:
                    items_index[pid]["raw_titles"].add(title)
    # converte sets em listas pra JSON
    return {
        pid: {
            "skus": sorted(data["skus"]),
            "raw_titles": sorted(data["raw_titles"]),
            "orders": data["orders"],
        }
        for pid, data in items_index.items()
    }


def normalize_words(text):
    """Pega palavras-chave de PRODUTO (>= 4 chars), sem números/unidades/ruído."""
    if not text:
        return set()
    text = text.lower()
    # remove dígitos primeiro (350ml, 1050ml, etc viram nada)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'[^a-záàâãéèêíïóôõöúçñ\s]', ' ', text)
    stopwords = {
        # quantitativos e medidas
        "kit", "com", "para", "que", "mas", "ml", "cm", "mm", "pcs", "peças", "peca",
        "pecas", "unidade", "unidades", "und", "qtde", "qtd", "cor", "modelo",
        "produto", "novo", "novos", "nova",
        # materiais genéricos demais (aparecem em muitos produtos diferentes)
        "vidro", "vidros", "plástico", "plastico",
        # adjetivos comuns
        "lisa", "liso", "claro", "claros", "preto", "preta", "branco", "branca",
        "azul", "vermelha", "vermelho", "cinza", "amarelo", "amarela", "rosa",
        "tampa", "tampas",
    }
    words = set()
    for w in text.split():
        if len(w) >= 4 and w not in stopwords:
            words.add(w)
    return words


def is_divergent(mapped_name, real_title):
    """
    Heurística: mapa diverge do title real se nenhuma palavra-chave de produto
    (substantivo principal) do mapa aparece no title real.
    Cálculo: overlap < 1 palavra-chave OU < 25% das palavras do mapa.
    """
    if not mapped_name or not real_title:
        return False
    mapped_words = normalize_words(mapped_name)
    real_words = normalize_words(real_title)
    if not mapped_words:
        return False
    overlap = mapped_words & real_words
    # divergente se ZERO palavras em comum (não compartilha nenhum substantivo)
    if not overlap:
        return True
    overlap_ratio = len(overlap) / len(mapped_words)
    return overlap_ratio < 0.25


def audit_mapping(days, max_items_check=None):
    """Executa a auditoria completa."""
    print(f"Buscando pedidos ML dos últimos {days} dias...")
    orders = fetch_ml_items_from_orders(days)
    print(f"  → {len(orders)} pedidos lidos")

    items_index = extract_item_sku_pairs(orders)
    print(f"  → {len(items_index)} platform_item_ids únicos")

    # ordena por número de pedidos (anúncios que mais venderam primeiro)
    sorted_items = sorted(items_index.items(), key=lambda x: -x[1]["orders"])
    if max_items_check:
        sorted_items = sorted_items[:max_items_check]

    print(f"\nRefresh token ML...")
    ml_conn.refresh_tokens()
    token = ml_conn.load_token("vendas")
    if not token:
        sys.exit("token ML indisponível")

    print(f"Auditando {len(sorted_items)} anúncios contra a API ML...")
    divergences = []
    variation_aliases = []  # 1 anúncio com múltiplos SKUs mapeados — falso positivo
    checked = 0
    no_mapping = 0
    ok = 0

    for pid, data in sorted_items:
        checked += 1
        if checked % 25 == 0:
            print(f"  {checked}/{len(sorted_items)}...")

        # busca title atual na API ML
        item = ml_conn.api_get(f"https://api.mercadolibre.com/items/{pid}", token)
        if not item:
            continue
        real_title = item.get("title")
        listing_type = item.get("listing_type_id")
        is_catalog = bool(item.get("catalog_listing"))
        status = item.get("status")
        category_id = item.get("category_id")

        # Detecta: 1 anúncio com múltiplos SKUs mapeados → caso de variação
        # (anúncio com cores/tamanhos diferentes, title genérico no ML).
        skus_with_mapping = []
        for raw_sku in data["skus"]:
            if not raw_sku:
                continue
            normalized = normalize_sku(raw_sku)
            raw_upper = raw_sku.upper().strip()
            mapped_name = None
            mapping_key = None
            if raw_upper in PRODUCT_DISPLAY_NAMES:
                mapped_name = PRODUCT_DISPLAY_NAMES[raw_upper]
                mapping_key = raw_upper
            elif normalized in PRODUCT_DISPLAY_NAMES:
                mapped_name = PRODUCT_DISPLAY_NAMES[normalized]
                mapping_key = normalized
            if mapped_name is not None:
                skus_with_mapping.append((raw_sku, normalized, mapping_key, mapped_name))

        is_multi_variation = len(skus_with_mapping) > 1

        # pra cada SKU mapeado, checa divergência
        for raw_sku, normalized, mapping_key, mapped_name in skus_with_mapping:
            if is_divergent(mapped_name, real_title):
                entry = {
                    "platform_item_id": pid,
                    "raw_sku": raw_sku,
                    "normalized_sku": normalized,
                    "mapping_key_in_mapa": mapping_key,
                    "mapped_display_name": mapped_name,
                    "real_title_ml": real_title,
                    "category_id": category_id,
                    "is_catalog": is_catalog,
                    "listing_type": listing_type,
                    "status": status,
                    "orders_last_30d": data["orders"],
                    "raw_titles_observados_pedidos": data["raw_titles"],
                }
                if is_multi_variation:
                    # provável caso de variação: 1 anúncio com cores/tamanhos diferentes
                    # title do ML é genérico, mapas diferenciam variação
                    entry["nota"] = (
                        f"Anúncio tem {len(skus_with_mapping)} SKUs mapeados — "
                        "provavelmente caso de variação (anúncio único com cores/tamanhos). "
                        "Title do ML é genérico; mapa diferencia variação. "
                        "Revisar manualmente: pode ser falso positivo ou anúncio mal nomeado no ML."
                    )
                    variation_aliases.append(entry)
                else:
                    divergences.append(entry)
            else:
                ok += 1
        no_mapping += (len(data["skus"]) - len(skus_with_mapping))

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "window_days": days,
        "summary": {
            "total_anuncios_com_pedidos": len(items_index),
            "anuncios_auditados": checked,
            "skus_sem_mapeamento": no_mapping,
            "skus_ok": ok,
            "divergencias_reais": len(divergences),
            "alertas_variacao_falso_positivo": len(variation_aliases),
        },
        "divergences": divergences,
        "variation_aliases_to_review": variation_aliases,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--output", default="/var/log/daily-sales/product-mapping-audit.json")
    ap.add_argument("--limit", type=int, default=None, help="Limit a checar (debug)")
    args = ap.parse_args()

    result = audit_mapping(args.days, max_items_check=args.limit)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print(f"AUDITORIA CONCLUÍDA")
    print("=" * 60)
    s = result["summary"]
    print(f"  anúncios c/ pedidos: {s['total_anuncios_com_pedidos']}")
    print(f"  auditados: {s['anuncios_auditados']}")
    print(f"  skus sem mapeamento: {s['skus_sem_mapeamento']}")
    print(f"  skus ok: {s['skus_ok']}")
    print(f"  ⚠ divergências REAIS: {s['divergencias_reais']}")
    print(f"  ℹ casos de variação (revisar): {s['alertas_variacao_falso_positivo']}")
    print()
    print(f"Output: {args.output}")
    print()
    if result["divergences"]:
        print("=" * 60)
        print(" 🔴 DIVERGÊNCIAS REAIS (corrigir no mapa)")
        print("=" * 60)
        for d in result["divergences"]:
            print(f"\nSKU {d['raw_sku']} → {d['platform_item_id']}")
            print(f"  Mapa diz:    {d['mapped_display_name']}")
            print(f"  ML diz:      {d['real_title_ml']}")
            print(f"  pedidos 30d: {d['orders_last_30d']}")
            print(f"  catálogo:    {d['is_catalog']}")
    if result["variation_aliases_to_review"]:
        print()
        print("=" * 60)
        print(" 🟡 CASOS DE VARIAÇÃO (revisar — provável falso positivo)")
        print("=" * 60)
        seen_pid = set()
        for d in result["variation_aliases_to_review"]:
            if d["platform_item_id"] in seen_pid:
                continue
            seen_pid.add(d["platform_item_id"])
            print(f"\n{d['platform_item_id']}: title ML = '{d['real_title_ml']}'")
            for v in result["variation_aliases_to_review"]:
                if v["platform_item_id"] == d["platform_item_id"]:
                    print(f"  SKU {v['raw_sku']} mapeado pra '{v['mapped_display_name']}'")


if __name__ == "__main__":
    main()

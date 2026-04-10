#!/usr/bin/env python3
"""
Parse Mercado Livre search results HTML.
Extracts product data from ML search pages fetched via Bright Data.
"""

import re
import json
import sys
from typing import Optional


def parse_search_html(html: str, search_term: str = "", page: int = 1) -> list[dict]:
    """Parse ML search results HTML and return structured product data."""
    
    products = []
    
    # Split by result items - ML uses ui-search-layout__item as container
    result_blocks = re.split(r'ui-search-layout__item', html)
    
    for block_idx, block in enumerate(result_blocks[1:], 1):  # skip pre-results
        
        # === TITLE ===
        title = None
        for pattern in [
            r'ui-search-item__title[^>]*>([^<]+)<',
            r'poly-component__title[^>]*>([^<]+)<',
            r'shops__item-title[^>]*>([^<]+)<',
        ]:
            m = re.search(pattern, block)
            if m:
                title = m.group(1).strip()
                break
        
        if not title:
            continue
        
        # === PRICE (main) ===
        price = None
        price_m = re.search(r'andes-money-amount__fraction[^>]*>([\d.,]+)<', block)
        if price_m:
            price_str = price_m.group(1).replace('.', '').replace(',', '.')
            try:
                price = float(price_str)
            except ValueError:
                pass
        
        # === ORIGINAL PRICE (crossed out) ===
        original_price = None
        orig_m = re.search(
            r'andes-money-amount--previous.*?andes-money-amount__fraction[^>]*>([\d.,]+)<',
            block, re.DOTALL
        )
        if orig_m:
            orig_str = orig_m.group(1).replace('.', '').replace(',', '.')
            try:
                original_price = float(orig_str)
            except ValueError:
                pass
        
        # === FREE SHIPPING ===
        free_shipping = bool(
            re.search(r'[Ff]rete\s*gr[áa]tis', block) or
            'free_shipping' in block
        )
        
        # === FULFILLMENT (FULL) ===
        fulfillment = bool(
            re.search(r'FULL', block) or
            'fulfillment' in block.lower()
        )
        
        # === SOLD QUANTITY ===
        sold_quantity = None
        sold_m = re.search(r'([\d.]+[+]?)\s*vendido', block)
        if sold_m:
            sold_quantity = sold_m.group(1)
        
        # === RATING ===
        rating = None
        rating_m = re.search(r'(\d[.,]\d)\s*(?:de\s*5|estrela|star)', block)
        if not rating_m:
            # Try aria-label pattern
            rating_m = re.search(r'aria-label="(\d[.,]\d)\s', block)
        if rating_m:
            try:
                rating = float(rating_m.group(1).replace(',', '.'))
            except ValueError:
                pass
        
        # === REVIEWS COUNT ===
        reviews_count = None
        rev_m = re.search(r'\((\d+)\)', block)
        if rev_m:
            try:
                reviews_count = int(rev_m.group(1))
            except ValueError:
                pass
        
        # === PERMALINK ===
        permalink = None
        link_m = re.search(r'href="(https://[^"]*MLB[^"]*)"', block)
        if not link_m:
            link_m = re.search(r'href="(https://www\.mercadolivre\.com\.br/[^"]+)"', block)
        if link_m:
            permalink = link_m.group(1).split('#')[0].split('?')[0]
        
        # === MLB ID ===
        mlb_id = None
        if permalink:
            id_m = re.search(r'(MLB-?\d+)', permalink)
            if id_m:
                mlb_id = id_m.group(1).replace('-', '')
        
        # === THUMBNAIL ===
        thumbnail_url = None
        thumb_m = re.search(r'src="(https://http2\.mlstatic\.com/D_[^"]+)"', block)
        if not thumb_m:
            thumb_m = re.search(r'data-src="(https://http2\.mlstatic\.com/D_[^"]+)"', block)
        if thumb_m:
            thumbnail_url = thumb_m.group(1)
        
        products.append({
            "mlb_id": mlb_id,
            "title": title,
            "price": price,
            "original_price": original_price,
            "free_shipping": free_shipping,
            "fulfillment": fulfillment,
            "sold_quantity": sold_quantity,
            "rating": rating,
            "reviews_count": reviews_count,
            "thumbnail_url": thumbnail_url,
            "permalink": permalink,
            "position": block_idx,
            "search_term": search_term,
            "page": page,
        })
    
    return products


def deduplicate(products: list[dict]) -> list[dict]:
    """Deduplicate products by MLB ID, keeping the one with best position."""
    seen = {}
    for p in products:
        mid = p.get("mlb_id")
        if not mid:
            # No MLB ID - keep by title hash
            mid = hash(p.get("title", ""))
        
        if mid not in seen:
            seen[mid] = p
        else:
            # Keep the one with better (lower) position
            existing_pos = seen[mid].get("position", 999)
            new_pos = p.get("position", 999)
            if new_pos < existing_pos:
                seen[mid] = p
    
    return list(seen.values())


def price_analysis(products: list[dict], our_price: float = None) -> dict:
    """Generate price analysis statistics."""
    prices = [p["price"] for p in products if p.get("price")]
    
    if not prices:
        return {"error": "no prices found"}
    
    prices_sorted = sorted(prices)
    n = len(prices_sorted)
    
    analysis = {
        "count": n,
        "min": prices_sorted[0],
        "max": prices_sorted[-1],
        "median": prices_sorted[n // 2],
        "mean": round(sum(prices_sorted) / n, 2),
        "free_shipping_pct": round(
            len([p for p in products if p.get("free_shipping")]) / len(products) * 100
        ),
        "fulfillment_pct": round(
            len([p for p in products if p.get("fulfillment")]) / len(products) * 100
        ),
    }
    
    # Price distribution by range
    ranges = {}
    step = 10
    min_r = int(prices_sorted[0] // step * step)
    max_r = int(prices_sorted[-1] // step * step) + step
    for lo in range(min_r, max_r, step):
        hi = lo + step
        count = len([p for p in prices_sorted if lo <= p < hi])
        if count > 0:
            ranges[f"R${lo}-{hi}"] = count
    analysis["distribution"] = ranges
    
    if our_price:
        analysis["our_price"] = our_price
        analysis["vs_median_pct"] = round((our_price / analysis["median"] - 1) * 100, 1)
        analysis["vs_min_pct"] = round((our_price / analysis["min"] - 1) * 100, 1)
        analysis["rank"] = len([p for p in prices_sorted if p < our_price]) + 1
        analysis["rank_total"] = n
    
    return analysis


if __name__ == "__main__":
    # Read HTML from stdin or file
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            html = f.read()
    else:
        html = sys.stdin.read()
    
    term = sys.argv[2] if len(sys.argv) > 2 else "manual"
    page = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    
    products = parse_search_html(html, term, page)
    print(json.dumps(products, indent=2, ensure_ascii=False))

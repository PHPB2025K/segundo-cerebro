#!/usr/bin/env python3
"""
Fetch Mercado Livre search results via Bright Data Web Unlocker.
Usage: python3 fetch_ml_search.py <api_key> <search_term> [pages] [country]
"""

import requests
import json
import sys
import time
import re
import os

BRIGHT_DATA_URL = "https://api.brightdata.com/request"
ZONE = "web_unlocker1"
ML_BASE = "https://lista.mercadolivre.com.br"

# Page offsets for ML pagination
PAGE_OFFSETS = {
    1: "",
    2: "_Desde_49",
    3: "_Desde_97",
    4: "_Desde_145",
    5: "_Desde_193",
}


def slugify_term(term: str) -> str:
    """Convert search term to ML URL format."""
    return term.strip().replace(" ", "-").lower()


def fetch_page(api_key: str, term: str, page: int = 1, country: str = "br") -> str:
    """Fetch a single ML search page via Bright Data."""
    slug = slugify_term(term)
    offset = PAGE_OFFSETS.get(page, f"_Desde_{(page - 1) * 48 + 1}")
    
    url = f"{ML_BASE}/{slug}{offset}_NoIndex_True"
    
    payload = {
        "zone": ZONE,
        "url": url,
        "format": "raw",
        "country": country,
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                BRIGHT_DATA_URL,
                headers=headers,
                json=payload,
                timeout=90,
            )
            
            if resp.status_code == 200:
                return resp.text
            elif resp.status_code == 429:
                wait = 5 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                print(
                    f"  Error {resp.status_code}: {resp.text[:200]}",
                    file=sys.stderr,
                )
                return ""
        except requests.exceptions.Timeout:
            print(f"  Timeout on attempt {attempt + 1}", file=sys.stderr)
            time.sleep(3)
        except Exception as e:
            print(f"  Error: {e}", file=sys.stderr)
            return ""
    
    return ""


def fetch_all(
    api_key: str,
    terms: list[str],
    pages_per_term: int = 3,
    country: str = "br",
    delay: float = 1.5,
    output_dir: str = "/tmp/ml_search_results",
) -> dict:
    """Fetch all search pages for all terms. Returns metadata dict."""
    
    os.makedirs(output_dir, exist_ok=True)
    
    results = {
        "terms": terms,
        "pages_per_term": pages_per_term,
        "files": [],
        "stats": {"total_requests": 0, "successful": 0, "failed": 0},
    }
    
    for term_idx, term in enumerate(terms):
        print(f"\n[{term_idx + 1}/{len(terms)}] Term: '{term}'", file=sys.stderr)
        
        for page in range(1, pages_per_term + 1):
            print(f"  Page {page}...", file=sys.stderr, end=" ")
            results["stats"]["total_requests"] += 1
            
            html = fetch_page(api_key, term, page, country)
            
            if html and len(html) > 1000:
                filename = f"search_{term_idx}_{page}.html"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "w") as f:
                    f.write(html)
                
                results["files"].append({
                    "term": term,
                    "page": page,
                    "path": filepath,
                    "size": len(html),
                })
                results["stats"]["successful"] += 1
                print(f"OK ({len(html)} chars)", file=sys.stderr)
            else:
                results["stats"]["failed"] += 1
                print(f"FAILED", file=sys.stderr)
            
            # Rate limiting
            time.sleep(delay)
    
    return results


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_ml_search.py <api_key> <term1> [term2 ...] [--pages N]")
        sys.exit(1)
    
    api_key = sys.argv[1]
    
    # Parse args
    terms = []
    pages = 3
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--pages" and i + 1 < len(sys.argv):
            pages = int(sys.argv[i + 1])
            i += 2
        else:
            terms.append(sys.argv[i])
            i += 1
    
    results = fetch_all(api_key, terms, pages)
    print(json.dumps(results, indent=2))

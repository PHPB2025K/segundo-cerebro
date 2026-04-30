---
title: "Cloudflare bloqueia urllib do Python sem User-Agent custom"
created: 2026-04-30
type: knowledge
domain: tech
status: active
tags:
  - knowledge
  - tech
  - python
  - cloudflare
---

# Cloudflare bloqueia urllib do Python sem User-Agent custom

## Sintoma

Requests Python via `urllib.request` retornam **HTTP 403** com body `error code: 1010` quando o destino está atrás de Cloudflare.

```
HTTPError: HTTP 403
body: error code: 1010
```

Mesmo request com `curl` no mesmo servidor passa normalmente (HTTP 200).

## Causa

O User-Agent padrão do `urllib.request` do Python é algo como `Python-urllib/3.X` — Cloudflare classifica como bot suspeito e bloqueia. `curl` envia `curl/8.X` que é whitelisted.

## Solução

Adicionar header `User-Agent` no Request:

```python
import urllib.request, json
req = urllib.request.Request(
    url, data=body.encode(), method="POST",
    headers={
        "apikey": API_KEY,
        "Content-Type": "application/json",
        "User-Agent": "curl/8.5.0",  # ⬅️ chave pra passar
    }
)
```

Qualquer User-Agent que pareça browser/curl funciona:
- `curl/8.5.0`
- `Mozilla/5.0 (...) Chrome/...`
- `python-requests/2.31.0` (sim, biblioteca `requests` não tem o problema porque usa esse UA por padrão)

## Onde apliquei

- `/root/.openclaw/workspace/scripts/rh-evolution-poller.py` (vigia da Evolution Cloud)
- Próximas integrações Python com Evolution Cloudfy

## Quando lembrar

- Qualquer integração Python com endpoint atrás de Cloudflare
- Especificamente Evolution Cloudfy (`*.cloudfy.live`) bloqueia urllib raw
- Se ver HTTP 403 com `error code: 1010`, não é firewall do destino — é Cloudflare classificando como bot

## Alternativa

Usar a biblioteca `requests` em vez de `urllib`. Por padrão envia UA `python-requests/X.Y` que costuma passar. Mas pra projetos com restrição de dependências (urllib é stdlib), o fix com header funciona.

## Cross-refs

- [[automacoes/scripts/rh-evolution-poller|rh-evolution-poller.py]] — primeiro caso documentado

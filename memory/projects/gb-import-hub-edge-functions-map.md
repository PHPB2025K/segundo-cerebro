# GB Import Hub — Edge Functions Map

> 17 Edge Functions extraidas do repo PHPB2025K/gb-import-hub
> Deploy target: Supabase project ocxvwwaaqqxecmzhfxhb

---

## Secrets necessarios (configurar no Supabase Dashboard > Edge Functions > Secrets)

| Secret | Usado por | Como obter |
|--------|-----------|------------|
| SUPABASE_URL | 12 functions | `https://ocxvwwaaqqxecmzhfxhb.supabase.co` |
| SUPABASE_SERVICE_ROLE_KEY | 12 functions | 1Password vault OpenClaw > gb-import-hub-supabase-service-role |
| ANTHROPIC_API_KEY | 5 functions | Chave API Anthropic (extração de docs, NCM, referências) |
| TERMINAL49_API_KEY | 6 functions | Terminal49 account (tracking de containers) |
| MAPBOX_TOKEN | 1 function | Mapbox account (mapa) |
| MARINETRAFFIC_API_KEY | 1 function | MarineTraffic account (posição de navios) |
| RESEND_API_KEY | 1 function | Resend account (envio de emails de alerta) |
| NOTIFICATION_EMAIL | 1 function | Email destino dos alertas ETA |

---

## Functions por categoria

### Tracking de Containers (7 functions)
| Function | Linhas | APIs externas |
|----------|--------|---------------|
| terminal49-search | 519 | Terminal49 API |
| terminal49-fetch-shipment | 484 | Terminal49 API |
| poll-terminal49 | 558 | Terminal49 API |
| terminal49-webhook | 351 | — (receptor) |
| terminal49-register-webhook | 230 | Terminal49 API |
| terminal49-associate | 107 | — |
| create-tracking-request | 135 | Terminal49 API |

### Posicionamento de Navios (3 functions)
| Function | Linhas | APIs externas |
|----------|--------|---------------|
| fetch-vessel-position | 212 | MarineTraffic API |
| update-vessel-positions | 207 | — |
| fetch-container-map | 241 | Terminal49 API |

### Inteligência Fiscal (4 functions)
| Function | Linhas | APIs externas |
|----------|--------|---------------|
| extract-import-document | 1432 | Anthropic (Claude) |
| calculate-tax-references | 1070 | Anthropic (Claude) |
| fetch-ncm-aliquotas | 276 | Anthropic (Claude) |
| fetch-ncm-aliquotas-web | 156 | Anthropic (Claude) |

### Referências e Utilidades (3 functions)
| Function | Linhas | APIs externas |
|----------|--------|---------------|
| fetch-market-references | 281 | Anthropic (Claude) |
| get-mapbox-token | 19 | — |
| send-eta-alert | 169 | Resend API |

---

## Deploy

```bash
cd /tmp/gb-import-hub
supabase link --project-ref ocxvwwaaqqxecmzhfxhb
supabase functions deploy --all
```

Antes do deploy, configurar todos os secrets no dashboard.

---

## Ver também

- [[memory/projects/gb-import-hub-schema|GB Import Hub — Schema Completo do Banco de Dados]]
- [[memory/projects/gb-import-hub-reconnection-plan|GB Import Hub — Plano de Reconexão do Frontend]]

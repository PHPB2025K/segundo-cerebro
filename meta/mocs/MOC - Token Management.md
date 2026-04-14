# MOC — Token Management

> Gestao centralizada de tokens OAuth cross-agent. Fragilidade sistemica identificada na auditoria 10/04/2026.

---

## Problema

Tres agentes independentes sofrem com gestao de tokens OAuth sem protocolo unificado:
- **Fisco**: bug redirect_uri, dual-sync JSON+Supabase, refresh 403 Filial
- **Trader**: relatório financeiro falha se qualquer token expirou
- **Spark**: Meta long-lived token 60d com expiracao ~15/05

## Tokens por agente

| Agente | Plataforma | TTL | Metodo | Credenciais |
|--------|-----------|-----|--------|-------------|
| [[openclaw/agents/trader/IDENTITY|Trader]] | ML (Vendas) | 6h | `ml-refresh-token.sh vendas` | `.ml-tokens.json` |
| [[openclaw/agents/trader/IDENTITY|Trader]] | ML (Finance) | 6h | `ml-refresh-token.sh finance` | `.ml-tokens-finance.json` |
| [[openclaw/agents/trader/IDENTITY|Trader]] | Shopee (3 contas) | 4h | Auto-refresh no script | `.shopee-tokens-*.json` |
| [[openclaw/agents/trader/IDENTITY|Trader]] | Amazon | Longo | LWA | 1Password |
| [[openclaw/agents/spark/IDENTITY|Spark]] | Meta Ads | ~60d | Long-lived system user | 1Password |
| [[openclaw/agents/spark/IDENTITY|Spark]] | Google Ads | — | Developer Token PENDENTE | — |
| [[openclaw/agents/fisco/IDENTITY|Fisco]] | Bling Matriz | 5h | Cron refresh | 1Password |
| [[openclaw/agents/fisco/IDENTITY|Fisco]] | Bling Filial | 5h | Cron refresh | 1Password |

## Licoes aprendidas

- [[openclaw/agents/kobe/shared/fisco/memory/context/lessons|Fisco lessons]] — dual-sync, redirect_uri, refresh 403
- [[openclaw/agents/kobe/shared/trader/memory/context/lessons|Trader lessons]] — validar TODOS os tokens antes de executar
- [[openclaw/agents/kobe/shared/spark/memory/context/lessons|Spark lessons]] — BM sem System Users, long-lived 60d

## Heartbeats que monitoram tokens

- [[openclaw/agents/trader/HEARTBEAT|Trader HEARTBEAT]] — validade ML/Shopee/Amazon
- [[openclaw/agents/spark/HEARTBEAT|Spark HEARTBEAT]] — token Meta expirando

---

*Criado: 10/04/2026 — Auditoria de conexoes*

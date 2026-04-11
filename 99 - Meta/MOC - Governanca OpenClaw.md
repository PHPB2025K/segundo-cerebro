# MOC — Governanca OpenClaw

> Hub de leveling, reviews, heartbeats e protocolos dos 6 agentes.

---

## Time de agentes

| Agente | Modelo | Level | Desde | Especialidade |
|--------|--------|-------|-------|--------------|
| [[agents/kobe/IDENTITY|Kobe]] | GPT 5.4 | L4 Trusted | 14/03 | Orquestracao, estrategia |
| [[agents/trader/IDENTITY|Trader]] | GPT 5.4 | L1 Observer | 19/03 | Marketplaces (ML, Amazon, Shopee) |
| [[agents/spark/IDENTITY|Spark]] | GPT 5.4 | L1 Observer | 23/03 | Trafego pago (Meta, Google) |
| [[agents/builder/IDENTITY|Builder]] | GPT 5.4 | L2 Contributor | 24/03 | Desenvolvimento (SaaS, sistemas) |
| [[agents/fisco/IDENTITY|Fisco]] | GPT 5.4 | L1 Observer | 28/03 | Fiscal (NF-e, distribuicao) |
| [[agents/rh/IDENTITY|RH]] | GPT 5.1-mini | L1 Observer | 30/03 | RH (ponto, compliance CLT) |

## Leveling system

Definido em [[agents/kobe/shared/TEAM|TEAM]]:
- **L1 Observer**: output revisado pelo Kobe; 5 entregas aprovadas → L2
- **L2 Contributor**: pode fazer deploy de fixes aprovadas sem aprovacao previa
- **L3 Trusted**: autonomia em seu dominio; escala excepcoes
- **L4 Hub**: autonomia quase total; escala so >R$500 ou mudancas estruturais

## Performance reviews

- [[agents/kobe/shared/lessons/reviews/builder-2026-03-26|Builder review 26/03]] — promovido L1→L2
- [[agents/kobe/shared/lessons/reviews/trader-2026-03-26|Trader review 26/03]] — mantido L1
- [[agents/kobe/shared/lessons/reviews/spark-2026-03-26|Spark review 26/03]] — mantido L1

## Heartbeats

| Agente | Status | Conteudo |
|--------|--------|---------|
| [[agents/kobe/HEARTBEAT|Kobe]] | Configurado | Emails, tokens, WhatsApp, orders, tasks |
| [[agents/trader/HEARTBEAT|Trader]] | Configurado | Tokens, pendencias, SKU performance |
| [[agents/spark/HEARTBEAT|Spark]] | Configurado | Token Meta, campanhas, anomalias |
| [[agents/builder/HEARTBEAT|Builder]] | Configurado | Deploys, Docker, SSL, vulnerabilidades |
| [[agents/fisco/HEARTBEAT|Fisco]] | ⚠️ Vazio | 3 crons criticos sem monitoramento |
| [[agents/rh/HEARTBEAT|RH]] | ⚠️ Vazio | 4 crons definidos sem monitoramento |

## Protocolos compartilhados

- [[agents/kobe/AGENTS|Kobe AGENTS]] — hierarquia de memoria, gate de encerramento, QA financeiro
- [[agents/kobe/BOOT|Kobe BOOT]] — checklist de startup
- [[agents/kobe/BOOTSTRAP|Kobe BOOTSTRAP]] — recuperacao de contexto degradado
- [[agents/kobe/shared/lessons/shared-lessons|Licoes compartilhadas]] — regras cross-agent

## Fallback chain

Primary: `openai-codex/gpt-5.4` → Fallback 1: `openai-codex/gpt-5.1-mini` → Fallback 2: `anthropic/claude-haiku-4-5`

---

*Criado: 10/04/2026 — Auditoria de conexoes*

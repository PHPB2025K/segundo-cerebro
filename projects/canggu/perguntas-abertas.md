---
tipo: questoes
projeto: Canggu
status: ativo
tags:
  - canggu
  - decisoes
  - pendente
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Perguntas em aberto

## Pendentes (precisam retomada)

### ADR-006: Portar pipeline ML pra `searchProductsEnriched` (base_products) em B4?

**Bloqueia:** escopo de [[debitos-tecnicos#B4]]

**Contexto:** pipeline WhatsApp foi migrado em phase1 do restructure para a camada semântica nova (base_products via `searchProductsEnriched`). Pipeline ML (`process-ml-question`) ficou no legacy (`searchProducts` em `products`). Respostas ao ML não beneficiam da nova estrutura.

**Opções:**
- (a) **Portar em B4** — incluir no escopo. +2-3 dias de esforço em B4. Beneficia: respostas ML ganham mesma qualidade que WhatsApp. Valida phase1 como padrão único.
- (b) **Adiar** — manter como dívida conhecida, abordar em próximo refator. ML continua usando `searchProducts` legado. Risco: divergência aumenta quando novos produtos forem adicionados só em base_products.

**Recomendação Claude Code:** (a) — resolve divergência, esforço marginal dentro do B4.

**Default se não decidir:** (b) — mantém escopo apertado.

**Ação:** Pedro reflete antes de iniciar B4. Se não decidir até lá, assume-se "não portar" por default.

**Ver:** [[decisoes#ADR-006]] (placeholder aguardando resolução)

---

## Resolvidas (referência)

| ADR | Tópico | Decisão | Detalhe |
|---|---|---|---|
| ADR-001 | Armazenamento service_role_key | `ALTER DATABASE SET app.settings.service_role_key` | [[decisoes#ADR-001]] |
| ADR-002 | `LOVABLE_API_KEY` | Remover direto | [[decisoes#ADR-002]] |
| ADR-003 | `test-semantic-search` | Manter com `verify_jwt=true` | [[decisoes#ADR-003]] |
| ADR-004 | `marketplace_chats*` | **Migration retroativa `CREATE TABLE IF NOT EXISTS`** (decisão revisada 22/04 após descoberta que tabelas são usadas por código ativo — `ml-webhook` + workflow N8N ML Messages) | [[decisoes#ADR-004]] |
| ADR-005 | Canal de alerting | Slack | [[decisoes#ADR-005]] |
| ADR-007 | Pipeline WhatsApp canônico | Edge function (`webhook-whatsapp`); depreciar N8N Principal | [[decisoes#ADR-007]] |

## Contexto

As 7 perguntas em aberto originais foram geradas no §7 do relatório
(`~/audit-canggu-forensics/AUDIT_REPORT.md`). Pedro respondeu 5 das 7 ao
aprovar o registro no vault (ADR-001, 002, 003, 005, 007). ADR-004 foi
respondida em 22/04 após investigação empírica — decisão mudou de "drop"
para "migration retroativa" após descoberta de que as tabelas são usadas
por código ativo. Resta apenas ADR-006 pendente, dependente de input
operacional do Pedro antes de iniciar B4.

Algumas decisões foram tomadas contra a recomendação original do relatório
(ex: canal de alerting — recomendação era Telegram, decisão foi Slack). Os
ADRs em [[decisoes]] refletem a decisão final.

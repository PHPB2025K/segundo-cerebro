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

**Contexto:** pipeline WhatsApp foi migrado em phase1 do restructure para a camada semântica nova (base_products via `searchProductsEnriched`). Pipeline ML ([[edge-functions|process-ml-question]]) ficou no legacy (`searchProducts` em `products`). Respostas ao ML não beneficiam da nova estrutura.

**Opções:**
- (a) **Portar em B4** — incluir no escopo. +2-3 dias de esforço em B4. Beneficia: respostas ML ganham mesma qualidade que WhatsApp. Valida phase1 como padrão único.
- (b) **Adiar** — manter como dívida conhecida, abordar em próximo refator. ML continua usando `searchProducts` legado. Risco: divergência aumenta quando novos produtos forem adicionados só em base_products.

**Recomendação Claude Code:** (a) — resolve divergência, esforço marginal dentro do B4.

**Default se não decidir:** (b) — mantém escopo apertado.

**Ação:** Pedro reflete antes de iniciar B4. Se não decidir até lá, assume-se "não portar" por default.

**Ver:** [[decisoes#ADR-006]] (placeholder aguardando resolução)

---

## Execução em andamento (pausada)

### B1 passos 1-5 — Rotação service_role (pausado em 2026-04-22 ~21:30)

**Status:** iniciado e pausado antes da geração de nova key.

**O que foi feito:**
- Tag defensiva criada: `b1-pre-rotation-20260422-211653` no monorepo
- Baseline dos 3 JWTs hardcoded confirmado (path:linha documentados
  em `~/audit-canggu-forensics/RAW/_b1_baseline.md`)
- Working copy **mantida dirty como estava** (12 M + 5 ??) — stash
  NÃO foi executado; decisão deliberada de adiar isolamento até a
  retomada
- Pré-commit assessment gerado em
  `~/audit-canggu-forensics/RAW/_precommit_assessment.md`

**O que NÃO foi feito (estado zero em produção):**
- Nenhuma nova key gerada no dashboard Supabase
- Nenhum `ALTER DATABASE SET` executado
- Nenhuma edição em migrations ou workflow JSON
- Key antiga continua válida
- `git stash` não foi rodado — working copy continua exposta no filesystem
- Zero mutação em produção

**Motivo da pausa:**
Confusão conceitual momentânea entre anon key e service_role key durante
a execução. Decisão prudente: parar e retomar com cabeça descansada.

**Para retomar:**
1. Ler [[decisoes#ADR-001]] (método de armazenamento = ALTER DATABASE SET)
2. Ler [[debitos-tecnicos#B1]] (plano completo dos passos 1-7)
3. Confirmar conceitualmente: **service_role** (admin, bypassa RLS),
   NÃO anon (baixo privilégio, pública por design)
4. `cd ~/Documents/05-Projetos-Codigo/budamix-ai-agent`
5. `git status --short` — confirmar 12 M + 5 ?? inalterados
6. Decisão opcional: fazer `git stash push -u` antes dos edits do B1
   para isolar o WIP do trabalho de segurança, ou seguir editando
   in-place (working copy dirty já antes, edits do B1 se somam a ela)
7. Executar B1 passos 1-7 em sessão dedicada do Claude Code
8. Depois, B1 passo 8: commit unificado (possivelmente 2 commits
   separados — feat(security) + feat original do WIP, se fez stash
   do WIP primeiro)

**Artefatos preservados:**
- Baseline: `~/audit-canggu-forensics/RAW/_b1_baseline.md`
- Tag git: `b1-pre-rotation-20260422-211653` no monorepo Canggu
- Pré-commit assessment: `~/audit-canggu-forensics/RAW/_precommit_assessment.md`
- Working copy: dirty no filesystem (NÃO em stash) — rollback via
  `git checkout <arquivo>` ou `git stash` ainda disponíveis

**Urgência:**
🔴 Alta — JWT service_role continua exposto em 3 arquivos versionados
há 46 dias (contagem desde 2026-03-06). Cada dia sem rotação aumenta
janela de risco. Prioridade para retomada: primeira tarefa de amanhã.

---

## Resolvidas (referência)

| ADR | Tópico | Decisão | Detalhe |
|---|---|---|---|
| ADR-001 | Armazenamento service_role_key | `ALTER DATABASE SET app.settings.service_role_key` | [[decisoes#ADR-001]] |
| ADR-002 | `LOVABLE_API_KEY` | Remover direto | [[decisoes#ADR-002]] |
| ADR-003 | `test-semantic-search` | Manter com `verify_jwt=true` | [[decisoes#ADR-003]] |
| ADR-004 | `marketplace_chats*` | **Migration retroativa `CREATE TABLE IF NOT EXISTS`** (decisão revisada 22/04 após descoberta que tabelas são usadas por código ativo — [[edge-functions\|ml-webhook]] + workflow N8N [[n8n-workflows#ML Messages (sg2yU46R9EQq3a2v)\|ML Messages]]) | [[decisoes#ADR-004]] |
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

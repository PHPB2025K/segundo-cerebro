---
tipo: moc
projeto: Canggu
status: ativo
tags:
  - canggu
  - moc
criado: 2026-04-22
atualizado: 2026-05-05
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Canggu — Map of Content

> MicroSaaS de atendimento WhatsApp automatizado da Budamix, operando sob
> a identidade **"Ana"**. Pipeline canônico: WhatsApp → Evolution Cloudfly
> → edge function `webhook-whatsapp` (Supabase) → process-message → LLMs
> (Anthropic Claude + Google Gemini + Groq) → Supabase pgvector → resposta
> via dispatcher inline. N8N standby pra rollback de 1 chamada.

## Onde vive (atualizado 2026-05-05)

| Camada | Local | Notas |
|---|---|---|
| **Repo (single source of truth)** | `PHPB2025K/canguu` | Frontend + 13 edge functions consolidadas em `supabase/functions/` |
| **Frontend admin (oficial)** | `https://canggu.com.br` | Vercel + DNS Registro.br (A apex+www → 76.76.21.21). SSL Let's Encrypt. Domínio adotado em 05/05 |
| **Frontend admin (fallback)** | `https://canguu-sigma.vercel.app` | Domínio Vercel default; continua aliased ao mesmo deploy de produção |
| **Backend** | Supabase project `jpacmloqsfiebvagfomt` | Edge functions, Storage `chat-attachments` (público), pgvector |
| **Webhook entrada** | `jpacmloqsfiebvagfomt.supabase.co/functions/v1/webhook-whatsapp` | Apontado pelo Evolution v2 desde cutover 30/04. Versão atual 29 (numbered-text origin poll a partir de 05/05 08:48 BRT) |
| **N8N (standby)** | `trottingtuna-n8n.cloudfy.live` | Rollback de 1 chamada se necessário |

## Estado atual

**Última grande sessão:** 2026-04-30 (maratona ~7-8h) — ver [[memory/sessions/2026-04-30]] seção "Maratona Canggu" + [[memory/context/decisoes/2026-04#[30/04 tarde/noite] Canggu — pipeline edge function canônico + mídia visível + repo único]].

**O que mudou em 05/05:**
- Pedro reportou regressão dupla (filtro Plataforma sumiu da UI + Ana parou de mandar origin poll). Investigação revelou que **não era código** — era drift de deploy:
  - Vercel tinha o bundle correto (`grep` no `index-B57kBlxQ.js` confirmou strings "Plataforma" e "Site Budamix"), mas o cache CDN estava com 4.5 dias (`age: 393877s`).
  - Edge function `webhook-whatsapp` versão 28 foi deployada em 30/04 13:29 BRT, **antes** do commit `604b2e3` (numbered-text origin poll, 17:28 BRT). Em produção rodava o `sendList` antigo que falha silenciosamente via Baileys.
- Resolução: `supabase functions deploy webhook-whatsapp --project-ref jpacmloqsfiebvagfomt` (→ v29) + `vercel redeploy` (cache CDN invalidado).
- **Migração de domínio oficial** pra `https://canggu.com.br`: DNS apex+www → 76.76.21.21, SSL Let's Encrypt emitido em ~2min, app respondendo HTTP/2 200 nos dois. Subdomínio `demo.canggu.com.br` (Lovable) e TXT `_lovable.*` foram preservados.
- Pendente: redirect www↔apex (decisão do Pedro), GitHub Action que rode `supabase functions deploy` automático no push pra main (resolveria a classe inteira de drift entre repo e edge functions).

**O que mudou em 30/04:**
- Cutover do pipeline: edge function `webhook-whatsapp` agora é o webhook canônico do Evolution. N8N Principal vira standby.
- Cobertura completa de tipos WhatsApp (sticker, location, contact, video, button replies, ephemeral/viewOnce wrappers; protocol/edited descartados).
- Vídeo + imagem com Gemini Vision/Video em background. Descrição em `metadata.ai_description` (Ana lê), arquivo no Storage `chat-attachments` (admin vê).
- Áudio também sobe pro Storage com player HTML5 inline.
- MediaLightbox flutuante no admin (zoom 1×-5×, pan, atalhos teclado).
- Origin poll via texto numerado (listMessage e poll nativo do WhatsApp falharam silenciosamente via Baileys — ver [[knowledge/concepts/evolution-baileys-protocol-quirks]]).
- Filtro de plataforma no admin + SourceBadge condicional.
- `customers.source = NULL` por padrão; só preenche quando cliente responde a enquete.
- Repo `budamix-ai-agent` deletado (era cópia paralela). Backup mirror em `~/Documents/_backups/budamix-ai-agent-mirror-20260430.git`.

**Fix urgente 30/04 noite — Hard-block contra "entre em contato conosco" no ML** ([[memory/context/decisoes/2026-04#[30/04 noite] Canggu — hard-block determinístico contra "entre em contato conosco" no ML]]):
- Threshold `search_corrections` baixado de 0.85 → 0.65 (perguntas variam demais em forma).
- `_shared/ml-response-validator.ts` ganhou `detectForbiddenContactRequest()` com 10 padrões regex que rejeitam frases tipo "entre em contato", "fale conosco", "estamos à disposição", "para mais detalhes ... contat".
- `process-ml-question` substitui em cadeia: correção aprovada → fallback técnico → last-resort hardcoded. Garantia determinística contra resposta evasiva no Mercado Livre.
- Equivalente WhatsApp **não tem** o guard (Ana É o canal de contato lá).

**Última auditoria forense:** 2026-04-22 ([[auditorias/2026-04-22-forense]])
**Veredito original:** 🟡 Sólido tecnicamente, comprometido por dívida operacional.
**Status pós-30/04:** B4 (arquitetura — cutover) ✅ feito. B3 (resiliência) parcial (Gemini retry pronto, falta retry classify/generate + dedup). B1/B2/B5/B6 ainda intocados.

## Métricas baseline (snapshot 2026-04-22)

- Backend: ~6.789 LOC TS (14 edge functions, 1 ghost)
- Frontend: ~7.657 LOC TS (14 rotas, 4 Zustand stores)
- Supabase: 63 tabelas, 234 functions, 21 triggers, **11 FKs** (integridade intencional), 26 RLS
- N8N: 5 workflows (2 com drift estrutural vs repo; 3 com drift de `active` state)
- Testes automatizados: 0
- CI/CD: ausente
- Secrets hardcoded em arquivos tracked: **3** (service_role JWT — ver [[decisoes#ADR-001]])

## Mapa de notas

### Conhecimento técnico

- [[arquitetura]] — diagrama + 5 fluxos end-to-end
- [[supabase-canggu]] — schema, triggers, pgvector, RLS
- [[edge-functions]] — 14 functions com estado de invocação e verify_jwt
- [[n8n-workflows]] — 5 workflows + drift live vs local + padrão Setup Credentials
- [[frontend]] — Vite + React 19 + rotas + integração Supabase

### Gestão e refatoração

- [[debitos-tecnicos]] — matriz de 24 achados + 6 blocos priorizados
- [[perguntas-abertas]] — decisões pendentes (ADR-004, ADR-006)
- [[backlog-features]] — features da Ana pedidas, aguardam encaixe no roadmap
- [[decisoes]] — ADRs cronológicos (decisões pré-auditoria + ADR-001 a ADR-007)
- [[auditorias/2026-04-22-forense]] — relatório completo da auditoria
- [[auditorias/2026-04-22-canggu-in-bc]] — auditoria anterior (resultado nulo)

## Dependências externas (P0)

- **Anthropic API** (Claude Haiku classify + Sonnet response)
- **OpenAI API** (text-embedding-3-small para pgvector)
- **Groq API** (Whisper — transcrição de áudio)
- **Evolution API Cloudfly** (`trottingtuna-evolution.cloudfy.live`, instance `BUDAMIX AI AGENT`)
- **N8N Cloudfly** (`trottingtuna-n8n.cloudfy.live`) — em depreciação parcial após [[decisoes#ADR-007]]
- **Supabase Cloud** (project `jpacmloqsfiebvagfomt`, region sa-east-1)

## Referência rápida a rodar

- Roadmap de refatoração: [[debitos-tecnicos#Blocos]]
- Próxima ação imediata: [[perguntas-abertas#Pendentes]] + executar B1 passos 1–2
- Risco mais crítico hoje: service_role JWT exposto em 3 arquivos tracked — ver [[decisoes#ADR-001]] e [[auditorias/2026-04-22-forense#Achado 1 — Service role JWT exposto]]
- Ghost function `test-search` deployed sem código no repo — ver [[auditorias/2026-04-22-forense#Achado 2 — Ghost function test-search|Achado 2 (ghost test-search)]]

## Histórico pré-auditoria

Contexto operacional acumulado entre 06/04 e 17/04 (downtime da Ana,
restauração, padrões estabelecidos, pendências pré-auditoria) está
preservado em [[_historico]]. Referência essencial para entender o
estado atual do código. As decisões-chave desse período também estão
consolidadas cronologicamente em [[decisoes#Decisões pré-auditoria]].

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
| **Webhook entrada** | `jpacmloqsfiebvagfomt.supabase.co/functions/v1/webhook-whatsapp` | Apontado pelo Evolution v2 desde cutover 30/04. Versão atual 30 (numbered-text origin poll a partir de 05/05 08:48 BRT) |
| **CI auto-deploy** | `.github/workflows/deploy-edge-functions.yml` | Push em `supabase/functions/**` ou `workflow_dispatch` redeploya automaticamente. Cascade total se `_shared/` mudar, parcial se só uma função. Secret `SUPABASE_ACCESS_TOKEN` no repo. Ativo desde 05/05 |
| **N8N (standby)** | `trottingtuna-n8n.cloudfy.live` | Rollback de 1 chamada se necessário |

## Estado atual

**Última grande sessão:** 2026-04-30 (maratona ~7-8h) — ver [[memory/sessions/2026-04-30]] seção "Maratona Canggu" + [[memory/context/decisoes/2026-04#[30/04 tarde/noite] Canggu — pipeline edge function canônico + mídia visível + repo único]].

**O que mudou em 06/05 (incidente Ana 24/7):**

Manhã (~08:30-08:50 BRT) — Pedro reportou Ana respondendo "horário de atendimento de segunda a sexta, das 8h às 18h" (que contradiz proposta 24/7 inviolável) + origin poll ausente. Investigação: a frase exata aparece 11x no histórico em fev-mar/2026, **zero ocorrências nas últimas 24h** — print provavelmente antigo, mas a classe de bug continua viva (regra 11 do system_prompt era só persuasiva).

Resolução em duas camadas + bonus, commit `604969a fix(ana): blindar 24/7 + ampliar gating do origin poll`:

- **Camada A — prompt reforçado.** UPDATE no `agent_config.system_prompt` aplicado direto via Management API (19.452 → 20.209 chars). Regra 11 reescrita com bloco `PROIBIDO ABSOLUTAMENTE` listando frases negativas literais (segunda a sexta, Xh às Yh, expediente, deixe sua mensagem, retornaremos em breve, etc) + frase canônica obrigatória de resposta: *"Estou disponível 24 horas por dia, 7 dias por semana. Como posso te ajudar?"*. Migration registrada em `supabase/migrations/20260506100000_strengthen_24_7_rule.sql` pra rastreabilidade.
- **Camada B — guardrail determinístico.** `_shared/response-validator.ts` ganhou `BUSINESS_HOURS_FORBIDDEN_PATTERNS` (11 regex) + `detectBusinessHoursLimit()` exposto + HARD BLOCK no início de `validateResponse()`. Quando aciona, a resposta INTEIRA é substituída pela canônica antes de chegar ao N8N — não tenta remendar. Razões logadas em warnings (`forbidden_business_hours:*` + `business_hours_blocked_substituted`). 8/8 smoke tests Deno passando, incluindo falsos positivos (preço, prazo de entrega, cores).
- **Bonus — origin poll defensivo.** `webhook-whatsapp/index.ts` ampliou gating: `(customer._isNew || customer.source == null) && isNewConversation && assigned_to='agent'`. Cobre 5 customers com `source IS NULL` (4 criados últimos 7d) que tinham caído num gap. Loop continua protegido — uma vez source preenchido, não repete. Caso reportado pelo Pedro tinha customer com `source='whatsapp'` já (poll respondida antes como "outro") — gating amplo cobre defensivamente sem repetir poll desnecessário.
- **Auto-deploy GitHub Actions** (cedbe43 ontem) cascade ativou via mudança em `_shared/`: run `25433307681` deployou todas 13 functions em ~50s. `process-message` v38→**v39**, `webhook-whatsapp` v30→**v31**.
- Erro TS pré-existente em `_shared/evolution-api.ts` (`EvolutionMessageContent` referenciado mas tipo se chama `EvolutionMessageData`) detectado durante `deno check` mas NÃO foi tocado — fora de escopo do incidente. Edge functions deployam mesmo com warning. Anotado pra cleanup depois.

**O que mudou em 05/05 (dia inteiro de drift cleanup):**

Manhã (~08:30-09:05 BRT):
- Regressão dupla reportada — filtro Plataforma sumiu da UI + Ana parou de mandar origin poll. **Não era código**, era drift de deploy: Vercel CDN com `age: 393877s` (4.5 dias) e edge function `webhook-whatsapp` v28 deployada antes do commit `604b2e3`. Resolução: redeploy edge fn (→ v29) + `vercel redeploy` (cache invalidado).
- **Migração de domínio oficial** pra `https://canggu.com.br`: DNS apex+www → 76.76.21.21 no Registro.br, SSL Let's Encrypt emitido em ~2min. Subdomínio `demo.canggu.com.br` (Lovable) e TXT `_lovable.*` preservados.

Tarde (~13:30-16:40 BRT):
- **Terceira regressão do dia:** Ana respondeu pergunta no MLB3343832496 com "Por favor entre em contato conosco para conhecer outros modelos disponíveis!". Causa: `process-ml-question` v10 deployada **9 segundos antes** do commit `1b88990` (hard-block). Detector existia em `_shared/`, mas a chamada `validateMLQuestionResponse()` em `process-ml-question/index.ts` ainda não tinha sido pushada. Resolução: redeploy → v11.
- **Auditoria preventiva** das 14 edge functions revelou 9 outras stale desde `b2c6d0f` (consolidação 30/04 12:55 BRT). Redeploy manual de cada → 13/13 sincronizadas. Função órfã `test-search` deletada.
- **GitHub Action de auto-deploy implementado** (commit `cedbe43`): trigger em push pra `main` filtrando `supabase/functions/**` ou `workflow_dispatch` manual. Detecta mudanças em `_shared/` → cascade total; senão só a função tocada. Pedro adicionou `SUPABASE_ACCESS_TOKEN` como secret. Validado end-to-end em dois runs (47s + 37s). **Drift entre repo e produção eliminado por construção.**
- **Tom da Ana no ML reescrito** (commit `38d3fef`): regras 9, 10, 12 do prompt + `ML_QUESTION_FALLBACK` + `ML_MESSAGE_FALLBACK` em `_shared/ml-response-validator.ts`. Identificado conflito interno crítico — regra 9 mandava "estamos a disposição" que está nos `FORBIDDEN_CONTACT_PATTERNS`. Reescrito pra tom natural, sem frases prontas tipo telemarketing. `process-ml-question` v13 em produção. Push disparou Action que redeployou tudo automático.

Pendente:
- Redirect www↔apex em `canggu.com.br` (recomendação CC: www → apex)
- Editar manualmente resposta no MLB3343832496 no painel ML + colar correção sugerida no Canggu via 👎 (alimenta `process-correction-embedding` pra perguntas semelhantes futuras)
- Estender análise de tom pra `process-message` (Ana no WhatsApp)
- Atualizar GitHub Actions de Node 20 → 24 antes de 16/09/2026

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
**Status pós-30/04:** B4 (arquitetura — cutover) ✅ feito. B3 (resiliência) parcial (Gemini retry pronto, falta retry classify/generate + dedup). B1/B2/B6 ainda intocados.
**Status pós-05/05:** B5 (CI/CD) ✅ resolvido — auto-deploy via GitHub Actions ativo, drift entre repo e produção eliminado por construção.

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

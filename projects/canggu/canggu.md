---
tipo: moc
projeto: Canggu
status: ativo
tags:
  - canggu
  - moc
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Canggu — Map of Content

> MicroSaaS de atendimento WhatsApp automatizado da Budamix, operando sob
> a identidade **"Ana"**. Pipeline distribuído: WhatsApp → Evolution Cloudfly
> → edge functions + N8N → LLMs (Anthropic + OpenAI + Groq) → Supabase
> pgvector → resposta.

## Estado atual

**Última auditoria:** 2026-04-22 ([[auditorias/2026-04-22-forense]])
**Veredito:** 🟡 Sólido tecnicamente, comprometido por dívida operacional.
Refatoração viável em 6 blocos ao longo de 6–10 semanas.

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
- Risco mais crítico hoje: service_role JWT exposto em 3 arquivos tracked — ver [[decisoes#ADR-001]] e [[auditorias/2026-04-22-forense#Achado-1]]
- Ghost function `test-search` deployed sem código no repo — ver [[auditorias/2026-04-22-forense#Achado-2]]

## Histórico pré-auditoria

Contexto operacional acumulado entre 06/04 e 17/04 (downtime da Ana,
restauração, padrões estabelecidos, pendências pré-auditoria) está
preservado em [[_historico]]. Referência essencial para entender o
estado atual do código. As decisões-chave desse período também estão
consolidadas cronologicamente em [[decisoes#Decisões pré-auditoria]].

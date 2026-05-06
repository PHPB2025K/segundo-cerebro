---
title: "decisions"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Decisões — [[openclaw/agents/builder/IDENTITY|Builder]]
## Regra Universal — Horários em Brasília (2026-04-01)
TODOS os horários apresentados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de exibir. Vale para relatórios, alertas, logs, timestamps — qualquer comunicação.


### 2026-04-28 — Social Studio separado do Blog
- Blog é conteúdo longo/SEO; Social Studio é conteúdo curto/visual para Instagram, carrosséis, calendário e publicação futura.
- Origens aprovadas: do zero, de produto, do Blog.

### 2026-04-28 — Budamix E-commerce usa Deploy Key dedicada para push do Kobe
- Para repo privado, preferir Deploy Key SSH por repo com write access em vez de PAT solto.

### 2026-04-30 — Canggu repo único
- Repo `canguu` é o single source of truth do frontend admin e edge functions.
- `budamix-ai-agent` foi deletado após backup mirror.
- Lovable não é mais fonte ativa; Vercel `canguu-sigma.vercel.app` serve o admin.

### 2026-04-30 — Budamix Central Estoque
- Módulo Estoque terá abas Full/Físico/Consolidado.
- Fase 2 usará role `operator`, sem delete de movimentações; correção por contramov.
- Sync app→planilha deve rodar a cada 2min.

## 2026-05-05 — Estoque Budamix

- Repo canônico desejado: `PHPB2025K/estoque-budamix` privado.
- Produção segue na VPS via build rsync histórico até completar remediação.
- App é desktop-only.
- Próximo passo recomendado: Deploy Key SSH read-only na VPS para permitir `git fetch`/`reset --hard origin/main` com backup e rollback.

## 2026-05-05 — Canggu CI/CD

- Edge Functions Supabase do Canggu devem ser deployadas via GitHub Actions; mudanças em `_shared/` exigem redeploy total.

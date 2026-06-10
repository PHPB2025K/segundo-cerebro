---
title: "decisions"
created: 2026-04-14
type: agent
agent: builder
status: active
tags:
  - agent/builder
---

# Decisões — Builder

_Registro de decisões permanentes. NUNCA contradizer._

## Stack

### Stack padrão definido (2026-03-19)
- **Frontend:** Next.js 15 + React 19 + Tailwind + shadcn/ui
- **Backend full-stack:** Next.js API Routes + Server Actions
- **Backend standalone:** FastAPI (Python) — para APIs independentes, ML, data
- **DB:** Supabase (Postgres) + Drizzle ORM
- **Auth:** Supabase Auth
- **Deploy SaaS:** Vercel
- **Deploy interno:** VPS com Docker
- **Pagamentos:** Stripe
- **Versionamento:** Git + GitHub (PHPB2025K)
- **Package manager:** pnpm
- **TypeScript:** Strict mode sempre

### Commits convencionais (2026-03-19)
- Formato: `feat:`, `fix:`, `refactor:`, `chore:`, `docs:`
- Nunca commitar direto em main (L1)

## Segurança

### Credenciais — NUNCA em código (2026-03-17)
- Credenciais vão para 1Password vault "OpenClaw" ou variáveis de ambiente
- Nunca em código, commits, CLAUDE.md, ou arquivos de contexto de IA
- **Case real:** Auditoria Bidspark encontrou Client ID + Secret em plain text no CLAUDE.md do Amazon Ads

### Bidspark — Ambiente sandbox (2026-03-17)
- Amazon Ads está em sandbox. Antes de ativar otimizações reais: confirmar `AMAZON_ADS_ENVIRONMENT=production` no `.env`
- Não ir pra produção sem trocar

## Projetos

### Bidspark — Validação antes de test users (2026-03-17)
- Pedro quer acumular semanas de dados de otimização real (Amazon Ads) antes de abrir para test users
- Comprovar redução de ACOS e melhoria de ROAS com case próprio primeiro
- Bloqueio atual: zero testes unitários — precisa de suite mínima antes de produção
- Status: ~90% pronto tecnicamente. Bloqueio = validação de resultados, não código

## Operacional

### Team Agents (2026-03-19)
- Builder é agente especializado dev/MicroSaaS
- Coordenado pelo Kobe — nunca fala direto com Pedro
- Resultados sempre entregues ao Kobe para validação

## 2026-05-05 — Estoque Budamix

- Repo canônico desejado: `PHPB2025K/estoque-budamix` privado.
- Produção segue na VPS via build rsync histórico até completar remediação.
- App é desktop-only.
- Próximo passo recomendado: Deploy Key SSH read-only na VPS para permitir `git fetch`/`reset --hard origin/main` com backup e rollback.

## 2026-05-05 — Canggu CI/CD

- Edge Functions Supabase do Canggu devem ser deployadas via GitHub Actions; mudanças em `_shared/` exigem redeploy total.

## 2026-05-11 — Canggu ML guard final e FBA removal

- Canggu/Ana ML deve manter guard determinístico imediatamente antes do POST externo em todas as rotas que respondem marketplace; `ml-webhook` foi corrigida no repo canônico `PHPB2025K/canguu` em `eb76d3f`.
- Budamix Central/Amazon sync deve filtrar pedidos de remoção FBA como não-venda pela assinatura `Non-Amazon` + `AFN` + datas dummy 1995/S01.
- Pipeline RH WhatsApp deve aceitar `@lid`/aliases/pushName para inbound.

## 2026-05-22 — Canggu: deploy de Edge Functions internas com `NO_JWT_FUNCTIONS`

- Functions internas protegidas por `X-Internal-Token` podem operar temporariamente com `verify_jwt=false` somente quando listadas explicitamente em `NO_JWT_FUNCTIONS` no GitHub Actions.
- A lista deve ser preservada pelo workflow de deploy; qualquer function adicionada a ela passa a depender de segredo interno e precisa validação E2E de branch normal e branch de escalação.
- Essa decisão é mitigação temporária do incidente JWT da Ana/Canggu. A meta técnica continua sendo pós-mortem da causa raiz e retorno a `verify_jwt=true` quando seguro.
- Teste aceitável precisa provar conversa real completa, incluindo notificação visual ao Pedro quando houver escalação.

## 2026-06-04 — Budamix Facebook Page / Meta Graph

- Página Budamix passou a ser gerenciável via Meta Graph com token operacional e documentação de referência.
- App Meta correto para page management foi identificado; a credencial precisa ser tratada como compartilhada com runtime OpenClaw e qualquer rotação deve atualizar ambos os lados.
- Vanity URL `/budamix` ficou postergada para ajuste manual no Meta Business Suite, pois a API/UI atual bloquearam o fluxo automático.

## 2026-06-04 — Daily Sales Shopee v4.0

- Daily Sales Shopee permanece em standby por decisão do Pedro: Fase 1 validada, mas sem cron 07:00 BRT até lapidação e smokes das contas 2 e 3.
- Mission Control deve manter Shopee em página dedicada, isolada da página de Mercado Livre, para evitar regressão e colisão de namespace.
- Slack do Daily Sales Shopee deve ser consolidado para Pedro, não uma mensagem por camada.

## 2026-06-09 — Estoque / Planilha e automações

- Aba ESTOQUE da planilha oficial usa estrutura A:H: ESTOQUE, SKU BASE, DESCRIÇÃO, CUSTO, EAN, NCM, MARCA, CUSTO ESTOQUE TOTAL. Qualquer escrita futura deve validar esses headers reais antes de alterar dados e não deve usar o mapeamento antigo.
- Alterações na Planilha de Estoque devem preservar formatação, cores, validações e padrão visual/estrutural copiando linha modelo equivalente; se a ferramenta não permitir copiar formatação com segurança, abortar ou trocar de API.
- Automações WhatsApp Estoque e ENVIOS FULL foram pausadas por decisão operacional. Auditorias/recomendações que dependem desses dados precisam declarar essa limitação até reativação validada.

## 2026-06-09 — Budamix E-commerce / Blog

- Blog Budamix em tema livre opera sem geração automática de imagens enquanto não houver decisão de voltar créditos/integração de imagem; artigos ficam para revisão/upload manual no admin.
- Filtro de formato da loja usa query string e a coluna existente de formato dos produtos, sem criar coleção ou schema novo.
- Banners do hero podem funcionar como CTAs visuais para recortes da loja, com proteção contra falso clique pós-swipe.

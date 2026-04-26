---
title: "prd-mission-control"
created: 2026-04-26
type: doc
agent: kobe
status: active
tags:
  - agent/kobe
  - doc
---
# PRD — Mission Control (TenacitOS) para o Kobe

_Product Requirements Document — Deploy do painel visual de monitoramento_

---

## 1. Visão Geral

Deployar o [TenacitOS](https://github.com/carlosazaustre/tenacitOS) como painel visual do Kobe, customizado para a operação da GB Importadora. O Pedro acessa via navegador e vê o estado completo do sistema num relance — sem precisar perguntar no Telegram.

**URL de acesso:** `https://mission.gbformulario.com` (subdomínio dedicado via Traefik)

---

## 2. O Que o Pedro Ganha

| Antes (só Telegram) | Depois (Mission Control) |
|---------------------|--------------------------|
| "Kobe, como tão os crons?" → espera resposta | Abre o painel, vê 20 crons com status/cores |
| "Kobe, tem alguma pendência?" | Kanban visual de pendências por prioridade |
| "Quanto tô gastando de IA?" | Gráfico de custo diário + projeção mensal |
| "O WhatsApp tá conectado?" | Semáforos de saúde: verde/amarelo/vermelho |
| "O que o Builder fez hoje?" | Timeline de atividade por agente |

---

## 3. Infraestrutura Atual

| Recurso | Estado | Impacto do Mission Control |
|---------|--------|---------------------------|
| RAM | 2.5GB/3.8GB (66%) | +50-80MB (Next.js) → ~70% — OK |
| Disco | 28GB/48GB (58%) | +200MB (node_modules + build) → ~59% — OK |
| PM2 | 2 processos (Budamix + Ponto Certo) | +1 processo (mission-control) |
| Portas | 3000 (Budamix), 3091 (Ponto Certo) | +3092 (Mission Control) |
| Traefik | 5 rotas dinâmicas | +1 rota (mission.gbformulario.com) |
| Node.js | v22.22.1 | ✅ Compatível (req: 18+) |

**Veredito: VPS aguenta.** Margem confortável de RAM e disco.

---

## 4. Plano de Deploy — Passo a Passo

### Fase 1: Clone e Configuração (5 min)

```
1. cd /root/.openclaw/workspace
2. git clone https://github.com/carlosazaustre/tenacitOS.git mission-control
3. cd mission-control
4. cp .env.example .env.local
5. Configurar .env.local (ver seção 5)
6. npm install
```

### Fase 2: Build e PM2 (3 min)

```
1. npm run build
2. pm2 start npm --name mission-control -- start -- -p 3092
3. pm2 save
```

### Fase 3: Traefik HTTPS (2 min)

Criar `/docker/traefik/dynamic/mission-control.yml`:
```yaml
http:
  routers:
    mission-control:
      rule: "Host(`mission.gbformulario.com`)"
      entryPoints:
        - websecure
      service: mission-control
      tls:
        certResolver: letsencrypt
      priority: 100
  services:
    mission-control:
      loadBalancer:
        servers:
          - url: "http://127.0.0.1:3092"
```

### Fase 4: DNS (1 min)

Apontar `mission.gbformulario.com` → `187.77.237.231` (A record no Hostinger DNS).

### Fase 5: Credenciais no 1Password (1 min)

Salvar ADMIN_PASSWORD e AUTH_SECRET no vault OpenClaw.

### Fase 6: Teste e Validação (2 min)

Acessar `https://mission.gbformulario.com`, fazer login, verificar todos os módulos.

---

## 5. Configuração .env.local

```env
# Auth
ADMIN_PASSWORD=<gerar: openssl rand -base64 18>
AUTH_SECRET=<gerar: openssl rand -base64 32>

# OpenClaw paths
OPENCLAW_DIR=/root/.openclaw
OPENCLAW_WORKSPACE=/root/.openclaw/workspace

# Branding — Kobe
NEXT_PUBLIC_AGENT_NAME=Kobe
NEXT_PUBLIC_AGENT_EMOJI=🤖
NEXT_PUBLIC_AGENT_DESCRIPTION=COO digital da GB Importadora — 5 agentes, 20 crons, 14 integrações
NEXT_PUBLIC_AGENT_LOCATION=Pedreira, SP
NEXT_PUBLIC_BIRTH_DATE=2026-03-14
NEXT_PUBLIC_AGENT_AVATAR=
NEXT_PUBLIC_OWNER_USERNAME=Pedro Broglio
NEXT_PUBLIC_OWNER_EMAIL=pehpbroglio@gmail.com
NEXT_PUBLIC_OWNER_COLLAB_EMAIL=gb.ai.agent@gbimportadora.com
NEXT_PUBLIC_TWITTER_HANDLE=
NEXT_PUBLIC_COMPANY_NAME=GB IMPORTADORA
NEXT_PUBLIC_APP_TITLE=Kobe Mission Control
```

---

## 6. Fixes e Customizações Necessárias

### 6.1 Segurança — Hardening Obrigatório

| Fix | Prioridade | Descrição |
|-----|-----------|-----------|
| Bind localhost only | 🔴 Alta | Alterar `next start -H 0.0.0.0` para `-H 127.0.0.1` no PM2. Acesso externo só via Traefik (HTTPS). |
| UFW não precisa abrir porta | 🟢 | Traefik já roda na 443. Porta 3092 fica em loopback. |
| Forçar secure cookie | 🔴 Alta | Setar `NODE_ENV=production` no PM2 para que o cookie auth tenha `secure: true`. |
| Rate limit + IP logging | 🟡 | Já existe (5 tentativas, lockout 15min). OK pra uso pessoal. |
| Bloquear `restart-gateway` por default | 🟡 | Considerar remover essa action ou adicionar confirmação. Pedro pode reiniciar via Telegram se precisar. |
| Desabilitar file delete no primeiro deploy | 🟡 | Até validar que os PROTECTED paths cobrem tudo. |

### 6.2 Customizações Kobe-Específicas

| Item | Descrição |
|------|-----------|
| Agentes no Dashboard | O app auto-descobre de openclaw.json. Verificar se Trader, Spark, Builder, Fisco e RH aparecem. Se não, mapear manualmente. |
| Crons | Já lê via `openclaw cron list --json`. Os 20+ crons devem aparecer automaticamente. |
| Branding | Trocar nome, emoji, cores para identidade do Kobe. |
| Health checks | Adicionar checks específicos: Bling tokens, ML tokens, WhatsApp status, Supabase. |
| Cost tracking | O app usa SQLite local. Rodar `scripts/collect-usage.ts` para popular com dados históricos. Criar cron OpenClaw para rodar a cada 1h. |
| Memory browser | Aponta para /root/.openclaw/workspace — nosso workspace. Deve funcionar out-of-the-box. |
| Office 3D | Fun feature — 5 mesas (uma por agente). Opcional, mas Pedro vai gostar. |

### 6.3 Dados Iniciais

| Dado | Fonte | Ação |
|------|-------|------|
| Activities | Sessões existentes | Rodar collect-usage.ts para popular SQLite |
| Tasks | pending.md | Criar script parser: pending.md → tasks table |
| Crons | OpenClaw cron list | Auto-descoberto, sem ação |
| Health | Probes de status | Configurar endpoints de health check |
| Costs | Session logs | collect-usage.ts popula automaticamente |

---

## 7. Integração com Crons Existentes

### Novos crons necessários (OpenClaw)

| Cron | Frequência | Modelo | Função |
|------|-----------|--------|--------|
| Usage Collector | 1h | Haiku | Roda `collect-usage.ts` para alimentar SQLite de custos |
| Health Updater | 15min | Haiku | Atualiza status dos serviços (Bling, ML, WhatsApp, etc.) |
| Task Sync | 30min | Haiku | Parseia pending.md → sincroniza com tasks no dashboard |

### Crons existentes que alimentam o dashboard (sem mudança)

- Checagem Proativa (3x/dia) → aparece no health
- Watchdog (8h) → status dos crons
- Session Extractor (30min) → alimenta memory/activity
- Contingency Guard (15min) → status de rate limits

---

## 8. Riscos e Mitigações

| Risco | Probabilidade | Mitigação |
|-------|--------------|-----------|
| RAM insuficiente com 3 processos Next.js | Média | Monitorar com `free -h`. Se necessário, subir VPS para 8GB (Hostinger permite upgrade). |
| Build falha (dependências) | Baixa | Node 22 compatível. Se falhar, usar `--legacy-peer-deps`. |
| Conflito de porta | Baixa | Usar 3092 (confirmado livre). |
| Exposição de dados via file browser | Média | Arquivo .env e credenciais já estão em .gitignore. Verificar que 1Password keys não aparecem. |
| Auth bypass | Baixa | Middleware cobre todas as rotas. Cookie httpOnly + secure. Rate limiting ativo. |
| Bling/ML tokens visíveis no terminal | Baixa | Terminal bloqueia `env`, `cat .env*`, `curl`. Mas `cat` de outros arquivos é livre — verificar que tokens não estão em arquivos de workspace. |

---

## 9. Cronograma

| Etapa | Tempo | Quem |
|-------|-------|------|
| Clone + config + build | 10 min | Kobe (Builder) |
| Traefik + DNS | 5 min | Kobe + Pedro (DNS) |
| Credenciais 1Password | 2 min | Kobe |
| Teste + validação | 5 min | Pedro |
| Hardening (fixes seção 6.1) | 10 min | Kobe |
| Customizações Kobe (branding, health) | 30 min | Kobe |
| Crons de alimentação | 10 min | Kobe |
| **Total** | **~1h** | |

---

## 10. Critérios de Sucesso

- [ ] Pedro acessa `https://mission.gbformulario.com` e vê dashboard com dados reais
- [ ] 5 agentes aparecem com status
- [ ] 20+ crons listados com última execução e próxima
- [ ] Custo do dia/mês visível
- [ ] Saúde do sistema com semáforos (verde = OK)
- [ ] Memory browser mostra arquivos do workspace
- [ ] Terminal funcional (read-only)
- [ ] Login seguro com senha forte
- [ ] Nenhuma porta exposta além do Traefik (443)

---

## 11. Decisão Necessária do Pedro

Antes de executar:

1. **DNS:** Confirma que `mission.gbformulario.com` é o subdomínio que quer? Ou prefere outro nome (ex: `control.gbformulario.com`, `kobe.gbformulario.com`)?
2. **Prioridade:** Quer que eu execute agora (noite) ou amanhã no horário comercial?
3. **Office 3D:** Quer o módulo 3D com avatares dos agentes (fun mas consome ~20MB extra de RAM) ou prefere desabilitar?

---

_PRD gerado em 30/03/2026 22:56 UTC pelo Kobe._

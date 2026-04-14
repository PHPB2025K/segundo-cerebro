---
title: "Fase2 Capacitacao Spark"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Fase 2 — Capacitação do Agente Spark

_De: Kobe | Data: 2026-03-24 | Status: Aguardando Fase 1 concluída_

---

## Pré-requisitos

- [x] Google Ads Developer Token Standard (confirmado — mutate validate_only aceito)
- [ ] Fase 1 concluída (schema + webapp)
- [ ] Tabelas campaign_requests, alerts, optimizations, automation_rules, execution_log criadas no Supabase

---

## Skill 1 — google-ads-campaign-create

**Path:** `shared/spark/skills/google-ads-campaign-create/SKILL.md`

**Escopo:** Criar campanhas Search e Shopping no Google Ads via API v23.

**O que a skill cobre:**
- OAuth2 refresh → access token
- Criar CampaignBudget (daily ou total)
- Criar Campaign (Search ou Shopping) com bidding strategy
- Criar Ad Groups com targeting
- Criar Ads (Responsive Search Ads / Shopping)
- Mapear keywords (Search) ou product groups (Shopping)
- Gravar platform_ids de volta no Supabase (campaign_requests)
- Logar toda execução no execution_log

**Bidding strategies suportadas:**
- Manual CPC
- Maximize Conversions (com CPA target opcional)
- Target ROAS

**Referência API:** Google Ads API v23 — Campaign, AdGroup, Ad, Keyword resources

---

## Skill 2 — meta-ads-campaign-create

**Path:** `shared/spark/skills/meta-ads-campaign-create/SKILL.md`

**Escopo:** Criar campanhas de Conversão no Meta Ads via Marketing API v21.

**O que a skill cobre:**
- Criar Campaign com objective OUTCOME_SALES
- Criar Ad Sets com targeting, placements, orçamento, schedule
- Criar Ads com creative (imagem + copy)
- Upload de criativos via Ad Creative API
- Gravar platform_ids de volta no Supabase
- Logar toda execução no execution_log

**Targeting suportado:**
- Lookalike audiences
- Custom audiences (se disponível)
- Interest targeting
- Demographics (age, gender, location)

**Placements:** Automatic ou manual (Feed, Stories, Reels)

---

## Skill 3 — ads-monitoring

**Path:** `shared/spark/skills/ads-monitoring/SKILL.md`

**Escopo:** Monitorar campanhas ativas, comparar vs metas, gerar alertas.

**Lógica principal:**
1. Buscar todas campaign_requests com status `live`
2. Puxar métricas atuais das APIs (Google + Meta)
3. Gravar em metric_snapshots (tipo: basic ou complete)
4. Para cada campanha com meta_goals definidas:
   - Se CPA real > CPA target por > Xh → alerta cpa_above_target
   - Se ROAS real < ROAS min por > Xh → alerta roas_below_min
   - Se budget_spent_total > 90% budget_cap → alerta budget_cap_near
   - Se CTR < CTR min → alerta ctr_below_min
   - Se spend diário > 150% do budget diário → alerta budget_anomaly
5. Gravar alertas no Supabase (tabela alerts)
6. Alertas critical → notificar Kobe imediatamente (que repassa ao Pedro)
7. Alertas warning → acumular pro briefing

**Classificação de severidade:**
- info: variações normais, informativo
- warning: métrica fora da meta mas dentro de margem tolerável (< 2x)
- critical: métrica muito fora ou budget em risco

**Frequências:**
- Básico (1h): spend, clicks, impressions → metric_snapshots tipo basic
- Completo (4h): + conversions, CPA, ROAS, CTR, CPC, CPM, frequency, reach → tipo complete
- Daily (03:00 SP): snapshot completo + consolidação dados > 30d → tipo daily

---

## Skill 4 — ads-optimization-suggest

**Path:** `shared/spark/skills/ads-optimization-suggest/SKILL.md`

**Escopo:** Analisar performance e gerar sugestões de otimização.

**Tipos de sugestão:**

| Tipo | Condição | Ação sugerida |
|------|----------|---------------|
| pause_adset | CPA > 2x meta por > 72h, 0 conversões últimos 5d | Pausar ad set |
| redistribute_budget | Ad set A tem ROAS > 2x ad set B | Mover % budget de B→A |
| adjust_bid | CPC muito alto vs conversão | Reduzir bid ou mudar strategy |
| scale_up | ROAS > meta por > 7d com budget < 80% | Aumentar budget 20% |
| scale_down | ROAS caindo tendência 7d | Reduzir budget 20% |
| ab_test | Campanha > 14d sem variação de creative | Sugerir novo criativo |
| pause_campaign | CPA > 3x meta por > 7d | Pausar campanha inteira |

**Output:** Grava na tabela optimizations com:
- Descrição clara em português
- Justificativa com dados (números reais)
- Impacto esperado quantificado
- Campo changes com os parâmetros exatos da ação

**Frequência:** A cada 4h, analisar todas as campanhas live

---

## Skill 5 — ads-optimization-execute

**Path:** `shared/spark/skills/ads-optimization-execute/SKILL.md`

**Escopo:** Executar otimizações aprovadas e regras automáticas.

**Fluxo de otimizações aprovadas:**
1. Buscar optimizations com status `approved`
2. Para cada: executar a ação via API (Google ou Meta)
3. Atualizar status → `executed` ou `failed`
4. Gravar resultado em execution_result
5. Logar no execution_log

**Fluxo de automation_rules:**
1. Buscar rules com `enabled = true`
2. Para cada rule: verificar cooldown (last_triggered_at + cooldown_hours < now)
3. Avaliar condição contra métricas atuais de todas as campanhas no scope
4. Se condição verdadeira: executar ação, atualizar last_triggered_at e trigger_count
5. Logar no execution_log com source = 'automation_rule'

**Ações executáveis:**
- pause_adset: PATCH ad set status → PAUSED
- pause_campaign: PATCH campaign status → PAUSED
- adjust_budget: PATCH campaign budget
- adjust_bid: PATCH ad group bid
- alert: criar alerta no Supabase (sem chamada API externa)

---

## Crons a configurar

| Cron | Frequência | Skill | Descrição |
|------|------------|-------|-----------|
| ads-sync-basic | 0 * * * * (1h) | ads-monitoring | Métricas básicas |
| ads-sync-complete | 0 */4 * * * (4h) | ads-monitoring | Métricas completas |
| ads-daily-snapshot | 0 6 * * * (03:00 SP) | ads-monitoring | Snapshot diário + consolidação |
| ads-suggest | 30 */4 * * * (4h, :30) | ads-optimization-suggest | Gerar sugestões |
| ads-execute | 15 */4 * * * (4h, :15) | ads-optimization-execute | Executar aprovados + rules |
| ads-create | 45 */4 * * * (4h, :45) | google/meta-create | Processar requests approved |

**Nota:** O cron sync-ads existente (hourly) já faz upsert na tabela campaigns. Os novos crons complementam com snapshots granulares e lógica de management.

---

## Integração Telegram

O Spark não fala direto com Pedro. Fluxo:
1. Spark gera alerta/sugestão → grava no Supabase
2. Cron de monitoramento do Kobe verifica alerts critical → envia via Telegram Hub
3. Alertas warning → acumula no briefing diário do Kobe
4. Relatório diário de ADS → Kobe formata e envia no tópico Marketplaces

---

## Ordem de implementação

1. Skill 3 (monitoring) — é a base, precisa funcionar primeiro
2. Skill 4 (suggest) — depende do monitoring
3. Skill 1 + 2 (create) — pode ser paralelo ao monitoring
4. Skill 5 (execute) — última, depende de tudo anterior
5. Crons — configurar conforme cada skill fica pronta

---

## Estimativa

- Skills 1-2 (criação): 1 dia cada de capacitação iterativa
- Skill 3 (monitoring): 1 dia
- Skill 4 (suggest): 0.5 dia
- Skill 5 (execute): 0.5 dia
- Crons + integração: 0.5 dia
- **Total: ~4 dias úteis** (pode ser menos se fluir bem)

---

## Critérios de sucesso

- [ ] Campanhas criadas via webapp aparecem nas APIs do Google/Meta
- [ ] Métricas em metric_snapshots atualizando automaticamente
- [ ] Alertas sendo gerados quando performance viola metas
- [ ] Sugestões de otimização com dados reais e justificativas claras
- [ ] Regras automáticas executando com cooldown correto
- [ ] execution_log registrando toda ação
- [ ] Kobe recebendo alertas critical via Telegram

# Spark Ads Management System — Plano Completo

_De: Kobe | Data: 2026-03-24 | Status: Aguardando aprovação Pedro_

---

## Visão Geral

Evoluir o Spark Ads de dashboard de visualização para um Ads Management System completo — criação, gestão, monitoramento e otimização de campanhas Google Ads + Meta Ads.

**Arquitetura:** Webapp (interface) ↔ Supabase (ponte/banco) ↔ Agente Spark (cérebro)

---

## Fase 1 — Fundação (Builder)

**Escopo:** Schema Supabase (6 tabelas novas) + Evolução do webapp (3 novas páginas + melhorias)

**Pré-requisitos:** Nenhum blocker externo
**Estimativa Builder:** 120-150 min
**Dependência:** Aguardar Budamix Central terminar

### Entregáveis:
1. Migration SQL com 6 tabelas novas + alterações nas existentes
2. Página "Nova Campanha" — formulário completo multi-step
3. Página "Aprovações" — fila de pending_review + optimizations pendentes
4. Página "Detalhes de Campanha" — métricas em tempo real + metas + alertas + histórico
5. Página "Regras Automáticas" — CRUD de automation_rules
6. API routes para todas as operações
7. Sistema de notificações/alertas no webapp (badge + lista)
8. Componentes de status workflow (draft → live)

### Schema novo detalhado:
- `campaign_requests` — fila de criação (com meta_goals, spark_plan, missing_info, budget_spent_total)
- `metric_snapshots` — histórico granular de métricas (retenção 30d granular → daily)
- `alerts` — alertas com type, severity, priority, acknowledged
- `optimizations` — sugestões com justification, expected_impact, execution_result
- `automation_rules` — regras com condition, action, cooldown_hours, enabled
- `execution_log` — toda chamada de API logada (request/response/status)

---

## Fase 2 — Agente Spark (Kobe capacita)

**Escopo:** 5 skills novas + crons de monitoramento + integração Telegram

**Pré-requisitos:** Fase 1 concluída + Google Ads Developer Token Standard (✅ confirmado)
**Estimativa:** 2-3 dias de capacitação iterativa

### Skills a criar:
1. `google-ads-campaign-create` — criação Search/Shopping via API v23
2. `meta-ads-campaign-create` — criação Conversão via Marketing API v21
3. `ads-monitoring` — comparação performance vs metas, geração de alertas
4. `ads-optimization-suggest` — análise e geração de sugestões
5. `ads-optimization-execute` — execução de otimizações aprovadas via API

### Crons:
- A cada 1h: métricas básicas (spend, clicks, impressions) → metric_snapshots
- A cada 4h: métricas completas (CPA, ROAS, CTR, CPC, CPM, frequência, reach)
- A cada 24h (03:00 SP): snapshot completo + consolidação de dados > 30d
- A cada 4h: verificação de campaign_requests approved → executar criação
- A cada 4h: verificação de optimizations approved → executar
- A cada 2h: motor de automation_rules → executar regras ativas

### Integração Telegram:
- Alertas critical → notificação imediata via Kobe no Hub
- Alertas warning → acumula no briefing diário
- Relatório diário automático → tópico Spark/ADS no Hub

---

## Fase 3 — Automação (após 1-2 semanas de dados reais)

**Escopo:** Motor de regras automáticas + relatórios automáticos
**Pré-requisitos:** Fase 2 funcional com dados reais

### Entregáveis:
- Motor de automation_rules executando bypass de aprovação
- Relatórios diários automáticos (HTML) → Telegram + email
- Relatórios semanais consolidados
- Política de retenção metric_snapshots (> 30d → consolida em daily)
- Dashboard de automation_rules com histórico de execuções

---

## Dependências

```
Budamix Central (em build) ──→ Fase 1 Builder ──→ Fase 2 Spark ──→ Fase 3 Automação
                                    │                    │
                                    │                    └── Google Dev Token ✅
                                    └── Sem blocker externo
```

## Riscos Mapeados

| Risco | Mitigação |
|-------|-----------|
| Rate limits Google Ads API | Frequências conservadoras (1h/4h/24h) |
| Crescimento metric_snapshots | Retenção 30d granular → daily consolidado |
| Meta Ads token expira ~2026-05-18 | Cron de renovação já agendado |
| Criação de campanha com dados incompletos | Campo missing_info + validação no webapp |
| Otimização automática incorreta | Toda execução logada + cooldown_hours |

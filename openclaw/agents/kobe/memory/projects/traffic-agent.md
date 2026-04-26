---
title: "traffic-agent"
created: 2026-04-26
type: memory-project
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - project
---
# Projeto: Agente de Gestão de Tráfego Pago

## Status: 📋 Planejamento (rascunho recebido 2026-03-19)

## O que é
Agente autônomo de gestão de tráfego pago da GB. Opera como gestor sênior de mídia paga com domínio total sobre Meta Ads + Google Ads. Planeja, executa, monitora, otimiza e reporta todas as campanhas.

## Plataformas
- **Meta Ads** — ✅ API integrada, skill criada
- **Google Ads** — ✅ API integrada (2026-03-23). REST API v23. Credenciais no 1Password "Google Ads API - Spark"

## 7 Módulos Planejados

### 1. Dashboard e Monitoramento
- Painel consolidado Meta vs Google lado a lado
- KPIs: investimento, impressões, cliques, CTR, CPC, CPM, conversões, CPA, ROAS, receita
- Filtros por período (hoje, 7d, 30d, mês, custom)
- Variação % vs período anterior com tendência
- Indicador de saúde geral vs metas

### 2. Gestão de Campanhas
- Listagem filtrada por plataforma, status, objetivo, orçamento, período
- Detalhamento: objetivo, budget, datas, público, posicionamentos, lance
- Ações: pausar, ativar, duplicar, arquivar, ajustar budget
- Visão hierárquica: Campaign → Ad Set/Group → Ad
- Comparativo entre campanhas
- Diagnóstico automático quando não performa (público, criativo, lance, budget, saturação)

### 3. Gestão de Criativos
- Preview visual + copy + CTA + URL + status aprovação
- Métricas por anúncio (impressões, alcance, cliques, CTR, CPC, conversões, CPA, frequência, relevância/Quality Score)
- Detecção de fadiga criativa (frequência ↑ + CTR ↓)
- Recomendação de substituição

### 4. Analytics Avançado
- Segmentação: plataforma, campanha, conjunto/grupo, anúncio, período, device, geo, idade, gênero, posicionamento
- Funil: impressões → cliques → pageviews → add to cart → checkout → compra/lead
- Atribuição com janelas configuráveis (1d click, 7d click, 1d view)
- Frequência e saturação de público
- Custo por etapa do funil

### 5. Insights e Alertas Proativos
- CPA acima da meta
- Budget prestes a esgotar
- CTR caiu / CPC subiu anomalamente
- Fadiga criativa (frequência alta + queda engajamento)
- Oportunidade de realocar verba entre plataformas
- Formato: O QUE está acontecendo → POR QUE → O QUE FAZER
- Projeção de gastos/resultados baseada no ritmo atual

### 6. Relatórios e Exportação
- Relatórios customizáveis (métricas, período, agrupamento, detalhe)
- Templates: resumo executivo, performance, criativos, Meta vs Google
- Exportação: PDF (com gráficos), Excel/CSV, email automático
- White-label com logo/cores GB
- Agendamento recorrente (diário, semanal, mensal)
- Sumário executivo com destaques + problemas + próximos passos

### 7. Gestão de Orçamento
- Visão consolidada Meta + Google
- Alertas em marcos (50%, 75%, 90%, 100%)
- Projeção de gasto até fim do mês
- Histórico comparativo mensal/trimestral
- Recomendações de redistribuição por performance

## Metas da GB
- Ticket médio: R$100-300
- Margem bruta: ~70%
- CPA alvo aprendizado: até 50% do lucro bruto
- CPA alvo otimização: até 35% do lucro bruto
- CPA alvo escala: até 25% do lucro bruto
- ROAS mínimo: 10x

## Padrões de Comportamento
- Proativo — não espera pergunta
- Específico — dados concretos, não genéricos
- Mentalidade de dono — cada real conta
- Ação > informação — sempre termina com recomendação
- PT-BR com termos técnicos naturais

## Contas Google Ads
- **Manager Account:** 965-668-6533 (TrafficAI)
- **Customer Account:** 762-580-1774 (GB Distribuição)
  - Currency: BRL
  - Timezone: America/Sao_Paulo
  - Status: ENABLED
- **API Version:** v23 (v19 sunset fev/2026)
- **Campanhas encontradas:** 1 (Search, PAUSED — campanha de jul/2024)
- **1Password:** "Google Ads API - Spark" (dev token, client id/secret, refresh token, account IDs)

## Plano de Execução
### Fase 1 — Google Ads Integration ✅ (2026-03-23)
- [x] Configurar Google Ads API
- [x] Credenciais OAuth no 1Password
- [x] Refresh token gerado
- [x] API testada e funcionando (v23)
- [ ] Criar/atualizar skill google-ads com v23

### Fase 2 — Agente Unificado
- [ ] Skill/agente consolidando Meta + Google
- [ ] Definir formato: webapp vs relatórios vs ambos
- [ ] Monitoramento via cron

### Fase 3 — Inteligência
- [ ] Regras automatizadas cross-platform
- [ ] Detecção fadiga criativa
- [ ] Alertas proativos
- [ ] Projeções e recomendações

## Decisões Pendentes
- [ ] Dashboard como webapp ou relatórios pelo Telegram (ou ambos)?
- [ ] Valores exatos de CPA alvo por fase (Pedro precisa definir R$X)
- [ ] Google Ads: Pedro tem conta ativa? Precisa configurar?

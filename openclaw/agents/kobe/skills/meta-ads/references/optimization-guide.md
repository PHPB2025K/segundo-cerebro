---
title: "optimization-guide"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/meta-ads
---
# Otimização e Bidding — Meta Ads
**Referência:** 2025/2026

---

## Estratégias de Lance

| Estratégia | API Value | Como funciona | Quando usar |
|---|---|---|---|
| **Lowest Cost** | `LOWEST_COST_WITHOUT_CAP` | Meta compra ao menor custo possível | Padrão — fase inicial, learning |
| **Cost Cap** | `COST_CAP` | Tenta manter CPA médio abaixo do valor | CPA-alvo definido + histórico |
| **Bid Cap** | `LOWEST_COST_WITH_BID_CAP` | Limita bid máximo por leilão | Controle fino de leilão (avançado) |
| **Minimum ROAS** | `MINIMUM_ROAS` | Só gasta se atingir ROAS mínimo | Escala conservadora com meta ROAS |

### Parâmetros na API

```bash
# Lowest Cost (padrão — começar aqui sempre)
bid_strategy=LOWEST_COST_WITHOUT_CAP

# Cost Cap — target de R$80 por compra
bid_strategy=COST_CAP
bid_amount=8000  # em centavos

# Minimum ROAS — pelo menos 3x
bid_strategy=MINIMUM_ROAS
roas_average_floor=3.0
```

### Quando migrar do Lowest Cost para outra estratégia
- **Lowest Cost** → até estabilizar e ter benchmarks claros
- **Cost Cap** → quando ROAS está ok mas CPA é inconsistente e você tem um CPA-alvo
- **Minimum ROAS** → escala conservadora com margem definida
- **Bid Cap** → raramente necessário; para operações com controle de leilão muito fino

> **Regra prática:** A maioria das contas de e-commerce funciona bem com Lowest Cost + monitoramento por regras automáticas. Não complicar sem necessidade.

---

## Eventos de Otimização

O evento define **o que o algoritmo do Meta tenta maximizar** no Ad Set.

| Evento | `optimization_goal` | Quando usar |
|---|---|---|
| Purchase | `OFFSITE_CONVERSIONS` | Principal para Sales com >50 compras/mês |
| Add to Cart | `OFFSITE_CONVERSIONS` | Sales com baixo volume de compras |
| Landing Page Views | `LANDING_PAGE_VIEWS` | Traffic qualificado |
| Link Clicks | `LINK_CLICKS` | Traffic básico |
| Impressões | `IMPRESSIONS` | Awareness puro |
| Reach | `REACH` | Cobertura máxima |
| Video ThruPlays | `THRUPLAY` | Vídeos de branding |

### Regra do volume mínimo
**Meta precisa de 50 eventos por Ad Set por semana** para otimizar bem.

```
Compras por semana < 50 → Otimizar por Add to Cart
Add to Cart < 50/semana → Otimizar por Landing Page Views
LPV < 50/semana → Otimizar por Link Clicks
```

**Para a GB (estimativa):**
- Se fazendo R$5k/mês em Meta Ads com ticket médio R$100 → ~50 compras/mês ≈ ~12/semana
- Nesse caso: otimizar por Add to Cart é mais seguro que Purchase

---

## Learning Phase — Guia Completo

### O que é
Período em que o algoritmo coleta dados para otimizar. Performance instável, CPA pode ser 2–3x mais alto.

### Duração típica
- **Objetivo:** 50 eventos de otimização por Ad Set em 7 dias
- **Tempo médio:** 7–14 dias
- **Contas novas/budget baixo:** Pode levar 21–30 dias ou ficar em "Learning Limited"

### Como identificar no Ads Manager
- Status do Ad Set mostra "Em aprendizado" (Learning)

### Via API
```bash
curl -s "https://graph.facebook.com/v21.0/{ADSET_ID}?\
fields=name,status,learning_stage_info&access_token=$TOKEN"

# Retorna:
# "learning_stage_info": {
#   "status": "LEARNING",         <- em aprendizado
#   "attribution_windows": [...],
#   "conversions": 12,            <- eventos coletados até agora
#   "last_sig_edit_ts": 1234567   <- último reset
# }
#
# Status possíveis: LEARNING | LEARNING_LIMITED | NOT_DELIVERING | DATA_UNAVAILABLE
```

### O que RESETA a Learning Phase (evitar)
- ❌ Pausar e reativar o Ad Set
- ❌ Mudar orçamento em >20%
- ❌ Mudar o targeting (qualquer campo)
- ❌ Mudar o criativo (adicionar ou remover)
- ❌ Mudar o evento de otimização
- ❌ Mudar bid strategy
- ❌ Mudar o placements
- ❌ Adicionar/remover Custom Audiences

### O que NÃO reseta
- ✅ Pausar/reativar Ads individuais (não o Ad Set)
- ✅ Editar a copy do anúncio em alguns casos (verificar)
- ✅ Aumentar budget até 20%

### Protocolos durante Learning Phase
1. **Não mexer em nada por 7 dias mínimo**
2. Monitorar: gasto deve ser consistente
3. Se depois de 14 dias ainda em Learning Limited → ação necessária

### Resolver Learning Limited
| Causa | Solução |
|---|---|
| Budget muito baixo | Aumentar para 2x o custo do evento-alvo |
| Targeting muito restrito | Ampliar público ou usar Advantage+ |
| Evento difícil de alcançar | Mudar para evento mais alto no funil |
| Conta muito nova | Paciência + aumentar budget gradualmente |

---

## CBO vs ABO

### CBO — Campaign Budget Optimization

Budget definido na **Campanha**. Meta distribui entre Ad Sets.

```bash
# Campanha CBO
curl -X POST "https://graph.facebook.com/v21.0/$AC/campaigns" \
  -d "name=BUDAMIX_CBO_Mar2026" \
  -d "objective=OUTCOME_SALES" \
  -d "daily_budget=30000" \
  -d "bid_strategy=LOWEST_COST_WITHOUT_CAP" \
  -d "access_token=$TOKEN"

# Ad Sets não têm budget (herdam da campanha)
```

**Quando usar CBO:**
✅ Conta com histórico de dados
✅ Ad Sets similares (mesma estrutura, targeting diferente)
✅ Escala: quer que Meta decida onde gastar
✅ Mínimo de 3–5 Ad Sets para a distribuição fazer sentido

**Limitações CBO:**
- Pode concentrar 80%+ do budget em 1–2 Ad Sets
- Harder para testar variações com dados comparáveis

### ABO — Ad Set Budget Optimization

Budget definido em cada **Ad Set**. Controle manual.

```bash
# Campanha SEM budget
curl -X POST "https://graph.facebook.com/v21.0/$AC/campaigns" \
  -d "name=BUDAMIX_TEST_ABO_Mar2026" \
  -d "objective=OUTCOME_SALES" \
  -d "access_token=$TOKEN"
# (sem daily_budget)

# Ad Set COM budget próprio
curl -X POST "https://graph.facebook.com/v21.0/$AC/adsets" \
  -d "campaign_id={CAMPAIGN_ID}" \
  -d "daily_budget=5000" \
  -d "..." -d "access_token=$TOKEN"
```

**Quando usar ABO:**
✅ Testes: saber exatamente quanto gastou em cada variação
✅ Públicos muito diferentes que precisam de controle separado
✅ Garantir que todos os Ad Sets recebam dados para decisão

### Estratégia prática (como combinar)

```
Fase 1 — TESTE (ABO)
  → 3–5 Ad Sets com budget igual (R$50–100/dia cada)
  → Rodar 7–14 dias sem mexer
  → Identificar os vencedores

Fase 2 — ESCALA (CBO)
  → Pegar Ad Sets vencedores
  → Migrar para CBO com budget maior
  → Deixar Meta otimizar a distribuição
  → Continuar testando novas variações em ABO separado
```

---

## Escala de Campanhas

### Vertical Scaling (mais budget, mesma campanha)

**Regra de ouro:** Máximo 20% de aumento por vez.
```
R$100/dia → R$120/dia → R$145/dia → R$175/dia...
Aguardar 3–5 dias entre cada incremento
```

**Por que 20%?** Aumentos maiores resetam a Learning Phase. O algoritmo precisa recalibrar.

### Horizontal Scaling (mais Ad Sets/campanhas)

- Criar novos Ad Sets com variações de targeting
- Lançar 2–3 novos Lookalikes por semana
- Testar novos criativos em Ad Sets separados
- Expandir para novos países/regiões se fizer sentido

### Sinais para escalar
✅ ROAS > 3.5x por 3+ dias consecutivos
✅ CPA estável e abaixo do target
✅ Frequência < 2.5 (audiência não saturada)
✅ Ad Set fora do Learning Phase

### Sinais para não mexer
❌ Ad Set em Learning Phase (aguardar)
❌ Performance instável (dia bom/dia ruim — aguardar)
❌ Frequência > 4 (resolver fadiga primeiro)

---

## Frequência — Gestão e Benchmarks

| Objetivo | Frequência Ideal | Alerta | Ação |
|---|---|---|---|
| Awareness | 2–3x/semana | >5 em 7d | Ampliar público |
| Sales (prospecção) | 1.5–2.5 | >3.0 | Renovar criativo / ampliar |
| Retargeting | 3–5 | >7 | Saturação: reduzir janela |

### Como resolver frequência alta
1. **Ampliar audiência:** Broader targeting, Lookalike maior (3% vs 1%)
2. **Renovar criativos:** Novos visuais + copy = "novo" para o algoritmo
3. **Excluir audiências:** Remover quem já converteu
4. **Aumentar budget:** Mais alcance por dia = menor frequência
5. **Pausar e aguardar:** 7–14 dias de pausa "reseta" a exposição percebida

---

## Regras de Decisão — Quando Pausar vs. Ajustar

### Pausar imediatamente
- CPA > 3x o target E gasto > R$200
- CTR < 0.3% E impressões > 2.000
- ROAS < 0.8x E gasto > R$100
- Frequência > 8 em retargeting

### Ajustar (não pausar)
- CTR caindo gradualmente → renovar criativo
- ROAS abaixo do target mas acima de breakeven → testar nova variação
- Frequência 3–5 em prospecção → ampliar audiência
- CPM subindo → normal no Q4/datas; aguardar ou testar novo placement

### Aguardar (não fazer nada)
- Qualquer métrica nos primeiros 7 dias (Learning Phase)
- Variações normais de dia a dia (+/-30%)
- Segunda-feira após fim de semana (geralmente baixa)

### Dar dados suficientes antes de julgar
- Para Purchase: mínimo R$150–300 de gasto (2–3x o CPP esperado)
- Para Add to Cart: mínimo 500–1000 impressões + R$50
- Para Traffic: mínimo 1000 impressões + 2–3 dias

---

## Janelas de Atribuição

| Window | Código | Significado |
|---|---|---|
| 1-day click | `1d_click` | Compra em até 24h após clicar |
| 7-day click | `7d_click` | Compra em até 7 dias após clicar |
| 1-day view | `1d_view` | Compra em até 24h após VER |
| **7d click + 1d view** | `7d_click_1d_view` | **Padrão Meta — usar** |

### Especificar na Insights API
```bash
curl "https://graph.facebook.com/v21.0/{ID}/insights?\
fields=spend,actions,purchase_roas\
&attribution_setting=7d_click_1d_view\
&access_token=$TOKEN"
```

> Para análise conservadora (eliminar view-through que pode ser orgânico): `1d_click`

---

## ROAS Benchmarks e Cálculos

### Benchmarks por tipo de campanha (BR 2025)
| Tipo | ROAS Esperado |
|---|---|
| Retargeting | 4–8x |
| Advantage+ Shopping | 3–5x |
| LAL 1% | 2.5–4x |
| Broad / Prospecção | 1.5–3x |
| Awareness | N/A |
| Mediana Meta BR | 2.19x |

### Calcular ROAS de Breakeven
```
ROAS Breakeven = 1 / Margem Bruta (%)
Margem 40% → ROAS mínimo = 1/0.40 = 2.5x
Margem 30% → ROAS mínimo = 1/0.30 = 3.33x
```

**Para a GB Importadora:**
- Verificar margem bruta dos potes herméticos (importação China)
- Estimar: margem bruta ~35–45%? → ROAS breakeven ~2.2–2.9x
- Meta conservador: ROAS > 3x para escala sustentável

### Calcular CPP máximo aceitável
```
CPP máximo = Ticket Médio × Margem Bruta
Ticket R$100 × Margem 40% = CPP máximo R$40
```

---

## Checklist de Otimização Semanal

**Toda semana:**
- [ ] Verificar ROAS global e por campanha (7d e 28d)
- [ ] Checar Ad Sets em Learning Phase
- [ ] Verificar frequência de todos os Ad Sets ativos (> 3.0 = agir)
- [ ] Identificar Ad Sets com CPA > 2x o target
- [ ] Ver quais criativos têm CTR caindo
- [ ] Verificar se regras automáticas estão disparando corretamente
- [ ] Checar CPM: subiu muito? (Indica maior competição ou audiência saturada)
- [ ] Comparar performance mobile vs. desktop

**Todo mês:**
- [ ] Revisar estratégia de targeting — Broad ou Interesses?
- [ ] Renovar criativos fatigados
- [ ] Atualizar Custom Audiences (compradores do mês)
- [ ] Comparar ROAS Meta vs. vendas reais (atribuição)
- [ ] Ajustar budget baseado no histórico do mês anterior

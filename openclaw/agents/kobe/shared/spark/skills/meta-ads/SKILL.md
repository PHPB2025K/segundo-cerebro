---
title: "SKILL"
created: 2026-04-14
modified: 2026-06-08
type: skill-definition
agent: spark
status: active
tags:
  - agent/spark
---

# Skill: Meta Ads — [[openclaw/agents/spark/IDENTITY|Spark]] v3.0

_Análise, diagnóstico, otimização e relatórios de Meta Ads (Facebook + Instagram)._
_Versão 3.0 (08/06/2026) — refactor pra Strategy 2026 Budamix._

---

## Quando usar
- Analisar performance de campanhas Meta Ads **Budamix** (conta primária 08/06)
- Diagnosticar queda de performance (CPA subindo, CTR caindo, frequência alta)
- Recomendar otimizações (pausar, escalar, trocar criativo, ajustar público)
- Gerar relatórios (diário/semanal/mensal)
- Avaliar criativos e detectar fadiga
- Projetar gastos e resultados
- Estruturar novas campanhas e públicos dentro da Strategy 2026
- Analisar breakdowns (idade, gênero, posicionamento, device, região)

## Contas e IDs (atualizado 2026-06-08)

| Item | Valor | Notas |
|---|---|---|
| **Conta primária** | Budamix `act_1140258596603533` | 🟢 ATIVA — Strategy 2026 em curso |
| Conta legacy | GB Distribuição `act_323534883953033` | 🔴 PARADA (06/2026) — não operar |
| Business Manager | `836285430695962` | Budamix BM |
| App | KOBE.OPENCLAW `1486886096369858` | Live mode desde 08/06 |
| Page | `106066888942641` (Budamix) | |
| Instagram | `17841466202361418` (budamix.br) | 2.934 seguidores |
| Catálogo | `1973158136897277` | 23 produtos via feed XML |
| Pixel + CAPI | `460889899401645` | Operacional |
| API Version | `v25.0` | atualizado de v21 em 08/06 |
| Token | 1P "OpenClaw" → "Meta System User Token - Budamix Ads" (id `hxvgwjrdluw4yblo4lbktatoyy`), campo notesPlain com cleanup | SYSTEM_USER permanente — não expira |

---

## ⚠️ Regras invioláveis Budamix (NUNCA violar)

| Regra | Por que |
|---|---|
| **NÃO usar "borossilicato" em copy/anúncios** | O vidro não é borossilicato — claim falso |
| **NÃO usar claim "freezer/micro-ondas"** | Depende de borossilicato pra ser seguro |
| **NÃO tocar Campanha 1 entre 08/06 e ~22/06** | Fase de aprendizado em curso — mudança >20% reseta |
| **Paleta oficial Budamix** em criativos novos | Deep Teal #0a5b5b, Teal #096969, Burnt Terracotta #C1553D, Lima Sutil #B8D043, Ivory Mist #FAF7F2, Linen #E8DFD4 |
| **Antonio Bold** como fonte padrão | Identidade visual |
| **Texto crítico em criativos dentro da safezone 1:1** (y entre 420 e 1500 em 1080×1920) | Cortes do Feed Instagram |
| **NÃO mexer no targeting fixo** (mulheres + Advantage+ ON + Norte excluído) | Decisão técnica fixada — Norte excluído por frete proibitivo |

Detalhes em `~/segundo-cerebro/projects/budamix-meta-ads.md`.

---

## Scripts disponíveis (via Kobe — Spark NÃO executa diretamente)

O Spark é **L1 Observer** — solicita ao Kobe que execute:

| Script | O que faz | Como solicitar |
|---|---|---|
| `skills/marketing/meta-ads/scripts/meta-ads-report.py` | Relatório performance (7/30/90 dias) | "Kobe, preciso pull Meta Budamix últimos [X] dias, nível [campaign/adset/ad]" |
| `skills/marketing/meta-ads/scripts/meta-ads-create.py` | Criar campanha completa | "Kobe, recomendo criar campanha [specs]. Aprovas?" |
| `skills/marketing/meta-ads/scripts/meta-ads-rules.py` | Regras automatizadas | "Kobe, recomendo ativar regra [specs]. Aprovas?" |

**⚠️ Guardrail nos scripts:** desde 08/06 refusam executar sem `META_AD_ACCOUNT=act_1140258596603533`. Kobe sempre passa explícito.

**Quando solicitar dados, especificar:**
- Período (7d, 14d, 30d, custom)
- Nível (campaign, adset, ad)
- Breakdowns necessários (age, gender, placement, device, region)
- Métricas específicas além do padrão (se aplicável)

---

## Strategy 2026 ativa Budamix

3 campanhas focadas no HERO IMB501 (Conjunto 5 Potes Redondos de Vidro):

```
CAMPANHA 1 — ASC (Advantage+ Sales) — R$20/dia CBO — 🟢 ATIVA desde 08/06
  → Cold acquisition, mulheres BR (Norte excluído)
  → Otimização: AddToCart
  → Creative v4 (vídeo v2 safezone + copy multiuso)

CAMPANHA 2 — Teste Criativos (ABO 3:2:2) — R$11/dia — 🟡 PAUSED
  → Aguardando vídeos 2 e 3 do Pedro

CAMPANHA 3 — Retargeting WCA (ABO) — R$9/dia — 🟡 PAUSED
  → Aguardando WCAs (ViewContent 14d + Purchase 30d)
```

**Estrutura ANTIGA (4 campanhas R$900/mês com LAL + Interesses + Broad + Retargeting):** **DESCONTINUADA.** Não recomendar mais — playbook 2026 (Advantage+ Audience + Andromeda + interesses consolidados) tornou ineficaz.

---

## Framework de Análise

### Análise de Campanha (quando Kobe pede diagnóstico)

1. **Puxar dados** — solicitar ao Kobe report do período relevante
2. **Métricas obrigatórias por nível:**

| Nível | Métricas |
|---|---|
| Campaign | spend, impressions, clicks, CTR, CPC, CPM, conversions, CPA, ROAS, frequency, reach, hook_rate, hold_rate |
| Ad Set | tudo acima + cost_per_unique_click, unique_CTR, audience_size, delivery_status |
| Ad | tudo acima + quality_ranking, engagement_rate_ranking, conversion_rate_ranking |

3. **Aplicar framework:** Estado Atual → Meta → Gap → Ação → Impacto
4. **Classificar status:** 🟢 🟡 🔴 ⚪ por métrica
5. **Consultar `decisions.md` e `lessons.md`** antes de recomendar
6. **Logar recomendação:** insert em `meta.recommendations` no Supabase Spark
7. **Contextualizar:** comparar com período anterior + sazonalidade

### Análise de Breakdowns (quando performance não é óbvia)

| Breakdown | O que revela | Quando solicitar |
|---|---|---|
| **age + gender** | Demografia convertendo melhor/pior | CPA variando entre ad sets com mesmo criativo |
| **placement** | Feed vs Stories vs Reels | CTR/CPA muito diferente do esperado |
| **device** | Mobile vs Desktop | Taxa conversão LP suspeita |
| **region** | Estados/cidades com melhor performance | Validar exclusão Norte funcionando |
| **hourly** | Horários de pico de conversão | Otimização de delivery schedule |

**Regra:** só solicitar breakdown quando necessário — consome cota de API.

---

## Estratégia de Públicos (Strategy 2026)

**Padrão atual:**
- **Advantage+ Audience ON** em todas as campanhas (Meta decide alcance via signals)
- Idade: 18-65 (Meta força age_max≥65 quando Advantage+ ativo)
- Gênero: mulheres (gender=[2]) — decisão Budamix
- Geo: BR `home` location_type, **Norte excluído** (AC/AP/AM/PA/RO/RR/TO — frete proibitivo)

**Para Camp 3 (Retargeting), quando ativar:**
| Audiência | Retention | Uso |
|---|---|---|
| ViewContent | 14d | Quem viu produto sem comprar |
| Purchase | 30d | Excluir de prospecção |

**DPA (Dynamic Product Ads):** **Mês 3+** quando pixel maturar (~30-50 vendas Purchase/mês). Hoje pixel é novo — DPA chuta.

**Lookalikes:** as 2 LALs antigas da GB Distribuição (`120220400359220456` 1% Visitantes, `120219003397950456` 3% Engajados) estão **INACTIVE (operation_status_code 433)** desde 2024 — não reutilizáveis.

---

## Consciência de Privacidade (iOS 14+ / ATT) — atualizado 2026

| Impacto | Como lidar |
|---|---|
| Janelas atribuição removidas (7d view, 28d view) em 12/01/2026 | Padrão atual: 7d click + 1d view. ROAS reportado caiu 15-40% sem mudança real. |
| Pixel sozinho perde 30-60% conversões | **CAPI obrigatório** — Budamix já tem operacional (event_id dedup) |
| Demografia menos confiável | Cruzar com dados marketplace + UTM no GA4 |

**Regra prática:** ROAS blended = gasto total ÷ receita total via Stripe/Shopify/marketplaces. NÃO confiar só no Meta-reported.

---

## Detecção de Fadiga Criativa

| Sinal | Threshold | Nível | Ação |
|---|---|---|---|
| Hook rate <25% por 3+ dias | Criativo fraco | 🔴 | Substituir antes do CTA cair |
| Frequência > 2.5 + CTR estável | Atenção | 🟡 | Preparar novos criativos |
| Frequência > 3.0 | Preparar refresh | 🟡 | Novos criativos prontos |
| Frequência > 3.4 (prospecção) | Trocar urgente | 🔴 | Subir novo criativo |
| Frequência > 4.0 | Pausar imediato | 🔴 | Pausar + subir substituto |

### Matriz de Performance Criativa

```
                    CTR Alto
                       │
         ⭐ WINNER     │    🧪 TESTER
         (escalar)     │    (bom hook, LP ruim?)
                       │
  ──────────────────────┼──────────────────────
                       │
         💀 CORTAR     │    🤔 REVISAR
         (não funciona)│    (converte mas não atrai)
                       │
                    CTR Baixo

       ROAS Baixo ─────┼───── ROAS Alto
```

**Formato briefing pra novo criativo:**
```
⚡ BRIEFING CRIATIVO — [produto Budamix]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Campanha: [nome]
📊 Motivo: [fadiga / CTR queda / teste A/B / novo lançamento]
🎯 Público: [mulheres BR Advantage+ — manter padrão Budamix]
📐 Formato: 1080×1920 vertical (9:16) — texto na safezone 1:1
📍 Posicionamento: Feed + Stories + Reels (Advantage+ Placements)
💡 Mensagem principal: [baseado em dados]
🎬 CTA: SHOP_NOW (padrão Budamix)
✅ Referência: [ad anterior que funcionou + métricas]
🚫 Evitar: borossilicato, claim freezer/micro-ondas, texto fora da safezone
📅 Deadline: [quando]
🎨 Visual: paleta oficial Budamix + Antonio Bold
```

---

## Relatórios

### Snapshot Diário (cron 10:20 BRT)
```
⚡ SPARK — META BUDAMIX | YYYY-MM-DD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 Spend hoje: R$X | Mês: R$Y / R$600 (X%)
📈 Projeção fim mês: R$X (🟢/🟡/🔴)

| Campanha | Status | Spend | CPA | ROAS | CTR | Freq | Sinal |
|---|---|---|---|---|---|---|---|
| Camp 1 ASC | 🟢 | R$X | R$X | Xx | X% | X.X | 🟢/🟡/🔴 |

📌 Alertas: [se houver — ou "Nenhum"]
🔄 Mudanças vs ontem: [o que mudou significativamente]
⏭️ Recomendação: [se aplicável — ou "Manter curso"]

⚠️ Lembrete: Camp 1 em fase aprendizado até ~22/06 — NÃO tocar.
```

### Report Semanal (segunda 09h, para Pedro via Kobe — duas versões)

**Técnica (Kobe):**
- Performance 7d por campanha/adset com cruzamento Pixel/CAPI
- Top 3 e Bottom 3 por ROAS e CPA
- Breakdowns relevantes (region, age, placement)
- Frequency/hook rate trends
- Budget gasto vs planejado vs projeção
- Recomendações com justificativa técnica + risk_level

**Negócio (Kobe repassa Pedro):**
- Quanto gastou, quanto rendeu, ROAS blended
- O que funcionou em linguagem simples
- O que precisa atenção
- Top 3 ações próxima semana com impacto esperado em R$

---

## Naming Convention (Strategy 2026)

```
Campaign:   YYYY-MM-DD_[FASE]_[TIPO]_[PRODUTO]_[FAIXA]
            ex: 2026-06-06_Cold_ASC_IMB501_25-55

AdSet:      [FASE]_[GEO]_[FAIXA]_[PRODUTO]_[EVENTO]
            ex: Cold_BR_25-55_IMB501_ATC

Ad:         [PRODUTO]_[FORMATO_DESCR]_[VERSAO]
            ex: IMB501 Hero v2 - Cold ASC - 15s 9:16
```

---

## KPIs de Referência (Budamix Strategy 2026)

| KPI | Saudável | Alerta |
|---|---|---|
| ROAS Mês 1 (exploração) | 1.0-1.3 | <1.0 |
| ROAS Mês 2 (transição Purchase) | 1.5-2.0 | <1.3 |
| ROAS Mês 3+ (escala) | 2.0-3.0+ | <2.0 |
| CTR link | ≥2% | <1% |
| CPM Feed BR | R$15-35 | >R$40 |
| CPM Reels BR | R$8-20 | >R$25 |
| Hook rate (3s/imp) | ≥30% | <25% |
| Hold rate (15s/3s) | ≥25% | <25% |
| Frequência prospecção | 1.5-2.5 | >3.4 |
| Frequência remarketing | 3.0-5.0 | >7 |

---

## Logs e auditoria (Supabase Spark — `wzhmrpskiscassbixurr`)

Toda recomendação e ação Meta Ads é logada em schema dedicado `meta`:

| Tabela | Uso |
|---|---|
| `meta.recommendations` | Diagnósticos + sugestões do Spark (status: open/accepted/rejected/expired) |
| `meta.actions_log` | Execuções pelo Kobe (old_value, new_value, risk_level, approval_status, status, raw_response) |
| `meta.daily_pulses` | Snapshot diário com métricas + anomalias detectadas |

⚠️ Schemas separados por plataforma (regra Pedro): NÃO usar tabela genérica multi-plataforma. Amazon vai pro schema `amazon`, ML pro `ml`, etc.

---

## Limitações (L1 Observer — não mudou)

- ❌ Spark NÃO executa scripts — solicita ao Kobe
- ❌ Spark NÃO modifica campanhas — recomenda ao Kobe
- ❌ Spark NÃO publica criativos — envia briefing ao Kobe
- ❌ Spark NÃO cria públicos — especifica e solicita ao Kobe
- ❌ Spark NUNCA fala direto com Pedro — sempre via Kobe
- ✅ Spark analisa, diagnostica, recomenda, reporta, loga em Supabase
- ✅ Spark cruza dados com `business.md` pra contextualizar

**Janela de promoção pra autonomia:** após 1-2 ciclos sem erro (>22/06), avaliar promover ajustes pequenos (pause, escala ≤+20%) pra auto-execução. Estruturais (criar/swap creative, mudar público, escalar >20%) **sempre** aprovação no tópico Marketing (Telegram thread 9).

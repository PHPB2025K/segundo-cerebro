---
name: meta-ads
description: >
  Skill de Meta Ads (Facebook/Instagram Ads) para operação profissional via Marketing API v25.0.
  Usar quando: criar campanha no Meta, subir anúncio no Facebook ou Instagram, gerar
  relatório de performance, verificar ROAS, escalar/pausar campanha, configurar targeting,
  criar Custom Audience/Lookalike, analisar CTR/CPM/CPC/CPA/ROAS, configurar Advantage+
  Shopping Campaign, ads para e-commerce, Budamix ads, Strategy 2026, campanha de sales
  no Meta, relatório de ads últimos 7/30/90 dias, automação de anúncios.
---

# Meta Ads — Skill de Operação Profissional

> Usado por [[openclaw/agents/spark/IDENTITY|Spark]] | Atualizado 2026-06-08

Skill de gestão e automação de Meta Ads via Marketing API **v25.0**.
Contexto principal: **Budamix** (utensílios domésticos vidro/cerâmica/porcelana).

---

## ⚠️ Contas e estado atual (2026-06-08)

| Conta | ID | Status | Notas |
|---|---|---|---|
| **Budamix** (PRIMÁRIA) | `act_1140258596603533` | 🟢 ATIVA | Strategy 2026, Camp 1 ASC R$20/dia rodando desde 08/06 |
| GB Distribuição (legacy) | `act_323534883953033` | 🔴 PARADA (06/2026) | NÃO operar — conta antiga inativa |
| Broglio Brinquedos | `act_599689043839914` | ⚪ Sem campanhas | Mapear quando reativar |
| Trades Up | `act_851375860374263` | ⚪ Sem campanhas | Mapear quando reativar |

⚠️ **Guardrail nos scripts:** desde 08/06/2026 os 3 scripts (`meta-ads-report.py`, `meta-ads-create.py`, `meta-ads-rules.py`) refusam execução sem `META_AD_ACCOUNT` explícito. Whitelist atual permite apenas Budamix.

---

## Coordenadas Budamix

| Item | Valor |
|---|---|
| **Ad Account** | `act_1140258596603533` |
| **Business Manager** | `836285430695962` |
| **App** | KOBE.OPENCLAW (`1486886096369858`) — em Live mode desde 08/06 |
| **Page** | Budamix (`106066888942641`) |
| **Instagram** | budamix.br (`17841466202361418`) — 2.934 seguidores |
| **Catálogo** | Budamix Catálogo (`1973158136897277`) — 23 produtos via feed XML |
| **Pixel + CAPI** | `460889899401645` |
| **Feed XML** | `https://budamix.com.br/feeds/meta-catalog.xml` |
| **API Version** | `v25.0` |
| **Base URL** | `https://graph.facebook.com/v25.0/` |

---

## Credenciais (1Password)

Token System User permanente (não expira). Salvo no 1P, **campo notesPlain com cleanup obrigatório**:

```bash
# Lê o token (sed remove aspas, tr remove newline — ambos vêm do encoding do op)
TOKEN=$(op item get hxvgwjrdluw4yblo4lbktatoyy --vault=OpenClaw \
  --fields notesPlain --reveal | sed 's/^"//; s/"$//' | tr -d '\n')

# Verificar validade
curl "https://graph.facebook.com/v25.0/me?access_token=$TOKEN"

# Item completo: vault "OpenClaw" → "Meta System User Token - Budamix Ads"
# Item ID: hxvgwjrdluw4yblo4lbktatoyy
```

Item 1P contém metadados (System User Fat_User_CRM, scopes, IDs) — ver memória interna do agente para detalhes.

**Token velho `Meta Ads API - KOBE.OPENCLAW`:** descontinuado em 08/06 (era long-lived 60 dias, do app antigo). Não usar.

---

## Strategy 2026 — Estrutura ativa Budamix

3 campanhas focadas no HERO IMB501 (Conjunto 5 Potes Redondos de Vidro):

```
CAMPANHA 1 — ASC (Advantage+ Sales) — R$20/dia CBO — 🟢 ATIVA desde 08/06
  → Cold acquisition
  → Mulheres BR (Norte excluído: AC/AP/AM/PA/RO/RR/TO) + Advantage+ Audience ON
  → Otimização: AddToCart inicialmente
  → Creative v4 ativo (vídeo v2 safezone + copy multiuso)

CAMPANHA 2 — Teste de Criativos (ABO 3:2:2) — R$11/dia — 🟡 PAUSED
  → Aguardando vídeos 2 e 3 do Pedro
  → Vencedores graduam pra ASC semanalmente

CAMPANHA 3 — Retargeting WCA (ABO) — R$9/dia — 🟡 PAUSED
  → Aguardando 2 WCAs criadas (ViewContent 14d + Purchase 30d)
  → Otimização: Purchase
```

**Decisões fixas:**
- Strategy D 2026 (3 campanhas) substitui playbook antigo de 4 campanhas (Retargeting + LAL + Interesses + Broad) — não recomendar mais a estrutura antiga
- Mulheres + Advantage+ Audience é o padrão. Idade fica 18-65 (Meta exige age_max≥65 com Advantage+ ON)
- Sem interesses detalhados manuais (Meta consolidou em jan/26, empilhamento Sobral-style não funciona mais)
- Retargeting começa WCA + vídeo. DPA só no mês 3+ quando pixel tiver maturidade (~30-50 vendas/mês)

---

## Regras invioláveis (Budamix)

| Regra | Por que |
|---|---|
| **NÃO usar "borossilicato" em copy/anúncios** | O vidro Budamix não é borossilicato — claim falso |
| **NÃO usar claim "freezer/micro-ondas"** | Depende de borossilicato pra ser seguro |
| **NÃO tocar Campanha 1 entre 08/06 e ~22/06** | Mudança >20% reseta fase de aprendizado |
| **Paleta oficial Budamix** em criativos novos | Deep Teal #0a5b5b, Teal #096969, Burnt Terracotta #C1553D, Lima Sutil #B8D043, Ivory Mist #FAF7F2, Linen #E8DFD4 |
| **Antonio Bold** como fonte padrão | Identidade visual Budamix |
| **NÃO mexer no targeting (idade/gender/Advantage+)** | Decisão técnica fixada — ver detalhes em `knowledge/concepts/meta-ads-paid-social-2026.md` |
| **Texto crítico em criativos dentro da safezone 1:1** (y entre 420 e 1500 em 1080×1920) | Cortes do Feed Instagram |

---

## Playbook 2026 — mudanças recentes da Meta (ler antes de recomendar)

- **15/01/2026 — Consolidação de interesses:** interesses específicos (EDM, comida vegana, modelos de carro) fundidos em grupos amplos. Empilhamento de interesses tipo "Sobral 2021" parou de entregar. Usar como SIGNAL via Advantage+ Audience, não filtro.
- **12/01/2026 — Janelas de atribuição:** removidas 7d view + 28d view. Padrão atual: 7d click + 1d view. ROAS reportado caiu 15-40% sem mudança real de performance.
- **Advantage+ Audience força age_max ≥ 65:** quando ON, Meta rejeita restringir idade abaixo de 65. Funciona só como SIGNAL.
- **Andromeda + GEM:** novo motor de delivery usa criativo pra encontrar público. 70-80% da performance vem do criativo, não orçamento ou targeting. Recompensa diversidade de criativos, não volume de variações da mesma ideia.
- **Pixel + CAPI obrigatório** em 2026 — pixel sozinho perde 30-60% das conversões.

Detalhes completos: `~/segundo-cerebro/knowledge/concepts/meta-ads-paid-social-2026.md`

---

## Scripts Disponíveis (com guardrail desde 08/06)

| Script | O que faz | Comando |
|---|---|---|
| `scripts/meta-ads-report.py` | Relatório performance (7/30/90 dias), salva JSON | `META_AD_ACCOUNT=act_1140258596603533 python3 scripts/meta-ads-report.py --days 7 --level campaign` |
| `scripts/meta-ads-create.py` | Criar campanha completa (campaign + adset + ad) | `META_AD_ACCOUNT=act_1140258596603533 python3 scripts/meta-ads-create.py --name "..." --budget 2000` |
| `scripts/meta-ads-rules.py` | Criar/listar/pausar regras automatizadas | `META_AD_ACCOUNT=act_1140258596603533 python3 scripts/meta-ads-rules.py --list` |

**Sem `META_AD_ACCOUNT`:** scripts refusam executar e mostram contas válidas. Vital pra não operar conta errada.

---

## Workflow Principal

### 1. Verificar performance atual
```bash
export META_AD_ACCOUNT=act_1140258596603533
python3 scripts/meta-ads-report.py --days 7 --level campaign
```

### 2. Análise + recomendação (Spark L1 — entrega ao Kobe, NÃO executa)
- Spark gera diagnóstico no formato Estado → Meta → Gap → Ação → Impacto
- Logs em `meta.recommendations` no Supabase Spark (`wzhmrpskiscassbixurr`)
- Kobe posta no tópico Marketing (Telegram thread 9) com etiqueta `[Spark — Meta Ads Daily]`
- Pedro aprova → Kobe executa via script

### 3. Mudanças em produção (sempre via Kobe após aprovação)
- Toda execução loga em `meta.actions_log` no Supabase Spark
- Backups de configuração antes de mudança (`old_value` no log)
- Rollback fácil via `swap_creative` ou restore de campaign state

---

## Quick Reference — Comandos diretos via curl (Budamix)

```bash
TOKEN=$(op item get hxvgwjrdluw4yblo4lbktatoyy --vault=OpenClaw --fields notesPlain --reveal | sed 's/^"//; s/"$//' | tr -d '\n')
AC="act_1140258596603533"

# Status da conta
curl -s "https://graph.facebook.com/v25.0/$AC?fields=name,currency,account_status,spend_cap&access_token=$TOKEN" | python3 -m json.tool

# Listar campanhas
curl -s "https://graph.facebook.com/v25.0/$AC/campaigns?fields=id,name,objective,status,daily_budget,bid_strategy&access_token=$TOKEN" | python3 -m json.tool

# Pausar/ativar campanha
curl -X POST "https://graph.facebook.com/v25.0/CAMPAIGN_ID" -d "status=PAUSED" -d "access_token=$TOKEN"

# Insights últimos 7d
curl -s "https://graph.facebook.com/v25.0/$AC/insights?fields=campaign_name,spend,impressions,clicks,ctr,cpm,cpc,purchase_roas,actions&level=campaign&date_preset=last_7d&access_token=$TOKEN" | python3 -m json.tool
```

---

## Naming Convention (Strategy 2026 Budamix)

```
Campaign:   YYYY-MM-DD_[FASE]_[TIPO]_[PRODUTO]_[FAIXA]
            ex: 2026-06-06_Cold_ASC_IMB501_25-55

AdSet:      [FASE]_[GEO]_[FAIXA]_[PRODUTO]_[EVENTO]
            ex: Cold_BR_25-55_IMB501_ATC

Ad:         [PRODUTO]_[FORMATO]_[VERSAO]_[OBJETIVO]
            ex: IMB501 Hero v2 - Cold ASC - 15s 9:16
```

---

## KPIs de Referência — E-commerce BR 2026

| KPI | Saudável | Alerta |
|---|---|---|
| **Hook rate** (3s ÷ impressões) | ≥30% | <25% (criativo fraco — substituir) |
| **Hold rate** (15s ÷ 3s) | ≥25% | <25% (mensagem fraca) |
| **CTR link** | ≥2% | <1% (problema sério) |
| **Frequência prospecção** | 1.5-2.5 / 7d | >3.4 (adicionar criativo) |
| **Frequência remarketing** | 3.0-5.0 | >7 (fadiga) |
| **CPM BR** | R$15-35 Feed / R$8-20 Reels | — |
| **ROAS breakeven** | 1 / margem bruta | — |

**ROAS por fase Budamix:**
- Mês 1 (exploração): 1.0-1.3
- Mês 2 (transição Purchase): 1.5-2.0
- Mês 3+ (escala): 2.0-3.0+

---

## Referências detalhadas

| Arquivo | Conteúdo |
|---|---|
| `references/api-reference.md` | Endpoints, parâmetros, exemplos curl (atualizar bump v25) |
| `references/campaign-guide.md` | Criação por objetivo, estrutura ODAX |
| `references/audience-targeting.md` | Custom Audiences, Lookalike, Advantage+ |
| `references/creative-specs.md` | Specs técnicas, formatos, copy framework |
| `references/optimization-guide.md` | Bidding, Learning Phase, escala, regras |
| `references/ecommerce-strategy.md` | Estratégia GB/Budamix/marketplace |
| `~/segundo-cerebro/knowledge/concepts/meta-ads-paid-social-2026.md` | Playbook 2026 (mudanças críticas Meta) |
| `~/segundo-cerebro/projects/budamix-meta-ads.md` | Estado operacional Budamix (IDs, criativos, decisões) |

---

## Instalação de Dependências

```bash
pip3 install facebook-business requests tabulate
```

---

## Alertas Importantes

⚠️ **NÃO tocar Camp 1 Budamix entre 08/06 e ~22/06** — fase de aprendizado em curso, mudança >20% reseta.

⚠️ **Learning Phase:** sem mexer por 7-14 dias após criar/modificar Ad Set. Qualquer mudança reseta.

⚠️ **Budget changes:** máximo 20% por vez. Acima reseta.

⚠️ **Meta Ads → Mercado Livre:** evitar (sem Pixel, sem ROAS mensurável). Funil próprio (Pixel + CAPI) é o caminho.

⚠️ **Criativos sem "borossilicato" e sem "freezer/micro-ondas":** regras invioláveis Budamix.

⚠️ **API v25.0:** versão atual da Marketing API. Checar sunset dates periodicamente.

---
## Referências
- [[skills/marketing/meta-ads/references/api-reference|API Reference]]
- [[skills/marketing/meta-ads/references/audience-targeting|Audience Targeting]]
- [[skills/marketing/meta-ads/references/campaign-guide|Campaign Guide]]
- [[skills/marketing/meta-ads/references/creative-specs|Creative Specs]]
- [[skills/marketing/meta-ads/references/ecommerce-strategy|E-commerce Strategy]]
- [[skills/marketing/meta-ads/references/optimization-guide|Optimization Guide]]

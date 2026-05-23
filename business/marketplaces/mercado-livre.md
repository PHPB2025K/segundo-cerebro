---
title: "Mercado Livre — Conta Budamix"
type: reference
domain: marketplace
created: 2026-05-22
updated: 2026-05-22
tags:
  - marketplace/mercado-livre
  - account/budamix
  - reputation/mercadolider-gold
---

# Mercado Livre — Conta Budamix

Contexto operacional canônico da conta ML. Atualizado quando algum atributo estrutural muda (medalha, nome, IDs, regras de exibição).

## Identidade da conta

| Campo | Valor |
|---|---|
| Nome comercial atual | **Budamix** |
| `nickname` na API ML (legado) | `GAMMAOFICIAL` |
| Seller ID | `532562281` |
| Advertiser ID (Mercado Ads) | `172453` |
| Site | MLB (Brasil) |
| Tipo | `brand` (conta oficial) |
| Cadastro | 2020-03-03 |
| Permalink | http://perfil.mercadolivre.com.br/GAMMAOFICIAL |
| Responsável operacional | Yasmin |
| Responsável ADS | Himmel (acionado SEMPRE via Yasmin) |

**Regra de exibição:** todo texto humano (Slack, briefings, relatórios) deve usar **"Budamix"**. `GAMMAOFICIAL` só aparece em logs técnicos ou auditoria.

## Status MercadoLíder (snapshot 22/05/2026)

- **Medalha atual:** **MercadoLíder Gold**
- **Termômetro:** `5_green` (verde escuro, no topo)
- **Período de proteção:** nenhum ativo (`real_level: null`, `protection_end_date: null`)

### Métricas oficiais ML (janela 60d, 23/mar a 22/mai/2026)

| Métrica | Atual | Limite/Threshold | Status |
|---|---|---|---|
| Vendas (60d) | 5.907 | — | — |
| Com Envios | 5.584 | — | — |
| Concluídas | 5.595 | ≥ 1.725 para Platinum | ✅ +3.870 |
| Faturado em concluídas | R$ 237.587 | ≥ R$ 296.000 para Platinum | ⚠️ falta R$ 58.413 |
| Reclamações | 0,25% (15 casos) | < 1% | ✅ +0,75 pp |
| Atrasos Mercado Envios | 0,10% (6 casos) | < 6% | ✅ +5,90 pp |
| Cancelamentos | 0,00% (0 casos) | < 2% | ✅ +2,00 pp |
| Vendas canceladas pelo vendedor | 0% | ≤ 0,5% | ✅ |

**Conclusão:** 7/8 requisitos para Platinum cumpridos. Falta apenas **sustentar faturamento** até a janela 60d atingir R$ 296.000 acumulados.

## Trajetória de promoção a Platinum

- **Janela de medição:** 60 dias corridos rolling (cada dia que passa entra o dia novo e sai o dia D−60).
- **Ritmo médio diário atual:** R$ 3.959,78/dia (R$ 237.587 ÷ 60).
- **Gap restante:** R$ 58.413.
- **ETA estimado mantendo ritmo:** ~14,8 dias úteis (estimativa grosseira, ignora o rolling — cálculo real precisa simular dia a dia descontando o que sai).
- **Bloqueador:** sustentação — qualquer dia abaixo do ritmo necessário atrasa a promoção; cada dia acima adianta.

## Vocabulário e regras de pipeline

### Termos oficiais (ordem crescente de nível)

1. **MercadoLíder** (Silver/Padrão) — 230 vendas, R$ 37.000 em 60d
2. **MercadoLíder Gold** — 575 vendas, R$ 118.400 em 60d ← **estamos aqui**
3. **MercadoLíder Platinum** — 1.725 vendas, R$ 296.000 em 60d

### Modalidades de envio praticadas

- **Full** — estoque no CD do ML, exposição garantida
- **Cross-Docking** — Coleta na expedição Budamix
- **Flex** — desligado por decisão operacional (não usar)
- **Drop-off** — não praticado

### Mapeamento API ML

| Conceito | Campo na API |
|---|---|
| Cor do termômetro | `seller_reputation.level_id` (ex: `5_green`) |
| Medalha | `seller_reputation.power_seller_status` (`null` / `silver` / `gold` / `platinum`) |
| Medalha real durante proteção | `seller_reputation.real_level` |
| Fim do período de proteção | `seller_reputation.protection_end_date` |
| Vendas 60d | `seller_reputation.metrics.sales.completed` |
| Vendas histórico | `seller_reputation.transactions.completed` (NÃO usar como 60d) |
| Taxa de reclamações 60d | `seller_reputation.metrics.claims.rate` |
| Taxa de atrasos 60d | `seller_reputation.metrics.delayed_handling_time.rate` |
| Taxa de cancelamentos 60d | `seller_reputation.metrics.cancellations.rate` |
| Faturamento 60d | **não retornado pela API** — calcular a partir dos pedidos no Supabase |

## Benefícios por nível (referência)

| Benefício | Silver | Gold | Platinum |
|---|---|---|---|
| Limite anúncios ativos | 20.000 | 50.000 | 50.000 |
| Boost em buscas | Baixo | Médio | Máximo (prioridade Buy Box) |
| Subsídio frete grátis (R$ 79+) | 50% sobre custo do envio | Maior (% não publicado) | Maior ainda (% não publicado) |
| Acesso a campanhas/blitz | Limitado | Médio | Prioritário (lançamentos e promoções de elite) |
| Acesso antecipado a features | Não | Não | Sim |
| Suporte | Padrão | Personalizado | Prioritário/diferenciado |

**Implicação prática:** perder Gold pra Silver muda limite de anúncios (50k → 20k) e reduz subsídio de frete; perder Platinum pra Gold mantém limites mas perde prioridade Buy Box e acesso antecipado.

## Decisão final de modelos LLM no pipeline DSA (23/05/2026)

Após benchmark quádruplo das 7 camadas no mesmo dia (22/05/2026, `weekly.md` populado): Sonnet 4.6 puro, Opus 4.7 puro, GPT 5.5 (via codex) e **híbrido (Sonnet default + Opus em L04/L05)**, decidido:

### Cron diário (todo dia 06:50 BRT) — **modo híbrido**

| Camada | Modelo | Por quê |
|---|---|---|
| L01 Estratégica | `claude-sonnet-4-6` | Análise panorâmica, latência baixa, custo modesto. |
| L02 Tática | `claude-sonnet-4-6` | Tradução estratégia→ação; baixa complexidade analítica. |
| L03 Operacional | `claude-sonnet-4-6` | Decomposição estrutural do dia; Sonnet performa muito bem. |
| **L04 Granular** | **`claude-opus-4-7`** | Rigor investigativo, cruzamento de fontes, declaração de divergências. Camada com 2º maior peso analítico. |
| **L05 Condensadora** | **`claude-opus-4-7`** | Julgamento de relevância, classificação `fato`/`hipótese`/`risco latente`, aplicação dos 6 padrões. Camada de maior peso analítico. |
| L06 Slack Writer | `claude-sonnet-4-6` | Tradução estruturada, baixa complexidade. |
| L07 QA Gate | `claude-sonnet-4-6` | Validação cruzada, 12 gates; não rediagnostica. |

**Validação empírica do híbrido (run 23/05 11:12 BRT):**
- APROVADO COM RESSALVA, **2 menores** (vs 5 do Sonnet puro, 3 do Opus puro)
- Insight estrutural novo que **só apareceu no híbrido**: "ADS share alto num dia liderado por Cross-Docking sugere campanha acompanha produto, não modalidade"
- Latência ~9-10 min (vs 6 min Sonnet puro, 13 min Opus puro)
- Custo ~R$ 0,50/run (vs R$ 0,40 Sonnet puro, R$ 0,70 Opus puro)

### Cron semanal (toda segunda 09:00 BRT) — **Opus 4.7 puro**

Script: `daily-sales-weekly-consolidator-ml.py`. Lê 7 blocos diários do `weekly.md` da semana anterior, chama Opus 4.7 com prompt `08-weekly-consolidator.md`, gera bloco `### Semana: DD/MM a DD/MM/AAAA` no Histórico Semanal.

### Cron mensal (dia 1 do mês 09:00 BRT) — **Opus 4.7 puro**

Script: `daily-sales-monthly-consolidator-ml.py`. Lê 4-5 blocos semanais do mês anterior, chama Opus 4.7 com prompt `09-monthly-consolidator.md`, gera bloco `### Mês: MM/AAAA` no `monthly.md`.

### Descartado: GPT 5.5

GPT 5.5 (via codex CLI, assinatura ChatGPT Pro 5x) foi descartado para o pipeline: análise mais rasa (1 insight só vs 3 dos modelos Claude), hedging excessivo, bug de formatação (vazou "text" no início do bloco Slack). Vantagem do custo zero não compensa perda de qualidade analítica.

### Como o override por camada funciona

Config em `/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/config/daily-sales-analyst.json`:

```json
{
  "llm_model": "claude-sonnet-4-6",
  "llm_timeout_seconds": 450,
  "llm_model_per_layer": {
    "04": "claude-opus-4-7",
    "05": "claude-opus-4-7"
  },
  "llm_timeout_seconds_per_layer": {
    "04": 900,
    "05": 900
  }
}
```

O runner (`daily-sales-runner-ml.py`) lê `llm_model_per_layer` e aplica override por camada via função `_resolve_model_for_layer`. Suporta tanto modelos Claude (via `claude -p`) quanto OpenAI/Codex (via `codex exec` com `--output-last-message`).

### Custos estimados consolidados

| Cron | Frequência/mês | Custo estimado/run | Custo/mês |
|---|---|---|---|
| Diário (híbrido) | 30 | R$ 0,50 | R$ 15,00 |
| Semanal (Opus puro) | 4 | R$ 0,80 | R$ 3,20 |
| Mensal (Opus puro) | 1 | R$ 1,20 | R$ 1,20 |
| **Total ML/mês** | | | **~R$ 19,40** |

## Pipeline DSA — onde isso entra (planejado, ainda não implementado)

- **Coletor (`ml-snapshot-fetcher.py`)** — capturar `power_seller_status`, `real_level`, `protection_end_date`, métricas 60d e persistir em `ml_account_snapshots` (migration pendente).
- **Cálculo de trajetória** — função no fetcher ou job paralelo que calcula diariamente: faturamento 60d (rolling), gap pro Platinum, ETA estimado.
- **L01 Estratégica** — nova lente "Medalha + Trajetória": estamos no ritmo de promoção? O dia ajudou ou atrapalhou?
- **L05 Condensadora** — mudança de medalha = fato; gap se aproximando do limite = risco latente.
- **L06 Slack Writer** — usar vocabulário correto ("MercadoLíder Gold" / "MercadoLíder Platinum"), nunca "verde-gold" colado.
- **L07 QA Gate** — bloquear termos inventados ("verde-gold"), validar grafia oficial.

## Fontes consultadas

- [Vendedores ML — Como ser MercadoLíder](https://vendedores.mercadolivre.com.br/nota/como-ser-um-mercadolider)
- [Developers ML — Reputação de vendedores](https://developers.mercadolivre.com.br/pt_br/reputacao-de-vendedores)
- [Developers ML — Seller reputation (EN)](https://developers.mercadolivre.com.br/en_us/sellers-reputation)
- [GoSmarter — Como ser MercadoLíder Platinum 2026](https://gosmarter.com.br/como-ser-mercadolider-platinum/)
- [Magis5 — MercadoLíder Platinum](https://magis5.com.br/mercadolider-platinum-o-que-e-e-como-se-tornar/)

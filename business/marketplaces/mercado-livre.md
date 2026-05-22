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

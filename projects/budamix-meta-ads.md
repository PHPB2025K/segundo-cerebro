---
title: "Budamix Meta Ads — Paid Social"
created: 2026-06-06
modified: 2026-06-06
type: project
status: active
path: "Meta Ads Manager — conta Budamix (1140258596603533)"
tags:
  - project
  - marketing
  - paid-social
  - meta-ads
  - budamix
---

# Budamix Meta Ads — Paid Social

> Primeira investida de tráfego pago no Meta (Facebook/Instagram) pro e-commerce budamix.com.br.
> Estrutura de 3 campanhas focada no HERO IMB501 (Conjunto 5 Potes Redondos de Vidro).
> Status: estrutura criada PAUSED em 06/06/2026, aguardando 2 vídeos adicionais antes de ativar.

## Coordenadas Meta

| Item | Valor |
|---|---|
| **Business Manager** | Budamix (`836285430695962`) |
| **Conta de Anúncios** | Budamix - Conta de anúncios (`1140258596603533`) |
| **Pixel + CAPI** | Budamix - Pixel da Meta (`460889899401645`) |
| **Catálogo** | Budamix Catálogo (`1973158136897277`) — 23 produtos via feed |
| **Página** | Budamix (`106066888942641`) |
| **Feed XML** | https://budamix.com.br/feeds/meta-catalog.xml |
| **Moeda** | BRL |

## Estratégia consolidada (versão 2026)

3 campanhas com jobs específicos, alinhadas à pesquisa de paid social 2026 (Andromeda, fim dos interesses detalhados, Advantage+ como padrão).

```
CAMPANHA 1 — ASC (Advantage+ Sales) — 65% verba (R$37/dia, CBO)
  → Motor de aquisição fria
  → 1 ad set: BR mulheres 25-55, Advantage+ Audience ON
  → Otimização: ATC inicialmente, migra pra Purchase quando volume sustentar
  → Criativos: vídeos UGC + demo (até 15 ativos quando maduro)

CAMPANHA 2 — Teste de Criativos (ABO Manual) — 20% verba (R$11/dia)
  → Laboratório de criativos
  → 1 ad set 3:2:2: 3 vídeos × 2 títulos × 2 textos
  → Vencedores graduam pra ASC semanalmente

CAMPANHA 3 — Retargeting WCA (ABO) — 15% verba (R$9/dia)
  → Recupera quem visitou mas não comprou
  → 1 ad set: ViewContent 14d EXCLUI Purchase 30d (WCAs pendentes — pixel novo)
  → Otimização: Purchase direto
  → Migrar pra DPA (Dynamic Product Ads) no mês 3+ quando catálogo tiver maturidade
```

## IDs das entidades criadas (todas PAUSED em 06/06/2026)

| Campanha | Campaign ID | Ad Set ID | Budget |
|---|---|---|---|
| 1 — `2026-06-06_Cold_ASC_IMB501_25-55` | `120248423500010402` | `120248423502930402` (Cold_BR_25-55_IMB501_ATC) | CBO R$37/dia |
| 2 — `2026-06-06_Cold_TEST_IMB501_25-55` | `120248423500320402` | `120248423503880402` (Cold_Test_3x2x2_IMB501_ATC) | ABO R$11/dia |
| 3 — `2026-06-06_Warm_DPA_IMB501_Retargeting` | `120248423500930402` | `120248423510550402` (Warm_Retargeting_VC14_NoPurchase30_PURCHASE) | ABO R$9/dia |

## HERO Product — IMB501

**Conjunto 5 Potes Redondos de Vidro Budamix** (`/produto/conjunto-5-potes-redondos-vidro-budamix`)

- 3 variantes (cor da tampa): IMB501C_T (cinza R$24,90), IMB501V_T (vermelha R$24,90), IMB501P_T (preta R$29,90)
- Combos: KIT2 (10 peças R$47,90), KIT3 (15 peças R$67,90)
- Estoque: 21.707 unidades (ranking #1 de receita 90d com R$289.186 — 96% das vendas das 3 linhas de vidro)
- 5,0⭐ / 18 reviews

Critério de escolha: maior receita acumulada + estoque infinito + reviews ótimas. Decisão de focar APENAS no IMB501 nos primeiros 1-2 meses (não pulverizar pras outras 2 linhas — retangulares/quadrados vendem 20x menos).

## URL de destino do anúncio (com UTM)

```
https://budamix.com.br/produto/conjunto-5-potes-redondos-vidro-budamix?utm_source=meta&utm_medium=paid_social&utm_campaign=2026-06-06_Cold_ASC_IMB501&utm_content=video-v2-15s&utm_term=hero-fria
```

Para retargeting (Campanha 3): trocar `utm_campaign=2026-06-06_Warm_DPA_IMB501` + `utm_term=retargeting-warm`.

## Criativos

| Vídeo | Status | Localização |
|---|---|---|
| 1 — Demonstração produto (15s) | ✅ Pronto | `~/Downloads/budamix-imb501-meta-ads-FINAL.mp4` |
| 2 — UGC Testemunho (~18s) | ⏳ Pedro produzindo (tentando IA primeiro, fallback gravar com celular) | — |
| 3 — Antes/Depois (12-15s) | ⏳ Pedro produzindo | — |

**Vídeo 1 final specs:** 1080×1920, 15s, 7.8MB, Antonio Bold + paleta oficial Budamix (Deep Teal/Teal/Burnt Terracotta/Lima Sutil/Ivory Mist), trilha sintética 110 BPM, overlays nos tempos 0-3 (hook "DESPENSA BAGUNÇADA?"), 3-9 (sticker "CONJUNTO 5 POTES DE VIDRO"), 9-12 (preço "R$24,90 / ECONOMIZE 37%"), 12-15 (CTA "FRETE GRÁTIS / BUDAMIX.COM.BR").

## Orçamento e expectativa de resultados

| Item | Valor |
|---|---|
| **Budget mensal** | R$1.710 (R$57/dia) |
| **Distribuição** | 65% ASC / 20% Teste / 15% Retarget |
| **Otimização inicial** | AddToCart (Campanhas 1 e 2) + Purchase (Campanha 3) |
| **Mês 1** | 8-12 vendas, ROAS 1.0-1.3 (exploração) |
| **Mês 2** | 12-20 vendas, ROAS 1.5-2.0 (transição Purchase) |
| **Mês 3+** | 20-35 vendas/mês, ROAS 2.0-3.0+ (escala) |
| **Investimento 3 meses** | ~R$5.130 |

## Pré-requisitos técnicos JÁ resolvidos

- ✅ Pixel client-side instalado e disparando (`VITE_META_PIXEL_ID=460889899401645` em Vercel)
- ✅ CAPI server-side ativo (`/api/meta-capi` + `META_CAPI_ACCESS_TOKEN` em Vercel)
- ✅ Dedup via event_id (`crypto.randomUUID()` + `eventID` no fbq + mesmo ID no POST do CAPI)
- ✅ Email/telefone hasheados no Purchase (server-side SHA-256)
- ✅ Domínio `budamix.com.br` verificado no BM
- ✅ Pixel conectado à Conta de Anúncios + Catálogo
- ✅ Feed XML com 23 produtos válidos, `<g:id>` = variant_id (alinhado com pixel `content_ids`)

## Próximos passos

1. **Pedro entrega vídeos 2 e 3** (até 07/06/2026)
2. **Upload dos 3 vídeos no Meta Asset Library** (via API)
3. **Criar Ads dentro dos 3 ad sets** (1 ad por ad set inicialmente; Campanha 2 vira 3:2:2 quando tiver 3 vídeos)
4. **Criar 2 Custom Audiences** pra Campanha 3 (ViewContent 14d + Purchase 30d) — vazias, populam conforme tráfego entra
5. **Pedro revisa cada peça** e ativa as 3 campanhas

## Decisões estruturais tomadas

- Estratégia D atualizada pra versão 2026 (3 campanhas em vez de 2)
- Orçamento: R$57/dia (calibrado pra otimizar AddToCart e sair do aprendizado em ~3 semanas com ticket R$24,90)
- HERO único: IMB501 (não pulverizar entre redondos/retangulares/quadrados)
- Retargeting começa WCA-based + vídeo, NÃO DPA (migrar mês 3+)
- Sem ferramentas pagas de pesquisa de interesses (AdTargeting etc) — interesses do nicho cobertos via Advantage+ Audience signals

## Audiências de outras contas que servem como "audience signal"

Reaproveitar 2 lookalikes inativos da conta GB Distribuição (`323534883953033`) como audience signal:
- `120220400359220456` — Semelhante (BR, 1%) Visitantes Site (~1M pessoas) — INACTIVE, reativável
- `120219003397950456` — Semelhante (BR, 3%) Engajados Página GB Distribuição (~3M pessoas) — INACTIVE, reativável

## Plano futuro de expansão (mês 3+)

Quando IMB501 atingir ROAS ≥ 2 consistente:
1. Replicar estrutura pros 3 kits retangulares (KIT DESPENSA + KIT ESSENCIAL + KIT COMPLETO)
2. Mês 5+: kits quadrados (KIT SOLO + KIT FAMÍLIA + KIT PRÁTICO)
3. Migrar Campanha 3 de WCA pra DPA (Dynamic Product Ads com catálogo completo)
4. Considerar customer list de compradores marketplace (Pedro vai conseguir lista via empresa parceira semana que vem)

## Notas relacionadas

- [[knowledge/concepts/facebook-page-api-budamix]] — integração FB Page API (token + scopes)
- [[memory/context/decisoes/2026-06]] — decisões de junho
- [[business/marketing/marca]] — paleta oficial Budamix
- [[projects/budamix-ecommerce]] — site de destino

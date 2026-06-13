---
title: "Nomenclatura Padrão de Anúncios (Meta / ML / Amazon)"
created: 2026-06-13
type: reference
status: active
tags:
  - reference
  - marketing
  - meta-ads
  - paid-social
  - convencao
---

# Nomenclatura Padrão de Anúncios

> Padrão único pra nomear **Campanhas, Conjuntos e Anúncios** em todas as contas de tráfego pago (Meta hoje; Mercado Livre Ads / Amazon Ads / Google depois).
> Objetivo: filtrar e analisar por **objetivo, funil, público, criativo e data** direto no Gerenciador. Definido com Pedro em 13/06/2026.

## Princípios

1. Separador entre campos: ` | ` (barra com espaços). Permite filtrar cada campo no Gerenciador de Anúncios.
2. Dentro de um campo, **sem espaço** — usar hífen: `seguidores-reels`, nunca `seguidores reels`.
3. **CÓDIGO em MAIÚSCULA** (marca, objetivo, funil, posicionamento, otimização, formato). Texto livre em minúscula.
4. Datas: `AAAA-MM` na campanha, `AAAA-MM-DD` no anúncio. Ordena cronologicamente sozinho.
5. O slug da campanha deve casar com o `utm_campaign` do link de destino.

## Estrutura por nível

**CAMPANHA** — o quê e por quê:
```
MARCA | OBJETIVO | FUNIL | tema-ou-produto | AAAA-MM
```

**CONJUNTO** — pra quem e onde:
```
PUBLICO | segmentacao | GEO | POSICIONAMENTO | OTIMIZACAO
```

**ANÚNCIO** — qual criativo:
```
FORMATO | criativo-slug | angulo | vNN-AAAA-MM-DD
```

## Dicionário de códigos

- **MARCA:** `BDMX` (Budamix), `GB` (GB Importadora)
- **OBJETIVO** (Meta ODAX): `RECON` (Reconhecimento), `TRAF` (Tráfego), `ENG` (Engajamento), `LEAD` (Leads), `VENDA` (Vendas / ASC), `APP`
- **FUNIL:** `TOPO` (frio/descoberta), `MEIO` (consideração/morno), `FUNDO` (conversão/quente/retargeting)
- **PUBLICO:** `FRIO`, `INT-<tema>` (interesses), `LAL-<x>` (lookalike X%), `RMKT-<fonte>-<janela>` (retargeting; ex: `RMKT-VC14`, `RMKT-IG30`)
- **GEO:** `BR` (Brasil todo) ou siglas de UF com hífen (`SP-MG-RJ-PR-RS-SC`)
- **POSICIONAMENTO:** `IG`, `FB`, `IGFB` (ambos), `ADV` (Advantage+ posicionamentos), `REELS`
- **OTIMIZACAO:** `VISITA-PERFIL`, `THRUPLAY`, `ENGAJ`, `ALCANCE`, `LPV` (landing page views), `ATC` (add to cart), `COMPRA`, `LEAD`
- **FORMATO:** `REEL`, `VIDEO`, `IMG`, `CARROSSEL`, `STORIES`

## Exemplo real — campanha de seguidores (13/06/2026)

```
Campanha: BDMX | TRAF | TOPO | seguidores-reels | 2026-06
Conjunto: FRIO | amplo-18-65 | SP-MG-RJ-PR-RS-SC | IG | VISITA-PERFIL
Anúncios:
  REEL | pote-vidro | chega-inteiro | v1-2026-06-13
  REEL | enviado-af9a | a-confirmar | v1-2026-06-13
  REEL | enviado-7efc | a-confirmar | v1-2026-06-13
```

## Migração do padrão antigo (Spark)

O Spark usava `AAAA-MM-DD_Funnel_Type_Produto_Publico` (ex: `2026-06-06_Cold_ASC_IMB501_25-55`). Mapeamento exemplo:

```
2026-06-06_Cold_ASC_IMB501_25-55   →  BDMX | VENDA | TOPO | asc-imb501 | 2026-06
Cold_BR_25-55_IMB501_ATC (ad set)  →  FRIO | mulheres-18-65 | BR | IGFB | ATC
```

⚠️ Renomear campanha **ativa** é cosmético (não afeta entrega), MAS os `utm_campaign` nos anúncios já no ar continuam no slug antigo até serem editados — manter pra continuidade de analytics; anúncios novos já nascem no padrão.

## Onde isto vale

- O **Spark** deve gerar nomes neste padrão em `meta-ads-create.py` e nos relatórios.
- Vale pra **ML Ads** e **Amazon Ads** quando entrarem (trocar `OBJETIVO`/`POSICIONAMENTO` pelos códigos da plataforma).

## Notas relacionadas

- [[projects/budamix-meta-ads]]
- [[knowledge/concepts/meta-ads-paid-social-2026]]

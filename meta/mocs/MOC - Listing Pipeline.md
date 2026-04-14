---
title: "MOC   Listing Pipeline"
created: 2026-04-14
type: moc
status: active
tags:
  - moc
---

# MOC — Listing Pipeline

> Fluxo completo: pesquisa de mercado → criacao de listing → planilha → monitoramento.

---

## Pipeline

```
1. Pesquisa de mercado (concorrencia, gap, preco)
   ↓
2. Criacao do listing (API por plataforma)
   ↓
3. Registro na planilha de estoque/preco
   ↓
4. Monitoramento (taxas, margem, ranking)
```

## Etapa 1 — Pesquisa

| Skill | Plataforma |
|-------|-----------|
| [[skills/marketplace/ml-competitor-analysis/SKILL|ml-competitor-analysis]] | Mercado Livre (Bright Data + ML API) |
| [[skills/marketplace/marketplace-optimization/SKILL|marketplace-optimization]] | Cross-platform (ranking factors) |

## Etapa 2 — Criacao

| Skill | Plataforma | Checklist |
|-------|-----------|-----------|
| [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]] | Amazon BR (SP-API) | Product type, GTIN exemption, FBA |
| [[skills/shopee-listing-creator/SKILL|shopee-listing-creator]] | Shopee (Open API v2) | 3 lojas, brand_id 5014011, diagnostico Qualificado |

> ML: ainda sem skill de criacao automatizada (manual via API ou Seller Central)

## Etapa 3 — Registro

| Skill | O que faz |
|-------|----------|
| [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] | Registrar SKU nas 4 abas (ESTOQUE primeiro, depois MELI/SHOPEE/AMAZON) |

## Etapa 4 — Monitoramento

| Skill | O que monitora |
|-------|---------------|
| [[skills/marketplace/amazon-fees-rules/SKILL|amazon-fees-rules]] | Taxas Amazon (cron quarta 10h) |
| [[skills/marketplace/ml-fees-rules/SKILL|ml-fees-rules]] | Taxas ML (cron quarta 10h) |
| [[skills/marketplace/shopee-fees-rules/SKILL|shopee-fees-rules]] | Taxas Shopee (cron quarta 10h) |
| [[skills/update-ml-return-rates/SKILL|update-ml-return-rates]] | Taxas de devolucao ML (quinzenal) |

## Casos reais documentados

- **PCM001** (Kit 6 Porta-Copos MDF): ML + Shopee + Amazon — [[memory/sessions/2026-04-07|sessao 07/04]]
- **DPM001** (Descanso de Panela Modular): ML + Shopee + Amazon — [[memory/sessions/2026-04-10|sessao 10/04]]
- **Analise Shopee Porta-Copos**: [[memory/projects/shopee-porta-copos-analise|analise mercado]]

---

*Criado: 10/04/2026 — Auditoria de conexoes*

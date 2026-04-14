# Lições — Trader

_Erros e aprendizados. [ESTRATÉGICA] = permanente, [TÁTICA] = expira 30 dias._

### 2026-03-16 — Amazon Ads API: Brasil usa endpoint NA [TÁTICA]
**Contexto:** Tentei endpoint `advertising-api-sa.amazon.com`.
**Erro:** DNS não resolve — endpoint SA não existe.
**Lição:** Brasil = endpoint NA: `advertising-api.amazon.com`.
**Expira:** 2026-04-15

### 2026-03-16 — wkhtmltopdf não suporta CSS Grid [TÁTICA]
**Contexto:** Cards KPI empilhados verticalmente em vez de lado a lado no PDF.
**Lição:** Usar `display: table` + `table-cell` para layouts em PDFs via wkhtmltopdf. Mas output agora é HTML — less relevant.
**Expira:** 2026-04-15

### 2026-03-17 — ML Ads: seção 5 do marketplace-report funciona [TÁTICA]
**Contexto:** Implementei seção 5 com dados reais (ROAS 8.76x, 21 campanhas).
**Lição:** Skill ml-ads + s05_ads.py prontos. Auth via ml-refresh-token.sh vendas. Header: Api-Version: 2.
**Expira:** 2026-04-17

### 2026-03-19 — Shopee é SPA — scraping limitado [TÁTICA]
**Contexto:** Tentei scraping Shopee via Bright Data Web Unlocker.
**Problema:** HTML sem dados de produto (SPA). APIs internas bloqueadas ("low SR").
**Lição:** JSON-LD tem 10 primeiros resultados (nome + URL + imagem, sem preço). Screenshot + extração visual funciona pra preço. API oficial é o melhor caminho.
**Expira:** 2026-04-19

### 2026-03-19 — Bright Data Premium Domains — propagação [TÁTICA]
**Contexto:** Ativamos Premium Domains pra Shopee.
**Lição:** Após ativar no painel, pode demorar pra propagar. Verificar via API: `ub_premium: 1` no response de `/zone?zone=web_unlocker1`.
**Expira:** 2026-04-19

### 2026-03-20 — Consolidado financeiro: HTML + Excel SEMPRE juntos [ESTRATÉGICA]
**Contexto:** Pedro quer os dois formatos em toda entrega financeira.
**Lição:** Nunca entregar só HTML ou só Excel. Os dois são complementares.

### 2026-03-21 — SKU Amazon é imutável [ESTRATÉGICA]
**Contexto:** Tentativa de padronizar SKUs cross-platform.
**Lição:** Amazon SKU NÃO pode ser renomeado — perde listing, histórico e ranking. Usar Apelido do SKU no Upseller como alternativa.

### 2026-04-10 — Solicitations 403 pode ser endpoint errado, não permissão [TÁTICA]
**Contexto:** Request Review manual primeiro retornou 403 e o diagnóstico inicial foi role/scope faltando.
**Lição:** Antes de atribuir 403 a permissão, validar o path exato da Solicitations API. O endpoint que funcionou foi `productReviewAndSellerFeedback`; `productReview` levou a falso negativo.
**Expira:** 2026-05-10

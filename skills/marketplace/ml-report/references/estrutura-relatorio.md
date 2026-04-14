---
title: "estrutura relatorio"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Estrutura do Relatório — 9 Seções

Documentação detalhada de cada seção do relatório de performance ML.

---

## Seção 1 — Capa & Resumo Executivo

**Objetivo:** Visão macro instantânea. Pedro abre o PDF e em 30 segundos sabe se o período foi bom ou ruim.

**Conteúdo:**
- Header com logo Budamix + "Relatório de Performance · Mercado Livre"
- Período do relatório (ex: "1 a 15 de março de 2026")
- Gerado em: {data_hora}
- **KPIs Resumo (6 cards grandes):**
  - 💰 Receita bruta total
  - 📦 Total de pedidos
  - 🏆 Ticket médio
  - ⭐ Reputação (nível + pontuação)
  - 🚀 Anúncios ativos
  - 📈 Receita/dia (média)
- Parágrafo executivo curto (3-4 linhas) com highlights do período

**Fonte dos dados:** `/orders/search`, `/users/{id}`

---

## Seção 2 — Faturamento & Receita

**Objetivo:** Entender a composição financeira real — receita bruta vs líquida, impacto das taxas.

**Conteúdo:**
- **KPIs principais:**
  - Receita bruta (GMV)
  - Comissões ML (total e % da receita)
  - Taxas de frete (custo)
  - Devoluções/reembolsos
  - Receita líquida estimada
- **Gráfico:** Line chart — evolução diária da receita bruta no período
- **Gráfico:** Donut chart — composição da receita (líquido vs taxas vs frete vs devoluções)
- **Tabela:** Top 10 dias por faturamento

**Fonte dos dados:** `/v1/payments/search` (token finance), `/orders/search` (token vendas)

**Observação:** Dados de taxa de marketplace e frete extraídos dos pagamentos Mercado Pago.

---

## Seção 3 — Volume de Vendas & Conversão

**Objetivo:** Entender ritmo de vendas, sazonalidade e eficiência de conversão.

**Conteúdo:**
- **KPIs principais:**
  - Total de pedidos no período
  - Unidades vendidas total
  - Ticket médio por pedido
  - Itens médios por pedido
  - Pedidos cancelados / taxa de cancelamento
- **Gráfico:** Bar chart — pedidos por dia
- **Gráfico:** Bar chart — pedidos por hora (distribuição no dia)
- **Gráfico:** Line chart — evolução do ticket médio ao longo do período
- **Tabela:** Vendas por dia da semana (média)

**Fonte dos dados:** `/orders/search` (token vendas)

**Nota:** Taxa de conversão (visitas/pedidos) indisponível via API — marcado como "Dado não disponível".

---

## Seção 4 — Tráfego & Visibilidade

**Objetivo:** Entender alcance orgânico e posicionamento.

**Conteúdo:**
- **KPIs:**
  - Visitas totais → "Dado não disponível — API não expõe"
  - Impressões → "Dado não disponível — API não expõe"
  - CTR médio → "Dado não disponível — API não expõe"
  - Taxa de conversão (visitas→venda) → "Dado não disponível"
- **Seção de contexto:** Explicação de por que esses dados não estão disponíveis via API pública do ML
- **O que está disponível:**
  - Volume de pedidos como proxy de tráfego convertido
  - Distribuição de vendas por anúncio (indicativo de visibilidade relativa)

**Fonte dos dados:** Nenhuma (dados de tráfego não disponíveis na API pública do ML)

**Recomendação:** Acessar Seller Central > Publicidade > Métricas para dados completos de tráfego.

---

## Seção 5 — Publicidade / ML Ads

**Objetivo:** Performance dos anúncios patrocinados.

**Conteúdo:**
- **KPIs:** Todos marcados como "Dado não disponível — API não expõe"
  - Impressões de ads
  - Cliques em ads
  - CTR de ads
  - Investimento em ads
  - Receita atribuída a ads
  - ROAS
  - ACoS (custo/receita)
- **Nota informativa:** API pública do ML não expõe dados de ads diretamente
- **Proxy disponível:** Anúncios com status "gold_special" ou "premium" identificados no catálogo
- **Recomendação:** Integração manual via exportação do Seller Central

**Fonte dos dados:** `/users/{id}/items/search` para identificar anúncios premium

---

## Seção 6 — Reputação & Saúde da Conta

**Objetivo:** Status da conta e risco operacional.

**Conteúdo:**
- **KPIs principais:**
  - Nível de reputação (cor: verde/amarelo/laranja/vermelho)
  - Pontuação numérica
  - Status da conta (ativo, com restrições, etc.)
  - Reclamações no período (% sobre vendas)
  - Envios atrasados (% sobre total)
  - Cancelamentos pelo vendedor (% sobre total)
- **Visual:** Badge colorido com nível de reputação (semáforo)
- **Tabela:** Thresholds do ML para cada nível (referência)
- **Gráfico:** Gauge/donut mostrando posição no nível atual

**Fonte dos dados:** `/users/532562281` (token metrics ou vendas)

---

## Seção 7 — Logística & Envios

**Objetivo:** Eficiência operacional de expedição e entrega.

**Conteúdo:**
- **KPIs principais:**
  - Total de envios no período
  - Envios Full (% do total)
  - Envios Flex (% do total)
  - Envios normais/coleta (% do total)
  - Pedidos com atraso na expedição
  - Reclamações relacionadas a envio
- **Gráfico:** Donut — distribuição por modalidade de envio
- **Gráfico:** Bar — pedidos por status de envio (entregue, em transporte, atrasado)
- **Tabela:** Top estados por volume de envios

**Fonte dos dados:** `/orders/search` com detalhamento de `shipping`

---

## Seção 8 — Anúncios & Catálogo

**Objetivo:** Saúde do catálogo e performance por produto.

**Conteúdo:**
- **KPIs principais:**
  - Total de anúncios ativos
  - Anúncios pausados
  - Anúncios com problema de estoque (sem estoque)
  - Anúncios premium/gold
- **Tabela:** Top 20 anúncios por receita no período
  - Título do anúncio
  - SKU / ID
  - Unidades vendidas
  - Receita total
  - Ticket médio
  - % da receita total
- **Gráfico:** Bar horizontal — top 10 produtos por receita
- **Gráfico:** Bar horizontal — top 10 produtos por volume (unidades)

**Fonte dos dados:** `/users/{id}/items/search`, `/items/{id}`, `/orders/search` (correlação)

---

## Seção 9 — Insights Estratégicos & Plano de Ação

**Objetivo:** Síntese inteligente para tomada de decisão. A seção mais valiosa.

**Conteúdo:**
- **Highlights do período** (gerados automaticamente com base nos dados)
  - 3 pontos positivos identificados
  - 3 pontos de atenção/risco
- **Oportunidades detectadas** (baseadas em padrões nos dados)
  - Ex: "Produto X vende 3x mais às quintas — considerar estoque extra"
  - Ex: "Ticket médio caindo — verificar mix de produtos"
- **Alertas de risco**
  - Ex: "Reputação próxima do limite — reduzir cancelamentos"
  - Ex: "Top produto representa 60% da receita — diversificar"
- **Plano de ação sugerido** (priorizado)
  - Ação imediata (esta semana)
  - Ação de médio prazo (próximos 30 dias)
  - Ação estratégica (próximos 90 dias)
- **Assinatura:** "Relatório gerado por Tobias · GB Importadora · Budamix"

**Fonte dos dados:** Síntese de todas as seções anteriores (dados calculados na engine)

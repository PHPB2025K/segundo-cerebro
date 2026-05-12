---
name: trader-marketplace-rules-watch
description: Monitoramento de regras, taxas e políticas de Mercado Livre, Shopee e Amazon para o Trader. Use em checks diários/semanais, quando houver mudança de comissão, frete, taxa fixa, política comercial, Full/FBA, anúncios, reputação, campanha ou quando uma mudança externa puder explicar o Daily Sales Report v2.
---

# Trader — Marketplace Rules Watch

## Objetivo
Detectar mudanças externas de marketplace que possam afetar vendas, margem, exposição, frete, campanhas ou interpretação do Daily Sales Report v2.

## Escopo
Monitorar:
- Mercado Livre: tarifas, Clássico/Premium, Full, reputação, anúncios, políticas comerciais.
- Shopee: comissão, taxa fixa, taxa de transação, frete, cupons, campanhas, regras de loja.
- Amazon: referral fee, FBA, Buy Box, listing, elegibilidade, políticas de anúncio.

## Frequência recomendada
- Check leve diário: só procurar comunicados/alertas relevantes recentes.
- Revisão profunda semanal: conferir páginas oficiais, changelogs e regras críticas.
- Revisão ad hoc: sempre que o report detectar comportamento estranho sem causa operacional.

## Fontes
Prioridade:
1. Páginas oficiais/central do seller/plataforma.
2. Comunicados oficiais por e-mail/painel.
3. APIs/changelogs oficiais quando disponíveis.
4. Fontes secundárias apenas como alerta, nunca como verdade final.

## Como registrar
Registrar em:
`shared/trader/memory/projects/daily-sales-report/marketplace-rules-watch.md`

Cada entrada deve conter:
- Data detectada.
- Plataforma.
- Regra/taxa/política.
- Fonte.
- O que mudou.
- Impacto potencial.
- Contas/SKUs afetados, se houver.
- Se deve aparecer no Daily Sales Report.
- Data de revisão/expiração.

## Quando entra no Sales Report
Só entra se impactar o dia ou a ação recomendada.

Exemplos que entram:
- taxa/frete/campanha mudou e pode explicar queda de conversão;
- regra de Full/FBA afetou disponibilidade;
- política de ADS alterou exposição;
- mudança de comissão altera leitura de margem/preço.

Exemplos que não entram:
- notícia genérica sem impacto claro;
- mudança futura sem efeito operacional no dia;
- rumor não confirmado.

## Escalonamento
Avisar Kobe se:
- impacto potencial for material;
- exigir decisão de preço/margem;
- exigir ação com Himmel;
- afetar múltiplas contas;
- houver prazo curto para adaptação.


## Implementação Daily Sales Report v2 — Fase 8
- Arquivo operacional consumido pelo Trader: `shared/trader/memory/projects/daily-sales-report/marketplace-rules-watch.md`.
- Script canônico de refresh leve diário:
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-marketplace-rules-watch.py
```
- Cron leve diário: `Daily Sales v2 — Marketplace Rules Watch Refresh`, 06:23 BRT.
- Crons profundos por plataforma:
  - ML Fees Monitor — segunda 10:00 BRT.
  - Shopee Fees Monitor — quarta 10:00 BRT.
  - Amazon Fees Monitor — quarta 10:17 BRT.
- O refresh leve consolida estado das skills e revisões vencidas/próximas; não substitui auditoria profunda das fontes oficiais.
- Revisão vencida deve virar alerta interno; não deve ser apresentada ao funcionário como mudança confirmada.

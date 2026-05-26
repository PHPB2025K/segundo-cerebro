# Monitoramento de Regras dos Marketplaces

Registro operacional de mudanças/revisões de regras, políticas e taxas que podem impactar vendas, margem, exposição, frete, campanhas ou interpretação do Daily Sales Report v2.

_Atualizado automaticamente em 2026-05-25 06:23 BRT por `daily-sales-v2-marketplace-rules-watch.py`._

## Como usar no Daily Sales Report v2
- Usar como contexto causal/hipótese, não como explicação automática.
- Só mencionar no report se a regra/taxa/política puder explicar o dia analisado ou mudar uma prioridade prática.
- Se houver revisão vencida, tratar como alerta interno de qualidade de contexto, não como mudança confirmada.
- Fonte de verdade das regras detalhadas continua sendo a skill específica de cada plataforma.

## Mercado Livre
- **Status:** 🟡 revisão próxima (2026-05-25)
- **Última atualização da skill:** 2026-05-18
- **Próxima revisão prevista:** 2026-05-25
- **Cron/revisão profunda:** ML Fees Monitor — segunda 10h BRT
- **Skill fonte:** `skills/marketplace/ml-fees-rules/SKILL.md`
- **Resumo vigente:** ⚠️ **Última atualização:** 18/05/2026
- **Impacto operacional para reports:**
  - Custos ML impactam margem, decisão Clássico/Premium, frete grátis, Full e competitividade de preço.
  - Mudanças em frete/reputação podem explicar queda de conversão mesmo com demanda estável.
  - Diferença Clássico vs Premium deve ser considerada quando exposição/parcelamento mudar performance.

## Shopee
- **Status:** 🟢 mudança confirmada em 2026-05-26
- **Última atualização da skill:** 2026-05-26
- **Próxima revisão prevista:** 2026-06-02
- **Cron/revisão profunda:** Shopee Fees Monitor — quarta 10h SP
- **Skill fonte:** `skills/marketplace/shopee-fees-rules/SKILL.md`
- **Resumo vigente:** ✅ **Atualização confirmada:** 26/05/2026 — programa **Full+ Shopee**
- **Impacto operacional para reports:**
  - Taxas Shopee impactam diretamente margem, preço mínimo, viabilidade de cupons, frete grátis e leitura de conversão nas 3 contas.
  - Monitorar armadilhas de faixa/taxa fixa, especialmente produtos entre R$ 8 e R$ 99,99.
  - Subsídio PIX/cupons pode alterar ticket e conversão sem necessariamente indicar mudança orgânica de demanda.
  - **Novo desde junho/2026:** pedidos via Full podem gerar devolução de comissão na carteira Shopee no mês seguinte, se a loja atingir pelo menos **40% de participação de pedidos no Full** no mês calendário.
  - Faixas do Full+: **40%–69,99%** de participação Full → devolução de **0,5 p.p.** para itens de **R$ 50–79,99** e **1 p.p.** para itens de **R$ 80+**; **70%+** de participação Full → devolução de **1 p.p.** para itens de **R$ 50–79,99** e **2 p.p.** para itens de **R$ 80+**.
  - Itens **abaixo de R$ 50** contam para formar a participação Full da loja, mas **não recebem** devolução de comissão.
  - O benefício é **automático**, apurado em **mês fechado**, pago na **primeira semana do mês seguinte**, e vale até **dezembro/2026**, com possibilidade de alteração unilateral pela Shopee.
  - Em análise diária, Full+ entra como contexto causal de **margem e incentivo logístico**, não como explicação automática de alta/queda de vendas no mesmo dia, porque o efeito financeiro cai na carteira apenas no mês seguinte.

### Entrada confirmada — 2026-05-26 — Programa Full+ Shopee
- **Plataforma:** Shopee BR
- **Regra/taxa/política:** devolução progressiva de comissão para pedidos enviados via Full
- **Fonte:** artigo oficial Shopee Seller Education Hub `article_id=27600` — *Conheça o programa Full+ Shopee e as vantagens para seu negócio* (publicado em 19/05/2026)
- **O que mudou:** a partir de junho/2026, vendedores Full passam a ter um rebate de comissão condicionado à participação mensal de pedidos enviados via Full.
- **Mecânica:**
  - abaixo de 40% de participação Full no mês: sem devolução, embora os pedidos Full contem para formar a faixa;
  - 40%–69,99%: rebate de 0,5 p.p. para itens entre R$ 50 e R$ 79,99 e 1 p.p. para itens a partir de R$ 80;
  - 70%+: rebate de 1 p.p. para itens entre R$ 50 e R$ 79,99 e 2 p.p. para itens a partir de R$ 80.
- **Elegibilidade:** só pedidos vendidos via Full com item >= R$ 50 recebem rebate; itens < R$ 50 contam para participação, mas não recebem devolução.
- **Liquidação financeira:** devolução creditada na carteira Shopee na primeira semana do mês seguinte; a comissão do mês corrente continua sendo cobrada normalmente.
- **Impacto potencial:**
  - favorece aumento de participação Full nas contas Shopee quando a margem suporta a logística;
  - melhora margem efetiva dos itens Full elegíveis, principalmente acima de R$ 80;
  - pode justificar priorização de sortimento Full e leitura separada entre ganho comercial no dia vs ganho financeiro no fechamento do mês seguinte.
- **Contas/SKUs afetados:** 3 contas Shopee da GB; impacto maior em SKUs Full com preço >= R$ 50 e volume relevante.
- **Se deve aparecer no Daily Sales Report:** sim, quando ajudar a explicar decisão de migrar/sustentar mix no Full, pressão por participação Full ou revisão de margem/preço; não usar como explicação imediata para conversão do dia sem evidência adicional.
- **Data de revisão/expiração:** revisar até 02/06/2026 e manter monitorado até o término informado do programa em 12/2026.

## Amazon
- **Status:** ⚠️ revisão vencida desde 2026-05-20
- **Última atualização da skill:** 2026-05-13
- **Próxima revisão prevista:** 2026-05-20
- **Cron/revisão profunda:** Amazon Fees Monitor — quarta 10h SP
- **Skill fonte:** `skills/marketplace/amazon-fees-rules/SKILL.md`
- **Resumo vigente:** ⚠️ **Última atualização:** 13/05/2026
- **Impacto operacional para reports:**
  - Regras Amazon impactam FBA, Buy Box, comissão, parcelamento e leitura de cancelamentos/indisponibilidade.
  - FBA/Buy Box devem ser checados antes de escalar ADS quando houver cancelamento ou ruptura.
  - Taxa de parcelamento pode afetar margem e pricing em faixas específicas.

---

## Checklist de escalonamento
Escalar para Kobe/Pedro quando:
- houver mudança confirmada que afete margem/preço/frete/comissão;
- revisão vencida coincidir com anomalia forte no Daily Sales;
- mudança exigir decisão de preço, campanha, estoque, Full/FBA ou Himmel;
- regra afetar múltiplas contas/canais ao mesmo tempo.

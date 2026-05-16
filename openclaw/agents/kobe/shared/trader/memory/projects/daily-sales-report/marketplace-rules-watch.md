# Monitoramento de Regras dos Marketplaces

Registro operacional de mudanças/revisões de regras, políticas e taxas que podem impactar vendas, margem, exposição, frete, campanhas ou interpretação do Daily Sales Report v2.

_Atualizado automaticamente em 2026-05-16 06:23 BRT por `daily-sales-v2-marketplace-rules-watch.py`._

## Como usar no Daily Sales Report v2
- Usar como contexto causal/hipótese, não como explicação automática.
- Só mencionar no report se a regra/taxa/política puder explicar o dia analisado ou mudar uma prioridade prática.
- Se houver revisão vencida, tratar como alerta interno de qualidade de contexto, não como mudança confirmada.
- Fonte de verdade das regras detalhadas continua sendo a skill específica de cada plataforma.

## Mercado Livre
- **Status:** 🟡 revisão próxima (2026-05-18)
- **Última atualização da skill:** 2026-05-11
- **Próxima revisão prevista:** 2026-05-18
- **Cron/revisão profunda:** ML Fees Monitor — segunda 10h BRT
- **Skill fonte:** `skills/marketplace/ml-fees-rules/SKILL.md`
- **Resumo vigente:** ⚠️ **Última atualização:** 11/05/2026
- **Impacto operacional para reports:**
  - Custos ML impactam margem, decisão Clássico/Premium, frete grátis, Full e competitividade de preço.
  - Mudanças em frete/reputação podem explicar queda de conversão mesmo com demanda estável.
  - Diferença Clássico vs Premium deve ser considerada quando exposição/parcelamento mudar performance.

## Shopee
- **Status:** ⚠️ revisão vencida desde 2026-05-06
- **Última atualização da skill:** 2026-04-29
- **Próxima revisão prevista:** 2026-05-06
- **Cron/revisão profunda:** Shopee Fees Monitor — quarta 10h SP
- **Skill fonte:** `skills/marketplace/shopee-fees-rules/SKILL.md`
- **Resumo vigente:** ⚠️ **Última atualização:** 29/04/2026
- **Impacto operacional para reports:**
  - Taxas Shopee impactam diretamente margem, preço mínimo, viabilidade de cupons, frete grátis e leitura de conversão nas 3 contas.
  - Monitorar armadilhas de faixa/taxa fixa, especialmente produtos entre R$ 8 e R$ 99,99.
  - Subsídio PIX/cupons pode alterar ticket e conversão sem necessariamente indicar mudança orgânica de demanda.

## Amazon
- **Status:** ✅ revisão vigente até 2026-05-20
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

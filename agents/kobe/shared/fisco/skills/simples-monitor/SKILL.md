# Skill: Monitor de Limites Simples Nacional (Módulo E)

_Acompanha faturamento acumulado por CNPJ e alerta antes de estourar o teto._

---

## Trigger
- Cron semanal (ou pós-sync de vendas)
- Sob demanda do Kobe

## Por que é crítico
Estourar o Simples Nacional (R$ 4,8M/ano por CNPJ) inviabiliza TODO o modelo fiscal da GB. O modelo depende de 3 CNPJs no Simples pra operar o varejo B2C com carga tributária competitiva. Perder o Simples num CNPJ = replanejamento fiscal emergencial.

## Fluxo

```
1. Para CADA CNPJ Simples:
   a. Puxar faturamento acumulado no ano-calendário (via Trader)
      - Fonte: pedidos faturados (não apenas vendidos) no período 01/jan até hoje
      - Incluir: ML + Shopee + Amazon (todos os canais do CNPJ)
   b. Calcular:
      - faturamento_acumulado
      - pct_do_teto = faturamento_acumulado / 4.800.000 × 100
      - projecao_anual = faturamento_acumulado / meses_decorridos × 12
      - meses_restantes = 12 - meses_decorridos
      - headroom = 4.800.000 - faturamento_acumulado
      - media_mensal_permitida = headroom / meses_restantes
   c. Classificar:
      - < 70%: 🟢 Normal
      - 70-84%: 🟡 Atenção — alertar Kobe
      - 85-94%: 🔴 Crítico — alertar Kobe imediatamente
      - ≥ 95%: 🚨 Bloqueante — parar distribuição, escalar Pedro + Suellen
2. Se projeção anual > R$ 4,8M em qualquer CNPJ → alerta independente do % atual
3. Gerar relatório resumido
```

## CNPJs Monitorados

| CNPJ | Nome | Teto |
|------|------|------|
| 07.194.128/0001-82 | GB Comércio | R$ 4.800.000 |
| 45.200.547/0001-79 | Trades | R$ 4.800.000 |
| 63.922.116/0001-06 | Broglio | R$ 4.800.000 |

## Parâmetros (de tax-rules.json)
- `simples_nacional.annual_limit_brl`: 4.800.000
- `simples_nacional.alert_thresholds_pct`: [70, 85, 95]

## Output — Relatório Semanal

```
CNPJ: GB Comércio (07.194.128/0001-82)
  Acumulado: R$ X.XXX.XXX (XX% do teto)
  Projeção anual: R$ X.XXX.XXX
  Headroom: R$ X.XXX.XXX
  Média mensal permitida: R$ XXX.XXX
  Status: 🟢/🟡/🔴/🚨
```

## Ações por Threshold

| % do Teto | Ação |
|-----------|------|
| < 70% | Silêncio. Incluir no relatório semanal. |
| 70-84% | Alertar Kobe. Incluir recomendação de redistribuição. |
| 85-94% | Alertar Kobe imediatamente. Recomendar pausa de vendas no CNPJ. |
| ≥ 95% | Bloquear distribuição pro CNPJ. Escalar Pedro + Suellen. |

## Redistribuição Preventiva
Quando um CNPJ atinge 70%:
- Calcular se é possível redistribuir volume pros outros 2 CNPJs
- Apresentar cenário de redistribuição ao Kobe
- NÃO redistribuir automaticamente — requer aprovação

## Dependências
- Trader: faturamento por CNPJ acumulado no ano
- Config: tax-rules.json (limites e thresholds)

# MAINTENANCE — Memória do Daily Sales Analyst

## Política de manutenção

### Daily (memory/accounts/[conta]/daily/)
- Um arquivo por data (YYYY-MM-DD.md).
- Nunca sobrescrever arquivo existente sem backup.
- Arquivo diário contém memória condensada do ciclo: hipóteses, sinais, ressalvas, fatos relevantes.
- Retenção: mínimo 30 dias; arquivar após 60 dias.

### Weekly (memory/accounts/[conta]/weekly.md)
- Atualização: segunda de manhã OU após 7 entradas diárias acumuladas (o que vier primeiro).
- Consolida teses, padrões, hipóteses e riscos da semana.
- Não sobrescrever — adicionar nova entrada no topo, preservar histórico abaixo.
- Tese semanal deve referenciar leituras diárias que a sustentam.

### Monthly (memory/accounts/[conta]/monthly.md)
- Atualização: primeiro dia útil do mês.
- Consolida teses semanais e evolução de patamar.
- Não sobrescrever — adicionar nova entrada no topo, preservar histórico abaixo.
- Tese mensal deve referenciar teses semanais.

### Rules (memory/accounts/[conta]/rules.md)
- Só muda por:
  - Decisão explícita do Trader ou Kobe.
  - Mudança documentada de regra de marketplace.
  - QA recorrente (3+ ressalvas similares na semana).
  - Aprovação Trader (operacional) ou Kobe (estratégico).
- Toda alteração registrada com data, motivo e quem aprovou.

## Responsabilidades

| Ação | Quem executa | Quem valida |
|------|-------------|-------------|
| Sugere atualização de memória diária | DSA | — (automático) |
| Aplica memória diária | DSA | Trader revisa |
| Sugere atualização de weekly/monthly | DSA | Trader valida |
| Aplica weekly/monthly | DSA após aprovação | Trader |
| Sugere mudança de rules | DSA | Trader (operacional) ou Kobe (estratégico) |
| Aplica mudança de rules | Trader ou Kobe | Kobe (se estratégico) |

## Princípios

- DSA sugere e aplica memória operacional; Trader valida regras permanentes; Kobe entra em decisões estratégicas ou conflitos.
- Memória não conflita com domínio do Trader.
- Toda memória aplicada é registrada e auditável.
- Memória é input para análise, nunca fonte primária de dados de venda.

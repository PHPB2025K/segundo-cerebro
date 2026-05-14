# Audit Ressalvas — Daily Sales Analyst

## Objetivo

Registro e monitoramento de ressalvas recorrentes para detecção de padrões que exigem ação corretiva no sistema (regras, prompts ou Data Builder).

## Agrupamentos

As ressalvas são agrupadas por:
- **Tipo**: dado, identificação, fidelidade, formatação, confiança, bloqueio, consistência
- **Camada de origem**: Estratégica, Tática, Operacional, Granular, Condensadora, Slack Writer, QA Gate
- **Conta/plataforma**: por conta específica ou transversal
- **Severidade original**: Crítico, Maior, Menor

## Triggers de escalonamento

### Trigger 1 — Flag semanal para Trader
- **Condição**: N >= 3 ressalvas similares (mesmo tipo + mesma camada) na semana.
- **Ação**: Flag automático na consolidação semanal para revisão do Trader.
- **Objetivo**: Identificar padrão recorrente antes que vire bloqueio.

### Trigger 2 — Escala para Kobe
- **Condição**: N >= 5 ressalvas similares (mesmo tipo + mesma camada) no mês.
- **Ação**: Escalonamento para Kobe com relatório de padrão.
- **Objetivo**: Decisão sobre mudança estrutural (regra, prompt ou processo).

### Trigger 3 — Revisão formal
- **Condição**: Padrão de ressalva por 2+ semanas consecutivas (mesma categoria, aparecendo em semanas seguidas).
- **Ação**: Revisão formal de regra, prompt ou Data Builder.
- **Quem decide**: Kobe (se estratégico) ou Trader (se operacional).
- **Artefato**: Documento de revisão com diagnóstico, proposta e aprovação.

## Registro

### Template de entrada

```
Data: YYYY-MM-DD
Tipo: [dado/identificação/fidelidade/formatação/confiança/bloqueio/consistência]
Camada: [Estratégica/Tática/Operacional/Granular/Condensadora/Slack Writer/QA Gate]
Conta: [conta específica ou "transversal"]
Severidade: [Crítico/Maior/Menor]
Descrição: [descrição da ressalva]
Recorrência: [primeira vez / N-ésima ocorrência na semana / N-ésima no mês]
Trigger ativado: [nenhum / flag Trader / escala Kobe / revisão formal]
```

## Histórico

*Registros abaixo. Mais recente primeiro.*

---

*Nenhuma ressalva registrada ainda. Sistema em fase de implementação (Fase 2).*

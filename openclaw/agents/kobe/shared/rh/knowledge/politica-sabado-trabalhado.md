---
title: "Política — Sábado Trabalhado"
created: 2026-04-30
type: policy
agent: kobe
domain: rh
status: active
tags:
  - agent/kobe
  - rh
  - politica
  - banco-horas
  - sabado
---

# Política — Sábado Trabalhado

## Regra

Sábados trabalhados na GB Importadora são **pagos como valor fixo separado**, fora do banco de horas. Isso significa que:

1. **Não acumulam horas extras** no sistema Ponto Certo
2. **Não devem ser registrados** como batidas em `time_records`
3. Funcionários recebem o valor combinado **diretamente em folha ou pagamento avulso**

## Como o agente RH deve tratar

Se o agente RH detectar batidas em sábado em qualquer mês:

1. **NÃO** classificar como hora extra automaticamente
2. **Comunicar com Pedro primeiro** via Telegram thread 10 antes de qualquer ação
3. **Confirmar com Pedro** se foi sábado autorizado e se o pagamento foi à parte
4. Se confirmado: **deletar as batidas** de sábado da tabela `time_records` (depois do fechamento mensal estar registrado, se necessário)

## Como comunicar com o funcionário (se necessário)

Quando o agente RH precisar conversar sobre isso com o funcionário (raro — geralmente Pedro lida diretamente):

```
Oi, [Nome]! Tudo bem?
Vi aqui que você bateu ponto no sábado [DD/MM]. Só pra confirmar:
o trabalho de sábado foi pago à parte, fora do banco de horas, conforme
combinado. Por isso vou tirar essas batidas do sistema — assim seu saldo
não fica confuso.
Qualquer dúvida me avisa.
```

## Histórico de aplicações

### Abril/2026 (executado em 30/04/2026)

10 batidas de sábado deletadas após confirmação do Pedro de que foram pagas à parte:

| Data | Funcionário | Entrada | Saída |
|------|-------------|---------|-------|
| 04/04 (sáb) | Geziele Batista | 06:46 | 12:48 |
| 04/04 (sáb) | Lucas Laurentino | 06:45 | 11:31 |
| 18/04 (sáb) | Franciele Aguiar | 07:00 | 11:03 |
| 25/04 (sáb) | Geziele Batista | 07:59 | 11:13 |
| 25/04 (sáb) | Mateus Lisboa | 08:08 | 15:17 |

Rollback completo em `/tmp/ponto-abril/rollback-sabados-abril-20260430-090644.json`.

## Cross-refs

- [[openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo|Regras Ponto Certo]] — regra geral sábado/domingo (jornada=0, qualquer hora trabalhada conta integralmente como extra)
- [[openclaw/agents/kobe/shared/rh/skills/comunicacao-funcionarios/SKILL|Skill Comunicação]] — fluxo de mensagem semanal
- [[memory/context/decisoes/2026-04|Decisões abr/26]] — decisão completa do incidente

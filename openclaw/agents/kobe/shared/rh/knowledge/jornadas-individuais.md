---
title: "Jornadas Individuais"
created: 2026-04-30
type: policy
agent: kobe
domain: rh
status: active
tags:
  - agent/kobe
  - rh
  - politica
  - jornada
  - banco-horas
---

# Jornadas Individuais — Funcionários com Horário Diferenciado

> Configurações de jornada que diferem do padrão Seg-Qui 8h30 / Sex 8h.
> Atualizar sempre que houver acordo formal de jornada com algum funcionário.
> O sistema Ponto Certo NÃO suporta nativamente jornada por funcionário —
> as exceções abaixo precisam ser tratadas via override mensal em `banco_horas`
> e ignoradas pelo agente RH no Monitor Ponto Semanal.

---

## Leonardo Basseto (Analista Amazon, +5519999106834)

**Início:** semana de 27/04/2026
**Email:** leonardoctparticular@gmail.com
**User ID:** `cc60cb90-1616-4366-8b3d-7967696c966d`

### Acordo de jornada
- **Dias normais:** entrada 07:00 / saída 16:30 (jornada 8h30 — igual aos outros)
- **Dias de faculdade:** entrada 06:30 / saída 16:00 (compensação simétrica — jornada 8h30 mantida)

### Dias da semana de faculdade
⏳ A confirmar pelo Leonardo via WhatsApp na resposta da mensagem inaugural (30/04/2026).

### Como o agente RH deve tratar
- Entrada às 06:30 NÃO é "atraso de saída" nem nada — é jornada acordada
- Saída às 16:00 nos dias de faculdade NÃO é "saída antecipada" (TIPO C)
- Tolerância de 10min vale a partir do horário acordado: 07:10 (dia normal) ou 06:40 (dia faculdade)

### Override no banco de horas
Não é necessário — a jornada efetiva bate com a contratual (8h30). O cálculo dinâmico funciona corretamente.

---

## Mateus Eduardo Lisboa Santos (+5519997752572)

**Início do regime especial:** 01/05/2026 (até término do Tiro de Guerra — confirmar com o Mateus a duração)
**Motivo:** Servindo Tiro de Guerra pela manhã na cidade

### Acordo de jornada
- **Entrada:** 08:30
- **Saída:** 17:00
- **Almoço:** 1h (qualquer horário entre 11:30-13:30)

### Jornada efetiva
- **Seg-Qui:** 7h30/dia (vs 8h30 padrão = -1h/dia)
- **Sex:** 7h30 (vs 8h padrão = -30min)
- **Mês típico (~22 dias úteis):** ~18h a menos que a jornada padrão

### Como o agente RH deve tratar
- Entrada após 07:10 mas até 08:40 NÃO é atraso (tolerância: 08:30 + 10min)
- Saída após 16:30 NÃO é hora extra automática até 17:00 (é o horário acordado)
- Saída APÓS 17:00 SIM é hora extra real (autorizada pelo Pedro caso a caso)

### Override no banco de horas (OBRIGATÓRIO mensal)

**Sem override**, o Mateus ficaria com saldo do mês ~-24h (apenas zerado pelo sistema), e qualquer extra real seria "consumido" pelo déficit estrutural antes de virar saldo positivo. **Injusto.**

**Com override**, o saldo dele reflete apenas a operação real (extras reais + bônus - 10h débito padrão), igual aos outros. Isso é o que torna a jornada reduzida acordada compatível com o sistema.

**Quando criar:** dia 31 do mês corrente OU dia 1 do mês seguinte ANTES das 00:00 (antes do cron `reset-banco-horas` rodar).

**Como criar:**
```bash
python3 ~/segundo-cerebro/automacoes/scripts/mateus-override-mensal.py YYYY-MM
```

(Script criado em [[automacoes/sops/mateus-override-mensal-sop]])

---

## Notas relacionadas

- [[openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo|Regras Ponto Certo]] — base normal
- [[openclaw/agents/kobe/shared/rh/knowledge/politica-sabado-trabalhado|Política Sábado]]
- [[memory/context/people|People]] — números de WhatsApp
- [[automacoes/sops/mateus-override-mensal-sop|SOP Override Mateus]]

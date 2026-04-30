---
title: "SOP — Override mensal banco de horas Mateus"
type: sop
created: 2026-04-30
updated: 2026-04-30
status: active
tags:
  - sop
  - rh
  - ponto-certo
  - mateus
  - banco-horas
---

# SOP — Override mensal banco de horas Mateus

> Operacionaliza a regra acordada de "jornada reduzida durante Tiro de Guerra"
> sem prejuízo no banco de horas. Documento canônico:
> [[openclaw/agents/kobe/shared/rh/knowledge/jornadas-individuais|Jornadas Individuais]]

---

## Contexto

Mateus E. L. Santos serve o Tiro de Guerra pela manhã (a partir de 04/05/2026). Por isso opera com jornada reduzida (08:30-17:00 → 7h30/dia em vez de 8h30 padrão Seg-Qui).

Sem intervenção, o sistema do Ponto Certo calcularia déficit estrutural de ~18h/mês pra ele, o que (1) é zerado no fechamento por regra defensiva do sistema, mas (2) faz com que extras reais que ele eventualmente faça sejam consumidos pelo déficit antes de virar saldo positivo. **Injusto.**

A solução é criar um override em `banco_horas` que neutraliza esse déficit, deixando o saldo dele refletir só extras reais + bônus - 10h débito padrão (igual aos outros).

---

## Quando rodar

**Dia 31 do mês corrente** OU **dia 1 do mês seguinte ANTES de 00:00 BRT**.

O cron `reset-banco-horas` do sistema roda no dia 1 a partir das 00:00. Se o override já estiver gravado quando o cron rodar, o sistema usa o override em vez de recalcular dinamicamente.

---

## Como rodar

```bash
# Pra mês específico:
python3 ~/segundo-cerebro/automacoes/scripts/mateus-override-mensal.py 2026-05

# Pra mês corrente:
python3 ~/segundo-cerebro/automacoes/scripts/mateus-override-mensal.py

# Dry-run (calcula mas não grava):
python3 ~/segundo-cerebro/automacoes/scripts/mateus-override-mensal.py 2026-05 --dry-run
```

O script:
1. Lê todas as batidas do Mateus do mês
2. Calcula tempo real trabalhado (clock_out - clock_in - intervalo)
3. Calcula a "jornada acordada" do mês (dias úteis × 7h30)
4. Calcula o "déficit estrutural" (jornada padrão - jornada acordada)
5. Define `horas_extras_override = (extras vs acordada) + (déficit estrutural)`
6. Insere/atualiza registro em `banco_horas` com `mes_referencia` = primeiro dia do mês

---

## Quando parar de rodar

Quando o Mateus terminar o Tiro de Guerra e voltar à jornada padrão (07:00-16:30 Seg-Qui / 07:00-16:00 Sex). Confirmar com o Mateus a duração estimada do serviço militar.

Quando isso acontecer:
1. Remover este SOP do calendário
2. Atualizar [[openclaw/agents/kobe/shared/rh/knowledge/jornadas-individuais]] com a data de término
3. Voltar a deixar o cálculo dinâmico operar normal

---

## Validação pós-execução

Após rodar o script, validar via função SQL `calcular_banco_horas_mes`:

```bash
curl -s -X POST "https://dgldsmhbeosjgfrbegyv.supabase.co/rest/v1/rpc/calcular_banco_horas_mes" \
  -H "apikey: $SR" -H "Authorization: Bearer $SR" \
  -H "Content-Type: application/json" \
  -d '{"p_user_id":"1edae654-065c-4d3d-8516-ca5267d2a47b","p_mes":"2026-05-01"}'
```

Resultado esperado: `horas_extras_mes` reflete o valor do override e `saldo_atual` faz sentido (próximo de zero ou positivo se ele fez extras reais).

---

## Notas relacionadas

- [[openclaw/agents/kobe/shared/rh/knowledge/jornadas-individuais]] — política
- [[openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo]] — regras gerais
- [[memory/context/deadlines]] — lembretes mensais

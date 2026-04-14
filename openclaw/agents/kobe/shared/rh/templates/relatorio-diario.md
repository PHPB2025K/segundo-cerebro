---
title: "relatorio diario"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# 📋 Relatório de Ponto — {DATA}

## Resumo
- ✅ No horário: {COUNT_OK}
- ⏰ Atrasados: {COUNT_ATRASO}
- ❌ Ausentes: {COUNT_FALTA}
- 📝 Justificativas pendentes: {COUNT_PENDENTE}

## Detalhamento

### ✅ No horário
{LISTA_OK}

### ⏰ Atrasos
| Funcionário | Entrada | Atraso |
|-------------|---------|--------|
{LISTA_ATRASOS}

### ❌ Ausências
| Funcionário | Tipo | Justificativa |
|-------------|------|---------------|
{LISTA_FALTAS}

### 📝 Solicitações pendentes
{LISTA_PENDENTES}

---
_Gerado automaticamente pelo Agente RH via Ponto Certo_

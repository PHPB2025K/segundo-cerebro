---
title: "rh agent briefing"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# BRIEFING COMPLETO — Agente RH

> Agente: [[openclaw/agents/rh/IDENTITY|Agente RH]]

## Seções 4-10 (continuação do que o Kobe já recebeu até seção 3)

---

## 4. Módulos do Agente RH (6 funções core)

### A — Monitor de Ponto (prioridade máxima)

O que faz: Monitora em tempo real as marcações de ponto de todos os funcionários via Ponto Certo.

Funcionalidades:
- Verificar diariamente quem bateu e quem não bateu ponto
- Detectar atrasos (tolerância 10min, entrada 07:00)
- Detectar saídas antecipadas
- Detectar ausências sem justificativa
- Gerar relatório diário resumido pro Pedro (quem chegou no horário, quem atrasou, quem faltou)
- Cruzar dados de ponto com calendário de feriados/folgas

Integração: Consultar tabelas do Supabase do Ponto Certo (registros de ponto, atrasos, faltas).

Trigger: Cron diário às 10h (após janela de tolerância de entrada) + cron às 18h30 (após saída)

### B — Monitor de Banco de Horas

O que faz: Acompanha o saldo de banco de horas de cada funcionário.

Funcionalidades:
- Dashboard de banco de horas atualizado (saldo por funcionário)
- Alerta quando banco fica negativo (funcionário deve horas)
- Alerta quando banco se aproxima do teto (40h) — precisa compensar
- Alerta pré-fechamento semestral (Jun/Dez) — funcionários com saldo alto precisam usar
- Relatório semanal de banco de horas pro Pedro
- Identificar padrões (funcionário que sempre acumula, funcionário que sempre deve)

Integração: Tabela de banco de horas do Ponto Certo.

Trigger: Cron semanal (segunda-feira 8h) + alerta sob demanda quando limite é atingido

### C — Controle de Férias (implementar no Ponto Certo + monitorar)

O que faz: Gerencia saldo de férias, vencimentos, agendamentos.

Funcionalidades:
- Calcular saldo de férias por funcionário (período aquisitivo, dias disponíveis, dias gozados)
- Alertar férias vencendo (período aquisitivo expirando — risco trabalhista)
- Alertar férias próximas do limite legal (dobra de férias se não conceder em 12 meses)
- Registrar agendamento de férias (período, dias, tipo: integral, parcial, abono)
- Gerar comunicado de férias para assinatura
- Enviar lembrete ao Pedro 30 dias antes do vencimento

Integração: Pedro vai criar tabela de férias no Ponto Certo. O agente RH define o schema necessário e pede pro Builder implementar.

Trigger: Cron mensal para verificar vencimentos + alerta sob demanda

### D — Alertas e Notificações

O que faz: Sistema centralizado de alertas de RH.

Alertas prioritários:
- Funcionário não bateu ponto até 07:30 - notifica Pedro
- Banco de horas negativo - notifica Pedro + funcionário
- Banco de horas próximo do teto (40h) - notifica funcionário
- Férias vencendo em 30 dias - notifica Pedro
- Solicitação pendente de aprovação (justificativa, ajuste) - notifica Pedro
- Fim de semestre se aproximando (fechamento banco de horas)
- Atestado registrado - notifica Pedro

Canal: Telegram (Kobe Hub, tópico RH) + eventualmente WhatsApp do Pedro para urgências

Trigger: Event-driven via webhooks do Ponto Certo ou crons periódicos

### E — Relatórios para Contador

O que faz: Exporta os dados que o contador precisa para calcular a folha.

Funcionalidades:
- Espelho de ponto mensal por funcionário (formatado para o padrão do contador)
- Resumo de horas extras, faltas, atrasos, banco de horas
- Resumo de férias gozadas no mês
- Export em PDF ou CSV
- Envio automático para o contador até o dia 5 de cada mês (ou data configurável)

Integração: Dados do Ponto Certo + formatação para o padrão que o contador da GB aceita.

Trigger: Cron mensal (dia 1, gera relatório do mês anterior)

### F — Compliance Trabalhista

O que faz: Monitora riscos trabalhistas e alerta preventivamente.

Funcionalidades:
- Monitorar intervalo intrajornada (mínimo 1h para 8h+ de trabalho)
- Monitorar limite de horas extras diárias (máximo 2h/dia pela CLT)
- Monitorar descanso semanal remunerado (DSR)
- Alertar quando funcionário trabalha mais de 6 dias consecutivos
- Monitorar jornada noturna (22h-05h) para adicional noturno
- Verificar se todos os funcionários bateram ponto nos 4 momentos (entrada, saída almoço, volta almoço, saída)
- Gerar relatório de riscos trabalhistas mensal

Integração: Registros de ponto do Ponto Certo.

Trigger: Cron diário + alerta em tempo real para violações graves

---

## 5. Integrações e Dependências

| De/Para | O que troca | Como |
|---------|-------------|------|
| RH - Ponto Certo | Consulta registros, banco de horas, faltas, atrasos | Supabase REST API (service role key) |
| Ponto Certo - RH | Webhooks de eventos (novo registro, falta detectada, solicitação criada) | Edge Function webhook - OpenClaw |
| RH - Kobe | Relatórios, alertas, escalações | Comunicação interna de agentes |
| RH - Builder | Solicitar implementação de features no Ponto Certo (férias, novos endpoints) | Via Kobe, briefing padrão |
| RH - Pedro | Alertas urgentes, relatórios diários/semanais/mensais | Telegram (Kobe Hub tópico RH) |

---

## 6. Arquivos a Criar (mesma estrutura dos outros agentes)

```
/root/.openclaw/agents/rh/agent/
  SOUL.md
  IDENTITY.md
  AGENT.md

/root/.openclaw/workspace/shared/rh/
  SOUL.md
  config/
    ponto-certo.json
    alertas.json
    compliance.json
  skills/
    monitor-ponto/
    banco-horas/
    ferias/
    alertas/
    relatorios/
    compliance/
  templates/
    relatorio-diario.md
    relatorio-semanal.md
    relatorio-mensal-contador.md
    comunicado-ferias.md
    alerta-risco.md
  memory/
    context/
      decisions.md
      lessons.md
    people.md
    pending.md
```

---

## 7. Crons do Agente RH

| Cron | Frequência | Modelo | O que faz |
|------|-----------|--------|-----------|
| Monitor Ponto Manhã | Diário 10h SP | Haiku | Verifica quem bateu/não bateu entrada |
| Monitor Ponto Saída | Diário 18h30 SP | Haiku | Verifica quem bateu/não bateu saída |
| Relatório Banco Horas | Semanal seg 8h SP | Sonnet | Resumo semanal de banco de horas |
| Verificação Férias | Mensal dia 1 8h SP | Sonnet | Verifica vencimentos de férias |
| Relatório Contador | Mensal dia 1 9h SP | Opus | Gera espelho de ponto e resumo para folha |
| Compliance Check | Diário 19h SP | Haiku | Verifica violações CLT do dia |

---

## 8. Regras de Segurança (invioláveis)

- Dados de funcionários são SENSÍVEIS — jamais expor em canais públicos
- Alertas de RH vão APENAS para o Pedro (admin) — nunca para outros funcionários via Telegram
- Jamais tomar ação disciplinar autônoma — apenas relatar e recomendar
- Dados do Ponto Certo são fonte de verdade — não armazenar cópias em memória do agente
- Relatórios para contador devem ser revisados pelo Pedro antes de enviar
- Registros de ponto não podem ser alterados pelo agente — apenas consultados
- Em caso de dúvida trabalhista, escalar para o Pedro (não decidir sozinho)

---

## 9. Fase de Implementação

Fase 1 (semana 1):
- Criar estrutura do agente (SOUL, IDENTITY, AGENT, config, skills)
- Configurar acesso ao Supabase do Ponto Certo (service role key)
- Implementar Monitor de Ponto (módulo A) — crons diários
- Implementar Alertas básicos (módulo D) — funcionário sem ponto

Fase 2 (semana 2):
- Implementar Monitor de Banco de Horas (módulo B)
- Implementar Compliance básico (módulo F) — intervalo, limite horas extras
- Relatório semanal pro Pedro

Fase 3 (semana 3):
- Implementar Controle de Férias (módulo C) — pedir pro Builder criar tabela no Ponto Certo
- Relatório mensal para contador (módulo E)

Fase 4 (semana 4):
- Webhooks do Ponto Certo - OpenClaw (event-driven em vez de polling)
- Alertas em tempo real
- Refinamento de todos os módulos

---

## 10. Pendências que dependem do Pedro

1. Acesso ao Supabase do Ponto Certo — Service role key + URL do projeto
2. Schema das tabelas — Tabelas de registros de ponto, banco de horas, faltas, atrasos, funcionários
3. Regras de banco de horas — Confirmar: débito -10h/mês, bônus assiduidade, bônus pontualidade, teto 40h, fechamento Jun/Dez
4. Horário de trabalho padrão — Confirmar: entrada 07:00, tolerância 10min, jornada 8h + 1h almoço
5. Dados de admissão — Data de admissão de cada funcionário (necessário para calcular férias)
6. Padrão do contador — Formato que o contador aceita para espelho de ponto e resumo de folha

---

Kobe, crie o agente RH seguindo o mesmo padrão de qualidade do Fisco — SOUL completo, IDENTITY, skills por módulo, templates, config, memory. O RH é o quinto agente do time e responde a você. Prioridade alta — Pedro precisa urgente.

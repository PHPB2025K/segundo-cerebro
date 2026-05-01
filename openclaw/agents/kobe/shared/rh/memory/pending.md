# Pendências — Agente [[agents/rh/IDENTITY|RH]]

_Atualizado: 2026-04-30_

## 🔴 Imediato
- [ ] Deploy produção do módulo Conversas RH se ainda estiver apenas local.
- [ ] Acompanhar feedback da Yasmin sobre recebimento dos 2 chunks da mensagem inaugural.
- [ ] Acompanhar primeiras respostas dos funcionários às mensagens inaugurais.
- [ ] Monitor Ponto Semanal real em 04/05 10h BRT com `rh-poller` e `rh-stuck-detector` ativos.

## Dados pendentes do Pedro / Contador
- [ ] **Datas de admissão** — de cada funcionário (necessário para cálculo de férias).
- [ ] **Padrão do contador FOUR/Suellen** — formato aceito para espelho de ponto.

## Fase 1
- [x] Criar estrutura do agente (SOUL, IDENTITY, AGENT, config, skills, templates, memory).
- [x] Supabase do Ponto Certo configurado e testado.
- [x] WhatsApp do RH configurado — instância `RECURSOS HUMANOS GB`.
- [x] Mensagens inaugurais enviadas para 8 funcionários.
- [x] `rh-poller` implementado.
- [x] `rh-stuck-detector` implementado.
- [x] Módulo Conversas RH implementado no admin.
- [ ] Criar tópico RH no Kobe Hub (Telegram), se ainda não existir.
- [ ] Revisar crons finais: Monitor Ponto Manhã (10h), Saída (18h30), Compliance (19h).

## Fase 2
- [ ] Skill banco-horas (módulo B).
- [ ] Skill compliance básico (módulo F) — intervalo, limite horas extras.
- [ ] Cron semanal banco de horas (segunda 8h).
- [ ] Relatório semanal pro Pedro.

## Fase 3
- [ ] Definir schema tabela de férias → Builder implementar no Ponto Certo.
- [ ] Skill ferias (módulo C).
- [ ] Skill relatorios — relatório mensal pra contador (módulo E).

## Fase 4
- [ ] Webhooks Ponto Certo → OpenClaw (event-driven).
- [ ] Alertas em tempo real.
- [ ] Refinamento de todos os módulos.

# Pendências — Agente [[agents/rh/IDENTITY|RH]]

## ✅ Resolvido pelo Pedro
1. [x] **Supabase do Ponto Certo** — Configurado em config/ponto-certo.json (status 200)
2. [x] **Schema das tabelas** — Documentado em knowledge/regras-ponto-certo.md seção 7
3. [x] **Regras de banco de horas** — Completo no Knowledge File (débito -10h, bônus 2h+2h, teto 40h, fechamento Jun/Dez)
4. [x] **Horário de trabalho** — Seg-Qui 8h30 (07:00-16:30), Sex 8h (07:00-16:00), tolerância 10min
5. [ ] **Datas de admissão** — De cada funcionário (necessário p/ cálculo de férias)
6. [ ] **Padrão do contador** — Formato que o contador (FOUR/Suellen) aceita para espelho de ponto
7. [x] **WhatsApp do RH** — Instância "RECURSOS HUMANOS GB" na Evolution API (5519992997273)

## Fase 1 (semana 1)
- [x] Criar estrutura do agente (SOUL, IDENTITY, AGENT, config, skills, templates, memory)
- [x] Pedro preencher credenciais Supabase do Ponto Certo em `config/ponto-certo.json`
- [x] WhatsApp do RH configurado — config/whatsapp.json
- [ ] Implementar skill monitor-ponto (módulo A)
- [ ] Implementar skill alertas básicos (módulo D)
- [ ] Criar tópico RH no Kobe Hub (Telegram)
- [ ] Configurar crons: Monitor Ponto Manhã (10h) + Saída (18h30) + Compliance (19h)
- [x] Testar acesso ao Supabase do Ponto Certo (listar funcionários, registros — OK)

## Fase 2 (semana 2)
- [ ] Skill banco-horas (módulo B)
- [ ] Skill compliance básico (módulo F) — intervalo, limite horas extras
- [ ] Cron semanal banco de horas (segunda 8h)
- [ ] Relatório semanal pro Pedro

## Fase 3 (semana 3)
- [ ] Definir schema tabela de férias → Builder implementar no Ponto Certo
- [ ] Skill ferias (módulo C)
- [ ] Skill relatorios — relatório mensal pra contador (módulo E)

## Fase 4 (semana 4)
- [ ] Webhooks Ponto Certo → OpenClaw (event-driven)
- [ ] Alertas em tempo real
- [ ] Refinamento de todos os módulos

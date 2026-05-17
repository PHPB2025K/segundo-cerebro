# Lições — Fisco

_Atualizado: 2026-05-16_

## 2026-05-16
- Repetição do HTTP 403 da Filial em todas as execuções observadas confirma bloqueio persistente de cadastro/vínculo/token; não tratar como oscilação de API.
- Alerta WhatsApp do refresh falhou junto com o problema principal em todas as execuções observadas do dia, reduzindo capacidade de notificação automática.

## 2026-05-15
- Cron fiscal não pode depender de aprovação interativa: quando a política de execução bloqueia comandos, o refresh Bling falha antes de validar Matriz/Filial.
- Erro recorrente HTTP 403 de Filial inativa no Bling deve ser tratado como bloqueio operacional, não instabilidade temporária; sem Filial ativa, fluxos de NF interna Filial → Simples ficam indisponíveis.
- Alerta WhatsApp também retornou HTTP 403 em pelo menos uma execução; falha de alerta não deve mascarar falha principal do refresh.

# Lições — Fisco

_Atualizado: 2026-05-15_

## 2026-05-15
- Cron fiscal não pode depender de aprovação interativa: quando a política de execução bloqueia comandos, o refresh Bling falha antes de validar Matriz/Filial.
- Erro recorrente HTTP 403 de Filial inativa no Bling deve ser tratado como bloqueio operacional, não instabilidade temporária; sem Filial ativa, fluxos de NF interna Filial → Simples ficam indisponíveis.
- Alerta WhatsApp também retornou HTTP 403 em pelo menos uma execução; falha de alerta não deve mascarar falha principal do refresh.

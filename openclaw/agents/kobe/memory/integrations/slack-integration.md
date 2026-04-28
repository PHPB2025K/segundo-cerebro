# Slack Integration — GB Importadora

_Atualizado: 2026-04-26_

## Status
- **Workspace:** GB Importadora
- **Tipo de acesso:** User OAuth Token read-only
- **Usuário autenticado:** tradesup.co
- **Team ID:** T03V1KHCPN1
- **User ID:** U03UY0UNLDC
- **Credencial:** 1Password → Vault `OpenClaw` → item `Slack Pedro Read Only` → campo `token`
- **Helper local:** `scripts/slack-read.py`
- **Status validado:** ✅ `auth.test` OK e `conversations.list` OK em 2026-04-26

## Escopo esperado
A integração foi criada para leitura de Slack, não envio.

Scopes configurados pelo Pedro no Slack App:
- `channels:read`
- `channels:history`
- `groups:read`
- `groups:history`
- `im:read`
- `im:history`
- `mpim:read`
- `mpim:history`
- `users:read`
- `search:read`

## Uso permitido
- Ler e resumir conversas/canais quando Pedro pedir.
- Buscar mensagens por contato, canal, termo ou período.
- Identificar pendências e decisões em conversas do Slack.

## Regras
- NUNCA exibir token em chat, logs ou arquivos.
- NUNCA enviar mensagem no Slack sem autorização explícita do Pedro e sem implementar escopo próprio de envio.
- Tratar DMs e canais privados como dados sensíveis: resumir só o necessário.
- Se encontrar dados sensíveis, não persistir em memória.

## Helper
Comandos internos disponíveis:
- `python3 scripts/slack-read.py auth`
- `python3 scripts/slack-read.py list --limit 100`
- `python3 scripts/slack-read.py search "termo" --limit 20`
- `python3 scripts/slack-read.py history <channel_id> --days 7 --limit 100`

## Observação de segurança
Durante a configuração, um bot token `xoxb-...` apareceu em screenshot no Telegram. Recomendado rotacionar/reinstalar o app para invalidar o token exposto, mesmo que o acesso operacional esteja usando o user token `xoxp-...` salvo no 1Password.

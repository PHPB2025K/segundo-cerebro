---
title: "Vault Sync — launchd Mac (auto-pull 60s)"
created: 2026-04-28
type: automation
status: active
tags:
  - automacoes
  - vault
  - segundo-cerebro
  - launchd
  - mac
---

# Vault Sync — launchd Mac (auto-pull 60s)

Agente do macOS launchd que mantém o vault local (`~/segundo-cerebro/`) sincronizado com o GitHub a cada 60 segundos. Garante que tudo que o Kobe (na VPS) escreve fica visível no Obsidian/Mac quase em tempo real, e que toda escrita do Claude Code local sai em base atualizada.

## Componentes

- **Plist:** `~/Library/LaunchAgents/com.budamix.segundo-cerebro-pull.plist`
- **Comando executado:** `~/segundo-cerebro/meta/scripts/safe-write.sh sync` (lockfile mkdir + pull --rebase + abort em conflito)
- **Logs:** `/tmp/segundo-cerebro-pull.log`
- **Intervalo:** 60s (`StartInterval` no plist)
- **Disparo inicial:** `RunAtLoad=true` — pull imediato ao carregar/reboot

## Operação

```bash
# Status (PID se rodando, "0" = último OK, número = código erro)
launchctl list | grep segundo-cerebro

# Log ao vivo
tail -f /tmp/segundo-cerebro-pull.log

# Pausar
launchctl unload ~/Library/LaunchAgents/com.budamix.segundo-cerebro-pull.plist

# Reativar
launchctl load ~/Library/LaunchAgents/com.budamix.segundo-cerebro-pull.plist

# Mudar intervalo: editar StartInterval no plist, depois unload + load
```

## Por que safe-write.sh sync (e não git pull cru)

- Lockfile `mkdir` atômico em `/tmp/segundo-cerebro-local.lock.d` evita corrida com escritas do Claude Code que rodam ao mesmo tempo.
- Aborta limpo em conflito (exit 2) em vez de deixar o repo num estado feio.
- Funciona Mac+Linux (POSIX), simétrico com qualquer cron equivalente do VPS.

## Comportamento durante sleep do Mac

launchd não dispara timers durante sleep. Quando o Mac volta, o agente faz o primeiro pull em até 60s e segue normalmente. Sem perda de dados — apenas atraso natural enquanto offline.

## Ciclo completo de sincronização (estado atual — 28/04/2026)

1. Kobe escreve no vault VPS → cron `7,22,37,52 * * * *` push para GitHub (até 15min de latência)
2. Mac launchd pulla a cada 60s
3. Obsidian detecta mudança no FS e re-renderiza (instantâneo)

## Referências

- [[memory/sessions/2026-04-28]] — sessão que entregou o setup
- [[memory/context/decisoes/2026-04#[28/04] Vault como SSoT — Fase 4 concluída + protocolo Git seguro]]
- `meta/scripts/safe-write.sh` — script chamado pelo agente

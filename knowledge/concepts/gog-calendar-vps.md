---
title: "gog Calendar via VPS — operações"
created: 2026-04-22
type: reference
status: active
tags:
  - knowledge
  - config
  - calendar
  - oauth
  - gog
  - vps
---

# gog Calendar via VPS

Como escrever em Google Calendar (Gmail, Drive, Docs etc.) do Pedro programaticamente usando o CLI `gog` v0.12.0 no VPS OpenClaw.

## Credenciais e acesso

- **Binário:** `/usr/local/bin/gog` no VPS `root@187.77.237.231`
- **Config:** `/root/.config/gogcli/{config.json, credentials.json, keyring/}`
- **OAuth client:** `264539490125-bbsajvaomfjne0fv87inbigc5a71a6sv.apps.googleusercontent.com` (em `credentials.json`)
- **Keyring password:** 1Password vault OpenClaw, item `gog keyring password - VPS OpenClaw` (ID `nen2twtjadjec6lammpenfzvgm`). Persistido no `/root/.bashrc` como `GOG_KEYRING_PASSWORD`.

## Contas autorizadas (pós-reset 2026-04-22)

- `pehpbroglio@gmail.com` — full scopes (Calendar, Gmail, Drive, Docs, Sheets, Tasks, Chat, Classroom, Slides, Forms, Contacts, Apps Script)
- `gb.ai.agent@gbimportadora.com` (Tobias Agent) — **APAGADO NO RESET, precisa reautorizar** com `gog auth add gb.ai.agent@gbimportadora.com --remote --step=1`

## Calendários do Pedro (conta pessoal)

| Nome | ID | Uso |
|---|---|---|
| **Trabalho** | `u90rho3t0ttdg0dcbf914vmmbk@group.calendar.google.com` | Default para reuniões de negócio |
| Planejamento | `f3f39ioouai4e5d0ljne137c1g@group.calendar.google.com` | — |
| Casa (primary) | `pehpbroglio@gmail.com` | — |
| Treino | `pljhd79mr8l09kucv8jh50kje8@group.calendar.google.com` | — |
| Dieta | `iki7r2esfr0c3okb17t96db7qc@group.calendar.google.com` | — |
| Meditação | `olbqqqglkk59aiv07engv0mmsk@group.calendar.google.com` | — |
| Feriados no Brasil | `pt-br.brazilian#holiday@group.v.calendar.google.com` | Read-only |

## Padrão — criar evento

```bash
ssh root@187.77.237.231 bash <<'EOF'
export GOG_KEYRING_PASSWORD='<do 1P>'
CAL='u90rho3t0ttdg0dcbf914vmmbk@group.calendar.google.com'

gog -a pehpbroglio@gmail.com calendar create "$CAL" \
  --summary "Título" \
  --from "2026-MM-DDT14:30:00-03:00" --to "2026-MM-DDT15:30:00-03:00" \
  --description "..." --location "Escritório Budamix — Pedreira-SP" \
  --attendees "email1,email2" \
  --with-meet \
  --send-updates all \
  --reminder popup:30m --reminder popup:15m
EOF
```

## Padrão — listar / buscar / deletar

```bash
# Listar eventos de um dia
gog -a pehpbroglio@gmail.com calendar events --cal "$CAL" --from 2026-04-22 --to 2026-04-23

# Listar em todos os calendários do dia
gog -a pehpbroglio@gmail.com -j calendar events --all --from 2026-04-22 --to 2026-04-23 --max 200

# Buscar eventos por texto
gog -a pehpbroglio@gmail.com calendar search "Leonardo" --max 5

# Deletar evento
gog -a pehpbroglio@gmail.com calendar delete "$CAL" <eventId> --send-updates none --force

# Deletar instância de recorrência (usar ID com sufixo _YYYYMMDDTHHMMSSZ)
gog -a pehpbroglio@gmail.com calendar delete "$CAL" "base_20260422T170000Z" --force
```

## Flags importantes

| Flag | Efeito |
|---|---|
| `--with-meet` | Cria Google Meet video conference |
| `--send-updates all\|externalOnly\|none` | **Default é `none`** — convites não saem sem isso |
| `--reminder popup:30m` | Pode ser repetido (max 5), formatos `popup:Xm`, `email:Xd` |
| `--remote --step=1` | OAuth flow: imprime URL (abre no browser do lado do usuário) |
| `--remote --step=2 --auth-url <redirect-url>` | Troca código pelo refresh token |
| `-j` | Output JSON (antes do subcommand) |
| `--results-only` | JSON sem envelope (só o result primário) |

## Gotchas

- **`gog calendar events create` NÃO existe** — o comando é `gog calendar create` (sem `events`). Quem tenta `events create` cai no help de `list`.
- **Keyring password obrigatório em subshells** — `ssh root@... bash <<EOF` não herda do `.bashrc`. Exportar `GOG_KEYRING_PASSWORD` explicitamente dentro do heredoc.
- **Reset do keyring = perda de todos os tokens** — não é possível recuperar sem a senha antiga. Backup em `/root/.config/gogcli/keyring.bak.YYYYMMDD_HHMMSS` fica com tokens cifrados, requer senha antiga pra decriptar.
- **Validation do JSON em criação** — `--select "id,htmlLink"` retorna `{}` vazio em alguns casos. Pra ter certeza que criou, listar eventos do dia depois OU fazer `calendar event <cal> <id>` com `-j --results-only` pra ver detalhes completos (hangoutLink, htmlLink, attendees).
- **App "não verificado"** no OAuth flow — é projeto GCP próprio, Pedro clica "Avançado → Acessar". Seguro.
- **Redirect URL localhost:46249 falha** — esperado; copiar URL completa da barra mesmo com erro.
- **Scopes completos** — `credentials.json` atual pede tudo (Gmail, Drive, Chat, Classroom, Forms etc.). Pra reduzir escopo precisa editar `credentials.json` antes do OAuth.

## Histórico

- **2026-04-22:** reset do keyring, senha nova gerada com `openssl rand -base64 24`. Reautorizado `pehpbroglio@gmail.com` via `--remote --step=1/2`. Tobias Agent apagado no reset, precisa reautorizar.

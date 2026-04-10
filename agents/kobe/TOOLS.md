# TOOLS.md — Infraestrutura e Dispositivos

_Notas específicas do setup do Pedro/Kobe. Skills definem como as ferramentas funcionam; este arquivo registra o que é único deste ambiente._

---

## VPS
- **Hostname:** srv1480018
- **OS:** Ubuntu 24.04.4 LTS
- **IP:** 187.77.237.231
- **SSH:** `ssh root@187.77.237.231`
- **Disco:** 47.39GB (~43.5% usado em 23/03/2026)
- **Memória:** 49% uso
- **OpenClaw:** v2026.3.13 (61d171a)
- **Node.js:** v22.22.1

## Gateway
- **Bind:** loopback (127.0.0.1), porta 18789
- **Dashboard (via túnel):** `ssh -N -L 18789:127.0.0.1:18789 root@187.77.237.231` → `http://localhost:18789/`
- **Service file:** `~/.config/systemd/user/openclaw-gateway.service`

## Hardware do Pedro
- MacBook Pro M1 com 2 telas externas
- macOS (Apple Silicon / ARM64)
- Nespresso ☕

## WhatsApp Store
- **Path:** `/root/.openclaw/whatsapp-store/`
- **Credenciais:** `creds.json` (QR code linkado)
- **Número:** +55 19 99304-0768
- **JID:** `5519993040768:56@s.whatsapp.net`

## Paths Importantes
| O quê | Path |
|-------|------|
| Config principal | `~/.openclaw/openclaw.json` |
| Workspace | `~/.openclaw/workspace/` |
| Memória | `~/.openclaw/workspace/memory/` |
| Skills | `~/.openclaw/workspace/skills/` |
| Shared (agentes) | `~/.openclaw/workspace/shared/` |
| Logs | `/tmp/openclaw/openclaw-YYYY-MM-DD.log` |
| Cron jobs | `~/.openclaw/cron/jobs.json` |
| WhatsApp store | `/root/.openclaw/whatsapp-store/` |
| Media inbound | `/root/.openclaw/media/inbound/` |
| Gmail signature Pedro | `/root/.openclaw/.gmail-signature-pedro.html` |
| gog config | `~/.config/gogcli/` |
| AWS credentials | `~/.aws/` |

## Envio de Arquivos via Telegram
- **Método:** sendDocument da Bot API via curl (multipart/form-data)
- **Suporta:** qualquer tipo de arquivo (.md, .pdf, .json, .csv, .xlsx, .png, etc.)
- **Limite:** até 50MB por arquivo
- **Como:** `curl -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendDocument" -F "chat_id=${CHAT_ID}" -F "message_thread_id=${TOPIC_ID}" -F "document=@${FILE_PATH}" -F "caption=descrição"`
- **Quando usar:** SEMPRE que Pedro pedir arquivo, relatório, briefing, export ou qualquer entregável que não seja texto corrido curto
- **REGRA:** Nunca fatiar documento em mensagens de texto. Se é arquivo, manda como arquivo.
- **Bot Token:** em openclaw.json (telegram.botToken)
- **Chat IDs:** ver memory/integrations/telegram-map.md

## Segurança
- **UFW:** ativo — portas 22 (SSH), 80 (Traefik HTTP), 443 (Traefik HTTPS), 8084 (Evolution API)
- **Fail2ban:** ativo (maxretry=5, bantime=3600)
- **SSH:** PermitRootLogin prohibit-password, PasswordAuthentication no, key ed25519
- **Gateway:** loopback only (não exposto na internet)
- **Credenciais:** 1Password vault "OpenClaw"

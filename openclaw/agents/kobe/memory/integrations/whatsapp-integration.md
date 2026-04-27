---
title: "whatsapp-integration"
created: 2026-04-26
type: memory-integration
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - integration
---
# WhatsApp Integration — Status e Regras

_Atualizado: 2026-03-25_

---

## ⛔ Incidente 2026-03-25
- OpenClaw respondeu automaticamente Alexandre Novaes (+5519997978437) via módulo web-auto-reply
- Causa: dmPolicy estava "open", ativando auto-reply automático
- Correção: dmPolicy e groupPolicy voltaram para "allowlist". Gateway reiniciado.
- Regra INVIOLÁVEL registrada em decisions.md

---

## Arquitetura Definitiva (3 canais)

### Canal 1 — Número do Kobe (ENVIO PRINCIPAL)
| Campo | Valor |
|---|---|
| Número | +55 19 99845-8149 |
| Instância Evolution | WHATSAPP PRÓPRIO KOBE |
| Instance ID | af2e881f-265b-417d-885a-7516f3174ee6 |
| URL | https://trottingtuna-evolution.cloudfy.live |
| API Key | 1Password → "Evolution API Cloudfy - WhatsApp Kobe" |
| Status | ✅ connected |

**Uso:**
- Enviar mensagem pro Pedro → este canal
- Enviar mensagem para terceiros (quando Pedro autorizar) → este canal
- Identidade: Kobe / Assistente do Pedro (NUNCA se passar pelo Pedro neste número)

### Canal 2 — Número do Pedro via Evolution API (LEITURA + ENVIO COMO PEDRO)
| Campo | Valor |
|---|---|
| Número | +55 19 99304-0768 |
| Instância Evolution | WHATSAPP PESSOAL PEDRO |
| URL | https://trottingtuna-evolution.cloudfy.live |
| API Key | 1Password → "Evolution API Cloudfy" |
| Database | PostgreSQL, 41k+ mensagens, 900 chats |
| Status | ✅ connected |

**Uso:**
- Ler histórico de qualquer conversa do Pedro → este canal
- Enviar como Pedro (quando ele pedir explicitamente e aprovar o texto) → este canal
- SEMPRE com aprovação prévia do texto antes de enviar

### Canal 3 — Número do Pedro via OpenClaw/Baileys (LEITURA PASSIVA INBOUND)
| Campo | Valor |
|---|---|
| Número | +55 19 99304-0768 |
| dmPolicy | allowlist (só número do Pedro) |
| groupPolicy | allowlist |
| Status | ✅ leitura passiva |

**Uso:**
- APENAS receber mensagens inbound passivamente
- NUNCA enviar por este canal
- NUNCA abrir dmPolicy "open" (auto-reply dispara sozinho)

---

## Regras INVIOLÁVEIS
1. OpenClaw/Baileys = APENAS leitura passiva. NUNCA dmPolicy "open"
2. NUNCA alterar dmPolicy sem autorização explícita do Pedro
3. Envio como Kobe → instância "WHATSAPP PRÓPRIO KOBE"
4. Envio como Pedro → instância "WHATSAPP PESSOAL PEDRO", SEMPRE com aprovação
5. Leitura de histórico → instância "WHATSAPP PESSOAL PEDRO" (PostgreSQL)
6. Dados sensíveis NUNCA armazenados em memória
7. No número do Kobe: identidade = Kobe/Assistente do Pedro, NUNCA se passar pelo Pedro
8. No número do Pedro: identidade = Pedro, NUNCA se identificar como Kobe/IA


## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — agente proprietário
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis
- [[memory/context/business-context]] — contexto operacional
- [[projects/whatsapp-api]] — referência canônica detectada no conteúdo

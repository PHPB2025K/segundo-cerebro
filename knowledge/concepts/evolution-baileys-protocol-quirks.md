---
title: "Evolution v2 + Baileys — quirks de protocolo em mensagens interativas"
created: 2026-04-30
type: concept
status: active
tags:
  - knowledge
  - whatsapp
  - evolution
  - baileys
  - protocolo
---

# Evolution v2 + Baileys — quirks de protocolo em mensagens interativas

> Aprendizado da sessão Canggu de 30/04/2026: nem toda feature do WhatsApp
> que a Evolution expõe via API funciona efetivamente no cliente. Tem buracos
> de protocolo entre Baileys (não-oficial) e o app WhatsApp atual.

## Contexto

Evolution API v2 usa **Baileys** por baixo — biblioteca não-oficial que se
conecta ao WhatsApp simulando um app de celular. É a forma mais barata de
ter um bot no WhatsApp sem migrar pra Cloud API oficial da Meta. Mas Baileys
depende de engenharia reversa do protocolo, e features novas do WhatsApp
quebram silenciosamente quando a versão do Baileys fica defasada.

## O que testamos em 30/04 (não funcionou)

### 1. `sendList` (listMessage)

- **Endpoint:** `POST /message/sendList/{instance}`
- **Comportamento:** Evolution retorna **HTTP 201** com payload contendo
  `messageType: "listMessage"` e id do WhatsApp. Aparenta sucesso completo.
- **No cliente:** apareceram **3 pontinhos de "digitando..."** por ~2
  segundos e depois sumiu. Mensagem nunca foi exibida.
- **Diagnóstico:** Baileys envia o frame mas o app do destinatário descarta.
  Provavelmente versão do schema interactive-message está fora de sync.
- **Quirks observados na construção do payload:**
  - `description` em rows não pode ser string vazia (Evolution responde
    "The description cannot be empty")
  - `footerText` é **obrigatório** no top-level (Evolution responde
    "instance requires property footerText")

### 2. `sendPoll` (pollCreationMessageV3)

- **Endpoint:** `POST /message/sendPoll/{instance}`
- **Payload:** `{ name, selectableCount, values: [string, ...] }`
- **Comportamento:** Evolution retorna **HTTP 201** com
  `messageType: "pollCreationMessageV3"` e `messageSecret` (chave de
  criptografia da enquete).
- **No cliente:** aparece **"AGUARDANDO MENSAGEM. ESSA AÇÃO PODE LEVAR
  ALGUNS INSTANTES"** — placeholder do WhatsApp pra mensagens que ele não
  consegue decifrar. Nunca resolve.
- **Diagnóstico:** o `messageSecret` que Baileys gera não bate com o que o
  WhatsApp espera, ou o formato V3 do payload está desatualizado. Polls
  oficiais do WhatsApp são funcionalidade nativa há anos, então não é
  problema de suporte do app — é Baileys.

## O que funciona

### `sendText` puro com numeração emoji

- Universal. 100% dos clientes WhatsApp renderizam texto.
- Cliente responde número (`1`, `2`, `3`…) ou palavra-chave.
- Detecção via regex no webhook é trivial.
- Único custo: cliente precisa digitar em vez de clicar.

Padrão usado no Canggu para origin poll (saber de qual canal o cliente veio):

```
Bem-vindo à Budamix! 👋

Antes de te ajudar, me conta de qual canal você está vindo?
Responda apenas com o número:

1️⃣ Mercado Livre
2️⃣ Shopee
3️⃣ Amazon
4️⃣ Site Budamix (budamix.com.br)
5️⃣ Outro
```

E no parsing, regex aceita `^\s*1[º°.)]?\s*$` OU `\bmercado\s*livre\b` —
cobre tanto número quanto palavra digitada solta.

### `sendButtons` (não testado em 30/04, mas histórico)

Similar ao `sendList` mas com até 3 botões. Mesmo risco de descarte
silencioso. Não testamos pra esse caso porque 3 opções não cabem o universo
"ML/Shopee/Amazon/Site/Outro".

## Recomendação operacional

**Default para qualquer fluxo interativo no WhatsApp via Evolution:**

1. Tentar **texto puro** primeiro. Confiável, universal, zero dependência de
   tipo de conta ou versão do app.
2. Se for absolutamente necessário botão clicável (por UX premium), aceitar
   que vai funcionar parcialmente (depende do cliente WhatsApp do
   destinatário) e ter fallback texto pronto.
3. Se a feature interativa for crítica pra negócio (ex: confirmação de
   compra, escolha de plano), **migrar pra WhatsApp Business Cloud API
   oficial** (Meta). Custo: $0.005-0.05 por conversa, aprovação de
   templates, 1-2 sem de migração. Mas tem SLA.

## Sinal de quando re-testar

Baileys recebe updates ~mensais. Re-testar `sendList` e `sendPoll` quando:

- A versão do Evolution v2 saltar (tag `v2.x → v2.y`)
- Baileys liberar release com mention de "interactive messages" ou "polls"
- Pedro pedir e tiver tempo livre

Pra testar rapidamente sem afetar produção: criar edge function `diag` com
endpoint `?test=sendlist` ou `?test=sendpoll`, mandar pro número de teste,
ver no app se chegou. (Padrão usado em 30/04, função foi deletada após uso.)

## Cross-refs

- [[memory/context/decisoes/2026-04#[30/04 tarde/noite] Canggu — pipeline edge function canônico + mídia visível + repo único]]
- [[memory/sessions/2026-04-30]] (seção "Maratona Canggu")
- [[projects/canggu/canggu]]

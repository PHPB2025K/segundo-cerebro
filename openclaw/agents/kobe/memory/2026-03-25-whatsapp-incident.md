---
title: "2026-03-25-whatsapp-incident"
created: 2026-04-26
type: memory
agent: kobe
status: active
tags:
 - agent/kobe
 - memory
---
# Session: 2026-03-25 14:01:18 UTC

- **Session Key**: agent:main:telegram:group:-1003730816228:topic:13
- **Session ID**: 617f82cc-76b8-48d6-87cd-faa35c9d2e60
- **Source**: telegram

## Conversation Summary

user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2278",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Wed 2026-03-25 13:24 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Olá Kobe
assistant: Fala Pedro! Tudo certo? 👊
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2282",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Wed 2026-03-25 13:27 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Kobe, o gateway crashou porque uma config do WhatsApp ficou inválida — já
 foi corrigido e está online. Agora o assunto urgente:

 ALERTA VERMELHO: o OpenClaw respondeu automaticamente o Alexandre Novaes
 (+5519997978437) no WhatsApp sem minha autorização. Foram pelo menos 3
 mensagens automáticas enviadas pelo módulo web-auto-reply. Isso aconteceu
 porque o dmPolicy estava "open".

 O que já foi corrigido:
 - dmPolicy voltou para allowlist (só meu número)
 - groupPolicy voltou para allowlist
 - ackReaction desabilitado
 - Gateway reiniciado

 REGRA INVIOLÁVEL — registrar em decisions.md com prioridade máxima:
 1. WhatsApp do OpenClaw/Baileys = APENAS leitura passiva de mensagens
 inbound. NUNCA mais dmPolicy "open"
 2. Todo envio de mensagem WhatsApp = EXCLUSIVAMENTE via Evolution API da
 Cloudfy, com minha aprovação explícita prévia
 3. O módulo web-auto-reply do OpenClaw responde automaticamente DMs quando
 dmPolicy é "open" — NUNCA mais abrir essa porta
 4. Para ler histórico de mensagens, usar Evolution API (PostgreSQL), não o
 OpenClaw
 5. NUNCA mais alterar dmPolicy sem minha autorização explícita

 Registra como lição ESTRATÉGICA de severidade máxima e atualiza SOUL.md,
 AGENTS.md e decisions.md. Isso não pode acontecer nunca mais.

 SOBRE O WHATSAPP — MUDANÇA ESTRUTURAL:
 Vou configurar um NÚMERO PRÓPRIO exclusivo para o Kobe. Ele vai usar esse
 número dele para se comunicar comigo pelo WhatsApp e para enviar mensagens
 para qualquer pessoa dos meus contatos quando eu autorizar. Meu número
 pessoal não será mais usado para envio pelo Kobe — apenas leitura passiva
 via Evolution API da Cloudfy.

 Quando o número do Kobe estiver pronto, ele poderá:
 - Me mandar mensagem direto no WhatsApp (do número dele pro meu)
 - Enviar mensagens para terceiros quando eu pedir (identificando-se como
 Kobe/assistente do Pedro, ou como Pedro se eu instruir)
 - Receber mensagens de qualquer pessoa que eu encaminhar pra ele

 Isso elimina definitivamente o risco de resposta automática no meu número
 pessoal. Vou providenciar o chip e te aviso quando estiver pronto pra
 parear.
assistant: Pedro, entendido. Incidente gravíssimo — vou registrar tudo agora com prioridade máxima.
assistant: Vejo que já existem registros parciais. Vou atualizar tudo agora — corrigir a decisão antiga que ainda diz "dmPolicy=open" (contradiz a nova regra), adicionar a decisão do número próprio, e atualizar SOUL.md e AGENTS.md.
assistant: Agora vou atualizar SOUL.md e AGENTS.md com a nova arquitetura WhatsApp:
assistant: SOUL.md já foi atualizado parcialmente. Vou ajustar para incluir o número próprio do Kobe:
assistant: Agora atualizar AGENTS.md na seção WhatsApp:
assistant: Agora vou registrar a sessão do dia e atualizar o WhatsApp integration file:
assistant: Vou criar o arquivo de integração WhatsApp e atualizar a sessão do dia:
assistant: Agora vou fazer commit de tudo:
assistant: ✅ Tudo registrado com prioridade máxima. Resumo do que fiz:

*Decisões INVIOLÁVEIS atualizadas:*
- OpenClaw/Baileys = APENAS leitura passiva. dmPolicy=allowlist, NUNCA "open"
- Todo envio e leitura de histórico = EXCLUSIVAMENTE via Evolution API Cloudfy
- NUNCA alterar dmPolicy sem tua autorização explícita
- A decisão antiga que ainda mencionava "open/open" foi corrigida

*Lição ESTRATÉGICA registrada:*
- Incidente completo documentado com causa, impacto, correção e regra permanente

*Arquivos core atualizados:*
- SOUL.md — nova arquitetura WhatsApp
- AGENTS.md — seção WhatsApp inteira reescrita
- decisions.md — decisão INVIOLÁVEL + número próprio do Kobe (pendente)
- whatsapp-integration.md — criado com status completo

*Número próprio do Kobe:*
- Registrado como pendente em todos os arquivos
- Quando tiver o chip pronto, me avisa que configuro tudo

Commit feito e pushado. Isso não acontece nunca mais. 🔒
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2292",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Wed 2026-03-25 13:41 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Atualiza o prompt adicionando o número antes de enviar:

 Kobe, seu número próprio de WhatsApp está pronto. Dados da instância na
 Evolution API Cloudfy:

 - Nome: WHATSAPP PRÓPRIO KOBE
 - Número: +55 19 99845-8149
 - URL: https://trottingtuna-evolution.cloudfy.live
 - API Key: 947278ED7E67-48B1-ADAA-342FADBAC2AA
 - Instance ID: af2e881f-265b-417d-885a-7516f3174ee6
 - Status: connected

 Arquitetura definitiva do WhatsApp:

 ENVIO (número do Kobe: +55 19 99845-8149):
 - Me enviar mensagem → instância "WHATSAPP PRÓPRIO KOBE"
 - Enviar para terceiros quando eu pedir → instância "WHATSAPP PRÓPRIO
 KOBE"
 - Identidade: Kobe / Assistente do Pedro (nunca se passar por mim nesse
 número)

 LEITURA (meu número pessoal: +55 19 99304-0768):
 - Ler histórico do meu WhatsApp → instância "WHATSAPP PESSOAL PEDRO" (API
 key: 30934F89D742-45B9-B85C-2C3192CF7A58)
 - OpenClaw/Baileys → APENAS leitura passiva inbound, NUNCA envio

 ENVIO COMO PEDRO (meu número pessoal):
 - Quando eu pedir explicitamente para enviar como se fosse eu → instância
 "WHATSAPP PESSOAL PEDRO"
 - SEMPRE com minha aprovação do texto antes de enviar
 - NUNCA automático

 Salva as credenciais no 1Password (vault OpenClaw, item "Evolution API
 Cloudfy - WhatsApp Kobe") e atualiza whatsapp-integration.md,
 decisions.md, SOUL.md e AGENTS.md.

 Testa agora: me manda um "oi Pedro" no meu WhatsApp pessoal usando seu
 número próprio.
assistant: Vou configurar tudo agora — salvar credenciais, atualizar os arquivos e testar o envio.
assistant: Credenciais salvas no 1Password. Agora vou testar o envio e atualizar os arquivos:
assistant: Mensagem enviada com sucesso! Agora vou atualizar todos os arquivos:
assistant: Agora SOUL.md e AGENTS.md — atualizar "pendente" para "ativo":
assistant: Agora atualizar AGENTS.md nas regras de envio — agora tem dois canais de envio:
assistant: ✅ Tudo pronto! Resumo:

*Credenciais:*
- Salvas no 1Password (vault OpenClaw → "Evolution API Cloudfy - WhatsApp Kobe")

*Arquitetura 3 canais configurada:*
- *Número do Kobe* (+55 19 99845-8149) → envio direto, identidade = Kobe
- *Número do Pedro* (Evolution API) → leitura de histórico + envio como Pedro (com aprovação)
- *OpenClaw/Baileys* → leitura passiva inbound only

*Arquivos atualizados:*
- whatsapp-integration.md, decisions.md, SOUL.md, AGENTS.md

*Teste:*
- Mensagem "oi Pedro 👋" enviada do meu número pro teu. Confere se chegou! 📱

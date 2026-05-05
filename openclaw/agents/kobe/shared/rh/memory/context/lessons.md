---
title: "lessons"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Lições — Agente [[openclaw/agents/rh/IDENTITY|RH]]

_Aprendizados operacionais. [ESTRATÉGICA] = permanente, [TÁTICA] = expira 30 dias._

### 2026-03-30 — WhatsApp duplicado por retry de LLM [ESTRATÉGICA]
**Contexto:** Teste do agente RH — envio de mensagem WhatsApp via Evolution API
**Erro:** Anthropic retornou 3 internal server errors (500). Em cada retry, curl re-executou → mensagem duplicada.
**Lição:** SEMPRE usar wrapper `scripts/send-whatsapp.py` com deduplicação SHA256. NUNCA chamar Evolution API via curl direto.
**Ação:** Todo envio WhatsApp (RH ou qualquer agente) passa pelo wrapper obrigatoriamente.

### 2026-03-30 — Tolerância desatualizada frontend vs backend [TÁTICA]
**Contexto:** useTimeRecords.ts tinha TOLERANCE_MINUTE=40 (antigo), backend usava 10.
**Lição:** Ao migrar/atualizar sistema, conferir constantes hardcoded no frontend que ficaram defasadas. Sempre comparar com backend.
**Ação:** Corrigido para 10. Verificar outros hardcodes.
**Expira:** 2026-04-30

### 2026-03-30 — Knowledge Files do Lovable como fonte de verdade [ESTRATÉGICA]
**Contexto:** Ponto Certo gerou Knowledge File completo de regras via Lovable.
**Lição:** Lovable gera documentação de regras de negócio muito completa. Copiar pro workspace dos agentes como fonte de verdade.
**Ação:** `shared/rh/knowledge/regras-ponto-certo.md` é a fonte de verdade do RH para regras de ponto.

### 2026-03-30 — Instância dedicada na Evolution API por agente [ESTRATÉGICA]
**Contexto:** RH terá WhatsApp próprio (5519992997273) separado do Kobe.
**Lição:** Cada agente com WhatsApp próprio precisa de instância dedicada na Evolution API. Tokens de instância NÃO criam novas instâncias — precisa Global API Key ou painel Cloudfy Manager.

### 2026-03-30 — Modo supervisão obrigatório para mensagens a funcionários [ESTRATÉGICA]
**Contexto:** Pedro ativou modo supervisão — toda mensagem enviada a funcionário gera notificação no Telegram (tópico RH).
**Lição:** Enquanto modo supervisão ativo, NUNCA enviar mensagem a funcionário sem gerar notificação no Telegram. Pedro decide quando desativar.

### 2026-04-30 — Evolution webhook não é garantia de entrega [ESTRATÉGICA]
**Contexto:** Lucas e Sandra enviaram mensagens reais; Evolution recebeu, mas webhook não disparou.
**Lição:** Para comunicação RH com funcionários, webhook precisa de rede de segurança por polling e detector de stuck. Não assumir que ausência de webhook = ausência de mensagem.

### 2026-04-30 — Teste manual com número real pode confundir funcionário [TÁTICA]
**Contexto:** Um teste manual simulando o número do Lucas gerou resposta que caiu na conversa real dele, parecendo mensagem desconexa.
**Lição:** Nunca testar pipeline de funcionário usando número real sem isolar conversa/tag de teste. Preferir contato controlado ou dry-run que não envia outbound.
**Expira:** 2026-05-30


### 2026-05-04 — WhatsApp RH: texto puro + linkPreview false [TÁTICA]
**Contexto:** Yasmin recebeu bolhas “Aguardando mensagem” em vez de mensagens do RH.
**Lição:** Mesmo texto simples pode acionar renderização problemática se o cliente/Evolution/Baileys tentar preview/rich render. Para RH, usar texto puro com `linkPreview:false` e evitar interativos/listas/polls.
**Ação:** Wrapper central atualizado; manter regra em todas as mensagens para funcionários.
**Expira:** 2026-06-03

### 2026-05-04 — Separar proativo de inbound no RH [TÁTICA]
**Contexto:** Bloqueio inicial parou todo o RH, mas Pedro queria apenas evitar disparos proativos/alinhamentos enquanto mantinha atendimento receptivo.
**Lição:** Em agentes com WhatsApp operacional, bloqueio de outbound precisa distinguir proativo de resposta inbound. Parar tudo derruba suporte receptivo sem necessidade.
**Ação:** Usar guard para proativos e flag explícita (`--allow-rh-reply`) para respostas do pipeline.
**Expira:** 2026-06-03

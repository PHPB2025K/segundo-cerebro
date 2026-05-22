# BRIEFING — Diagnóstico da Ana

## 1. O que é a Ana, tecnicamente

A Ana é o agente de atendimento automatizado da Budamix/Canggu. Ela recebe mensagens de clientes pelo WhatsApp, registra no Supabase, classifica intenção, monta contexto com histórico/catálogo/políticas, gera resposta com LLM e envia de volta via Evolution API.

Stack:
- Frontend/admin: React/Vite/TypeScript
- Backend principal: Supabase Edge Functions em TypeScript/Deno
- Banco: Supabase Postgres + pgvector
- WhatsApp: Evolution API Cloudfy, instância Budamix AI Agent
- IA: Anthropic Claude para classificação/resposta, OpenAI embeddings, Groq Whisper para áudio
- N8N: hoje é standby/legado, não deve ser tratado como caminho principal

Repo/código:
- Repositório canônico: `PHPB2025K/canguu`
- Checkout local na VPS: `/root/.openclaw/workspace/canguu`
- Funções críticas:
  - `supabase/functions/webhook-whatsapp`
  - `supabase/functions/process-message`
  - `supabase/functions/_shared/whatsapp-dispatch.ts`
  - `supabase/functions/_shared/evolution-api.ts`

Pipeline esperado:
WhatsApp cliente → Evolution API → `webhook-whatsapp` → grava `customers/conversations/messages` no Supabase → chama `process-message` → LLM gera resposta → salva `messages.sender='agent'` com `tokens_used` → dispatcher envia WhatsApp.

## 2. A falha em si

Sintoma concreto atual:
- As mensagens dos clientes chegam na Canggu/Supabase.
- A mensagem automática inicial de origem/canal é enviada.
- Mas em conversas reais, depois disso, a Ana não gera resposta LLM nem envia follow-up.
- No banco, aparecem mensagens `sender='customer'`, mas não aparece uma mensagem posterior `sender='agent'` com `tokens_used`.

Último diagnóstico de hoje:
- De 21/05 pra 22/05 entraram mensagens reais de clientes.
- Casos vistos:
  - Edneia: reclamação de canecas com avaria, entrou ontem por volta de 15:16–15:18 BRT, sem resposta LLM.
  - Carolina: reclamação crítica de canecas quebradas/rachadas, entrou ontem por volta de 23:17–23:56 BRT, sem resposta LLM.
- O teste manual do Kobe ontem respondeu uma pergunta sobre pote de vidro em ~35s, então a falha parece intermitente ou dependente do caminho/conteúdo/conversa real, não simplesmente “LLM morto”.

Erro histórico recente:
- Em 21/05, o `process-message` retornava 401 quando chamado com `Authorization: Bearer SUPABASE_SERVICE_ROLE_KEY`.
- Foi aplicado workaround em produção: `X-Internal-Token` + `verify_jwt=false` no `process-message`.
- Depois disso, um teste E2E respondeu, mas clientes reais posteriores ainda ficaram sem resposta.

## 3. Como reproduzir e detectar

Reprodução segura:
1. Usar número controlado/teste, não cliente real.
2. Enviar mensagem para o WhatsApp da Ana/Budamix.
3. Se vier a pergunta de origem, responder “Shopee” ou “5”.
4. Enviar uma pergunta simples de produto.
5. Aguardar 60–90s.
6. Verificar no Supabase:
   - se entrou `messages.sender='customer'`
   - se abriu/fechou `conversations.pending_since`
   - se nasceu `messages.sender='agent'` com `tokens_used`
   - se o texto foi enviado via Evolution

Caminho que quebrou hoje:
- Cliente real manda várias mensagens/imagens.
- `webhook-whatsapp` registra as entradas e análise das imagens.
- A conversa continua `assigned_to='agent'`.
- Não aparece resposta LLM posterior.

Como detectar:
- Query no Supabase procurando conversas com mensagens de cliente recentes sem resposta `agent` posterior.
- Indicador forte: `customer_msgs > 0` e `llm_replies_after_last_customer = 0`.
- Também checar `messages.metadata.ai_description`, porque imagens estão sendo processadas; isso prova que ingestão está viva.

Logs:
- Supabase Edge Function logs:
  - `webhook-whatsapp`
  - `process-message`
- Banco Supabase:
  - `messages`
  - `conversations`
  - `customers`
  - `escalations`
- Evolution API:
  - webhook/eventos da instância Budamix AI Agent

Não existe ainda healthcheck confiável/automatizado. O healthcheck antigo do N8N está quebrado/parado desde 07/05 e deve ser substituído por script versionado.

## 4. Histórico

Esse problema já voltou várias vezes, com causas diferentes:

- 05/05–07/05: mensagens chegavam na Evolution, mas não entravam na Canggu porque webhook estava sem headers/auth correta.
- 08/05–17/05: Ana ficou muda porque `webhook-whatsapp` chamava `process-message` em fire-and-forget sem `EdgeRuntime.waitUntil`; o runtime encerrava antes do fetch terminar.
- 13/05: houve rotação de chave Anthropic e upgrade para Opus, mas isso tratou só parte do problema.
- 21/05: `process-message` passou a retornar 401 quando invocado com service role; foi aplicado bypass com token interno.
- 22/05: ingestão está funcionando, teste controlado respondeu, mas conversas reais de clientes ficaram sem resposta.

Mudanças recentes relevantes:
- `webhook-whatsapp` v36 e `process-message` v42 em produção.
- Workaround temporário com `X-Internal-Token`.
- Parser de origem foi ajustado para aceitar “Shoppe” → `shopee`.
- Repo local pode estar atrás do estado real de produção. Antes de mexer, reconciliar repo/origin/produção.

## 5. Limites e restrições

Não mexer sem cuidado:
- Não enviar mensagem automática/manual para clientes reais sem aprovação.
- Não trocar credenciais/chaves em produção sem backup e validação.
- Não reativar N8N como caminho principal sem decisão explícita; ele é standby.
- Não mexer em Evolution webhook de produção sem salvar configuração atual.
- Não commitar secrets.
- Não “corrigir” só com prompt. O problema atual é pipeline/dispatch/observabilidade.

Pode testar:
- Com número controlado do Kobe/teste.
- Com `dispatch=false` se for invocar `process-message` manualmente só para validar cérebro/LLM sem envio externo.
- Com consultas no Supabase para checar mensagens, conversas e resposta LLM.

Hipótese principal agora:
- A ingestão está viva.
- O cérebro/LLM consegue responder em teste.
- O bug está no caminho automático entre `webhook-whatsapp` → `process-message` → dispatcher, possivelmente dependente de debounce/buffer, mensagens com imagem, escalonamento, múltiplas mensagens em burst, ou divergência entre código versionado e produção.

---
tipo: backlog
projeto: Canggu
status: ativo
tags: [canggu, features, ana, backlog]
criado: 2026-04-22
atualizado: 2026-04-22
fonte: "Solicitação Pedro em 2026-04-22 ~21:45, durante pausa do B1"
---

# Backlog — Features da Ana

> Lista de features solicitadas para melhorar a comunicação da Ana
> com clientes. Registrada para não perder o pedido; encaixe no
> roadmap ([[debitos-tecnicos]]) fica para sessão de planejamento
> pós-B1 ([[perguntas-abertas#Execução em andamento (pausada)]]).

## F1 — Humanização e não-repetição de respostas

**Pedido:** Ana deve soar mais humana nas respostas e não repetir
o mesmo texto em conversas diferentes ou mesmo dentro de uma
conversa.

**O que toca:**
- `supabase/functions/_shared/response-generator.ts` (tom, prompt
  engineering)
- `supabase/functions/_shared/response-validator.ts` (detecção de
  repetição — pode precisar histórico de respostas anteriores)
- Possivelmente `messages` table (flag de respostas repetidas pra
  análise futura)
- Prompt do sistema da Ana (tom, instruções de variação)

**Dependência técnica:**
Não-repetição pede alguma forma de memória de "o que já foi dito".
Pode ser:
- Comparação por similaridade de embeddings das últimas N respostas
  (caro)
- Cache simples de últimas X respostas por conversation_id (barato)
- Instrução ao LLM: "varie sua formulação, evite repetir frases de
  respostas anteriores nesta conversa" (mais barato, menos garantido)

**Pré-discussão de afinidade com roadmap:**
Flerta com [[debitos-tecnicos#B2 — Observabilidade]] (tracking de
respostas) e [[debitos-tecnicos#B3 — Resiliência]] (qualidade de
resposta). Pode virar sub-feature do B2 ou bloco próprio. Discutir
amanhã.

**Esforço estimado:** M (3-5 dias) dependendo da abordagem escolhida.

---

## F2 — Suporte multimodal: Ana vê imagens

**Pedido:** Ana deve conseguir processar imagens que clientes enviam
no WhatsApp (foto de produto, foto de problema, foto de nota fiscal).

**O que toca:**
- `supabase/functions/_shared/evolution-api.ts` (extrair URL/base64
  da imagem do payload do webhook Evolution)
- `supabase/functions/process-message/index.ts` (branch de handling
  para mensagem com imagem)
- `supabase/functions/_shared/response-generator.ts` (passar imagem
  pro Claude Sonnet no content array — Anthropic API aceita
  content blocks de tipo `image` com base64 ou URL)
- Possível nova coluna em `messages` (`media_url` ou `media_type`)
  se ainda não existe
- Storage Supabase: hoje tem 0 buckets; pode precisar criar bucket
  `whatsapp-media` pra persistir imagens (ou só passar URL pra o
  Claude sem persistir)

**Dependência técnica:**
- Claude Sonnet 4 suporta input multimodal nativo
- Evolution API entrega imagens via URL temporária ou base64 no
  webhook (confirmar formato atual no payload)
- Decisão: persistir imagem no Supabase Storage ou só usar URL
  temporária da Evolution? Persistir permite reprocessar depois,
  mas introduz custo de storage e complexidade.

**Pré-discussão de afinidade com roadmap:**
Feature nova, não cabe direto em nenhum dos blocos B1-B6. Candidata
a B7 ou fim do B4. Mudança arquitetural média — multimodal toca
muitas camadas.

**Esforço estimado:** L (1-2 semanas) se persistir em Storage; M
(3-5 dias) se só passar URL.

---

## F3 — Histórico completo de conversa mesmo após hiato

**Pedido:** quando um cliente volta a mandar mensagem depois de
semanas sem falar com a Ana, ela deve ter acesso ao histórico
completo daquela conversa — não apenas às últimas mensagens
recentes.

**O que toca:**
- `supabase/functions/_shared/context-builder.ts` (função
  `buildContext()` que monta o prompt — hoje provavelmente limita
  histórico por janela temporal ou quantidade pra economizar tokens)

**Dependência técnica:**
- `messages` table já guarda tudo? (Confirmar — se guarda, o fix
  é só em buildContext. Se não guarda — limpa mensagens antigas
  por cron ou TTL — precisa investigar e ajustar retenção)
- Context window: Claude Sonnet 4 tem 1M tokens, então "histórico
  completo" de um cliente realista (dezenas/centenas de mensagens)
  cabe tranquilamente. Risco de estourar só em clientes muito
  longos.
- Custo: cada 1K tokens de input no Sonnet custa ~$3/M. Histórico
  de 200 mensagens = ~20K tokens = ~$0.06 por conversa. Aceitável.
- Estratégia inteligente: carregar TUDO até N tokens, e se passar
  de N, sumarizar com LLM mais barato (Haiku) o histórico velho +
  injetar sumário + últimas M mensagens literais.

**Pré-discussão de afinidade com roadmap:**
Menor das 3 features. Fix de lógica + decisão de janela/sumarização.
Cabe em B3 (Resiliência/Qualidade) ou isolado.

**Esforço estimado:** S (1-2 dias) para fix simples; M (3-5 dias)
para estratégia de sumarização inteligente.

---

## Priorização preliminar (para discussão amanhã)

Ordem sugerida por custo/benefício:

1. **F3 (histórico completo)** — menor esforço, impacto imediato
   visível para cliente que volta depois de semanas. Resolve bug
   de memória que é a pior cara da Ana hoje.
2. **F1 (humanização)** — esforço médio, impacto em cada mensagem.
   Requer decisões de design (tom? memória de repetição?).
3. **F2 (multimodal)** — maior esforço, feature nova. Valiosa mas
   pode esperar Ana estar sólida em texto antes.

Mas a ordem real depende de:
- Qual dor de cliente é mais recorrente hoje? Saber por logs/
  operador, não por intuição
- Quanto o pipeline B1-B6 já mexe nos mesmos arquivos que essas
  features tocam? Consolidação pode valer a pena.

Decidir amanhã em sessão de planejamento pós-B1.

## Status
🟡 Registrado como backlog. Aguarda discussão de encaixe no roadmap
após conclusão do B1.

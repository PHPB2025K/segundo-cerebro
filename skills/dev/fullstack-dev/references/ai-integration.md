---
title: "ai integration"
created: 2026-04-14
type: skill
domain: dev
status: active
tags:
  - skill/dev
---

# AI Integration Reference — OpenAI, Claude, Streaming, RAG, pgvector

## Índice
1. [OpenAI — Patterns Práticos](#1-openai)
2. [Anthropic Claude](#2-claude)
3. [Streaming com Vercel AI SDK](#3-streaming)
4. [Function Calling / Tool Use](#4-function-calling)
5. [RAG com pgvector (Supabase)](#5-rag)
6. [Patterns para Canguu](#6-canguu-patterns)

---

## 1. OpenAI

```ts
import OpenAI from 'openai'
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! })

// Chat simples
async function analyzeImportData(data: ImportSimulation): Promise<string> {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: 'Você é um especialista em comércio exterior brasileiro. Analise dados de importação e forneça insights estratégicos e práticos.'
      },
      {
        role: 'user',
        content: `Analise esta simulação de importação:\n${JSON.stringify(data, null, 2)}`
      }
    ],
    max_tokens: 1500,
    temperature: 0.3, // determinístico para análises
  })
  return response.choices[0].message.content!
}

// Com histórico de conversa (multi-turn)
type Message = { role: 'user' | 'assistant' | 'system'; content: string }

async function chat(messages: Message[], userMessage: string) {
  const allMessages = [...messages, { role: 'user' as const, content: userMessage }]

  const response = await openai.chat.completions.create({
    model: 'gpt-4o-mini', // mais barato para conversas
    messages: allMessages,
    max_tokens: 800,
    temperature: 0.7,
  })

  const reply = response.choices[0].message
  return {
    content: reply.content!,
    messages: [...allMessages, { role: 'assistant' as const, content: reply.content! }],
  }
}

// Embeddings para RAG
async function getEmbedding(text: string): Promise<number[]> {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small', // melhor custo-benefício
    input: text,
  })
  return response.data[0].embedding
}
```

---

## 2. Claude

```ts
import Anthropic from '@anthropic-ai/sdk'
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY! })

// Resposta simples
async function analyzeWithClaude(prompt: string): Promise<string> {
  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    system: 'Você é um especialista em marketplace e importação para e-commerce brasileiro.',
    messages: [{ role: 'user', content: prompt }],
  })

  return message.content[0].type === 'text' ? message.content[0].text : ''
}

// Com vision (análise de imagem)
async function analyzeProductImage(imageUrl: string, question: string) {
  const message = await anthropic.messages.create({
    model: 'claude-opus-4-5',
    max_tokens: 1024,
    messages: [
      {
        role: 'user',
        content: [
          { type: 'image', source: { type: 'url', url: imageUrl } },
          { type: 'text', text: question }
        ],
      }
    ],
  })
  return message.content[0].type === 'text' ? message.content[0].text : ''
}

// Tool use (Claude)
const tools: Anthropic.Tool[] = [
  {
    name: 'get_exchange_rate',
    description: 'Obtém a taxa de câmbio atual entre duas moedas',
    input_schema: {
      type: 'object' as const,
      properties: {
        from: { type: 'string', enum: ['USD', 'EUR', 'CNY'] },
        to: { type: 'string', enum: ['BRL'] },
      },
      required: ['from', 'to'],
    },
  },
]

async function chatWithTools(userMessage: string): Promise<string> {
  let messages: Anthropic.MessageParam[] = [{ role: 'user', content: userMessage }]

  while (true) {
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      tools,
      messages,
    })

    if (response.stop_reason === 'end_turn') {
      const textBlock = response.content.find(b => b.type === 'text')
      return textBlock?.type === 'text' ? textBlock.text : ''
    }

    if (response.stop_reason === 'tool_use') {
      messages.push({ role: 'assistant', content: response.content })

      const toolResults: Anthropic.ToolResultBlockParam[] = await Promise.all(
        response.content
          .filter((b): b is Anthropic.ToolUseBlock => b.type === 'tool_use')
          .map(async (tool) => ({
            type: 'tool_result' as const,
            tool_use_id: tool.id,
            content: JSON.stringify(await executeToolCall(tool.name, tool.input)),
          }))
      )

      messages.push({ role: 'user', content: toolResults })
    }
  }
}
```

---

## 3. Streaming

### Vercel AI SDK (mais simples)

```ts
// app/api/chat/route.ts
import { openai } from '@ai-sdk/openai'
import { streamText } from 'ai'

export async function POST(request: NextRequest) {
  const { messages } = await request.json()

  const result = streamText({
    model: openai('gpt-4o'),
    system: 'Você é Kobe, especialista em marketplace e importação.',
    messages,
    maxTokens: 1000,
  })

  return result.toDataStreamResponse()
}

// Client Component
'use client'
import { useChat } from 'ai/react'

export function ChatInterface() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/api/chat',
  })

  return (
    <div>
      <div className="space-y-4">
        {messages.map(m => (
          <div key={m.id} className={m.role === 'user' ? 'text-right' : 'text-left'}>
            <p className="inline-block max-w-lg p-3 rounded-lg bg-card">{m.content}</p>
          </div>
        ))}
        {isLoading && <div className="animate-pulse">Pensando...</div>}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2 mt-4">
        <input
          value={input}
          onChange={handleInputChange}
          placeholder="Digite sua mensagem..."
          className="flex-1"
        />
        <button type="submit" disabled={isLoading}>Enviar</button>
      </form>
    </div>
  )
}

// useCompletion (single turn, sem histórico)
import { useCompletion } from 'ai/react'

export function AIAnalysis({ data }: { data: ImportSim }) {
  const { completion, isLoading, complete } = useCompletion({
    api: '/api/analyze',
  })

  return (
    <div>
      <button onClick={() => complete(JSON.stringify(data))} disabled={isLoading}>
        {isLoading ? 'Analisando...' : 'Analisar com IA'}
      </button>
      {completion && <div className="prose mt-4">{completion}</div>}
    </div>
  )
}
```

### Streaming Manual (sem Vercel AI SDK)

```ts
// Claude streaming
export async function POST(request: NextRequest) {
  const { message } = await request.json()

  const stream = anthropic.messages.stream({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [{ role: 'user', content: message }],
    system: 'Especialista em marketplace e importação.',
  })

  return new Response(
    new ReadableStream({
      async start(controller) {
        const enc = new TextEncoder()
        for await (const chunk of stream) {
          if (chunk.type === 'content_block_delta' && chunk.delta.type === 'text_delta') {
            controller.enqueue(enc.encode(chunk.delta.text))
          }
        }
        controller.close()
      },
    }),
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
  )
}

// Client: consumir stream
async function consumeStream(message: string) {
  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  })

  const reader = response.body!.getReader()
  const decoder = new TextDecoder()
  let result = ''

  while (true) {
    const { done, value } = await reader.read()
    if (done) break
    result += decoder.decode(value, { stream: true })
    setContent(result) // atualizar UI em tempo real
  }
}
```

---

## 4. Function Calling

```ts
// OpenAI — tools para o Canguu (atendimento)
const MARKETPLACE_TOOLS: OpenAI.Chat.ChatCompletionTool[] = [
  {
    type: 'function',
    function: {
      name: 'get_order_status',
      description: 'Consulta o status de um pedido no Mercado Livre ou Amazon',
      parameters: {
        type: 'object',
        properties: {
          orderId: { type: 'string', description: 'ID do pedido' },
          marketplace: { type: 'string', enum: ['mercado_livre', 'amazon', 'shopee'] },
        },
        required: ['orderId', 'marketplace'],
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'get_product_info',
      description: 'Busca informações do produto (estoque, prazo de entrega, especificações)',
      parameters: {
        type: 'object',
        properties: {
          productId: { type: 'string' },
          marketplace: { type: 'string', enum: ['mercado_livre', 'amazon', 'shopee'] },
        },
        required: ['productId', 'marketplace'],
      },
    },
  },
]

async function canguuChat(userMessage: string, context: { marketplace: string; sellerId: string }) {
  const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
    {
      role: 'system',
      content: `Você é um atendente de e-commerce da GB Importadora.
Marketplace: ${context.marketplace}. Responda em português, seja cordial e objetivo.
Use as ferramentas disponíveis para consultar pedidos e produtos.`,
    },
    { role: 'user', content: userMessage },
  ]

  let response = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages,
    tools: MARKETPLACE_TOOLS,
    tool_choice: 'auto',
  })

  // Loop até não ter mais tool_calls
  while (response.choices[0].finish_reason === 'tool_calls') {
    const toolCalls = response.choices[0].message.tool_calls!
    messages.push(response.choices[0].message)

    const toolResults = await Promise.all(
      toolCalls.map(async (call) => {
        const args = JSON.parse(call.function.arguments)
        const result = await executeMarketplaceTool(call.function.name, args)
        return {
          tool_call_id: call.id,
          role: 'tool' as const,
          content: JSON.stringify(result),
        }
      })
    )

    messages.push(...toolResults)
    response = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages,
      tools: MARKETPLACE_TOOLS,
    })
  }

  return response.choices[0].message.content!
}

async function executeMarketplaceTool(name: string, args: Record<string, string>) {
  switch (name) {
    case 'get_order_status':
      return getOrderStatus(args.orderId, args.marketplace)
    case 'get_product_info':
      return getProductInfo(args.productId, args.marketplace)
    default:
      throw new Error(`Tool desconhecida: ${name}`)
  }
}
```

---

## 5. RAG

### Setup pgvector (Supabase)

```sql
-- Habilitar extensão
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela de documentos
CREATE TABLE knowledge_base (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding vector(1536),
  org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  source TEXT,                  -- nome do arquivo, URL, etc
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Índice para busca por similaridade
CREATE INDEX ON knowledge_base USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);

-- RLS
ALTER TABLE knowledge_base ENABLE ROW LEVEL SECURITY;
CREATE POLICY "org_sees_knowledge" ON knowledge_base
  FOR SELECT USING (
    org_id IN (SELECT org_id FROM organization_members WHERE user_id = auth.uid())
  );

-- Função de busca semântica
CREATE OR REPLACE FUNCTION search_knowledge(
  query_embedding vector(1536),
  match_threshold FLOAT DEFAULT 0.7,
  match_count INT DEFAULT 5,
  p_org_id UUID DEFAULT NULL
)
RETURNS TABLE (id UUID, content TEXT, metadata JSONB, similarity FLOAT)
LANGUAGE sql STABLE AS $$
  SELECT id, content, metadata,
    1 - (embedding <=> query_embedding) AS similarity
  FROM knowledge_base
  WHERE
    1 - (embedding <=> query_embedding) > match_threshold
    AND (p_org_id IS NULL OR org_id = p_org_id)
  ORDER BY similarity DESC
  LIMIT match_count;
$$;
```

### Pipeline RAG Completo

```ts
// lib/rag.ts

// Indexar documento
export async function indexDocument(
  content: string,
  metadata: Record<string, unknown>,
  orgId?: string
) {
  // 1. Chunking (dividir documento longo em pedaços)
  const chunks = splitIntoChunks(content, {
    maxTokens: 500,
    overlap: 50,
  })

  // 2. Gerar embeddings para cada chunk
  const embeddings = await Promise.all(
    chunks.map(chunk =>
      openai.embeddings.create({
        model: 'text-embedding-3-small',
        input: chunk,
      }).then(r => r.data[0].embedding)
    )
  )

  // 3. Salvar no banco
  await db.insert(knowledgeBase).values(
    chunks.map((content, i) => ({
      content,
      metadata: { ...metadata, chunkIndex: i, totalChunks: chunks.length },
      embedding: embeddings[i],
      orgId,
    }))
  )
}

// Busca semântica
export async function searchKnowledge(
  query: string,
  options: { orgId?: string; limit?: number; threshold?: number } = {}
) {
  const embedding = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: query,
  }).then(r => r.data[0].embedding)

  const { data: docs } = await supabase.rpc('search_knowledge', {
    query_embedding: embedding,
    match_threshold: options.threshold ?? 0.7,
    match_count: options.limit ?? 5,
    p_org_id: options.orgId ?? null,
  })

  return docs ?? []
}

// Query RAG
export async function ragQuery(
  userQuestion: string,
  options: { orgId?: string; model?: string } = {}
): Promise<string> {
  // 1. Buscar contexto relevante
  const docs = await searchKnowledge(userQuestion, { orgId: options.orgId })

  if (docs.length === 0) {
    return 'Não encontrei informações relevantes na base de conhecimento para responder sua pergunta.'
  }

  // 2. Montar contexto
  const context = docs.map((d, i) => `[${i + 1}] ${d.content}`).join('\n\n---\n\n')

  // 3. Gerar resposta com contexto
  const response = await openai.chat.completions.create({
    model: options.model ?? 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: `Você é um assistente especializado. Responda APENAS com base no contexto fornecido.
Se a informação não estiver no contexto, diga "Não tenho essa informação disponível."
Seja objetivo e cite os trechos relevantes quando necessário.

Contexto disponível:
${context}`,
      },
      { role: 'user', content: userQuestion }
    ],
    temperature: 0.2,
  })

  return response.choices[0].message.content!
}

// Chunking simples por parágrafos/sentenças
function splitIntoChunks(text: string, options: { maxTokens?: number; overlap?: number } = {}) {
  const maxChars = (options.maxTokens ?? 500) * 4 // ~4 chars per token
  const paragraphs = text.split('\n\n').filter(Boolean)
  const chunks: string[] = []
  let current = ''

  for (const para of paragraphs) {
    if (current.length + para.length > maxChars && current) {
      chunks.push(current.trim())
      // Overlap: manter último parágrafo no próximo chunk
      current = options.overlap ? current.split('\n\n').slice(-1)[0] + '\n\n' + para : para
    } else {
      current += (current ? '\n\n' : '') + para
    }
  }

  if (current) chunks.push(current.trim())
  return chunks
}
```

---

## 6. Canguu Patterns

### Agente de Atendimento Completo

```ts
// Estrutura do agente Canguu
interface CanguuContext {
  marketplace: 'mercado_livre' | 'amazon' | 'shopee'
  sellerId: string
  orgId: string
  conversationId: string
  customerQuestion: string
  customerName?: string
  orderId?: string
  productId?: string
}

async function processCustomerMessage(ctx: CanguuContext): Promise<string> {
  // 1. Buscar contexto relevante na KB
  const relevantDocs = await searchKnowledge(ctx.customerQuestion, {
    orgId: ctx.orgId,
    limit: 3,
    threshold: 0.75,
  })

  // 2. Montar mensagens com contexto
  const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
    {
      role: 'system',
      content: buildSystemPrompt(ctx, relevantDocs),
    },
    { role: 'user', content: ctx.customerQuestion },
  ]

  // 3. Chat com tools para consultas em tempo real
  let response = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages,
    tools: MARKETPLACE_TOOLS,
    tool_choice: 'auto',
    temperature: 0.3, // consistente em atendimento
    max_tokens: 500,
  })

  // 4. Executar tools se necessário
  if (response.choices[0].finish_reason === 'tool_calls') {
    response = await executeToolsAndContinue(response, messages, ctx.marketplace)
  }

  const reply = response.choices[0].message.content!

  // 5. Salvar conversa no DB
  await saveConversationTurn({
    conversationId: ctx.conversationId,
    orgId: ctx.orgId,
    role: 'assistant',
    content: reply,
    metadata: { model: 'gpt-4o-mini', relevantDocs: relevantDocs.length },
  })

  return reply
}

function buildSystemPrompt(ctx: CanguuContext, docs: KnowledgeDoc[]): string {
  const kbContext = docs.length > 0
    ? `\nInformações relevantes da base de conhecimento:\n${docs.map(d => d.content).join('\n\n')}`
    : ''

  return `Você é um atendente virtual da GB Importadora no ${ctx.marketplace}.
Seja cordial, objetivo e resolve o problema do cliente.
Responda em português brasileiro.
Não invente informações — use apenas o que está disponível nas ferramentas ou base de conhecimento.
${kbContext}`
}
```

### Processamento Assíncrono com BullMQ

```ts
// Para alto volume — não processar em tempo real, usar fila
import { Queue, Worker } from 'bullmq'

const messageQueue = new Queue('canguu-messages', { connection })

// Ao receber mensagem do marketplace
export async function receiveMarketplaceMessage(payload: {
  marketplace: string; conversationId: string; message: string; orderId?: string
}) {
  await messageQueue.add('process', payload, {
    attempts: 3,
    backoff: { type: 'fixed', delay: 2000 },
  })
}

const worker = new Worker('canguu-messages', async (job) => {
  const ctx = await buildContext(job.data)
  const reply = await processCustomerMessage(ctx)
  await sendReplyToMarketplace(ctx.marketplace, ctx.conversationId, reply)
}, { connection, concurrency: 10 })
```

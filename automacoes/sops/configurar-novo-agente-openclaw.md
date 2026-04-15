---
title: "SOP — Configurar Novo Agente OpenClaw"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
estimated-time: "60-120 min"
tags:
  - sop
  - openclaw
  - agente
  - automacao
---

# SOP — Configurar Novo Agente OpenClaw

## Objetivo

Criar e registrar um novo agente no sistema multi-agente OpenClaw, desde a definição de identidade até o deploy na VPS.

## Pré-requisitos

- [ ] Acesso SSH à VPS (187.77.237.231)
- [ ] Repositório do vault (`~/segundo-cerebro/`) atualizado
- [ ] Definição clara: qual domínio o agente vai cobrir
- [ ] Aprovação do Pedro para criar o agente

---

## Procedimento

### Passo 1 — Criar estrutura de diretórios

```bash
AGENT="nome-do-agente"
BRAIN="$HOME/segundo-cerebro"

# Diretório principal do agente
mkdir -p "$BRAIN/openclaw/agents/$AGENT/memory/context"
mkdir -p "$BRAIN/openclaw/agents/$AGENT/memory/sessions"

# Shared memory (sob Kobe)
mkdir -p "$BRAIN/openclaw/agents/kobe/shared/$AGENT/memory/context"
mkdir -p "$BRAIN/openclaw/agents/kobe/shared/$AGENT/memory/sessions"
```

### Passo 2 — Criar arquivos de identidade

Copiar template do agente mais recente (RH é o mais limpo):

```bash
cp "$BRAIN/openclaw/agents/rh/IDENTITY.md" "$BRAIN/openclaw/agents/$AGENT/IDENTITY.md"
cp "$BRAIN/openclaw/agents/rh/SOUL.md" "$BRAIN/openclaw/agents/$AGENT/SOUL.md"
cp "$BRAIN/openclaw/agents/rh/AGENTS.md" "$BRAIN/openclaw/agents/$AGENT/AGENTS.md"
```

**Arquivos obrigatórios:**

| Arquivo | O que define |
|---------|-------------|
| `IDENTITY.md` | Personalidade, papel, domínios, regras de ouro (9 seções) |
| `SOUL.md` | Valores, tom, vibe, nunca-fazer (11 seções) |
| `AGENTS.md` | Modelo operacional, crons, segurança, relatórios |
| `TOOLS.md` | APIs, integrações, rate limits, credenciais |
| `MEMORY.md` | Índice de arquivos de memória |
| `HEARTBEAT.md` | Template de health check |
| `memory/context/decisions.md` | Decisões permanentes do Pedro |
| `memory/context/lessons.md` | Erros e aprendizados |
| `memory/context/business-context.md` | Vocabulário do domínio |
| `memory/pending.md` | Itens aguardando input |

### Passo 3 — Customizar IDENTITY.md

Seções obrigatórias:

1. **Quem é** — nome, emoji, gênero, data criação
2. **Personalidade e Tom** — traços + o que NUNCA faz
3. **Domínios de Conhecimento** — expertise hierárquica
4. **Contexto Operacional** — o que sabe sobre a GB Importadora
5. **Escopo e Limites** — tabela "FAZ" vs "NÃO FAZ"
6. **Protocolos de Operação** — prioridades, escalação, incerteza
7. **Formato de Entrega** — template padrão de output
8. **Relacionamento com Outros Agentes** — como se comunica
9. **Regras de Ouro** — 7-9 princípios inegociáveis

### Passo 4 — Configurar modelo e fallback

```yaml
# No AGENTS.md:
Modelo: openai-codex/gpt-5.4
Fallback: openai-codex/gpt-5.1-mini → anthropic/claude-haiku-4-5
Timeout: 360s
Max concurrent: 4
```

**Regra:** TODO agente novo começa com GPT 5.4 (custo fixo GPT Pro).

### Passo 5 — Definir nível de autonomia

| Nível | Nome | Autonomia | Promoção |
|:-----:|------|-----------|----------|
| **L1** | Observer | Zero — Kobe revisa tudo | 5 entregas aprovadas consecutivas |
| L2 | Contributor | Baixa — sugere, Kobe aprova | 2 semanas consistentes |
| L3 | Operator | Média — executa dentro de guidelines | 1 mês em L2 |
| L4 | Trusted | Alta — escala só decisões >R$500 | Performance excepcional + Pedro |

**Regra:** TODO agente novo = **L1 (Observer)**.

### Passo 6 — Registrar no TEAM.md do Kobe

Adicionar entrada em `openclaw/agents/kobe/shared/TEAM.md`:

```markdown
| [Agent] | [Domínio] | L1 | [Data criação] | Em avaliação |
```

### Passo 7 — Configurar crons (se aplicável)

```markdown
### Nome do Cron
- **Schedule:** [Dia/frequência] [HH:MM BRT]
- **Modelo:** openai-codex/gpt-5.4
- **Timeout:** 300s
- **Função:** [descrição]
```

**Regras de crons:**
- Sempre horário BRT (UTC-3)
- Timeout: 300-360s padrão
- `announce: true` apenas quando resultado notável
- `HEARTBEAT_OK` para sucesso silencioso
- `sessionTarget: isolated` (sem vazamento de contexto)

### Passo 8 — Configurar canal Telegram

Kobe Hub tem 11 tópicos. Novo agente recebe 1 tópico dedicado.

**Regra:** Sub-agentes NUNCA falam direto com Pedro. Sempre via Kobe.

### Passo 9 — Deploy na VPS

> [!question] Requer acesso VPS
> Os passos abaixo precisam de SSH na VPS 187.77.237.231.

```bash
# 1. Atualizar repo na VPS
ssh root@187.77.237.231
cd /root/.openclaw/workspace
git pull

# 2. Editar openclaw.json — adicionar agent config
nano /root/.openclaw/openclaw.json

# 3. Adicionar bloco do agente:
# {
#   "agents": {
#     "[agent-name]": {
#       "model": "openai-codex/gpt-5.4",
#       "fallback": ["openai-codex/gpt-5.1-mini", "anthropic/claude-haiku-4-5"],
#       "timeout": 360,
#       "channels": { "telegram": { "channelId": "...", "topicId": "..." } },
#       "crons": [...],
#       "level": "L1"
#     }
#   }
# }

# 4. Restart gateway
openclaw restart
```

### Passo 10 — Testar

1. **Sessão isolada:** Kobe spawna agente com query simples
   - Verifica: leu SOUL.md? IDENTITY.md? AGENTS.md? Acessa memória?
2. **Primeiro cron:** Executar manualmente
   - Verifica: timeout correto? Output no tópico Telegram certo? Formato correto?
3. **Teste de escalação:** Simular situação bloqueada
   - Verifica: escala para Kobe? Formato de escalação conforme AGENTS.md?

---

## Verificação

- [ ] Todos os arquivos obrigatórios criados (IDENTITY, SOUL, AGENTS, TOOLS, MEMORY, HEARTBEAT)
- [ ] Frontmatter YAML válido em todos os arquivos
- [ ] Agente registrado no TEAM.md com L1
- [ ] Tópico Telegram criado e configurado
- [ ] Crons em BRT, não UTC
- [ ] Modelo = GPT 5.4 com fallback definido
- [ ] Memory structure criada (context/, sessions/, pending.md)
- [ ] Primeiro cron executou com sucesso
- [ ] Output apareceu no Telegram correto

## Troubleshooting

| Problema | Causa provável | Solução |
|----------|---------------|---------|
| Agente não responde | Config não carregada | `openclaw restart` na VPS |
| Cron não executa | Horário UTC em vez de BRT | Converter para BRT no schedule |
| Output no tópico errado | topicId incorreto | Verificar channelId/topicId no openclaw.json |
| Timeout em crons | Timeout insuficiente | Aumentar para 300-600s |
| Rate limit | Modelo sobrecarregado | Fallback chain deve engajar automaticamente |

## Referências

- [[openclaw/agents/rh/IDENTITY]] — template mais limpo (agente mais recente)
- [[openclaw/agents/kobe/AGENTS]] — governança completa
- [[openclaw/agents/kobe/SOUL]] — valores e tom
- [[automacoes/crons-index]] — índice de crons existentes
- [[projects/openclaw-vps]] — infraestrutura VPS
- [[knowledge/concepts/credenciais-map]] — credenciais 1Password

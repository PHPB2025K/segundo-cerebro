# MEMORY.md — Índice de Memória do Spark v2.0

> Agente: [[openclaw/agents/spark/IDENTITY|Spark]] | Orquestrador: [[openclaw/agents/kobe/AGENTS|Kobe Team]]

_Último update: 2026-03-20. Não duplica conteúdo — aponta pra onde está cada coisa._

---

## Índice de arquivos

- [[openclaw/agents/kobe/shared/spark/SOUL|SOUL]]
- [[openclaw/agents/kobe/shared/spark/IDENTITY|IDENTITY]]
- [[openclaw/agents/kobe/shared/spark/memory/accounts|Contas]]
- [[openclaw/agents/kobe/shared/spark/memory/campaigns/active|Campanhas Ativas]]
- [[openclaw/agents/kobe/shared/spark/memory/campaigns/history|Histórico de Campanhas]]
- [[openclaw/agents/kobe/shared/spark/memory/context/business|Contexto de Negócio]]
- [[openclaw/agents/kobe/shared/spark/memory/context/decisions|Decisões]]
- [[openclaw/agents/kobe/shared/spark/memory/pending|Pendências]]
- [[openclaw/agents/kobe/shared/spark/memory/playbook|Playbook]]

### Sessões
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-21|Sessão 2026-03-21]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-22|Sessão 2026-03-22]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-23|Sessão 2026-03-23]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-24|Sessão 2026-03-24]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-26|Sessão 2026-03-26]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-27|Sessão 2026-03-27]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-05|Sessão 2026-04-05]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-06|Sessão 2026-04-06]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-07|Sessão 2026-04-07]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-08|Sessão 2026-04-08]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-09|Sessão 2026-04-09]]
- [[openclaw/agents/kobe/shared/spark/memory/sessions/TEMPLATE|Template de Sessão]]

---

## Estrutura

```
shared/spark/
├── SOUL.md                    ← Quem eu sou (princípios, escopo, regras)
├── IDENTITY.md                ← Como opero (tom, protocolos, cadeia de comando)
├── MEMORY.md                  ← Este arquivo (índice + regras de memória)
├── memory/
│   ├── context/
│   │   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   │   ├── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
│   │   └── business.md        ← Contexto do negócio, metas, público, sazonalidade
│   ├── campaigns/
│   │   ├── active.md          ← Campanhas ativas com status e métricas
│   │   └── history.md         ← Campanhas encerradas + aprendizados de cada
│   ├── sessions/
│   │   └── YYYY-MM-DD.md      ← Notas diárias (expira 30 dias após consolidação)
│   ├── feedback/
│   │   └── reviews.json       ← Aprovações/rejeições do Kobe sobre outputs do Spark
│   ├── accounts.md            ← Contas de anúncio, IDs, pixels, acessos, tokens
│   └── playbook.md            ← Regras operacionais aprendidas (playbook vivo)
```

---

## Hierarquia de Memória (o que prevalece sobre o quê)

Quando dois arquivos se contradizem, prevalece o de maior prioridade:

| Prioridade | Arquivo | Motivo |
|---|---|---|
| 1 (máxima) | `decisions.md` | Decisões do Pedro/Kobe são absolutas e irrevogáveis |
| 2 | `SOUL.md` / `IDENTITY.md` | Princípios de identidade e protocolos operacionais |
| 3 | `playbook.md` | Regras aprendidas com dados reais da GB |
| 4 | `lessons.md` | Erros a não repetir |
| 5 | `feedback/reviews.json` | Histórico de aprovações/rejeições do Kobe |
| 6 (mínima) | `sessions/` | Contexto recente (volátil) |

**Regra de ouro:** Se uma decisão em `decisions.md` contradiz algo no `playbook.md`, a decisão vence. Sempre.

---

## Carregamento por Sessão

### Sempre carregado (boot obrigatório — toda vez que Spark é ativado)
- `SOUL.md` — identidade
- `IDENTITY.md` — protocolos
- `MEMORY.md` — este índice
- `memory/context/decisions.md` — decisões permanentes
- `memory/context/business.md` — contexto do negócio
- `memory/accounts.md` — contas e acessos
- `memory/playbook.md` — regras operacionais

### Carregado no boot (contexto recente)
- `memory/sessions/` — sessão de hoje + ontem (se existirem)
- `memory/campaigns/active.md` — campanhas que estão rodando

### Sob demanda (carregar quando necessário)
- `memory/context/lessons.md` — **ANTES** de recomendar qualquer mudança
- `memory/feedback/reviews.json` — **ANTES** de repetir abordagem que já usou
- `memory/campaigns/history.md` — quando analisar padrões ou comparar campanhas

---

## Ciclo de Evolução Contínua

### Após cada tarefa
Registrar em `sessions/YYYY-MM-DD.md`:
- O que foi feito
- Resultado obtido
- Qualquer aprendizado relevante

### Após cada feedback do Kobe
Registrar em `feedback/reviews.json`:
- ID da entrega
- Status (aprovado / rejeitado / revisão)
- Motivo do feedback
- O que mudar na próxima vez

### Após cada erro
Extrair lição e adicionar a `lessons.md`:
- Tag `[ESTRATÉGICA]` = permanente (erro de princípio)
- Tag `[TÁTICA]` = expira em 30 dias (erro de execução pontual)

### Quando descobrir padrão recorrente
Adicionar ao `playbook.md`:
- Padrão observado
- Dados que sustentam (mínimo 2 ocorrências)
- Regra operacional derivada
- Nível de confiança (Alta/Média/Baixa)

### Quando campanha encerrar
Mover de `active.md` → `history.md`:
- Métricas finais consolidadas
- O que funcionou / não funcionou
- Lição extraída (com referência cruzada ao `lessons.md`)

---

## Regra Inviolável — Extração ANTES de Compactação

Antes de consolidar ou arquivar qualquer sessão, **obrigatoriamente** executar nesta ordem:

1. Extrair decisões novas → `decisions.md`
2. Extrair lições → `lessons.md`
3. Atualizar campanhas → `campaigns/active.md` ou `history.md`
4. Atualizar playbook → `playbook.md` (se padrão novo descoberto)
5. Registrar feedback → `feedback/reviews.json`
6. **SÓ DEPOIS** compactar a sessão

**Compactar sem extrair = perder memória. Proibido.**

---

## Health Check de Memória

O Spark deve executar este checklist **semanalmente** (ou quando o Kobe solicitar):

```
⚡ HEALTH CHECK — Memória do Spark
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] decisions.md está atualizado? (última decisão registrada: [data])
[ ] lessons.md tem lições TÁTICAS expiradas? (remover se > 30 dias)
[ ] accounts.md — token Meta expira em quanto tempo? (🔴 se < 7 dias)
[ ] accounts.md — Google Ads integrado? (status atual)
[ ] playbook.md — benchmarks internos atualizados? (🟡 se > 30 dias sem update)
[ ] campaigns/active.md — reflete o que está rodando de verdade?
[ ] feedback/reviews.json — últimas entregas foram revisadas pelo Kobe?
[ ] sessions/ — sessões antigas (> 30 dias) foram consolidadas e extraídas?
[ ] Algum campo [PREENCHER] continua vazio? (listar quais)
```

Resultado entregue ao Kobe no formato padrão de relatório.

---

## Template de Sessão Diária

Cada novo dia de operação, criar `sessions/YYYY-MM-DD.md` com:

```markdown
# Sessão — YYYY-MM-DD

## Tarefas executadas
- [ ] [tarefa 1 — status]
- [ ] [tarefa 2 — status]

## Métricas observadas (se monitoramento ativo)
| Campanha | CPA | ROAS | CTR | Freq | Status |
|---|---|---|---|---|---|
| [nome] | R$X | Xx | X% | X.X | 🟢/🟡/🔴 |

## Alertas emitidos
- [nenhum / lista de alertas com nível]

## Feedback do Kobe
- [nenhum / feedback recebido + ação tomada]

## Aprendizados do dia
- [o que aprendi / nada novo]

## Pendências para amanhã
- [lista]
```

---

## Regra Final

**O que não tá escrito, não existe.**

- Não confiar em "memória de sessão" — arquivos são a única continuidade entre sessões
- Se importa, escreve em arquivo
- Nunca "notas mentais"
- Se Spark foi desligado e religado, o que está nos arquivos é tudo que ele sabe

---

_⚡ Memória do Spark é viva, estruturada e honesta. Dados reais, nunca achismo._

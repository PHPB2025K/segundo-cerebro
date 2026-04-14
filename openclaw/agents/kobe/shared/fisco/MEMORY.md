# MEMORY.md — Índice de Memória do Fisco v1.0

> Agente: [[openclaw/agents/fisco/IDENTITY|Fisco]] | Orquestrador: [[openclaw/agents/kobe/AGENTS|Kobe Team]]

_Último update: 2026-03-29. Não duplica conteúdo — aponta pra onde está cada coisa._

---

## Índice de arquivos

- [[openclaw/agents/kobe/shared/fisco/IDENTITY|IDENTITY]]
- [[openclaw/agents/kobe/shared/fisco/memory/accounts|Contas]]
- [[openclaw/agents/kobe/shared/fisco/memory/context/business|Contexto de Negócio]]
- [[openclaw/agents/kobe/shared/fisco/memory/context/decisions|Decisões]]
- [[openclaw/agents/kobe/shared/fisco/memory/decisions|Decisões (alt)]]
- [[openclaw/agents/kobe/shared/fisco/memory/lessons|Lições]]
- [[openclaw/agents/kobe/shared/fisco/memory/nfe-log|Log de NF-e]]
- [[openclaw/agents/kobe/shared/fisco/memory/pending|Pendências]]
- [[openclaw/agents/kobe/shared/fisco/memory/playbook|Playbook]]
- [[openclaw/agents/kobe/shared/fisco/memory/sessions/TEMPLATE|Template de Sessão]]
- [[openclaw/agents/kobe/shared/fisco/reference/session-nf-planning-20260331|Sessão NF Planning 31/03]]
- [[openclaw/agents/kobe/shared/fisco/templates/distribution-report|Template Distribuição]]
- [[openclaw/agents/kobe/shared/fisco/templates/reconciliation-report|Template Conciliação]]

---

## Estrutura

```
shared/fisco/
├── SOUL.md                    ← Quem eu sou (princípios, escopo, regras, fluxo operacional)
├── IDENTITY.md                ← Como opero (tom, protocolos, cadeia de comando, leveling)
├── MEMORY.md                  ← Este arquivo (índice + regras de memória)
├── config/
│   └── tax-rules.json         ← Regras fiscais configuráveis (validadas pelo contador)
├── memory/
│   ├── context/
│   │   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   │   ├── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
│   │   └── business.md        ← Contexto fiscal: calendário, datas SEFAZ, sazonalidade
│   ├── sessions/
│   │   ├── TEMPLATE.md        ← Template padrão para registros de operação
│   │   └── YYYY-MM-DD.md      ← Notas por operação (expira 30 dias após consolidação)
│   ├── feedback/
│   │   └── reviews.json       ← Aprovações/rejeições do Kobe sobre outputs do Fisco
│   ├── accounts.md            ← Bling OAuth, endpoints, CNPJs, status de integração
│   └── playbook.md            ← Regras operacionais aprendidas (benchmarks fiscais)
├── skills/
│   ├── distribution/          ← Módulo A: Motor de Distribuição
│   ├── nf-transfer/           ← Módulo B: NF Transferência Matriz→Filial
│   ├── nf-internal/           ← Módulo C: NFs Venda Interna Filial→Simples
│   ├── reconciliation/        ← Módulo D: Conciliação Fisco
│   └── simples-monitor/       ← Módulo E: Monitor de Limites Simples
└── templates/
    ├── distribution-report.md  ← Template relatório de distribuição
    └── reconciliation-report.md ← Template relatório de conciliação
```

---

## Hierarquia de Memória (o que prevalece sobre o quê)

Quando dois arquivos se contradizem, prevalece o de maior prioridade:

| Prioridade | Arquivo | Motivo |
|---|---|---|
| 1 (máxima) | `decisions.md` | Decisões do Pedro/Kobe/Suellen são absolutas |
| 2 | `config/tax-rules.json` | Regras fiscais validadas pelo contador |
| 3 | `SOUL.md` / `IDENTITY.md` | Princípios de identidade e protocolos |
| 4 | `playbook.md` | Regras aprendidas com operações reais |
| 5 | `lessons.md` | Erros a não repetir |
| 6 | `feedback/reviews.json` | Histórico de aprovações/rejeições do Kobe |
| 7 (mínima) | `sessions/` | Contexto recente (volátil) |

**Regra de ouro:** Se uma decisão em `decisions.md` contradiz algo no `playbook.md`, a decisão vence. Se `tax-rules.json` contradiz qualquer outro arquivo, o config vence (foi validado pelo contador).

---

## Carregamento por Sessão

### Sempre carregado (boot obrigatório — toda vez que Fisco é ativado)
- `SOUL.md` — identidade e escopo
- `IDENTITY.md` — protocolos operacionais
- `MEMORY.md` — este índice
- `memory/context/decisions.md` — decisões permanentes
- `memory/context/business.md` — contexto fiscal do negócio
- `memory/accounts.md` — contas, acessos e integrações
- `config/tax-rules.json` — regras fiscais vigentes

### Carregado no boot (contexto recente)
- `memory/sessions/` — sessão de hoje + ontem (se existirem)
- `memory/pending.md` — pendências fiscais

### Sob demanda (carregar quando necessário)
- `memory/context/lessons.md` — **ANTES** de executar qualquer módulo
- `memory/feedback/reviews.json` — **ANTES** de repetir abordagem já usada
- `memory/playbook.md` — quando precisar de benchmarks ou padrões históricos

---

## Ciclo de Evolução Contínua

### Após cada operação fiscal
Registrar em `sessions/YYYY-MM-DD.md`:
- Módulo executado (A/B/C/D/E)
- Dados de entrada e resultado
- Exceções encontradas
- Tempo de execução

### Após cada feedback do Kobe
Registrar em `feedback/reviews.json`:
- ID da entrega
- Módulo
- Status (aprovado / rejeitado / revisão)
- Motivo do feedback
- O que mudar na próxima vez

### Após cada erro
Extrair lição e adicionar a `lessons.md`:
- Tag `[ESTRATÉGICA]` = permanente (erro de princípio fiscal)
- Tag `[TÁTICA]` = expira em 30 dias (erro de execução pontual)

### Quando descobrir padrão recorrente
Adicionar ao `playbook.md`:
- Padrão observado (ex: distribuição histórica por CNPJ)
- Dados que sustentam (mínimo 2 operações)
- Regra operacional derivada
- Nível de confiança (Alta/Média/Baixa)

### Quando importação for processada
Registrar em `playbook.md`:
- Distribuição calculada (% por CNPJ)
- Quantidade total e por CNPJ
- Tempo de processamento
- Exceções encontradas

---

## Health Check de Memória

O Fisco deve executar este checklist **quinzenalmente** (ou quando o Kobe solicitar):

```
📋 HEALTH CHECK — Memória do Fisco
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] decisions.md está atualizado? (última decisão: [data])
[ ] lessons.md tem lições TÁTICAS expiradas? (remover se > 30 dias)
[ ] accounts.md — OAuth Bling válido? (🔴 se expirado ou ausente)
[ ] accounts.md — status de integração atualizado?
[ ] tax-rules.json — parâmetros conferidos com o último input da Suellen?
[ ] playbook.md — benchmarks de distribuição atualizados? (🟡 se > 60 dias sem update)
[ ] pending.md — bloqueios resolvidos foram removidos?
[ ] sessions/ — sessões antigas (> 30 dias) foram consolidadas e extraídas?
[ ] feedback/reviews.json — últimas entregas foram revisadas pelo Kobe?
[ ] Limites Simples — última verificação há menos de 7 dias?
```

Resultado entregue ao Kobe no formato padrão.

---

## Regra Inviolável — Extração ANTES de Compactação

Antes de consolidar ou arquivar qualquer sessão, **obrigatoriamente** executar nesta ordem:

1. Extrair decisões fiscais novas → `decisions.md`
2. Extrair lições → `lessons.md`
3. Atualizar playbook → `playbook.md` (se padrão novo descoberto)
4. Registrar feedback → `feedback/reviews.json`
5. Atualizar pending → `pending.md`
6. **SÓ DEPOIS** compactar a sessão

**Compactar sem extrair = perder memória fiscal. Proibido.**

---

## Regra Final

**O que não tá escrito, não existe.**

- Não confiar em "memória de sessão" — arquivos são a única continuidade
- Se importa, escreve em arquivo
- Nunca "notas mentais"
- Se Fisco foi desligado e religado, o que está nos arquivos é tudo que ele sabe
- Em matéria fiscal, precisão é inegociável — registrar tudo com rastreabilidade

---

_Memória do Fisco é auditável, estruturada e precisa. Cada operação registrada, cada exceção documentada._

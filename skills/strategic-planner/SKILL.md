# Skill: Strategic Planner

## Metadata
- **Name:** strategic-planner
- **Version:** 1.0
- **Created:** 2026-03-20
- **Purpose:** Framework obrigatório de planejamento estratégico antes de executar tarefas

## Description
Skill de planejamento que força uma pausa estruturada antes de agir. Classifica a complexidade da tarefa em 3 níveis e aplica profundidade proporcional. Garante que toda ação relevante tenha objetivo claro, dependências mapeadas, riscos identificados e critérios de sucesso definidos.

---

## Hard Rules (INVIOLÁVEIS)
1. **NUNCA** usar modelo diferente de claude-opus-4-6 para tarefas de planejamento.
2. **NUNCA** entregar um plano sem processamento de extended thinking ativo.
3. **NUNCA** produzir steps vagos como "pesquisar o mercado" sem especificar O QUÊ pesquisar, ONDE, COMO e qual o ENTREGÁVEL esperado.
4. **SEMPRE** default em Português (Brasil) a menos que o usuário escreva explicitamente em outro idioma.
5. **SEMPRE** priorizar profundidade sobre velocidade. Um plano completo entregue em 60s é infinitamente melhor que um raso em 10s.

---

## Trigger Conditions

### Trigger Explícito (qualquer nível)
Ativa quando o usuário pede qualquer forma de: planejamento, estratégia, roadmap, plano de ação, cronograma, roteiro, estruturação de projeto, ou similar.

### Trigger Implícito (apenas nível Lite)
Ativa quando o contexto implica necessidade de planejamento, mesmo sem pedido explícito:
- Pedidos envolvendo múltiplos steps com dependências entre si
- Solicitações de lançamento, migração, expansão, reestruturação
- "Como eu faço pra...", "Preciso organizar...", "Me ajuda a estruturar..."

**Regra:** Trigger implícito NUNCA ativa Standard ou Deep automaticamente. Só Lite. Eu escalo se a complexidade justificar, informando o Pedro.

---

## Sistema de Níveis

### Classificação (Phase 0)

| Nível | Critérios | Thinking |
|---|---|---|
| **Lite** | <5 steps, sem dependências externas, conclusão <1 dia, escopo claro | Extended (curto) |
| **Standard** | Múltiplas fases, 1-4 semanas, dependências moderadas, 1-2 stakeholders | Extended (médio) |
| **Deep** | Projeto complexo, multi-stakeholder, >2 semanas, riscos reais, impacto financeiro/operacional | Extended (máximo) |

**Gate de Aprovação:**
- **Lite:** Executo direto após entregar o plano
- **Standard:** Executo direto após entregar o plano
- **Deep:** **ESPERO APROVAÇÃO EXPLÍCITA** do Pedro antes de qualquer execução

**Escalação:** Se durante o planejamento eu perceber que o nível classificado é insuficiente, informo e escalo. Nunca desescalo sem avisar.

---

## Integração com Memória (OBRIGATÓRIO)

### Antes de planejar — consultar:
1. `memory/context/decisions.md` — NUNCA contradizer decisões existentes
2. `memory/context/lessons.md` — NUNCA repetir erros documentados
3. `memory/feedback/` — NUNCA sugerir abordagens já rejeitadas
4. `memory/projects/` — contexto do projeto se existir

### Depois de aprovar — salvar:
- Plano aprovado → `memory/projects/[nome-do-projeto].md` (atualizar ou criar)
- Decisões tomadas durante planejamento → `memory/context/decisions.md`
- Se aplicável, atualizar `memory/pending.md` com próximos passos

---

## Execution Protocol

### Phase 0 — Classificação & Deep Reasoning
1. Ativar extended thinking
2. Classificar nível (Lite / Standard / Deep)
3. Considerar no mínimo 3 abordagens alternativas antes de selecionar a ótima
4. Consultar memória (decisions, lessons, feedback)
5. Se nível Deep: informar Pedro que será plano completo com gate de aprovação

### Phase 1 — Context & Objective Mapping
- Restatar o objetivo do Pedro em termos precisos
- Identificar: objetivo principal, objetivos secundários, restrições implícitas
- Fazer perguntas clarificadoras APENAS se informação crítica estiver faltando e não puder ser razoavelmente inferida
- Se assumir algo, flaggear explicitamente como `[PREMISSA]`

### Phase 2 — Variable & Dependency Analysis
*(Standard e Deep apenas)*
- Mapear TODAS as variáveis relevantes que influenciam o resultado
- Identificar dependências entre tarefas (o que bloqueia o quê)
- Flaggear itens de caminho crítico — tarefas onde atraso cascateia pro plano inteiro
- Classificar riscos: Baixo / Médio / Alto / Crítico (probabilidade × impacto)

### Phase 3 — Scenario Modeling
*(Deep apenas)*
- Definir no mínimo:
  - **Cenário otimista** (premissas favoráveis)
  - **Cenário base** (premissas realistas)
  - **Cenário pessimista** (premissas desfavoráveis)
- Para cada risco Alto/Crítico: plano de contingência com trigger conditions ("se X acontecer, fazer Y")

### Phase 4 — Plan Generation
- Usar template correspondente ao nível:
  - Lite → `references/template-lite.md`
  - Standard → `references/template-standard.md`
  - Deep → `references/template-deep.md`

### Phase 5 — Self-Audit
Antes de entregar, verificar internamente:
- [ ] Cada tarefa tem critério de conclusão claro?
- [ ] Cada step especifica O QUÊ, ONDE, COMO e ENTREGÁVEL?
- [ ] Nenhum step é ambíguo o suficiente pra causar dúvida na execução?
- [ ] Dependências estão explicitamente mapeadas? *(Standard+)*
- [ ] Riscos têm contingências? *(Deep)*
- [ ] O plano poderia ser entregue a alguém com zero contexto e ainda ser executável?
- [ ] Nenhuma decisão existente foi contradita?
- [ ] Nenhum erro documentado em lessons.md foi repetido?
- [ ] Nenhuma abordagem rejeitada em feedback/ foi resugerida?

Se qualquer check falhar → revisar antes de entregar.

### Phase 6 — Delivery & Persistence
1. Entregar plano ao Pedro
2. Se Deep: aguardar aprovação explícita
3. Após aprovação (ou entrega no Lite/Standard):
   - Salvar em `memory/projects/`
   - Atualizar `memory/context/decisions.md` se houver decisões novas
   - Atualizar `memory/pending.md` se houver próximos passos

---

## Anti-Patterns (NUNCA fazer)

- ❌ Entregar plano sem extended thinking
- ❌ Steps como "pesquisar concorrentes" sem dizer quais, onde, como
- ❌ Ignorar decisões passadas do Pedro
- ❌ Repetir abordagens já rejeitadas no feedback
- ❌ Aplicar Deep em tarefa que é claramente Lite (over-planning)
- ❌ Aplicar Lite em tarefa que é claramente Deep (under-planning)
- ❌ Executar plano Deep sem aprovação explícita
- ❌ Planejar sem consultar memória primeiro

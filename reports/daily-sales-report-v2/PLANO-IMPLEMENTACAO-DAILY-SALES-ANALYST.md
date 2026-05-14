# Plano de Implementação — Daily Sales Analyst

**Projeto:** Daily Sales Report v2.5 — Pipeline em 7 camadas  
**Arquitetura aprovada:** Trader como dono/orquestrador; Daily Sales Analyst como executor especializado; Kobe como governança/QA final em bloqueios e rollout.  
**Status:** Planejamento aprovado para orientar implementação faseada.  
**Data:** 14/05/2026

---

## 1. Visão Geral da Arquitetura

O novo pipeline do **Daily Sales Report enviado aos funcionários** será operado por um subagente especializado chamado **Daily Sales Analyst**.

A hierarquia operacional fica assim:

- **Trader**: dono/orquestrador do Daily Sales Report.
- **Daily Sales Analyst**: executor especializado das 7 camadas analíticas.
- **Kobe**: governança, QA final em bloqueios, rollout e mudanças estratégicas.
- **Cron**: aciona o Trader, não o Daily Sales Analyst diretamente.
- **Envio Slack**: feito pelo Trader apenas após retorno aprovado do Daily Sales Analyst.

O Daily Sales Analyst **não tem autonomia de canal**. Ele não fala com Pedro, não fala com funcionários e não envia Slack sozinho. Ele devolve ao Trader:

- análises das 7 camadas;
- veredito QA;
- payload Slack pronto;
- bloqueios;
- ressalvas;
- memória sugerida;
- status final.

---

## 2. Decisão de Arquitetura

A decisão aprovada é manter o **Trader como dono/orquestrador** e criar o **Daily Sales Analyst como executor especializado**.

### Por que não rodar independente?

Rodar independente criaria um segundo dono paralelo para:

- memória de marketplace;
- regras comerciais;
- exceções por plataforma;
- qualidade das análises;
- integração com Himmel/Pedro/Kobe;
- envio dos relatórios.

Isso aumentaria o risco de drift e transformaria o cron em um “script inteligente solto”, sem contexto operacional suficiente.

### Por que como subagente do Trader?

Porque o Daily Sales Report é parte da operação de marketplace. O Trader deve continuar sendo o dono da rotina, enquanto o Daily Sales Analyst concentra o raciocínio pesado em camadas.

Vantagens:

- mantém memória e responsabilidade dentro do domínio do Trader;
- isola o pipeline pesado sem poluir o Trader principal;
- facilita evoluir prompts, regras e QA;
- reduz risco de envio errado;
- mantém governança clara.

---

## 3. Pipeline Analítico em 7 Camadas

O Daily Sales Analyst executa as camadas nesta ordem:

1. **Estratégica**  
   Lê trajetória, contexto histórico, riscos estruturais e tese do momento.

2. **Tática**  
   Transforma leitura estratégica em decisões de atenção e prioridades possíveis.

3. **Operacional**  
   Analisa a execução do dia: pedidos, faturamento, ticket, cancelamentos, mix, contas e comportamento prático.

4. **Granular**  
   Faz investigação forense: produto certo, ASIN correto, shop_id, divergências, concentração, riscos de identificação e microevidências.

5. **Condensadora**  
   Corta o excesso e decide o que realmente merece sobreviver para a mensagem final.

6. **Slack Writer**  
   Transforma a saída aprovada da Condensadora em mensagem Slack no template final.

7. **QA Gate**  
   Valida estrutura, fidelidade, segurança dos dados, ausência de SKU cru, ausência de análise rasa e bloqueios.

---

## 4. Fase 1 — Estrutura do Workspace e Identidade

### Objetivo

Criar o Daily Sales Analyst como agente completo, não apenas como um conjunto de prompts chamados em sequência.

### Escopo

- Criar workspace próprio.
- Definir identidade, papel, limites e hierarquia.
- Registrar relação com Trader, Kobe e Pedro.
- Estabelecer que o agente não tem autonomia de canal.

### Entregáveis

Estrutura sugerida:

```text
shared/daily-sales-analyst/
├── IDENTITY.md
├── SOUL.md
├── AGENTS.md
├── MEMORY.md
├── prompts/
├── memory/
│   ├── accounts/
│   ├── rules/
│   ├── context/
│   └── executions/
├── runs/
├── handoff/
└── README.md
```

Arquivos principais:

- `IDENTITY.md` — quem é o agente, escopo, limites.
- `SOUL.md` — estilo analítico, postura, princípios de decisão.
- `AGENTS.md` — regras operacionais e relação com Trader/Kobe.
- `MEMORY.md` — índice da memória própria.
- `README.md` — visão geral de operação.

### Critérios de saída

- O agente existe como entidade completa.
- Escopo fechado: executor das 7 camadas.
- Sem autonomia de canal.
- Trader confirmado como dono/orquestrador.
- Kobe confirmado como governança/QA final.

### Checkpoint Kobe

Kobe valida se:

- a identidade não conflita com Trader;
- o agente não ganhou autonomia indevida;
- os limites de envio e comunicação estão claros;
- a hierarquia está consistente.

---

## 5. Fase 2 — Prompts e Memória Operacional

### Objetivo

Organizar os 7 prompts aprovados e criar uma base de memória estável para o Daily Sales Analyst.

### Escopo

- Versionar os 7 prompts dentro do workspace do agente.
- Criar memória por conta/plataforma.
- Registrar regras de marketplace.
- Registrar responsáveis e contexto operacional.
- Registrar relação com Himmel/Pedro/Kobe.

### Entregáveis

Prompts:

```text
prompts/
├── 01-estrategica.md
├── 02-tatica.md
├── 03-operacional.md
├── 04-granular.md
├── 05-condensadora.md
├── 06-slack-writer.md
└── 07-qa-gate.md
```

Memória por conta:

```text
memory/accounts/
├── shopee-budamix-store/
│   ├── daily.md
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── shopee-budamix-oficial-2/
│   ├── daily.md
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── shopee-budamix-shop-3/
│   ├── daily.md
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── mercado-livre/
│   ├── daily.md
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
└── amazon/
    ├── daily.md
    ├── weekly.md
    ├── monthly.md
    └── rules.md
```

Contexto operacional:

```text
memory/context/
├── responsaveis.md
├── contas-shopee.md
├── himmel.md
├── marketplace-rules.md
├── slack-format.md
└── qa-standards.md
```

### Regras críticas a registrar

- Lucas = Shopee, com separação obrigatória por `shop_id`.
- Yasmin = Mercado Livre.
- Leonardo = Amazon.
- Shopee nunca deve ser analisada como bloco único quando o diagnóstico depende das contas.
- Amazon deve usar pedido real + ASIN/platform_item_id + título real como fonte primária.
- Alias manual de SKU nunca é fonte primária.
- Produto visível nunca deve ser SKU cru.
- Atacado/Bling fica fora do report individual dos funcionários.
- Todo período deve ser BRT: 00:00–23:59 America/Sao_Paulo.

### Critérios de saída

- Os 7 prompts estão versionados e organizados.
- Cada conta tem memória própria.
- As regras críticas estão explícitas.
- O agente consegue operar com contexto estável, não só com prompt isolado.

### Checkpoint Kobe

Kobe valida se:

- regras de Shopee, ML e Amazon estão corretas;
- responsáveis foram mapeados corretamente;
- memória por conta não duplica ou conflita com a memória do Trader;
- handoff com Trader continua limpo.

---

## 6. Fase 3 — Integração com Trader

### Objetivo

Definir o contrato formal de delegação entre Trader e Daily Sales Analyst.

### Escopo

- Criar input schema.
- Criar output schema.
- Definir quando o Trader chama o Daily Sales Analyst.
- Definir o que o Daily Sales Analyst devolve.
- Definir quando Trader envia, bloqueia ou escala para Kobe.

### Entregáveis

```text
handoff/
├── TRADER-CONTRACT.md
├── input-schema.json
├── output-schema.json
├── examples/
│   ├── input-example.json
│   └── output-example.json
└── escalation-rules.md
```

### Input esperado do Trader

O Trader envia:

- data analisada;
- plataforma/responsável;
- pacote de dados validado;
- memória relevante;
- regras ativas;
- contexto Himmel/marketplace quando aplicável;
- modo de execução: `dry-run`, `preview`, `shadow`, `send-candidate`.

### Output esperado do Daily Sales Analyst

O agente devolve:

```text
status: APPROVED | APPROVED_WITH_REMARKS | BLOCKED
send_real_allowed: true | false
recipient: Lucas | Yasmin | Leonardo
platform: Shopee | Mercado Livre | Amazon
date: YYYY-MM-DD
layers:
  01_strategic
  02_tactical
  03_operational
  04_granular
  05_condenser
  06_slack_writer
  07_qa_gate
slack_payload:
  text
  blocks opcional
qa:
  status
  errors
  warnings
memory_updates:
  suggested
  applied
escalation:
  required
  reason
```

### Critérios de saída

- Trader sabe exatamente como delegar.
- Daily Sales Analyst sabe exatamente o que devolver.
- Envio real continua pertencendo ao Trader.
- Bloqueios e ressalvas têm formato padronizado.

### Checkpoint Kobe

Kobe valida o contrato antes de codar o runner definitivo.

---

## 7. Fase 4 — Pipeline Ponta a Ponta em Dry-run

### Objetivo

Executar as 7 camadas em sequência usando o Daily Sales Analyst, sem envio real.

### Escopo

- Criar runner dry-run.
- Executar as 7 camadas na ordem correta.
- Salvar artefatos auditáveis por data e destinatário.
- Manter `send_real_allowed=false`.

### Entregáveis

Estrutura de execução:

```text
runs/YYYY-MM-DD/
├── manifest.json
├── lucas/
│   ├── 01-estrategica.md
│   ├── 02-tatica.md
│   ├── 03-operacional.md
│   ├── 04-granular.json
│   ├── 05-condensadora.json
│   ├── 06-slack-preview.md
│   └── 07-qa.json
├── yasmin/
│   └── ...
└── leonardo/
    └── ...
```

Runner:

```text
scripts/daily-sales-analyst-runner.py
```

Modos:

- `--dry-run`
- `--shadow`
- `--preview`

Nesta fase, todos devem manter envio real bloqueado.

### Critérios de saída

- Rodada completa para Lucas, Yasmin e Leonardo.
- As 7 camadas são geradas e salvas.
- QA bloqueia análise rasa ou genérica.
- Nenhum Slack real é enviado.
- `send_real_allowed=false` em todos os manifests.

### Checkpoint Kobe

Kobe revisa uma rodada completa antes de avançar para validação em múltiplos dias.

---

## 8. Fase 5 — Validação com Dados Reais e Ajuste Fino

### Objetivo

Validar o novo pipeline com dados reais antes de qualquer envio para funcionários.

### Escopo

- Rodar shadow em 3 a 5 datas reais.
- Comparar contra o report atual.
- Avaliar profundidade, segurança e utilidade.
- Ajustar prompts, regras e memória.

### Entregáveis

```text
validation/
├── shadow-runs-summary.md
├── quality-matrix.md
├── issues-found.md
├── fixes-applied.md
└── approval-candidate.md
```

### Matriz de avaliação

Cada rodada deve ser avaliada por:

- profundidade da análise;
- fidelidade aos dados;
- ausência de SKU cru;
- produto correto;
- ASIN/título correto na Amazon;
- separação correta das contas Shopee;
- ausência de mistura de plataformas;
- prioridades realmente acionáveis;
- bloqueios corretos;
- clareza do Slack final;
- utilidade para Lucas/Yasmin/Leonardo.

### Critérios de saída

- Pelo menos 3 execuções reais em shadow.
- QA aprovado ou aprovado com ressalva em todas.
- Zero caso de produto errado.
- Zero SKU cru visível.
- Zero prioridade genérica.
- Zero mistura de plataforma.
- Kobe aprova o padrão final.

### Checkpoint Kobe

Obrigatório antes de qualquer envio real.

---

## 9. Fase 6 — Rollout Supervisionado

### Objetivo

Colocar o novo pipeline em operação controlada, ainda com supervisão.

### Escopo

- Cron aciona Trader.
- Trader chama Daily Sales Analyst.
- Daily Sales Analyst devolve payload e QA.
- Primeiro ciclo envia preview para Kobe/Pedro.
- Depois libera envio real supervisionado.

### Entregáveis

- Cron atualizado para o fluxo Trader → Daily Sales Analyst.
- Modo `--preview-to-kobe`.
- Modo `--send-real` protegido por QA.
- Registro em `sent-reports.md`.
- Alerta automático em caso de `BLOCKED`.

### Proteções obrigatórias

- Se QA = `BLOCKED`, não envia.
- Se houver erro de dados, não envia.
- Se houver produto inseguro, não cita nominalmente.
- Se houver SKU cru visível, bloqueia.
- Se houver prioridade genérica, bloqueia.
- Se `send_real_allowed=false`, não envia.

### Critérios de saída

- 1 execução preview aprovada.
- 1 execução real supervisionada aprovada.
- Logs completos.
- Memória atualizada.
- Nenhum envio externo fora do fluxo Trader.

### Checkpoint Kobe

Kobe precisa aprovar explicitamente a retomada do envio real.

---

## 10. Fase 7 — Operação em Produção

### Objetivo

Rodar diariamente com autonomia controlada.

### Escopo

- Cron diário definitivo.
- Trader orquestra.
- Daily Sales Analyst executa.
- Trader envia se aprovado.
- Kobe só entra em bloqueio, mudança estratégica ou rollout novo.

### Entregáveis

- Cron definitivo às 06:50 BRT.
- Rotina diária de execução.
- Consolidação semanal.
- Consolidação mensal.
- Rules Watch integrado.
- Contexto Himmel/Granola integrado quando relevante.
- Playbook de falha.

### Critérios de saída

- Cron roda sem intervenção manual.
- Se QA aprova, Trader envia.
- Se QA bloqueia, Trader não envia e escala Kobe.
- Toda execução fica auditável.
- Memória diária/semanal/mensal é atualizada.

---

## 11. Estados Permitidos do Pipeline

### `DRY_RUN`

- Gera análise.
- Não envia Slack.
- Pode usar dados reais.
- Serve para desenvolvimento.

### `SHADOW`

- Gera análise como se fosse produção.
- Não envia Slack.
- Salva logs completos.
- Usado para validação.

### `PREVIEW_TO_KOBE`

- Gera payload final.
- Envia apenas para Kobe/Pedro revisar.
- Funcionários não recebem.

### `SEND_CANDIDATE`

- Gera payload com intenção de envio.
- Só envia se QA aprovar e `send_real_allowed=true`.

### `PRODUCTION_SEND`

- Fluxo normal de produção.
- Trader envia para funcionários após aprovação do QA.

---

## 12. Critérios Globais de Bloqueio

O pipeline deve bloquear envio se ocorrer qualquer um destes casos:

- dados incompletos ou divergentes sem resolução;
- período errado ou timezone errado;
- mistura de plataformas;
- Shopee analisada sem separar contas quando isso afeta diagnóstico;
- Amazon citando produto sem pedido real/ASIN/título confiável;
- SKU cru visível no Slack;
- produto com risco alto de identificação citado nominalmente;
- prioridade genérica sem evidência;
- análise apenas descritiva, sem tese;
- Slack Writer reintroduzindo seção proibida;
- QA Gate com status `BLOCKED`;
- `send_real_allowed=false`;
- erro no handoff Trader ↔ Daily Sales Analyst.

---

## 13. Estrutura Final Recomendada do Agente

```text
shared/daily-sales-analyst/
├── README.md
├── IDENTITY.md
├── SOUL.md
├── AGENTS.md
├── MEMORY.md
├── prompts/
│   ├── 01-estrategica.md
│   ├── 02-tatica.md
│   ├── 03-operacional.md
│   ├── 04-granular.md
│   ├── 05-condensadora.md
│   ├── 06-slack-writer.md
│   └── 07-qa-gate.md
├── memory/
│   ├── accounts/
│   │   ├── shopee-budamix-store/
│   │   ├── shopee-budamix-oficial-2/
│   │   ├── shopee-budamix-shop-3/
│   │   ├── mercado-livre/
│   │   └── amazon/
│   ├── context/
│   │   ├── responsaveis.md
│   │   ├── contas-shopee.md
│   │   ├── himmel.md
│   │   ├── marketplace-rules.md
│   │   ├── slack-format.md
│   │   └── qa-standards.md
│   ├── rules/
│   └── executions/
├── handoff/
│   ├── TRADER-CONTRACT.md
│   ├── input-schema.json
│   ├── output-schema.json
│   ├── escalation-rules.md
│   └── examples/
├── runs/
└── validation/
```

---

## 14. Ordem Recomendada de Execução

A ordem recomendada é:

1. **Fase 1 + Fase 2 juntas**  
   Criar fundação do agente, identidade, prompts e memória.

2. **Fase 3**  
   Definir contrato formal com Trader.

3. **Fase 4**  
   Rodar pipeline em dry-run.

4. **Fase 5**  
   Validar com múltiplos dias reais.

5. **Fase 6**  
   Rollout supervisionado.

6. **Fase 7**  
   Produção contínua.

---

## 15. Recomendação Final

O próximo passo deve ser implementar **Fase 1 + Fase 2** antes de mexer no runner definitivo.

Motivo: se o runner for codado antes do Daily Sales Analyst existir como agente completo, o projeto vira apenas um script com prompts. O ganho real vem de criar um agente com:

- identidade clara;
- memória própria;
- regras versionadas;
- logs auditáveis;
- contrato formal com Trader;
- limites operacionais bem definidos.

Depois disso, o runner passa a executar um agente de verdade, não apenas uma sequência solta de prompts.

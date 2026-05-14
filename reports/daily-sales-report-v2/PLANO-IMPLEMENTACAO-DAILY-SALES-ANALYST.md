# Plano Definitivo de Implementação — Daily Sales Analyst

**Projeto:** Daily Sales Report v2.5 — Pipeline em camadas para Sales Report dos funcionários  
**Arquitetura aprovada:** Trader como dono/orquestrador; Daily Sales Analyst como executor especializado; Kobe como governança/QA final em bloqueios e rollout.  
**Status:** Definitivo para início da implementação.  
**Data:** 14/05/2026

---

## 1. Decisão Arquitetural

O **Daily Sales Report enviado aos funcionários** será operado por um novo subagente especializado chamado **Daily Sales Analyst**.

A hierarquia operacional aprovada é:

- **Trader**: dono/orquestrador do Daily Sales Report.
- **Daily Sales Analyst (DSA)**: executor especializado do pipeline analítico.
- **Kobe**: governança, QA final em bloqueios, mudanças estratégicas e rollout.
- **Cron**: aciona o Trader, não o DSA diretamente.
- **Envio Slack**: feito pelo Trader apenas após retorno aprovado do DSA.

O DSA **não tem autonomia de canal**:

- não fala com Pedro;
- não fala com funcionários;
- não envia Slack sozinho;
- não toma decisão de rollout;
- não altera regra permanente sem governança.

Ele devolve ao Trader:

- pacote de análise das camadas;
- veredito QA;
- payload Slack pronto;
- status por destinatário/plataforma;
- bloqueios;
- ressalvas;
- memória sugerida/aplicada;
- logs auditáveis.

---

## 2. Motivo da Arquitetura

Rodar o Daily Sales Analyst de forma independente criaria um segundo dono paralelo para:

- memória de marketplace;
- regras comerciais;
- exceções por plataforma;
- qualidade das análises;
- integração com Himmel/Pedro/Kobe;
- envio dos relatórios.

Isso aumentaria o risco de drift e transformaria o cron em um “script inteligente solto”, sem contexto operacional suficiente.

Como subagente operacional do Trader, o DSA concentra o raciocínio pesado sem tirar do Trader a responsabilidade de marketplace.

Vantagens:

- mantém memória e responsabilidade no domínio do Trader;
- isola o pipeline pesado em agente próprio;
- facilita evoluir prompts, regras e QA;
- reduz risco de envio errado;
- permite rollback/versionamento de prompts;
- preserva governança clara.

---

## 3. Pipeline Final — Layer 0 + 7 Camadas

O pipeline definitivo tem **Layer 0 determinístico** e **7 camadas analíticas com LLM**.

### Layer 0 — Data Builder / Data Readiness

Componente determinístico. Não usa LLM.

Responsável por produzir o pacote validado de dados consumido pelas camadas analíticas.

### Camadas analíticas

1. **Estratégica**  
   Interpreta trajetória, qualidade da base, riscos estruturais e tese do momento.

2. **Tática**  
   Transforma leitura estratégica em foco de decisão e prioridades possíveis.

3. **Operacional**  
   Analisa execução do dia: pedidos, faturamento, ticket, cancelamentos, mix, contas, fulfillment e comportamento prático.

4. **Granular**  
   Faz investigação forense: produto certo, ASIN correto, shop_id, divergências, concentração e risco de identificação.

5. **Condensadora**  
   Corta excesso e decide o que realmente merece sobreviver para a mensagem final.

6. **Slack Writer**  
   Transforma a saída aprovada da Condensadora em mensagem Slack no template final.

7. **QA Gate**  
   Valida estrutura, fidelidade, segurança dos dados, ausência de SKU cru, ausência de análise rasa e bloqueios.

---

## 4. Fase 0 — Layer 0: Data Builder & Data Readiness

### Objetivo

Criar a camada determinística responsável por consultar, validar e empacotar os dados antes de qualquer LLM interpretar algo.

Essa fase existe porque o maior risco técnico do report está no input:

- timezone;
- fonte canônica;
- separação Shopee por shop_id;
- divergência entre fontes;
- status/cancelamentos atrasados;
- latência de sync;
- top produtos calculados por fonte errada;
- identificação incorreta de produto.

### Princípio

O Layer 0 **não usa LLM**.

Os 7 prompts assumem dado estável e auditável. Qualquer não-determinismo no Layer 0 contaminaria todas as camadas posteriores.

### Escopo

O Data Builder deve produzir um `package.json` validado contendo:

- data analisada em BRT;
- janela `00:00–23:59 America/Sao_Paulo`;
- fonte canônica `orders`;
- totais por plataforma;
- totais por conta Shopee;
- pedidos válidos;
- cancelamentos separados;
- top produtos por pedido real;
- ASIN/platform_item_id/título real quando disponível;
- histórico 7d/30d/60d;
- concentração top 3/top 5;
- flags de qualidade;
- última sincronização por marketplace;
- reconciliação entre fontes quando aplicável;
- status de Data Readiness.

### Critério objetivo de Data Readiness

O Layer 0 retorna um destes estados:

```text
DADOS_OK
DADOS_PARCIAIS
NOT_READY
```

#### DADOS_OK

Condições:

- todas as fontes necessárias sincronizadas nas últimas 4h;
- volume dentro da banda 30d: entre -40% e +40% da média;
- zero divergências críticas detectadas;
- timezone BRT validado;
- fonte canônica disponível;
- Shopee separada corretamente por `shop_id`;
- Amazon com identificação segura por pedido real quando produtos forem citados.

Resultado:

- pipeline pode rodar normalmente;
- `data_quality = ok`;
- camadas podem operar com confiança normal.

#### DADOS_PARCIAIS

Condição quando uma ou mais ocorrerem:

- uma fonte com latência entre 4h e 8h;
- volume fora da banda 30d, mas dentro da banda 60d;
- divergência menor entre fontes do mesmo dado, abaixo de 5%;
- algum dado secundário ausente sem comprometer totais principais;
- qualidade suficiente para análise, mas com ressalva.

Resultado:

- pipeline pode rodar;
- `data_quality = partial`;
- Estratégica deve reduzir confiança da tese;
- Condensadora deve preservar ressalva se afetar leitura;
- QA pode aprovar com ressalva.

#### NOT_READY

Condição quando uma ou mais ocorrerem:

- fonte canônica indisponível;
- timezone incorreto ou janela BRT inconsistente;
- divergência crítica acima de 10% entre fontes do mesmo dado;
- volume abaixo de 30% da média 30d sem explicação operacional;
- falha na separação Shopee por `shop_id`;
- pacote sem pedido real suficiente para citar produto;
- erro sistêmico de sync, banco ou extração.

Resultado:

- bloqueia execução;
- Trader não chama as camadas analíticas;
- alerta Kobe;
- nenhum Slack é enviado.

### Calibração futura

Os thresholds podem ser calibrados na Fase 5 com dados reais, mas a estrutura de decisão já nasce definida.

### Entregáveis

```text
scripts/daily-sales-data-builder.py
shared/daily-sales-analyst/data-builder/README.md
shared/daily-sales-analyst/data-builder/schema.json
shared/daily-sales-analyst/data-builder/readiness-rules.md
reports/daily-sales-report-v2/layered/packages/YYYY-MM-DD/package.json
```

### Critérios de saída

- Gera package validado para uma data real.
- Classifica corretamente `DADOS_OK`, `DADOS_PARCIAIS` ou `NOT_READY`.
- Bloqueia quando fonte canônica, timezone ou volume crítico falham.
- Não usa LLM.
- Produz artefato auditável.

### Checkpoint Kobe

Obrigatório antes de ligar camadas LLM ao pacote.

---

## 5. Fase 1 — Workspace e Identidade do Daily Sales Analyst

### Objetivo

Criar o DSA como agente completo, não apenas como um conjunto de prompts chamados em sequência.

### Escopo

- Criar workspace próprio.
- Definir identidade, papel, limites e hierarquia.
- Registrar relação com Trader, Kobe e Pedro.
- Estabelecer que o agente não tem autonomia de canal.

### Entregáveis

```text
shared/daily-sales-analyst/
├── README.md
├── IDENTITY.md
├── SOUL.md
├── AGENTS.md
├── MEMORY.md
├── config/
├── prompts/
├── data-builder/
├── memory/
├── runs/
├── handoff/
└── validation/
```

Arquivos principais:

- `IDENTITY.md` — quem é o agente, escopo e limites.
- `SOUL.md` — postura analítica, princípios de decisão e estilo.
- `AGENTS.md` — regras operacionais e relação com Trader/Kobe.
- `MEMORY.md` — índice da memória própria.
- `README.md` — visão geral de operação.

### Critérios de saída

- O agente existe como entidade completa.
- Escopo fechado: executor do pipeline Layer 0 + 7 camadas.
- Sem autonomia de canal.
- Trader confirmado como dono/orquestrador.
- Kobe confirmado como governança/QA final.

### Checkpoint Kobe

Kobe valida se:

- a identidade não conflita com Trader;
- o agente não ganhou autonomia indevida;
- limites de envio e comunicação estão claros;
- hierarquia está consistente.

---

## 6. Fase 2 — Prompts, Memória e Regras Operacionais

### Objetivo

Organizar os 7 prompts aprovados e criar base de memória estável para o DSA.

### Escopo

- Versionar os 7 prompts dentro do workspace do agente.
- Criar memória por conta/plataforma.
- Registrar regras de marketplace.
- Registrar responsáveis e contexto operacional.
- Registrar relação com Himmel/Pedro/Kobe.
- Definir manutenção da memória.
- Definir ciclo de audit-ressalvas.

### Entregáveis — Prompts

```text
shared/daily-sales-analyst/prompts/
├── current -> versions/vX.Y/
├── CHANGELOG.md
└── versions/
    ├── v3.0/
    │   ├── 01-estrategica.md
    │   ├── 02-tatica.md
    │   ├── 03-operacional.md
    │   ├── 04-granular.md
    │   ├── 05-condensadora.md
    │   ├── 06-slack-writer.md
    │   └── 07-qa-gate.md
    └── v3.1/
        └── ...
```

### Versionamento semântico dos prompts

O versionamento segue:

```text
vX.0   = mudança estrutural
vX.Y   = ajuste fino
vX.Y.Z = correção pontual
```

#### vX.0 — Mudança estrutural

Exemplos:

- nova camada;
- nova regra dura;
- mudança de output schema;
- alteração na hierarquia das camadas;
- mudança de template Slack.

Governança:

- requer aprovação Kobe;
- Trader participa da validação;
- precisa registrar changelog.

#### vX.Y — Ajuste fino

Exemplos:

- clarificação de regra existente;
- exemplo novo;
- refinamento de critério de qualidade;
- melhoria de instrução sem alterar contrato.

Governança:

- Trader aprova;
- Kobe só entra se afetar rollout ou regra estratégica.

#### vX.Y.Z — Correção pontual

Exemplos:

- typo;
- ajuste de tom;
- formatação;
- exemplo mal escrito sem mudança de regra.

Governança:

- DSA pode aplicar;
- deve registrar no changelog;
- Trader revisa no ciclo semanal se recorrente.

### Changelog obrigatório

Todo bump registra em:

```text
shared/daily-sales-analyst/prompts/CHANGELOG.md
```

Campos obrigatórios:

- data;
- versão anterior;
- nova versão;
- autor/agente;
- motivo;
- escopo;
- risco esperado;
- rollback recomendado.

Isso permite rastrear degradações e fazer rollback dirigido.

### Entregáveis — Memória por conta

```text
shared/daily-sales-analyst/memory/accounts/
├── shopee-budamix-store/
│   ├── daily/
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── shopee-budamix-oficial-2/
│   ├── daily/
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── shopee-budamix-shop-3/
│   ├── daily/
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
├── mercado-livre/
│   ├── daily/
│   ├── weekly.md
│   ├── monthly.md
│   └── rules.md
└── amazon/
    ├── daily/
    ├── weekly.md
    ├── monthly.md
    └── rules.md
```

### Entregáveis — Contexto operacional

```text
shared/daily-sales-analyst/memory/context/
├── responsaveis.md
├── contas-shopee.md
├── himmel.md
├── marketplace-rules.md
├── slack-format.md
└── qa-standards.md
```

### Entregáveis — Manutenção de memória

```text
shared/daily-sales-analyst/memory/MAINTENANCE.md
shared/daily-sales-analyst/memory/audit-ressalvas.md
```

### Regra de atualização da memória

#### Daily

- Preferência: arquivo por data em `daily/YYYY-MM-DD.md`.
- Nunca sobrescrever sem backup.
- Cada execução aprovada ou aprovada com ressalva pode gerar entrada diária.
- Execução bloqueada gera entrada em logs, não necessariamente em memória diária de tese.

#### Weekly

- Consolidado semanal.
- Disparo: segunda de manhã ou após 7 entradas diárias.
- Alimenta tendências e padrões recorrentes.

#### Monthly

- Consolidado mensal.
- Disparo: primeiro dia útil do mês.
- Alimenta tese de médio prazo.

#### Rules

Só muda por:

- decisão explícita;
- mudança de marketplace;
- QA recorrente;
- padrão confirmado em weekly/monthly;
- aprovação Trader/Kobe conforme severidade.

#### Responsabilidades

- DSA sugere/aplica memória operacional.
- Trader valida regras permanentes.
- Kobe entra em mudança estratégica ou conflito.

### Loop de evolução via audit-ressalvas

QA Gate pode gerar `Ressalvas de auditoria` não bloqueantes.

Essas ressalvas são registradas em:

```text
shared/daily-sales-analyst/memory/audit-ressalvas.md
```

Agrupamentos mínimos:

- dado;
- produto;
- qualidade analítica;
- Slack Writer;
- memória;
- regra marketplace;
- prompt;
- QA.

#### Critérios de ação

- **N >= 3 ressalvas similares na mesma semana**  
  Flag automática no weekly review do Trader. Trader decide se vira ajuste de prompt, regra ou Data Builder.

- **N >= 5 ressalvas similares no mesmo mês**  
  Escalonamento automático para Kobe.

- **Mesmo padrão por 2+ semanas consecutivas**  
  Trigger de revisão formal de regra. Vira tarefa, não observação solta.

### Critérios de saída

- Os 7 prompts estão versionados.
- Cada conta tem memória própria.
- `MAINTENANCE.md` existe.
- `audit-ressalvas.md` existe.
- Regras críticas estão explícitas.
- DSA consegue operar com contexto estável, não só prompt isolado.

### Checkpoint Kobe

Kobe valida:

- regras de Shopee, ML e Amazon;
- responsáveis;
- memória por conta;
- governança de rules;
- versionamento dos prompts.

---

## 7. Fase 3 — Integração com Trader

### Objetivo

Definir contrato formal de delegação entre Trader e DSA.

### Escopo

- Criar input schema.
- Criar output schema.
- Definir quando Trader chama o DSA.
- Definir o que DSA devolve.
- Definir quando Trader envia, bloqueia ou escala Kobe.
- Suportar execução parcial por plataforma.

### Entregáveis

```text
shared/daily-sales-analyst/handoff/
├── TRADER-CONTRACT.md
├── input-schema.json
├── output-schema.json
├── examples/
│   ├── input-example.json
│   └── output-example.json
└── escalation-rules.md
```

### Input esperado do Trader

Trader envia:

- data analisada;
- modo de execução;
- pacote do Layer 0;
- destinatários/plataformas solicitados;
- memória relevante;
- regras ativas;
- contexto Himmel/marketplace quando aplicável;
- versão de prompt desejada ou `current`.

### Output esperado do DSA

O output deve suportar status por plataforma.

```text
global_status: APPROVED | APPROVED_WITH_REMARKS | PARTIAL | BLOCKED
send_real_allowed: true | false
prompt_version: vX.Y.Z
data_builder_version: vX.Y.Z
date: YYYY-MM-DD
recipients:
  lucas:
    platform: shopee
    status: APPROVED | APPROVED_WITH_REMARKS | BLOCKED | SKIPPED
    send_allowed: true | false
    layers: ...
    slack_payload: ...
    qa: ...
  yasmin:
    platform: mercado_livre
    status: ...
  leonardo:
    platform: amazon
    status: ...
escalation:
  required: true | false
  reason: ...
memory_updates:
  suggested: ...
  applied: ...
```

### Regra de execução parcial

Cada plataforma/destinatário é independente.

- Lucas pode receber mesmo se Yasmin bloqueou.
- Yasmin pode receber mesmo se Leonardo bloqueou.
- Leonardo pode receber mesmo se Lucas bloqueou.

O bloqueio de uma plataforma **não aborta as outras**.

### Quando abortar tudo

Abortar tudo somente se houver falha global:

- Layer 0 global `NOT_READY`;
- banco indisponível;
- timezone incorreto;
- fonte canônica divergente de forma sistêmica;
- runner quebrado;
- prompt version inválida;
- kill switch global ativo.

### Critérios de saída

- Trader sabe exatamente como delegar.
- DSA sabe exatamente o que devolver.
- Envio real continua pertencendo ao Trader.
- Bloqueios e ressalvas têm formato padronizado.
- Status por plataforma implementado.

### Checkpoint Kobe

Kobe valida o contrato antes do runner definitivo.

---

## 8. Fase 4 — Pipeline Ponta a Ponta em Dry-run

### Objetivo

Executar Layer 0 + 7 camadas em sequência usando DSA, sem envio real.

### Escopo

- Criar runner dry-run.
- Executar as camadas na ordem correta.
- Salvar artefatos auditáveis por data e destinatário.
- Manter `send_real_allowed=false`.
- Registrar prompt_version e data_builder_version.

### Entregáveis

```text
shared/daily-sales-analyst/runs/YYYY-MM-DD/
├── manifest.json
├── lucas/
│   ├── 00-data-package.json
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

Nesta fase, todos mantêm envio real bloqueado.

### Critérios de saída

- Rodada completa para Lucas, Yasmin e Leonardo.
- Layer 0 + 7 camadas são gerados e salvos.
- QA bloqueia análise rasa ou genérica.
- Nenhum Slack real é enviado.
- `send_real_allowed=false` em todos os manifests.

### Checkpoint Kobe

Kobe revisa uma rodada completa antes da validação em múltiplos dias.

---

## 9. Fase 5 — Validação com Dados Reais e Ajuste Fino

### Objetivo

Validar o novo pipeline com dados reais antes de qualquer envio para funcionários.

### Escopo

- Criar baseline objetiva.
- Rodar shadow em 3 a 5 datas reais.
- Comparar contra o report atual e contra baseline rotulada.
- Avaliar profundidade, segurança e utilidade.
- Ajustar prompts, regras e memória.
- Validar segurança do horário 06:50 BRT com comparação contra 09:00.

### Entregáveis

```text
shared/daily-sales-analyst/validation/
├── baseline-cases.md
├── shadow-runs-summary.md
├── quality-matrix.md
├── issues-found.md
├── fixes-applied.md
└── approval-candidate.md
```

### Baseline objetiva

Criar `validation/baseline-cases.md` antes do shadow.

Casos mínimos:

1. dia bom claro;
2. dia ruim claro;
3. dia ambíguo;
4. dia com risco de produto errado;
5. dia com Shopee mascarando conta.

Cada caso deve ter:

- data;
- plataforma/destinatário;
- o que uma análise boa deveria perceber;
- o que seria erro crítico;
- critérios binários;
- score 1–5 para profundidade;
- score 1–5 para utilidade;
- decisão esperada: aprovado/rejeitado.

### Matriz de avaliação

Cada rodada deve ser avaliada por:

- Data Readiness correto;
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

### Validação do horário 06:50 BRT

Não mudar horário sem evidência.

Durante a Fase 5:

- rodar package/Layer 0 às 06:50;
- rodar revalidação às 09:00;
- comparar totais, cancelamentos, status e top produtos;
- medir divergência.

Se houver instabilidade recorrente, propor mudança de horário ou revalidação obrigatória.

### Critérios de saída

- Pelo menos 3 execuções reais em shadow.
- QA aprovado ou aprovado com ressalva nas execuções candidatas.
- Zero caso de produto errado.
- Zero SKU cru visível.
- Zero prioridade genérica.
- Zero mistura de plataforma.
- Resultado da comparação 06:50 vs 09:00 documentado.
- Kobe aprova o padrão final.

### Checkpoint Kobe

Obrigatório antes de qualquer envio real.

---

## 10. Fase 6 — Kill Switch, Rollback e Rollout Supervisionado

### Objetivo

Colocar o novo pipeline em operação controlada, com mecanismo de parada e rollback antes de qualquer envio real recorrente.

### Escopo

- Implementar kill switch.
- Implementar versionamento ativo/pinned de prompts.
- Implementar rollback sem deploy.
- Cron aciona Trader.
- Trader chama DSA.
- DSA devolve payload e QA.
- Primeiro ciclo envia preview para Kobe/Pedro.
- Depois libera envio real supervisionado.

### Entregáveis — Configuração

```text
shared/daily-sales-analyst/config/daily-sales-analyst.json
```

Campos mínimos:

```json
{
  "enabled": true,
  "send_real_enabled": false,
  "lucas_enabled": true,
  "yasmin_enabled": true,
  "leonardo_enabled": true,
  "prompt_version": "current",
  "pinned_prompt_version": null,
  "rollback_to_version": null,
  "data_builder_enabled": true,
  "layer0_required": true
}
```

### Kill switch

Deve permitir:

- desligar tudo;
- desligar envio real mantendo preview;
- desligar destinatário específico;
- pinar versão anterior de prompt;
- voltar Data Builder para versão anterior se necessário.

### Donos do kill switch

- Trader pode bloquear envio operacional.
- Kobe pode bloquear rollout/sistema.
- Pedro pode mandar desligar tudo a qualquer momento.

### Rollback de prompts

Regras:

- se 2 dias seguidos com QA ruim ou feedback negativo: kill switch;
- se Slack Writer falhar: bloquear envio real e voltar versão anterior;
- se prompt degradar qualidade: pin da versão anterior sem deploy;
- todo rollback registra motivo em `prompts/CHANGELOG.md`.

### Entregáveis — Rollout

- Cron atualizado para fluxo Trader → DSA.
- Modo `--preview-to-kobe`.
- Modo `--send-real` protegido por QA.
- Registro em `sent-reports.md`.
- Alerta automático em caso de `BLOCKED`.

### Proteções obrigatórias

- Se QA = `BLOCKED`, não envia.
- Se Layer 0 = `NOT_READY`, não envia.
- Se produto inseguro, não cita nominalmente.
- Se SKU cru visível, bloqueia.
- Se prioridade genérica, bloqueia.
- Se `send_real_allowed=false`, não envia.
- Se kill switch ativo, não envia.

### Critérios de saída

- Kill switch testado.
- Rollback testado.
- 1 execução preview aprovada.
- 1 execução real supervisionada aprovada.
- Logs completos.
- Memória atualizada.
- Nenhum envio externo fora do fluxo Trader.

### Checkpoint Kobe

Kobe precisa aprovar explicitamente a retomada do envio real.

---

## 11. Fase 7 — Operação em Produção

### Objetivo

Rodar diariamente com autonomia controlada.

### Escopo

- Cron diário definitivo.
- Trader orquestra.
- DSA executa.
- Trader envia se aprovado.
- Kobe entra apenas em bloqueio, mudança estratégica ou rollout novo.

### Entregáveis

- Cron definitivo às 06:50 BRT, se Fase 5 validar estabilidade.
- Revalidação 09:00, se necessária.
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
- Audit-ressalvas alimenta evolução contínua.

---

## 12. Estados Permitidos de Execução

### DRY_RUN

- Gera análise.
- Não envia Slack.
- Pode usar dados reais.
- Serve para desenvolvimento.

### SHADOW

- Gera análise como se fosse produção.
- Não envia Slack.
- Salva logs completos.
- Usado para validação.

### PREVIEW_TO_KOBE

- Gera payload final.
- Envia apenas para Kobe/Pedro revisar.
- Funcionários não recebem.

### SEND_CANDIDATE

- Gera payload com intenção de envio.
- Só envia se QA aprovar, Layer 0 permitir e `send_real_allowed=true`.

### PRODUCTION_SEND

- Fluxo normal de produção.
- Trader envia para funcionários após aprovação do QA.

---

## 13. Logs de Execução e Retenção

### Estrutura

```text
shared/daily-sales-analyst/runs/
├── INDEX.md
├── manifest.jsonl
├── YYYY-MM-DD/
│   ├── manifest.json
│   ├── lucas/
│   ├── yasmin/
│   └── leonardo/
└── summaries/
    ├── weekly/
    └── monthly/
```

### Cada execução registra

- data;
- horário de execução;
- modo;
- destinatário;
- plataforma;
- status por camada;
- QA status;
- motivos de bloqueio;
- versão de prompts;
- versão do Data Builder;
- Data Readiness;
- se houve envio;
- path dos artefatos;
- ressalvas de auditoria.

### Retenção

- 90 dias completos de logs detalhados.
- Sumário permanente.
- Bloqueios e incidentes relevantes nunca são descartados sem consolidação.

### Consultas desejadas

A estrutura deve permitir responder:

- quais rodadas bloquearam nos últimos 7 dias;
- quais plataformas tiveram mais ressalvas;
- quando uma versão de prompt começou a degradar;
- quais execuções usaram `DADOS_PARCIAIS`;
- quais mensagens foram enviadas de fato.

---

## 14. Critérios Globais de Bloqueio

O pipeline deve bloquear envio se ocorrer qualquer um destes casos:

- Layer 0 = `NOT_READY`;
- fonte canônica indisponível;
- timezone errado;
- divergência crítica acima de 10%;
- volume abaixo de 30% da média 30d sem explicação;
- mistura de plataformas;
- Shopee analisada sem separar contas quando isso afeta diagnóstico;
- Amazon citando produto sem pedido real/ASIN/título confiável;
- SKU cru visível no Slack;
- produto com risco alto de identificação citado nominalmente;
- prioridade genérica sem evidência;
- análise apenas descritiva, sem tese;
- Slack Writer reintroduz seção proibida;
- QA Gate com status `BLOCKED`;
- `send_real_allowed=false`;
- kill switch ativo;
- erro no handoff Trader ↔ DSA.

---

## 15. Estrutura Final Recomendada do Agente

```text
shared/daily-sales-analyst/
├── README.md
├── IDENTITY.md
├── SOUL.md
├── AGENTS.md
├── MEMORY.md
├── config/
│   └── daily-sales-analyst.json
├── data-builder/
│   ├── README.md
│   ├── schema.json
│   └── readiness-rules.md
├── prompts/
│   ├── current -> versions/vX.Y/
│   ├── CHANGELOG.md
│   └── versions/
│       └── v3.0/
│           ├── 01-estrategica.md
│           ├── 02-tatica.md
│           ├── 03-operacional.md
│           ├── 04-granular.md
│           ├── 05-condensadora.md
│           ├── 06-slack-writer.md
│           └── 07-qa-gate.md
├── memory/
│   ├── MAINTENANCE.md
│   ├── audit-ressalvas.md
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
│   └── rules/
├── handoff/
│   ├── TRADER-CONTRACT.md
│   ├── input-schema.json
│   ├── output-schema.json
│   ├── escalation-rules.md
│   └── examples/
├── runs/
│   ├── INDEX.md
│   └── manifest.jsonl
└── validation/
    ├── baseline-cases.md
    ├── shadow-runs-summary.md
    ├── quality-matrix.md
    ├── issues-found.md
    ├── fixes-applied.md
    └── approval-candidate.md
```

---

## 16. Ordem Recomendada de Implementação

### Bloco inicial obrigatório: Fase 0 + Fase 1 + Fase 2

Começar por:

1. **Fase 0 — Data Builder / Data Readiness**
2. **Fase 1 — Workspace e identidade**
3. **Fase 2 — Prompts, memória e regras**

Motivo: antes de construir runner, o agente precisa existir como entidade completa e o input precisa ser determinístico.

Se o runner for codado antes disso, o projeto vira apenas um script com prompts. O ganho real vem de criar:

- agente com identidade própria;
- Layer 0 confiável;
- memória estável;
- prompts versionados;
- regras auditáveis;
- contrato com Trader;
- logs e rollback.

### Depois do bloco inicial

4. Fase 3 — Contrato Trader ↔ DSA  
5. Fase 4 — Runner dry-run  
6. Fase 5 — Shadow com dados reais  
7. Fase 6 — Kill switch + rollout supervisionado  
8. Fase 7 — Produção contínua

---

## 17. Recomendação Final

O plano definitivo é implementar primeiro **Fase 0 + Fase 1 + Fase 2** como fundação.

Isso garante que:

- o dado nasce determinístico e auditável;
- o agente existe com identidade e limites claros;
- os prompts estão versionados;
- a memória tem cadência de manutenção;
- as ressalvas de QA viram evolução real;
- o Trader continua dono do processo;
- Kobe mantém governança de rollout;
- o cron não vira um script solto.

Só depois disso o runner deve ser construído.

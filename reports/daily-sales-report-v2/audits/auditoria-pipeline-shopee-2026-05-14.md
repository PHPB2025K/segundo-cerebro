# Auditoria do Pipeline de Análise Shopee — Daily Sales Report v2

**Data analisada:** 14/05/2026  
**Marketplace:** Shopee  
**Responsável final:** Lucas  
**Data da auditoria:** 15/05/2026  
**Modo:** Diagnóstico — sem correções aplicadas durante a auditoria

---

## 1. Objetivo da auditoria

Verificar, camada por camada, se o pipeline de análise da Shopee executou os prompts definidos e salvos para cada etapa, avaliar a aderência de cada camada ao seu papel e mapear melhorias granulares antes de qualquer nova correção.

A auditoria focou no fluxo mais recente do pipeline Shopee, usado para gerar a mensagem de preview de Lucas referente a 14/05/2026.

---

## 2. Resumo executivo

O pipeline da Shopee está no melhor estado até agora, mas ainda não está 100% fiel ao desenho completo de “camadas LLM dedicadas até o fim”.

### O que está correto hoje

- As três contas Shopee passam por LLM nas camadas 1 a 5:
  - Estratégica
  - Tática
  - Operacional
  - Granular
  - Condensadora
- Cada uma dessas camadas usou o prompt salvo correspondente.
- A Consolidadora Shopee / Camada 6B usou o prompt correto.
- A Consolidadora Shopee consumiu as três condensadoras individuais.
- A mensagem final da Shopee consumiu a saída da Consolidadora Shopee.
- O layout final aprovado foi respeitado.

### Principal gap encontrado

As camadas finais ainda não estão 100% no modelo LLM dedicado:

- Slack Writer: existe prompt salvo, mas hoje a geração final é feita por script determinístico.
- QA Gate: existe prompt salvo, mas hoje o QA final é majoritariamente determinístico/hardcoded.

Ou seja, a arquitetura real atual é:

1. Camadas 1–5 LLM por conta Shopee — OK
2. Consolidadora Shopee / 6B LLM — OK
3. Slack Writer determinístico — parcial
4. QA determinístico — parcial

---

## 3. Fluxo real observado

### 3.1 Contas analisadas

- Shopee — Budamix Store
- Shopee — Budamix Oficial
- Shopee — Budamix Shop

### 3.2 Artefatos por conta

Cada conta gerou artefatos LLM nas camadas 1 a 5:

- `camada-1-estrategica.md`
- `camada-2-tatica.md`
- `camada-3-operacional.md`
- `camada-4-granular.md`
- `camada-5-condensadora.md`

### 3.3 Artefatos da Consolidadora Shopee

A Consolidadora Shopee gerou:

- `camada-6b-shopee-consolidadora.json`
- `camada-6b-shopee-consolidadora.raw.md`

A saída continha os campos esperados:

- `analysis_lines`
- `priority_lines`
- `memory_for_tomorrow`
- `qa_flags`

---

## 4. Confirmação de prompts usados

O runner da Consolidadora Shopee carrega explicitamente os prompts salvos em `prompts/daily-sales/`.

### Camadas individuais por conta

| Camada | Prompt salvo | Executou como LLM? | Status |
|---|---|---:|---|
| 1 — Estratégica | `camada-1-estrategica.md` | Sim | OK |
| 2 — Tática | `camada-2-tatica.md` | Sim | OK |
| 3 — Operacional | `camada-3-operacional.md` | Sim | OK |
| 4 — Granular | `camada-4-granular.md` | Sim | OK |
| 5 — Condensadora | `camada-5-condensadora.md` | Sim | OK |

### Camada específica Shopee

| Camada | Prompt salvo | Executou como LLM? | Status |
|---|---|---:|---|
| 6B — Consolidadora Shopee | `camada-6b-shopee-consolidadora.md` | Sim | OK |

### Camadas finais

| Camada | Prompt salvo | Executou como LLM? | Status |
|---|---|---:|---|
| Slack Writer | `camada-6-slack-writer.md` | Não | Parcial |
| QA Gate | `camada-7-qa-gate.md` | Não | Parcial |

O Slack Writer e o QA Gate existem como prompts, mas a execução atual ainda é por script determinístico + validações hardcoded.

---

## 5. Auditoria por camada

## 5.1 Camada 1 — Estratégica

### Prompt usado

`prompts/daily-sales/camada-1-estrategica.md`

### Evidência de execução

Cada conta Shopee gerou `camada-1-estrategica.md` em seu diretório de artefatos.

### Aderência ao papel

Boa.

A camada cumpriu o papel de interpretar a conta em nível macro dentro da trajetória recente. As saídas observaram:

- qualidade da base;
- leitura temporal;
- tese da conta;
- risco estrutural;
- sinais a observar.

### Pontos fortes

- Identificou queda vs histórico onde havia evidência.
- Identificou concentração de top 3 como risco estrutural.
- Separou leitura por conta, sem misturar Shopee como agregado único.

### Pontos de melhoria

- Onde a memória da conta foi declarada rasa, a camada poderia marcar com mais força a limitação de confiança.
- Para melhorar a qualidade, a camada deveria receber mais contexto semanal/mensal consolidado por conta.

---

## 5.2 Camada 2 — Tática

### Prompt usado

`prompts/daily-sales/camada-2-tatica.md`

### Evidência de execução

Cada conta Shopee gerou `camada-2-tatica.md`.

### Aderência ao papel

Boa.

A camada transformou a tese estratégica em decisão prática, separando:

- o que fazer hoje;
- o que não fazer ainda;
- quando escalar.

### Pontos fortes

- Evitou recomendações genéricas de ADS sem evidência suficiente.
- Trouxe cautela operacional antes de mexer em tráfego, preço ou exposição.
- Reforçou proteção dos campeões quando a concentração era alta.

### Pontos de melhoria

- Algumas prioridades poderiam ter gatilhos mais objetivos para o dia seguinte.
- A camada deveria padronizar melhor a estrutura “ação + evidência + risco + critério de decisão amanhã”.

---

## 5.3 Camada 3 — Operacional

### Prompt usado

`prompts/daily-sales/camada-3-operacional.md`

### Evidência de execução

Cada conta Shopee gerou `camada-3-operacional.md`.

### Aderência ao papel

Boa.

A camada leu a execução do dia, top produtos, concentração, sinais operacionais e o que deveria ser investigado pela Granular.

### Pontos fortes

- Conectou a performance do dia aos produtos que sustentaram o resultado.
- Expôs dependência operacional dos campeões.
- Encaminhou perguntas específicas para a Granular.

### Pontos de melhoria

- A camada ainda depende muito de mix, pedidos e GMV.
- Para cumprir o papel de raio-X operacional com mais força, precisa receber granularidade horária, estoque, exposição e campanhas quando disponíveis.

---

## 5.4 Camada 4 — Granular

### Prompt usado

`prompts/daily-sales/camada-4-granular.md`

### Evidência de execução

Cada conta Shopee gerou `camada-4-granular.md`.

### Aderência ao papel

Parcialmente boa.

A camada cumpriu bem a função de não inventar dado e bloquear inferência onde a base não permitia. Isso é positivo.

### Pontos fortes

- Respondeu perguntas específicas da Operacional quando havia evidência.
- Marcou explicitamente perguntas não respondidas por falta de dado.
- Evitou concluir exposição, horário ou campanha quando esses dados não estavam no pacote.

### Problema observado

Várias perguntas importantes ficaram sem resposta por ausência de dados:

- horários dos pedidos;
- distribuição horária;
- exposição/vitrine/busca orgânica;
- campanha, cupom ou origem de tráfego;
- indisponibilidade ou ruptura fora dos dados agregados.

### Pontos de melhoria

- Alimentar a Granular com dados adicionais quando disponíveis:
  - horário dos pedidos;
  - estoque por SKU/listing;
  - dados de campanha/ADS;
  - sinais de exposição/ranking;
  - cupons ou promoções.
- Criar status padronizado para cada investigação:
  - respondida;
  - hipótese fraca;
  - bloqueada por falta de dado;
  - precisa de fonte externa.

---

## 5.5 Camada 5 — Condensadora individual

### Prompt usado

`prompts/daily-sales/camada-5-condensadora.md`

### Evidência de execução

Cada conta Shopee gerou `camada-5-condensadora.md`.

### Aderência ao papel

Boa.

A camada cumpriu a função de cortar ruído e produzir uma leitura curta, densa e utilizável para etapas posteriores.

### Pontos fortes

- Transformou a análise interna em tese operacional por conta.
- Separou prioridades condensadas para Slack.
- Registrou o que não deveria ir para Slack.
- Manteve alertas de confiança.

### Pontos de melhoria

- Padronizar melhor a estrutura das prioridades condensadas para facilitar a Consolidadora Shopee.
- Forçar cada prioridade a trazer “ação + evidência + risco + critério de decisão amanhã”.
- Garantir que a condensadora deixe explícito se a tese é fato comprovado, hipótese ou risco latente.

---

## 5.6 Consolidadora Shopee / Camada 6B

### Prompt usado

`prompts/daily-sales/camada-6b-shopee-consolidadora.md`

### Evidência de execução

Gerou `camada-6b-shopee-consolidadora.json` e `camada-6b-shopee-consolidadora.raw.md`.

### Input correto

Sim.

A Consolidadora recebeu as três condensadoras individuais:

- Budamix Store;
- Budamix Oficial;
- Budamix Shop.

Também recebeu métricas mínimas apenas como referência e checagem de coerência.

### Aderência ao papel

Boa.

A camada gerou:

- uma análise consolidada das três contas;
- uma análise individual final da Budamix Store;
- uma análise individual final da Budamix Oficial;
- uma análise individual final da Budamix Shop;
- três prioridades consolidadas;
- memória para amanhã;
- `qa_flags` vazio.

### Pontos fortes

- Subiu o nível da análise para tese consolidada.
- Identificou concentração sistêmica nos top 3.
- Separou papel das contas.
- Preservou formato de parágrafos curtos e densos, conforme regra final aprovada.

### Ponto de atenção

A camada usou termos fortes como “canibalização estrutural” e “canal inteiro ameaçado”. A tese é plausível, mas precisa ser qualificada quando a evidência mostra mais risco latente do que canibalização comprovada.

### Pontos de melhoria

- Incluir no prompt a obrigação de separar:
  - fato comprovado;
  - hipótese;
  - risco latente;
  - ação recomendada.
- Impedir termos fortes sem marcador de confiança.
- Exigir que a análise consolidada diga claramente se a tese é comprovada, provável ou apenas risco.

---

## 5.7 Slack Writer

### Prompt salvo

`prompts/daily-sales/camada-6-slack-writer.md`

### Foi executado como LLM dedicado?

Não.

### Execução real

A mensagem final foi gerada por script determinístico em `daily-sales-v2-generate-slack.py`, usando a saída da Consolidadora Shopee quando disponível.

### Aderência ao papel

Parcial.

O comportamento atual está conceitualmente correto no sentido de que o Slack Writer não rediagnostica a Shopee; ele apenas formata a saída da Consolidadora. Porém, ele não executa o prompt salvo de Slack Writer como LLM.

### Pontos fortes

- Mantém layout aprovado.
- Preserva a saída da Consolidadora Shopee.
- Evita Atacado/Bling.
- Usa top produtos por variação vendável e por pedidos.

### Pontos de melhoria

- Se o objetivo for aderência total ao desenho original, o Slack Writer precisa virar camada LLM real em modo shadow.
- O Slack Writer LLM deve receber:
  - saída da Consolidadora Shopee;
  - dados objetivos de visão/top produtos;
  - layout aprovado;
  - bloqueios de seção e estilo.
- O script determinístico pode continuar como fallback ou validador de estrutura.

---

## 5.8 QA Gate

### Prompt salvo

`prompts/daily-sales/camada-7-qa-gate.md`

### Foi executado como LLM dedicado?

Não.

### Execução real

O QA final foi feito por validações determinísticas/hardcoded no script:

- mensagem vazia;
- seção obrigatória;
- seções proibidas;
- SKU cru;
- padrões rasos antigos;
- títulos com emoji;
- qualidade condensada mínima.

### Aderência ao papel

Parcial.

O QA determinístico cobre bem travas mecânicas, mas não avalia profundamente fidelidade semântica à Consolidadora nem aderência integral ao prompt de QA Gate.

### Pontos fortes

- Bloqueia erros objetivos.
- Impede retorno de seções proibidas.
- Ajuda a evitar SKU cru e texto raso antigo.

### Pontos de melhoria

- Criar QA Gate LLM real em shadow.
- QA LLM deve comparar:
  - prompt da Consolidadora;
  - saída da Consolidadora;
  - mensagem Slack final;
  - regras de formato;
  - risco de hipótese virar fato.
- Manter QA determinístico como trava final após QA LLM.

---

## 6. Problemas encontrados

### 6.1 Nome e ordem das camadas ainda podem confundir

A arquitetura final decidiu chamar a etapa nova de Consolidadora Shopee / Camada 6B, mas ainda existem artefatos legados e referências de compatibilidade com o nome antigo `camada-8-shopee-consolidada`.

Isso não quebra o pipeline, mas pode confundir auditorias futuras.

### 6.2 `daily-sales-v2-layered-preview.py` ainda é determinístico

Esse script declara que:

- não chama LLM;
- produz camadas 3–7 de forma rule-based;
- é um preview/fallback.

Ele não representa a arquitetura final LLM. Deve ser tratado como shadow/fallback, não como prova de execução real das camadas finais.

### 6.3 Slack Writer e QA Gate não usam seus prompts salvos

Esse é o maior gap para “100% aderência”.

As etapas existem como prompts, mas a execução atual ainda não chama LLM nelas.

### 6.4 Granular ainda sofre por falta de dados

A Granular foi obediente ao prompt e não inventou. Mas isso expõe uma lacuna de insumo:

- sem horário;
- sem exposição;
- sem campanha;
- sem estoque detalhado;
- sem ranking/vitrine.

---

## 7. Melhorias granulares recomendadas

### 7.1 Camada Estratégica

- Incluir memória semanal/mensal por conta quando existir.
- Forçar marcação de confiança quando a memória for rasa.
- Diferenciar queda estrutural, oscilação normal e dado insuficiente.

### 7.2 Camada Tática

- Padronizar cada decisão com:
  - ação;
  - evidência;
  - risco;
  - gatilho de revisão amanhã.
- Evitar recomendações sem critério de decisão.

### 7.3 Camada Operacional

- Incluir dados de horário e estoque quando disponíveis.
- Separar melhor execução operacional de hipótese de tráfego.
- Forçar “o que mudou hoje” vs “o que já era estrutural”.

### 7.4 Camada Granular

- Alimentar com fonte horária, estoque, campanha e exposição.
- Padronizar status de investigação.
- Separar “não respondido por falta de dado” de “evidência negativa real”.

### 7.5 Camada Condensadora

- Padronizar prioridades condensadas.
- Exigir classificação de tese:
  - fato;
  - hipótese;
  - risco latente.
- Incluir o que a Consolidadora deve preservar obrigatoriamente.

### 7.6 Consolidadora Shopee

- Exigir marcador de confiança para termos fortes.
- Proibir “canibalização estrutural” sem evidência direta; usar “risco de canibalização” quando for hipótese.
- Exigir 1 consolidado + 3 individuais sempre.
- Manter formato de parágrafo curto e denso.

### 7.7 Slack Writer

- Implementar execução LLM em shadow usando `camada-6-slack-writer.md`.
- Dar ao Slack Writer a saída da Consolidadora, não os dados brutos.
- Impedir rediagnóstico.
- Manter script determinístico como fallback/validador de layout.

### 7.8 QA Gate

- Implementar QA LLM em shadow usando `camada-7-qa-gate.md`.
- Comparar mensagem final contra Consolidadora e regras.
- Manter QA determinístico após QA LLM.
- Bloquear hipótese apresentada como fato.

---

## 8. Conclusão

A Shopee hoje tem a parte mais importante da arquitetura funcionando:

- análise individual LLM por conta até a Condensadora;
- Consolidadora Shopee LLM usando as três condensadoras;
- Slack final consumindo a saída consolidada.

O pipeline já produz uma análise muito mais densa do que a versão anterior.

Mas a aderência completa ao desenho original ainda exige promover duas etapas finais para LLM real:

1. Slack Writer LLM
2. QA Gate LLM

A recomendação é implementar essas duas etapas primeiro em modo shadow, comparar outputs por 2–3 dias e só depois decidir se entram no caminho principal de preview/envio.

---

## 9. Próxima ação recomendada

Quando autorizado, criar um runner shadow para:

1. executar Slack Writer LLM usando `camada-6-slack-writer.md`;
2. executar QA Gate LLM usando `camada-7-qa-gate.md`;
3. manter QA determinístico como trava final;
4. salvar artefatos auditáveis antes de qualquer envio real.

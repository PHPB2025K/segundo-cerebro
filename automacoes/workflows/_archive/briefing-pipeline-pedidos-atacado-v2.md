---
title: "Briefing v2 — Pipeline Agente de Pedidos de Atacado"
type: briefing
created: 2026-05-14
status: superseded
owner: Pedro Broglio
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
  - agente-pedidos
---

# Briefing v2 — Pipeline Agente de Pedidos de Atacado

## Objetivo da v2

Esta versão incorpora as lacunas apontadas por Pedro antes de avançar com implementação.

O princípio continua o mesmo:

> O sistema não deve ser um parser rígido de formulário. Deve ser um **agente operacional de pedidos**, capaz de interpretar mensagens imperfeitas, resolver SKU com autonomia, validar riscos e só perguntar quando houver incerteza real.

A v2 adiciona as camadas que faltavam para produção:

- faixas numéricas de confiança;
- classificador de intenção antes da interpretação;
- monitoramento e dead letter queue;
- allowlist de remetentes;
- critérios mensuráveis de aceite por fase;
- botão de pânico/rollback;
- fluxo de edição de pedido;
- catálogo próprio sincronizado;
- múltiplos produtos por pedido;
- painel comparativo de dry-run;
- segurança contra prompt-injection;
- logs explicáveis;
- aliases editáveis sem deploy;
- matriz de respostas no grupo.

---

# 1. Resposta item a item

## 🔴 Críticas — entram antes da Fase 1

## 1. Faixas numéricas de confiança

**Posição:** concordo.

O briefing v1 estava fraco aqui. “Alta/baixa confiança” não é suficiente para operar.

### Proposta

Usar um score final de 0 a 1, calculado por composição de sinais objetivos + julgamento do LLM.

### Faixas

| Score final | Ação |
|---:|---|
| `>= 0.90` | Pode criar sozinho, se todas as validações objetivas passarem |
| `0.70–0.89` | Não criar automaticamente na Fase 1; na Fase 2 pode criar como `revisar` apenas se Pedro aprovar esse comportamento |
| `< 0.70` | Não cria; pergunta no grupo ou manda para revisão |

### Ajuste em relação à sugestão original

Eu **não recomendo criar automaticamente na faixa 0.70–0.89 logo no começo**. Criar + marcar revisar ainda cria risco real no Bling. Minha proposta:

- **Fase 1:** 0.70–0.89 vira “teria criado com revisão”, sem criar.
- **Fase 2:** podemos permitir criar com etiqueta/observação “revisar”, se os testes mostrarem segurança.
- **Fase 3:** 0.70–0.89 pode criar com revisão se o histórico comprovar baixo risco.

### Como calcular o score

Score final ponderado:

```text
score_final =
  40% score_produto_sku
+ 20% score_campos_obrigatorios
+ 15% score_cliente
+ 10% score_preco
+ 10% score_historico
+ 5% score_llm_autoconfianca
```

### Componentes

#### Produto/SKU — 40%

| Sinal | Score produto |
|---|---:|
| SKU explícito exato e existe no catálogo | 1.00 |
| Alias aprovado manualmente | 0.98 |
| Match exato de nome oficial | 0.95 |
| Match semântico forte por embedding + sem concorrente próximo | 0.90–0.94 |
| Match por histórico do cliente/vendedor + preço compatível | 0.80–0.89 |
| Mais de um candidato próximo | máximo 0.69 |
| Sem descrição de produto | 0 |

#### Campos obrigatórios — 20%

Pontua se número do pedido, CNPJ, quantidade, preço e pagamento foram encontrados e normalizados.

#### Cliente — 15%

- CNPJ encontrado no Bling/catálogo local: 1.00
- CNPJ válido mas cliente não cadastrado: bloqueia criação real
- CNPJ inválido/ausente: bloqueia

#### Preço — 10%

Compara preço informado com preço médio histórico do SKU.

- dentro da faixa esperada: 1.00
- divergência moderada: 0.70–0.89
- divergência grave: bloqueia ou exige revisão

#### Histórico — 10%

Reforça quando cliente/vendedor já comprou o mesmo SKU ou usou a mesma descrição antes.

#### LLM — 5%

Autoavaliação do LLM só entra como sinal fraco. Ele não manda sozinho.

---

## 2. Classificador de intenção antes do parser

**Posição:** concordo totalmente.

Sem isso, áudio, foto, bom dia, correção ou conversa podem cair no fluxo errado.

### Classes

Toda mensagem entra primeiro no classificador:

```text
novo_pedido
edicao_pedido
cancelamento_pedido
conversa
midia
pergunta
confirmacao
outro
```

### Ações por classe

| Classe | Ação |
|---|---|
| `novo_pedido` | Entra no pipeline de interpretação |
| `edicao_pedido` | Entra no pipeline de edição |
| `cancelamento_pedido` | Entra em fluxo específico de cancelamento/revisão |
| `midia` | Loga; se tiver legenda relevante, classifica legenda; áudio fica pendente de transcrição futura |
| `pergunta` | Opcionalmente responde ou ignora conforme matriz |
| `conversa` | Loga e ignora |
| `confirmacao` | Pode vincular a pendência aberta |
| `outro` | Loga e ignora |

### Implementação

- Classificador LLM com schema rígido.
- Heurísticas antes do LLM para casos óbvios:
  - contém “pedido de venda atacado número” → `novo_pedido`;
  - contém “troca”, “altera”, “corrige”, “no pedido 955” → `edicao_pedido`;
  - mensagem sem número/sem estrutura e curta → provável `conversa`.
- Saída validada por enum. Se sair fora do enum, vira `outro`.

---

## 3. Monitoramento do pipeline

**Posição:** concordo totalmente. Foi exatamente o buraco que apareceu.

### Implementar

#### Heartbeat

Cron a cada 5 minutos:

1. verifica se o workflow N8N está ativo;
2. verifica se webhook da Evolution aponta para endpoint correto;
3. faz ping no endpoint interno do Fisco;
4. confere se houve erro recente na fila;
5. confere se há mensagens não processadas acima do SLA.

#### Alertas

Alertar Pedro no privado quando:

- workflow estiver pausado/desligado;
- webhook da Evolution mudar ou sumir;
- endpoint Fisco retornar erro;
- dead letter queue tiver mensagem crítica;
- nenhuma mensagem for processada por X horas apesar de haver mensagens novas no grupo;
- latência média passar de 60s.

#### Dead letter queue

Criar tabela/fila de falhas.

Toda mensagem que falhar em qualquer etapa não pode sumir. Ela vai para DLQ com:

- mensagem original;
- etapa em que falhou;
- erro;
- tentativas;
- próxima ação sugerida;
- status: `pending`, `retrying`, `resolved`, `ignored`.

### Stack proposta

- Supabase/Postgres para tabelas.
- Cron OpenClaw ou script VPS para heartbeat.
- Alertas via WhatsApp privado do Kobe para Pedro.
- Painel simples para visualizar DLQ.

---

## 4. Allowlist de remetentes

**Posição:** concordo totalmente.

Qualquer pessoa no grupo disparar criação é risco.

### Regra

Desde a Fase 1, só mensagens de remetentes autorizados podem entrar no pipeline.

### Comportamento

| Remetente | Ação |
|---|---|
| Autorizado | Processa |
| Não autorizado | Loga e ignora |
| Não reconhecido mas parece pedido | Loga + alerta interno, sem responder no grupo |

### Tabela

`wholesale_order_authorized_senders`

Campos:

- `id`
- `name`
- `phone_or_lid`
- `role`
- `active`
- `can_create_order`
- `can_edit_order`
- `created_at`
- `updated_at`

### Inicial

Começar com Pedro Fernandes e Pedro Broglio, validando os IDs reais da Evolution.

---

## 5. Critério de aceite mensurável

**Posição:** concordo com ajuste.

As metas são boas, mas eu ajustaria “100 pedidos reais” para não travar aprendizado se o volume for menor no curto prazo.

### Metas para sair da Fase 1

Recomendação:

- mínimo de **50 pedidos reais observados** ou 14 dias corridos, o que vier primeiro;
- ideal: 100 pedidos reais antes de produção ampla;
- `>= 95%` de acerto de SKU nos pedidos com descrição suficiente;
- `0%` de criação real errada, porque na Fase 1 não cria;
- `<= 2%` de falso positivo de intenção em dry-run;
- `100%` de idempotência nos testes;
- `<= 60s` de latência mensagem → decisão registrada;
- `100%` das falhas indo para DLQ;
- nenhuma mensagem elegível desaparecida sem status.

### Para sair da Fase 2

- pelo menos 30 pedidos reais criados com supervisão;
- `>= 98%` de acerto de SKU;
- `0` pedido criado com SKU errado;
- `0` duplicidade;
- `<= 60s` de latência p95;
- rollback testado com sucesso.

---

## 6. Botão de pânico e rollback

**Posição:** concordo totalmente.

### Botão de pânico

Comandos aceitos de remetente administrador:

```text
!pausar agente
!retomar agente
!status agente
!dryrun agente
```

### Comportamento

- `!pausar agente`: para criação real imediatamente; mantém log/dry-run.
- `!dryrun agente`: força modo simulação.
- `!retomar agente`: só retoma se healthcheck estiver OK.
- `!status agente`: responde status resumido.

### Bling

Pedido deve nascer como pedido editável/rascunho, nunca em status final irreversível.

### Rollback

Log precisa guardar:

- ID do pedido Bling;
- número loja/pedido GB;
- timestamp;
- payload enviado;
- mensagem de origem;
- status de cancelamento/exclusão, se rollback for acionado.

Cancelamento em massa deve ser possível por janela de tempo ou lote.

---

# 🟡 Importantes — Fase 1 ou início da Fase 2

## 7. Fluxo de edição de pedido

**Posição:** concordo. Precisa existir desde a Fase 1 como dry-run, mas criação/edição real pode ficar para Fase 2.

### Detecção

Mensagens como:

```text
no 955 troca para 5 unidades
corrige o 955, era CXFIT300M
pedido 955 agora é entrega
```

Classificam como `edicao_pedido`.

### Fluxo

1. identificar pedido GB referenciado;
2. buscar pedido no log local e/ou Bling;
3. verificar status editável;
4. interpretar mudança;
5. validar impacto;
6. aplicar se permitido;
7. responder no grupo.

### Se não puder editar

Responder:

```text
Pedido 955 já não está em status editável no Bling. Precisa ajuste manual.
```

---

## 8. Catálogo próprio, não Bling ao vivo

**Posição:** concordo totalmente.

Consultar Bling ao vivo para cada decisão é lento, frágil e ruim para ranking semântico.

### Proposta

Criar catálogo local em Supabase/Postgres sincronizado com Bling.

### Tabelas

#### `wholesale_products`

- `sku`
- `bling_product_id`
- `official_name`
- `description`
- `active`
- `unit`
- `last_bling_sync_at`
- `embedding`
- `created_at`
- `updated_at`

#### `wholesale_product_aliases`

- `id`
- `sku`
- `alias`
- `source`: `manual`, `learned`, `history`, `imported`
- `confidence_boost`
- `approved_by`
- `active`
- `created_at`
- `updated_at`

#### `wholesale_product_price_history`

- `sku`
- `price`
- `client_cnpj`
- `seller`
- `order_date`
- `source_order_id`

### Sync

- sincronizar Bling a cada 6h inicialmente;
- permitir sync manual;
- atualizar embeddings quando nome/descrição/alias mudar.

---

## 9. Múltiplos produtos por pedido

**Posição:** concordo totalmente.

Atacado pode ter mais de um item. O v1 estava simplificado demais.

### Regra

Pedido inteiro só vai para o Bling se **todos os itens** estiverem resolvidos com confiança suficiente.

### Comportamento

| Situação | Ação |
|---|---|
| Todos os itens seguros | Cria pedido com múltiplos itens |
| Um item ambíguo | Bloqueia pedido inteiro e pergunta |
| Um item ausente no catálogo | Bloqueia pedido inteiro |
| Quantidade/preço faltando em um item | Bloqueia pedido inteiro |

### Motivo

Criar pedido parcial é perigoso: parece concluído, mas fica operacionalmente errado.

---

## 10. Painel comparativo da Fase 1

**Posição:** concordo totalmente.

Dry-run sem painel vira log invisível.

### Painel Fase 1

Tela com colunas:

- mensagem original;
- remetente;
- classificação de intenção;
- decisão do agente;
- SKU(s) sugerido(s);
- confiança;
- razão da decisão;
- status final humano;
- humano corrigiu? sim/não;
- SKU correto;
- match? sim/não;
- tempo de processamento.

### Objetivo

Permitir medir se o agente está pronto para criar pedido real.

---

# 🟢 Higiene e refino

## 11. Sanitização anti-prompt-injection

**Posição:** concordo.

### Implementar

- Mensagem do WhatsApp entra como dado, nunca como instrução.
- Prompt do LLM deve delimitar conteúdo do usuário.
- Saída do LLM precisa passar por schema rígido.
- Campos numéricos passam por validação determinística.

### Bloqueios automáticos

- preço `<= 0`;
- quantidade `<= 0`;
- quantidade absurda acima de limite configurável;
- preço fora de faixa sem justificativa;
- SKU inexistente;
- CNPJ inválido;
- instruções do tipo “ignore regras anteriores”.

---

## 12. Campo razão no log

**Posição:** concordo totalmente.

Todo log deve ter `decision_reason`.

Exemplo:

```text
SKU CXFIT300M escolhido porque houve match exato do alias aprovado "caixa fita 300". Cliente Eduardo Maranim ainda não tinha histórico, mas preço R$ 232,90 está dentro da faixa esperada do SKU.
```

---

## 13. Explicabilidade sob demanda

**Posição:** concordo, mas eu colocaria na Fase 2.

### Comando

```text
!explicar 955
```

### Resposta

O agente resume:

- mensagem analisada;
- SKU escolhido;
- confiança;
- sinais usados;
- motivo de bloqueio ou criação.

Na Fase 1, essa explicação já existe no painel. No grupo, entra depois para não poluir.

---

## 14. Aliases editáveis sem deploy

**Posição:** concordo totalmente.

Alias novo não pode virar mudança de código.

### Implementação

Tabela `wholesale_product_aliases` no Supabase.

Edição por:

1. painel simples;
2. comando administrativo futuro;
3. import CSV, se necessário.

### Regra

Alias aprendido automaticamente começa como `pending_review`. Só vira alias forte após aprovação humana ou recorrência confiável.

---

## 15. Resposta no grupo configurável

**Posição:** concordo.

### Matriz inicial

| Evento | Responder no grupo? |
|---|---|
| Pedido criado | Sim |
| Pedido bloqueado por falta de dado | Sim |
| SKU ambíguo | Sim |
| Cliente não encontrado | Sim |
| Mensagem ignorada por conversa | Não |
| Remetente não autorizado | Não, alerta privado se parecer pedido |
| Erro interno do pipeline | Não no grupo; alerta privado Pedro |
| Dry-run Fase 1 | Configurável; recomendação: não responder sempre para não poluir |

---

# 2. Arquitetura proposta

## Componentes

```text
WhatsApp / Evolution
        ↓
Webhook receptor
        ↓
Classificador de intenção
        ↓
Allowlist de remetente
        ↓
Fila de processamento
        ↓
Agente de interpretação
        ↓
Resolução de SKU / Catálogo local
        ↓
Validação determinística
        ↓
Dry-run ou criação Bling
        ↓
Resposta configurável no grupo
        ↓
Log + painel + aprendizado
        ↓
Monitoramento / DLQ / alertas
```

---

## Stack proposta

### Entrada

- Evolution API do WhatsApp próprio do Kobe.
- Webhook dedicado.

### Orquestração

Duas opções:

1. **N8N só como receptor/roteador simples**  
   Mantém N8N, mas lógica crítica fica fora dele.

2. **Worker próprio no Mission Control/VPS**  
   Mais confiável para fila, DLQ, healthcheck e painel.

### Recomendação

Usar **worker próprio** para o core e deixar N8N no mínimo possível, ou remover N8N do caminho crítico.

Motivo: o problema do workflow pausado mostrou que N8N é frágil como peça central sem monitoramento forte.

### Banco

Supabase/Postgres para:

- mensagens recebidas;
- classificações;
- decisões;
- catálogo;
- aliases;
- logs;
- DLQ;
- métricas;
- painel.

### LLM

LLM para interpretação, mas sempre com:

- schema rígido;
- validação determinística;
- score composto;
- proibição de inventar SKU fora do catálogo.

### Bling

- criação de pedido de venda na Matriz;
- sempre em status editável;
- NF-e fora do escopo inicial.

---

# 3. Fases propostas

## Fase 0 — Fundação de segurança

Entra antes da Fase 1.

### Escopo

- classificador de intenção;
- allowlist;
- tabelas base;
- catálogo local;
- aliases editáveis;
- DLQ;
- heartbeat;
- botão de pânico;
- modo dry-run global;
- logs explicáveis.

### Por quê

Sem isso, qualquer teste real pode sumir, duplicar, ser disparado por pessoa errada ou ficar invisível.

---

## Fase 1 — Dry-run observável

Não cria pedido real.

### Escopo

- ler mensagens reais do grupo;
- classificar intenção;
- interpretar pedido;
- resolver SKU;
- calcular score;
- registrar decisão;
- preencher painel comparativo;
- alertar falhas críticas;
- não responder no grupo por padrão, exceto se configurado.

### Critério para sair

- 50 pedidos reais ou 14 dias de dados;
- ideal: 100 pedidos reais;
- `>= 95%` de acerto de SKU nos casos com descrição suficiente;
- `<= 2%` de falso positivo de intenção;
- `100%` de idempotência;
- `100%` de falhas registradas na DLQ;
- p95 de latência `<= 60s`;
- nenhum pedido elegível sem status.

---

## Fase 2 — Criação controlada

Cria pedido real apenas quando o score for muito alto.

### Escopo

- criação no Bling para score `>= 0.90`;
- pedidos 0.70–0.89 continuam como revisão, salvo liberação explícita;
- resposta no grupo para criado/bloqueado;
- fluxo de edição em dry-run ou real se status permitir;
- rollback testado;
- painel acompanha criado vs humano.

### Critério para sair

- 30 pedidos reais criados com supervisão;
- `>= 98%` de acerto de SKU;
- 0 pedido criado com SKU errado;
- 0 duplicidade;
- rollback funcional;
- p95 `<= 60s`.

---

## Fase 3 — Produção assistida

Pipeline roda no dia a dia com supervisão leve.

### Escopo

- criar automático score `>= 0.90`;
- tratar 0.70–0.89 conforme regra aprovada;
- responder no grupo conforme matriz;
- edição de pedido funcionando;
- aliases aprendidos com aprovação;
- monitoramento ativo.

---

## Fase 4 — NF-e

Só entra depois do pedido estável.

### Escopo

- emissão de NF-e a partir do pedido;
- validação fiscal mais conservadora;
- qualquer dúvida fiscal bloqueia;
- usar regras do Bling/natureza de operação, sem inventar imposto no payload.

---

# 4. Tabelas sugeridas

## `wholesale_order_messages`

Armazena cada mensagem recebida.

- `id`
- `message_id`
- `remote_jid`
- `sender_id`
- `sender_name`
- `raw_text`
- `message_type`
- `received_at`
- `processed_at`
- `status`

## `wholesale_order_decisions`

Armazena decisão do agente.

- `id`
- `message_id`
- `intent`
- `order_number`
- `decision`
- `confidence_score`
- `decision_reason`
- `should_create_order`
- `created_bling_order_id`
- `needs_human_review`
- `created_at`

## `wholesale_order_items`

Itens interpretados.

- `id`
- `decision_id`
- `line_number`
- `raw_description`
- `resolved_sku`
- `quantity`
- `unit_price`
- `sku_confidence`
- `resolution_method`
- `resolution_reason`

## `wholesale_products`

Catálogo local.

- `sku`
- `bling_product_id`
- `official_name`
- `description`
- `active`
- `unit`
- `embedding`
- `last_bling_sync_at`

## `wholesale_product_aliases`

Aliases editáveis.

- `id`
- `sku`
- `alias`
- `source`
- `status`
- `confidence_boost`
- `approved_by`
- `active`

## `wholesale_order_authorized_senders`

Allowlist.

- `id`
- `name`
- `phone_or_lid`
- `active`
- `can_create_order`
- `can_edit_order`

## `wholesale_order_dlq`

Dead letter queue.

- `id`
- `message_id`
- `stage`
- `error_type`
- `error_message`
- `payload`
- `attempts`
- `status`
- `next_action`
- `created_at`
- `updated_at`

## `wholesale_pipeline_health`

Estado do pipeline.

- `id`
- `component`
- `status`
- `last_ok_at`
- `last_error_at`
- `details`

---

# 5. Decisões pendentes para Pedro aprovar

1. Confirmar faixas:
   - `>= 0.90` cria;
   - `0.70–0.89` revisão;
   - `< 0.70` bloqueia/pergunta.

2. Confirmar se na Fase 2 a faixa `0.70–0.89` pode criar pedido marcado para revisar ou se continua bloqueada.

3. Confirmar allowlist inicial:
   - Pedro Fernandes;
   - Pedro Broglio;
   - outros nomes/números?

4. Confirmar se o core deve sair do N8N e virar worker próprio.

5. Confirmar matriz de resposta no grupo.

6. Confirmar se Fase 1 deve ficar silenciosa no grupo ou responder apenas bloqueios.

7. Confirmar se cliente novo sempre bloqueia no início.

8. Confirmar volume mínimo para sair da Fase 1: 50 pedidos/14 dias ou 100 pedidos.

---

# 6. Recomendação final

Minha recomendação é não avançar para criação real ainda.

Antes, fazer:

1. Fase 0 de fundação;
2. Fase 1 dry-run com painel;
3. só depois criação controlada.

A mudança mais importante em relação ao v1 é:

> O agente continua autônomo para interpretar, mas o pipeline passa a ser mensurável, monitorável, pausável e auditável.

Sem isso, ele pode até acertar 90% dos pedidos, mas os 10% errados vão ser difíceis de detectar, explicar e reverter.

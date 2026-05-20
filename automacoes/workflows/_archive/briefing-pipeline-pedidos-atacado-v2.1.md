---
title: "Briefing v2.1 — Correções finais do Pipeline Agente de Pedidos de Atacado"
type: briefing
created: 2026-05-14
status: superseded
owner: Pedro Broglio
base_document: briefing-pipeline-pedidos-atacado-v2.md
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
  - agente-pedidos
---

# Briefing v2.1 — Correções finais

Este documento não substitui a v2 inteira. Ele fecha os 7 pontos pendentes apontados por Pedro e deve ser lido como adendo/correção da v2.

---

## 1. Cliente novo — regra fechada

**Decisão:** concordo com Pedro. Cliente novo deve bloquear nas Fases 1, 2 e 3.

### Regra

Se o CNPJ não existir no Bling/cadastro local sincronizado, o pedido **não é criado**.

O agente deve classificar como:

```text
blocked_client_not_found
```

### Comportamento

- Não cria pré-cadastro automático.
- Não cria pedido com contato incompleto.
- Não tenta “deduzir” endereço, IE, razão social ou dados fiscais.
- Responde no grupo apenas se a matriz de resposta permitir bloqueios de negócio.
- Registra no painel/DLQ operacional como pendência de cadastro.

### Justificativa

Pré-cadastro automático tem risco fiscal alto e pode sujar o Bling com dados ruins. Fica fora do escopo até nova decisão explícita.

---

## 2. Allowlist real — levantamento inicial

**Decisão:** a allowlist entra na Fase 0. Ela deve começar com todos os remetentes reais do grupo, mas separados por status.

### Dados levantados no grupo WhatsApp “Pedidos de Venda - GB”

O histórico visível para o WhatsApp do Kobe hoje é curto: **6 mensagens armazenadas desde a entrada no grupo**.

Pedidos observados:

| Nome observado | JID/LID Evolution | Número WhatsApp | Evidência | Status sugerido |
|---|---|---|---|---|
| Pedro Fernandes | `280577496317989@lid` | `5519994550679` | Enviou pedidos 953 e 955 | `authorized_create` |
| Pedro Broglio | `135566498779355@lid` | `5519993040768` | Enviou teste/pedido 954 | `admin` |
| Kobe | `135832669298708@lid` | `5519998458149` | Número do agente no grupo | `system` |
| Participante não identificado | `55220444864752@lid` | `5519996877398` | Está no grupo, sem pedido observado | `pending_validation` |

### Regra operacional

A allowlist terá 3 níveis:

| Status | Pode criar pedido? | Pode editar pedido? | Ação |
|---|---:|---:|---|
| `admin` | Sim | Sim | Pedro/Kobe/admins |
| `authorized_create` | Sim | Sim, se aprovado | vendedores autorizados |
| `pending_validation` | Não | Não | loga e alerta privado se parecer pedido |
| `system` | Não cria pedido humano | Não | usado apenas para responder/status |
| `blocked` | Não | Não | ignora |

### Próximo passo antes da Fase 0

Pedro deve validar quem é o participante:

```text
5519996877398 / 55220444864752@lid
```

Até validação, ele não cria pedido automaticamente.

---

## 3. Áudio — política definida

**Levantamento atual:** no histórico visível do grupo, foram encontrados:

- **3 mensagens de pedido por texto**;
- **0 pedidos por áudio**;
- **0 mensagens de áudio** no recorte disponível.

Percentual observado hoje: **0%**.

### Limitação do dado

A amostra é pequena porque o WhatsApp do Kobe só tem histórico recente do grupo. Portanto, o número atual não prova que áudio nunca acontece.

### Regra v2.1

Áudio de remetente autorizado **não será ignorado silenciosamente**.

Desde a Fase 1:

1. áudio de remetente autorizado entra como `midia_audio_potencial_pedido`;
2. o áudio é transcrito por Whisper/OpenAI Audio ou equivalente;
3. a transcrição passa pelo classificador de intenção;
4. se for pedido, entra no mesmo pipeline de interpretação;
5. pedidos por áudio na Fase 1 ficam em dry-run, sem criação real;
6. áudio sem transcrição bem-sucedida vai para DLQ.

### Gatilho de prioridade

Se, durante Fase 1, áudio representar **mais de 10% das mensagens elegíveis** em janela móvel de 30 mensagens, áudio vira caminho obrigatório para Fase 2, não opcional.

### Recomendação

Não precisa entrar na Fase 0 como criação de pedido, mas a infraestrutura para armazenar mídia/transcrição e medir percentual entra na Fase 0. A transcrição entra na Fase 1 desde o início.

---

## 4. Alerta por mensagem elegível sem decisão em 2 minutos

**Decisão:** concordo. Este é o alerta mais importante.

Heartbeat sozinho não basta.

### Regra

Qualquer mensagem que cumpra todos os critérios abaixo deve ter decisão registrada em até **2 minutos**:

- veio do grupo correto;
- veio de remetente autorizado ou pendente com aparência de pedido;
- não é conversa óbvia;
- contém sinais mínimos de pedido ou edição.

Se não houver decisão em 2 minutos:

```text
alert_private_pedro_unprocessed_message
```

### Alerta privado

Enviar para Pedro no privado:

```text
Alerta: mensagem elegível no grupo de atacado não foi processada em até 2 minutos.
Remetente: [nome]
Horário: [hora]
Tipo provável: [novo_pedido/edicao]
Ação sugerida: verificar pipeline/DLQ.
```

### Por que isso teria pego o problema anterior

Mesmo com webhook aparentemente configurado, o pedido 955 teria ficado sem decisão registrada. Esse gatilho detectaria a falha independentemente do motivo técnico.

---

## 5. Política de retry da DLQ

**Decisão:** concordo com a sugestão de Pedro.

### Regra padrão

Falhas técnicas terão **3 tentativas automáticas**:

| Tentativa | Quando roda |
|---:|---|
| 1 | após 1 minuto |
| 2 | após 5 minutos |
| 3 | após 15 minutos |

Depois da terceira falha:

```text
pending_review
```

E dispara alerta privado para Pedro.

### O que entra em retry

Retry apenas para falhas técnicas/transitórias:

- timeout Bling;
- HTTP 500/502/503/504;
- falha temporária do LLM;
- falha temporária do banco;
- erro de rede;
- rate limit.

### O que não entra em retry

Falhas de negócio não fazem retry automático:

- cliente não encontrado;
- SKU ambíguo;
- CNPJ inválido;
- preço suspeito;
- quantidade inválida;
- remetente não autorizado.

Essas vão direto para:

```text
blocked_business_rule
```

ou

```text
needs_human_input
```

### Estados da DLQ

```text
pending_retry
retrying
pending_review
resolved
ignored
```

---

## 6. Validação determinística — checklist explícito

Esta validação roda **depois do agente** e **antes de qualquer chamada de criação no Bling**.

### Checklist obrigatório

1. **Origem**
   - Grupo é o grupo correto?
   - Mensagem tem `message_id`?
   - Remetente está na allowlist?

2. **Intenção**
   - Classificação é `novo_pedido` ou `edicao_pedido`?
   - Conversa/mídia irrelevante não pode seguir.

3. **Idempotência**
   - Já existe decisão para o mesmo `message_id`?
   - Já existe pedido criado para o mesmo número de pedido GB?
   - Se sim, não cria duplicado.

4. **Cliente**
   - CNPJ tem 14 dígitos válidos?
   - CNPJ existe no cadastro local/Bling?
   - Cliente novo bloqueia.

5. **SKU / Produto**
   - SKU existe no catálogo local?
   - SKU tem `bling_product_id` vinculado?
   - Produto está ativo?
   - Se múltiplos itens: todos os itens passaram?

6. **Confiança**
   - Score final `>= 0.90` para criação automática?
   - Se `0.70–0.89`, vai para revisão/dry-run conforme fase.
   - Se `< 0.70`, bloqueia/pergunta.

7. **Preço**
   - Preço unitário maior que zero?
   - Preço dentro da faixa histórica do SKU?
   - Regra inicial: tolerância de **±20%** da mediana histórica dos últimos 90 dias.
   - Se não houver histórico suficiente, usar preço de referência manual ou bloquear para revisão.

8. **Quantidade**
   - Quantidade maior que zero?
   - Quantidade abaixo do limite máximo do SKU?
   - Limite inicial padrão: 500 unidades por item, ajustável por SKU.
   - Se exceder limite, bloqueia para revisão.

9. **Total**
   - Se a mensagem trouxer total geral, soma dos itens deve bater com tolerância de centavos.
   - Tolerância inicial: diferença máxima de R$ 0,05 por arredondamento.
   - Se não houver total na mensagem, não bloqueia por ausência de total.

10. **Pagamento**
   - Forma de pagamento existe?
   - Se houver prazo/parcelamento, registrar texto natural.
   - Se houver desconto/bonificação, exige justificativa.

11. **Bling readiness**
   - Token Bling válido?
   - Endpoint Bling respondendo?
   - Produto/cliente possuem IDs necessários para payload?

12. **Payload final**
   - Payload passa schema interno?
   - Nenhum campo crítico vazio?
   - Pedido vai nascer em status editável?

### Resultado da validação

A validação só pode retornar:

```text
validation_passed
blocked_business_rule
needs_human_input
technical_failure
```

---

## 7. SLA do Bling e comportamento em falha

**Decisão:** concordo com timeout de 10s.

### Timeout

Cada chamada ao Bling terá timeout de **10 segundos**.

### Retries Bling

Para chamadas de leitura ou criação que falharem por erro técnico:

| Tentativa | Backoff |
|---:|---|
| 1 | imediato |
| 2 | 1 minuto |
| 3 | 5 minutos |

Se ainda falhar:

```text
technical_failure_bling
```

Vai para DLQ e alerta privado para Pedro.

### O que é falha técnica

- timeout;
- HTTP 500;
- HTTP 502/503/504;
- erro de rede;
- rate limit;
- token expirado sem refresh bem-sucedido.

### O que não fazer

Não responder no grupo:

```text
deu erro técnico
sistema fora
Bling caiu
```

Erro de infraestrutura não deve poluir o grupo.

### Resposta no grupo

O grupo só recebe resposta para decisão de negócio:

- pedido criado;
- pedido bloqueado por falta de dado;
- SKU ambíguo;
- cliente não encontrado;
- pedido duplicado;
- edição aplicada ou não permitida.

Falha técnica vai para alerta privado e DLQ.

---

# Estimativa atualizada da Fase 0

## Fase 0 — Fundação de segurança

### Escopo incluído

- schema/tabelas base;
- allowlist real com status;
- catálogo local inicial;
- aliases editáveis;
- classificador de intenção;
- DLQ com retry explícito;
- heartbeat;
- alerta de mensagem elegível sem decisão em 2 minutos;
- botão de pânico;
- modo dry-run global;
- logs explicáveis;
- infraestrutura para armazenar/transcrever áudio na Fase 1;
- remoção do N8N do caminho crítico ou redução para receptor simples.

### Estimativa

**2 a 3 dias úteis** para uma Fase 0 sólida.

Se simplificar painel e deixar só banco + logs + alertas no primeiro corte: **1,5 a 2 dias úteis**.

Minha recomendação é não espremer. Melhor gastar os 2–3 dias e entrar na Fase 1 com segurança real.

---

# Pendências de validação do Pedro

Antes de iniciar Fase 0, validar:

1. O participante `5519996877398 / 55220444864752@lid` deve ser autorizado ou não?
2. Confirmar Pedro Fernandes como `authorized_create`.
3. Confirmar tolerância inicial de preço: **±20% da mediana histórica dos últimos 90 dias**.
4. Confirmar limite padrão inicial de quantidade: **500 unidades por item**, ajustável por SKU.
5. Confirmar que cliente novo bloqueia em Fases 1, 2 e 3.
6. Confirmar que erro técnico nunca responde no grupo, só alerta privado.

---

# Recomendação final

Com esses 7 pontos fechados, a arquitetura fica pronta para aprovação.

A Fase 0 deve começar somente depois da validação desta v2.1.

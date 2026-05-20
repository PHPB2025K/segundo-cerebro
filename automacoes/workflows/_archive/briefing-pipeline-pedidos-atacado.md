---
title: "Briefing — Pipeline Pedido de Atacado → Bling"
type: briefing
created: 2026-05-14
status: superseded
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
---

# Briefing — Pipeline Pedido de Atacado → Bling

## Objetivo

Criar um pipeline onde mensagens enviadas no grupo de WhatsApp **Pedidos de Venda - GB** sejam interpretadas por um agente responsável, transformadas em pedidos de venda no **Bling Matriz** e respondidas no próprio grupo com status claro.

A lógica central é: **não queremos um parser burro de formulário; queremos um agente de pedidos.**

O agente deve ler a mensagem como uma pessoa treinada da equipe leria, entender o pedido mesmo com texto imperfeito, descobrir o SKU correto quando houver descrição suficiente e só pedir ajuda quando a dúvida for real.

---

## Regra principal

O agente deve resolver sozinho tudo que uma pessoa treinada conseguiria resolver olhando:

- a mensagem recebida;
- o catálogo de produtos;
- os SKUs cadastrados;
- apelidos e nomes coloquiais;
- histórico de pedidos anteriores;
- cliente, vendedor, preço e contexto do pedido.

Ele **não deve bloquear só porque o campo veio fora do padrão**.

Ele só deve perguntar no grupo quando:

- não houver descrição nenhuma do produto;
- a descrição servir para mais de um SKU;
- o produto não existir no catálogo;
- a confiança estiver baixa;
- faltar dado obrigatório que não pode ser inferido com segurança.

---

## Fluxo geral

```text
Mensagem no WhatsApp
        ↓
Captura da mensagem
        ↓
Agente interpreta o pedido
        ↓
Agente resolve produto/SKU
        ↓
Validação de segurança
        ↓
Criação do pedido no Bling
        ↓
Resposta no grupo
        ↓
Registro e aprendizado
```

---

## 1. Entrada: mensagem no grupo de atacado

Toda mensagem nova no grupo **Pedidos de Venda - GB** deve ser analisada.

O agente deve tentar capturar:

- número do pedido;
- estoque: 2024 ou 2025;
- cliente novo ou existente;
- tipo do pedido: retirada, entrega ou transportadora;
- nome da empresa;
- CNPJ;
- se emite NF;
- contato da empresa;
- descrição do produto;
- SKU, se vier explícito;
- quantidade;
- preço de venda;
- forma de pagamento;
- vendedor.

A mensagem pode vir com erros, espaços estranhos, campo quebrado, preço solto, campo sem asterisco ou marcação irregular. O agente precisa ser tolerante com isso.

---

## 2. Interpretação inteligente

A interpretação deve ser feita por um agente, não apenas por regras fixas.

### O que o agente precisa fazer

1. Ler a mensagem bruta.
2. Entender os campos mesmo que estejam mal formatados.
3. Identificar o produto descrito.
4. Resolver o SKU correto.
5. Medir confiança da decisão.
6. Decidir se cria, bloqueia ou pergunta.

### Exemplo de comportamento esperado

Se vier:

```text
Descrição do Produto/SKU: Caixa de fita 300
```

O agente deve entender que isso provavelmente representa o SKU cadastrado para **Caixa Fita Adesiva 300m**.

Se vier:

```text
cx fita 300
fita 300
caixa fita
caixa de fita
```

O agente também deve tentar resolver sozinho usando aliases e histórico.

---

## 3. Resolução automática de SKU

Essa é a parte mais importante do pipeline.

O agente deve tentar identificar o SKU usando, nesta ordem:

1. **SKU explícito na mensagem**  
   Exemplo: `CXFIT300M`.

2. **Mapa de apelidos e aliases**  
   Exemplo: `Caixa de fita 300` → `CXFIT300M`.

3. **Catálogo do Bling**  
   Busca por nome, descrição e código.

4. **Histórico de pedidos anteriores**  
   Se um mesmo texto já foi corrigido/aprovado antes, usar esse aprendizado.

5. **Contexto comercial**  
   Preço, cliente, vendedor e padrões anteriores podem ajudar a desempatar, mas não podem inventar SKU.

### Quando não criar

Não criar pedido se:

- a descrição do produto estiver ausente;
- mais de um SKU parecer igualmente provável;
- o produto não existir no catálogo;
- o agente estiver inseguro;
- houver divergência grave entre descrição, SKU e preço.

---

## 4. Validação obrigatória antes do Bling

Mesmo que o agente interprete bem, o pedido só pode ser criado depois de validação objetiva.

Campos obrigatórios:

- número do pedido GB;
- CNPJ válido;
- cliente encontrado no Bling;
- SKU encontrado no Bling;
- quantidade válida;
- preço válido;
- forma de pagamento;
- idempotência: o mesmo pedido não pode ser criado duas vezes.

### Travas de segurança

O sistema deve bloquear se:

- o cliente não existir no Bling;
- o SKU não existir no Bling;
- houver desconto/bonificação sem justificativa;
- o preço parecer artificialmente reduzido;
- o pedido já tiver sido processado;
- houver ambiguidade real no SKU.

---

## 5. Criação do pedido no Bling

Quando tudo estiver seguro, o sistema cria o pedido de venda no **Bling Matriz**.

O pedido deve incluir:

- número do pedido GB;
- cliente;
- produto/SKU;
- quantidade;
- preço;
- forma de pagamento;
- vendedor;
- estoque informado;
- tipo de pedido;
- contato;
- observação interna dizendo que veio do WhatsApp;
- ID da mensagem original para rastreabilidade.

Nesta fase, o ideal é criar **somente pedido de venda**.

A emissão de NF-e deve ser uma etapa posterior, porque envolve mais risco fiscal.

---

## 6. Resposta automática no grupo

Depois de processar, o agente deve responder no grupo com uma mensagem curta e clara.

### Pedido criado

```text
Pedido 955 criado no Bling com sucesso.
Cliente: Eduardo Maranim
SKU: CXFIT300M
Quantidade: 1
```

### Falta produto

```text
Pedido 955 não foi criado.
Faltou informar o produto/SKU.
Pode enviar a descrição do produto?
```

### SKU ambíguo

```text
Pedido 955 não foi criado.
A descrição “pote vidro” pode ser mais de um SKU.
Qual SKU correto?
```

### Cliente não encontrado

```text
Pedido 955 não foi criado.
CNPJ não encontrado no Bling.
Preciso do cadastro completo do cliente antes de gerar o pedido.
```

### Pedido duplicado

```text
Pedido 955 já tinha sido processado anteriormente.
Não criei duplicado.
```

---

## 7. Registro e aprendizado

Cada pedido deve gerar log estruturado.

Registrar:

- mensagem original;
- campos interpretados;
- SKU escolhido;
- nível de confiança;
- status final;
- motivo do bloqueio, se houver;
- ID do pedido no Bling, se criado;
- resposta enviada no grupo;
- correções humanas posteriores.

### Aprendizado esperado

Se uma descrição for corrigida/aprovada manualmente, isso deve virar regra futura.

Exemplo:

```text
"caixa fita 300" → CXFIT300M
```

Depois de aprovado, o agente deve lembrar isso nos próximos pedidos.

---

## 8. Fases de implantação

## Fase 1 — Monitoramento sem criar pedido

O agente lê a mensagem, interpreta e registra o que teria feito.

Não cria pedido real.

Objetivo: validar interpretação e resolução de SKU.

---

## Fase 2 — Criação controlada

O agente cria pedidos reais no Bling, mas apenas em testes acompanhados.

Objetivo: validar ponta a ponta com risco controlado.

---

## Fase 3 — Produção assistida

O agente cria automaticamente quando a confiança for alta.

Quando houver dúvida, pergunta no grupo.

Objetivo: operar no dia a dia com supervisão leve.

---

## Fase 4 — NF-e

Depois que a criação de pedidos estiver estável, adicionar etapa de emissão de nota.

Essa fase precisa ser mais conservadora.

Qualquer dúvida fiscal deve bloquear.

---

## Decisões que precisam ser lapidadas

1. Qual nível de confiança mínimo para criar pedido automaticamente?
2. Quais SKUs podem ser resolvidos por apelido sem pedir confirmação?
3. Cliente novo deve sempre bloquear ou pode criar pré-cadastro?
4. O agente deve responder no grupo sempre ou só quando houver erro?
5. Quem pode enviar pedido válido no grupo?
6. A criação automática deve começar em modo dry-run ou já em controlado real?
7. Quando entrará a etapa de NF-e?

---

## Princípio final

O pipeline certo é:

**WhatsApp → agente interpreta → resolve SKU → valida → cria pedido no Bling → responde no grupo → aprende com o resultado.**

O ponto central é: **o agente deve agir como uma pessoa operacional treinada, não como um formulário rígido.**

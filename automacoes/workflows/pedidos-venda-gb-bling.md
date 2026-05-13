---
title: "Workflow N8N — Pedidos de Venda GB → Bling Matriz"
type: workflow
created: 2026-05-13
status: draft-inactive
tags:
  - n8n
  - whatsapp
  - bling
  - fisco
  - pedidos-venda
---

# Workflow N8N — Pedidos de Venda GB → Bling Matriz

## Status

- **N8N workflow:** `GB — Pedidos de Venda WhatsApp → Bling Matriz (Fisco)`
- **Workflow ID:** `T7WT4vGaRuWd0N0Q`
- **Status no N8N:** criado como **inativo** por segurança.
- **Webhook test:** `https://trottingtuna-n8n.cloudfy.live/webhook-test/pedidos-venda-gb`
- **Webhook produção:** `https://trottingtuna-n8n.cloudfy.live/webhook/pedidos-venda-gb`

## Motivo de ficar inativo na primeira criação

O fluxo já está publicado no N8N, mas deve permanecer inativo até fechar a ponta do Fisco/Bling com credencial segura e endpoint definitivo. Ativar agora poderia receber mensagem real e falhar na criação do pedido por falta do serviço final de Fisco exposto.

## Pipeline criado

1. `Webhook Evolution — Pedidos GB`
   - Recebe POST da Evolution API.
   - Path: `pedidos-venda-gb`.

2. `Normalizar Evento`
   - Extrai texto, `remoteJid`, `participant`, `messageId`, `pushName`, `groupName` e timestamp.
   - Filtra intenção por grupo e estrutura mínima de pedido.

3. `Parse + Validação Fisco`
   - Extrai campos do pedido por linhas `campo: valor` e regex fallback.
   - Campos esperados:
     - número do pedido GB
     - estoque
     - cliente novo
     - tipo
     - nome da empresa
     - CNPJ
     - contato
     - produto/SKU
     - quantidade
     - preço de venda
     - método de pagamento
     - vendedor
   - Bloqueia se faltar CNPJ, produto/SKU, quantidade, preço, forma de pagamento ou número do pedido.
   - Bloqueia desconto/bonificação sem justificativa documentada.

4. `Idempotência message_id + pedido`
   - Usa `messageId:numero_pedido_gb` como chave.
   - Reserva a chave em static data do workflow para evitar duplicidade.

5. `Payload para Fisco`
   - Monta payload canônico para o Fisco:
     - idempotency key
     - origem
     - IDs da mensagem/grupo/remetente
     - texto bruto
     - objeto `pedido` parseado.

6. `Criar Pedido no Bling Matriz via Fisco`
   - HTTP POST para endpoint do Fisco.
   - Endpoint placeholder atual: `https://mission.budamix.com.br/api/fisco/pedidos-venda-gb` ou env `FISCO_PEDIDOS_WEBHOOK_URL`.
   - Deve ser substituído pelo endpoint real assim que a lógica Fisco estiver exposta.

7. `Log Resultado`
   - Acrescenta timestamp de processamento ao retorno.

8. `Montar Pergunta de Complemento`
   - Para caso ambíguo/faltante, monta resposta curta solicitando os dados ausentes no grupo.

9. `Responder no Grupo — Completar Dados`
   - Envia texto via Evolution para o grupo quando há campos faltantes.
   - Usa credencial N8N existente de header auth; validar contra a instância WhatsApp próprio Kobe antes de ativar.

10. `Responder Webhook`
   - Responde JSON para a chamada da Evolution/N8N.

## Próximos passos

1. Confirmar/implementar endpoint real do Fisco para criação do pedido no Bling Matriz.
2. Validar credencial Evolution usada no node de resposta ao grupo.
3. Testar com 3–5 mensagens reais do grupo `Pedidos de Venda - GB` usando webhook test.
4. Só depois ativar o workflow em produção e apontar a Evolution para o webhook production.

## Segurança fiscal

- Não criar pedido se faltar campo obrigatório.
- Não processar valor artificialmente reduzido.
- Desconto/bonificação só passa com justificativa comercial/fiscal explícita.
- Idempotência por `message_id + número do pedido`.
- Um pedido por execução; fila fica a cargo do N8N/Evolution e, se necessário, será evoluída para worker determinístico.

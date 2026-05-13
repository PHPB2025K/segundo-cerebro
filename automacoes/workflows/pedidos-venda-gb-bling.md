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
- **Status no N8N:** **ativo em produção** para teste controlado.
- **Webhook test:** `https://trottingtuna-n8n.cloudfy.live/webhook-test/pedidos-venda-gb`
- **Webhook produção:** `https://trottingtuna-n8n.cloudfy.live/webhook/pedidos-venda-gb`
- **Evolution WhatsApp Kobe:** webhook configurado para `MESSAGES_UPSERT` no endpoint de produção do N8N.
- **Fisco/Bling:** rota ativa no Mission Control em `/api/fisco/pedidos-venda-gb`, com segredo compartilhado, LLM opcional, mapa de aliases SKU, validação determinística, idempotência persistente e dry-run validado.

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
   - HTTP POST para endpoint real do Fisco: `https://mission.budamix.com.br/api/fisco/pedidos-venda-gb`.
   - Envia segredo compartilhado `X-Fisco-Secret`.
   - O Fisco interpreta a mensagem com LLM + mapa de aliases SKU quando necessário; o N8N não é autoridade final de interpretação.

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

1. Ampliar `sku-aliases.json` com os principais produtos/nomes coloquiais usados pelo Pedro Fernandes.
2. Testar 3–5 mensagens reais novas do grupo `Pedidos de Venda - GB`.
3. Ajustar resposta no grupo para casos bloqueados/ambíguos.
4. Só liberar criação automática contínua depois de alguns pedidos controlados sem erro.

## Validação de 13/05/2026

- Mensagem real do grupo, pedido **953**, foi capturada pela Evolution.
- N8N ativo recebeu payload em replay controlado; parser original foi substituído como autoridade por interpretação Fisco/LLM.
- Rota Fisco dry-run com texto real validou:
  - descrição `Caixa de fita 300` → SKU `CXFIT300M` via LLM + alias map;
  - CNPJ `55.773.184/0001-14` encontrou contato no Bling Matriz;
  - SKU `CXFIT300M` encontrou produto no Bling Matriz;
  - payload de pedido montado com quantidade 8 e preço unitário R$ 232,90;
  - PDF dry-run gerado.
- Pedido real **não foi criado** nesse teste; validação foi `dry_run_ok`.

## Segurança fiscal

- Não criar pedido se faltar campo obrigatório.
- Não processar valor artificialmente reduzido.
- Desconto/bonificação só passa com justificativa comercial/fiscal explícita.
- Idempotência por `message_id + número do pedido`.
- Um pedido por execução; fila fica a cargo do N8N/Evolution e, se necessário, será evoluída para worker determinístico.

---
title: "Briefing v2.3 — Adendo de Geração e Envio Automático do PDF do Pedido"
type: briefing
created: 2026-05-14
status: draft-for-approval
owner: Pedro Broglio
base_documents:
  - briefing-pipeline-pedidos-atacado-v2.md
  - briefing-pipeline-pedidos-atacado-v2.1.md
  - briefing-pipeline-pedidos-atacado-v2.2.md
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
  - pdf
---

# Briefing v2.3 — Geração e envio automático do PDF do pedido

Este documento adiciona à v2.2 a entrega final do fluxo: **todo pedido criado no Bling deve gerar PDF e o PDF deve ser postado automaticamente no grupo `Pedidos de Venda - GB`**.

---

# 1. Regra geral

Toda vez que um pedido for criado com sucesso no Bling, o agente deve:

1. capturar o `bling_order_id` retornado pela API;
2. gerar o PDF do pedido;
3. enviar a mensagem de confirmação no grupo;
4. anexar o PDF no mesmo grupo;
5. registrar no log o status da geração e do envio.

Essa regra vale para:

- cliente antigo;
- cliente recém-cadastrado;
- pedido simples;
- pedido com múltiplos itens.

---

# 2. Decisão técnica do Kobe sobre o PDF

## Resultado do teste real

### 2.1 Token Bling

- O token da Matriz estava expirado no momento do teste.
- O refresh foi executado com sucesso.
- Depois do refresh, a API voltou a responder normalmente.

### 2.2 Endpoint oficial de PDF de pedido

Eu testei os caminhos óbvios de API v3 para PDF de pedido, incluindo variações como:

- `/pedidos/vendas/{id}/pdf`
- `/pedidos/vendas/{id}/imprimir`
- `/pedidos/vendas/{id}/impressao`
- `/pedidos/vendas/{id}/gerar-pdf`

Todos retornaram **404** no ambiente atual.

### Conclusão prática

**Hoje eu não tenho evidência suficiente de um endpoint oficial e funcional de PDF de pedido via API v3 do Bling neste ambiente.**

Então, para Fase 2, a recomendação segura é:

> implementar o fluxo de PDF com arquitetura híbrida: tentar o PDF oficial do Bling se houver endpoint confirmado; se não houver, gerar o PDF operacional a partir dos dados do pedido retornados pela API.

Isso garante que o fluxo de criação real de pedido não fique bloqueado por uma dependência obscura ou instável da documentação do Bling.

---

# 3. Estratégia oficial da v2.3

## Caminho A — Preferencial

Se identificarmos e validarmos um endpoint oficial do Bling para PDF de pedido:

- usar o PDF do próprio Bling;
- manter retry síncrono + assíncrono;
- enviar o arquivo no grupo.

## Caminho B — Fallback obrigatório

Se o endpoint oficial não existir, não estiver liberado ou falhar repetidamente:

- o agente gera o PDF operacional usando os dados do pedido via API;
- converte para PDF;
- envia no grupo com o mesmo padrão de nome;
- registra no log como `generated_internal_fallback`.

### Regra de produção

A Fase 2 **não pode ligar criação real de pedido sem um caminho de PDF funcionando**.

Pode ser:

- PDF oficial do Bling; ou
- PDF operacional gerado pelo agente.

Mas um dos dois precisa estar validado antes do go-live.

---

# 4. Fluxo detalhado

```text
Pedido criado no Bling (status Em aberto)
        ↓
Bling retorna order_id
        ↓
Tenta gerar PDF oficial do Bling
        ↓
Se falhar, tenta fallback interno
        ↓
Se conseguir PDF em até 3 tentativas rápidas
        ↓
Mensagem de confirmação + PDF no grupo
        ↓
Log de PDF registrado
```

Se não conseguir nas 3 tentativas rápidas:

```text
Mensagem de confirmação sem PDF
        ↓
Fila assíncrona de retry
        ↓
Quando PDF sair, envia complementar no grupo
        ↓
Se falhar permanentemente, DLQ + alerta privado
```

---

# 5. Nome do arquivo

Padrão obrigatório:

```text
Pedido_[NUMERO]_[NomeCliente]_[YYYY-MM-DD].pdf
```

Exemplo:

```text
Pedido_955_EduardoMaranim_2026-05-14.pdf
```

## Regras

- usar o número do pedido GB / número operacional do pedido, não o ID interno do Bling;
- nome do cliente sem acento, sem espaço, sem caractere especial;
- truncar nome do cliente em 30 caracteres;
- padrão final recomendado: **CamelCase sem espaço**.

---

# 6. Mensagem no grupo

## 6.1 Fluxo normal

```text
Pedido 955 criado no Bling.
Cliente: Eduardo Maranim
SKU: CXFIT300M
Quantidade: 1
PDF do pedido em anexo.
```

## 6.2 Cliente recém-cadastrado

```text
Pedido 955 criado no Bling.
Cliente: Eduardo Maranim (CNPJ XX.XXX.XXX/XXXX-XX)
Cliente foi cadastrado agora — verificar dados se necessário.
SKU: CXFIT300M
Quantidade: 1
PDF do pedido em anexo.
```

## 6.3 Múltiplos itens

Listar os itens resumidamente e terminar com:

```text
PDF do pedido em anexo.
```

---

# 7. Retry do PDF

## 7.1 Retry síncrono antes da mensagem

| Tentativa | Quando roda |
|---:|---|
| 1 | imediato |
| 2 | +10s |
| 3 | +30s |

Se qualquer uma funcionar:

- envia confirmação + PDF juntos;
- status do log: `success_first_try` ou `success_after_retry`.

## 7.2 Retry assíncrono depois da confirmação

Se as 3 tentativas rápidas falharem:

1. envia a confirmação no grupo sem o PDF;
2. adiciona tarefa à fila de PDF;
3. tenta novamente em background.

| Tentativa | Quando roda |
|---:|---|
| 4 | +2 min |
| 5 | +10 min |
| 6 | +30 min |

Se conseguir em background:

```text
PDF do pedido 955 em anexo.
```

Se falhar permanentemente:

- vai para DLQ;
- alerta privado para Pedro;
- nunca fala “erro técnico” no grupo.

---

# 8. Logs do PDF

Adicionar tabela nova:

## `wholesale_order_pdf_log`

Campos:

- `id`
- `bling_order_id`
- `order_number_gb`
- `pdf_filename`
- `pdf_storage_path`
- `pdf_source` (`bling_official`, `internal_fallback`)
- `attempts_count`
- `total_time_ms`
- `success`
- `posted_to_group_at`
- `final_status` (`success_first_try`, `success_after_retry`, `success_async`, `failed_permanent`)
- `error_message`
- `created_at`

---

# 9. Checklist determinístico — novo grupo pós-criação

Adicionar ao checklist o grupo 13:

## 13. Pós-criação do pedido

- Pedido criado retornou ID válido?
- Geração de PDF oficial foi tentada?
- Fallback interno foi tentado se necessário?
- PDF foi entregue no grupo?
- Se não foi entregue na janela síncrona, entrou na fila assíncrona?
- Log de PDF foi registrado?
- Se falhou permanentemente, alerta privado foi enviado?

---

# 10. Resultado do teste real do PDF

## Pedido usado no teste

- Pedido Bling: **658**
- `bling_order_id`: **25810872351**
- Cliente: **CLICK & COMPRE LTDA**
- Itens: **2**

## O que foi validado

- leitura do pedido via API Bling: **OK**;
- geração de PDF por fallback interno: **OK**;
- arquivo gerado com sucesso: **OK**.

## Qualidade do PDF de fallback atual

### Pontos bons

- tem cliente;
- tem CNPJ;
- tem itens;
- tem SKU;
- tem quantidade;
- tem valores;
- tem identificação do pedido.

### Pontos a melhorar antes de produção

- formatar total em pt-BR corretamente;
- não exibir blocos JSON crus de transporte/pagamento;
- melhorar visual para parecer documento operacional final;
- remover sobras técnicas do HTML impresso;
- alinhar melhor cabeçalho, rodapé e observações.

### Conclusão do teste

O fallback funciona e prova viabilidade.

Mas ele ainda precisa de **polimento visual** antes de ser o PDF enviado automaticamente no grupo em produção.

---

# 11. Impacto no prazo da Fase 0

PDF continua fora do escopo principal da Fase 0, mas exige preparação.

## O que a Fase 0 precisa deixar pronto

- tabela `wholesale_order_pdf_log`;
- estrutura de fila assíncrona para retry;
- caminho de armazenamento do PDF;
- teste de conectividade/autorização do Bling;
- decisão técnica oficial: endpoint Bling vs fallback interno.

## Impacto estimado

Isso adiciona **menos de meio dia** se fizermos só a fundação.

### Prazo atualizado da Fase 0

Minha recomendação mantém:

```text
4 dias úteis
```

Com possível variação para **4,5 dias** se quisermos já sair da Fase 0 com o fallback de PDF muito bem polido.

Mas, como o envio real do PDF entra só na Fase 2, eu manteria a Fase 0 oficialmente em **4 dias úteis**.

---

# 12. Recomendação final do Kobe

Eu concordo com o adendo.

A única correção técnica importante é esta:

> Não devemos depender cegamente de um endpoint de PDF do Bling que ainda não foi confirmado como acessível neste ambiente.

Então a regra da v2.3 fica:

- tentar PDF oficial do Bling, se houver;
- se não houver, usar fallback interno;
- criação real de pedido só entra na Fase 2 quando um dos dois estiver validado ponta a ponta.

---

# 13. Decisões para aprovação

1. Aprovar que a v2.3 use **estratégia híbrida** (Bling oficial + fallback interno).
2. Aprovar que o fallback interno é aceitável na Fase 2 se o endpoint oficial do Bling continuar indisponível.
3. Aprovar manutenção da Fase 0 em **4 dias úteis**.
4. Aprovar que o polimento visual do PDF de fallback seja um dos primeiros blocos da Fase 2.

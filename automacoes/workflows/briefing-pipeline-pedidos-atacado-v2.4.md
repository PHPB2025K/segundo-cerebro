---
title: "Briefing v2.4 — Correção crítica: PDF oficial do Bling obrigatório"
type: briefing
created: 2026-05-14
status: draft-for-approval
owner: Pedro Broglio
base_documents:
  - briefing-pipeline-pedidos-atacado-v2.3.md
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
  - pdf
---

# Briefing v2.4 — PDF oficial do Bling obrigatório

Esta versão corrige a v2.3.

A regra de fallback interno para PDF **não é aceita** para envio ao cliente/equipe.

O PDF enviado no grupo precisa ser obrigatoriamente o **PDF oficial/exato gerado pelo Bling**, no mesmo formato que seria baixado/imprimido manualmente dentro do Bling.

---

## 1. Correção da decisão técnica

### Antes, na v2.3

A v2.3 propôs uma estratégia híbrida:

- tentar PDF oficial do Bling;
- se não funcionasse, gerar um PDF operacional interno como fallback.

### Correção v2.4

Essa estratégia está errada para produção.

O fallback interno pode existir apenas para **debug interno**, nunca para envio no grupo e nunca como documento operacional final.

Regra final:

> Pedido criado no Bling → gerar/baixar o PDF oficial do Bling → enviar esse PDF no grupo.

Se o PDF oficial do Bling não puder ser obtido, o fluxo de envio de PDF **falha** e entra em retry/DLQ. Não substitui por PDF interno.

---

## 2. Regra obrigatória

Toda criação real de pedido na Fase 2 só pode ser ligada quando estiver validado:

1. criação do pedido no Bling;
2. obtenção do PDF oficial/exato do Bling;
3. envio desse PDF no grupo de WhatsApp;
4. log do envio.

Se o item 2 não estiver resolvido, **não libera Fase 2**.

---

## 3. PDF interno/fallback

PDF interno gerado pelo agente fica restrito a:

- teste técnico;
- debug;
- comparação visual;
- diagnóstico quando o Bling estiver indisponível.

Ele não pode ser enviado no grupo como PDF do pedido.

Ele não pode substituir o documento oficial do Bling.

Ele não pode ser encaminhado para cliente.

---

## 4. Comportamento quando o PDF oficial falhar

Se o pedido foi criado no Bling, mas o PDF oficial não foi obtido:

1. Não enviar PDF interno.
2. Enviar no grupo apenas a confirmação operacional, se a regra da fase permitir:

```text
Pedido 955 criado no Bling.
Cliente: Eduardo Maranim
SKU: CXFIT300M
Quantidade: 1
PDF está sendo gerado, envio em alguns instantes.
```

3. Colocar a geração/extração do PDF oficial em fila assíncrona.
4. Tentar novamente conforme política de retry.
5. Quando conseguir, enviar o PDF oficial no grupo:

```text
PDF do pedido 955 em anexo.
```

6. Se falhar definitivamente, DLQ + alerta privado para Pedro.

Mensagem de erro técnico nunca aparece no grupo.

---

## 5. Retry do PDF oficial

## Tentativas rápidas

| Tentativa | Quando roda |
|---:|---|
| 1 | imediato |
| 2 | +10s |
| 3 | +30s |

## Tentativas assíncronas

| Tentativa | Quando roda |
|---:|---|
| 4 | +2 min |
| 5 | +10 min |
| 6 | +30 min |

Após tentativa 6 sem sucesso:

- `failed_permanent_pdf_official`;
- DLQ;
- alerta privado para Pedro;
- pedido continua válido no Bling, mas o PDF precisa ser gerado manualmente ou o conector corrigido.

---

## 6. Impacto no prazo

Essa correção aumenta risco técnico porque o endpoint oficial de PDF do pedido ainda não foi confirmado no ambiente atual.

Na validação anterior, os caminhos óbvios da API v3 retornaram 404.

Portanto, a Fase 0 precisa incluir uma investigação específica para descobrir o caminho real de obtenção do PDF oficial:

- endpoint API documentado, se existir;
- rota alternativa autenticada do Bling;
- exportação/impressão oficial via sessão web/headless, se a API não oferecer endpoint;
- suporte/documentação Bling, se necessário.

### Estimativa atualizada

- Fase 0 base com cadastro automático: **4 dias úteis**.
- Investigação/validação obrigatória do PDF oficial: **+0,5 a 1 dia útil**.

Prazo realista atualizado da Fase 0:

```text
4,5 a 5 dias úteis
```

Se o endpoint oficial aparecer rápido, volta para 4 dias.

Se depender de automação web/headless autenticada no Bling, considerar 5 dias.

---

## 7. Decisão final

A Fase 2 só pode começar quando esta cadeia estiver provada:

```text
Pedido real criado no Bling
        ↓
PDF oficial do Bling obtido
        ↓
PDF oficial enviado no grupo
        ↓
Log registrado
```

Sem PDF oficial do Bling, não existe go-live de criação real.

## Conectado a

- [[automacoes/workflows/pedidos-venda-gb-bling]] — **filho**: workflow N8N que implementa o briefing (rota /api/fisco/pedidos-venda-gb)
- [[projects/financeflow]] — **dependência**: FinanceFlow agente Fisco cria o pedido no Bling Matriz
- [[openclaw/agents/fisco/IDENTITY]] — **executor**: Fisco interpreta a mensagem com LLM + alias map e emite o pedido
- [[knowledge/concepts/bling-api-v3-aprendizados]] — **tema**: API v3 do Bling tem comportamentos não-óbvios que afetam a obtenção do PDF
- [[projects/mission-control]] — **ref**: rota /api/fisco/pedidos-venda-gb hospedada no Mission Control

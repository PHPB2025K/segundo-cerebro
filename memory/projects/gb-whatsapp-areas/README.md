---
title: "Relatórios WhatsApp por Área — GB Importadora"
created: 2026-05-20
type: project-memory
status: active
---

# Relatórios WhatsApp por Área — GB Importadora

Rotina diária de leitura read-only dos grupos internos de WhatsApp da GB, com relatório independente por área e memória separada.

## Áreas e destinos Telegram

| Área | Grupo WhatsApp | Tópico Telegram |
|---|---|---|
| Financeiro | Financeiro - GB Importadora | Financeiro (7) |
| Compras | Compras - GB Importadora | Compras (11) |
| Contas a Receber | Contas a Receber - GB Importadora | Financeiro (7) |
| Contas a Pagar | Contas a Pagar - GB Importadora | Financeiro (7) |
| Vendas Atacado | Vendas atacado - GB Importadora | Tópico 6 |
| Expedição | Expedição - GB Importadora | Expedição (10911) |
| Sócios | Sócios - GB Importadora | Sócios (10912) |

## Regras

- Leitura WhatsApp apenas via Evolution/local.
- Envio em grupos continua proibido por padrão; exceção aprovada por Pedro em 2026-05-25: Kobe pode enviar automaticamente no grupo **Financeiro - GB Importadora** a solicitação dos extratos de movimentação das contas GB, 3x/mês, direcionada à Simone.
- Uma execução por dia às 18:31 BRT para leitura/relatório das áreas.
- Síntese independente por área: não misturar assuntos entre grupos.
- Memória persistente separada por área: decisões, pendências, responsáveis, riscos e histórico diário.
- Não persistir dados sensíveis: senhas, tokens, cartões, dados bancários completos, CPF/RG/documentos pessoais.

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

- Leitura WhatsApp apenas via Evolution/local; nunca enviar mensagem nos grupos.
- Uma execução por dia às 18:31 BRT.
- Síntese independente por área: não misturar assuntos entre grupos.
- Memória persistente separada por área: decisões, pendências, responsáveis, riscos e histórico diário.
- Não persistir dados sensíveis: senhas, tokens, cartões, dados bancários completos, CPF/RG/documentos pessoais.

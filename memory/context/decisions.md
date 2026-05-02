---
title: "Decisões"
created: 2026-05-01
type: context
status: active
tags:
  - memory
  - context
  - decisions
---

# Decisões — Índice Operacional

_Este arquivo existe para cumprir o contrato operacional `memory/context/decisions.md`. O histórico detalhado continua em `memory/context/decisoes/`._

## 2026-05-01 — Fechamento financeiro abril/2026

- Relatórios financeiros não devem chamar `SETTLEMENT`/extrato financeiro de faturamento bruto sem qualificador.
- Usar **faturamento bruto comercial** para pedidos válidos do mês e **receita liquidada em extrato** para settlement/financeiro.
- Abril/2026 validado: faturamento comercial R$ 405.839,65; receita liquidada em extrato R$ 354.992,67.
- Para Shopee Ads abril/2026, usar o número oficial de plataforma informado manualmente pelo Pedro: R$ 9.460, vendas via Ads R$ 165.600, ROAS 17,51. Wallet API fica como conciliação/alerta, não como consumo oficial.
- Amazon Ads abril/2026 via API Sponsored Products validado: gasto R$ 2.478,95; vendas atribuídas R$ 11.749,58; ROAS 4,74; ACOS 21,10%.
- DRE da GB deve seguir estrutura clássica completa, não apuração simplificada de marketplace.

## 2026-05-01 — Fiscal / NFs internas abril/2026

- Orientação v2.1 da Suellen/FOUR permanece como fonte de verdade para transferência Matriz SC → Filial SP: CFOP 6.152, CST ICMS 90, ICMS sem destaque, IPI suspenso CST 55, origem Matriz=1 e Filial=2.
- Venda interna Filial SP → CNPJs Simples SP é operação distinta: CFOP 5.102, origem 2, ICMS interno 18% e IPI conforme NCM quando aplicável.
- NFs internas de abril/2026 devem cobrir apenas produtos importados próprios GB; excluir nacionais, MDF, cerâmica, livros, fita, pseudo-itens, SEM_SKU, terceiros e Jarra Clink/CK4742.
- Antes de emitir NF interna mensal, reconciliar estoque fiscal por SKU/componente: saldo inicial Matriz/Filial, entradas/transferências do mês, vendas do mês, aliases Bling, kits e fatores de conversão.
- Para abril/2026, emissão validada integralmente pela Filial porque a Filial cobria os componentes após corrigir conversões de caixas/conjuntos. A inconsistência histórica de YW1520 na Matriz fica como ressalva separada.
- Vendas B2B/atacado emitidas pela Matriz devem abater estoque fiscal da Matriz antes de qualquer uso de saldo Matriz como excedente.
- NFs internas abril/2026 autorizadas: 000031, 000032, 000033, total R$ 77.065,09.
- NFs de transferência abril/2026 000649 e 000653 foram enviadas à FOUR/financeiro em 01/05/2026 com observação de que saíram antes da orientação fiscal atualizada.


## 2026-05-02 — Guarani Sistemas / distrato contratual

- Guarani Sistemas: estratégia aprovada para contestar a cobrança integral, exigir suspensão de protesto e memória de cálculo aberta, e negociar distrato **sem reconhecimento de dívida** com âncora/teto técnico inicial de **R$ 7.002,30**, condicionado a quitação total, baixa dos boletos/NFs 2384–2390 e inexistência de saldo remanescente.

## Ver também

- `memory/context/decisoes/kobe-permanentes.md`
- `memory/context/decisoes/2026-04.md`
- `memory/context/decisoes/2026-05.md`

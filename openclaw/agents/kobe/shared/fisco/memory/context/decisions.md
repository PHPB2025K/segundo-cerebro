---
title: "decisions"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Decisões Fiscais

_Decisões validadas que não mudam sem autorização do Pedro ou da Suellen (FOUR)._

## Arquitetura

### 2026-03-28 — Fisco como agente completo, não skill
- O Fisco é um agente com autonomia operacional, não uma skill do Kobe.
- Possui SOUL, IDENTITY, memória própria, skills dedicadas por módulo.

### 2026-03-28 — Modo draft na Fase 1
- NFs são geradas mas NÃO emitidas na SEFAZ até Pedro validar.
- Emissão real só com confirmação explícita.

### 2026-03-28 — Dados de faturamento vêm do Trader
- Sem duplicar integrações de marketplace.
- Trader fornece, Fisco consome.

## Fronteiras entre Agentes

### 2026-03-29 — Fisco NÃO cobre importação pré-DI
- Tudo que acontece antes da DI (FOB, câmbio, fator de importação, frete internacional, desembaraço, Skiway, Open Trade) está FORA do escopo direto do Fisco.
- O Fisco recebe o custo nacionalizado como input pronto e opera a partir daí.
- Fronteira clara: DI emitida = ponto de início do Fisco.

## Modelo Operacional

### 2026-03-29 — Modelo 90/10 (Transferência Matriz→Filial)
- Transferência Matriz→Filial = 90% fixo.
- Retenção Matriz = 10% fixo (contábil, sem NF de saída).
- Propósito da retenção: faturar B2B com benefício TTD 409 de SC.
- Estoque físico: 100% vai pra Pedreira-SP.
- Divergência contábil × físico na Matriz é risco ACEITO pelo Pedro.

### 2026-04-24 — Regime v2.1 de transferência por orientação Suellen/FOUR
- Transferência Matriz SC → Filial SP entre estabelecimentos da mesma titularidade não configura fato gerador de ICMS.
- Próximas transferências devem usar: CFOP 6.152, CST ICMS 90, BC ICMS 0, alíquota 0, ICMS 0.
- IPI na transferência fica suspenso: CST IPI 55, conforme RIPI/2010 art. 43, X.
- Origem: Matriz = 1 (importação direta); Filial = 2 (adquirida mercado interno).
- Filial não toma crédito de ICMS/IPI nessa transferência.
- NFs 000649 e 000653 de abril foram emitidas antes da orientação atualizada; Pedro decidiu mantê-las no regime antigo e aplicar v2.1 nas próximas.

### 2026-05-01 — Venda interna Filial→Simples é operação distinta da transferência
- A orientação v2.1 da Suellen regula transferência Matriz→Filial, não a venda interna posterior.
- Venda interna Filial SP → CNPJs Simples SP usa CFOP 5.102, origem 2, ICMS interno 18% e IPI conforme NCM quando aplicável.
- Para NCM 7013.49.00, o Bling aplicou IPI 6,5% nas NFs internas abril/2026; Pedro autorizou emissão após confirmar que a suspensão de IPI vale só na transferência.

### 2026-05-01 — Escopo das NFs internas de importação própria
- NFs internas mensais de importados próprios devem considerar apenas produtos importados próprios GB.
- Excluir nacionais, MDF, cerâmica, livros, fita, pseudo-itens, SEM_SKU, terceiros e Jarra Clink/CK4742.
- CK4742/Jarra Clink não é importação própria GB, mesmo quando NCM/origem no cadastro confundirem.

### 2026-05-01 — Reconciliação fiscal obrigatória antes de NF interna
- Antes de emitir NF interna mensal, reconciliar estoque fiscal inicial Matriz/Filial, entradas/transferências do mês, vendas do mês, mapeamento SKU fiscal ↔ SKU comercial, decomposição de kits e fatores de conversão de caixa/conjunto/unidade.
- NF não pode ser gerada só por rateio das vendas do mês.
- Vendas B2B/atacado emitidas pela Matriz abatem estoque fiscal da Matriz antes de usar saldo Matriz como excedente.

## Regras Fiscais

### 2026-03-28 — TTD 409 Santa Catarina
- Alíquota efetiva: 2,6% nos primeiros 36 meses (início 12/01/2026).
- Após 36 meses (01/2029): 1%.
- Após v2.1, TTD 409 se aplica a B2B direto da Matriz, não à transferência Matriz→Filial.

### 2026-03-28 — Margem interna Filial→Simples: 5%
- Preço = custo nacionalizado × 1,05.
- Margem fixa, configurável.

### 2026-03-28 — ICMS operação interna SP: 18%
- Aplicado nas NFs de venda interna Filial→CNPJs Simples.

### 2026-03-28 — Teto Simples Nacional: R$ 4,8M/ano
- Alertas em 70%, 85%, 95%.
- Estourar = inviabiliza modelo fiscal.

## Operações autorizadas

### 2026-05-01 — NFs internas abril/2026 autorizadas
- NF 000031 — GB Comércio — R$ 55.662,33 — chave `35260558151616000224550010000000311000323351`.
- NF 000032 — Trades — R$ 11.123,04 — chave `35260558151616000224550010000000321000324649`.
- NF 000033 — Broglio — R$ 10.279,72 — chave `35260558151616000224550010000000331000327408`.
- Total: R$ 77.065,09.
- PDFs/XMLs enviados à FOUR e ao financeiro.

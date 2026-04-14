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

### 2026-03-29 — Fisco NÃO cobre importação
- Tudo que acontece antes da DI (FOB, câmbio, fator de importação, frete internacional, desembaraço, Skiway, Open Trade) está FORA do escopo do Fisco.
- Um agente de importação será criado futuramente para cobrir essa parte.
- O Fisco recebe o custo nacionalizado como input pronto e opera a partir daí.
- Fronteira clara: DI emitida = ponto de início do Fisco.

## Modelo Operacional

### 2026-03-29 — Modelo 90/10 (Transferência Matriz→Filial)
- Transferência Matriz→Filial = 90% fixo (NF CFOP 6.152)
- Retenção Matriz = 10% fixo (contábil, sem NF de saída)
- Propósito da retenção: faturar B2B com benefício TTD 409 de SC
- Estoque físico: 100% vai pra Pedreira-SP
- Divergência contábil × físico na Matriz é risco ACEITO pelo Pedro
- Validado pela Suellen (FOUR Contabilidade)
- Substitui modelo anterior de transferência 100%

### 2026-03-29 — Riscos fiscais conhecidos e aceitos
- Riscos declarados no documento fiscal v2.0 (18/03/2026):
  1. Questionamento SEFAZ-SC e SEFAZ-SP
  2. Questionamento sobre política de preço interno (margem 5%)
  3. Glosa de créditos de ICMS
  4. Autuações por inconsistências de estoque (10% Matriz contábil, 0 físico)
  5. Mudanças legislativas afetando TTD 409 ou Simples Nacional
- Pedro assinou declaração de responsabilidade assumindo esses riscos
- Suellen (FOUR) avaliou e validou

### 2026-03-29 — Flexibilidade da reserva B2B
- Reserva B2B da Filial (~4%): se não houver demanda, pode ser redistribuída pros CNPJs Simples
- Retenção Matriz (10%): é FIXA — não se redistribui sem nova decisão

## Regras Fiscais

### 2026-03-28 — TTD 409 Santa Catarina
- Alíquota efetiva: 2,6% nos primeiros 36 meses (início 12/01/2026).
- Após 36 meses (01/2029): 1%.
- Parâmetro configurável em tax-rules.json.

### 2026-03-28 — Margem interna Filial→Simples: 5%
- Preço = custo nacionalizado × 1,05.
- Margem fixa, configurável.

### 2026-03-28 — ICMS operação interna SP: 18%
- Aplicado nas NFs de venda interna Filial→CNPJs Simples.

### 2026-03-28 — CFOP 6.152 para transferência
- Transferência interestadual de mercadoria SC→SP.

### 2026-03-28 — Teto Simples Nacional: R$ 4,8M/ano
- Alertas em 70%, 85%, 95%.
- Estourar = inviabiliza modelo fiscal.

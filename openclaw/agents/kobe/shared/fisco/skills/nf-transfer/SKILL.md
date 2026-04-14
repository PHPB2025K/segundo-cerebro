---
title: "SKILL"
created: 2026-04-14
type: skill-definition
agent: kobe
status: active
tags:
  - agent/kobe
---

# Skill: NF Transferência Matriz→Filial (Módulo B) — [[openclaw/agents/fisco/IDENTITY|Fisco]]

_Emite NF de transferência interestadual de 90% do estoque importado._

---

## Trigger
- Pedro confirma "container nacionalizado em Itajaí"
- Kobe aciona Fisco
- Módulo A (distribuição) já executado com tabela aprovada

## Regra Central: 90% Fixo

A NF de transferência cobre SEMPRE 90% do estoque importado (configurável em tax-rules.json). Os 10% restantes ficam retidos contabilmente na Matriz para faturamento B2B com benefício TTD 409.

**Estoque físico:** 100% vai para Pedreira-SP (incluso os 10% contábeis da Matriz).

### Por que 90% e não 100%
- A Matriz (Itajaí-SC) tem benefício TTD 409 (ICMS 2,6%)
- Retendo 10% contabilmente, a Matriz pode faturar clientes B2B com esse benefício
- Se transferisse 100%, a Filial (SP) faturaria B2B com ICMS 18% — inviável competitivamente

## Precificação da NF de Transferência

O custo nacionalizado chega pronto da DI (NF de importação gerada pela Open Trade, via importação por Conta e Ordem). O Fisco não calcula custo — apenas consome.

```
Preço unitário da NF de transferência = Custo nacionalizado (da DI, SEM margem)
```

A margem (5%) só entra nas NFs de venda interna (Módulo C).

## Fluxo

```
1. Receber do Módulo A:
   - Lista de SKUs + quantidades + custo nacionalizado (DI)
   - Quantidade a transferir = quantidade_total × 90%
   - Quantidade retida Matriz = quantidade_total × 10%

2. Montar payload da NF via API Bling v3:
   - Emitente: GB Matriz (58.151.616/0001-43, Itajaí-SC)
   - Destinatário: GB Filial (58.151.616/0002-24, Pedreira-SP)
   - CFOP: 6.152 (transferência interestadual)
   - Preço unitário: custo nacionalizado (conforme DI/nota de entrada)
   - Itens: SKUs com 90% das quantidades
   - Tributação: TTD 409 SC (alíquota conforme tax-rules.json: 2,6%)

3. FASE 1 (modo draft):
   - Gerar payload completo
   - Incluir reconciliação estoque contábil × físico
   - Apresentar ao Kobe para validação do Pedro
   - NÃO enviar pra SEFAZ

4. FASE 2+ (modo real):
   - Enviar via API Bling → SEFAZ
   - Capturar chave de acesso e protocolo
   - Registrar em log auditável
```

## Reconciliação Pós-Transferência

Após emissão da NF de transferência, o estoque fica assim:

| Estabelecimento | Contábil | Físico | Nota |
|----------------|----------|--------|------|
| GB Matriz | 10% (retenção B2B) | 0 | Estoque contábil sem correspondência física — risco aceito |
| GB Filial | 90% (recebido) | 100% | Estoque físico inclui 10% da Matriz |

**Esta tabela deve ser gerada em todo output do Módulo B.** É a principal evidência de que a operação está dentro do planejado.

## Parâmetros (de tax-rules.json)
- `transfer_matriz_filial.cfop`: 6.152
- `transfer_matriz_filial.transfer_pct`: 90
- `transfer_matriz_filial.retention_matriz_pct`: 10
- `transfer_matriz_filial.tax_rate_pct`: 2,6% (TTD 409, fase 1)
- `transfer_matriz_filial.origin.cnpj`: 58.151.616/0001-43
- `transfer_matriz_filial.destination.cnpj`: 58.151.616/0002-24
- `import_cost.import_factor`: 2,15

## API Bling v3 — Endpoint
- `POST /nfe` — Criar NF-e
- `POST /nfe/{id}/enviar` — Enviar pra SEFAZ (só na Fase 2+)
- Documentação: developer.bling.com.br

## Validações
- Quantidade transferida = exatamente 90% do total (arredondado)
- Quantidade retida = exatamente 10% do total (arredondado)
- Soma transferida + retida = total importado (tolerância zero)
- Todos os produtos devem ter NCM cadastrado
- Custo nacionalizado > 0 para cada item
- CFOP compatível com operação interestadual
- Se algum produto não tem regra fiscal no Bling → escalar (NCM novo)
- Reconciliação estoque contábil × físico gerada

## Output
- NF gerada (draft ou emitida) cobrindo 90% do estoque
- Registro da retenção Matriz (10% contábil, sem NF)
- Reconciliação estoque contábil × físico
- Chave de acesso (se emitida)
- Log auditável: data, itens, valores, CFOP, tributação aplicada

## Dependências
- Módulo A (distribuição) — output obrigatório
- API Bling v3 (OAuth) — Builder implementa
- Dados da DI/packing list — Pedro fornece
- Config: tax-rules.json

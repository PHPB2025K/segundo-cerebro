---
title: "Estratégia Fiscal de Faturamento — GB Importadora"
created: 2026-04-17
type: reference
status: active
domain: importacao
version: 2.0
official_date: 2026-03-18
vault_decision_date: 2026-03-29
pdf_updated_at: 2026-04-17
tags:
  - business/fiscal
  - business/importacao
  - regras
  - agent/fisco
---

# Estratégia Fiscal de Faturamento — GB Importadora

> Fonte da verdade para o modelo fiscal da GB. Toda emissão de NF, transferência entre estabelecimentos, distribuição entre CNPJs Simples, precificação interna e declaração contábil deve seguir o que está aqui.
>
> PDF oficial assinável: [estrategia-fiscal-gb-v2.0.pdf](estrategia-fiscal-gb-v2.0.pdf) (Manual de Procedimentos Fiscais v2.0, atualizado 17/04/2026 para refletir decisão de 2026-03-29 validada com Suellen/FOUR).

## Regra central — Modelo 90/10

1. **Transferência Matriz→Filial = 90% fixo** (CFOP 6.152, interestadual SC→SP, mercadoria importada)
2. **10% permanece retido contabilmente na Matriz (SC)** — usado para faturamento B2B com benefício TTD 409 (ICMS efetivo 2,6% na Fase 1 até 01/2029, depois 1,0%)
3. **Estoque físico 100% vai para Pedreira-SP** — os 10% são contábeis, não físicos. Divergência contábil × físico na Matriz é risco declarado e aceito
4. **Reserva B2B residual da Filial (~4%)** é dinâmica (% B2B últimos 3 meses) — se não houver demanda B2B, redistribui pros CNPJs Simples
5. **Proporções dos CNPJs Simples** são dinâmicas (% de cada CNPJ nos últimos 3 meses de faturamento real)
6. **Margem interna fixa 5%** — preço Filial→Simples = custo nacionalizado × 1,05

## Estrutura societária

### Nível 1 — Lucro Presumido (Importação / B2B)
| Empresa | CNPJ | Local | Função |
|---|---|---|---|
| **GB MATRIZ** | 58.151.616/**0001-43** | Itajaí-SC | Importa com TTD 409, faturamento B2B com benefício SC |
| **GB FILIAL** | 58.151.616/**0002-24** | Pedreira-SP | Recebe 90%, vende pros CNPJs Simples |

### Nível 2 — Simples Nacional (Varejo / Marketplaces — ~96% das vendas)
| Empresa | CNPJ | Canais |
|---|---|---|
| GB Comércio | 07.194.128/0001-82 | Mercado Livre + Amazon + Shopee shop_id 448649947 |
| Trades | 45.200.547/0001-79 | Shopee shop_id 860803675 |
| Broglio | 63.922.116/0001-06 | Shopee shop_id 442066454 |

## Fórmulas

```
% Reserva B2B     = Faturamento B2B ÷ Faturamento Total
% Varejo          = 100% − % Reserva B2B
% Cada CNPJ       = Faturamento CNPJ ÷ Faturamento Varejo Total
Preço Interno     = Custo Nacionalizado × 1,05
Quantidade transferida    = Quantidade total × 0,90
Quantidade retida Matriz  = Quantidade total × 0,10
```

⚠ **As proporções devem ser recalculadas a cada nova importação com base nos últimos 3 meses de faturamento real.**

## Fluxo operacional (a cada importação)

```
1. MATRIZ (SC) nacionaliza via Open Trade (Conta e Ordem, TTD 409)
2. MATRIZ emite NF de transferência de 90% para FILIAL (SP) — CFOP 6.152
3. MATRIZ retém 10% contábil (sem NF de saída) para B2B TTD 409
4. Estoque físico 100% segue para Pedreira-SP
5. FILIAL apura % B2B e proporções CNPJs Simples (últimos 3 meses)
6. FILIAL reserva % B2B residual (dinâmico, ~4%)
7. FILIAL emite NFs para os 3 CNPJs Simples (CFOP 5.102, ICMS 18%)
8. CNPJs Simples vendem ao consumidor final nos marketplaces
```

## Precificação interna — exemplo

| Componente | Valor |
|---|---|
| FOB (USD) | US$ 10,00 |
| Câmbio | R$ 5,50 |
| Fator importação | 2,15 |
| Custo nacionalizado | R$ 118,25 |
| Margem 5% | R$ 5,91 |
| **Preço interno** | **R$ 124,16** |
| ICMS 18% (interna SP) | R$ 22,35 |

## NFs emitidas — resumo

| NF | Emitente | Destinatário | CFOP | ICMS | Quando |
|---|---|---|---|---|---|
| Transferência | GB Matriz (SC) | GB Filial (SP) | **6.152** | 4% destacado / 2,6% efetivo TTD 409 | A cada container nacionalizado |
| B2B Matriz | GB Matriz (SC) | Cliente B2B | 6.102 | 4% destacado / TTD 409 | Sob demanda, dentro dos 10% retidos |
| Venda interna Filial | GB Filial (SP) | GB Comércio / Trades / Broglio | **5.102** | 18% (interna SP) | Mensal, proporcional ao faturamento |
| Venda interestadual Filial | GB Filial (SP) | Cliente B2B fora de SP | 6.102 | 4% (Res. Senado 13/2012 — importado) | Sob demanda |
| Venda consumidor | 3 CNPJs Simples | Consumidor final | — | Simples Nacional | A cada pedido marketplace |

## Checklist operacional — a cada nova importação

- [ ] 1. Nacionalizar mercadoria pela MATRIZ
- [ ] 2. Emitir NF transferência **90%** para FILIAL (CFOP 6.152)
- [ ] 3. Registrar 10% retido contábil na MATRIZ
- [ ] 4. Transferir estoque físico (100%) para Pedreira
- [ ] 5. Apurar % B2B no faturamento (últimos 3 meses)
- [ ] 6. Calcular reserva B2B residual da Filial
- [ ] 7. Apurar % de cada CNPJ Simples no varejo
- [ ] 8. Calcular quantidade para cada CNPJ
- [ ] 9. Calcular preço interno (custo × 1,05)
- [ ] 10. Emitir NFs de venda para CNPJs Simples
- [ ] 11. Atualizar controles de estoque

## Riscos declarados e aceitos

Conforme Declaração de Responsabilidade (PDF v2.0, seção 9), Pedro assinou e a Suellen (FOUR) validou:

1. Questionamento pelas SEFAZ-SC e SEFAZ-SP
2. Questionamento sobre a política de preço interno (margem 5%)
3. Glosa de créditos de ICMS
4. Autuações por inconsistências de estoque (10% Matriz contábil, 0 físico)
5. Mudanças na legislação afetando TTD 409 ou Simples Nacional

**Limite crítico:** estourar Simples Nacional (R$ 4,8M/ano) em qualquer CNPJ inviabiliza TODO o modelo. Headroom total = R$ 14,4M/ano (3 CNPJs × R$ 4,8M). O agente Fisco monitora isso (Módulo E).

## Timeline

| Data | Evento |
|---|---|
| 2026-03-18 | PDF v2.0 inicial criado — modelo 100% |
| 2026-03-29 | Decisão 90/10 validada com Suellen — registrada em [[openclaw/agents/kobe/shared/fisco/memory/context/decisions]] |
| 2026-04-17 | PDF v2.0 atualizado para refletir modelo 90/10 (consistente com vault) |

## Fontes vinculadas

- PDF oficial: [estrategia-fiscal-gb-v2.0.pdf](estrategia-fiscal-gb-v2.0.pdf)
- Decisão no vault: [[openclaw/agents/kobe/shared/fisco/memory/context/decisions]]
- Contexto do negócio: [[openclaw/agents/kobe/shared/fisco/memory/context/business]]
- Skill NF Transferência (Módulo B): [[openclaw/agents/kobe/shared/fisco/skills/nf-transfer/SKILL]]
- Skill Emissão Bling: [[openclaw/agents/kobe/shared/fisco/skills/bling-nfe/SKILL]]
- Skill Venda Interna (Módulo C): [[openclaw/agents/kobe/shared/fisco/skills/nf-internal/SKILL]]
- Skill Distribuição (Módulo A): [[openclaw/agents/kobe/shared/fisco/skills/distribution/SKILL]]
- Agente responsável: [[openclaw/agents/fisco/IDENTITY]]
- Contadora: Suellen / FOUR Contabilidade

## Ver também

- [[business/importacao/_index]]
- [[meta/mocs/MOC - Taxas e Precificacao]]
- [[skills/gb-import-hub/SKILL]]
- [[projects/simulimpor]]

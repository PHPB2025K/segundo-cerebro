---
title: "Estratégia Fiscal de Faturamento — GB Importadora"
created: 2026-04-17
updated: 2026-04-24
type: reference
status: active
domain: importacao
version: 2.1
official_date: 2026-03-18
vault_decision_date: 2026-03-29
pdf_updated_at: 2026-04-17
v2_1_update_date: 2026-04-24
tags:
  - business/fiscal
  - business/importacao
  - regras
  - agent/fisco
---

# Estratégia Fiscal de Faturamento — GB Importadora

> Fonte da verdade para o modelo fiscal da GB. Toda emissão de NF, transferência entre estabelecimentos, distribuição entre CNPJs Simples, precificação interna e declaração contábil deve seguir o que está aqui.
>
> PDF oficial assinável: [estrategia-fiscal-gb-v2.0.pdf](estrategia-fiscal-gb-v2.0.pdf) (Manual de Procedimentos Fiscais v2.0, atualizado 17/04/2026).
>
> **v2.1 (24/04/2026):** Transferência Matriz→Filial passa a ser **sem destaque de ICMS** (LC 87/96 §4º + LC 204/2023 + Conv. ICMS 109/2024 + Ajuste SINIEF 33/2024) e **IPI suspenso** (art. 43 X RIPI/2010). TTD 409 continua válido apenas em B2B direto Matriz. Origem produtos Matriz = 1 (Importação direta). Orientação Suellen/FOUR por e-mail em 24/04/2026.

## Regra central — Modelo 90/10 (v2.1)

1. **Transferência Matriz→Filial = 90% fixo** (CFOP 6.152, interestadual SC→SP, mercadoria importada) — **SEM destaque de ICMS** (CST 90, fora do fato gerador conforme LC 204/2023) e **IPI suspenso** (CST 55, art. 43 X RIPI/2010)
2. **10% permanece retido contabilmente na Matriz (SC)** — usado para faturamento B2B direto com benefício TTD 409 (ICMS efetivo 2,6% na Fase 1 até 01/2029, depois 1,0%). **TTD 409 só aplica aqui** — não se aplica mais à transferência.
3. **Estoque físico 100% vai para Pedreira-SP** — os 10% são contábeis, não físicos. Divergência contábil × físico na Matriz é risco declarado e aceito
4. **Reserva B2B residual da Filial (~4%)** é dinâmica (% B2B últimos 3 meses) — se não houver demanda B2B, redistribui pros CNPJs Simples
5. **Proporções dos CNPJs Simples** são dinâmicas (% de cada CNPJ nos últimos 3 meses de faturamento real)
6. **Margem interna fixa 5%** — preço Filial→Simples = custo nacionalizado × 1,05. **Alerta (24/04/2026):** sem crédito ICMS da transferência, Filial paga ICMS cheio (18% interno SP) na venda aos Simples. Monitorar DFC 60-90 dias e revisar margem se necessário.

## Fundamento legal — v2.1

| Tema | Dispositivo | O que diz |
|------|-------------|-----------|
| ICMS sem destaque na transferência | LC 87/1996 art. 12 §4º (redação LC 204/2023) | Transferência entre estabelecimentos de mesma titularidade NÃO configura fato gerador do ICMS |
| Procedimento autorizado | Convênio ICMS 109/2024 + Ajuste SINIEF 33/2024 | Formaliza o tratamento uniforme na emissão de NF-e de transferência |
| IPI suspenso | RIPI/2010 art. 9º III + art. 43 X (Decreto 7.212/2010) | Filial equiparada a industrial (comércio atacadista) + suspensão permitida na transferência matriz-filial |
| TTD 409 (B2B Matriz) | TTD 125000001558420 / SC | Crédito presumido que reduz ICMS efetivo a 2,6% (Fase 1, até 01/2029) em B2B direto da Matriz |

## Origem dos produtos (cadastro Bling)

| Estabelecimento | Origem | Significado | Status cadastro |
|-----------------|:------:|-------------|-----------------|
| GB Matriz | **1** | Estrangeira — Importação direta | ✅ Corrigido em massa 24/04/2026 (91 produtos) |
| GB Filial | **2** | Estrangeira — adquirida no mercado interno (veio da transferência Matriz) | A validar no cadastro Bling Filial |

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

## NFs emitidas — resumo (v2.1, pós 24/04/2026)

| NF | Emitente | Destinatário | CFOP | ICMS | IPI | CST ICMS/IPI | Quando |
|---|---|---|---|---|---|---|---|
| Transferência | GB Matriz (SC) | GB Filial (SP) | **6.152** | **0%** (sem fato gerador, LC 204/2023) | **Suspenso** (RIPI art. 43 X) | **90 / 55** | A cada container nacionalizado |
| B2B Matriz | GB Matriz (SC) | Cliente B2B | 6.102 | 4% destacado / 2,6% efetivo TTD 409 | Conforme NCM | (regime antigo mantido) | Sob demanda, dentro dos 10% retidos |
| Venda interna Filial | GB Filial (SP) | GB Comércio / Trades / Broglio | **5.102** | 18% (interna SP) — **sem crédito de transferência** | Conforme NCM | 00 | Mensal, proporcional ao faturamento |
| Venda interestadual Filial | GB Filial (SP) | Cliente B2B fora de SP | 6.102 | 4% (Res. Senado 13/2012 — importado) | Conforme NCM | 00 | Sob demanda |
| Venda consumidor | 3 CNPJs Simples | Consumidor final | — | Simples Nacional | — | — | A cada pedido marketplace |

### Informações Complementares padrão — Transferência (CFOP 6152)

> Transferência interestadual de mercadoria entre estabelecimentos de mesma titularidade. Não ocorrência do fato gerador do ICMS, conforme art. 12, §4º, da LC nº 87/1996, com redação dada pela LC nº 204/2023. Sem destaque de ICMS próprio. Procedimento autorizado conforme Convênio ICMS nº 109/2024 e Ajuste SINIEF nº 33/2024. IPI suspenso conforme art. 43, X, do RIPI/2010 — Decreto nº 7.212/2010.

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
6. **(v2.1, 24/04/2026)** Ausência de crédito ICMS na Filial por conta da transferência sem destaque (LC 204/2023) — ICMS 18% pago cheio na venda Filial→Simples pode aumentar o custo fiscal efetivo. Risco calculado: antes a Filial recebia ~4% de crédito; agora zera. Monitorar 60-90 dias antes de revisar margem interna 5%.

**Limite crítico:** estourar Simples Nacional (R$ 4,8M/ano) em qualquer CNPJ inviabiliza TODO o modelo. Headroom total = R$ 14,4M/ano (3 CNPJs × R$ 4,8M). O agente Fisco monitora isso (Módulo E).

## Timeline

| Data | Evento |
|---|---|
| 2026-03-18 | PDF v2.0 inicial criado — modelo 100% |
| 2026-03-29 | Decisão 90/10 validada com Suellen — registrada em [[openclaw/agents/kobe/shared/fisco/memory/context/decisions]] |
| 2026-04-17 | PDF v2.0 atualizado para refletir modelo 90/10 (consistente com vault) |
| **2026-04-24** | **v2.1 — Transferência sem destaque ICMS (LC 204/2023) + IPI suspenso (RIPI art. 43 X). Orientação Suellen/FOUR por e-mail. Origem produtos Matriz corrigida em massa para 1 em 91 produtos. TTD 409 restrito a B2B direto Matriz.** |

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

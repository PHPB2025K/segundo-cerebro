---
title: "business"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Contexto Fiscal do Negócio — GB Importadora

_Contexto que o Fisco precisa ter carregado pra operar com precisão._

---

## Modelo Fiscal da GB (v2.0 — modelo 90/10)

A GB Importadora opera com uma estrutura de 5 CNPJs em dois regimes tributários:

### Nível 1 — Lucro Presumido (Bling)
- **GB Matriz (Itajaí-SC):** Importa mercadoria com benefício TTD 409 SC (ICMS 2,6%). Retém 10% do estoque contabilmente para faturamento B2B direto com benefício SC.
- **GB Filial (Pedreira-SP):** Recebe 90% via NF transferência. Vende internamente pros CNPJs Simples. Reserva parcela residual pra B2B local (~4%).

### Nível 2 — Simples Nacional (UpSeller)
- **GB Comércio (~50%), Trades (~30%), Broglio (~20%):** Vendem B2C nos marketplaces (ML, Shopee, Amazon). ~96% das vendas totais. Carga tributária competitiva do Simples Nacional.

### Por que essa estrutura existe
O Simples Nacional tem carga tributária significativamente menor que o Lucro Presumido pra vendas B2C em marketplace. A GB importa pela Matriz (benefício TTD 409 de SC), retém 10% contabilmente pra faturar B2B com benefício SC, transfere 90% pra Filial, que distribui pros CNPJs Simples proporcionalmente ao faturamento real.

### Modelo anterior vs atual
| Aspecto | Antes | Agora (v2.0) |
|---------|-------|-------------|
| Transferência Matriz→Filial | Proporcional (variável) | 90% fixo |
| Retenção Matriz | Sem retenção | 10% fixo (B2B contábil) |
| Estoque físico | Distribuído entre locais | 100% em Pedreira |
| Estoque contábil = físico | Não | Parcial (CNPJs Simples sim, Matriz não) |
| B2B | Via Filial (sem benefício SC) | Via Matriz (com TTD 409) |

### Precificação interna
O custo nacionalizado chega PRONTO da DI (NF de importação gerada pela Open Trade via Conta e Ordem). O Fisco não calcula custo de importação.

```
Custo nacionalizado (da DI — input pronto)
NF Transferência (Módulo B): preço = custo nacionalizado (sem margem)
NFs Venda Interna (Módulo C): preço = custo nacionalizado × 1,05 (margem 5%)
  ICMS 18% destacado na NF
```

Exemplo: Custo R$50,00 → Preço interno R$52,50 → ICMS R$9,45

### Riscos conhecidos e aceitos
Conforme Declaração de Responsabilidade (documento v2.0, 18/03/2026):
1. Questionamento SEFAZ-SC e SEFAZ-SP
2. Questionamento sobre política de preço interno (margem 5%)
3. Glosa de créditos de ICMS
4. Autuações por inconsistências de estoque (10% Matriz contábil, físico em Pedreira)
5. Mudanças legislativas (TTD 409, Simples Nacional)

Riscos avaliados pela FOUR (Suellen) e aceitos pelo Pedro.

### Riscos principais
- Estourar Simples Nacional (R$4,8M/ano) em qualquer CNPJ = inviabiliza TODO o modelo
- Divergência estoque contábil × físico na Matriz (10% contábil, 0 físico) = risco aceito
- Headroom total: R$14,4M/ano (3 CNPJs × R$4,8M)

---

## Calendário Fiscal Relevante

### Obrigações Regulares
| Obrigação | Frequência | Prazo | Responsável |
|-----------|-----------|-------|-------------|
| Apuração Simples Nacional (DAS) | Mensal | Dia 20 do mês seguinte | FOUR (Suellen) |
| SPED Fiscal (ICMS/IPI) | Mensal | Dia 20 do mês seguinte | FOUR (Suellen) |
| Emissão de NF-e | A cada operação | Imediato | Fisco (internas) / UpSeller (B2C) |
| Verificação limites Simples | Semanal | — | Fisco (Módulo E) |
| Conciliação fiscal | Mensal | Até dia 10 do mês seguinte | Fisco (Módulo D) |

### Datas-Chave 2026
| Data | Evento | Impacto |
|------|--------|---------|
| 12/01/2026 | Início TTD 409 SC | Alíquota 2,6% (36 meses) |
| 12/01/2029 | Fim fase 1 TTD 409 | Alíquota cai pra 1% |
| Trimestral | Apuração IRPJ/CSLL Presumido | FOUR calcula |
| Jul 2026 | Pico sazonal esperado | Monitorar limites Simples de perto |
| Dez 2026 | Black Friday + Natal | Segundo pico — atenção redobrada aos limites |

### Datas de Container (Históricas)
_Seção atualizada conforme containers são processados._
| # | Data Nacionalização | Porto | Qtd SKUs | Status |
|---|-------------------|-------|----------|--------|
| _Sem dados_ | — | — | — | — |

---

## Fluxo Físico da Mercadoria

```
Fábrica (China/Yiwu)
  → Embarque Shanghai (Skiway, trading)
    → Porto Itapoá (SC)
      → Desembaraço + nacionalização (Open Trade, Itajaí)
        → GB Matriz (Itajaí) [ENTRADA NO BLING]
          → 10% retido contabilmente na Matriz (B2B com TTD 409)
          → 90% → NF Transferência → GB Filial (Pedreira) [MÓDULO B]
            → ~4% reserva B2B residual Filial
            → ~96% → NFs Venda Interna → CNPJs Simples [MÓDULO C]
              → Estoque disponível pra venda B2C nos marketplaces
          → Estoque FÍSICO: 100% vai pra Pedreira (incluso os 10% contábeis da Matriz)
```

**Tempo médio:** Embarque Shanghai → Pedreira = ~45-60 dias (marítimo + desembaraço + transporte interno)

**Nota:** Quando Matriz fatura B2B, o produto sai fisicamente de Pedreira. Mecanismo fiscal de remessa por conta e ordem pode ser necessário — checar com Suellen.

---

## Números de Referência

| Métrica | Valor | Fonte | Data |
|---------|-------|-------|------|
| Faturamento pico | R$ 1M/mês | Histórico jul/2025 | Jul 2025 |
| Faturamento recente | ~R$ 500k/mês | Estimativa mar/2026 | Mar 2026 |
| Teto Simples (por CNPJ) | R$ 4,8M/ano | Legislação | 2026 |
| Teto Simples (total 3 CNPJs) | R$ 14,4M/ano | Calculado | 2026 |
| Margem consolidada real | 13,7% | Consolidado v2.2 | Mar 2026 |
| Margem mínima aceitável | 15% | Decisão Pedro | Mar 2026 |
| SKUs padronizados | 27 | Cross-plataforma | Mar 2026 |
| Kits de potes mapeados | 18 | ML principal | Mar 2026 |
| Modalidade importação | Conta e Ordem (Open Trade) | Estrutura operacional | Mar 2026 |
| Split Matriz/Filial | 10%/90% | Decisão Pedro 29/03 | Mar 2026 |
| B2B total | ~4% do faturamento | Documento fiscal v2.0 | Mar 2026 |
| Varejo (Simples) | ~96% do faturamento | Documento fiscal v2.0 | Mar 2026 |
| GB Comércio (do varejo) | ~50% | Benchmark operacional | Mar 2026 |
| Trades (do varejo) | ~30% | Benchmark operacional | Mar 2026 |
| Broglio (do varejo) | ~20% | Benchmark operacional | Mar 2026 |

---

## Parceiros Fiscais

| Parceiro | Função | Contato |
|----------|--------|---------|
| FOUR Contabilidade | Contador — valida todas as regras | Suellen |
| Open Trade (Itajaí) | Trading — desembaraço + benefício SC | — |
| Skiway (Yiwu) | Trading China — embarque até Shanghai | Neve / Rômulo |
| Rodonaves Amparo | Transportadora regional | — |

---

## Glossário Fiscal

| Termo | Significado |
|-------|-----------|
| **TTD 409** | Tratamento Tributário Diferenciado 409 de SC — reduz ICMS na importação |
| **DI** | Declaração de Importação — documento base de custo nacionalizado |
| **CFOP 6.152** | Código fiscal para transferência interestadual de mercadoria |
| **Simples Nacional** | Regime tributário simplificado para empresas até R$ 4,8M/ano |
| **Lucro Presumido** | Regime tributário para Matriz e Filial da GB |
| **NF-e** | Nota Fiscal Eletrônica |
| **SEFAZ** | Secretaria de Fazenda — autoriza NF-e |
| **B2B** | Venda para empresas (fica na Filial) |
| **B2C** | Venda ao consumidor final (via CNPJs Simples nos marketplaces) |

---

_Atualizado em: 2026-03-29. Revisar quando houver mudança na estrutura fiscal ou nova importação._

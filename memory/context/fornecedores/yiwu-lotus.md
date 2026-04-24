---
title: "Yiwu Lotus / Skiway — Fornecedor China"
created: 2026-04-23
type: reference
status: active
confidential: true
tags:
  - fornecedor
  - importacao
  - china
  - yiwu-lotus
  - skiway
---

# Yiwu Lotus / Skiway

> ⚠️ **CONFIDENCIAL** — contém dados bancários de TT. Não versionar em repositório público.
>
> Fonte de verdade: `~/Documents/03-Financeiro/FINANCEIRO SKIWAY/Dados_Financeiros_Skiway.pdf` (gerado 06/04/2026 18:24).

## Identidade

| Campo | Valor |
|-------|-------|
| **Razão Social** | YIWU LOTUS IMP. AND EXP. CO., LIMITED |
| **Nome Comercial / Apelidos** | Skiway, Skiway Group |
| **Endereço** | Room 205, Building 1, No. 31, Wuhua Road, Heyetang Industrial Zone, Futian Street, Yiwu City, Zhejiang Province |
| **CEP** | 322010 |
| **País** | China (República Popular) |
| **Manufacturer associado** | Zhejiang Zhongcai Stationery Manufacturing Co., Ltd (GB25007 mix canetas/panos) |

> **Nota:** no GB Import Hub o campo `supplier` está gravado como "Skiway", mas a entidade contratual (Sales Contract, Commercial Invoice) e a entidade bancária é **YIWU LOTUS IMP. AND EXP. CO., LIMITED**.

## Contatos

| Nome | Função | Email |
|------|--------|-------|
| **Neve Liu (刘柳华)** | Principal — contratos, PLs, coordenação | neve@skiwaygroup.com |
| Eike | Backup — sempre em cc | eike@skiwaygroup.com |
| Rômulo Macedo | Brasil-side (Skiway) | skwgved@gmail.com |

## Dados bancários TT — 3 beneficiários

### Beneficiário 1 — OFICIAL (Yiwu Lotus)

| Campo | Valor |
|-------|-------|
| Beneficiary | YIWU LOTUS IMP. AND EXP. CO., LIMITED |
| Bank | Bank of China — Yiwu Sub-Branch |
| Bank Address | No. 500, Chouzhou North Road, Yiwu, Zhejiang, China |
| SWIFT | BKCHCNBJ92H |
| Conta RMB | 4026 7703 3810 |
| Conta USD | 3701 7715 7087 |
| Conta EUR | 3935 7714 5442 |

### Beneficiário 2 — OFICIAL (Yiwu Acorn)

| Campo | Valor |
|-------|-------|
| Beneficiary | YIWU ACORN IMP. AND EXP. CO., LIMITED |
| Bank | Bank of China — Yiwu Sub-Branch |
| Bank Address | No. 500, Chouzhou North Road, Yiwu, Zhejiang, China |
| SWIFT | BKCHCNBJ92H |
| Conta RMB | 3649 7791 2491 |
| Conta USD | 3818 7804 5931 |
| Conta EUR | 4000 7805 4245 |

### Beneficiário 3 — NÃO OFICIAL (Tenthway)

| Campo | Valor |
|-------|-------|
| Beneficiary | TENTHWAY INTERNATIONAL TRADING LIMITED |
| Beneficiary Address | No. 31 Wuhua Road, Heyetang Industrial Zone, Yiwu, Zhejiang, China |
| Bank | Ping An Bank, H.O., Offshore Banking Department |
| Bank Address | 14/F, No. 5047, Road Shennan Dong, Shenzhen, P.R. China |
| SWIFT | SZDBCNBS |
| Conta (OSA) | OSA15000111688914 |

## Fluxo de pagamento

| Etapa | Quando | Destino |
|-------|--------|---------|
| **1. Sinal 30% FOB** | Fechamento do pedido, antes da fabricação | 100% Tenthway (não oficial) |
| 2. Fabricação + embarque | Trânsito marítimo 30–40 dias | — (sem pagamento) |
| **3. Impostos** | Chegada ao Brasil, antes da liberação | **Open Trade** (`07.104.810/0001-37`) |
| **4. Balanço 70% FOB** | Até 90 dias após B/L (~2 meses após chegada no BR) | Oficial + Não oficial — **proporção definida caso a caso** |

> **Crítico:** a proporção oficial/não oficial no balanço 70% **não é padrão** — confirmar com a Neve em cada pagamento.

## Plataformas TT

| Plataforma | Spread/Câmbio | Taxas | IOF |
|-----------|---------------|-------|-----|
| Remessa Online | 1,3% sobre comercial | Sem tarifa ≥ R$ 2.500 | 0,38% |
| Wise | Comercial puro | ~0,5–0,7% | 1,1% |

Sempre simular nas duas antes de fechar.

## Cupons Remessa Online (validade 03/2026)

| Cupom | Desconto | Notas |
|-------|----------|-------|
| `ESCOLADELOJISTA50` | 50% OFF taxas | Uso único |
| `CUPONOMIA25` | 25% OFF spread | PF e PJ |
| `ESCOLADELOJISTA` | 15% OFF taxas | Todas |
| `MELIUZ10` | 10% OFF extra | Via Meliuz |

## Containers pagos a este beneficiário

Fonte: GB Import Hub (`supplier=Skiway`). Todos Yiwu Lotus exceto onde marcado.

| Container | Status | Sinal 30% | Numerário | Balanço 70% | Nota |
|-----------|--------|-----------|-----------|-------------|------|
| GB25007 | finished | ✅ R$ 74.278 | ✅ R$ 148.556 | ✅ R$ 173.316 | Mix heterogêneo antigo |
| GB25008 | finished | ✅ R$ 37.102 | ✅ R$ 60.338 | ✅ R$ 113.820 | Dedicado a kits |
| GB25009 | finished | ✅ R$ 26.374 | ✅ R$ 65.293 | 🔴 R$ 72.232 vencido 16/04 | Via Yiwu Lotus (via alternativa) |
| GB25010 | customs | ✅ R$ 38.151 | 🔴 R$ 64.136 vencido 20/04 | ⏳ R$ 81.750 (10/05) | Baseline mix futuro |
| GB25011 | road | ✅ R$ 31.330 | ✅ R$ 60.000 | ⏳ R$ 71.419 (24/05) | Baseline mix futuro |
| GB26001 | production | ✅ R$ 33.720 | ⏳ R$ 61.817 | ⏳ R$ 72.120 | — |
| GB26002 | production | ✅ R$ 33.720 | — | — | — |

## Sugestão de item 1Password (criar manual)

- **Vault:** OpenClaw (ou vault pessoal se preferir fora do service account)
- **Tipo:** Bank Account (3 itens separados — um por beneficiário)
- **Nomes:**
  - `Yiwu Lotus — Wire TT (Bank of China, USD)`
  - `Yiwu Acorn — Wire TT (Bank of China, USD)`
  - `Tenthway — Wire TT (Ping An Bank, não oficial)`
- **Tags:** `china`, `fornecedor`, `importacao`, `yiwu-lotus`, `skiway`

## Referências cruzadas

- [[projects/gb-import-hub]] — sistema que registra `supplier=Skiway`
- [[projects/planejamento-importacao-2026]] — plano de cadência dos lotes
- [[business/importacao/_index]] — índice importação
- [[business/importacao/estrategia-fiscal-gb]] — estratégia fiscal 90/10
- [[openclaw/agents/kobe/USER]] — contatos Neve e Rômulo

*Criado: 23/04/2026 a partir de `~/Documents/03-Financeiro/FINANCEIRO SKIWAY/Dados_Financeiros_Skiway.pdf` (06/04/2026)*

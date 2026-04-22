---
title: "Planejamento Importação 2026"
created: 2026-04-20
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/planejamento-importacao-2026/"
tags:
  - project
  - estrategia
  - importacao
  - essencialismo
---

# Planejamento Importação 2026 — GB Importadora

**Path:** `~/Documents/05-Projetos-Codigo/planejamento-importacao-2026/`
**Stack:** Markdown + Python venv (parsing PNI/packing lists) + Supabase Import Hub
**Método:** Essencialismo (Greg McKeown)
**CLAUDE.md:** sim (8 decisões validadas)

## O que é

Projeto estratégico para **dimensionar a cadência ótima de importação** sob a tese do flywheel: estoque contínuo nos marketplaces (ML + Amazon + Shopee) prioriza o vendedor nos algoritmos, acelerando vendas de forma não-linear. Objetivo é decidir se deve migrar de fluxo contínuo (1 container por vez conforme caixa) para lotes de 4 containers idênticos (4× GB25011), e se sim, em que cadência nos próximos 6 meses.

**Disciplina essencialista:** 4 arquivos no total (3 de 1 página), modelar só o que muda decisão, trade-offs explícitos, preferir cortar a adicionar.

## Pipeline (4 fases)

| Fase | Output | Status |
|------|--------|--------|
| 1 — Diagnóstico do Presente | `01-estado-atual.md` | ✅ Concluída 20/04 |
| 2.1 — Parsing PNIs | `data/pnis-extraidos.csv` | ✅ Concluída 20/04 (86 rubricas, totais validados) |
| 2.2 — Custo do lote de 4 | `02-custo-lote.md` + `data/rubricas-classificadas.csv` | ✅ FECHADA 20/04 (modelo corrigido + câmbio conservador +7%) |
| 2.3.1 — Mapa container→SKU | `data/container-sku-map.csv` | ✅ FECHADA 21/04 (76 linhas, 46 SKUs únicos, 5 PLs parseadas) |
| 2.3.2 — ML vendas | `data/vendas-ml.csv` + `data/mini-analise-flywheel-imb501.md` | ✅ 21/04 (19 SKUs, 717 linhas, 7 meses, flywheel IMB501 VALIDADO) |
| 2.3.2 — Amazon SP-API | `data/vendas-amazon.csv` + `data/amazon-sku-mapping-discovery.csv` | ✅ 22/04 (6 SKUs alvo, 120 un — Amazon portfólio diferente do ML) |
| 2.3.2 — Shopee OpenAPI | `data/vendas-shopee.csv` | 🔴 BLOQUEADO — 3 contas localizadas na VPS, aguarda autorização Pedro |
| 2.3.3 — Análise consolidada 3 canais | a definir | ⏳ Aguarda Shopee |
| 3 — Modelagem do Flywheel (8 meses, simulação) | `03-flywheel.xlsx` + `03-interpretacao.md` | ⏳ Aguarda Fase 2 |
| 4 — Decisão | `04-plano.md` (1 página) | ⏳ Aguarda Fase 3 |

## Decisões-chave (validadas 20/04)

1. **Base empírica n=5** — GB25007–25011. GB25010/11 pesam mais (refletem mercado atual); 07/08/09 são baseline histórico.
2. **Cruzamento container→SKU via packing lists** do Supabase `documents` (xlsx/xls — parsing openpyxl/pandas).
3. **Lote de 4 = GB25011 × 4** com ajustes de escala identificados na Fase 2A.
4. **Data de nacionalização = proxy** `finance_pagamentos.numerario_paid_date`.
5. **Horizonte simulação 8 meses** (20/04/2026 → 20/12/2026). Janela de pedidos = 6 meses; simulação cobre venda completa do último lote.
6. **Consolidação de canais:** 1 ML + 1 Amazon + 3 Shopee = 5 canais, somar tudo em 1 número por SKU. Flagar outlier >60% sem mudar metodologia.
7. **Cenário B confirmado** — máx 1 DI/DUIMP por container; PNIs cobrem 100% da nacionalização. Divergência FOB PNI (USD 7.939 GB25011) vs banco (USD 22.525) é split contábil, não múltiplas DIs.
8. **Câmbio baseline R$ 5,0899** (GB25011, fixo para projeção do lote).

## Descobertas empíricas vs premissas iniciais

- **Ordem real de pagamento:** sinal 30% → **numerário** → balanço 70% (não o inverso como estava no CLAUDE.md original do projeto).
- **Ciclo real:** registro → nacionalização ≈ **D+69** (não D+100 como o modelo assumia). GB25011: registro 01/02 → numerário pago 11/04.
- **Transporte rodoviário:** até GB25008 vinha em PNI complementar; de GB25010 em diante já incluso no PNI principal.
- **finance_numerario_itens vazio** para GB25011 — sem decomposição do numerário no banco.

## Fontes de dados

- **GB Import Hub** (Supabase `ocxvwwaaqqxecmzhfxhb`) — containers, pagamentos, documents, milestones
- **6 PNIs em PDF** (Open Trade) — baixados via script Gmail API (`scripts/download-pnis.py`, OAuth reusado do google-sheets-claude)
- **APIs marketplace** — credenciais em 1Password vault OpenClaw (ML, Amazon SP-API, Shopee, Bling ERP)

## Arquivos do projeto

- `CLAUDE.md` — 8 decisões validadas + princípios essencialistas
- `.claude/settings.json` — permissions restritivas (sem rm -rf, sudo, curl delete)
- `01-estado-atual.md` — extração Fase 1 (7 containers, calendário desembolsos, ficha GB25011)
- `data/pnis/` — 6 PNI PDFs padronizados
- `scripts/download-pnis.py` — reutilizável para GB26001/02 quando PNIs saírem
- `scripts/.venv/` — Python venv isolado (google-api-python-client, pdfplumber quando 2A rodar)

## Números canônicos (Fase 2.2 FECHADA, 20/04 final da noite)

### Cenário conservador (câmbio R$ 5,4462 = baseline + 7%)
- **Custo 1 container:** R$ 183.872,57 = FOB R$ 122.675,66 + PNI R$ 61.196,92
- **Custo lote de 4 (escala linear):** **R$ 735.490,28**
- **Timeline lote:** D+0 sinal R$ 147.210,78 | D+85 PNI R$ 244.787,68 | D+100 balanço R$ 343.491,82

### Cenário realista (referência — câmbio R$ 5,0899)
- **Custo 1 container:** R$ 175.846,92
- **Custo lote de 4:** R$ 703.387,68
- **Buffer cambial (conservador − realista):** R$ 32.102,60 (+4,6%)

### Premissa cambial (decisão 20/04 final da noite)
Usar câmbio **+7% acima do baseline** (R$ 5,4462) para todo FOB do projeto. Racional: FOB pago em 2 momentos (D+0 e D+50) com câmbios distintos; variação ±7-8% em ciclo 100d é ruído natural; buffer cria assimetria favorável. PNI é BRL puro (sem variação). Ver [[memory/context/decisoes/2026-04#[20/04 final da noite] Importação 2026 — câmbio de planejamento conservador (+7%)|decisão cambial]].

### Gap timeline vs custo canônico (resolvido)
6,8% de diferença entre custo canônico e timeline dos containers reais é **ruído cambial natural** dentro da tolerância ±7-8% — absorvido pelo buffer do planejamento conservador. Não é erro de dados.

## Regra canônica de custo (decisão 20/04 noite)

```
Custo 1 container = FOB (banco) + PNI total
```

FOB e PNI são universos separados — somam-se, nunca se escalam. O "FOB USD" no header do PDF do PNI é referência declarativa do aduaneiro usado pela Open Trade na DI, não indica que o PNI é parcial. Ver [[memory/context/decisoes/2026-04#[20/04 noite] Importação 2026 — modelo canônico de custo de container|decisão completa]].

## Descobertas empíricas da Fase 2.3 (21/04)

### MLB mestre IMB501: MLB3288536143
- Criado 2023-04-14, active, 4 variações de cor (Preto/Sortido/Rosa/Vermelho)
- sold_quantity histórico: 4.473 unidades
- `seller_sku` vazio nas variações (razão da busca inicial não achar)
- Mapping decidido: Preto=IMB501P | Vermelho=IMB501V | Sortido=IMB501C | Rosa=IMB501R

### Ciclo observado abr/25 → abr/26 (só ML)
- Aquecimento (4 meses): 365 un
- **Pico ago/25: 687 un (22,2 un/dia)**
- **Ruptura out/25-fev/26: ZERO em 5 meses** (custo ~3.330 un perdidas, ~R$ 99k)
- Recuperação mar-abr/26: 60 → 686 un (projetado ~980 un até 30/04, supera pico)
- **Tempo de recuperação = 2× mais rápido que aquecimento inicial**

### 6 MLBs IMB501 novos criados 17/03/26
- 3 principais (R$ 24,90, IMB501C/V/P_T): ativos, responsáveis por 56% das vendas abr/26
- 3 secundários (R$ 29,88, KITIMB501*_T): zombies, 0 vendas em 35 dias — candidatos para higiene

## Descobertas adicionais (22/04)

### Amazon: portfólio complementar, não substituível ao ML
- 21 SKUs alvo na Amazon: 120 un / R$ 3.676 em 7 meses (3% do volume ML)
- 108 outros SKUs Amazon vendem **R$ 137.274** no mesmo período
- Top Amazon: CK4742_BB (Jarra, 1.433 un), 914C_BB (Canequinhas), Pano Microfibra, Tapete, Suporte Gamer
- **Anomalia crítica**: IMB501P Amazon tem listing (B0DCP9TBTM) mas 0 vendas em 7 meses (ML: 491 un)
- 7 SKUs alvo com listing mas 0 vendas; 8 sem listing sequer

### Algoritmo Amazon menos tolerante a ruptura que ML
- IMB501V Amazon rompeu dez/25 e **não recuperou em 5 meses**
- IMB501V ML rompeu out/25 e **recuperou em 2 meses**
- Ranking Amazon exige reativação manual (Ads + FBA + BuyBox)
- Implicação: estoque contínuo é ainda mais crítico na Amazon

### Shopee localizada na VPS (não no 1P)
- 3 contas ativas com auto-refresh rodando há 12 dias
- Partner ID produção **2031533** (o 1228462 do 1P é test-mode)
- shop_ids: 448649947 (store default), 860803675 (store2 Oficial), 442066454 (shop)
- IP whitelist Shopee obriga coleta NA VPS

## Handoff file disponível

`data/HANDOFF-IA-PARALELA.md` (14 KB, 13 seções) — state completo para continuidade por outra instância Claude Code sem retrabalho.

## Em aberto

### Bloqueio imediato
- 🔴 **Shopee 2.3.2**: Pedro autorizar diretório na VPS (A-tmp vs A-workspace) para executar coleta

### Pendências técnicas
- 🟡 **Anomalia IMB501P Amazon**: investigar BuyBox/FBA stock/listing quality manualmente no Seller Central
- 🟡 **8 kits alvo sem listing Amazon**: cadastrar ou aceitar lacuna
- 🟡 **7 kits com listing mas 0 vendas Amazon**: diagnosticar
- 🟡 2 kits sem MLB no ML (KIT2YW800SQ, KIT9S098): criar ou descontinuar
- 🟡 3 MLBs novos zombies ML (R$ 29,88 sufixo _T): desligar?
- 🟡 Gap operacional: pré-configurar listings ANTES da chegada do container (GB25009 ficou 3 semanas sem anúncio ativo ML)

### Próximas fases
- ⏭️ **2.3.3** — análise consolidada ML + Amazon + Shopee após Shopee concluído
- ⏭️ **Fase 3** — simulação flywheel 8 meses → `03-flywheel.xlsx` + `03-interpretacao.md`
- ⏭️ **Fase 4** — plano de decisão 1 página → `04-plano.md`

### Pendências externas
- 🟡 Pergunta Open Trade (Sérgio): desconto em lote de 4 processos simultâneos?
- 🟡 DI/DUIMP do GB25011 não anexada em `documents` — útil para auditoria futura
- 🟡 GB25010 numerário R$64.136,40 — pagamento pendente de confirmação

## Ver também

- [[projects/gb-import-hub]] — sistema de gestão de importações (fonte de dados primária)
- [[business/importacao/estrategia-fiscal-gb]] — TTD 409, 90/10, margem interna
- [[memory/context/deadlines]] — GB25010/GB25011 balanço

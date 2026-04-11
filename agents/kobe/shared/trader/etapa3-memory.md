# MEMORY.md — Trader

_Último update: 2026-03-23_

---

## Índice de arquivos

- [[agents/kobe/shared/trader/SOUL|SOUL]]
- [[agents/kobe/shared/trader/memory/context/decisions|Decisões]]
- [[agents/kobe/shared/trader/memory/pending|Pendências]]

### Sessões
- [[agents/kobe/shared/trader/memory/sessions/2026-03-24|Sessão 2026-03-24]]
- [[agents/kobe/shared/trader/memory/sessions/2026-03-26|Sessão 2026-03-26]]
- [[agents/kobe/shared/trader/memory/sessions/2026-03-27|Sessão 2026-03-27]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-05|Sessão 2026-04-05]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-06|Sessão 2026-04-06]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-07|Sessão 2026-04-07]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-08|Sessão 2026-04-08]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-09|Sessão 2026-04-09]]

---

## Quem sou

Especialista sênior de marketplaces da GB Importadora. Opero ML, Amazon BR e Shopee. Coordenado pelo Kobe. Nível L1 (Observer) — todo output revisado.

## Estrutura de memória

```
memory/
├── context/
│   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   ├── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
│   ├── marketplace-algorithms.md ← Algoritmos ML/Amazon/Shopee (46KB)
│   └── platforms.md       ← Status e contexto de cada plataforma
├── sessions/              ← Notas diárias (YYYY-MM-DD.md)
├── projects/              ← Contexto de projetos
└── feedback/
    └── reviews.json       ← Reviews de performance do Kobe
pending.md                 ← Tarefas pendentes
```

## Regras de memória

- **Decisão do Pedro ou Kobe?** → `memory/context/decisions.md`
- **Lição aprendida?** → `memory/context/lessons.md` (tag [ESTRATÉGICA] permanente, [TÁTICA] expira 30 dias)
- **Se importa, escreve.** O que não tá escrito, não existe.
- **Antes de compactar sessão:** extrair lições → decisões → pendências → SÓ DEPOIS compactar

## Integrações

| Plataforma | API | Status | Tokens/Config |
|---|---|---|---|
| **Mercado Livre** | REST API (3 apps: Vendas, Financeiro, Métricas) | ✅ Ativa | `/root/.openclaw/.ml-tokens*.json` |
| **Amazon BR** | SP-API (marketplace A2Q3Y263D00KWC) | ✅ Ativa | 1Password vault "OpenClaw" |
| **Amazon Ads** | Advertising API (endpoint NA) | ✅ Ativa | Via Supabase Bidspark |
| **Shopee** | Open Platform (3 contas) | ✅ Ativa | Tokens por conta em `/root/.openclaw/` |
| **Bright Data** | Web Unlocker (zone web_unlocker1) | ✅ Ativa | 1Password vault "OpenClaw" |

### Shopee — 3 Contas

| Conta | Shop ID | Token |
|---|---|---|
| budamix-store | 448649947 | `.shopee-tokens-budamix-store.json` |
| budamix-store2 | 860803675 | `.shopee-tokens-budamix-store2.json` |
| budamix-shop | 442066454 | `.shopee-tokens-budamix-shop.json` |

Credenciais Shopee: `/root/.openclaw/workspace/integrations/shopee/.env`
Mapa de contas: `/root/.openclaw/workspace/integrations/shopee/accounts.json`

## Skills Disponíveis

### Extratos Financeiros
| Skill | Path | Uso |
|---|---|---|
| ml-extrato | `skills/marketplace/ml-extrato/` | Extrato financeiro ML (Excel) |
| shopee-extrato | `skills/marketplace/shopee-extrato/` | Extrato Shopee multi-conta (Excel) |
| amazon-extrato | `skills/marketplace/amazon-extrato/` | Extrato Amazon SP-API (Excel) |
| consolidado-financeiro | `skills/marketplace/consolidado-financeiro/` | Consolidado 3 plataformas (HTML + Excel) |

### Análise & Relatórios
| Skill | Path | Uso |
|---|---|---|
| marketplace-report | `skills/marketplace/marketplace-report/` | Relatório performance multi-plataforma |
| ml-competitor-analysis | `skills/marketplace/ml-competitor-analysis/` | Análise concorrência ML (Bright Data) |
| ml-ads | `skills/marketplace/ml-ads/` | Advertising API ML |

### Taxas & Regras
| Skill | Path | Uso |
|---|---|---|
| ml-fees-rules | `skills/marketplace/ml-fees-rules/` | Taxas e comissões ML |
| shopee-fees-rules | `skills/marketplace/shopee-fees-rules/` | Taxas e comissões Shopee |

### Inventário
| Skill | Path | Uso |
|---|---|---|
| inventory-management | `skills/marketplace/inventory-management/` | Gestão estoque, composição kits |

### Design
| Skill | Path | Uso |
|---|---|---|
| report-design-system | `skills/design/report-design-system/` | Design system HTML dark mode |
| excel-design-system | `skills/design/excel-design-system.md` | Paleta dark mode Excel |

Template HTML base: `templates/report-base.html`

## Conhecimento Core

- **Algoritmos de Marketplace** — `memory/context/marketplace-algorithms.md` (46KB)
  - ML: 12 fatores de ranking, penalizações, estratégias
  - Shopee: 4 pilares, sistema de penalidade, otimização
  - Amazon: A10, Buy Box, BSR, keywords
  - Análise cruzada GB: potes herméticos, kits, precificação cruzada

## QA Financeiro — Regras INVIOLÁVEIS (Decisão Pedro 2026-04-03)

1. **Validação de período obrigatória.** Primeiro pedido >= dia 1, último >= dia 28+. Incompleto → "DADOS INCOMPLETOS" e para.
2. **Nunca reutilizar extratos antigos** sem validar período. Fechamento mensal = extração nova.
3. **Carimbo obrigatório:** data/hora extração, período real (primeiro/último pedido), totais por status.
4. **Sanity check antes de entregar:** vendas vs meses anteriores, período completo, dados frescos, totais batendo.
5. Aplica-se a todo extrato/relatório financeiro. Permanente.

## Hierarquia

- **Pedro** — dono, decisor final
- **Kobe** — coordenador direto, decisões dele = decisões do Pedro
- **Trader** — executa, analisa, reporta ao Kobe
- Shared: ler/escrever em `/root/.openclaw/workspace/shared/` (outputs, lessons)

## Nível: L1 (Observer)

Todo output revisado pelo Kobe. Promoção: 5 entregas aprovadas consecutivas sem correções significativas.

---
title: "MEMORY"
created: 2026-04-26
type: memory
agent: trader
status: active
tags:
  - agent/trader
  - agent/trader
---
# MEMORY.md — Trader

_Último update: 2026-04-23 23:30 BRT (Consolidação Diária)._

---

## Índice de arquivos

- [[agents/kobe/shared/trader/SOUL|SOUL]]
- [[agents/kobe/shared/trader/memory/context/decisions|Decisões]]
- [[agents/kobe/shared/trader/memory/context/lessons|Lições]]
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
- [[agents/kobe/shared/trader/memory/sessions/2026-04-10|Sessão 2026-04-10]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-11|Sessão 2026-04-11]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-12|Sessão 2026-04-12]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-13|Sessão 2026-04-13]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-14|Sessão 2026-04-14]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-15|Sessão 2026-04-15]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-16|Sessão 2026-04-16]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-17|Sessão 2026-04-17]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-18|Sessão 2026-04-18]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-19|Sessão 2026-04-19]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-20|Sessão 2026-04-20]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-22|Sessão 2026-04-22]]
- [[agents/kobe/shared/trader/memory/sessions/2026-04-23|Sessão 2026-04-23]]

---

## Quem sou

Especialista sênior de marketplaces da GB Importadora. Opero ML, Amazon BR e Shopee. Coordenado pelo Kobe. Nível operacional com revisão do Kobe quando necessário.

## Estrutura de memória

```
memory/
├── context/
│   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   └── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
├── sessions/              ← Notas diárias (YYYY-MM-DD.md)
└── pending.md             ← Tarefas pendentes
```

## Regras de memória

- **Decisão do Pedro ou Kobe?** → `memory/context/decisions.md`
- **Lição aprendida?** → `memory/context/lessons.md` (tag [ESTRATÉGICA] permanente, [TÁTICA] expira 30 dias)
- **Se importa, escreve.** O que não tá escrito, não existe.
- **Antes de compactar sessão:** extrair lições → decisões → pendências → SÓ DEPOIS compactar
- **QA financeiro é inviolável.** Extrato parcial nunca entra como fechamento completo.

## Integrações

| Plataforma | API | Status | Tokens/Config |
|---|---|---|---|
| **Mercado Livre** | REST API (3 apps: Vendas, Financeiro, Métricas) | ✅ Ativa | `/root/.openclaw/.ml-tokens*.json` |
| **Amazon BR** | SP-API (marketplace A2Q3Y263D00KWC) | ✅ Ativa | 1Password vault "OpenClaw" |
| **Amazon Ads** | Advertising API (endpoint NA) | ✅ Ativa | Via Supabase Bidspark |
| **Shopee** | Open Platform (3 contas) | ✅ Ativa | Tokens por conta em `/root/.openclaw/` |
| **Bright Data** | Web Unlocker | ✅/⚠️ Uso pontual | 1Password vault "OpenClaw" |

## Conhecimento operacional vigente

- **QA Financeiro, 5 regras invioláveis** já incorporado em `decisions.md` e `lessons.md`.
- **Request Review Amazon** usa Supabase como fonte de pedidos e `productReviewAndSellerFeedback` como endpoint correto.
- **PCM001** consolidou 3 regras práticas de cadastro/preço cross-channel: `gold_special` no ML perto de R$39,90, cuidado com degrau de R$80 na Shopee e `DRINK_COASTER` com GTIN exemption validado na Amazon BR.
- **Fechamento de março** continua aberto por falta de ads spend e consolidado final sob as novas regras de QA.
- **Base Ana** segue com prioridade em cobertura Amazon, ML e Shopee avançaram, mas a parte Amazon continua incompleta.

## Estado real desta consolidação

### O que mudou nos últimos 15 dias
- 07/04 trouxe regras operacionais novas para cadastro e pricing do PCM001.
- 10/04 consolidou o fluxo correto do Amazon Request Review dentro do domínio Trader.
- 11/04 a 23/04 foram dias majoritariamente silenciosos, sem nova execução própria do Trader.

### O que NÃO mudou
- Não houve novo extrato financeiro completo.
- Não houve nova análise profunda de concorrência.
- Não houve nova entrega operacional autônoma além da consolidação do fluxo Request Review.

## Pendências prioritárias

- Fechar março com ads spend e novo consolidado.
- Cruzar margem por produto com custo real da planilha.
- Montar fluxo de caixa por liquidação real por plataforma.
- Fechar links Amazon da base Ana.

## Hierarquia

- **Pedro** — dono, decisor final
- **Kobe** — coordenador direto, decisões dele = decisões do Pedro
- **Trader** — executa, analisa, reporta ao Kobe

---

_Consolidação Diária 2026-04-23: MEMORY revalidado sem inflar atividade inexistente._
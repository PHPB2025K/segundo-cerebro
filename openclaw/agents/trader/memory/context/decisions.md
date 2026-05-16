---
title: "decisions"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Decisões — [[openclaw/agents/trader/IDENTITY|Trader]]

### Margem SEMPRE ponderada por volume e plataforma
- Nunca média simples. Consolidada real: 13,7%.

### Curva ABC é global (todas plataformas), não por plataforma
- Quando filtra por plataforma, mantém classificação global.

### Formato: HTML (leitura) + Excel (source of truth)
- Sempre enviar ambos juntos.

### Largura HTML relatórios: 1280px container, font 0.76rem tabelas

### Mapeamento CNPJ × Marketplace (DEFINITIVO)
| CNPJ | Empresa | Marketplaces |
|------|---------|-------------|
| 07.194.128/0001-82 | GB Comércio | ML + Amazon + Shopee 448649947 |
| 45.200.547/0001-79 | Trades | Shopee 860803675 |
| 63.922.116/0001-06 | Broglio | Shopee 442066454 |

### QA Financeiro — 5 Regras INVIOLÁVEIS (2026-04-03)
1. Validação de período obrigatória (primeiro pedido >= dia 1, último >= dia 28+; se incompleto → PARA)
2. Nunca reutilizar extratos antigos sem validar período
3. Carimbo obrigatório em todo extrato (data/hora extração, período real, totais por status)
4. Sanity check antes de entregar (vendas vs histórico, período completo, dados frescos, totais batendo)
5. Aplica-se a Kobe + Trader — todo relatório financeiro, permanente

### Amazon pending = venda real no Live Sales (2026-03-27)
- Pedidos Amazon FBA com status "pending" e total_amount > 0 contam no faturamento
- ML e Shopee excluem pending

## Budamix Central — Planilha oficial de precificação (2026-04-30)
- Fonte oficial de custo/anúncios: `1u74a...` (PLANILHA DE ESTOQUE / PRECIFICAÇÃO).
- `1dUoZ...` é legado/operacional; não usar para custo real de anúncio.
- Sync de custos resolve em ordem: custo direto na aba marketplace col F → ESTOQUE direto → mapping por SKU base/ID/anúncio/variações `_T`.

### Fechamento financeiro: faturamento comercial ≠ settlement (2026-05-01)
- Nunca chamar `SETTLEMENT`/extrato financeiro de faturamento bruto sem qualificador.
- Relatórios mensais devem separar faturamento bruto comercial/pedidos válidos e receita liquidada em extrato.

### DRE profissional obrigatória (2026-05-01)
- DRE da GB deve seguir estrutura clássica completa, não apuração simplificada de marketplace.
- Se dados contábeis faltarem, manter a linha e marcar lacuna.

## Regra Universal — Horários em Brasília (2026-04-01)
TODOS os horários apresentados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de exibir. Vale para relatórios, alertas, logs, timestamps — qualquer comunicação.

---

_Atualizado na Consolidação Profunda 2026-05-01._
### Daily Sales Report — rotina diária (2026-05-08)
- Rodar diariamente às **06:30 BRT** com entrega no Telegram Kobe Hub, tópico Marketplaces.
- Consolidar vendas/pedidos do dia anterior completo em BRT para Mercado Livre, Shopee 3 contas, Amazon BR e Bling Matriz como **Atacado - GB Matriz**.
- Não misturar settlement, extrato financeiro ou DRE com venda gerada; se fonte falhar, gerar parcial e marcar indisponibilidade sem estimar.

## 2026-05-11 — Daily Sales Report para equipe administrativa

- Daily Sales Report para Yasmin/Lucas/Leonardo deve usar Slack DM diário às 06:50 BRT, fonte canônica `v_daily_sales` + Bling Matriz, formato aprovado por Pedro e Top Produtos consolidado por SKU equivalente cross-plataforma.
- Não usar WhatsApp para esse relatório e não incluir seção `DESTAQUES DO DIA`.


### Daily Sales Report v2 — LLM como caminho principal (2026-05-15)
- Pedro aprovou tecnicamente o uso de LLM como caminho principal para os três reports individuais: Lucas/Shopee, Yasmin/Mercado Livre e Leonardo/Amazon.
- Slack Writer LLM + QA Gate LLM passam a ser o caminho aprovado; fallback determinístico não pode mascarar falha de camada LLM.
- Envio real continua bloqueado até autorização explícita de Pedro/Kobe; se camada LLM falhar, o recipient fica bloqueado em vez de seguir por fallback.

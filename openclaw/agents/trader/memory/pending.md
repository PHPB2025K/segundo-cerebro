# Pendências — Trader

_Atualizado: 2026-05-17_

## 🔴 Prioridade Alta

### Daily Sales Report
- [ ] Daily Sales Report v2: validar pós-promoção técnica LLM dos três recipients (Lucas/Shopee, Yasmin/ML, Leonardo/Amazon); preview de 16/05/2026 BRT ficou com Yasmin/ML e Leonardo/Amazon aprovados, Lucas/Shopee aprovado com ressalva numérica menor, e envio real segue bloqueado até autorização explícita de Pedro/Kobe.
- [ ] Monitorar primeira execução real/autorizada do wrapper v2 e garantir que análise por conta use memória diária/semanal/mensal, nome comercial e sem SKU cru; se LLM falhar, bloquear recipient em vez de fallback.
- [ ] Validar no próximo ciclo se os ajustes de prompt eliminam as ressalvas numéricas da camada Shopee Consolidator: percentuais com 1 casa decimal e valores monetários/tickets com centavos quando citados em texto analítico.
- [ ] Tornar obrigatório no log da Slack Writer o registro formal de todos os itens “não pode ir para Slack”, inclusive regras gerais e restrições de inferência.
- [ ] Revisar mapeamento/nome comercial Amazon quando o display name adiciona atributo não verificável pelo título real do pedido.
- [ ] Monitorar Shopee nas 3 contas por queda transversal vs média 30d, concentração dos top produtos e possível canibalização interna entre lojas.
- [ ] Revisar Shopee Rules Watch, vencido desde 06/05/2026, antes de usar regra/taxa como hipótese causal forte no Daily Sales.
- [ ] Registrar/obter definição dos produtos prioritários Shopee de maio por Lucas; sem isso, recomendações de ADS/mix ficam parcialmente condicionadas.
- [ ] Monitorar Mercado Livre após pico de 16/05/2026 BRT: se ritmo não se repetir até 12h BRT, tratar como pico pontual concentrado nos líderes, não novo normal.
- [ ] Monitorar Amazon por Buy Box, cobertura FBA e estabilidade dos ASINs líderes antes de recomendar escala de campanha.

### Relatório mensal
- [ ] **Relatório mensal abril — reexecutar job direto do Trader**: validar geração dos 3 artefatos finais, corrigir caminho Shopee e avisar conclusão/falha no tópico Marketplaces do Telegram.


### Fechamento Março — Gaps
- [ ] Ads spend março por plataforma (ML, Amazon, Shopee manual) para validar consolidado.
- [ ] Refazer consolidado financeiro de março com extratos completos e ads spend real.
- [ ] DRE semanal março (01-07, 08-14, 15-21, 22-31).
- [ ] Margem por produto — cruzar curva ABC com preço de custo da planilha oficial.

### Budamix Central Full — Estoque / Validação
- [ ] Validar ML Full e Amazon FBA com profundidade equivalente à validação Shopee 1D.
- [ ] Acompanhar monitoramento Shopee 1E quando implementado.
- [ ] Monitorar se fantasmas Amazon FBA com `unit_price=0` voltam a aparecer.

### Relatório de Performance — Connectors Faltantes
- [ ] Connector Amazon completo (SP-API: orders, items, seller metrics).
- [ ] Connector Shopee 3 contas (orders, items, shop metrics).
- [ ] HTML no mesmo design system do financeiro.

## 🟡 Prioridade Média

### Shopee
- [ ] Estratégia de pricing Shopee (margens menores que ML).
- [ ] Monitorar efeitos das regras de taxas abril/2026.

### Base Ana — Links de Marketplace
- [ ] Amazon segue prioridade #1 na base Ana; ML/Shopee manuais ficam para quando o tema voltar.

## 🟢 Backlog
- [ ] Análise concorrência ML expandida para 5+ termos.
- [ ] Tendência mês a mês no consolidado a partir de abril.

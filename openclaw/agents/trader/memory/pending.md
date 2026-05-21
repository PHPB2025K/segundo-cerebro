# Pendências — Trader

_Atualizado: 2026-05-20_

## 🔴 Prioridade Alta

### Daily Sales Report
- [ ] Corrigir e reexecutar Lucas/Shopee para 19/05/2026 BRT: remover duplicidade CTL002 no Top Produtos, posicionar a linha consolidada de 10 pedidos na 3ª posição, formatar breakdown com separadores claros e validar que o QA deixa de ser BLOCKED antes de qualquer envio.
- [ ] Ajustar Slack Writer/06B de Shopee para que linha consolidada cross-conta substitua integralmente linhas componentes já contidas no total; aplicar também ao KIT2YW800SQ e registrar decisões de formatação coerentes.
- [ ] Monitorar simplificações da Slack Writer Shopee frente à 6B: manter linguagem mais simples sem remover evidências operacionais essenciais; se o padrão persistir, ajustar prompt antes de envio real.
- [ ] Ajustar Slack Writer de Mercado Livre para preservar âncoras de framing Padrão B (“parece saudável, mas...”) e registrar formalmente qualquer simplificação relevante.
- [ ] Corrigir logs de Amazon: item exibido no ranking não pode aparecer como “omitido”; recalcular ranking/posições após exclusões antes de gerar decisões de formatação.
- [ ] Monitorar primeira execução real/autorizada do wrapper v2 e garantir que análise por conta use memória diária/semanal/mensal, nome comercial e sem SKU cru; se LLM falhar, bloquear recipient em vez de fallback.
- [ ] Tornar obrigatório no log da Slack Writer o registro formal de todos os itens “não pode ir para Slack”, inclusive regras gerais, restrições de inferência e toda omissão de Top Produtos por nome, mesmo item de 1 pedido com confiança alta.
- [ ] Corrigir mapeamentos/nome comercial que contaminam Daily Sales: Amazon TL250B/TL6250 não podem aparecer como tigelas de vidro; Shopee SKU 098 deve usar raw_title/descrição correta; ML 914C_BAV não deve receber rótulo inventado.
- [ ] Incluir/validar no pacote Daily Sales: Shopee Full real por conta, Buy Box e cobertura FBA por ASIN na Amazon, atribuição de cancelamentos por produto quando disponível.
- [ ] Monitorar Shopee nas 3 contas por queda transversal vs média 30d, concentração dos top produtos e possível canibalização interna entre lojas; se GMV Shopee ficar abaixo de R$ 4.500 por mais um ciclo corrigido, contar como segundo dia para possível intervenção Lucas + Himmel.
- [ ] Revisar Shopee Rules Watch, vencido desde 06/05/2026, e Amazon Rules Watch, previsto para 20/05/2026, antes de usar taxa/regra como hipótese causal forte no Daily Sales.
- [ ] Registrar/obter definição dos produtos prioritários Shopee de maio por Lucas; sem isso, recomendações de ADS/mix ficam parcialmente condicionadas.
- [ ] Monitorar Mercado Livre entre 20/05 e 26/05 pelos efeitos das otimizações Himmel de 19/05: CB1 com verba maior, MDF com ROAS alvo mais aberto e anúncios movidos para Balance.
- [ ] Monitorar Amazon por Buy Box, cobertura FBA, cancelamentos por ASIN e estabilidade dos ASINs líderes antes de recomendar escala de campanha.

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

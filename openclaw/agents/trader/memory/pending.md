# Pendências — Trader

_Atualizado: 2026-05-26_

## 🔴 Prioridade Alta

### Daily Sales Report
- [ ] Validar se os ciclos Daily Sales v2 de 24/05 e 25/05/2026 BRT terem gerado preview apenas para Yasmin/Mercado Livre foram intencionais ou lacuna; se lacuna, reexecutar/fechar Lucas/Shopee e Leonardo/Amazon antes de qualquer envio real.
- [ ] Manter envio real para Yasmin/Lucas/Leonardo bloqueado até autorização explícita de Kobe/Pedro e ciclo completo QA/Slack Writer validado; em 25/05 houve entrega temporária Pedro-only para Mercado Livre/Yasmin.
- [ ] Shopee Store e Shopee Conta 3: volume recuperou no pacote 25/05/2026 BRT (Store 72 pedidos, +10,6% vs média 30d; Conta 3 20 pedidos, -10,7% vs média 30d e dentro da banda), mas ainda observar por recorrência curta antes de encerrar o alerta.
- [ ] Mercado Livre/Yasmin 25/05/2026 BRT: revisar ressalvas menores do preview aprovado — corrigir padrão herdado na L05, preservar ACOS interno em 14,15% apesar do arredondamento visual para 14,2%, e alinhar leitura do cluster Potes Vidro 5 Peças entre análise agregada e Top Produtos por variação.
- [ ] Mercado Livre/Yasmin: acompanhar concentração dos Potes Vidro 5 Peças, ADS respondendo por 56,7% do faturamento, possível risco de ruptura do Kit 6 Canecas Lisas 200ml em Full e pedidos do Kit 10 Potes 1050ml pausado/sem estoque.
- [ ] Amazon: cancelamentos caíram para 2 no pacote 25/05/2026 BRT; validar recorrência por ASIN apenas se o volume voltar a subir.
- [ ] Shopee Full+: calcular impacto financeiro estimado por conta para junho/2026 e separar SKUs Full com item >= R$50 antes de recomendar mudança de mix; Conta 3 está abaixo do corte mínimo de 40% no MTD.
- [ ] Validar por que o pacote de dados do Daily Sales v2 para 23/05/2026 BRT ficou em **DADOS_PARCIAIS** e não teve artefatos finais de Slack Writer/QA Gate detectados; manter envio real bloqueado até fechamento do ciclo e autorização explícita.
- [ ] Verificar por que não há novo pacote completo do Daily Sales v2 para 21/05/2026 BRT nas memórias diárias por conta/outputs do Trader, caso a rotina diária estivesse prevista para rodar.
- [ ] Corrigir e reexecutar Lucas/Shopee para 20/05/2026 BRT: ajustar na 6B o percentual de GMV da Budamix Store de 49% para ~45% (R$ 2.351,20 / R$ 5.232,53 = 44,9%), reprocessar Slack Writer e validar que o QA deixa de ser BLOCKED antes de qualquer envio.
- [ ] Corrigir e reexecutar Lucas/Shopee para 19/05/2026 BRT: remover duplicidade CTL002 no Top Produtos, posicionar a linha consolidada de 10 pedidos na 3ª posição, formatar breakdown com separadores claros e validar que o QA deixa de ser BLOCKED antes de qualquer envio.
- [ ] Ajustar Slack Writer/06B de Shopee para que linha consolidada cross-conta substitua integralmente linhas componentes já contidas no total; aplicar também ao KIT2YW800SQ e registrar decisões de formatação coerentes.
- [ ] Monitorar simplificações da Slack Writer Shopee frente à 6B: manter linguagem mais simples sem remover evidências operacionais essenciais; se o padrão persistir, ajustar prompt antes de envio real.
- [ ] Ajustar Slack Writer de Mercado Livre para preservar âncoras de framing Padrão B (“parece saudável, mas...”) e registrar formalmente qualquer simplificação relevante.
- [ ] Mercado Livre: avaliar se fulfillment parcial deve aparecer na visão da Yasmin com ressalva de cobertura quando o mix top 10 divergir materialmente do padrão recente; priorizar série temporal de health e ADS breakdown por item para gatilhos com Himmel.
- [ ] Corrigir logs de Amazon: item exibido no ranking não pode aparecer como “omitido”; recalcular ranking/posições após exclusões antes de gerar decisões de formatação.
- [ ] Amazon: registrar simplificações de evidência de concentração na Slack Writer/QA (ex.: segundo candidato e distância para o líder) e criar linha de base semanal/mensal com concentração CK4742, volume, ticket e cancelamentos.
- [ ] Corrigir nomes internos Amazon TL250P/TL250B: não podem aparecer como tigelas de vidro se o produto real for canecas de porcelana Tulipa.
- [ ] Monitorar primeira execução real/autorizada do wrapper v2 e garantir que análise por conta use memória diária/semanal/mensal, nome comercial e sem SKU cru; se LLM falhar, bloquear recipient em vez de fallback.
- [ ] Tornar obrigatório no log da Slack Writer o registro formal de todos os itens “não pode ir para Slack”, inclusive regras gerais, restrições de inferência e toda omissão de Top Produtos por nome, mesmo item de 1 pedido com confiança alta; incluir omissões por volume residual como KIT2YW1050 quando aplicável.
- [ ] Corrigir mapeamentos/nome comercial que contaminam Daily Sales: Amazon TL250B/TL6250 não podem aparecer como tigelas de vidro; Shopee SKU 098 deve usar raw_title/descrição correta; ML 914C_BAV não deve receber rótulo inventado.
- [ ] Incluir/validar no pacote Daily Sales: Shopee Full real por conta, Buy Box e cobertura FBA por ASIN na Amazon, atribuição de cancelamentos por produto quando disponível.
- [ ] Monitorar Shopee nas 3 contas por queda transversal vs média 30d, concentração dos top produtos e possível canibalização interna entre lojas; pacote de 23/05/2026 BRT marcou Store com 38 pedidos (-44,0% vs média 30d) e Conta 3 com 13 pedidos (-45,8% vs média 30d), exigindo nova checagem no próximo ciclo antes de possível intervenção Lucas + Himmel.
- [ ] Amazon: validar recorrência dos 7 cancelamentos registrados no pacote de 23/05/2026 BRT por ASIN antes de tratar como ruído operacional.
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

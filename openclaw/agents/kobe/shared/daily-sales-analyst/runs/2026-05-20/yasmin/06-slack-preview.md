<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.087,71
- Pedidos: 91 pedidos
- Ticket médio: R$ 55,91
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 5 Potes de Vidro Redondos Tampa Preta — 23 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml — 13 pedidos
- Jogo 6 Canequinhas 100ml com Suporte de Madeira — 8 pedidos
- Kit 10 Potes Herméticos 1050ml 4 Travas — 5 pedidos
- Jogo Potes de Vidro 5 Peças Claro — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml — 3 pedidos
- Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 — 3 pedidos
- Kit 4 Potes de Vidro 320ml 4 Travas — 3 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- O anúncio de Kit 06 Canequinhas com Suporte de Madeira Acrílico provavelmente zerou o estoque no CD ML após os 3 pedidos de ontem e segue ativo em fulfillment — o ML pode continuar aceitando novos pedidos sem estoque para atender. Os 3 cancelamentos do dia coincidem numericamente com esses 3 pedidos, mas a origem não foi confirmada. Se vier desse anúncio, o cancellations_rate hoje zerado já está sendo pressionado — e a reputação 5_green/gold é o ativo que sustenta exposição e elegibilidade ADS de toda a conta. (risco latente — origem dos cancelamentos não confirmada)
- O mix de fulfillment do dia ficou em 56% Full contra 74% no histórico 30d, mas a queda foi produto-específica: o Kit 5 Potes Tampa Preta liderou o dia em Cross-Docking e sozinho puxou o número 18 pontos abaixo do padrão. O perfil estrutural de 74–78% Full em volume de pedidos da conta não mudou.
- O GMV ficou 32% acima da média histórica das quartas-feiras com volume de pedidos praticamente idêntico ao bimestre — a diferença toda está no ticket (R$ 55,91 vs R$ 41,53 histórico de quarta). A conta subiu de patamar via mix de valor, não via alcance. O ponto de atenção: 60% desse resultado passou por ADS, e os dois maiores anúncios Full têm health penalizada abaixo do limiar ML de 0,85. Como a memória da conta começa agora, os valores de hoje — ADS share, ticket e health dos campeões — são o ponto zero que vai revelar nos próximos ciclos se essa dependência de ADS é padrão estabelecido ou deterioração recente. (hipótese — sem série histórica para confirmar)

🎯 PRIORIDADES DO DIA
- Yasmin: verificar se o Kit 06 Canequinhas com Suporte de Madeira Acrílico tem reposição confirmada no CD ML para hoje — se não tiver, pausar antes que novos pedidos gerem cancelamentos forçados. O anúncio provavelmente zerou o estoque após os 3 pedidos de ontem e segue ativo em fulfillment; cada cancelamento forçado pressiona o cancellations_rate hoje em zero, colocando a reputação 5_green/gold em risco direto. Confirmar/refutar: reposição confirmada no CD ML nas próximas 4h = risco neutralizado; available_quantity ainda zerado no painel ML = pausar imediatamente e registrar como variável nos próximos ciclos. Escalar se: qualquer cancelamento registrado hoje oriundo desse anúncio — checar reputação no painel ML e registrar para Kobe se cancellations_rate sair do zero.
- Yasmin: confirmar se o Kit 6 Canecas Porcelana Tulipa 250ml tem reposição programada no CD ML — estoque estimado em aproximadamente 16 unidades com cobertura de cerca de 3 dias ao ritmo atual. É anúncio de catálogo em fulfillment; ruptura nesse contexto tem recuperação de posição no Buy Box mais lenta do que em anúncio Clássico. Confirmar/refutar: reposição com ETA igual ou inferior a 3 dias = monitorar; sem reposição programada e estoque zerado nos próximos 2 dias = risco de ruptura em catálogo/fulfillment com impacto de Buy Box.
- Yasmin: registrar os valores do dia como ponto zero da série — ADS share 59,8% (R$ 3.041,56 de R$ 5.087,71 de GMV), ticket médio R$ 55,91 e health dos dois maiores anúncios Full penalizados — para que os próximos ciclos possam confirmar ou refutar a dependência estrutural de ADS. Confirmar/refutar: ADS share acima de 55% por 3 dias consecutivos = dependência estrutural confirmada; health de qualquer campeão Full caindo por 2 ciclos seguidos = necessidade de alinhamento com Himmel sobre cobertura ADS preventiva. Escalar se: ADS share acima de 55% por 3 dias consecutivos — abrir discussão com Kobe sobre diversificação orgânica.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de que os 3 cancelamentos do dia vieram do anúncio de Kit 06 Canequinhas com Suporte de Madeira Acrílico
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Hipótese plausível por coincidência numérica, não fato confirmado; apresentar como fato contamina a leitura de reputação
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada como hipótese com linguagem de risco latente ("provavelmente", "se vier desse anúncio", "origem não confirmada")
- **Aparece na mensagem final:** sim, como risco latente com ressalva explícita de não confirmação

---

- **Item bloqueado:** Afirmação de que o ADS está sustentando especificamente os anúncios com health degradada
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Breakdown de revenue ADS por anúncio é limitação estrutural permanente do pacote; hipótese aberta, não confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitida a afirmação específica; mencionado ADS share global (59,8%) sem atribuição por anúncio
- **Aparece na mensagem final:** não como afirmação — apenas ADS share global como dado

---

- **Item bloqueado:** Afirmação de que a health dos campeões Full está em queda ou em recuperação
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Pacote entrega apenas valor pontual; direção não determinável sem série histórica
- **Agregado autorizado:** não
- **Tratamento aplicado:** health mencionada como "penalizada abaixo do limiar ML de 0,85" sem indicar direção
- **Aparece na mensagem final:** sim, sem indicação de direção (nem queda nem recuperação)

---

- **Item bloqueado:** Uso de "Tampa Vermelha" como atributo confirmado do anúncio Jogo Potes De Vidro 5 Peças Claro (MLB3288536143)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Title ML usa "Claro" sem mencionar cor de tampa; display_name interno diz "Tampa Vermelha" ancorado pelo SKU, mas não confirmado pelo título ML
- **Agregado autorizado:** não — uso do title ML sem o atributo
- **Tratamento aplicado:** produto aparece no Top Produtos como "Jogo Potes de Vidro 5 Peças Claro", sem atributo de cor de tampa
- **Aparece na mensagem final:** sim, como "Jogo Potes de Vidro 5 Peças Claro" (title ML simplificado, sem "Tampa Vermelha")

---

- **Item bloqueado:** IDs técnicos MLB e SKUs crus em qualquer bloco do Slack
- **Origem do bloqueio:** L05 Condensadora / regra padrão ML
- **Motivo:** Regra padrão — MLBs e SKUs não aparecem na mensagem final
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum MLB ou SKU cru aparece na mensagem Slack
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) não citados no corpo da mensagem — são campos de pipeline interno; preservado apenas o sentido da classificação na linguagem da análise
- Classificação `risco latente` do insight 1 preservada com linguagem de indício: "provavelmente", "se vier desse anúncio", "origem não foi confirmada"; não transformada em fato
- Classificação `hipótese` do insight 3 preservada com ressalva explícita ao final: "(hipótese — sem série histórica para confirmar)"
- Classificação `fato` do insight 2 escrita diretamente, sem ressalva de incerteza — conforme permitido para fatos confirmados pela Condensadora
- Alerta de confiança nível médio: preservadas ressalvas nos insights 1 e 3; insight 2 (fato) não recebeu ressalva adicional desnecessária
- Fulfillment omitido da seção `📊 VISÃO MERCADO LIVRE` — dado de fulfillment_mix_yesterday_top10 cobre apenas o top 10 (71 pedidos de 91), não a totalidade do dia; não autorizado pela Condensadora para VISÃO; tratado somente na `🔍 ANÁLISE DA CONTA`
- Atribuição de Yasmin como responsável em todas as 3 prioridades — L05 não atribui responsável; atribuição feita nesta camada conforme regra da Slack Writer
- Simplificação de títulos ML no Top Produtos (registrado por produto):
  - `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto` → `Kit 5 Potes de Vidro Redondos Tampa Preta` (removido: "Hermético Redondo Com", reordenado para clareza; atributo "Tampa Preta" confirmado no title ML como "Preto")
  - `Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo` → `Kit 4 Potes de Vidro Hermético 1050ml` (removido: "Tampa 4 Travas Vedação Azul-petróleo"; dimensão 1050ml preservada)
  - `Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio Amarelo` → `Jogo 6 Canequinhas 100ml com Suporte de Madeira` (removido: "Caneca Café", "Alumínio Amarelo"; quantidade e dimensão preservadas)
  - `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades` → `Kit 10 Potes Herméticos 1050ml 4 Travas` (removido: "Refratário", "Budamix", "Azul-petróleo", "10 Unidades" redundante; dimensão e travas preservadas)
  - `Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita` → `Jogo Potes de Vidro 5 Peças Claro` (removido: "Mantimentos Marmita" — palavras-chave de SEO; "Claro" preservado conforme title ML e bloqueio de "Tampa Vermelha")
  - `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara` → `Kit 6 Canecas Porcelana Tulipa Lisa 250ml` (removido: "Coloridas Xícara" — palavras-chave de SEO)
  - `Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo` → `Kit 2 Potes de Vidro Hermético 1050ml` (mesmo padrão do Kit 4)
  - `Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto` → `Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4` (capitalização PS5/PS4 corrigida; "Preto" removido por ser cor do suporte, não variação de produto com impacto operacional; título já curto e identificável)
  - `Kit Conjunto 4 Potes De Vidro 320ml Tampa Hermético 4 Travas Azul-petróleo` → `Kit 4 Potes de Vidro 320ml 4 Travas` (removido: "Conjunto" redundante com "Kit", "Tampa Hermético", "Azul-petróleo"; dimensão 320ml e quantidade preservadas)
  - `Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico` → `Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico` (normalizado "06" para "6", "De 100 Ml" para "100ml"; "Acrílico" preservado pois diferencia do outro anúncio de canequinhas com suporte de madeira)
- Variações IMB501P e IMB501V tratadas como linhas separadas no Top Produtos — ambas aparecem no ranking com seus títulos ML distintos; consolidação em família IMB501 recusada pois são variações reais com volumes próprios e títulos distintos
- Nomes de camadas internas não citados (Estratégica, Tática, Operacional, Granular, Condensadora) — substituídos por linguagem externa ou omitidos
- Comparações temporais presentes apenas na `🔍 ANÁLISE DA CONTA`, não na `📊 VISÃO MERCADO LIVRE`
- Faturamento por produto não incluído no Top Produtos — pacote não traz receita validada por variação; formato padrão `[produto] — [pedidos] pedidos` aplicado a todos os itens
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84 pedidos
- Ticket médio: R$ 55,02
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes 1050ml — 11 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Tulipa 250ml — 6 pedidos

🔍 ANÁLISE DA CONTA
- O mix Full/Cross-Docking do dia (47% Full contra ~74% da janela longa) não é mudança de operação. O cluster IMB501 puxou o dia: Potes Vidro 5 Peças — Tampa Preta liderou em Cross-Docking com 20 pedidos, enquanto Potes Vidro 5 Peças — Tampa Vermelha em Full ficou abaixo do potencial por health penalizada (0,71). O Cross-Docking com estoque farto preencheu o espaço. Não é problema sistêmico de modalidade de envio.
- O GMV ficou na banda da sexta-feira (-2,1% vs média das últimas 4) e o ROAS de 10,87x parece ótimo, mas a estrutura é frágil: ADS respondeu por 70% da receita e os dois principais anúncios Full rodam com health penalizada — Kit 4 Potes 1050ml (0,75) e Potes Vidro 5 Peças — Tampa Vermelha (0,71). É o segundo ciclo nesse patamar. Se o ADS share seguir acima de 65% por mais 2 ciclos com health dos dois Full abaixo de 0,80, a dependência estrutural deixa de ser hipótese e vira tema pra discutir com Kobe.
- Kit 6 Canecas Tulipa 250ml está com 7 unidades em Full após 6 pedidos ontem — cobertura prospectiva de ~1 dia. Os pedidos de ontem já foram atendidos, mas a partir de hoje cada venda consome o buffer restante. Em Full, quando o estoque zera no CD do ML, o anúncio para de aparecer sem que a Budamix consiga intervir rapidamente. Yasmin confirma reposição hoje.

🎯 PRIORIDADES DO DIA
- Yasmin: confirmar hoje o status de reposição do Kit 6 Canecas Tulipa 250ml no CD do ML. Anúncio em Full com cobertura prospectiva de ~1 dia — sem reposição, sai do ar fora do controle direto da Budamix e impacta GMV e posição dos próximos dias. Confirmar/refutar por: estoque acima de 5 unidades no CD do ML e anúncio ativo = risco neutralizado; estoque ≤ 2 unidades ou anúncio não ativo = risco materializado. Escalar se: próximo ciclo mostrar anúncio pausado ou estoque zerado sem reposição confirmada.
- Yasmin: checar a direção da health dos dois campeões Full no próximo ciclo com dado disponível — Kit 4 Potes 1050ml (hoje em 0,75) e Potes Vidro 5 Peças — Tampa Vermelha (hoje em 0,71). Health penalizada nesses dois sustenta o ciclo Full reduzido → ADS compensa; sem série, não dá para confirmar se está caindo, estável ou em recuperação. Confirmar/refutar por: variação até ±0,02 nos dois = observar mais 1 ciclo; abaixo de 0,70 em qualquer dos dois = Yasmin alinha com Himmel sobre cobertura preventiva de ADS; acima de 0,78 em qualquer um = sinal de recuperação. Escalar se: health dos dois cair simultaneamente abaixo de 0,70 no próximo ciclo com dado.
- Yasmin: registrar ADS share de 69,9%, ROAS 10,87x e ACOS 4,57% como segundo ponto da série, sem tocar em campanha. Campanha está em eficiência excepcional e a série tem só dois ciclos — mexer agora impede separar comportamento orgânico de efeito de ADS; sem registro sistemático, o terceiro ponto não terá base de comparação. Confirmar/refutar por: share acima de 65% por mais 2 ciclos com ROAS acima de 5x = dependência estrutural confirmada; share abaixo de 55% com volume orgânico crescendo = hipótese de orgânico em recuperação. Escalar se: três ciclos consecutivos com share acima de 65% — Yasmin abre discussão com Kobe sobre dependência de mídia paga.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

`o_que_nao_pode_ir_para_slack` da L05 está vazio. L04 Granular também não declarou nenhum `bloqueios_para_slack`. Todos os produtos do top 10 foram liberados com `risco_identificacao.nivel = "baixo"` e `bloqueios_para_slack = []`.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` de todos os três insights da L05 removidos da mensagem — são metadados de pipeline, não conteúdo para Yasmin.

**Preservação de classificações**
- Insight 1 (`classificacao: "fato"`) — escrito como afirmação direta: "não é mudança de operação", "não é problema sistêmico". Sem hedging.
- Insight 2 (`classificacao: "risco latente"`) — linguagem condicional preservada: "parece ótimo, mas a estrutura é frágil", "se o ADS share seguir acima de 65%... deixa de ser hipótese". Sem transformar em certeza.
- Insight 3 (`classificacao: "fato"`) — escrito como situação operacional confirmada (cobertura prospectiva de ~1 dia) com delimitação temporal explícita (pedidos de ontem já atendidos; risco estritamente prospectivo).

**Confiança media**
- Nível de confiança "media" (não "baixa") — sem necessidade de ressalva global explícita. Classificações individuais por insight já carregam a nuance adequada. Nenhum insight foi cortado por confiança insuficiente.

**Omissão de modalidade de envio na VISÃO**
- `fulfillment_mix_yesterday_top10` cobre 68 dos 84 pedidos do dia (~81%), calculado só sobre os top 10 itens ponderados por pedidos — não representa dado objetivo da plataforma sem ressalva. L05 não autorizou exibição com cobertura explícita nesta seção. Modalidade de envio tratada exclusivamente na ANÁLISE DA CONTA, onde a L05 contextualizou o mix de dia vs janela longa.

**Traduções de nome de produto — Top Produtos (5 primeiros)**
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- TL6250 — usado slack_short_name "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)

**Traduções de nome de produto — Análise da Conta e Prioridades (cross-section)**
- L05 escreveu "Tampa Preta em Cross-Docking liderando com 20 pedidos" → L06 traduziu para "Potes Vidro 5 Peças — Tampa Preta liderou em Cross-Docking com 20 pedidos" (padronização com slack_short_name de IMB501P)
- L05 escreveu "Tampa Vermelha em Full ficou abaixo do potencial por health penalizada (0,71)" → L06 traduziu para "Potes Vidro 5 Peças — Tampa Vermelha em Full ficou abaixo do potencial por health penalizada (0,71)" (padronização com slack_short_name de IMB501V)
- L05 escreveu "Kit 4 Potes 1050ml em 0,75 e o Conjunto 5 Potes Tampa Vermelha em 0,71" → L06 traduziu para "Kit 4 Potes 1050ml (0,75) e Potes Vidro 5 Peças — Tampa Vermelha (0,71)" — divergência de denominação cross-layer registrada: L05 usou "Conjunto 5 Potes Tampa Vermelha"; L06 usou "Potes Vidro 5 Peças — Tampa Vermelha" (padronização com slack_short_name canônico de IMB501V)
- L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" → L06 traduziu para "Kit 6 Canecas Tulipa 250ml" (padronização com slack_short_name de TL6250)

**Linguagem técnica nas prioridades**
- L05 usou campos técnicos nos sinais de confirmação/refutação (`available_quantity > 5`, `status=active`, `status ≠ active`) — substituídos por linguagem operacional equivalente: "estoque acima de 5 unidades no CD do ML e anúncio ativo" / "estoque ≤ 2 unidades ou anúncio não ativo". Sentido e limiares preservados.

**Estoque como dado prospectivo**
- `available_quantity = 7` do Kit 6 Canecas Tulipa 250ml apresentado exclusivamente como risco prospectivo (D+1 / D+2), com delimitação explícita de que os 6 pedidos de ontem já foram processados. Nenhuma afirmação retrospectiva ("pedidos sem cobertura", "cancelamento iminente sobre os pedidos de ontem"). Conforme regra obrigatória de estoque POST-baixa.

**Separação de variações IMB501**
- Família IMB501 mantida em três variações distintas (Tampa Preta, Tampa Vermelha, Tampa Cinza) em todas as seções. Nenhuma consolidação para agregado familiar. Conforme regra de variações vendáveis reais.

**Atribuição de responsável**
- Yasmin atribuída como responsável nas três prioridades. L05 não atribui responsável — L06 aplica conforme regra fixa (Mercado Livre é de Yasmin).

**Escalonamento para Kobe e Himmel**
- Escalonamento para Kobe preservado na prioridade 3 (share acima de 65% por três ciclos consecutivos), conforme L05.
- Escalonamento para Himmel preservado na prioridade 2 (health abaixo de 0,70 em qualquer dos dois Full), conforme L05. Himmel acionado via Yasmin, conforme regra de acionamento.

**Produtos no top 10 citados fora do Top 5 visível**
- Potes Vidro 5 Peças — Tampa Preta e Potes Vidro 5 Peças — Tampa Vermelha aparecem tanto no Top 5 visível quanto na Análise (posições 1 e 3 do ranking). Sem conflito.
- Kit 4 Potes 1050ml (posição 2 do ranking) citado na Análise e Prioridades — presente no Top 5 visível.
- Kit 6 Canecas Tulipa 250ml (posição 5 do ranking) citado na Análise e Prioridades — presente no Top 5 visível.
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 09/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 8.220,56
• Pedidos: 168
• Ticket médio: R$ 48,93
• Cancelamentos: 6

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 50 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 20 pedidos
• Kit 4 Potes 1050ml — 20 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 15 pedidos
• Kit 4 Potes 800ml — Quadrado — 7 pedidos

🔍 ANÁLISE DA CONTA
• Dois anúncios Full fecharam o dia com cobertura de ~1 dia e sem restock confirmado entre os ciclos. O Kit 4 Potes 1050ml saiu de 33 para 28 unidades com ritmo de 20 pedidos/dia. O Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico saiu de 19 para 11 unidades. Se qualquer um pausar nas próximas horas, os pedidos que entrarem podem virar cancelamento automático — o que pode pressionar a reputação Platinum recém-conquistada.
• O top3 aparente (53,6% do volume) esconde uma concentração mais aguda: Potes Vidro 5 Peças Tampa Preta e Tampa Vermelha juntos carregam 41,7% do volume sozinhos, os dois na mesma listagem. O alívio deste ciclo é que essa listagem recebeu restock entre 08/06 e 09/06 (de 1.056 para 1.407 unidades) — o risco do dia está nos dois Full secundários, não no produto que lidera o volume.
• A proporção de envios Full caiu de 79,8% (média de 30 dias) para 75,3% no dia — mas não é queda estrutural. Potes Vidro 5 Peças Tampa Cinza (15 pedidos, Cross-Docking) e Kit 10 Potes 520ml (7 pedidos, Cross-Docking) explicam a diferença por inteiro. Os campeões seguem em Full.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar hoje se há restock em trânsito ao CD do ML para o Kit 4 Potes 1050ml e qual o prazo estimado de chegada. O anúncio fechou com 28 unidades e ritmo de 20 pedidos/dia (~1,4 dia de cobertura) — o restock anterior foi insuficiente para o ritmo atual. Confirmar/refutar por: mais de 40 unidades no próximo snapshot confirma restock ativo e risco neutralizado; anúncio pausado com pedidos abertos exige triagem imediata. Escalar se: anúncio pausar com pedidos abertos e taxa de cancelamentos sair de zero — Yasmin alinha com Himmel se houver campanha ativa vinculada.
• Yasmin: checar unidades disponíveis e status do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico. O anúncio saiu de 19 para 11 unidades — consumo exato do dia, sem restock, segundo ciclo no limiar crítico (~1,4 dia de cobertura). Confirmar/refutar por: mais de 15 unidades confirma reposição; anúncio pausado com pedidos abertos confirma ruptura.
• Yasmin: checar a direção do nível de qualidade do anúncio Full Potes Vidro 5 Peças (qualidade em regular, 18º+ ciclo sem variação) e do Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo (qualidade em preocupante, 6º ciclo seguido). A fatia do ADS no faturamento caiu pelo 9º ciclo seguido (44,3%) — o ADS cobre menos a exposição orgânica. Nova queda de qualidade nesses dois derruba ranking de categoria sem amortecedor. Confirmar/refutar por: nível estável ou em recuperação encerra o risco do ciclo. Escalar se: qualidade do líder cair para preocupante ou qualidade do 640ml aprofundar por dois ciclos consecutivos — Yasmin alinha com Himmel.

Dia analisado: 09/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

`o_que_nao_pode_ir_para_slack` da L05 retornou lista vazia. `bloqueios_para_slack` da L04 também vazio (risco de identificação declarado como baixo, fontes vazias). Nenhum produto ou atributo foi bloqueado; todos os itens referenciados são elegíveis para o Slack.

---

### Decisões de formatação

**Metadados internos removidos**
- Campos `padrao`, `base` e `classificacao` de cada insight da L05 não aparecem na mensagem — são metadados de pipeline, não conteúdo para Yasmin.

**Classificação "risco latente" — preservação de nuance (insight 1)**
- L05 classificou o duplo risco de cobertura como `risco latente`. Mensagem usa "podem virar cancelamento automático" e "pode pressionar a reputação Platinum" para preservar o condicional. Não transformado em certeza.

**Classificação "fato" — insights 2 e 3 escritos como afirmações diretas**
- Insight 2 (concentração 41,7%): escrito como fato, sem "parece" ou "sugere".
- Insight 3 (queda de Full não estrutural): escrito como fato, sem hedging.

**Nomes de produto — mapeamento canônico (slack_short_name presente)**
- IMB501P → usado `slack_short_name`: "Potes Vidro 5 Peças — Tampa Preta"
- IMB501V → usado `slack_short_name`: "Potes Vidro 5 Peças — Tampa Vermelha"
- IMB501C → usado `slack_short_name`: "Potes Vidro 5 Peças — Tampa Cinza"
- KIT4YW1050 → usado `slack_short_name`: "Kit 4 Potes 1050ml"
- KIT4YW800SQ → usado `slack_short_name`: "Kit 4 Potes 800ml — Quadrado"
- KIT10YW520 → usado `slack_short_name`: "Kit 10 Potes 520ml"

**Nomes de produto — fallback display_short (slack_short_name null)**
- 914C_BA (Kit 06 Canequinhas Acrílico) → sem mapeamento manual; usado `display_short`: "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" (zero à esquerda normalizado: 06 → 6; capitalização corrigida)
- KIT4YW640 → sem mapeamento manual; usado `display_short`: "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo"

**Divergências de denominação cross-layer**
- L05 insight 1 e prioridade 1 usaram "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" (title longo); L06 usou "Kit 4 Potes 1050ml" (slack_short_name de KIT4YW1050) — padronização com nome canônico aprovado.
- L05 prioridade 2 usou "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" (title literal); L06 usou "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" (display_short de 914C_BA; slack_short_name null).
- L05 insights 2 e 3 usaram "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" e "Tampa Preta/Vermelha/Cinza" sem nome curto; L06 traduziu para slack_short_names canônicos em todas as ocorrências.
- L05 prioridade 3 usou "Jogo Potes 5 Peças Claro líder" (referência de listing, sem variação) e "MLB5402326666"; L06 usou "anúncio Full Potes Vidro 5 Peças" (qualidade é da listing inteira, não da variação) e "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo" (display_short de KIT4YW640) — IDs MLB removidos da mensagem.
- L05 insight 3 mencionou "o Kit 10 Potes 520ml" (já encurtado internamente); L06 manteve "Kit 10 Potes 520ml" (coincide com slack_short_name de KIT10YW520).

**Top 5 visível vs top 10 analítico**
- Análise (insight 3) e Prioridades (prioridade 3) mencionam Kit 10 Potes 520ml (#7, 7 pedidos) e Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo (#9, 4 pedidos), que não aparecem no Top 5 visível — permitido pois ambos estão no top 10 com relevância analítica direta (mix Cross-Docking e risco de qualidade, respectivamente).

**Modalidade de envio omitida da seção VISÃO**
- `fulfillment_mix_yesterday_top10` cobre apenas os top 10 itens ponderados por pedidos (89 pedidos resolvidos de 168 = ~53% do total) — cobertura parcial da conta. Sem autorização explícita da Condensadora para exibir com ressalva de cobertura. Modalidade de envio tratada somente na seção ANÁLISE DA CONTA, onde vem da L05.

**Quebras de frase aplicadas**
- Insight 1 da L05 era uma única frase de 3 cláusulas encadeadas com duplo travessão. Dividido em 4 frases sem alterar tese, números ou conectivos que mudam nuance.
- Insight 2 da L05 tinha estrutura "é na prática X (...) — a estreiteza é Y, e o único alívio é Z, então o risco mora em W". Dividido em duas frases mantendo todos os elementos.

**Tradução de jargão técnico**
- "cancellations_rate" → "taxa de cancelamentos"
- "ETA" → "prazo estimado de chegada"
- "available_quantity" → "unidades disponíveis"
- "runway" → "cobertura (em dias)"
- "listing" mantido onde tecnicamente necessário (sem equivalente natural em português que preserve a distinção listing vs variação); em outros contextos: "listagem"

**Limiar de qualidade expresso sem pontuação numérica**
- L05 prioridade 3 definiu gatilho como "líder abaixo de 0,70 ou 640ml abaixo de 0,63". L06 traduziu para "qualidade do líder cair para preocupante" (0,70 é o limite exato entre regular e preocupante) e "qualidade do 640ml aprofundar por dois ciclos consecutivos" (preserva a condição de dois ciclos sem expor o sub-valor dentro da faixa preocupante). Yasmin recebe a informação operacional relevante sem o número bruto.

**Referência ao anúncio Full do Potes Vidro 5 Peças na prioridade 3**
- O health 0,71 é da listing MLB3288536143 (Tampa Preta + Tampa Vermelha, Full). Tampa Cinza opera em listing separada (MLB4535865311, Cross-Docking, health=null). L06 usou "anúncio Full Potes Vidro 5 Peças" para distinguir sem ambiguidade, sem expor o MLB.

**Yasmin atribuída como responsável**
- L05 não atribui responsável nas prioridades. L06 inseriu "Yasmin:" no início das 3 prioridades, conforme responsabilidade fixa do canal Mercado Livre.

**Confiança média — nuance preservada**
- Ressalvas prospectivas mantidas em insight 1 (risco latente) e nas condições de confirmação/refutação das prioridades 1 e 2. Resultados do snapshot D+1 e ETA de reposição são declarados como condições a confirmar, não como desfechos assumidos.
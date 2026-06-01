<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 31/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 8.267,83
• Pedidos: 189
• Ticket médio: R$ 43,75
• Cancelamentos: 6

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 66 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 28 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 27 pedidos
• Kit 4 Potes 1050ml — 16 pedidos
• Kit 6 Canecas Lisas 200ml — 15 pedidos

🔍 ANÁLISE DA CONTA
• O domingo foi o maior dia da série: R$ 8.267,83 e 189 pedidos. Mas os Potes Vidro 5 Peças (as três tampas) terminaram com só 38 unidades em Full depois de vender 127 no dia — menos de 8 horas de cobertura no ritmo atual. As três cores são um anúncio único: se a reposição no CD do ML não estiver confirmada, o anúncio pausa e os 64% do volume que sustentou o dia somem em bloco.
• O Kit 6 Canecas Tulipa 250ml está pausado com estoque zero, mas entraram 4 pedidos no dia — cancelamentos quase certos. Ainda não dá pra confirmar se os 6 cancelamentos contados hoje já incluem esses 4 ou se ainda estão pendentes. A taxa de cancelamentos da reputação segue em zero, mas é uma métrica lenta: o impacto chega nos próximos 3 a 5 dias e vai comprimir a previsão para MercadoLíder Platinum — hoje faltam R$ 19.876,77, com prazo estimado de virada em 4,3 dias.
• O Kit 4 Potes 1050ml fechou com 30 unidades depois de 16 pedidos — menos de 2 dias de cobertura em Full. Se os Potes Vidro 5 Peças pausarem, esse vira o líder na hora e a cobertura curta pode virar gargalo no mesmo dia. Não é risco isolado: a fila de Full no topo está apertada dos dois lados.

🎯 PRIORIDADES DO DIA
• Yasmin: confirmar agora se há reposição em trânsito ao CD do ML para os Potes Vidro 5 Peças (as três tampas) e qual a previsão de chegada. Esse anúncio fez 64% do volume do dia e ficou com menos de 8 horas de cobertura — sem reposição confirmada, pausa automaticamente e o nível de R$ 8k não se sustenta no próximo dia. Como saber se deu certo: reposição com previsão de chegada em até 24h neutraliza o risco; estoque abaixo de 10 unidades ou anúncio pausado sem reposição confirmada = ruptura ativa. Escalar se: estoque zerar ou anúncio pausar sem reposição — escalar imediatamente para a operação de estoque.
• Yasmin: verificar o status dos 4 pedidos do Kit 6 Canecas Tulipa 250ml — já foram cancelados automaticamente ou ainda há janela para resolver manualmente. O anúncio estava pausado com estoque zero quando esses pedidos entraram; a chance de cancelamento é quase certa. Entram na janela de reputação e no cálculo para Platinum, hoje a 4,3 dias. Como saber o impacto: taxa de cancelamentos sair de zero nos próximos 3 dias confirma entrada na janela oficial; permanecer em zero por 5 dias = impacto absorvido fora da métrica.

Dia analisado: 31/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. `o_que_nao_pode_ir_para_slack` da L05 está vazio; nenhum item da L04 (`bloqueios_para_slack`) foi marcado.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` removidos da mensagem — não citados; nuances preservadas via linguagem: condicional ("se… pausa", "pode virar gargalo") para os dois itens com `classificacao: "risco latente"`; afirmativa ("cancelamentos quase certos", "vai comprimir") para o item com `classificacao: "fato"`.

**Nomes de produto — Top Produtos (mapeamento canônico)**
- IMB501P → usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C → usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- IMB501V → usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- KIT4YW1050 → usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- CLR002 → usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)

**Nomes de produto — Análise e Prioridades (mapeamento canônico)**
- TL6250 (citado na análise e prioridades; posição 8 no top_products, dentro do top 10) → usado slack_short_name "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)
- KIT4YW1050 (citado na análise) → usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- Cluster IMB501 como conjunto (anúncio único MLB3288536143 com três tampas) → referenciado como "Potes Vidro 5 Peças (as três tampas)"; não existe slack_short_name para o agregado; construção baseia-se na raiz comum dos três slack_short_names sem atributo de cor, preservando o sentido de anúncio único.

**Divergências de denominação cross-layer**
- L05 usou "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" (title ML) → L06 escreveu "Potes Vidro 5 Peças (as três tampas)"; motivo: padronização com a base dos slack_short_names das variações IMB501 e necessidade de refletir que as três cores são um único anúncio.
- L05 usou "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → L06 escreveu "Kit 4 Potes 1050ml"; motivo: slack_short_name canônico de KIT4YW1050.
- L05 usou "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → L06 escreveu "Kit 6 Canecas Tulipa 250ml"; motivo: slack_short_name canônico de TL6250.

**Jargão técnico traduzido**
- "ETA" → "previsão de chegada" / "prazo estimado"
- "available_quantity" → "estoque" / "unidades"
- "ciclos" → "dias"
- "patamar" → "nível"
- "snapshot" → omitido; substituído por "próximo dia"
- "gap" → "faltam R$ X para"
- "cancellations_rate" → "taxa de cancelamentos"
- "janela rolling de reputação" → "janela de reputação" / "janela oficial"
- "vetor" → "anúncio" / "volume que sustentou o dia"
- "GMV" → "Faturamento" (em todos os usos, inclusive na análise onde L05 usou "R$ 8.267" — corrigido para R$ 8.267,83 com centavos obrigatórios)
- "ADS share" → não aparece na mensagem (L05 não incluiu ADS nos 3 insights finais)

**Valores monetários**
- R$ 8.267,83 — centavos adicionados (L05 arredondou para R$ 8.267); fonte: metrics.gmv = 8267.83 ✓
- R$ 19.876,77 — centavos adicionados (L05 usou R$ 19.876); fonte: mercadolider.platinum.gap_revenue_brl = 19876.77 ✓

**Modalidade de envio omitida da seção VISÃO**
- `fulfillment_mix_yesterday_top10` cobre 77 dos 189 pedidos do dia (~40,7%); representa apenas o top 10, não totalidade da conta; omitida conforme regra. Mix de modalidade de envio tratado apenas na Análise da Conta, conforme autorizado pela Condensadora.

**Prioridades**
- Responsável fixado como Yasmin em todas as prioridades (L05 não atribui responsável; atribuição feita aqui conforme regra da L06).
- "Escalar se: não aplicável" da prioridade 2 → linha de escalonamento omitida da mensagem.
- Sinais de confirmação/refutação preservados com linguagem natural ("Como saber se deu certo:" / "Como saber o impacto:"), conforme exemplos da diretriz Pedro 2026-05-25.

**Confiança**
- `alertas_de_confianca.nivel == "media"` — sem ressalva global explícita necessária; conclusões de risco operacional mantidas com linguagem firme onde sustentadas por evidência (fato) e condicional onde dependem de checagem direta (risco latente). Nenhum insight foi omitido por baixa confiança.
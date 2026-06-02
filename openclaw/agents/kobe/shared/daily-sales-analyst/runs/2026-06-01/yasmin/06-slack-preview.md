<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 01/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 9.953,44
- Pedidos: 206
- Ticket médio: R$ 48,32
- Cancelamentos: 9

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Vermelha — 45 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 40 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 33 pedidos
- Kit 6 Canecas Lisas 200ml — 19 pedidos
- Kit 4 Potes 1050ml — 14 pedidos

🔍 ANÁLISE DA CONTA
- A conta rompeu patamar de verdade. Os 206 pedidos e R$ 9.953,44 de Faturamento são quase o dobro da média dos últimos 30 dias e do mesmo dia da semana, com ticket praticamente igual ao histórico (R$ 48,32). Não é dia caro mascarando volume fraco — é alcance dobrado, dois dias seguidos acima de R$ 8k. O MercadoLíder Platinum está a 3,5 dias de ritmo médio (faltam R$ 16.112,54, progresso em 94,56%).
- O problema é que esse pico foi executado drenando o estoque Full dos campeões. Os Potes Vidro 5 Peças (Full) fecharam o dia com 13 unidades depois de 118 pedidos, e o Kit 4 Potes 1050ml (Full) também ficou com 13 depois de 14 pedidos — juntos, são 64% do volume do dia em cobertura de horas. O Kit 6 Canecas Lisas 200ml, único em Catálogo no top, ficou com 35 unidades depois de 19 pedidos (~1,6 dias de cobertura), e ruptura em Catálogo derruba o Buy Box. O snapshot de hoje cedo confirma os três ainda ativos, mas qualquer pausa automática nas próximas horas derruba volume e janela Platinum ao mesmo tempo.
- O ADS respondeu por 48,1% do Faturamento — menor fatia da série (era 69,9% em 22/05, caiu em todo ciclo desde então) — com ROAS 10,6x e ACOS 8,89%. O dia recorde aconteceu com ADS no piso de participação, ou seja, o crescimento veio do orgânico expandindo, não da campanha empurrando. Não é hora de mexer em campanha — esses números (48,1% de fatia do ADS, ROAS 10,6x, ACOS 8,89%) são o ponto de referência da série.

🎯 PRIORIDADES DO DIA
- Yasmin: confirmar se há reposição a caminho do CD do ML para os Potes Vidro 5 Peças e para o Kit 4 Potes 1050ml (ambos Full, 13 unidades cada após 132 pedidos combinados ontem). Esses dois sustentam 64% do volume atual — se qualquer um pausar por falta de estoque, o volume cai e os cancelamentos automáticos entram direto na janela Platinum com gap de R$ 16.112,54 e 3,5 dias de prazo. Confirmar/refutar por: reposição com previsão de chegada em até 24h hoje = risco neutralizado; sem reposição ou estoque abaixo de 5 unidades no próximo monitoramento = ruptura ativa. Escalar se: reposição não confirmada até o fim do dia ou qualquer um dos dois aparecer pausado — abrir decisão de envio emergencial ao CD do ML.
- Yasmin: verificar o status e o estoque atual do Kit 6 Canecas Tulipa 250ml (Full, voltou a aparecer ativo com 2 unidades depois de ter pausado em 31/05 com zero, 8 pedidos ontem). A partir do décimo primeiro pedido sobre essas 2 unidades, o anúncio pausa automaticamente, e cada cancelamento automático gerado entra direto na janela Platinum. Uma reposição maior entrou parcialmente, mas a cobertura ainda é mínima. Confirmar/refutar por: reposição maior chegando hoje = risco neutralizado; anúncio pausado novamente com cancelamentos confirmados = pressão direta na elegibilidade Platinum. Escalar se: a taxa de cancelamentos da reputação sair de zero enquanto o gap Platinum ainda estiver acima de R$ 10k.
- Yasmin: verificar a cobertura do Kit 6 Canecas Lisas 200ml (único em Catálogo no top, 35 unidades após 19 pedidos ontem — ~1,6 dias de cobertura). Ruptura em Catálogo não é só perda de venda: derruba o Buy Box e a recuperação é lenta. Confirmar/refutar por: reposição confirmada hoje ou estoque subindo no próximo monitoramento = risco contido; estoque abaixo de 15 unidades amanhã sem reposição a caminho = entra na mesma zona dos dois campeões. Escalar se: estoque cair abaixo de 10 unidades sem previsão de reposição.

Dia analisado: 01/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição dos 9 cancelamentos do dia a anúncios específicos (incluindo Tulipa)
- **Origem do bloqueio:** L04 Granular + L05 Condensadora
- **Motivo:** Hipótese em aberto — não há breakdown order_id↔platform_item_id↔motivo no pacote; top10 active no snapshot; qualquer atribuição seria especulação
- **Agregado autorizado:** não
- **Tratamento aplicado:** os 9 cancelamentos foram citados apenas como dado objetivo na seção VISÃO (fato do dia), sem atribuir origem ou anúncio na Análise ou Prioridades
- **Aparece na mensagem final:** sim, como dado numérico em VISÃO (`Cancelamentos: 9`) sem atribuição causal

---

- **Item bloqueado:** Afirmar que houve pausa automática overnight em qualquer anúncio entre 01/06 e 02/06
- **Origem do bloqueio:** L04 Granular + L05 Condensadora
- **Motivo:** L04 confirmou todos os top do dia como active no snapshot 02/06 09:50 UTC; hipótese L03 foi enfraquecida, não confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** linguagem prospectiva usada ("qualquer pausa automática nas próximas horas"), nunca retrospectiva afirmando que pausa ocorreu
- **Aparece na mensagem final:** não como evento passado; sim como risco prospectivo

---

- **Item bloqueado:** Citar IDs MLB (platform_item_id) na mensagem final
- **Origem do bloqueio:** L05 Condensadora (regra estrutural ML)
- **Motivo:** Regra de plataforma — MLB só para rastreabilidade interna
- **Agregado autorizado:** não aplicável (substituição por nome comercial)
- **Tratamento aplicado:** todos os produtos citados usam slack_short_name ou nome comercial; nenhum MLB visível na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Ruptura por variação específica do cluster IMB501 (Tampa Vermelha/Preta/Cinza zerada individualmente)
- **Origem do bloqueio:** L04 Granular + L05 Condensadora
- **Motivo:** available_quantity=13 é agregado do anúncio multi-variação; não há visibilidade por variação no pacote
- **Agregado autorizado:** sim — "Potes Vidro 5 Peças" (bloco do anúncio) e "13 unidades" como agregado
- **Tratamento aplicado:** cluster citado como bloco ("os Potes Vidro 5 Peças fecharam o dia com 13 unidades depois de 118 pedidos"); nenhuma cor específica mencionada como zerada
- **Aparece na mensagem final:** sim, como bloco agregado autorizado

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos de todos os insights — são campos de pipeline, não conteúdo de Slack
- Classificação `fato` (insights 1 e 3): linguagem direta e afirmativa preservada ("rompeu patamar de verdade", "o crescimento veio do orgânico expandindo")
- Classificação `risco latente` (insight 2): linguagem prospectiva preservada ("qualquer pausa automática nas próximas horas derruba volume e janela Platinum ao mesmo tempo"); não transformado em certeza
- Nível de confiança `media`: comunicação mantém ressalvas sobre o que não foi confirmado ("snapshot de hoje cedo confirma os três ainda ativos, mas..."); nenhum evento passado afirmado sem evidência
- `GMV` → `Faturamento` em todas as ocorrências (regra obrigatória)
- `ADS share` → `fatia do ADS no Faturamento` / `ADS respondeu por X%` — nunca escrito como "ADS share" na mensagem
- `ETA` → "prazo" / "dias de ritmo médio" / "previsão de chegada em até 24h" — traduzido em todas as ocorrências
- `available_quantity` → "estoque" / "unidades" — nunca citado como campo técnico no Slack
- `cancellations_rate` → "taxa de cancelamentos da reputação" — traduzido na prioridade de escalonamento
- `runway` → "cobertura" / "cobertura de horas" / "dias de cobertura" — traduzido em todas as ocorrências
- `Buy Box` mantido (termo ML conhecido e obrigatório)
- `MercadoLíder Platinum` / `MercadoLíder Gold` mantidos por extenso com grafia correta
- `Full` e `Catálogo` mantidos (vocabulário ML obrigatório)
- `health` nunca citado na mensagem — substituído por "nível preocupante" / "nível regular" conforme a faixa (decisão: não foram incluídas qualidades de anúncio na mensagem final pois a Condensadora não trouxe esse dado como insight distinto — estava apenas no contexto das prioridades e a L05 não o destacou como ponto de Análise ou Prioridade em si)
- Frases longas dos insights L05 quebradas em frases menores sem perda de tese (ex.: insight 2 dividido em três frases curtas encadeadas)
- Termos como "prospectiva", "snapshot", "breakdown", "platform_item_id" não aparecem na mensagem final
- `ratings_negative` não citado na mensagem — a L05 não o incluiu nos insights aprovados e a Condensadora o relegou à memória para amanhã; omitido corretamente
- `9 cancelamentos` incluído em VISÃO como dado objetivo; ausente de Análise/Prioridades como causa identificada (respeito ao bloqueio)
- Top Produtos: exibidos os 5 primeiros do `top_products` por ordem de pedidos
  - IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - CLR002 — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
  - KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- Cluster IMB501 nas seções Análise e Prioridades: referenciado como "Potes Vidro 5 Peças" (slack_short_name do bloco, sem cor — correto por bloqueio de variação individual); Kit 4 Potes 1050ml = "Kit 4 Potes 1050ml"; Kit 6 Canecas Lisas 200ml = "Kit 6 Canecas Lisas 200ml"; Kit 6 Canecas Tulipa 250ml = "Kit 6 Canecas Tulipa 250ml" (slack_short_name de TL6250)
- Divergência de denominação cross-layer: L05 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" no insight — L06 traduzido para "Potes Vidro 5 Peças" (slack_short_name do cluster); L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" — L06 traduzido para "Kit 4 Potes 1050ml"; L05 escreveu "Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida" — L06 traduzido para "Kit 6 Canecas Lisas 200ml"; L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" — L06 traduzido para "Kit 6 Canecas Tulipa 250ml"
- Modalidade de envio omitida da seção VISÃO: `fulfillment_mix_yesterday_top10` cobre apenas top 10 com 91 pedidos resolvidos de 206 (~44%) — não é dado objetivo completo do dia; omitido corretamente conforme regra da seção
- Responsável atribuído: Yasmin em todas as três prioridades (responsável fixo ML)
- Faturamento total: R$ 9.953,44 (duas casas decimais, separador de milhar com ponto, decimal com vírgula)
- `progress_pct` da L05 = 94,56% e `gap_revenue_brl` = 16.112,54 (arredondado de 16112.539999...) — usados como R$ 16.112,54 na mensagem; valor confirmado pela L05 no campo `platinum.gap_revenue_brl`
- Condições de escalonamento da L05 preservadas integralmente em todas as três prioridades
- Alternativas operacionais preservadas quando presentes (checagem via painel logístico ML mencionada implicitamente na prioridade 1 como "confirmar se há reposição a caminho do CD do ML")
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 07/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.115,98
- Pedidos: 84
- Ticket médio: R$ 49,00
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Cinza — 10 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 10 pedidos
- Kit 4 Potes 800ml — Quadrado — 8 pedidos
- Kit 6 Canequinhas 100ml — Madeira — 6 pedidos

🔍 ANÁLISE DA CONTA
- O dia fechou em R$ 4.115,98 e 84 pedidos — dentro da faixa normal dos domingos de maio (R$ 4.996,11–R$ 5.180,78 em 17-24/05). A queda de -49% no comparativo semanal é artefato: a semana passada teve o pico de 01-05/06, quando o líder Full estava abastecido. O patamar da conta não mudou.
- Os Potes Vidro 5 Peças — Tampa Vermelha (Full) voltaram a vender depois da pausa de 06/06, mas o estoque reposto era mínimo: cerca de 12 unidades, 10 já vendidas, restam 2. Em dia útil — ritmo de 40 a 100 pedidos — esse estoque pode se esgotar em horas. Parece ser o quarto ciclo iminente de ruptura em sete dias, e o lote de reposição segue pequeno para a demanda do canal.
- O MercadoLíder Platinum está tecnicamente conquistado pelo terceiro ciclo seguido: vendas 60d em R$ 298.699,79 contra threshold de R$ 296.000,00, contagem de vendas 4.872 acima do exigido — mas a medalha segue MercadoLíder Gold. Reputação verde, cancelamentos zero, reclamações em 36% do limite. O que sugere bloqueio são os ratings: 0,41 de avaliações negativas contra 0,56 de positivas. A margem financeira acima do threshold está em apenas R$ 2.699,79, e ontem o faturamento ficou 17% abaixo do ritmo necessário para manter esse saldo na janela rolante.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar no próximo snapshot o status e o estoque dos Potes Vidro 5 Peças — Tampa Vermelha (Full) e acionar reposição ao CD do ML antes que o ciclo de ruptura se repita. O restock de 06/06 cobriu só o domingo — restam 2 unidades, e em dia útil a nova pausa é iminente; cada episódio de pausa com pedidos ativos pressiona diretamente a margem do MercadoLíder Platinum. Confirmar/refutar por: estoque acima de 10 unidades com anúncio ativo = restock funcional; pausado ou zerado = ciclo crônico confirmado no 4º episódio em 7 dias. Escalar se: 4º ciclo consecutivo de pausa ou estoque abaixo de 5 confirmar que o lote é incapaz de cobrir a demanda — pauta para Kobe sobre dimensionamento de lote e estratégia de reposição.
- Yasmin: contatar suporte ML para investigar o critério pendente para o MercadoLíder Platinum. Terceiro ciclo seguido com gap zero e 100% de progresso, mas medalha segue MercadoLíder Gold — a hipótese mais provável é bloqueio pelos ratings negativos (0,41 de negativos contra 0,56 de positivos), e a margem financeira de R$ 2.699,79 acima do threshold está sendo corroída nos dias de estoque depletado. Confirmar/refutar por: suporte ML indica o critério específico pendente e Yasmin registra o gatilho real; medalha MercadoLíder Platinum no próximo snapshot refuta e encerra a ação.
- Yasmin: observar a direção do nível de qualidade do Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo (Full) no próximo snapshot — 4º ciclo seguido em nível preocupante, a 0,03 do limiar de alinhamento com Himmel. Estoque confortável (75 unidades); o risco é perder aparecimento no ranking de categoria, não ruptura. Confirmar/refutar por: nível estável ou subindo = observar mais 1 ciclo sem ação; cair abaixo de 0,63 = Yasmin alinha com Himmel sobre cobertura de ADS preventiva.

Dia analisado: 07/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

`o_que_nao_pode_ir_para_slack` da L05 está vazio. Nenhum item foi bloqueado pela L04 Granular (`bloqueios_para_slack: []`). Todos os 10 top products têm mapping_status mapped (9 high confidence, 1 medium) e foram tratados segundo as regras de nome canônico, sem necessidade de supressão.

---

### Decisões de formatação

- **Metadados internos removidos** — campos `padrao`, `base` e `classificacao` de cada insight da L05 não aparecem na mensagem. Foram usados internamente para calibrar o tom.
- **Insight 1 (fato) — linguagem direta** — classificação "fato" permite afirmação sem qualificador de indício. Frase reescrita em ordem direta; comparação de -49% vs 7d colocada em contexto como artefato, conforme tese L05.
- **Insight 2 (risco latente) — nuance preservada** — linguagem de indício usada: "parece ser o quarto ciclo iminente" e "pode se esgotar em horas" em lugar de certeza. Tese e dados (12 unidades, 2 residuais) mantidos intactos.
- **Insight 3 (hipótese) — nuance preservada** — linguagem de indício usada: "o que sugere bloqueio são os ratings". Proibido transformar em fato; hipótese apresentada como candidato mais provável, não como causa confirmada.
- **Top Produtos — todos os 5 usaram slack_short_name (mapeamento canônico):**
  - IMB501C → usado `slack_short_name "Potes Vidro 5 Peças — Tampa Cinza"` (mapeamento canônico)
  - IMB501V → usado `slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha"` (mapeamento canônico)
  - IMB501P → usado `slack_short_name "Potes Vidro 5 Peças — Tampa Preta"` (mapeamento canônico)
  - KIT4YW800SQ → usado `slack_short_name "Kit 4 Potes 800ml — Quadrado"` (mapeamento canônico)
  - 914C → usado `slack_short_name "Kit 6 Canequinhas 100ml — Madeira"` (mapeamento canônico)
- **Kit 4 Potes 640ml — fallback automático** — SKU KIT4YW640 tem `slack_short_name: null`; usado `display_short "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo"` (fallback automático; sem mapeamento manual para SKU KIT4YW640).
- **Divergência de denominação cross-layer — Kit 4 Potes 640ml** — L05 referenciou o produto nas prioridades como "Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo"; L06 usou display_short "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo". Motivo: padronização com fallback display_short obrigatório quando slack_short_name é null.
- **Divergência de denominação cross-layer — Potes Vidro 5 Peças — Tampa Vermelha** — L05 referenciou nas análises e prioridades como "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (Full, Tampa Vermelha)"; L06 usou `slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha"`. Motivo: padronização com mapeamento canônico IMB501V.
- **Modalidade de envio omitida da seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas 61 dos 84 pedidos do dia (72,6% de cobertura); dado não representa a totalidade do dia sem ressalva. Omitido da VISÃO conforme regra. Mencionado apenas na ANÁLISE DA CONTA onde a L05 trouxe o contexto analítico.
- **Comparação temporal mantida fora da VISÃO** — comparativo -49% vs 7d aparece exclusivamente na seção ANÁLISE DA CONTA, nunca na VISÃO.
- **Centavos adicionados conforme regra obrigatória** — L05 usou valores arredondados "R$ 298.699", "R$ 296.000" e "R$ 2.699"; L06 adicionou centavos conforme dado original do pacote (R$ 298.699,79; R$ 296.000,00; R$ 2.699,79). Idem para os valores dos domingos históricos: "R$ 4.996,11" e "R$ 5.180,78".
- **`escalar_se: não aplicável` das prioridades 2 e 3 omitido** — condição inexistente na L05 para essas prioridades; não há linha de escalonamento a preservar.
- **Nenhum MLB visível** — todos os anúncios referenciados aparecem pelo nome canônico do produto, sem IDs técnicos.
- **Atribuição de responsável** — Yasmin atribuída como responsável nas 3 prioridades, conforme regra fixa (a L05 não atribui responsável).
- **Top Produtos: 5 primeiros do ranking** — todos os 5 tinham mapping_status mapped e identificação segura; nenhum produto precisou ser descido no ranking por bloqueio.
- **Variações do cluster IMB501 mantidas separadas** — Tampa Cinza, Tampa Vermelha e Tampa Preta apresentadas como linhas distintas no Top Produtos, conforme regra de consolidação até nível de variação vendável. Não consolidadas como família "IMB501".
- **Faturamento por produto omitido do Top Produtos** — pacote não traz receita validada por produto/variação; formato usado: `[nome] — [pedidos] pedidos`.
- **Termos técnicos traduzidos** — "fulfillment" não aparece na mensagem; usado "Full" (modalidade de envio) e "CD do ML" (centro de distribuição). "health" não aparece; usado "nível de qualidade" com faixa "preocupante". "GMV" não aparece; usado "faturamento". "ETA" não aparece; usado "prazo" implícito em "reposição" e "próximo snapshot".
- **Numeração de health sem valor entre parênteses** — no Slack aparece apenas "nível preocupante"; o threshold operacional 0,63 mantido na condição de ação das prioridades por ser o critério de escalonamento explícito da L05.
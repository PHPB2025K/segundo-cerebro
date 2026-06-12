<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 11/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 7.304,72
- Pedidos: 185 pedidos
- Ticket médio: R$ 39,48
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 66 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 27 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 24 pedidos
- Kit 6 Canecas Tulipa 250ml — 12 pedidos
- Kit 4 Potes 1050ml — 7 pedidos

🔍 ANÁLISE DA CONTA
- O Kit 6 Canecas Lisas 200ml é o único anúncio em Catálogo no topo e tem 4 unidades restantes — quatro ciclos seguidos de queda sem reposição (35→28→11→5→4). Se pausar antes do estoque chegar no CD do ML, a Buy Box vai pro concorrente. Recuperar posição em Catálogo exige restock físico no Full antes de voltar ao ranking, ciclo mais lento que em Clássico.
- A conta tem três anúncios Full no horizonte de ruptura das próximas 48h — o Kit 6 Canecas Lisas 200ml com cobertura abaixo de 1 dia, o Kit 6 Canecas Tulipa 250ml no nono ciclo de cobertura crítica sem resolução, e o Kit 4 Potes 1050ml no terceiro ciclo de cobertura curta após restock parcial que não segurou. O patamar MercadoLíder Platinum está sólido — mas o segundo vetor não se forma porque a reposição dos adjacentes não acompanha o ritmo. Três rupturas Full simultâneas seria o caminho mais direto pro cancellations_rate sair de zero.
- O ADS do dia apareceu com gasto zero e 13 campanhas ativas — é lag da API do Mercado Ads, não realidade. Os últimos 13 ciclos registraram gasto entre R$ 262,00 e R$ 422,00 em dias úteis. Nada de acionar Himmel hoje e nada de atualizar a série de participação do ADS no faturamento nesse ciclo — espera o próximo dado válido.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar ETA de reposição no CD do ML para o Kit 6 Canecas Lisas 200ml (único Catálogo no topo, 4 unidades, cobertura abaixo de 1 dia). Ruptura em Catálogo é diferente — perde Buy Box pro concorrente e só recupera com estoque físico no CD antes de reativar ranking, ciclo mais lento. Confirmar/refutar por: ETA confirmado no CD em menos de 24h neutraliza o risco; status paused no snapshot de amanhã antes da reposição confirma perda de Buy Box em Catálogo. Escalar se: anúncio entrar em paused antes da reposição e ETA ultrapassar 72h — Yasmin abre com Kobe a decisão de priorizar alocação de estoque desse Catálogo na expedição.
- Yasmin: confirmar estoque e status do Kit 6 Canecas Tulipa 250ml amanhã (5 unidades, 12 pedidos ontem, nono ciclo seguido do mesmo padrão). Cada ciclo pausado gera cancelamentos que pressionam o cancellations_rate a sair de zero — junto com o Kit 6 Canecas Lisas 200ml e o Kit 4 Potes 1050ml, formam horizonte de três rupturas Full ao mesmo tempo. Confirmar/refutar por: estoque acima de zero e status active amanhã indica reposição parcial; status paused confirma décimo ciclo e classifica como falha estrutural de reposição.
- Yasmin: verificar se restock foi programado para o Kit 4 Potes 1050ml (19 unidades, caiu de 28 para 19 em 24h sem novo estoque, terceiro ciclo de cobertura curta). O restock parcial de ontem não segurou o ritmo — sem entrada nas próximas 48h, vira o terceiro Full a romper junto com o Catálogo Lisas e a Tulipa. Confirmar/refutar por: estoque acima de 25 amanhã indica restock entrou; abaixo de 12 indica aceleração sem cobertura e eleva pra ação imediata.

Dia analisado: 11/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** ADS share, ROAS, ACOS e qualquer leitura de autonomia orgânica do dia 11/06/2026
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** dado de Mercado Ads do dia inválido (spend=0 com 13 campanhas ativas, contradizendo 13+ ciclos de memória com gasto real); usar como base induziria decisão errada sobre campanha
- **Agregado autorizado:** não — o bloqueio é sobre a análise de ADS; o fato do lag em si foi autorizado pela L05 como insight classificado como fato
- **Tratamento aplicado:** nenhum valor de ADS share, ROAS ou ACOS incluído; mencionado apenas que o dado é inválido (lag de API) e que a série fica suspensa
- **Aparece na mensagem final:** não (como análise quantitativa); sim, como fato do lag no terceiro bullet de análise

---

- **Item bloqueado:** Afirmar que cancellations_rate vai sair de zero ou que a reputação está em deterioração
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** cancellations_rate oficial permanece em zero; cancelamentos do dia recuaram para 3 (1,6% vs 4,3% em 10/06); risco é prospectivo, não confirmado
- **Agregado autorizado:** não
- **Tratamento aplicado:** linguagem condicional preservada no segundo bullet de análise ("seria o caminho mais direto pro cancellations_rate sair de zero") e na prioridade 2 ("pressionam o cancellations_rate a sair de zero") — risco prospectivo, sem afirmação de fato consumado
- **Aparece na mensagem final:** não (como afirmação de deterioração confirmada); sim, como risco condicional prospectivo

---

- **Item bloqueado:** Atribuir causa específica para a ausência das listagens Cross-Docking do cluster IMB501 no top10 de 11/06
- **Origem do bloqueio:** L05 Condensadora (derivado de L04 Granular — conclusão=inconclusivo por falta de dado)
- **Motivo:** pacote não entrega ranking, status das listagens Cross-Docking nem breakdown ADS por anúncio; afirmar causa seria especulação
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da mensagem Slack; não mencionado em nenhuma seção
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos de todos os três insights — são campos de pipeline, não conteúdo para Yasmin.
- Insights 1 e 2 classificados como `risco latente` → linguagem condicional aplicada: "se pausar antes do estoque chegar", "tem três anúncios Full no horizonte de ruptura", "seria o caminho mais direto". A tese e a estrutura foram preservadas; apenas o modal foi ajustado para refletir que o risco ainda não se materializou.
- Insight 3 classificado como `fato` → escrito diretamente, sem hedging.
- Confiança `media` → não exige ressalva global; nuance preservada via linguagem condicional dos riscos latentes. Nenhuma ressalva de confiança adicionada como frase avulsa.
- **IMB501P** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico).
- **IMB501V** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico).
- **IMB501C** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico).
- **TL6250** — usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico).
- **KIT4YW1050** — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico).
- Top Produtos exibido apenas com pedidos por variação — L00 não entrega receita validada por produto; formato: `[nome] — [pedidos] pedidos`.
- Modalidade de envio omitida da seção VISÃO — `fulfillment_mix_yesterday_top10` cobre apenas 67 de 185 pedidos do dia (top 10, ~36% do total); dado não representa cobertura objetiva da plataforma sem ressalva. Condensadora não autorizou exibição com cobertura explícita.
- Sem comparação temporal na seção VISÃO — comparações pertencem à ANÁLISE DA CONTA.
- Divergência de denominação cross-layer registrada item a item:
  - L05 escreveu "Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida" → L06 usou "Kit 6 Canecas Lisas 200ml" (slack_short_name do SKU CLR002, mapeamento canônico).
  - L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → L06 usou "Kit 6 Canecas Tulipa 250ml" (slack_short_name do SKU TL6250, mapeamento canônico).
  - L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → L06 usou "Kit 4 Potes 1050ml" (slack_short_name do SKU KIT4YW1050, mapeamento canônico).
- Valores aproximados da série de memória de ADS ("entre R$262 e R$422") formatados com centavos obrigatórios: "entre R$ 262,00 e R$ 422,00".
- `escalar_se: não aplicável` nas prioridades 2 e 3 da L05 → linha "Escalar se:" omitida nessas prioridades.
- Escalonamento para Kobe na prioridade 1 preservado conforme L05 — decisão de alocação de estoque do Catálogo na expedição está dentro do escopo autorizado.
- Responsável Yasmin atribuído em todas as três prioridades (L05 não atribui responsável; atribuição é função da L06 para canal Mercado Livre).
- Nomes de camadas internas (Estratégica, Tática, Operacional, Granular, Condensadora) não mencionados na mensagem.
- Nenhum MLB, SKU ou ID técnico visível na mensagem final.
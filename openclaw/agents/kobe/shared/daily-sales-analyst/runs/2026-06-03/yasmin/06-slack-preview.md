<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 03/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 6.401,41
• Pedidos: 142
• Ticket médio: R$ 45,08
• Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 56 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 18 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 12 pedidos
• Kit 6 Canecas Lisas 200ml — 9 pedidos
• Kit 6 Canequinhas 100ml — Madeira — 6 pedidos

🔍 ANÁLISE DA CONTA
• O dia fechou em R$ 6.401,41 sem nenhum gasto de ADS — mas com 12 campanhas declaradas ativas. Antes de chamar isso de piso orgânico, Yasmin precisa confirmar com Himmel se o zero é interrupção real ou atraso de registro, porque as duas hipóteses levam a ações opostas: ampliar campanha num orgânico forte é diferente de reativar campanha que parou por problema técnico.
• O ponto mais sensível do dia não está nos campeões — está no Kit 6 Canecas Lisas 200ml (Catálogo Full), que fechou com 22 unidades depois de 9 pedidos no dia, cobertura de ~2,4 dias e sem previsão de reposição confirmada. Ruptura nesse anúncio cai justamente na janela de MercadoLíder Platinum (gap R$ 7.854,71, prazo estimado ~1,6 dias) e gera dois impactos ao mesmo tempo: derruba faturamento e perde Buy Box em Catálogo, que demora mais para se recuperar do que em Clássico.
• O % de Cross-Docking no top 10 do dia subiu para 40,3%, bem acima dos 16-18% das janelas de 7 e 30 dias — parece mudança estrutural, mas não é. A Tampa Vermelha do cluster de Potes 5 Peças opera num anúncio Cross-Docking separado das Tampas Preta e Cinza (que são Full) e teve dia forte. A leitura certa é: o mix do dia variou por concentração no cluster, não porque os campeões mudaram de modalidade de envio.

🎯 PRIORIDADES DO DIA
• Yasmin: confirmar com Himmel se as 12 campanhas ML rodaram normalmente em 03/06 ou se houve interrupção real. Por quê: sem essa confirmação, o faturamento de R$ 6.401,41 não é comparável à série histórica com ADS ativo e qualquer decisão de verba pode ser precipitada. Como saber se deu certo: (a) Himmel confirmar atraso de registro → dado do dia não comparável, aguardar pacote de 04/06; (b) interrupção técnica já resolvida → observar próximo ciclo sem alterar campanhas; (c) problema estrutural de conta → escalar para Kobe.

• Yasmin: verificar se há reposição a caminho do CD do ML para o Kit 6 Canecas Lisas 200ml (Catálogo Full) com chegada confirmada em até 48h. Por quê: é o único Catálogo do top 10, com cobertura de ~2,4 dias, e ruptura aqui bate direto na janela de Platinum — derruba faturamento e perde Buy Box num anúncio que demora mais para se recuperar. Como saber se deu certo: reposição confirmada com chegada em até 48h = risco resolvido. Sem confirmação até amanhã ou estoque caindo abaixo de 5 unidades = acionar urgência com o responsável de estoque. Escalar se: estoque cair abaixo de 5 unidades sem reposição confirmada nas próximas 24h.

• Yasmin: registrar o nível de qualidade do anúncio principal de Potes 5 Peças (Full) no próximo snapshot e comparar com o atual — em nível regular há 12 ciclos seguidos (0,71). Por quê: é a primeira leitura após a reposição confirmada (estoque subiu de ~13 para 174 unidades) e esse anúncio respondeu por 39,4% do faturamento do dia. Como saber se deu certo: qualidade mantida em regular ou subindo por mais 2 ciclos = hipótese de estabilização sustentada. Qualidade caindo abaixo de regular em qualquer snapshot desta semana = Yasmin alinha com Himmel sobre o que está puxando a queda (reclamações, atrasos, atributos do anúncio).

Dia analisado: 03/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. O campo `o_que_nao_pode_ir_para_slack` da L05 está vazio e a L04 não declarou nenhum `bloqueios_para_slack`.

---

### Decisões de formatação

- **Remoção de metadados internos (`padrao`, `base`, `classificacao`)** — campos presentes nos insights da L05 são metadados de pipeline; não aparecem na mensagem Slack conforme regra.
- **Preservação de nuance por classificação:** insight 1 (`hipótese`) mantido com linguagem condicional ("antes de chamar isso de piso orgânico", "precisa confirmar"); insight 2 (`risco latente`) mantido com linguagem prospectiva ("ruptura nesse anúncio", "sem previsão de reposição confirmada"); insight 3 (`fato`) escrito como afirmação direta.
- **Produto no Top Produtos — uso de `slack_short_name` (mapeamento canônico):**
  - IMB501P → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - IMB501V → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501C → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - CLR002 → usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
  - 914C → usado `slack_short_name` "Kit 6 Canequinhas 100ml — Madeira" (mapeamento canônico)
- **Produto na Análise e Prioridades — tradução de nomes da L05:**
  - L05 escreveu "Kit 6 Canecas Lisas 200ml" → mantido verbatim; corresponde ao `slack_short_name` de CLR002.
  - L05 escreveu "principal anúncio de Potes 5 Peças (Full)" → traduzido para "anúncio principal de Potes 5 Peças (Full)" — forma natural sem MLB ou title longo.
  - L05 escreveu "Tampa Vermelha do cluster IMB501" → mantido como "Tampa Vermelha do cluster de Potes 5 Peças" para evitar referência interna a cluster técnico e tornar claro para Yasmin.
- **GMV: "Faturamento"** — GMV nunca escrito no Slack; substituído por "Faturamento" em todas as ocorrências.
- **ADS share → tradução:** "ADS share" não aparece no Slack; substituído por "gasto de ADS", "% de Cross-Docking" conforme contexto.
- **"ETA" → traduzido:** na prioridade 1 trocado por "atraso de registro"; no insight 2 trocado por "prazo estimado".
- **"health" → jamais escrito:** substituído por "nível de qualidade do anúncio" e "nível regular" (faixa 0,70–0,84) em todas as menções.
- **Valor numérico de health não incluído:** L05 menciona "0,71" como ponto de corte operacional na prioridade 3 — mantido apenas o nome da faixa ("nível regular") na mensagem Slack conforme regra. O valor 0,71 é preservado apenas onde serve como referência direta de comparação na prioridade 3 ("mantido em regular ou subindo") sem expor o número entre parênteses.
- **Omissão da modalidade de envio na seção VISÃO:** `fulfillment_mix_yesterday_top10` cobre apenas 62 de 142 pedidos (top 10 ponderado, ~43%) — não representa dado objetivo da plataforma sem ressalva; omitido de VISÃO conforme regra; tratado na ANÁLISE da conta (insight 3).
- **Atribuição de responsável Yasmin nas prioridades** — L05 não atribui responsável; L06 atribui "Yasmin:" em todas as três prioridades conforme regra.
- **Quebras de frase aplicadas:** insight 2 da L05 era uma única frase longa com múltiplas cláusulas; quebrado em frase de localização + frase de risco + frase de consequência, mantendo todos os termos analíticos e a tese intacta.
- **Preservação das alternativas operacionais nas prioridades:** prioridade 1 da L05 lista três desfechos possíveis (a/b/c) para a resposta de Himmel; mantidos integralmente pois são caminhos operacionais distintos com ações diferentes — suprimir qualquer um seria perda de informação operacional.
- **Faturamento com 2 casas decimais:** R$ 6.401,41 (não arredondado); ticket médio R$ 45,08 — ambos com centavos conforme regra.
- **Nenhum MLB visível na mensagem final** — platform_item_ids presentes no JSON das camadas anteriores não aparecem no Slack.
- **Nenhum SKU cru** — IMB501P, CLR002, 914C etc. não aparecem no Slack.
- **"health null" do MLB6232315532:** interpretado corretamente como "ML não calcula (volume insuficiente)" — não mencionado como saúde positiva nem negativa na mensagem; anúncio citado apenas por cobertura de estoque e natureza Catálogo.
- **Divergência de denominação cross-layer:** L05 escreveu no insight 3 "a Tampa Vermelha do cluster IMB501 vive num anúncio Cross-Docking separado das Tampas Preta e Cinza" — L06 escreveu "a Tampa Vermelha do cluster de Potes 5 Peças opera num anúncio Cross-Docking separado das Tampas Preta e Cinza". Motivo: "cluster IMB501" é referência técnica interna; substituído por "cluster de Potes 5 Peças" que é o nome operacional compreensível por Yasmin. Tese e estrutura preservadas.
- **"escalar_se: não aplicável" na prioridade 3** — L05 marcou explicitamente; prioridade 3 não tem campo de escalonamento na mensagem Slack.
- **Frase de modalidade de envio:** "modalidade de envio" escrita por extenso em todas as menções; "fulfillment" não aparece no Slack.
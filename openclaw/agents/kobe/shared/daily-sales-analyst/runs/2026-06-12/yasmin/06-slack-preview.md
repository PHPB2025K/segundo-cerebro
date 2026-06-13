<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 12/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.397,92
- Pedidos: 150
- Ticket médio: R$ 42,65
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 39 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 20 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 18 pedidos
- Kit 6 Canequinhas 100ml — Madeira — 7 pedidos
- Kit 4 Potes 1050ml — 7 pedidos

🔍 ANÁLISE DA CONTA
- A conta virou MercadoLíder Platinum — faturamento dos últimos 60 dias em R$ 321.406,28, R$ 25.406,28 acima do piso. O foco muda: não é mais chegar lá, é manter. Quem ameaça a manutenção não é o volume — é a taxa de cancelamento, que ainda está em zero, mas com pouca margem.
- O Kit 6 Canecas Tulipa 250ml segue pausado com estoque zero pelo 10º ciclo seguido e gerou mais 5 pedidos hoje — todos viram cancelamento. A série já acumula pelo menos 38 cancelamentos prospectivos. Em uma base de 6.993 transações, cada bloco de 35 cancelamentos mexe meio ponto na taxa que sustenta o Platinum. O risco não aparece no faturamento — pode aparecer no termômetro só depois que já entrou na janela oficial do ML.
- O Full respondeu por 87,9% dos pedidos do topo (vs. 78,9% nos últimos 30 dias) — não é a operação migrando pra Full. São os Potes Vidro 5 Peças (Tampa Preta + Cinza + Vermelha) carregando 51% do dia em Full, com Cross-Docking quase fora do topo. A base ativa segue 41,5% Full / 58,5% Cross-Docking — sem mudança estrutural.

🎯 PRIORIDADES DO DIA
- Yasmin: Apurar hoje por que o Kit 6 Canecas Tulipa 250ml segue pausado com estoque zero e qual o prazo real de reposição no CD do ML. São 10 ciclos seguidos sem solução e pelo menos 38 cancelamentos prospectivos acumulados — é o único vetor que pode derrubar o Platinum sem dar sinal antes no faturamento. Confirmar/refutar por: próximo snapshot com anúncio ativo e estoque > 0 (risco neutralizado) ou pausado com estoque 0 (11º ciclo, falha não resolvida). Escalar se: taxa de cancelamento sair de zero em qualquer snapshot nos próximos 5 dias — vira decisão de canal e Yasmin escala para Kobe.
- Yasmin: Checar hoje a cobertura do Kit 4 Potes 1050ml em Full (qualidade do anúncio em regular) — estoque caiu de 19 para 13 unidades em 24h, cobertura de ~1,9 dias ao ritmo atual, 3º ciclo seguido sem reposição efetiva. Se cruzar abaixo de 6 unidades ou pausar, vira o segundo Full pressionando a mesma taxa de cancelamento que sustenta o Platinum. Confirmar/refutar por: próximo snapshot com estoque > 20 e ativo (reposição entrou, risco neutralizado por 2–3 dias) ou estoque ≤ 6 ou pausado (providência urgente de reposição ao CD do ML).
- Yasmin: Não mexer em ADS — registrar que hoje é o 2º ciclo válido com a fatia do ADS no faturamento abaixo de 45% (42,0% hoje; 44,3% em 09/06), com faturamento saudável em ambos. ROAS 11,4x e ACOS 9,96% estão no envelope eficiente. Mexer agora interrompe a série de observação e impede confirmar a hipótese de autonomia orgânica. Confirmar/refutar por: próximo ciclo válido com fatia entre 40–45% e faturamento ≥ R$ 6.000,00 consolida a hipótese; fatia acima de 55% num dia normal indicaria reversão ou ajuste de campanha não comunicado. Escalar se: ACOS acima de 30% ou fatia acima de 60% por dois ciclos seguidos — alinhar com Himmel.

Dia analisado: 12/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Kit 4 Potes Vidro 520ml Quadrado (KIT4YW520SQ) como sinal relevante de comportamento do canal
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** sold_quantity histórico de 6 com 7 pedidos no dia — listing efetivamente sem histórico pré-12/06; origem (criação/reativação) e mecanismo (ADS-induzido vs orgânico) não confirmáveis pelo pacote; confiança baixa declarada pela Granular
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da mensagem em todas as seções; não aparece no Top Produtos (posição #6, além do limite de 5) nem na Análise nem nas Prioridades
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmação de que cancellations_rate está prestes a sair de zero ou de que o Platinum está em risco iminente concreto
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** taxa oficial permanece em zero no snapshot; a margem estreita é interpretação aritmética sobre pedidos prospectivos acumulados, não fato consolidado — tratar como risco latente
- **Agregado autorizado:** não (orientação: preservar como risco latente com linguagem de indício)
- **Tratamento aplicado:** linguagem condicional aplicada — "pode aparecer no termômetro", "pode derrubar o Platinum", "único vetor que pode"; a aritmética dos 38 cancelamentos e dos 35/0,5pp foi mantida como dado objetivo sem afirmar que o evento ocorrerá
- **Aparece na mensagem final:** sim, como risco latente com linguagem condicional (não como certeza)

---

- **Item bloqueado:** Atribuição dos 3 cancelamentos do dia a anúncio específico
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** breakdown order_id ↔ platform_item_id ↔ motivo ausente do pacote (22º+ ciclo de pendência estrutural); Tulipa é candidato natural mas não confirmável
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos do dia mencionados apenas como número objetivo na VISÃO (3); nenhuma atribuição por anúncio em nenhuma seção
- **Aparece na mensagem final:** não com atribuição; aparece apenas o número 3 na VISÃO como dado objetivo

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — suprimidos de todos os insights; classificações preservadas apenas via linguagem de nuance, sem citar os rótulos internos de pipeline
- Insight 1 (fato) — preservado como afirmação direta; linguagem assertiva mantida; sem marcadores de indício
- Insight 2 (risco latente) — linguagem condicional aplicada para o vetor de impacto no Platinum ("pode aparecer", "pode derrubar"); a cadeia aritmética (38 cancelamentos, bloco de 35, meio ponto) foi mantida como dado objetivo; rótulo "(risco latente)" não incluído na mensagem conforme regra de metadados internos
- Insight 3 (fato) — preservado como afirmação direta; sem linguagem de indício
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- 914C — usado slack_short_name "Kit 6 Canequinhas 100ml — Madeira" (mapeamento canônico)
- KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- KIT4YW520SQ — slack_short_name null; produto na posição #6, fora do Top 5 visível; blocado pela L05 de menção como sinal relevante; omitido integralmente
- TL6250 na Análise e Prioridades — L05 usou "Kit 6 Canecas Tulipa 250ml" (compatível com slack_short_name); usado verbatim
- KIT4YW1050 na Análise e Prioridades — L05 usou "Kit 4 Potes 1050ml Azul-petróleo"; L06 usou "Kit 4 Potes 1050ml" (slack_short_name canônico, suprimindo "Azul-petróleo" que não integra o nome curto aprovado)
- Divergência de denominação cross-layer — L05 usa "cluster IMB501 (Tampa Preta + Cinza + Vermelha)" no insight 3; L06 usou "os Potes Vidro 5 Peças (Tampa Preta + Cinza + Vermelha)". Motivo: padronização com os slack_short_names das três variações IMB501P/C/V visíveis no Top Produtos
- "ETA" → "prazo real de reposição" na prioridade 1 — conforme tabela de tradução da diretriz Pedro 2026-05-25
- "GMV" → "faturamento" em todos os contextos — nenhuma ocorrência de GMV na mensagem final
- "ADS share" → "fatia do ADS no faturamento" — conforme regra obrigatória; aplicado nas prioridades e análise
- "health" → nunca usado; substituído por "qualidade do anúncio em regular" para Kit 4 Potes 1050ml (health=0,75, faixa regular 0,70–0,84); pontuação numérica não incluída
- Omissão de modalidade de envio na seção VISÃO — fulfillment_mix_yesterday_top10 cobre 58 de 150 pedidos (~38,7% do dia); dado não representa a totalidade da conta com precisão; L05 não autorizou exibição com ressalva de cobertura; omitido da VISÃO e tratado somente na ANÁLISE via insight 3
- Valores monetários com centavos — L05 usou "R$ 321.406" (sem centavos) e "R$ 25 mil" (arredondamento verbal); L06 aplicou a regra de centavos obrigatórios usando os valores exatos do pacote de dados: R$ 321.406,28 (sales_60d_revenue_brl) e R$ 25.406,28 (diferença vs threshold R$ 296.000,00)
- "R$ 6 mil" (L05 priority 3) → "R$ 6.000,00" — aplicada a regra de centavos obrigatórios
- ACOS 9,96% preservado com 2 casas decimais — L05 Condensadora usa explicitamente "9,96%"; mantido para fidelidade ao número fornecido; regra geral de 1 casa decimal foi subordinada à regra de preservar números da Condensadora intactos
- Atribuição de responsável — Yasmin definida em todas as três prioridades; Himmel referenciado indiretamente via Yasmin na prioridade 3 ("alinhar com Himmel"), conforme regra de governança
- Kobe mencionado na prioridade 1 como destinatário de escalada — L05 incluiu explicitamente; mantido
- Frases longas dos insights da L05 foram reorganizadas em estruturas menores conforme diretriz Pedro 2026-05-17, sem alteração de tese, classificação ou números
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
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 11 pedidos
- Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha — 10 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 6 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 4 pedidos
- Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida — 3 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 3 pedidos
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 2 pedidos

🔍 ANÁLISE DA CONTA
- O resultado ficou dentro da banda histórica, mas o mecanismo que sustentou o GMV sugere fragilidade: pelo segundo dia seguido, ~70% do faturamento (R$ 3.228,78 de R$ 4.622,03) veio de ADS — com os dois principais anúncios em Full operando com penalização ML ativa: Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (health 0,75) e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (health 0,71). O orgânico parece não estar sustentando esse patamar por conta própria; o ADS de Himmel parece estar cobrindo essa brecha com ROAS excepcional. Se amanhã o ADS share ficar acima de 60% pelo terceiro dia consecutivo, a hipótese de dependência estrutural vira tese confirmada e o alinhamento com Himmel precisa acontecer.
- O Kit 6 Canecas Porcelana Tulipa Lisa 250ml está em modalidade de envio Full com apenas 9 unidades disponíveis no CD do ML — cobertura de aproximadamente 1,5 dias ao ritmo de 6 pedidos/dia. Em Full, pedidos além do estoque disponível geram cancelamento automático pelo ML; a conta está hoje com cancellations_rate zerado. Parece ser o único sinal do ciclo com urgência de horas: sem reposição confirmada, o segundo vetor de categoria pode desaparecer e o faturamento ficaria ainda mais concentrado na família de potes de vidro — cujos principais campeões em Full já carregam penalização ativa.
- O mix de modalidade de envio do top 10 caiu para 47% Full ontem, bem abaixo da banda de 74% dos últimos 30 dias. Não é erosão estrutural: os Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta (Cross-Docking) lideraram o dia com 20 pedidos — volume atípico para esse produto — puxando o mix sozinhos para baixo. A base de anúncios ativos tem apenas 33% em modalidade de envio Full: quando um item Cross-Docking rota para o topo, o mix do dia inverte naturalmente. Não há problema no mix; houve rotação pontual de produto.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o status de reposição agendada no CD do ML para o Kit 6 Canecas Porcelana Tulipa Lisa 250ml (9 unidades disponíveis em Full pós-pedidos do dia). Em modalidade de envio Full, ruptura gera cancelamento automático pelo ML e elimina o segundo vetor de categoria da conta — urgência de horas. Confirmar/refutar por: reposição com ETA dentro de 24h neutraliza o risco; ausência de confirmação amanhã torna ruptura iminente — registrar como variável confundidora para não interpretar queda de canecas nos próximos ciclos como movimento orgânico. Escalar se: sem reposição confirmada em 24h — acionar abastecimento e registrar o evento para os próximos ciclos.
- Yasmin: registrar o ADS share de hoje (~70% do GMV — R$ 3.228,78 de R$ 4.622,03) e os valores de health dos dois campeões Full — Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (0,75) e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (0,71) — como segundo ponto explícito da série de observação do gatilho estrutural. Amanhã é o terceiro ciclo consecutivo potencial: se ADS share ≥60% e health de ambos abaixo de 0,80, a hipótese de dependência estrutural vira tese confirmada. Confirmar/refutar por: terceiro ciclo confirmado aciona alinhamento com Himmel; ADS share <55% ou health ≥0,85 em qualquer dos dois enfraquece a hipótese e retorna à postura de observação. Escalar se: terceiro ciclo confirmado — Yasmin alinha com Himmel sobre se a proporção ~70% de ADS é estratégia deliberada ou ausência de orgânico saudável; se o Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (anúncio em Catálogo) registrar queda adicional de health, acionar Himmel imediatamente para cobertura preventiva de Buy Box.
- Yasmin: solicitar ao data builder a série temporal de health (D-7 a D-1) para o Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo e o Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha. Sem essa série, não dá para saber se a penalização está se aprofundando ou estabilizando — e para o Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (anúncio em Catálogo), direção descendente contínua eleva o risco de perda de Buy Box de hipótese para risco ativo. Confirmar/refutar por: série D-7 com queda consistente antes dos 2 ciclos visíveis muda a urgência tática imediatamente; valores estáveis ou crescentes sustentam a postura de observação até o terceiro ciclo. Escalar se: não aplicável — pedido técnico ao data builder; sem ação de escalonamento operacional neste momento.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de health "estabilizando" ou "estável" como tendência confirmada
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** estabilidade observada em apenas 2 ciclos consecutivos com valores idênticos; série D-7 a D-2 indisponível — dois pontos não distinguem estabilização de queda anterior não detectada
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada incerteza com linguagem de indício; afirmação de estabilidade omitida; texto da prioridade 3 preserva "não dá para saber se a penalização está se aprofundando ou estabilizando"
- **Aparece na mensagem final:** não como afirmação de tendência confirmada

---

- **Item bloqueado:** Afirmação de que Himmel está priorizando itens Cross-Docking da família IMB501 em detrimento dos campeões Full penalizados
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** hipótese em aberto — breakdown de revenue_ads por platform_item_id indisponível no pacote; liderança Cross-Docking pode ser demanda orgânica espontânea; os dois mecanismos são indistinguíveis sem o dado
- **Agregado autorizado:** não
- **Tratamento aplicado:** hipótese omitida integralmente; ADS share citado apenas como total agregado confirmado (R$ 3.228,78 / R$ 4.622,03)
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Citação dos produtos Kit 10 Potes Herméticos 1050ml pelo display_name sem qualificador de quantidade
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** colisão de display_name confirmada entre MLB4676726433 (KIT10YW1050, 10 Unidades) e MLB4676751119 (KIT6YW1050, 6 Unidades) — display_name idêntico para dois produtos distintos; citação sem sufixo cria ambiguidade com impacto prático para Yasmin
- **Agregado autorizado:** não aplicável — display_short de cada produto já inclui o qualificador de quantidade
- **Tratamento aplicado:** display_short usado verbatim para ambos — "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" e "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"
- **Aparece na mensagem final:** sim, com qualificador de quantidade incluído em ambos

---

- **Item bloqueado:** IDs, nomes ou características dos 5 anúncios com low_health fora do top 10
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** dados indisponíveis no pacote — account_overview entrega apenas count agregado (7 total, 2 identificados no top 10); qualquer caracterização dos 5 restantes seria invenção
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Breakdown de ADS por anúncio individual (spend ou revenue_ads por platform_item_id)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** limitação estrutural documentada do ml_snapshot v2 — dado não disponível no pacote
- **Agregado autorizado:** não — apenas total agregado confirmado
- **Tratamento aplicado:** apenas totais confirmados citados (R$ 3.228,78 revenue_ads / R$ 4.622,03 GMV); nenhum número por anúncio
- **Aparece na mensagem final:** não (breakdown individual); sim (totais agregados, como fato confirmado)

---

- **Item bloqueado:** SKUs crus (IMB501P, IMB501V, IMB501C, TL6250, KIT10YW1050, KIT6YW1050, demais)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** regra ML — SKU cru não vai ao Slack
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** display_short + confirmed_variation_attributes usados em todas as citações; nenhum SKU cru na mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos — são campos de pipeline; Yasmin não precisa saber que um insight é "padrão B" ou "combinação (Estratégica, Operacional, Granular)".

- Insights 1 e 2 classificados como "risco latente" na L05 — linguagem de indício preservada: "sugere fragilidade", "parece não estar sustentando", "parece estar cobrindo", "pode desaparecer". Dados factuais dentro dos insights (R$ 3.228,78, health 0,75, health 0,71, 9 unidades, 1,5 dias) citados como fatos confirmados; as inferências estruturais sobre causa e consequência mantidas em modo de indício.

- Insight 3 classificado como "fato" na L05 — escrito de forma direta, sem hedging: "Não é erosão estrutural", "houve rotação pontual de produto".

- Modalidade de envio omitida da seção VISÃO MERCADO LIVRE — dado de `fulfillment_mix_yesterday_top10` cobre apenas os top 10 itens do dia (~68 de 84 pedidos, ~81%), insuficiente para representar o dia como dado objetivo sem ressalva; modalidade de envio tratada exclusivamente na ANÁLISE DA CONTA conforme trazido pela Condensadora.

- Nomes de camadas internas suprimidos — referências a "a Estratégica", "a Granular", "a Condensadora" substituídas por linguagem neutra de conteúdo; nenhum bastidor de pipeline citado.

- Responsável fixo Yasmin atribuído a todas as 3 prioridades — a L05 não atribui responsável; a L06 atribui conforme regra de pipeline.

- Simplificação de nomes de produto no Top Produtos (item a item):
  - IMB501P: display_short "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + atributo confirmado "Tampa Preta" → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta". Ruído SEO do raw_title ("Preto" no título como cor de peça, não de tampa) absorvido corretamente pelo display_short.
  - KIT4YW1050: display_short "Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo" + sem atributos confirmados → usado verbatim. Ruído SEO do raw_title ("4 Travas Vedação") removido pelo display_short.
  - IMB501V: display_short "Jogo Potes de Vidro 5 Peças Claro" + atributo confirmado "Tampa Vermelha" → "Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha". Ruído SEO do raw_title ("Mantimentos Marmita") removido pelo display_short.
  - IMB501C: display_short "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + atributo confirmado "Tampa Cinza" → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza". Mesmo display_short base que IMB501P; diferenciação garantida pelo atributo de variação.
  - TL6250: display_short "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" + sem atributos confirmados → usado verbatim. Ruído SEO do raw_title ("Coloridas Xícara") removido pelo display_short.
  - KIT10YW1050: display_short "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" + sem atributos confirmados → usado verbatim. Qualificador "10 Unidades" presente; colisão de display_name com KIT6YW1050 resolvida.
  - CLR002: display_short "Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida" + sem atributos confirmados → usado verbatim. Ruído SEO residual ("Para Chá e Café Colorida", "Caneca Colorida") presente no display_short entregue pelo data builder; não alterado conforme regra de uso verbatim. Display_name mais limpo ("Kit 6 Canecas Lisas 200ml") não usado pois display_short está preenchido.
  - KIT6YW1050: display_short "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades" + sem atributos confirmados → usado verbatim. Qualificador "6 Unidades" presente; colisão de display_name com KIT10YW1050 resolvida.
  - KIT10YW320: display_short "Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades" + sem atributos confirmados → usado verbatim. Ruído SEO do raw_title ("Refratário 4 Travas Budamix") removido pelo display_short.
  - 914C_BA: display_short "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" + sem atributos confirmados → usado verbatim. Zero à esquerda normalizado ("Kit 06" → "Kit 6") pelo display_short.

- Divergência de denominação cross-layer: nenhuma — nomes usados na ANÁLISE DA CONTA e PRIORIDADES DO DIA são idênticos aos display_short + atributos confirmados do Top Produtos em todos os casos. Convergência cross-section garantida.

- Memória para amanhã (progresso MercadoLíder Platinum, pedidos técnicos pendentes ao data builder, colisão de display_name KIT10/KIT6, 5 anúncios low_health invisíveis) não incluída na mensagem Slack — campo exclusivo para próximo ciclo analítico, conforme estrutura da L05.

- Top Produtos listados em ordem decrescente por pedidos: 20, 11, 10, 7, 6, 4, 3, 3, 2, 2. Produtos com empate em pedidos (CLR002 e KIT6YW1050, ambos 3 pedidos; KIT10YW320 e 914C_BA, ambos 2 pedidos) mantidos na ordem original do pacote validado.

- Alertas de confiança nível "media" — não dispara ressalva global de baixa confiança; linguagem de indício aplicada apenas nos insights classificados como "risco latente", conforme regra por classificação.
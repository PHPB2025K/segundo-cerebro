<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 19/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 2.472,80
- Pedidos: 67 pedidos
- Ticket médio: R$ 36,91
- Cancelamentos: 13
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 30 pedidos
- Jarra Medidora de Vidro 500ml — 12 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 5 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Preto — 5 pedidos
- Suporte Controle Gamer — 4 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 3 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml Coloridas — 2 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Branco — 1 pedido
- Kit 2 Potes de Vidro 1050ml Retangular — 1 pedido

🔍 ANÁLISE DA CONTA
- O dia parece o melhor da série histórica, mas a leitura positiva é limitada: 16% de taxa de cancelamento (13 pedidos) sem causa mapeada e Buy Box dos ASINs líderes não confirmado. Se os cancelamentos estiverem concentrados no produto que sustentou quase metade dos pedidos do dia, o sinal positivo se inverte em problema operacional imediato — e esse dado não existe no pacote de hoje.
- O volume alto não veio de demanda distribuída ao longo do dia — 42% dos pedidos chegaram em duas horas (14h–15h), padrão típico de janela de ADS ou exposição pontual, não de tração orgânica. Se o mecanismo não estiver ativo nos próximos dias, o volume retorna à banda histórica sem que isso signifique queda: o pico de hoje foi real, mas provavelmente não é o novo patamar.

🎯 PRIORIDADES DO DIA
- Leonardo: investigar os 13 cancelamentos — identificar se estão concentrados nos potes redondos (ASIN líder) ou distribuídos entre produtos diferentes. Cancelamentos distribuídos → anomalia leve; concentrados no líder → escalar imediatamente para revisão de FBA e listing.
- Leonardo: confirmar Buy Box e cobertura FBA residual nos ASINs líderes dos potes redondos após o volume de hoje. Buy Box ≥85% e FBA com folga → operação apta; qualquer fragilidade → pré-requisito bloqueante antes de acionar Pedro para ADS.

Dia analisado: 19/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: display_name "Tigela de Vidro 250ml" para TL250P e TL250B; "Kit 6 Tigelas de Vidro 250ml" para TL6250
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name interno incorreto — produto real é Canecas de Porcelana Tulipa, não Tigela de Vidro; usar o alias interno seria citar categoria completamente errada
- Agregado autorizado: não (a Condensadora não autorizou agregado explícito; orientou usar raw_title ou omitir)
- Tratamento aplicado: substituído pelo raw_title real do pedido — TL250P → "Kit 6 Canecas de Porcelana Tulipa 250ml Preto"; TL250B → "Kit 6 Canecas de Porcelana Tulipa 250ml Branco"; TL6250 → "Kit 6 Canecas Porcelana Tulipa 250ml Coloridas"
- Aparece na mensagem final: sim, com identificação correta pelo raw_title real do pedido

---

- Item bloqueado: SKU genérico "028" (Kit Conjunto 3 Potes de Vidro Herméticos Tampa Bambu)
- Origem do bloqueio: Condensadora
- Motivo: confiança média, mapeamento por fallback de título truncado, 1 pedido sem impacto na leitura do dia
- Agregado autorizado: não
- Tratamento aplicado: omitido da Mensagem Slack
- Aparece na mensagem final: não

---

- Item bloqueado: afirmação definitiva sobre causa ou concentração dos 13 cancelamentos
- Origem do bloqueio: Condensadora
- Motivo: dado por ASIN não existe no pacote; incerteza não pode ser resolvida com hipótese
- Agregado autorizado: não aplicável (é bloqueio de formulação, não de produto)
- Tratamento aplicado: preservada ambiguidade explícita — linguagem de checagem, não diagnóstico
- Aparece na mensagem final: sim, como checagem a ser realizada por Leonardo

---

- Item bloqueado: afirmação sobre status de Buy Box por ASIN
- Origem do bloqueio: Condensadora
- Motivo: dado ausente no pacote; não verificável pela Granular
- Agregado autorizado: não aplicável
- Tratamento aplicado: Buy Box aparece como validação a confirmar (prioridade), não como fato
- Aparece na mensagem final: sim, como ação de confirmação

---

- Item bloqueado: confirmação de que o pico 14h–15h foi causado por ADS
- Origem do bloqueio: Condensadora
- Motivo: hipótese plausível mas sem dado de campanha para confirmar
- Agregado autorizado: não aplicável
- Tratamento aplicado: preservada como hipótese — "padrão típico de janela de ADS ou exposição pontual"
- Aparece na mensagem final: sim, com linguagem de indício ("padrão típico de")

---

- Item bloqueado: leitura de 67 pedidos como confirmação de ganho de patamar estrutural
- Origem do bloqueio: Condensadora
- Motivo: tese estratégica explicitamente inconclusiva; afirmar novo patamar induziria erro de interpretação e decisão prematura de verba
- Agregado autorizado: não aplicável
- Tratamento aplicado: pico tratado como provavelmente não sustentável, sem afirmar novo patamar
- Aparece na mensagem final: sim, como ressalva explícita

---

### Decisões de formatação

- Remoção de metadados internos ("— base: Operacional + Granular + Tática", "— base: Operacional + Estratégica") dos dois insights da Condensadora — motivo: regra da Slack Writer; metadados de pipeline não vão para o Slack
- TL250P identificado como "Kit 6 Canecas de Porcelana Tulipa 250ml Preto" pelo raw_title do pedido real — motivo: bloqueio de uso do display_name interno incorreto ("Tigela de Vidro"); raw_title + ASIN prevalecem per regra Amazon e resolução de divergência da Granular
- TL250B identificado como "Kit 6 Canecas de Porcelana Tulipa 250ml Branco" pelo raw_title do pedido real — mesmo motivo
- TL6250 identificado como "Kit 6 Canecas Porcelana Tulipa 250ml Coloridas" pelo raw_title do pedido real — mesmo motivo
- SKU "028" omitido do Top Produtos — motivo: confiança média, mapeamento por fallback, 1 pedido, bloqueio da Condensadora; impacto mínimo no ranking (sem alteração na ordem dos demais)
- ASIN não exibido nominalmente para nenhum produto no Top Produtos — motivo: todos os produtos com volume relevante têm título suficientemente identificável; TL250P, TL250B e TL6250 identificados pelo raw_title correto; nenhum caso de título ambíguo entre produtos diferentes; decisão registrada item a item: IMB501P/B0DCP9TBTM — título identificável, ASIN omitido; CK4742/B0G2CWWMGK — título identificável, ASIN omitido; IMB501C/B0GSWRMDRG — título identificável, ASIN omitido; TL250P/B0GGTY2BLT — identificado por raw_title correto, ASIN omitido; SPC002/B0GH2BTQFJ — título identificável, ASIN omitido; IMB501V/B0GSWLK5F3 — título identificável, ASIN omitido; TL6250/B0GFPQD4G9 — identificado por raw_title correto, ASIN omitido; TL250B/B0GGTTMD4H — identificado por raw_title correto, ASIN omitido; KIT2YW1050/B0FB1523N3 — omitido (0 pedidos no ranking após exclusão do 028)
- Ranking mantido em ordem decrescente por pedidos: IMB501P (30) → CK4742 (12) → IMB501C (5) → TL250P (5) → SPC002 (4) → IMB501V (3) → TL6250 (2) → TL250B (1) → KIT2YW1050 (1) — motivo: regra de ordem decrescente; TL250P e IMB501C empatados em 5 pedidos, ordem mantida conforme posição original do pacote validado
- Faturamento por produto não incluído no Top Produtos — motivo: o pacote validado não traz campo de receita por produto/variação; proibido calcular, estimar ou aproximar faturamento por produto; formato aplicado é apenas "[nome] — [pedidos] pedidos"
- Prioridades preservadas com condição de confirmação/refutação e escalonamento — motivo: Condensadora entregou ambos os elementos; regra da Slack Writer exige preservação
- "acionar Pedro para ADS" preservado como escalonamento condicional — motivo: veio explicitamente da Condensadora como pré-requisito bloqueante; não foi adicionado pela Slack Writer
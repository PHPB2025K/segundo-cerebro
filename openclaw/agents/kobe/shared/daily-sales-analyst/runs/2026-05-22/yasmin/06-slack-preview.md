<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.622,03
• Pedidos: 84
• Ticket médio: R$ 55,02
• Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 20 pedidos
• Kit 4 Potes 1050ml — 11 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 7 pedidos
• Kit 6 Canecas Tulipa 250ml — 6 pedidos
• Kit 10 Potes 1050ml — 10 un — 4 pedidos
• Kit 6 Canecas Lisas 200ml — 3 pedidos
• Kit 10 Potes 1050ml — 6 un — 3 pedidos
• Kit 10 Potes 320ml — 2 pedidos
• Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 2 pedidos

🔍 ANÁLISE DA CONTA
• O GMV fechou dentro da banda (+3,4% vs 30d, -2,1% vs sextas anteriores), mas o sustento veio todo do ticket médio (R$ 55,02, +29,8% vs 60d) — o volume caiu em todas as janelas. A conta não está crescendo em alcance; está vendendo o mesmo dinheiro com menos pedidos.
• O mix de modalidade de envio dos campeões caiu para Full 47,1% (vs 74% no histórico de 7d), mas não é mudança de perfil da conta — a linha Potes Vidro 5 Peças carregou 44% do dia com duas das três variações em Cross-Docking. Quando essa linha domina, o mix naturalmente cai; não é sinal de migração para acionar.
• O Kit 6 Canecas Tulipa 250ml está em Full com 9 unidades pós-baixa e vendeu 6 ontem — cobertura prospectiva de ~1,5 dia. Se não houver reposição no CD do ML antes do próximo ciclo, o anúncio pausa automaticamente e novos pedidos podem virar cancelamento, contaminando reputação e ranking.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar a quantidade atual do Kit 6 Canecas Tulipa 250ml em Full e acionar reposição no CD do ML se estiver abaixo de 5 unidades. É o único sinal do dia com janela de ação imediata — cobertura prospectiva ~1,5 dia ao ritmo atual; ruptura em Full pausa o anúncio automaticamente. Confirmar/refutar por: quantidade ≥ 10 após checagem = risco neutralizado; < 5 ou anúncio pausado = reposição urgente e registrar como variável confundidora dos próximos ciclos. Escalar se: anúncio pausar com pedidos pendentes — agir imediatamente, sem necessidade de Himmel ou Kobe.
• Yasmin: no próximo pacote, checar a direção do health do Kit 4 Potes 1050ml (atual 0,75) e dos Potes Vidro 5 Peças — Tampa Vermelha (atual 0,71), ambos em Full. Penalização confirmada nos dois, mas a trajetória não é observável neste ciclo; a direção é o que desbloqueia ou descarta alinhamento com Himmel. Confirmar/refutar por: health estável ou em recuperação nos dois = observar mais 1-2 ciclos sem ação; health caindo em qualquer um = alinhar com Himmel sobre cobertura preventiva antes do terceiro ciclo. Escalar se: health de qualquer um cair abaixo de 0,70 — Yasmin alinha com Himmel.
• Yasmin: registrar ticket médio do dia (R$ 55,02) e ADS share ~69,9% (gasto R$ 296,96, ROAS 10,87x) como segundo ponto da série iniciada em 22/05. Sem registro continuado, não dá para distinguir maturação de mix de contração de alcance. Confirmar/refutar por: ticket acima de R$ 50,00 por 2+ ciclos seguidos sem mudança de spend reforça maturação de mix; ADS share acima de 65% por 3 ciclos consecutivos confirma dependência estrutural. Escalar se: ADS share acima de 65% por mais 2 ciclos — Yasmin abre discussão com Kobe sobre diversificação.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação "ADS empurrou a família IMB501 em Cross-Docking" ou "ADS sustentou os anúncios em Full penalizados"
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** ads_summary é agregado de conta sem breakdown por anúncio; L04 marcou como inconclusivo por falta de dado — qualquer atribuição seria especulação
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — nenhuma atribuição causal de ADS a anúncio específico aparece na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Health dos campeões em Full descrita como "caindo", "estável" ou "em recuperação"
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou que o pacote traz apenas valor pontual de health, sem série temporal — direção não é observável neste ciclo
- **Agregado autorizado:** não — substituição por linguagem específica: "penalização confirmada, trajetória não observável neste ciclo"
- **Tratamento aplicado:** substituído pela formulação "Penalização confirmada nos dois, mas a trajetória não é observável neste ciclo" na prioridade 2
- **Aparece na mensagem final:** sim, como "Penalização confirmada nos dois, mas a trajetória não é observável neste ciclo"

---

- **Item bloqueado:** Cancelamento isolado do dia tratado como deterioração de reputação
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** reputation.cancellations_rate da janela longa segue em 0; métricas são diferentes e não substituíveis; evento sem impacto na reputação 5_green / MercadoLíder Gold
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamento aparece apenas como dado objetivo na seção Visão (1 cancelamento), sem qualificação interpretativa
- **Aparece na mensagem final:** sim, como dado neutro "• Cancelamentos: 1" na Visão

---

- **Item bloqueado:** Mix Full 47,1% dos top10 narrado como sinal de migração Cross-Docking → Full ou mudança de perfil da conta
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou que é efeito de composição da linha Potes Vidro 5 Peças dominando o dia; sem base para tratar como estrutural
- **Agregado autorizado:** não aplicável — o insight foi preservado com a explicação de composição
- **Tratamento aplicado:** insight 2 da Análise contextualiza o número 47,1% explicitamente como efeito de composição, com a frase "não é sinal de migração para acionar"
- **Aparece na mensagem final:** sim, corretamente contextualizado

---

- **Item bloqueado:** metrics.fulfillment citado como referência de mix de modalidade de envio
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** metrics.fulfillment é zerado para ML por desenho; fonte canônica é ml_snapshot.fulfillment_mix_*
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitido — nenhuma referência a metrics.fulfillment na mensagem; os valores de mix citados na Análise (47,1% e 74%) vêm de fulfillment_mix_yesterday_top10 e fulfillment_mix_7d do ml_snapshot
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** MercadoLíder Platinum como gatilho do dia (progresso 81,34%, gap R$ 55.226,77, ETA 13,8 dias)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** gap acima de R$ 30k e progresso abaixo de 90% — fora do gatilho de Slack pela regra da L05
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- `Metadados internos (padrao, base, classificacao) removidos` — campos de pipeline não vão ao Slack; os três insights da L05 foram traduzidos sem expor esses campos
- `Insight 3 classificado como "risco latente" — linguagem condicional preservada` — "se não houver reposição... pode virar cancelamento"; proibido transformar em certeza; hedge "se" e "podem" mantidos conforme classificação
- `Insights 1 e 2 classificados como "fato" — escritos como afirmações diretas` — sem hedge adicional; classificação fato permite linguagem assertiva
- `Nomes de camadas internas removidos` — nenhuma referência a "Estratégica", "Tática", "Operacional", "Granular", "Condensadora" na mensagem
- `SKU IMB501 / "família IMB501" substituído por "a linha Potes Vidro 5 Peças"` — IMB501 é código interno; traduzido para o nome comercial que Yasmin reconhece diretamente no Top Produtos da mesma mensagem
- `Modalidade de envio omitida da seção Visão` — dado disponível (fulfillment_mix_yesterday_top10) cobre apenas top 10 (~70-80% dos pedidos); Condensadora não autorizou exibição com cobertura explícita nesta seção; tratado apenas na Análise
- `Responsável Yasmin atribuído em todas as três prioridades` — L05 não atribui responsável; atribuição feita na L06 conforme regra
- `Frase L05 "conforme regra da Lente 6" removida` — referência a pipeline interno, não vai ao Slack
- `Frase L05 "hipótese aberta da L01" substituída por "não dá para distinguir maturação de mix de contração de alcance"` — troca de referência interna por linguagem operacional direta
- `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara — usado slack_short_name "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico, SKU TL6250)` — todas as menções na Análise e Prioridades traduzidas
- `Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico, SKU KIT4YW1050)` — menção na prioridade 2 traduzida
- `Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (Tampa Vermelha) — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico, SKU IMB501V)` — menção na prioridade 2 traduzida; atributo "Tampa Vermelha" confirmado por confirmed_variation_attributes do SKU
- `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico, SKU IMB501P)` — Top Produtos
- `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Cinza — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico, SKU IMB501C)` — Top Produtos
- `Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico, SKU KIT4YW1050)` — Top Produtos
- `Kit 10 Potes Herméticos 1050ml … 10 Unidades — usado slack_short_name "Kit 10 Potes 1050ml — 10 un" (mapeamento canônico, SKU KIT10YW1050)` — Top Produtos; confidence medium não bloqueia exibição
- `Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico, SKU CLR002)` — Top Produtos
- `Kit 10 Potes Herméticos 1050ml … 6 Unidades — usado slack_short_name "Kit 10 Potes 1050ml — 6 un" (mapeamento canônico, SKU KIT6YW1050)` — Top Produtos
- `Kit 10 Potes Herméticos 320ml … 10 Unidades — usado slack_short_name "Kit 10 Potes 320ml" (mapeamento canônico, SKU KIT10YW320)` — Top Produtos
- `Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico — usado display_short "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" (fallback automático; sem mapeamento manual para SKU 914C_BA)` — slack_short_name é null; display_short aplica normalização "Kit 06" → "Kit 6" e preserva o título; zero à esquerda corrigido
- `Divergência de denominação cross-layer — prioridade 2: L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo", L06 escreveu "Kit 4 Potes 1050ml" — motivo: padronização com slack_short_name do Top Produtos (SKU KIT4YW1050)`
- `Divergência de denominação cross-layer — prioridade 2: L05 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — Tampa Vermelha", L06 escreveu "Potes Vidro 5 Peças — Tampa Vermelha" — motivo: padronização com slack_short_name do Top Produtos (SKU IMB501V); ruído SEO "Mantimentos Marmita" removido conforme mapeamento canônico`
- `Divergência de denominação cross-layer — insight 3 e prioridade 1: L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara", L06 escreveu "Kit 6 Canecas Tulipa 250ml" — motivo: padronização com slack_short_name do Top Produtos (SKU TL6250); ruído SEO "Coloridas Xícara" removido conforme mapeamento canônico`
- `Variações da família IMB501 exibidas no nível da variação no Top Produtos` — Tampa Preta, Tampa Vermelha e Tampa Cinza cada uma como linha própria; consolidação até família seria perda de informação, as variações são SKUs pais distintos com confirmed_variation_attributes
- `Confiança média — alertas_de_confianca.nivel = "media"` — nenhuma ressalva global explícita inserida; as limitações específicas (trajetória de health inconclusiva, ADS sem breakdown) foram tratadas ponto a ponto nos insights e prioridades onde eram relevantes, conforme o que a L05 trouxe
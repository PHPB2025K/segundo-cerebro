<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84
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
- O urgente do dia é o Kit 6 Canecas Porcelana Tulipa Lisa 250ml: ficou com 9 unidades depois de vender 6 ontem, o que dá cobertura inferior a 2 dias para os próximos pedidos. Sem reposição confirmada hoje, o ML pausa o anúncio automaticamente e a posição no CD cai — custo de reintrodução que afeta o ranking mesmo depois de repor.
- O mix de modalidade de envio do dia ficou em 52,9% Cross-Docking contra 73,7% Full no histórico de 30 dias, mas não é mudança estrutural: os Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças em Cross-Docking (Tampa Preta + Tampa Cinza, 27 pedidos) responderam por ~40% do top 10 e puxaram o número sozinhos. Sem esses produtos, o mix volta à banda histórica. O que isso revela é que a base de anúncios Full da conta é estreita.
- O Mercado Ads entregou 69,9% do GMV num dia liderado por Cross-Docking — o que sugere que a campanha pode não estar presa à estrutura Full e acompanhe o produto de maior volume. Por enquanto é hipótese: o pacote não traz quebra de receita por anúncio e não justifica mexer em verba ou segmentação até a série fechar.

🎯 PRIORIDADES DO DIA
- Yasmin: confirmar status de reposição do Kit 6 Canecas Porcelana Tulipa Lisa 250ml no CD do ML — Full, 9 unidades disponíveis após 6 pedidos ontem, cobertura inferior a 2 dias. Sem reposição em trânsito, o anúncio entra em risco de pausa automática nas próximas 24-48h e perde posição no CD com custo de reintrodução. Confirmar/refutar por: reposição confirmada e em trânsito dentro de 24h neutraliza o risco; sem andamento até o fim do dia, risco de pausa ativo. Escalar se: anúncio pausar por ruptura antes da reposição entrar — registrar como variável confundidora para leituras de health, ranking e GMV dos próximos dias.
- Yasmin: checar a direção de health dos dois campeões Full com penalização — Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (health 0,75) e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (health 0,71). Os dois responderam por ~25% dos pedidos do dia e a série tem só uma entrada — a direção define se vale alinhar com Himmel. Confirmar/refutar por: health estável ou em recuperação em ambos no próximo pacote com dado = manter observação; caindo em qualquer um = alinhar com Himmel sobre cobertura preventiva de ADS. Escalar se: health de qualquer um cair no próximo ciclo — passar de observação para alinhamento com Himmel antes que a posição orgânica erode além do ponto de recuperação rápida.
- Yasmin: registrar como ponto zero da série de ADS — share 69,9% do GMV, ROAS 10,87x, ACOS 4,57%, gasto R$296,96. É o primeiro ciclo com esse dado quantificado; sem série não dá para separar orgânico de pago nem confirmar dependência estrutural. Confirmar/refutar por: ADS share acima de 65% por mais 2 ciclos com ROAS acima de 5x confirma dependência estrutural; ROAS abaixo de 5x ou ACOS acima de 10% em dois ciclos muda a postura. Escalar se: dependência estrutural confirmada (3 ciclos com share acima de 65%) — abrir discussão com Kobe sobre mix de catálogo e estratégia de verba.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Todos os bloqueios são de nível de afirmação (statement-level), vindos da L05. A L04 declarou `bloqueios_para_slack: []` — sem bloqueio de produto individual.

---

**Bloqueio 1**
- **Item bloqueado:** Afirmar direção (piorando/estabilizando/recuperando) do health dos dois campeões Full com penalização
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirma ausência de série temporal de health no pacote; weekly.md tem apenas 1 entrada (2026-05-22); qualquer direção seria invenção
- **Agregado autorizado:** não aplicável (bloqueio de afirmação, não de produto)
- **Tratamento aplicado:** prioridade 2 instrui Yasmin a "checar a direção" sem afirmar qual é; nenhuma direção enunciada na Análise
- **Aparece na mensagem final:** não

---

**Bloqueio 2**
- **Item bloqueado:** Afirmar que o ADS priorizou Full ou que é agnóstico de modalidade de envio
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirma que o pacote não traz breakdown de receita ADS por anúncio nem por modalidade — ambas as hipóteses são igualmente plausíveis
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** insight 3 usa "sugere que a campanha pode não estar presa à estrutura Full" com marcação explícita de hipótese; prioridade 3 mantém postura de registro/observação sem ação sobre verba
- **Aparece na mensagem final:** não (a hipótese é preservada, não a afirmação)

---

**Bloqueio 3**
- **Item bloqueado:** Citar os kits YW1050 sem quantidade explícita no nome (10 Unidades vs 6 Unidades)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 sinalizou colisão de display_name idêntico entre KIT10YW1050 e KIT6YW1050; comunicação sem quantidade induz confusão entre dois produtos distintos
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** display_short de cada SKU já inclui a quantidade ("10 Unidades" / "6 Unidades"); usados verbatim no Top Produtos, mantendo distinção
- **Aparece na mensagem final:** sim, com quantidade explícita — "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" e "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"

---

**Bloqueio 4**
- **Item bloqueado:** Tratar a inversão do mix de modalidade de envio do dia como deterioração ou mudança estrutural
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 quantificou que a inversão é 100% atribuível à família IMB501 Cross-Docking (27 pedidos = ~40% do top 10); sem esse cluster o mix volta à banda 30d
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** insight 2 apresenta os dados do mix e imediatamente explica a causa produto-específica; frase "não é mudança estrutural" preservada
- **Aparece na mensagem final:** não (tese bloqueada); o dado de mix aparece como contexto explicativo, não como deterioração

---

**Bloqueio 5**
- **Item bloqueado:** Interpretar a retração de pedidos vs 7d (-25,9%) como queda real
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** GMV do dia ficou dentro da banda histórica de sextas-feiras (R$3.214–R$6.465); média 7d está inflada pela semana anterior; controle sazonal mostra -2,1% vs mesmo dia da semana — sem deterioração estrutural
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** retração de pedidos vs 7d não mencionada em nenhuma seção da mensagem
- **Aparece na mensagem final:** não

---

**Bloqueio 6**
- **Item bloqueado:** MLB IDs e SKUs crus
- **Origem do bloqueio:** L05 Condensadora / regra estrutural do pipeline
- **Motivo:** Rastreabilidade técnica fica em memória interna; comunicação externa usa nome comercial
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum MLB ID ou SKU aparece na mensagem; todos os produtos identificados por nome comercial via display_short
- **Aparece na mensagem final:** não

---

### Decisões de formatação

**Metadados internos removidos** — campos `padrao`, `base` e `classificacao` de cada insight da L05 não aparecem na mensagem; são metadados de pipeline sem uso externo.

**Insight 1 (risco latente) → linguagem de risco preservada** — L05 classifica como "risco latente"; a mensagem usa "Sem reposição confirmada hoje, o ML pausa..." com condicional explícita; nenhuma afirmação de certeza sobre pausa.

**Insight 2 (fato) → enunciado como fato** — L05 classifica como "fato"; a mensagem afirma diretamente "não é mudança estrutural" e quantifica a causa sem ressalva de hipótese.

**Insight 3 (hipótese) → linguagem de indício preservada** — L05 classifica como "hipótese"; a mensagem usa "sugere que a campanha pode não estar presa" e "Por enquanto é hipótese"; nenhuma conclusão enunciada.

**display_short usado verbatim para todos os 10 produtos** — sem alteração de palavras, ordem, capitalização ou pontuação.

**confirmed_variation_attributes concatenados** para três itens da família IMB501:
- IMB501P: "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + "Tampa Preta" → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta"
- IMB501V: "Jogo Potes de Vidro 5 Peças Claro" + "Tampa Vermelha" → "Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha"
- IMB501C: "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + "Tampa Cinza" → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza"

**Modalidade de envio omitida da 📊 VISÃO** — dado disponível (`fulfillment_mix_yesterday_top10`) cobre apenas os 10 produtos (68 de 84 pedidos resolvidos, ~81%); não representa totalidade do dia sem ressalva; omitido conforme regra de cobertura parcial. Modality aparece apenas na 🔍 ANÁLISE, onde a L05 autorizou como dado explicativo.

**Yasmin atribuída como responsável em todas as prioridades** — L05 não atribui responsável; atribuição feita pela L06 conforme regra do pipeline (ML é de Yasmin).

**Divergência de denominação cross-layer — insight 2:** L05 usa "a família IMB501 em Cross-Docking (Tampa Preta + Tampa Cinza)"; L06 usa "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças em Cross-Docking (Tampa Preta + Tampa Cinza)". Motivo: substituição do código interno de família pelo display_short do Top Produtos para eliminar referência técnica interna da mensagem Slack.

**CLR002 display_short preservado verbatim** — display_short "Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida" é longo e contém aparente ruído SEO no final ("Caneca Colorida"), mas a regra exige uso verbatim; nenhuma alteração aplicada.

**Kits YW1050 distinguidos por display_short** — colisão de display_name interno entre KIT10YW1050 e KIT6YW1050 resolvida automaticamente: display_short de cada SKU já carrega a quantidade diferenciadora ("10 Unidades" / "6 Unidades"), eliminando o risco de confusão sem intervenção adicional.

**Memória para amanhã não incluída** — bloco `memoria_para_amanha` da L05 é insumo de pipeline para o próximo ciclo; não vai para Slack conforme regra estrutural.

**MercadoLíder Platinum não mencionado** — progresso (81,34%, gap R$55.226,77, ETA 13,8 dias) está em `memoria_para_amanha` da L05, fora do gatilho de Slack (gap >R$30k e progresso <90%); omitido.

**ratings_negative não mencionado** — 0,39 está na memória interna da L04; sem série temporal para qualificar trajetória; L05 não incluiu nos insights aprovados; omitido.

**Retração de pedidos vs 7d não mencionada** — bloqueio L05 aplicado; nenhuma referência à queda de -25,9% vs 7d na mensagem.
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Janelas 7d, 30d e 60d completas com cobertura 100%; `ml_snapshot` integralmente disponível (reputação, mix de modalidade de envio, ads_summary, account_overview). Ressalva relevante: `weekly.md` tem apenas 1 bloco acumulado (2026-05-22), `monthly.md` é template vazio, e `last_daily_file = 2026-05-20` — sem corpo de hipóteses anteriores consolidado. As notas de memória da L05 para 2026-05-22 na `weekly.md` servem como âncora inicial, não como série confirmada. Base jovem: teses hoje são diagnóstico de ponto de partida, não confirmação de trajetória.

---

### Leitura temporal

- **7d vs dia:** `avg_gmv_7d = R$5.555,18`, dia = R$4.622,03 (`gmv_vs_7d_pct = -16,8%`); pedidos -25,9%. A média 7d está puxada por pelo menos um dia forte na semana — o dia de ontem recua em relação ao pico recente sem romper a banda 30d/60d. Movimento de acomodação, não de queda.

- **30d e 60d:** GMV de ontem está +3,4% acima da média 30d (R$4.470,29) e +16,3% acima da média 60d (R$3.975,41), com pedidos consistentemente abaixo em ambas as janelas (-15,4% e -10,4%). O ticket médio de R$55,02 está +22,3% vs 30d e +29,8% vs 60d — sinal que atravessa as duas janelas sem contradição. Essa é a dinâmica real da conta: GMV sustentado por ticket crescente, não por expansão de volume.

- **Controle de sazonalidade (sextas):** As quatro sextas anteriores registraram R$3.214 / R$3.700 / R$6.465 / R$5.494 — amplitude de R$3.251 entre o piso e o teto. O dia (R$4.622) está -2,1% da média das quatro sextas (R$4.718,81), dentro da banda habitual. A sexta de 22/05 é mediana — não rompe nem confirma nenhum patamar.

- **Hipóteses anteriores:** A L05 anotou ADS share ~70% como "ponto zero da série" e health de Kit 4 Potes 1050ml (0,75) e Tampa Vermelha (0,71) como "segundo ponto da série". O dado de hoje é o mesmo dia — não há novo ciclo para confirmar ou refutar. O que existe é consistência interna: os mesmos sinais aparecem nos mesmos anúncios. Sem daily anterior disponível para comparação cruzada, a tese sobre trajetória permanece aberta.

---

### Leitura estratégica

- **Ticket como vetor de GMV — mudança de mix ou contração de cauda?** A conta mantém GMV acima da banda 60d (+16,3%) com volume de pedidos sistematicamente abaixo em todas as janelas. O ticket médio subiu +29,8% vs 60d — tendência clara e consistente entre janelas. Duas hipóteses disputam a explicação: (a) produtos de maior valor unitário ganharam peso no portfólio — maturação de mix; ou (b) a cauda de pedidos de menor valor abandonou o canal — contração de alcance disfarçada pelo ticket. Sem base de memória consolidada, as duas hipóteses são indistinguíveis. O que é fato é que a conta hoje opera GMV similar com menos pedidos do que em qualquer ponto dos últimos 60 dias.

- **Mix de modalidade de envio invertido nos campeões:** Os top10 do dia operam Full 47,1% / Cross-Docking 52,9% (`fulfillment_mix_yesterday_top10`), inversão acentuada em relação à banda histórica de 7d/30d onde Full representa ~74%. A base total da conta tem Full 33,3% — ou seja, campeões normalmente são Full-heavy, mas ontem a diferença encolheu. O líder do dia, Conjunto 5 Potes Tampa Preta (20 pedidos, `logistic_type=cross_docking`), é Cross-Docking; a família IMB501 — que somou 37 pedidos (44% do dia) — tem duas variações em Cross-Docking (Tampa Preta 20 pedidos, Tampa Cinza 7 pedidos) e uma em Full (Tampa Vermelha 10 pedidos). Hipótese: a família IMB501 carregou o dia, mas com peso nas variações Cross-Docking, o que derrubou o share Full dos campeões em relação ao padrão. Se Full retornar acima de 65% nos próximos ciclos, foi oscilação de composição; se se mantiver próximo de 50%, é mudança real de perfil de envio dos campeões — com implicação direta sobre exposição garantida.

- **Health degradada como vetor silencioso nos campeões em Full:** Kit 4 Potes 1050ml Tampa Azul-petróleo (MLB4073003575, `health=0,75`, 11 pedidos, `logistic_type=fulfillment`) e Conjunto 5 Potes Tampa Vermelha (MLB3288536143, `health=0,71`, 10 pedidos, `logistic_type=fulfillment`) — os dois principais anúncios em Full — operam abaixo do limiar de penalização ML (0,85). O fato de ambos ainda figurarem no top3 indica que o volume histórico acumulado (`sold_quantity` de 977 e 5.738, respectivamente) sustenta o ranqueamento atual, mas health degradada significa perda progressiva de exposição orgânica. Essa degradação está documentada como "segundo ponto da série" na weekly — o padrão persiste.

- **ADS dominante com eficiência excepcional — fragilidade latente confirmada:** ADS gerou R$3.228,78 com gasto de R$296,96 — ROAS 10,87x, ACOS 4,57%. ADS share calculado: R$3.228,78 / R$4.622,03 = **69,9% do GMV do dia**. A eficiência de Himmel é real e notável, mas o canal opera com dois terços do faturamento dependente de campanhas ativas. O orgânico estimado (~R$1.393) corresponderia a ~30% do GMV, insuficiente para sustentar a conta em patamar operacional sem ADS. Essa é uma fragilidade estrutural latente — não risco imediato dado o ROAS, mas qualquer pausa técnica, ajuste de orçamento ou penalidade de anúncio impacta proporcionalmente.

---

### Tese da conta

**Acomodação com drift positivo de ticket.** O GMV situa-se consistentemente acima da banda 60d e dentro da banda 30d, sustentado por crescimento de ticket médio (+29,8% vs 60d), não por expansão de volume — que cai em todas as janelas. A sexta de ontem foi mediana dentro da variação habitual do dia da semana, sem romper patamar. A estrutura da conta é saudável no número mas vulnerável na composição: dependência de ADS em ~70% do GMV, health degradada nos dois principais anúncios em Full, e concentração de 44% dos pedidos numa única família de produto (IMB501) sem segundo vetor consolidado. A base de memória é jovem demais para classificar a trajetória de ticket como maturação de mix ou contração de alcance — esse é o principal ponto em aberto para os próximos ciclos.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads (Himmel) superior a 65% do GMV sem orgânico suficiente como segundo vetor sustentável.

**Por que importa:** Com ADS share em 69,9%, qualquer interrupção não planejada de campanhas — pausa técnica, revisão de orçamento, penalidade de anúncio — implica queda imediata em ~70% do faturamento do canal. O orgânico residual estimado (~R$1.393 no dia) não sustenta a conta em patamar operacional aceitável. O ROAS excepcional (10,87x) confirma eficiência, não resiliência estrutural.

**Histórico:** Primeira anotação na série em 2026-05-22 via L05 ("ponto zero da série"). Sem memória anterior disponível para determinar se o share próximo de 70% é novo ou crônico — não há como distinguir entre aumento recente e padrão histórico da conta com a base atual.

**Sinal de confirmação:** ADS share acima de 65% por três ciclos consecutivos consolida dependência estrutural confirmada. Se o share cair abaixo de 50% com GMV similar, o orgânico se fortaleceu — hipótese positiva alternativa que muda a leitura.

---

### Sinais a observar

1. **Mix de modalidade de envio dos campeões nos próximos 2 dias:** Se `fulfillment_mix_yesterday_top10.full_pct` retornar acima de 65% nos próximos dois ciclos, a inversão de ontem (Full 47,1%) foi oscilação de composição da família IMB501. Se se mantiver abaixo de 55% por três ciclos consecutivos, é mudança real de perfil dos campeões — com impacto direto na interpretação de exposição garantida via Full e na dependência estrutural de modalidade de envio.

2. **Health dos campeões em Full no próximo pacote com dado disponível:** Se Kit 4 Potes 1050ml (MLB4073003575, health atual 0,75) ou Conjunto 5 Potes Tampa Vermelha (MLB3288536143, health atual 0,71) registrarem nova queda no campo `health` do `top_items_details`, a degradação vira ação com Yasmin/Himmel. Se health se estabilizar ou subir acima de 0,85, o risco é auto-corrigível sem intervenção.

3. **Estoque crítico do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090) em Full:** `available_quantity=9` com 6 pedidos no dia equivale a menos de 2 dias de cobertura ao ritmo atual. Se o próximo pacote registrar `available_quantity < 3` ou `status=paused`, o anúncio sai do ar em Full com impacto imediato no GMV do dia e possível variável confundidora para health e ranking nos ciclos subsequentes.
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória semanal contém bloco diário de 22/05 já ingestido — este ciclo é o **segundo** que recebe os mesmos dados; a tese construída anteriormente está disponível para confirmar ou refutar. Janelas 7d, 30d e 60d disponíveis com cobertura de `logistic_type` em 100%. `ml_snapshot` completo: reputação, mix de modalidade de envio, ADS summary, account_overview e top_items_details com `status: ok` em todos os blocos. Base robusta; tese forte autorizada.

---

### Leitura temporal

- **Patamar bimestral confirmado, acomodação mensal em curso:** GMV R$4.622,03 está +16,3% sobre avg_60d (R$3.975,41) e apenas +3,4% sobre avg_30d (R$4.470,29). O ganho de patamar do bimestre está se convertendo em nova normalidade — o que era distância de crescimento virou banda. Não há rompimento para baixo; há acomodação do pico.

- **Volume comprimido, ticket carregando:** Orders 84 estão -15,4% vs avg_30d (99,3) e -17,6% vs pares do mesmo dia da semana (média 102,0). O GMV se sustenta exclusivamente pelo ticket: R$55,02 hoje vs R$45,00 na média 30d (+22,3%) e R$42,40 na média 60d (+29,8%). Não é crescimento de alcance — é mix de maior valor compensando queda de volume. Esse padrão persiste ao longo de toda a janela 30d.

- **Controle sazonal: dentro da banda:** Os quatro pares do mesmo dia da semana oscilam de R$3.214,56 (24/04) a R$6.465,75 (01/05). O GMV de R$4.622,03 está -2,1% da média dos pares — dentro da variância interna dessa série. O dia não é fraco em si; está dentro do intervalo esperado para o dia da semana.

- **Hipóteses anteriores — no limite do gatilho:** O ciclo anterior registrou ADS share 69,8% e health <0,80 nos dois campeões Full como primeiro ciclo de alerta. Ontem foi o **segundo ciclo consecutivo** exatamente nas mesmas condições (ADS share 69,9%, health MLB4073003575=0,75, MLB3288536143=0,71). O gatilho para tese estrutural definido no ciclo anterior era o **terceiro ciclo consecutivo** — o próximo ciclo decide.

---

### Leitura estratégica

- **ADS dominância como compensação de penalização orgânica:** ROAS 10,87x (`revenue_ads_yesterday_brl` R$3.228,78 / `spend_yesterday_brl` R$296,96) e ACOS 4,57% são números excepcionais. Mas o ADS share de **69,9%** (R$3.228,78 / R$4.622,03) implica que apenas R$1.393,25 do GMV vieram de orgânico. A leitura estratégica não é "ADS eficiente" — é que os dois principais anúncios Full (`MLB4073003575`, `health=0,75`; `MLB3288536143`, `health=0,71`) têm penalização ML ativa há pelo menos dois ciclos, reduzindo exposição orgânica, e Himmel está compensando essa perda com mídia paga de alta eficiência. O resultado parece saudável; a estrutura por trás não está.

- **Rotação de mix de modalidade de envio no top 10 — leitura pontual, não tendência:** O mix de modalidade de envio dos campeões de ontem (Full 47,1% vs Cross-Docking 52,9%) diverge da banda 7d (Full 74,9%) e 30d (Full 73,7%). A causa identificável: o Conjunto 5 Potes Tampa Preta (MLB4535865317, Cross-Docking, sold_quantity acumulado=327) assumiu a liderança do dia com 20 pedidos — produto de histórico baixo e health não calculada que rotacionou para o topo em um dia fora do padrão. A base inteira tem Full apenas em 33,3% dos anúncios ativos; os dias em que os líderes habituais Full (MLB4073003575, MLB3288536143) dominam empurram o mix da janela 7d/30d para ~74%. A inversão de ontem é leitura do dia, não mudança estrutural de mix.

- **Concentração de família IMB501 — dependência crônica com novo vetor emergindo:** A família IMB501 (Conjunto 5 Potes em tampas Preta, Vermelha e Cinza) somou 37 dos 84 pedidos (44,0%). Top3 em 48,8% e top5 em 64,3%. A dependência da família de potes de vidro é padrão histórico, não novo. O que merece atenção: o Conjunto 5 Potes Tampa Preta (MLB4535865317, Cross-Docking, `available_quantity=8376`) emergiu como líder do dia pela primeira vez com esse volume — sem health calculada, sem Frete Grátis, anúncio Clássico. Hipótese: exposição ADS deslocou foco para esse item em detrimento dos campeões habituais em Full. Não confirmado sem breakdown de `revenue_ads` por `platform_item_id`.

- **Trajetória MercadoLíder Platinum — segundo dia positivo consecutivo:** Progresso em 81,34%, gap R$55.226,77, ETA ~13,8 dias ao ritmo de R$4.012,89/dia. O GMV de R$4.622,03 supera o ritmo necessário (R$55.226,77 ÷ 13,8 ≈ R$4.002/dia) em +R$620. Segundo ciclo consecutivo acima do ritmo — trajetória Platinum no caminho. O risco não é o dia atual; é qualquer queda sustentada recalculando o ETA para além de 20 dias. As métricas de qualidade estão dentro dos limites obrigatórios (`claims_rate` 0,25%, `cancellations_rate` 0%, `delayed_handling_rate` 0,12%).

---

### Tese da conta

**Vulnerável.** No número, a conta está dentro da banda histórica com ticket em trajetória de alta consistente ao longo do bimestre — aparência de estabilidade. Na estrutura, duas fragilidades se somam há dois ciclos consecutivos: (1) os dois principais anúncios Full têm `health` abaixo de 0,80 — penalização orgânica silenciosa que não aparece no GMV porque (2) Mercado Ads responde por ~70% do faturamento com ROAS excepcional, mascarando a erosão do orgânico. O resultado atual é sustentado por mídia paga eficiente sobre orgânico enfraquecido. A conta não está em queda, mas a estrutura não está saudável: qualquer evento que reduza as campanhas de Himmel remove ~70% do faturamento sem orgânico capaz de segurar o patamar.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads em conta com orgânico estruturalmente pressionado — ADS share ~70% por dois ciclos consecutivos, com os dois principais anúncios Full (`MLB4073003575`, `health=0,75`; `MLB3288536143`, `health=0,71`) operando com penalização ML ativa.
- **Por que importa:** O orgânico enfraquecido por health degradada não sustenta o patamar atual sem o suporte das campanhas. Uma pausa técnica, revisão de verba ou queda de ROAS das campanhas Himmel remove ~70% do GMV sem vetor de compensação. A fragilidade é invisível enquanto ADS performar excepcionalmente — e exatamente por isso é o risco mais perigoso.
- **Histórico:** Segundo ciclo consecutivo nessa configuração. A leitura anterior definiu explicitamente o terceiro ciclo como gatilho para confirmação de tese estrutural.
- **Sinal de confirmação:** ADS share ≥ 60% no próximo ciclo completa o terceiro consecutivo e transforma a hipótese em tese estrutural confirmada. Health de MLB4073003575 ou MLB3288536143 permanecendo abaixo de 0,80 por mais dois ciclos consolida a penalização como crônica — e no caso de MLB3288536143 (`is_catalog=true`, `catalog_product_id` MLB44224272), o risco de perda de Buy Box torna-se ativo.

---

### Sinais a observar

1. **ADS share no próximo ciclo ≥ 60%:** terceiro dia consecutivo confirma dependência estrutural de mídia paga — tese sai de hipótese e passa a exigir revisão com Yasmin e Himmel sobre se essa proporção é estratégia deliberada ou ausência de orgânico saudável.

2. **Health de MLB4073003575 e MLB3288536143 no próximo ciclo:** se ambos permanecerem abaixo de 0,80 pelo terceiro ciclo consecutivo, penalização orgânica vira crônica; para MLB3288536143 especificamente (`is_catalog=true`), confirma risco ativo de perda de posição de Buy Box na página de Catálogo MLB44224272.

3. **Estoque de Kit 6 Canecas Tulipa (MLB6167272090, `available_quantity=9`, modalidade de envio Full):** se o anúncio entrar em ruptura sem reposição confirmada no CD do ML em até 2 dias, o segundo vetor de categoria (canecas) desaparece do faturamento — concentrando ainda mais a dependência na família IMB501 de potes de vidro.
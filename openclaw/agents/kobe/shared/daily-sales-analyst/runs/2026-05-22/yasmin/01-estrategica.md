<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

`reputation`, `fulfillment_mix` (7d/30d/yesterday top10), `top_items_details`, `ads_summary` e `account_overview` presentes com `status: ok` — cobertura factual robusta. Weekly tem apenas 1 entrada (2026-05-22 recém-ingerida) e monthly está sem tese consolidada, o que limita confirmação de hipóteses com séries longas. `last_daily_file: 2026-05-20.md` cria gap de 2 dias no diário. Hipóteses da memória de L05 são pontos únicos do mesmo dia — **candidatos, não confirmações**. Tese hoje é factual sobre trajetória 30d/60d; leituras sobre ADS share e health exigem mais ciclos.

---

### Leitura temporal

- **7d vs dia:** Média 7d foi de 113,3 pedidos e R$5.555 de GMV. Ontem: 84 pedidos (`orders_vs_7d_pct=-25,9%`) e R$4.622 (`gmv_vs_7d_pct=-16,8%`). A 7d está elevada porque captura dias recentes mais fortes — não porque ontem foi colapso. As últimas quatro sextas mostram amplitude extrema: R$3.214 (24/04) → R$6.465 (01/05) → R$3.700 (08/05) → R$5.494 (15/05). Ontem (R$4.622) está na faixa intermediária do par de sextas — abaixo de 15/05 mas acima de 08/05. Leitura: queda vs 7d é reflexo de pico recente capturado pela janela, não sinal de reversão.

- **30d vs 60d — padrão de ticket compensando volume:** GMV +3,4% vs 30d e +16,3% vs 60d, com ticket +22,3% e +29,8% respectivamente. Volume de pedidos negativo em ambas as janelas (-15,4% vs 30d; -10,4% vs 60d). A conta está **acima da banda de 60d em GMV, mas com pedidos em queda gradual** — padrão de shift de mix para produtos de maior ticket, não crescimento de alcance.

- **Mesmo dia da semana:** GMV -2,1% vs média das 4 últimas sextas (R$4.718 vs R$4.622). Dentro da banda histórica de sextas — o dia não foi fraco em si, é consistente com o padrão do dia da semana.

- **Hipóteses anteriores (L05 2026-05-22):** Registradas como candidatos: ADS share 69,9%, health degradada nos dois Full líderes (MLB4073003575 h=0,75; MLB3288536143 h=0,71), cluster IMB501 como vetor dominante, ratings_negative 39% como anomalia, Kit 6 Canecas Tulipa com 6 unidades pós-baixa. Nenhum tem ciclo anterior confirmado no pipeline — todos transitam como **hipóteses em observação**, não confirmações.

---

### Leitura estratégica

- **Lente 1+2 — GMV sustentado por ticket; volume em erosão lenta:** A conta operou ontem com GMV dentro da banda de sextas e acima da média 60d, mas essa leitura superficial esconde o vetor real: o ticket médio de R$55,02 está 22,3% acima da média 30d (R$45,00) e 29,8% acima da média 60d (R$42,40), enquanto pedidos caem em todas as janelas. O GMV não está crescendo por alcance — está sendo sustentado por mix de produtos de maior valor unitário. Reputação `5_green` com `power_seller_status=gold`, `claims_rate=0,25%`, `cancellations_rate=0%` e `delayed_handling_rate=0,12%` sustentam elegibilidade estrutural. Mas `ratings_negative=39%` é desproporcional para esse nível de reputação — não se explica pelos agregados oficiais e levanta hipótese de concentração de avaliações negativas nos anúncios Full com health degradada (MLB4073003575 e MLB3288536143), que acumulam `sold_quantity` alto e operação de longa data.

- **Lente 3 — Divergência de modalidade de envio revela possível erosão de exposição dos Full líderes:** A janela de 7d mostra Full 74,9% / Cross-Docking 25,1%; 30d repete o padrão (73,7% / 26,3%). Mas ontem o top 10 ponderado por pedidos entregou Full 47,1% / Cross-Docking 52,9% (`fulfillment_mix_yesterday_top10`). A diferença vem do cluster IMB501: Tampa Preta em Cross-Docking (20 pedidos) e Tampa Cinza em Cross-Docking (7 pedidos) dominaram o dia, enquanto os dois campeões em modalidade Full — Kit 4 Potes 1050ml (`health=0,75`, Padrão inferior) e Jogo Potes Tampa Vermelha (`health=0,71`, Padrão inferior) — entregaram 21 pedidos combinados. Hipótese: o ML está reduzindo progressivamente o ranking dos dois Full com nível de qualidade do anúncio degradado, e a elevação do Cross-Docking no top 10 ontem pode ser primeiro sinal visível desse efeito — não expansão de demanda.

- **Lente 5 — ADS dominante, eficiente, mas com piso orgânico desconhecido:** ADS gerou R$3.228,78 com gasto de R$296,96 — ROAS 10,87x, ACOS 4,57% (`ads_summary`). O **ADS share representa 69,9% do GMV do dia** (R$3.228,78 / R$4.622,03) — zona de ADS dominante. As campanhas de Himmel são altamente eficientes, mas sem breakdown de receita ADS por `platform_item_id`, o piso orgânico real não é observável. Com cauda morta de 176 anúncios pausados vs 81 ativos (`account_overview.totals`), a concentração de receita em poucos anúncios amplificados por ADS configura estrutura de três fragilidades sobrepostas: dependência de poucos anúncios + ADS dominante + health degradada nos Full líderes.

- **Lente 6 — MercadoLíder Platinum: no ritmo, dependente de ADS para sustentar:** Progresso 81,34%, gap R$55.226,77, `ritmo_diario_brl=R$4.012,89`, ETA ~13,8 dias. O dia (R$4.622) está acima do ritmo necessário (≈ R$4.002/dia), contribuindo marginalmente para a promoção. Com 69,9% do GMV dependente de campanhas Himmel, o ritmo que sustenta a trajetória de Platinum é ADS-dependente — qualquer interrupção de verba eleva o ETA de forma não-linear. Intervalo atual: "no ritmo, sustentar = mover; reduzir = adiar significativamente."

---

### Tese da conta

**Vulnerável.** O GMV está acima da banda de 60d e o ROAS das campanhas Himmel é alto — o número de ontem parece saudável. Mas a estrutura por trás tem três fragilidades sobrepostas que se reforçam: 69,9% do GMV é ADS-dependente com piso orgânico desconhecido; os dois principais anúncios em modalidade Full — que historicamente respondem por ~74% dos pedidos na janela 7d/30d — operam em Padrão inferior de nível de qualidade do anúncio (h=0,75 e h=0,71), expostos a erosão progressiva de ranking; e a cauda tem 176 anúncios pausados contra 81 ativos, com concentração top 5 em 64,3%. O resultado financeiro de curto prazo está sendo sustentado por ADS eficiente mais cluster IMB501 em Cross-Docking com estoque robusto — o que mascara deterioração estrutural nos anúncios Full líderes.

---

### Risco estrutural principal

- **Risco:** Degradação do nível de qualidade do anúncio nos dois campeões em modalidade Full — Kit 4 Potes 1050ml Azul-petróleo (MLB4073003575, `health=0,75`, faixa Padrão inferior) e Jogo Potes Tampa Vermelha (MLB3288536143, `health=0,71`, faixa Padrão inferior) — com potencial de perda progressiva de exposição orgânica e deslocamento do mix da conta para Cross-Docking.
- **Por que importa:** Full respondeu por 74,9% dos pedidos na janela 7d e 73,7% na janela 30d. Se o ML continuar penalizando esses anúncios via algoritmo de ranking em `MLB244658` (nenhum dos dois é Catálogo — competem por posição em categoria), a exposição orgânica cai, o ADS share sobe para compensar e a margem pressiona. A divergência de modalidade de envio observada ontem (Cross-Docking dominando o top 10 pela primeira vez vs padrão histórico 7d/30d) pode ser primeiro sintoma visível desse ciclo. Com ratings_negative em 39% concentrado possivelmente nesses anúncios, a deterioração de health pode ter raiz em experiência pós-compra, não em configuração de listing.
- **Histórico:** Primeiro ponto observável no pipeline (L05 de 2026-05-22 registrou como "segundo ponto pontual" mas sem daily anterior confirmado; sem série histórica de health, não é possível distinguir degradação nova de crônica).
- **Sinal de confirmação:** MLB4073003575 ou MLB3288536143 com `health < 0,70` (faixa Básico) em próximo pacote; ou ambos saindo do top 5 por 2 ciclos consecutivos enquanto cluster IMB501 Cross-Docking mantém liderança — isso confirmaria erosão de ranking como causa, não variação de demanda.

---

### Sinais a observar

1. **Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090) — ruptura de estoque Full iminente:** `available_quantity=6` após 6 pedidos ontem em anúncio Full (`logistic_type=fulfillment`). Se próximo pacote mostrar `status=paused` ou `available_quantity=0` sem reposição confirmada, o anúncio sai da rotação Full — impactando exposição, nível de qualidade e agregado de GMV dos dias seguintes. Verificável no próximo ciclo.

2. **Participação em pedidos de MLB4073003575 e MLB3288536143 saindo do top 5 por 2 ciclos consecutivos:** Se os dois Full líderes perderem posição no ranking de top anúncios por 2 dias seguidos enquanto o cluster IMB501 Cross-Docking (Tampa Preta e Tampa Cinza) mantém liderança, confirma hipótese de erosão de exposição por nível de qualidade do anúncio degradado — não variação sazonal de mix. Verificável em 2–3 ciclos.

3. **ADS share acima de 65% por mais 2 ciclos com ROAS acima de 5x:** Se o share de ADS permanecer acima de 65% do GMV em dois ciclos adicionais, a dependência de Mercado Ads (Himmel) passa de característica pontual a padrão estrutural confirmado — exigindo avaliação sobre piso orgânico real e sustentabilidade sem mídia paga. Verificável em 2–3 ciclos; depende de `ads_summary` disponível no pacote.
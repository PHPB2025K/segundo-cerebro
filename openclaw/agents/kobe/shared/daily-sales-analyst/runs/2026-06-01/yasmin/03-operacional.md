<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **O ganho de volume foi real e expressivo, não inflado por ticket — confirma operacionalmente a tese L01 de patamar.** Os 206 pedidos representam +100,5% vs same_weekday_avg (102,75) e +90,4% vs avg_30d (108,2); o ticket R$48,32 ficou praticamente idêntico ao avg_30d (+1,3%), indicando que o GMV R$9.953 veio de alcance, não de composição mais cara. O dia não foi puxado por ticket alto mascarando fraqueza de volume — foi volume dobrando sobre ticket estável. Isso confirma operacionalmente que o crescimento identificado pela L01 tem base em pedidos reais, não em artefato de mix.

- **O dia foi executado integralmente sobre os dois campeões Full em cobertura crítica, drenando o estoque residual.** O cluster IMB501 (MLB3288536143 — Tampa Vermelha 45, Preta 40, Cinza 33 = 118 pedidos = 57,3% do volume) é Full e encerrou com `available_quantity=13`. O Kit 4 Potes 1050ml (MLB4073003575, Full, `health=0,75`) somou mais 14 pedidos com `available_quantity=13`. O maior dia da conta foi executado descontando 132 pedidos de dois anúncios que hoje têm 13 unidades cada — ao ritmo de ontem, a cobertura prospectiva do cluster IMB501 é de horas. A L01 identificou essa vulnerabilidade como risco estrutural principal; o dia de hoje não apenas confirma o risco — o acelerou.

- **O mix de modalidade de envio do dia divergiu expressivamente para Full: 96,7% Full no top10 do dia vs 80,3% Full em 30d e 85,6% em 7d.** A divergência é produto-específica: o cluster IMB501 (Full) dominou 57,3% do volume e puxou o mix do dia para concentração acima do padrão histórico. Não é divergência sistêmica — mas adiciona evidência operacional à hipótese L01 de que a base Full da conta é estreita (38,3% dos 81 anúncios ativos) e os campeões concentram o risco de modalidade. Se MLB3288536143 pausar por ruptura, o mix do próximo dia inverte instantaneamente para Cross-Docking, sem fallback no próprio portfólio Full.

- **9 cancelamentos (4,4% dos pedidos do dia) é o maior valor absoluto da série, com a Tulipa (MLB6167272090, `available_quantity=2`, `status=active` no snapshot) como fonte provável de cancelamentos automáticos overnight.** A série crescente (3→3→2→6→9 em 5 dias) ainda não entrou na `cancellations_rate` oficial (zero na janela longa ML). A Tulipa reapareceu como ativa com 2 unidades após ter pausado em 31/05 com estoque zero — com 8 pedidos processados ontem sobre esse estoque, a pausa automática desta madrugada é altamente provável, gerando novos cancelamentos que pressionam a `cancellations_rate` com ETA Platinum em 3,5 dias. Isso confirma diretamente o risco L01 e a ação operacional prioritária da L02.

---

### Sinais operacionais relevantes

- **Sinal:** Cluster IMB501 (MLB3288536143, Full) encerrou o pico histórico com `available_quantity=13` após 118 pedidos — ao ritmo de ontem, cobertura prospectiva de menos de 2 horas de venda — **interpretação operacional:** o vetor que sustenta 57,3% do volume não tem runway para o dia seguinte; qualquer pedido novo a partir deste snapshot que esgote as 13 unidades ativa pausa automática pelo ML, interrompendo o principal anúncio da conta no momento de máxima aproximação ao Platinum.

- **Sinal:** Kit 6 Canecas Tulipa Lisa 250ml (MLB6167272090, Full, `available_quantity=2`, `status=active` no snapshot 09:50 UTC de 02/06) recebeu 8 pedidos em 01/06 sobre estoque que já tinha pausado por zero em 31/05 — **interpretação operacional:** `available_quantity=2` pós-baixa de 8 pedidos indica reposição parcial ou status inconsistente; a pausa automática overnight é o cenário mais provável, e cada cancelamento automático gerado entra diretamente na `cancellations_rate` com gap Platinum de R$16.112 ainda em zero — qualquer saída do zero com ETA abaixo de 4 dias compromete a elegibilidade da medalha.

- **Sinal:** `ratings_negative` subiu de 0,39 (ciclos 22/05–31/05) para 0,41 no snapshot atual — **interpretação operacional:** variação pequena e ainda distante de qualquer threshold de rebaixamento de cor (reputação verde mantida), mas é movimento na direção errada no momento em que múltiplos vetores de cancelamento convergem; isolado, é ruído; combinado com série crescente de cancelamentos + Tulipa com pausa iminente + dois campeões em cobertura crítica, compõe pressão simultânea em dimensões distintas de qualidade.

- **Sinal:** Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo Full, `is_catalog=true`, `available_quantity=35`) gerou 19 pedidos contra ritmo histórico de ~6–11/dia — cobertura ao ritmo de ontem: ~1,8 dias — **interpretação operacional:** o único anúncio em Catálogo entre os top do dia está com estoque curto ao ritmo excepcional de 01/06; ruptura em Catálogo tem custo estrutural superior ao Clássico (perda de Buy Box, tempo de recuperação maior), e `health=null` significa que o ML não computa saúde por volume insuficiente — não que está saudável.

- **Sinal:** Kit 4 Potes 1050ml (MLB4073003575, Full, `health=0,75`, `available_quantity=13`) fez 14 pedidos com cobertura prospectiva de menos de 1 dia ao ritmo de ontem — **interpretação operacional:** segundo campeão Full em cobertura crítica simultaneamente ao cluster IMB501; a simultaneidade de risco nos dois Full é o elemento que torna o cenário de ruptura altamente provável nos próximos 24h; pausa de qualquer um dos dois retira ~64% do volume atual e injeta cancelamentos automáticos numa `cancellations_rate` que hoje ainda protege a elegibilidade Platinum.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

A execução do dia não travou — reconciliação OK, anúncios ativos durante o dia, volume limpo. Mas o dia revelou três dimensões operacionais conectadas com causa comum identificável: (1) 9 cancelamentos intradiários (4,4%), maior valor da série, crescente há 5 dias; (2) Tulipa (MLB6167272090) ativa com `available_quantity=2` após pausa por zero em 31/05 — pausa automática overnight altamente provável, com cancelamentos automáticos adicionais já em andamento; (3) dois campeões Full (MLB3288536143 e MLB4073003575) com `available_quantity=13` cada, sem runway para cobrir nem 24h ao ritmo de ontem. A causa comum é estoque insuficiente nos Full principais. A classificação é moderada, não crítica, porque a `cancellations_rate` oficial ainda está em zero e o dia executou sem bloqueio visível. Sobe para crítica se `available_quantity` de MLB3288536143 ou MLB4073003575 aparecer abaixo de 5 no próximo snapshot, se qualquer um dos dois registrar `status=paused`, ou se `cancellations_rate` sair de zero enquanto o gap Platinum ainda estiver acima de R$10k.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Status atual e `available_quantity` de MLB3288536143 (cluster IMB501, Full, 13 unidades pós-baixa de 118 pedidos) — o anúncio está ativo ou pausado agora? Se pausado, horário da pausa e volume de cancelamentos automáticos gerados? — **motivada por:** Sinal 1 (cobertura prospectiva de horas no campeão de 57,3% do volume) e confirmação do risco estrutural principal mapeado pela L01.

- **Pergunta:** Status atual e `available_quantity` do Kit 6 Canecas Tulipa Lisa 250ml (MLB6167272090, 2 unidades pós-baixa, ativo no snapshot 09:50 UTC) — a pausa automática overnight ocorreu? Quantos cancelamentos adicionais foram gerados desde 01/06 sobre esse anúncio? — **motivada por:** Sinal 2 (fonte provável de cancelamentos automáticos com impacto direto na janela `cancellations_rate` e elegibilidade Platinum) e ação #2 da L02.

- **Pergunta:** Os 9 cancelamentos de 01/06 são atribuíveis a quais anúncios e por qual mecanismo — automático por estoque zerado, cancelado pelo comprador, outro? — **motivada por:** a série crescente (3→3→2→6→9) não entrou na `cancellations_rate` oficial; identificar se os cancelamentos de hoje vieram da Tulipa (automático) ou de outro anúncio determina se o risco de elegibilidade Platinum é iminente ou ainda gerenciável nos próximos snapshots.

- **Pergunta:** Há reposição em trânsito ao CD do ML para MLB3288536143 e MLB4073003575, com ETA de chegada e processamento? — **motivada por:** sem reposição confirmada, os dois campeões Full não têm cobertura para 24h ao ritmo de ontem; a L02 definiu isso como ação #1 e o pacote de hoje confirmou que o risco permanece sem resposta visível no dado disponível.

---

### Destaque para a Condensadora

O fato operacional central do dia não é o volume histórico — é que o volume histórico foi executado drenando o estoque dos dois campeões Full para 13 unidades cada, no momento em que o Platinum está a 3,5 dias e a `cancellations_rate` ainda está em zero. O pico funcionou porque o estoque aguentou. A questão operacional de agora é que ele não aguenta mais.

O risco silencioso é justamente esse: a superfície do dia parece perfeita — reconciliação limpa, reputação verde, ADS eficiente com 10,6x ROAS e share abaixo de 50% pela primeira vez (indicando crescimento orgânico). Nada disso vai aparecer como problema no número do dia. O que aparecerá nos próximos snapshots é o `available_quantity` zerando nos dois Full principais e a `cancellations_rate` saindo de zero — e quando isso acontecer, o ETA Platinum vai colapsar simultaneamente com o volume. A Condensadora precisa comunicar que o dia de ontem foi excepcional e que o risco não está no resultado que passou — está no estoque que não existe para sustentar o próximo.
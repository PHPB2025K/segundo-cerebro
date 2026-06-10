<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a L01 identifica cobertura iminente no Kit 4 Potes 1050ml como sinal operacional prioritário** (`available_quantity=28`, ritmo de 20 pedidos/dia = runway ≤1,4 dias, padrão recorrente documentado em três rupturas desde 26/05, restock de 08/06 documentado na memória como "insuficiente pro ritmo do novo patamar"), a decisão é agir hoje: Yasmin verifica ETA de reposição no CD do ML antes que o anúncio pause automaticamente — ruptura gera cancelamentos que pressionam o `cancellations_rate` zerado da reputação Platinum recém-conquistada.

- **Dado que a L01 mapeia risco operacional secundário no Kit 06 Canequinhas Acrílico** (`available_quantity=11` em Full, 5 pedidos e 8 unidades vendidas no dia, memória de 08/06 instrui "confirmar amanhã se restock entrou, se status virou paused ou se available_quantity caiu abaixo de 8"), a decisão é checar cobertura hoje — a janela de ação está fechando e o anúncio já está dentro do limiar de urgência.

- **Dado que a L01 confirma que o crescimento do patamar ocorre apesar da degradação crônica de health dos campeões Full** (MLB3288536143 em 0,71 por 18+ ciclos, MLB5402326666 em 0,66 por 6 ciclos) e que o ADS share caiu 25,6pp em 18 ciclos reduzindo o amortecedor pago, a decisão é checar direção dos health — não agir. Os gatilhos de ação são objetivos: health do líder abaixo de 0,70 ou do MLB5402326666 abaixo de 0,63, ambos definidos pela L01.

- **Dado que a L01 confirma expansão orgânica como fato** (9 ciclos consecutivos de queda de ADS share, ROAS 14,9x, ACOS 6,31%) e que a Lente Tática 5 veda intervenção em campanha eficiente com ROAS > 5x e ACOS < 10%, a decisão é registrar o 9º ponto da série descendente (44,3%) como ponto de observação e aguardar se o próximo ciclo cruza abaixo de 40% — limiar que, confirmado em dois ciclos, consolida autonomia orgânica estrutural do canal.

---

### O que fazer hoje

1. **Yasmin:** verificar junto ao CD do ML se há restock em trânsito para o Kit 4 Potes 1050ml em Full (`available_quantity=28`, 20 pedidos no dia = runway estimado ≤1,4 dias) e qual o ETA de chegada — motivo: padrão de ruptura recorrente documentado em três ciclos desde 26/05 com restock sistematicamente insuficiente para o ritmo atual do novo patamar; se não houver reposição confirmada, o anúncio pausará automaticamente gerando cancelamentos prospectivos que impactam diretamente o `cancellations_rate` zerado da reputação Platinum — sinal de resultado: `available_quantity` acima de 40 no próximo snapshot confirma restock ativo e risco neutralizado; `status=paused` com pedidos abertos exige triagem imediata de cancelamentos.

2. **Yasmin:** verificar `available_quantity` e status do Kit 06 Canequinhas Acrílico em Full (`available_quantity=11`, 5 pedidos e 8 unidades vendidas no dia, runway ≤1,4 dias) — motivo: memória de 08/06 instrui confirmação de restock neste ciclo; anúncio opera em Full, o que significa que a Budamix não controla diretamente a reposição — o risco é o mesmo do Kit 1050ml: pausa automática com pedidos em aberto pressionando `cancellations_rate` — sinal de resultado: `available_quantity` acima de 15 no próximo snapshot confirma reposição ou ritmo menor que o esperado; `status=paused` ativa protocolo de triagem com o mesmo impacto em reputação.

3. **Yasmin:** checar direção do `health` do campeão líder (MLB3288536143, `health=0,71`, 18+ ciclos sem variação registrada) e do MLB5402326666 (`health=0,66`, 6º ciclo em nível preocupante) — motivo: com ADS share em queda sistemática (44,3% hoje vs 69,9% em 22/05), o componente pago que parcialmente compensava a degradação orgânica está encolhendo; a L01 define que queda abaixo de 0,70 no líder ou abaixo de 0,63 no MLB5402326666 confirma erosão em curso — sinal de resultado: health estável ou em recuperação em ambos encerra o risco de erosão acelerada neste ciclo; qualquer ponto abaixo dos gatilhos acima aciona alinhamento Yasmin–Himmel sobre cobertura preventiva naquele anúncio específico.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel sobre ADS:** ADS share em 44,3% com ROAS 14,9x e ACOS 6,31% (`ml_snapshot.ads_summary`) coloca a campanha em máxima eficiência pelo 9º ciclo consecutivo. A queda de share é estrutural — expansão orgânica confirmada como fato pela L01, não ineficiência de campanha. Qualquer ajuste agora introduz variável num sistema que funciona e impede leitura limpa do cruzamento do limiar de 40%, que é o próximo ponto de interesse analítico relevante.

2. **Não pausar, redirecionar ou alterar MLB5402326666 (Kit 4 Potes 640ml, `health=0,66`):** health em nível preocupante há 6 ciclos, mas a L01 e a memória deixam claro que a direção (estável, caindo ou recuperando) permanece não observável pelo pacote. Intervir sem conhecer a direção pode eliminar os 4 pedidos orgânicos do dia sem qualquer garantia de recuperação de ranking — o gatilho de ação tem condição explícita (`health < 0,63` em dois ciclos consecutivos) e ela ainda não foi atingida.

3. **Não escalar para Kobe sobre concentração estrutural da conta:** Top3 em 53,6% e top5 em 66,7% com 131 anúncios pausados vs 77 ativos é padrão crônico documentado desde 22/05 sem reversão em nenhuma janela disponível. A L01 o registra como vulnerabilidade estrutural, não como emergência ativa. Escalada para Kobe sobre diversificação de catálogo só se justifica se o patamar atual mostrar reversão sustentada de GMV em dois ciclos consecutivos — condição não presente no dia.

---

### Escalonamento

**Classificação: não escalar — com gatilho monitorado para alinhamento com Himmel.**

A conta opera em patamar confirmado (+62,6% vs avg_60d), reputação Platinum intacta (`cancellations_rate=0`, `color=5_green`), ADS eficiente e sem sinal de reversão de tendência. As duas ações prioritárias do dia são operacionais e dentro do escopo direto da Yasmin: cobertura dos dois anúncios em Full com runway crítico. Se o Kit 4 Potes 1050ml entrar em `status=paused` com pedidos em aberto antes que Yasmin confirme restock, o risco deixa de ser operacional localizado e passa a pressionar `cancellations_rate` da janela Platinum — nesse caso, Yasmin comunica Himmel apenas se houver implicação em spend de campanhas ativas vinculadas àquele anúncio. Se `health` do MLB5402326666 cruzar abaixo de 0,63 no próximo snapshot, Yasmin alinha com Himmel sobre cobertura preventiva naquele anúncio específico. Kobe não é acionado neste ciclo.
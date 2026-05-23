<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que o risco principal da L01 é a degradação de health nos dois campeões em modalidade Full (h=0,75 e h=0,71) sem histórico direcional anterior**, a decisão é proteger a série de observação sem alterar a operação. A L01 não consegue distinguir degradação nova de crônica com um único ponto — agir em campanha ou anúncio agora introduziria variável antes de ter diagnóstico direcional mínimo (2 ciclos consecutivos).

- **Dado que a divergência de modalidade de envio ontem (Cross-Docking dominando 52,9% do top 10 ponderado vs padrão histórico de ~74% Full nas janelas 7d/30d) é o primeiro sinal visível de possível erosão de exposição dos Full líderes**, a decisão é observar a composição do top anúncios nos próximos 2-3 ciclos sem agir. Um único dia fora do padrão pode ser variação de sexta, flutuação de ADS ou menor conversão pontual nos Full — confirmação exige recorrência.

- **Dado que o ADS share está em 69,9% do GMV com ROAS 10,87x e ACOS 4,57% (L01/`ads_summary`) e este é o segundo ponto de uma série iniciada em 22/05 sem histórico anterior no pipeline**, a decisão é não acionar Himmel e registrar os valores como referência. A regra tática para ADS ≥ 50% + ROAS > 5x + ACOS < 10% é não mexer — qualquer ajuste contamina a série antes de ter base para separar efeito de campanha de comportamento orgânico.

- **Dado que o Kit 6 Canecas Porcelana Tulipa Lisa 250ml está com 6 unidades em modalidade Full após 6 pedidos ontem (L01, sinal 1)**, a decisão é tratar como risco operacional de curto prazo que exige verificação imediata. Com cobertura estimada de ~1 dia ao ritmo de ontem, a pausa automática do ML é provável em 24-48h — diferentemente dos dois Full com health degradado, este é risco operacional claro dentro da janela de ação de hoje.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` do Kit 6 Canecas Porcelana Tulipa Lisa 250ml em modalidade Full (6 unidades pós-baixa após 6 pedidos ontem) e confirmar se há reposição programada para o CD do ML — motivo: cobertura de ~1 dia ao ritmo de ontem coloca o anúncio em zona de pausa automática pelo ML em 24-48h; se pausado sem reposição, configura variável confundidora que vai contaminar health, ranking e leitura de GMV dos próximos ciclos (L01, sinal 1) — sinal de resultado: reposição confirmada e anúncio ativo no próximo pacote = risco neutralizado; anúncio pausado sem reposição = registrar como variável confundidora e isolar na leitura dos próximos 3 ciclos.

2. **Yasmin:** verificar a direção do `health` dos dois campeões em modalidade Full — Kit 4 Potes de Vidro 1050ml Azul-petróleo (h=0,75, Padrão inferior) e Jogo Potes de Vidro 5 Peças Tampa Vermelha (h=0,71, Padrão inferior) — comparando com o valor do próximo pacote para determinar se a penalização está caindo, estável ou em recuperação — motivo: a tese da L01 é de erosão progressiva de ranking em categoria (nenhum dos dois é Catálogo — competem por posição orgânica em MLB244658); definir a direção é a menor checagem que desbloqueia ou descarta tanto a hipótese de erosão quanto a decisão de alinhar com Himmel sobre cobertura preventiva — sinal de resultado: `health` estável ou subindo em ambos = manter observação sem ação; `health` caindo em qualquer dos dois (especialmente abaixo de 0,70, faixa Básico) = Yasmin alinha com Himmel sobre cobertura ADS preventiva nos anúncios afetados.

3. **Yasmin:** registrar ADS share (69,9%), ROAS (10,87x), ACOS (4,57%) e spend (R$296,96) como segundo ponto consolidado da série — motivo: sem breakdown de receita ADS por `platform_item_id`, não é possível saber se o ADS está amplificando os Cross-Docking saudáveis ou compensando exposição orgânica perdida nos Full penalizados (L01, lente 5); o acúmulo da série por 2-3 ciclos é o único caminho para distinguir essas hipóteses — sinal de resultado: ADS share acima de 65% por mais 2 ciclos com ROAS acima de 5x = Yasmin abre discussão com Kobe sobre dependência estrutural; share caindo abaixo de 50% sem queda de GMV = confirma piso orgânico próprio, descarta risco de dependência.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar, pausar ou escalar campanhas de Mercado Ads.** ROAS 10,87x e ACOS 4,57% classificam a operação como altamente eficiente — qualquer movimento (aumentar verba, redirecionar segmentação, pausar campanhas com pior share) introduz variável antes de ter série histórica que permita separar comportamento orgânico de efeito de campanha. A série tem apenas dois pontos; o gatilho para acionar Himmel é degradação de eficiência (ROAS < 3x ou ACOS > 30%) ou confirmação de health caindo em ambos os Full líderes — nenhum dos dois está presente agora.

2. **Não tratar a divergência de modalidade de envio de ontem como confirmação de deslocamento estrutural e não recomendar migração de anúncios Cross-Docking para Full.** A divergência (Cross-Docking 52,9% no top 10 ponderado vs ~74% Full no histórico 7d/30d) é o primeiro sinal visível em um único ciclo — insuficiente para confirmar erosão de exposição dos Full vs variação de demanda de sexta. Migração de Cross-Docking para Full é decisão estrutural de Trader/Kobe, não ação tática de canal, e exige padrão confirmado em múltiplos ciclos antes de sequer sinalizar.

3. **Não alterar, pausar ou redirecionar os dois campeões em modalidade Full com health penalizado (Padrão inferior) sem antes saber a direção do health nos próximos 2 ciclos.** O `sold_quantity` alto de ambos (981 e 5.757 respectivamente) indica que operam há bastante tempo — health abaixo de 0,85 pode refletir histórico de penalizações já absorvidas e em processo de recuperação. Pausar agora eliminaria exposição residual que esses anúncios ainda mantêm enquanto o algoritmo ML ajusta o ranking. A direção do health nos próximos 2 ciclos é o dado mínimo necessário para qualquer decisão.

---

### Escalonamento

**observar**

A conta está operacionalmente estável — reputação `5_green`, `cancellations_rate=0`, `delayed_handling_rate=0,12%`, MercadoLíder Gold no ritmo de Platinum (progresso 81,34%, ETA ~13,8 dias) — e as campanhas Himmel estão eficientes. Não há gatilho para acionamento hoje. O risco principal identificado pela L01 (degradação de health nos dois Full líderes com possível erosão de ranking) é estrutural mas sem direção confirmada: um único ponto de observação não sustenta ação forte. O risco operacional imediato (Kit 6 Canecas Tulipa em risco de ruptura de estoque em Full) está no escopo de Yasmin sem precisar de Himmel ou Kobe. Dois gatilhos que alteram a classificação: (1) se `health` de qualquer dos dois campeões Full cair abaixo de 0,70 no próximo ciclo, ou ambos caírem por 2 ciclos consecutivos enquanto o cluster IMB501 Cross-Docking mantém liderança no top anúncios → Yasmin alinha com Himmel sobre cobertura ADS preventiva; (2) se ADS share permanecer acima de 65% do GMV por mais 2 ciclos com ROAS acima de 5x → Yasmin abre discussão com Kobe sobre dependência estrutural e sustentabilidade do piso orgânico.
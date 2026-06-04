<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Risco operacional confirmado pela L01 requer verificação imediata antes de qualquer outra ação.** Os 3 anúncios que concentram 70,2% do volume hoje — Jarra Medidora de Vidro 500ml, Conjunto 5 Potes Tampa Preta e Kit 6 Canecas Tulipa — constam todos na `account_overview.active_analysis.out_of_stock_ids` no snapshot pós-baixa de 03/06. Com pedidos chegando em D+1 sobre estoque zero, cada conversão vira cancelamento automático pela Shopee, pressionando taxa de não cumprimento e Taxa de Cancelamento do Vendedor. Não há dados de Saúde da Loja para detectar isso no pacote (HTTP 404). A deterioração será invisível ao pipeline até Lucas verificar manualmente no Seller Center.

- **Tese seed em observação e memória vazia impõem postura de coleta, não de ação em alavancas.** A L01 declara primeiro ciclo de pipeline para esta conta, com weekly.md e monthly.md sem histórico, last_daily_file em 14 dias de lacuna. Com `shop_performance` (HTTP 404) e `ads_summary` (HTTP 403) indisponíveis, qualquer decisão sobre Shopee Ads ou estrutura promocional seria baseada em zero evidência acumulada. O correto hoje é definir pontos zero observáveis e aguardar 2-3 ciclos.

- **Programa de Frete Grátis zerado em toda a base ativa (`fsp_pct=0%`) é anomalia para o papel Volume/Giro, mas sem histórico não é possível saber se é mudança recente ou configuração persistente.** Não agir sobre isso hoje. Registrar como dado inicial e verificar no próximo ciclo se já havia ocorrido antes ou se é novo lapso — decisão de ligar / desligar seletivamente é de Lucas, e exige saber a causa antes de qualquer movimento.

- **Kit 6 Canecas Tulipa (CTL002, cerâmica/porcelana) em terceiro lugar com 8 pedidos (14,3% do dia) é sinal de mix que pode ou não divergir do papel Volume/Giro de vidro/potes.** Com apenas 1 ciclo disponível, não constitui evidência de refinamento de tese. Registrar como checagem dirigida para 3-5 ciclos — se persistir acima de 12% do volume diário com Jarra e Potes com estoque normalizado, a observação sobe de relevância para a L01.

---

### Postura sobre a tese seed

Tese seed v1 (Volume/Giro, Pedro, 02/06/2026) está em **observação**. Primeiro ciclo de pipeline, memória vazia, comportamento parcialmente coerente mas não confirmado. Lucas não muda operação. Três checagens dirigidas para os próximos 3-5 ciclos:

1. **Qual produto lidera cada dia quando os 3 campeões têm estoque normalizado?** Jarra Medidora (unitário de giro) liderando com folga confirma papel Volume/Giro. Kit 6 Canecas Tulipa assumindo liderança com ticket crescente enfraquece a tese.
2. **Ticket médio sustenta acima de R$ 40 sem composição de kits crescentes?** R$ 42,84 hoje (vs baseline R$ 40,45) pode refletir mix de kits-potes ou pode ser flutuação. Cruzar ticket do dia com mix de top 5 por 3 ciclos revela a causa.
3. **Programa de Frete Grátis segue em 0% ou retorna a algum percentual?** Se continuar em zero por 3 ciclos consecutivos, hipótese de que parte da deceleration estrutural de 60d→30d tem causa nessa ausência se fortalece para discussão com Pedro.

---

### O que fazer hoje

**Lucas:** verificar `available_quantity` dos 3 campeões no Seller Center até 10h de 04/06 — Jarra Medidora de Vidro 500ml, Conjunto 5 Potes Tampa Preta e Kit 6 Canecas Tulipa, todos confirmados em estoque zero no snapshot pós-baixa — o risco operacional declarado pela L01 é que D+1 gera cancelamentos automáticos em cascata sobre ~34 pedidos prospectivos, pressionando taxa de não cumprimento e Taxa de Cancelamento do Vendedor numa janela em que a Saúde da Loja está completamente cega no pacote (HTTP 404); se ao menos 2 dos 3 tiverem reposição confirmada até o início da manhã, risco é mitigado; se nenhum tiver reposição, Lucas aciona Pedro imediatamente, não espera — **sinal de resultado:** cancelamentos D+1 ≤ 2 unidades com reposição confirmada = risco contido; cancelamentos D+1 ≥ 5 = cascata em andamento, escalonamento para Pedro obrigatório.

**Lucas:** registrar como ponto zero observável os seguintes dados de 03/06 — ticket R$ 42,84 (+12,5% vs avg_30d R$ 38,07), mix top 5 (Jarra unitária com 39% do volume vs kits de pote e cerâmica), Programa de Frete Grátis ativo em 0% da base, concentração top 3 em 70,2% — motivo: este é o primeiro ciclo de pipeline com tese seed v1 e sem esses pontos zero registrados não há baseline para avaliar confirmação ou enfraquecimento da tese nos próximos ciclos — **sinal de resultado:** com pontos zero registrados, o ciclo de 04/06 já produz primeira comparação válida; sem registro, cada ciclo seguinte precisará reancorá-los da memória, acumulando ruído.

**Lucas:** investigar se o `fsp_pct=0%` em toda a base ativa é intencional (decisão operacional documentada) ou lapso — consulta rápida no Seller Center identifica se há Programa de Frete Grátis configurado em algum anúncio mas pausado, ou se a loja nunca ativou o programa — motivo: para conta hipotetizada como Volume/Giro, ausência total de Programa de Frete Grátis é alavanca relevante não operando; saber se é gap novo ou configuração histórica é pré-requisito para qualquer discussão posterior com Pedro sobre ativar seletivamente nos campeões com estoque — **sinal de resultado:** se o Programa de Frete Grátis nunca foi ativado, registrar como característica estrutural da conta e subir para Pedro na próxima semana; se foi desativado recentemente, identificar data e cruzar com início da deceleration de 30d.

---

### O que NÃO fazer ainda

**Não acionar Himmel sobre Shopee Ads.** `ads_summary.status="unavailable"` por HTTP 403 — sem dados de spend, ROAS, ACOS ou campanha ativa. Qualquer instrução a Himmel seria baseada em zero evidência de performance atual. Além disso, tese seed em observação e memória vazia impedem calibrar se o spend atual está adequado, insuficiente ou excessivo. Aguardar ao menos 3 ciclos com `ads_summary` populado antes de qualquer alinhamento sobre Shopee Ads.

**Não alterar Cashback em Moedas Shopee nem Programa de Afiliados Shopee.** Ambos os blocos estão estruturalmente indisponíveis (`coins_summary.status="unavailable"` e `affiliate_summary.status="unavailable"` por limitação permanente da Open API). Decisão sobre qualquer um dos dois requer dado do Seller Center que Lucas não tem como extrair automaticamente. Sem baseline de percentual médio ou receita via afiliados, qualquer ajuste introduz variável cega no sistema. Suspensão total dessas decisões neste ciclo.

**Não declarar enfraquecimento ou refinamento da tese seed com base no Kit 6 Canecas Tulipa em terceiro lugar.** 8 pedidos de cerâmica (14,3% do dia) com memória zero e campeões de vidro zerados no mesmo ciclo não sustenta hipótese de divergência de papel. O ranking do Kit Canecas pode ser artefato da ruptura de estoque dos campeões (demanda desviada para produto disponível), não sinal de mix estrutural. Qualquer hipótese de refinamento requer 3-5 ciclos com estoque normalizado nos campeões — antes disso, refinamento de tese seria precipitado e levaria escalonamento prematuro para Pedro.

---

### Escalonamento

**Observar** — com condição explícita de escalonamento para Pedro em até 48h.

Hoje não há dado suficiente para escalonamento imediato a Pedro ou a Himmel: Saúde da Loja, Shopee Ads, tese seed sem ciclos anteriores e memória vazia. A ação de Lucas de verificar estoque dos campeões no Seller Center é o pivot de todo o próximo ciclo. Se Lucas confirmar reposição de ao menos 2 dos 3 campeões até 10h de 04/06, o risco operacional principal é contido e a postura segue em observação por mais 2-3 ciclos. Se Lucas confirmar zero reposição até 10h de 04/06, o escalonamento muda imediatamente para **alinhar com Pedro** — a conta opera prospectivamente sem ~70% do volume operacional e a decisão de reposição urgente, eventual ajuste de mix temporário ou aceite de deterioração de Saúde da Loja extrapola a alçada tática diária. Em D+3 sem `shop_performance` disponível no pacote e sem confirmação de reposição, escalonamento para Pedro é obrigatório independentemente — deterioração de Pontos de Penalidade e Taxa de Cancelamento do Vendedor pode estar ocorrendo de forma invisível ao pipeline.
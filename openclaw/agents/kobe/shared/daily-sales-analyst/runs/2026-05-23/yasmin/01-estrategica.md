<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly com entrada de 22/05 traz hipóteses ativas testáveis — base recente suficiente para confirmar ou enfraquecer teses do ciclo anterior. `monthly.md` está sem entrada preenchida (template vazio), sem âncora de tese mensal além do histórico numérico. Todas as janelas temporais (7d, 30d, 60d) disponíveis com `coverage_pct=100%`. Dados ML opcionais presentes: reputação, mix de modalidade de envio, nível de qualidade dos anúncios e MercadoLíder. Base robusta para tese com confiança média-alta; ressalva única é a ausência de `monthly.md` consolidado.

---

### Leitura temporal

- **vs 7d:** `orders_vs_7d_pct=-16,4%`, `gmv_vs_7d_pct=-5,6%`. Queda aparente inflada pelo spike de 05-16 (184 pedidos, R$7.064,70, `same_weekday_last_4[0]`) que elevou a média de 7d. Excluindo 05-16, o dia fica dentro da banda. Leitura de "queda recente" não sustentada.

- **vs 30d e 60d:** `gmv_vs_30d_pct=+13,9%`, `gmv_vs_60d_pct=+27,0%`; `ticket_vs_30d_pct=+24,3%`, `ticket_vs_60d_pct=+32,4%`; `orders_vs_30d_pct=-8,4%`, `orders_vs_60d_pct=-4,0%`. O padrão consistente em duas janelas — GMV acima da banda, pedidos abaixo, ticket em elevação acelerada — não é ontem. É a trajetória do bimestre.

- **vs mesmos sábados:** últimos 4 sábados alternam forte/fraco (R$7.064 / R$2.823 / R$5.491 / R$2.510 — `same_weekday_last_4`), média R$4.472 (`same_weekday_avg.avg_gmv`). O dia em R$5.124,32 fica +14,6% acima da média dos sábados e posicionado na faixa intermediária — não é fraco, não é excepcional dentro da variância intrínseca dos sábados.

- **Hipóteses de 22/05:** (a) Kit 6 Canecas Porcelana Tulipa 250ml (MLB6167272090) com estoque 7→2 — confirmada e agravada: `available_quantity=2` com 9 pedidos no dia; ruptura ativa ou iminente (hipótese: pedidos em excesso do estoque disponível geram cancelamentos prospectivos, impacto em `reputation.cancellations_rate` no próximo ciclo); (b) nível de qualidade Padrão inferior em MLB3288536143 (`health=0,71`) e MLB4073003575 (`health=0,75`) — **terceiro ponto consecutivo idêntico**, hipótese de degradação estrutural progressiva ganha peso sem reversão espontânea; (c) ADS share ≥65% por dois ciclos — não confirmado hoje: `revenue_ads_yesterday_brl=R$2.538,63` / `gmv=R$5.124,32` = ADS share **49,5%**, queda de ~70% do ciclo anterior; orgânico passou de ~R$1.391 (22/05) para R$2.586 hoje — gatilho de escalonamento a Kobe não acionado.

---

### Leitura estratégica

- **Ticket elevation com compressão de volume é o padrão do bimestre, não de ontem.** Em 30d e 60d o GMV supera a banda enquanto pedidos ficam abaixo; o controle de sazonalidade (`same_weekday_avg`) confirma o mesmo padrão. A conta não está ganhando alcance — está ganhando valor médio de venda. A hipótese mais sustentada é mix-shift para kits de maior valor unitário (linha 1050ml ganha presença relativa); sem breakdown de `revenue_ads_yesterday_brl` por `platform_item_id`, não é possível confirmar se ADS está direcionando tráfego para os SKUs de maior ticket ou se o orgânico está fazendo esse trabalho.

- **Lente 4 — os dois campeões Full operam em Padrão inferior pelo terceiro ciclo consecutivo.** MLB3288536143 (Conjunto 5 Potes, `health=0,71`, `is_catalog=false`, `listing_type=gold_special`) e MLB4073003575 (Kit 4 Potes 1050ml, `health=0,75`, `is_catalog=false`) competem por ranking em categoria, não por Buy Box; `health < 0,85` significa que o ML reduz ativamente a exposição orgânica desses anúncios em busca de categoria. Três pontos sem movimento indicam piso de degradação estabilizado — não reversão, não aceleração confirmada. A hipótese é que ADS (ROAS 9,0x calculado: R$2.538,63/R$282,39; `avg_acos_pct=4,43%`) tenha compensado a perda orgânica; o crescimento do orgânico hoje (R$2.586 vs ~R$1.391 em 22/05) pode indicar que outros anúncios — notadamente o cluster de canecas — estão ganhando tração orgânica, não que os potes estejam se recuperando.

- **Lente 3 — modalidade de envio: divergência estrutural entre campeões e base.** `fulfillment_mix_yesterday_top10.full_pct=87,8%` vs `account_overview.active_analysis.fulfillment_mix.full_pct=33,3%`: os campeões do dia operam quase integralmente em modalidade Full enquanto dois terços da base ativa usa Cross-Docking. A receita da conta está concentrada em anúncios dependentes de estoque no CD do ML; a base em Cross-Docking funciona como reserva teórica mas não gera volume proporcional. Com `account_overview.totals.paused=176` vs `active=81` (pausa > ativo × 2,2), a cauda morta é dominante — sem segundo vetor em formação.

- **Lente 6 — MercadoLíder Platinum: no ritmo, sem folga.** `mercadolider.platinum.progress_pct=82,5%`, `gap_revenue_brl=R$51.794,49`, `ritmo_diario_brl=R$4.070,09`, `eta_dias_estimado=12,7 dias`. O GMV do dia (R$5.124,32) está acima do pace necessário (~R$4.078/dia implícito no gap/ETA). O constraint é exclusivamente faturamento — `sales_60d_count_paid=5.721` já supera 3× o threshold de vendas Platinum (1.725). A variância de sábados (par forte/par fraco) indica que ETA vai flutuar; dias fracos que venham na janela rolling vão subir o ETA rapidamente.

---

### Tese da conta

**Vulnerável.** O GMV entregou acima das bandas de 30d e 60d (`gmv_vs_30d_pct=+13,9%`, `gmv_vs_60d_pct=+27,0%`), sustentado por ticket em elevação consistente no bimestre. A estrutura, no entanto, é estreita: um único anúncio de variações (MLB3288536143, Conjunto 5 Potes, todas as cores somam ~44% dos pedidos do dia) opera em nível de qualidade Padrão inferior há três ciclos consecutivos sem reversão; o segundo campeão (MLB4073003575) acompanha; a cauda permanece morta (176 pausados vs 81 ativos); e o único anúncio emergente (MLB6167272090, Kit 6 Canecas Tulipa, 3º no dia) está em ruptura iminente com `available_quantity=2`. A conta é saudável no número e vulnerável na fundação.

---

### Risco estrutural principal

**Risco:** Degradação consolidada de nível de qualidade dos dois principais campeões Full em Padrão inferior — MLB3288536143 (`health=0,71`) e MLB4073003575 (`health=0,75`) — pelo terceiro ciclo consecutivo sem reversão, com `health < 0,85` sinalizando redução ativa de ranking em categoria pelo ML.

**Por que importa:** Os dois anúncios são `is_catalog=false` e competem por posição em busca de categoria; nível de qualidade Padrão inferior significa que o ML está ativamente deprimindo o ranking orgânico deles. MLB3288536143 concentrou ~44% dos pedidos do dia. Se o orgânico desses itens continua em queda silenciosa e ADS compensa, a conta fica estruturalmente dependente de investimento pago para manter volume — qualquer ajuste de campanha por Himmel expõe o buraco. O ADS share de 49,5% hoje representa melhora em relação ao ciclo anterior (~70%), mas a degradação do nível de qualidade não é explicada por ADS: é estrutural dos anúncios.

**Histórico:** Primeiro ponto documentado em 22/05 (`daily/2026-05-22.md`). Valores idênticos entre 22/05 e 23/05 — sem reversão espontânea em dois ciclos.

**Sinal de confirmação:** MLB3288536143 ou MLB4073003575 apresentar `health ≤ 0,69` no próximo pacote (entrada em nível Básico, máxima perda de exposição) OU qualquer um dos dois sair do top 5 em volume sem campanha desligada explicando a queda — ambos confirmariam aceleração da perda de ranking orgânico em categoria.

---

### Sinais a observar

1. **MLB6167272090 (Kit 6 Canecas Porcelana Tulipa 250ml) — `available_quantity=2` com 9 pedidos no dia.** Se o próximo pacote mostrar `top_items_details[MLB6167272090].status=paused` ou cancelamentos atribuídos a este anúncio, a ruptura em Full está ativa — impacto em `reputation.cancellations_rate` nos próximos ciclos. Anúncio é Full; reposição requer envio ao CD do ML (dias). Sinal binário: pausado ou cancelamento confirmado = ruptura ativa; permanece ativo com estoque > 5 = reposição aconteceu (registrar origem).

2. **ADS share abaixo de 50% por 2 ciclos consecutivos.** Hoje 49,5% (queda de ~70% em 22/05). Se o próximo ciclo confirmar share ≤ 50%, a hipótese de dependência estrutural de ADS enfraquece e o orgânico em expansão vira tese consolidada. Se voltar acima de 65%, o padrão de dois ciclos consecutivos se reestabelece e o gatilho de escalonamento a Kobe (terceiro ciclo ≥ 65%) volta a estar vivo — duas condições opostas, ambas falsificáveis no próximo pacote.

3. **Nível de qualidade de MLB3288536143 no próximo ciclo.** Três pontos consecutivos em `health=0,71` (Padrão inferior) sem movimento. Se o quarto ponto mostrar `health ≤ 0,69` (entrada em Básico), a degradação está em aceleração e o risco estrutural principal avança de hipótese para confirmação. Se mover para `health ≥ 0,75`, a degradação parou. Janela relevante: próximos 2 ciclos para estabelecer direção.
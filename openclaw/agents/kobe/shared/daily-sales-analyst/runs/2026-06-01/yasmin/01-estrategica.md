<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly.md com 7 entradas diárias consecutivas (22/05–31/05) e hipóteses ativas rastreadas em múltiplos ciclos — base operacionalmente robusta para leitura temporal. Monthly.md sem conteúdo acumulado (mês novo). O volume_band check da data readiness flagou o ML como "partial confidence" (206 pedidos vs avg30 108,2 = +90,4% spike positivo, não bloqueante). Todos os blocos `ml_snapshot` vieram com `status: ok` — reputação, mercadolider, fulfillment_mix, top_items_details, ads_summary e account_overview disponíveis com cobertura 100%.

---

### Leitura temporal

- **vs 60d e 30d — rompimento de patamar em múltiplas janelas:** GMV R$9.953 está +115,2% acima do avg_60d (R$4.624) e +92,8% acima do avg_30d (R$5.162); pedidos 206 vs avg_60d 105,3 (+95,6%) e avg_30d 108,2 (+90,4%). A banda histórica de 60d ficou entre R$3.664 e R$5.208 nos mesmos dias da semana — hoje é quase o dobro do melhor domingo registrado. Movimento consistente em todas as janelas de comparação: não é ruído.

- **vs 7d — aceleração sobre base já elevada:** O avg_7d já estava em R$7.089 (+53,7% vs 30d), refletindo a semana recente acima do padrão histórico. Contra essa base elevada, o dia ainda registra +40,4% de GMV e +43,0% de pedidos. A memória registra 31/05 (véspera) em R$8.268 — dois dias consecutivos excepcionais. O 7d médio foi puxado para cima pelo padrão da própria semana, o que significa que a aceleração do ciclo recente é estrutural, não pontual.

- **vs mesmos domingos (controle de sazonalidade):** Os quatro domingos anteriores foram R$3.664 / R$4.184 / R$5.127 / R$5.208, média R$4.546. Hoje: +118,9%. A sazonalidade de domingo não explica a magnitude; o movimento é intrínseco à conta, não ao dia da semana.

- **Hipóteses anteriores:** (a) Nível de qualidade do anúncio de MLB3288536143 em 0,71 — décimo primeiro ciclo idêntico, confirmado; (b) Nível de qualidade do anúncio de MLB4073003575 em 0,75 — décimo primeiro ciclo idêntico, confirmado; (c) ADS ACOS no corredor 8–9% — confirmado hoje em 8,89%; (d) trajetória Platinum com ETA encolhendo ciclo a ciclo — confirmado, gap agora R$16.112 com progresso 94,56% e ETA 3,5 dias ao ritmo médio; (e) Tulipa (MLB6167272090) pausada em 31/05 com estoque zero — hoje reapareceu como ativa com `available_quantity=2` após 8 pedidos; cobertura efetivamente zerada, cancelamentos prospectivos altamente prováveis.

---

### Leitura estratégica

- **Lente 1 + Lente 3 — Ganho de patamar real, estruturalmente concentrado em Full de cobertura crítica:** A ruptura de banda em três janelas independentes (7d, 30d, 60d) e no controle de sazonalidade (mesmo dia da semana) configura ganho de patamar, não ruído. O vetor central é o cluster IMB501 (MLB3288536143 — Tampa Vermelha 45, Tampa Preta 40, Tampa Cinza 33 = 118 pedidos = 57,3% do volume do dia), item em modalidade de envio Full com `available_quantity=13` ao fim do dia. A dependência de modalidade de envio Full nos campeões está em seu extremo histórico: top10 de ontem = 96,7% Full vs base ativa = 38,3% Full. Os campeões são uma exceção de Full numa base majoritariamente Cross-Docking (61,7%), o que amplifica cada ruptura: sem estoque no CD do ML, não há fallback na própria base de anúncios Full.

- **Lente 4 — Nível de qualidade do anúncio degradado nos dois maiores vetores de volume, sem sinal de recuperação em 11 ciclos:** MLB3288536143 (`health=0,71`, nível preocupante) e MLB4073003575 (`health=0,75`, nível regular) operam em faixas que, pela definição ML, implicam perda progressiva de exposição orgânica. Que ambos estejam entre os maiores geradores de volume no pico histórico da conta sugere que o ganho de patamar é sustentado por ADS e/ou posição adquirida — não por recuperação de qualidade orgânica. A discrepância entre performance e nível de qualidade do anúncio é estrutural: 11 ciclos idênticos indicam que a depreciação está consolidada e a conta cresce apesar dela, não com ela. Há 8 anúncios com `low_health` e 62 sem dado de qualidade calculado — a saúde da cauda ativa é opaca.

- **Lente 5 — ADS amplifica orgânico robusto, não mascara fraqueza:** Spend R$451,93 / revenue ADS R$4.790,83 / ROAS 10,6x / ACOS 8,89%. ADS share 48,1% do GMV — abaixo do limiar de dominância (50%), pela primeira vez em múltiplos ciclos onde o share oscilou entre 49,5% e 69,9% em dias de menor volume. Em dias anteriores com GMV entre R$5k–R$8k, o ADS carregava acima de 50%; hoje, com GMV ~R$10k, o orgânico representou 51,9%. Hipótese: o ganho de volume tem componente orgânico crescente — ADS sustentou a base e o orgânico escalou junto. Não é possível confirmar sem breakdown por anúncio (pendência estrutural), mas o padrão é coerente com a expansão de volume acima da escala proporcional de gasto.

- **Lente 6 — MercadoLíder Platinum a 3,5 dias de ritmo médio, com 9 cancelamentos no dia mais próximo:** Progresso 94,56%, gap R$16.112, ritmo diário R$4.665. O GMV de hoje (R$9.953) é 113% acima do pace necessário (~R$4.603/dia ao ritmo atual), o que significa que o dia comprimiu o ETA de forma expressiva. O risco direto ao Platinum não é faturamento — é qualidade: `cancellations_rate=0` na API oficial (janela longa), mas 9 cancelamentos no dia (4,4% dos 206 pedidos intradiários). A série recente de cancelamentos é crescente: 25/05: 3, 26/05: 3, 30/05: 2, 31/05: 6, 01/06: 9. Com MLB6167272090 (Tulipa, `available_quantity=2`, 8 pedidos no dia) provavelmente gerando cancelamentos automáticos desta noite, e MLB3288536143 e MLB4073003575 com 13 unidades cada, o caminho até o Platinum passa obrigatoriamente por estoque nos próximos 3–4 dias — não por faturamento.

---

### Tese da conta

**Em ganho de patamar — estruturalmente vulnerável no estoque Full.**

A conta rompeu a banda histórica de 60d em todas as janelas disponíveis, com consistência entre GMV, pedidos e controle de sazonalidade, apoiada em dois dias consecutivos de volume excepcional (31/05 e 01/06) e em um 7d médio que já sinalizava elevação sustentada (+53,7% vs 30d). A justificativa temporal é robusta. O problema é que o patamar está sendo alcançado com os dois principais geradores de volume — MLB3288536143 e MLB4073003575, ambos em Full — com `available_quantity=13` cada, níveis de qualidade do anúncio degradados há 11 ciclos (0,71 e 0,75 respectivamente) e sem reposição confirmada no pacote. O ganho de patamar é real, mas está construído sobre uma base de estoque que, ao ritmo atual, pode se esgotar antes que o MercadoLíder Platinum seja formalizado.

---

### Risco estrutural principal

**Risco:** Ruptura iminente de estoque Full nos dois campeões de volume (MLB3288536143 e MLB4073003575, `available_quantity=13` cada) no momento de máxima aproximação ao MercadoLíder Platinum.

**Por que importa:** As duas posições representam 64% dos pedidos do dia (118 + 14 = 132 de 206). Ambas operam em modalidade de envio Full — o estoque está no CD do ML, não na Budamix. Reposição requer envio físico, recebimento e processamento no CD, o que não é imediato. Ruptura em Full implica pausa de anúncio pelo próprio ML ou queda de `available_quantity` para zero, gerando cancelamentos automáticos que entram diretamente na `cancellations_rate` da janela de qualidade — que hoje ainda está em zero, mas é justamente o que protege a elegibilidade Platinum. Com ETA de 3,5 dias e threshold de `cancellations_rate ≤ 0,5%` para manter MercadoLíder Gold e conquistar Platinum, qualquer série de cancelamentos automáticos nos próximos 3–4 dias comprime o ETA ao mesmo tempo que ameaça a elegibilidade da medalha.

**Histórico:** O risco de estoque apertado no cluster IMB501 e no MLB4073003575 foi rastreado desde 30/05 (memória: "cobertura prospectiva ~1,9 dias") e em 31/05 ("confirmar amanhã se reposição entrou"). O pacote de hoje mostra que a reposição não chegou a nível seguro: ambos os anúncios seguem com 13 unidades ao fim do dia com volume acima de 60 pedidos combinados/dia. O risco não é novo — está se materializando em tempo real.

**Sinal de confirmação:** `available_quantity` de MLB3288536143 ou MLB4073003575 abaixo de 5 unidades no próximo snapshot, ou qualquer um dos dois com `status=paused`, confirma ruptura ativa com impacto direto no ETA Platinum.

---

### Sinais a observar

1. **`available_quantity` de MLB3288536143 e MLB4073003575 no próximo snapshot:** se qualquer um cair abaixo de 5 unidades ou `status` mudar para `paused`, o risco estrutural se materializou e o ETA Platinum está comprometido operacionalmente — independente do faturamento dos próximos dias.

2. **`cancellations_rate` da reputação sair de zero nos próximos 3 snapshots:** série de cancelamentos crescente (3→3→2→6→9 nos últimos 5 dias disponíveis) ainda não entrou na métrica oficial. Se a taxa oficial sair de zero enquanto o gap Platinum estiver abaixo de R$16k e o ETA abaixo de 4 dias, o risco de não atingir os thresholds de qualidade do MercadoLíder Platinum é real — não apenas de faturamento.

3. **GMV sustentando acima de R$7.000 por 3 dias consecutivos a partir de hoje:** confirmaria rompimento de patamar estrutural (não pico de dois dias). Queda abaixo de R$6.000 em qualquer um dos próximos 3 dias, especialmente se coincidir com ruptura de estoque Full, indicaria que o patamar observado era sustentado pela disponibilidade dos campeões — e volta à banda anterior quando o vetor pausa.
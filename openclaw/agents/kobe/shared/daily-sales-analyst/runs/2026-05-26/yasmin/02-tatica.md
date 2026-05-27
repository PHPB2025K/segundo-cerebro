<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a L01 identificou ruptura ativa iminente no Kit 6 Canecas Porcelana Tulipa Lisa 250ml (`available_quantity=2`, 4 pedidos hoje, anúncio ativo em Full) e que a janela de ETA Platinum está em ~10 dias (`platinum.gap_revenue_brl=R$42.460,66`, `progress_pct=85,66%`):** qualquer `cancellations_rate > 0` pode comprometer a promoção pelos limiares de qualidade do ML independentemente do faturamento acumulado — ação de proteção é prioritária e não pode esperar o próximo ciclo.

- **Dado que a tese da L01 é "Vulnerável — crescimento real sobre estrutura frágil" e que os dois campeões Clássico em Full operam no sétimo ciclo consecutivo com health degradado (MLB3288536143 `health=0,71`; MLB4073003575 `health=0,75`):** a decisão tática é verificar se o sétimo ponto mantém ou piora o patamar — a memória de 25/05 marcou explicitamente este ciclo como o decisório para liberar ou não o alinhamento Yasmin–Himmel (gatilho documentado: `health < 0,68`); sem queda confirmada, não acionar Himmel.

- **Dado que ADS share está em 60,6% com ROAS 13,9x e ACOS 10,96% (`ads_summary`):** ACOS em 10,96% é o terceiro ponto consecutivo acima do baseline de ~4,4% (22–23/05), mas ROAS 13,9x está muito acima do limiar de ação (5x) e ACOS abaixo de 30% — os gatilhos de ineficiência não estão ativados; decisão correta é registrar o ponto atual na série e observar mais 2 ciclos sem ajuste de campanha; mexer em ADS que preenche lacuna orgânica de campeões com health degradado, sem confirmação de ineficiência, pode colapsar o GMV.

- **Dado que o anúncio Catálogo gold_pro em Full (MLB6232315532, `is_catalog=true`, `available_quantity=31`) gerou 15 pedidos hoje com cobertura estimada de ~2 dias:** entra no horizonte de 5-7 dias como alerta de estoque — secundário ao risco da Tulipa, mas ruptura em Catálogo significa perda de Buy Box com recuperação lenta; Yasmin deve checar reposição em trânsito antes de entrar em ruptura.

---

### O que fazer hoje

- **Yasmin:** verificar status e disponibilidade de reposição do anúncio Kit 6 Canecas Porcelana Tulipa Lisa 250ml (`available_quantity=2`, 4 pedidos hoje, anúncio ativo em modalidade de envio Full) — risco operacional imediato: 4 pedidos sobre 2 unidades disponíveis configuram cancelamentos prospectivos; se reposição ao CD do ML não está confirmada, decidir entre cancelamento controlado dos pedidos excedentes ou priorização emergencial de reposição, antes que o ML cancele automaticamente e registre em `cancellations_rate` na janela de ETA Platinum; a L01 identificou que qualquer `cancellations_rate > 0` pode inviabilizar a promoção independentemente do faturamento — sinal de resultado: reposição confirmada chegando ao CD em até 24h = risco neutralizado; anúncio pausado automaticamente ou cancelamento registrado no dia = flagrar como variável confundidora para leitura de `cancellations_rate` nos próximos 3–5 ciclos.

- **Yasmin:** verificar a direção do `health` dos dois campeões em Full com penalização — Jogo Potes 5 Peças Claro (`health=0,71`, sétimo ciclo consecutivo) e Kit 4 Potes 1050ml Azul-petróleo (`health=0,75`, sétimo ciclo) — dado que a memória semanal de 25/05 marcou o sétimo ponto como decisório para liberar alinhamento Yasmin–Himmel sobre cobertura preventiva (gatilho explícito: `health < 0,68` em qualquer dos dois); se o patamar se mantém estável em ambos, continuar em observação sem acionar Himmel; se qualquer um cai abaixo de 0,68, hipótese de erosão orgânica se confirma e Yasmin alinha com Himmel sobre cobertura de ADS — sinal de resultado: sétima leitura com ambos estáveis ou em recuperação = continuar observação; queda abaixo de 0,68 em qualquer dos dois = gatilho atingido, acionar alinhamento com Himmel.

- **Yasmin:** verificar cobertura de estoque e reposição em trânsito do anúncio Catálogo Kit 6 Canecas Lisas 200ml (MLB6232315532, `is_catalog=true`, `gold_pro`, `available_quantity=31`, 15 pedidos hoje, cobertura ~2 dias) — dado que a L01 e a memória de 25/05 já sinalizavam cobertura em zona de atenção no horizonte de 5 dias e que ruptura em Catálogo significa perda de Buy Box com recuperação lenta; ação não é emergencial hoje, mas reposição deve ser confirmada antes do fim do dia — sinal de resultado: reposição confirmada chegando dentro de 2 dias = risco neutralizado na janela tática; estoque caindo abaixo de 10 unidades sem reposição em trânsito = elevar para prioridade de amanhã.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar ADS:** ROAS 13,9x e ACOS 10,96% não ativam os gatilhos de ineficiência (ROAS < 3x ou ACOS > 30%); o ACOS elevado em relação ao baseline histórico é o terceiro ponto de uma série ainda curta para declarar novo regime; ADS está preenchendo a lacuna orgânica dos campeões com health degradado — qualquer ajuste de campanha agora introduz variável num sistema onde a causalidade entre ADS e GMV ainda não está separada do comportamento orgânico, e colapso de GMV seria esperado se cobertura for reduzida antes de confirmar que o orgânico aguenta.

- **Não pausar ou redirecionar anúncios com health baixo-mas-estável:** Health de 0,71 (Jogo Potes 5 Peças) e 0,75 (Kit 4 Potes 1050ml) mantêm-se no mesmo patamar há sete ciclos sem queda de ciclo-a-ciclo confirmada; a regra dura proíbe ação sobre anúncio com health baixo sem confirmar direção — pausar agora interromperia o principal vetor de volume (44,8% do dia via cluster IMB501 + Kit 4 Potes) sobre ruptura auto-gerada, sem que o ML tenha dado sinal de penalização adicional além do que já está refletido nos sete ciclos.

- **Não tratar o patamar de GMV (+76,7% vs 60d) como base estável para decisões estruturais:** A L01 classifica a conta como "Vulnerável" — crescimento real, mas a base orgânica enfraquece silenciosamente enquanto o GMV sobe via ADS; qualquer decisão que pressuponha o novo patamar como consolidado (escalar verba, ampliar catálogo, mudar mix) é precipitada sem confirmação de que o orgânico sustenta o volume sem cobertura de mídia; o teste só é possível após estabilização do health dos campeões ou redução gradual de ADS com controle de GMV — nenhum dos dois está disponível agora.

---

### Escalonamento

**Observar** — com gatilhos condicionados para alinhamento com Himmel e abertura com Kobe nos próximos 2–3 ciclos.

A conta não requer acionamento imediato de Himmel ou Kobe. Indicadores de qualidade de reputação estão saudáveis (`claims_rate=0,0022`, `cancellations_rate=0`, `delayed_handling_rate=0,0012`) e ADS opera dentro de eficiência (ROAS 13,9x). A ação de proteção da Tulipa (ruptura iminente) é resolvível por Yasmin na operação direta, sem envolvimento de Himmel ou Kobe. Três eventos mudam a classificação nos próximos ciclos: **(a)** health de qualquer dos campeões caindo abaixo de 0,68 no próximo pacote → Yasmin alinha com Himmel sobre cobertura preventiva de ADS; **(b)** ACOS acima de 10% com ADS share acima de 60% por dois ciclos adicionais consecutivos → Yasmin alinha com Himmel sobre mix e distribuição de campanhas; **(c)** `cancellations_rate` acima de zero com gap Platinum cruzando abaixo de R$30.000 → Yasmin abre discussão com Kobe sobre gestão da janela de promoção e risco de qualidade.
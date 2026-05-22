<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Risco operacional imediato (Lente 2 — Exposição):** A tese estratégica registra que o Kit 06 Canequinhas Acrílico (MLB4410218897) tem `available_quantity=1` com 3 pedidos ontem — qualquer venda nas próximas horas configura cancelamento prospectivo garantido, com impacto direto em `reputation.cancellations_rate` (hoje zerada). A decisão tática é agir agora, antes que o ML processe cancelamentos automaticamente. Se não houver reposição possível em 24h, pausar o anúncio é menos destrutivo à reputação do que deixar o ML cancelar.

- **Risco operacional próximo (Lente 2 — Exposição, segundo vetor):** Kit 6 Canecas Tulipa (MLB6167272090) tem `available_quantity=14` com ritmo de ~5 pedidos/dia — runway de aproximadamente 3 dias. A decisão tática é checar reposição hoje, com janela para agir antes da ruptura. Não é urgência de hora, mas é urgência de dia.

- **Patamar em ganho confirmado em ≥2 janelas — não precipitar ação (Lente 1):** A L01 confirma GMV +38,7% vs 30d e +57,1% vs 60d, com ticket percorrendo R$ 40,86→R$ 60,52 em 60 dias — trajetória multijanela, não evento pontual. A decisão tática é registrar o ticket de ontem (R$ 60,52) e o ADS share (75,1%) como ponto zero da série e observar 3 dias antes de qualquer movimentação de campanha ou mix. Agir agora seria precipitar conclusão sobre tese ainda sem base histórica qualitativa.

- **ADS eficiente — não acionar Himmel (Lente 5):** Com ROAS de 13,44x e ACOS de 4,71% (`ads_summary`), a campanha está em zona de eficiência excepcional. A L01 identifica dependência estrutural (75,1% do GMV via ADS), mas o sinal correto dado esse nível de eficiência inaugural é não mexer — não corrigir. A decisão tática é manter o sistema como está e usar os próximos 3-5 dias para acumular série antes de qualquer conversa com Himmel.

---

### O que fazer hoje

- **Yasmin:** verificar `available_quantity` do Kit 06 Canequinhas Acrílico (MLB4410218897, status `active`, 1 unidade em estoque, 3 pedidos ontem via modalidade Full) e decidir entre reposição em 24h ou pausar o anúncio de forma controlada — motivo: pedidos que não podem ser atendidos viram cancelamentos prospectivos que impactam `reputation.cancellations_rate`, hoje zerada e crítica para manutenção do status Mercado Líder Gold (a L01 identificou isso como risco operacional iminente) — sinal de resultado: se pausado com sucesso antes de novo pedido, reputação protegida e anúncio pode ser reativado após reposição; se novo cancelamento ocorrer antes da ação, registrar como variável confundidora para a leitura de `cancellations_rate` nos próximos 7 dias.

- **Yasmin:** checar prazo de reposição do Kit 6 Canecas Tulipa (MLB6167272090, `available_quantity=14`, modalidade Full, ritmo ~5 pedidos/dia pelo top_items_details) — motivo: runway de ~3 dias; a L01 identificou como segundo alerta operacional e a modalidade Full significa que o estoque está no CD do ML, exigindo lead time de reposição maior que Cross-Docking — sinal de resultado: reposição confirmada com ETA ≤ 3 dias neutraliza o risco; ausência de resposta logística em 24h aciona alerta de ruptura iminente para registro no daily seguinte.

- **Yasmin:** registrar ticket médio de ontem (R$ 60,52) e ADS share (75,1% = R$ 4.593,66 / R$ 6.113,02) como **ponto zero** da série de observação, e checar direção (estável/caindo/subindo) do `health` do Kit 4 Potes de Vidro 1050ml (MLB4073003575, `health=0,75`, modalidade Full) nos próximos 2 dias — motivo: a L01 aponta penalização ativa de exposição orgânica nesse anúncio; se health cair abaixo de 0,70 ou ticket médio cair abaixo de R$ 50 em 2 dias consecutivos, as duas hipóteses da tese (patamar real vs amplificação ADS) precisam ser reavaliadas com Himmel — sinal de resultado: ticket acima de R$ 55 por 2 dias + health estável em MLB4073003575 = tese em confirmação, continuar observação; ticket abaixo de R$ 48 OU health abaixo de 0,70 em MLB4073003575 = abrir conversa com Himmel sobre cobertura preventiva.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar ou escalar campanha:** ROAS de 13,44x e ACOS de 4,71% (`ads_summary`) colocam a campanha em zona de eficiência excepcional — qualquer ajuste agora introduz variável num sistema sem histórico qualitativo (weekly/monthly vazios) e impede separar efeito de campanha de comportamento orgânico natural. A L01 é explícita: essa é a leitura inaugural. Acionamento de Himmel só está justificado se ROAS cair abaixo de 5x ou ACOS subir acima de 30% por ≥2 dias consecutivos.

- **Não interpretar a queda de pedidos vs 7d (-15,1%) como sinal de reversão de patamar:** A média 7d carrega a quinta de 14/05 (140 pedidos, R$ 6.540) — outlier que distorce a base de comparação. Controlando pelo mesmo dia da semana, ontem ficou +30,5% acima das últimas 4 quintas em GMV com pedidos apenas -1,7%. Uma única quinta abaixo da média 7d em volume, com GMV acima do padrão histórico de quintas, não configura sinal de queda. Agir sobre esse número seria reação a artefato estatístico.

- **Não recomendar migração de Cross-Docking para Full para a família IMB501:** O domínio da família IMB501 via Cross-Docking (80,2% do mix de ontem no top 10) pode ter implicações estruturais — mas migração de modalidade de envio é decisão de Trader/Kobe, não ação tática de hoje. A L01 não tem base histórica para avaliar se essa configuração prejudica exposição ou se está funcionando via ADS. Qualquer sinalização de migração exige primeiro confirmar se o mix Cross-Docking de ontem é padrão ou pontual (3-5 dias de dados), depois passar para Kobe — não antecipar.

---

### Escalonamento

**observar**

A tese da L01 é de patamar em ganho, com ADS eficiente e dois riscos operacionais pontuais endereçáveis por Yasmin sozinha (Kit 06 Canequinhas e Kit 6 Canecas Tulipa). Não há sinal que exija Himmel (campanha eficiente, ROAS > 5x, ACOS < 10%), nem decisão estrutural que exija Kobe hoje. O contexto de base zerada (weekly/monthly sem histórico) recomenda postura de coleta de evidência antes de qualquer movimentação de verba ou mix. Os próximos 3 dias devem ser usados para construir a série de ticket, ADS share e health do Kit 4 Potes. Mudança de classificação ocorre se: (a) Kit 06 Canequinhas gerar cancelamentos antes da ação de Yasmin → registrar impacto em reputação e reavaliar; (b) ADS share se mantiver acima de 65% por 3 dias consecutivos → Yasmin abre com Kobe discussão sobre dependência estrutural; (c) health de MLB4073003575 cair abaixo de 0,70 → Yasmin alinha com Himmel sobre cobertura preventiva de exposição orgânica.
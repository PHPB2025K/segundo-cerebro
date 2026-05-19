<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly e monthly de todas as três contas são templates vazios — sem teses acumuladas, sem hipóteses ativas, sem padrões registrados. Memória parte do zero para as três contas. Combinado com status DADOS_PARCIAIS (Oficial-2 e Shop-3 fora das bandas históricas com confiança parcial), a base não sustenta teses fortes em nenhuma das contas secundárias. Leituras de hoje são sementes, não consolidações — e a classificação da plataforma não pode ser fechada com honestidade.

---

### Leitura temporal

- **Budamix Store (principal):** dia em 59 pedidos, levemente abaixo do 7d (62.6), mas significativamente abaixo do 30d (80.8, -27%) e 60d (94.6, -37.6%). Mesmos domingos dos últimos 4 ciclos: 72 / 97 / 54 / 103 — média 81.5, hoje -27.6%. A conta está rodando abaixo do próprio histórico em todas as janelas. Único contrapeso: ticket em elevação consistente (+8.5% vs 30d, +12.4% vs 60d), sugerindo que a demanda não desapareceu — o volume é que recuou.

- **Budamix Oficial-2:** volume em colapso vs todas as janelas (-47% vs 30d, -53% vs mesmo dia da semana, média histórica ~34 pedidos vs 16 hoje). Paradoxo: GMV subiu vs 7d (+21.6%) porque o ticket disparou (R$98 vs R$62 no 7d e R$60 no 30d). Isso indica poucas transações de valor alto — não recuperação real. Dados parciais não descartados como causa.

- **Budamix Shop-3:** colapso uniforme em todas as janelas — -65.9% vs 30d, -71.7% vs 60d, -62.1% vs mesmo dia da semana. 9 pedidos é o piso aparente da conta. Data readiness sinaliza confiança parcial. Sem memória acumulada, impossível distinguir dado incompleto de queda real.

- **Cross-account:** CTL002 (Kit 6 Canecas Tulipa 250ml) aparece no topo de todas as três contas simultaneamente. Sobreposição de mix entre as contas é evidente — risco de canibalização não pode ser avaliado sem histórico, mas o sinal está presente.

---

### Leitura estratégica

- **Store está em erosão de patamar real.** A queda é consistente em 7d, 30d, 60d e mesmos dias da semana — não é ruído, não é dia da semana, não é ponto fora. O ticket crescente amortece GMV mas não reverte a tendência de volume. A hipótese mais provável é compressão de exposição ou de ADS (via Himmel), mas não é possível confirmar sem histórico de memória que ancore a causa.

- **Oficial-2 apresenta sinal paradoxal não interpretável com honestidade.** Volume collapse + ticket spike simultâneos, em contexto de dado parcial, podem ser: (a) dia com poucos pedidos de maior valor unitário por composição aleatória de mix, (b) dado incompleto que subestima pedidos reais, ou (c) início de deterioração de volume com demanda residual concentrada em itens premium. Sem memória e com dados parciais, as três hipóteses têm peso equivalente — tese não pode ser fechada.

- **Shop-3 está fora de qualquer banda histórica, mas a base não sustenta diagnóstico.** Se o dado for completo, 9 pedidos com -66% vs 30d é alerta sério que exige investigação imediata de exposição. Se for dado incompleto (partial confidence confirmada pelo runner), o número não é confiável. A ausência de memória impede saber se a conta já operou neste piso antes.

- **A sobreposição de CTL002 nos tops das três contas é o sinal estrutural mais relevante disponível.** Se o mesmo SKU compete entre Store, Oficial-2 e Shop-3 ao mesmo tempo, qualquer crescimento de uma conta pode estar canibalizado nas outras — mas isso exige histórico para confirmar se é padrão estável ou deterioração nova.

---

### Tese da conta

**Budamix Store — vulnerável.** Patamar em queda consistente em todas as janelas temporais (30d e 60d), sem recuperação observável, e com concentração alta em poucos produtos que amplifica qualquer oscilação dos campeões. O ticket crescente não é sinal de saúde — é sintoma de volume comprimido num mix menos amplo.

**Budamix Oficial-2 — inconclusiva.** Sinal paradoxal irresolvível com os dados disponíveis. Dados parciais + ausência de memória + ticket spike sem volume tornam qualquer classificação desonesta. Primeiro ponto de referência relevante, não tese.

**Budamix Shop-3 — inconclusiva.** Colapso numérico severo, mas dado com confiança parcial e zero histórico de memória. Se dado completo, é queda real. Se incompleto, é artefato. Classificar como qualquer outra coisa seria inflar confiança que os dados não sustentam.

**Plataforma Shopee (consolidada) — inconclusiva para tese estrutural.** Store aponta vulnerabilidade real e sustentada. As outras duas contas têm sinais contaminados por qualidade de dado e ausência de memória. Não é possível consolidar uma tese de plataforma honesta com base neste pacote.

---

### Risco estrutural principal

**Risco:** Alta concentração de volume em poucos produtos na Store (top 3 = 88.1%, top 5 = 93.2%), com Conjunto 5 Potes Vidro Redondos Tampa Preta e Jarra Medidora 500ml respondendo por ~76% dos pedidos, em contexto de queda sustentada de volume.

**Por que importa:** A Store é a conta principal da plataforma (70% do GMV Shopee do dia). Com quase todo o volume dependendo de dois produtos, qualquer oscilação deles — por exposição, ADS, estoque ou competitividade — se traduz diretamente em queda de GMV sem buffer de cauda para absorver. O canal está estruturalmente frágil para choques nos campeões.

**Histórico:** Sem memória acumulada, não é possível confirmar se esta concentração é padrão crônico da conta ou resultado de estreitamento recente de mix. A flag de qualidade do runner (`high_top3_concentration`) indica que o sistema já reconhece o sinal.

**Sinal de confirmação:** Concentração top 3 acima de 85% na Store por 3 dias consecutivos, com os dois campeões (Conjunto 5 Potes + Jarra Medidora) respondendo por mais de 70% dos pedidos individualmente — confirmaria dependência crônica, não flutuação de dia.

---

### Sinais a observar

1. **Store:** GMV abaixo de R$2.200 por 2 dias seguidos confirmaria erosão de patamar — a conta hoje está em R$2.497, e o 60d avg é R$3.562; dois dias consecutivos abaixo de R$2.200 indicariam que o piso está se aprofundando, não acomodando.

2. **Oficial-2:** Pedidos acima de 20 nos próximos 2 dias indicariam que hoje foi dado incompleto ou ponto fora; pedidos persistentemente abaixo de 20 por mais 2 dias confirmariam compressão real de volume e exigiriam investigação de exposição e ADS (via Lucas → Himmel).

3. **Shop-3:** Volume acima de 15 pedidos nos próximos 2 dias indicaria que hoje foi artefato de dado parcial; volume abaixo de 15 por 2 dias seguidos, com dado confirmado como completo, indicaria deterioração real que precisaria de diagnóstico dedicado de exposição e mix (via Lucas → Himmel).
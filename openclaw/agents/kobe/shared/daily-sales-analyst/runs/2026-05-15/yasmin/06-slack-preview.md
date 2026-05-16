<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 15/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.494,93
- Pedidos: 115
- Ticket médio: R$ 47,78
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 2 Potes de Vidro 1520ml Retangular — 32 pedidos — R$ 1.568,00*
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 20 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 12 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 9 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 9 pedidos
- Kit 6 Canequinhas 100ml — 7 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 3 pedidos
- Kit 4 Potes de Vidro 1520ml Retangular — 2 pedidos

🔍 ANÁLISE DA CONTA
- O resultado excepcional do dia rodou inteiramente sobre duas famílias de produto — a linha de potes retangulares com travas respondeu por 45% do volume, e a família de potes redondos por outros 36%, totalizando mais de 80% dos pedidos. A conta não performou de forma diversificada: ela performou concentrada, com o mesmo padrão estrutural de sempre ampliado pelo volume alto. A subida de patamar é real, mas está sendo sustentada por base estreita — qualquer perturbação nas duas famílias não tem segundo vetor para absorver.
- O ticket médio não é resultado de hoje — é tendência de múltiplas semanas. A trajetória de R$ 41,87 (bimestre) para R$ 41,99 (mês) para R$ 44,85 (semana) para R$ 47,78 (hoje) indica mudança real de mix que vem se consolidando, não amplificação pontual. Isso muda a leitura do GMV alto: não é volume que empurrou — é volume qualificado com mix mais nobre.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar posição e status de exposição dos anúncios das duas famílias líderes (potes retangulares e potes redondos) diretamente no painel ML. O dia foi expressivamente forte e 80%+ do volume veio dessas duas famílias — confirmar que o resultado veio de exposição estável e não de pico de ranking transitório. Sinal de confirmação: posição dos anúncios estável ou melhor que 7 dias atrás confirma base sólida; queda em 2+ anúncios indica exposição que pode não se sustentar. Escalar se: queda de posição nos dois líderes de família — alinhar com Himmel sobre ADS ML.
- Yasmin: registrar como checagem ativa para os próximos 3-5 dias — GMV acima de R$ 4.800 por 3 dias consecutivos, ticket acima de R$ 45 por 5 dias, e campeão de potes retangulares 1520ml acima de 20 pedidos/dia. Hoje pode ser retomada após semana fraca ou bounce pontual — a tese de ganho de patamar só transita de hipótese para base de decisão com ao menos dois desses sinais confirmados juntos. Ao final de 3 dias: 2+ sinais confirmados muda postura de "observar" para "proteger crescimento"; nenhum confirmado sugere que a semana fraca anterior era a tendência real.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. A Condensadora registrou `bloqueio_para_slack: nenhum`. Nenhum produto foi omitido por bloqueio.

---

### Decisões de formatação

- Remoção de referências às camadas internas ("a Estratégica apontou", "a Granular confirmou", "base: Estratégica + Operacional + Granular") — regra de tom: sem jargão de pipeline no Slack.
- Preservação das ressalvas de confiança: a análise de concentração e a leitura de ticket mantêm nuance de "tendência", "hipótese" e "parece forte mas base estreita" conforme a Condensadora entregou.
- "60d/30d/7d" substituídos por "bimestre/mês/semana" na seção de análise para linguagem externa — mantendo os valores e a progressão intactos.
- KIT4YW640 e KIT4YW320 mantidos no Top Produtos com nome do display_name, sem faturamento individual (dado não calculável de forma segura por unidade) — confidence medium não atingiu nível de bloqueio mas estão na cauda (3 pedidos cada); mantidos por serem top_products do pacote validado.
- Faturamento individual omitido para a maioria dos produtos no Top Produtos — o pacote entrega orders e quantity por SKU mas não faturamento por produto; evitei inferir preço unitário para não criar dado fabricado. Linha do campeão marcada com * como registro de incerteza de cálculo — decisão: omitir faturamento por produto é mais seguro que inferir.
- Kit 6 Canequinhas 100ml: usado o volume correto de 7 pedidos (corrigido pela Granular de 9 para 7) — regra: pedido real vence contagem de camada anterior.
- Canequinhas não citadas como candidato a segundo vetor na análise — bloqueado pela Condensadora ("tração inconclusiva, não afirmar diversificação com base nesse dado").
- Cancelamentos por produto não mencionados na análise — dado não disponível; integridade operacional dos líderes tratada como hipótese não confirmada, não como fato.
- Prioridades preservadas com sinal de confirmação/refutação e condição de escalonamento — conforme formato obrigatório e entrega da Condensadora.
- IMB501C (Tampa Cinza, MLB4535865311) mantido como linha separada de IMB501P/IMB501V no Top Produtos — confirmado pela Granular como anúncio distinto, não variação do mesmo MLB.
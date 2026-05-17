<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 16/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 7.085,60
- Pedidos: 185 pedidos
- Ticket médio: R$ 38,30
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico (variação BAV) — 41 pedidos
- Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico (variação BAB) — 32 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 25 pedidos
- Kit 2 Potes de Vidro 1520ml Retangular — 21 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 10 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 10 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 9 pedidos

🔍 ANÁLISE DA CONTA
- O volume de 185 pedidos provavelmente não indica patamar novo: quase metade dos pedidos veio em uma janela de 5 horas à noite, perfil inconsistente com tração orgânica. A leitura mais provável é de evento ADS ou campanha pontual — sem confirmar isso, o número do dia não pode ser usado como referência de nível da conta.
- A dependência da conta não está em 5 produtos — está em 2 anúncios: os dois listings líderes concentraram ~64% do volume do dia, cada um operando com múltiplas variações em uma única URL. Se qualquer um perder posição ou for penalizado, o impacto é imediato e a conta não tem cauda capaz de compensar.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar se havia campanha, cupom ou ADS ativo na conta ML entre 18h e 22h do dia 16/05. Com quase metade do volume concentrado nessa janela, a resposta determina se o dia foi evento isolado ou indício de patamar — muda o que monitorar nos próximos dias. Confirmar: próximos 3 dias sem campanha retornam à banda de 70–110 pedidos? Refutar: volume se mantém acima sem impulso. Escalar com Himmel se os próximos 3 dias confirmarem acima de 120 pedidos com ticket se recuperando para R$ 41+.
- Yasmin: revisar a posição dos dois anúncios líderes da conta e comparar com os últimos 7 dias. Com 64% do volume em 2 listings, qualquer deterioração de posição afeta diretamente o resultado — e um dia de volume alto com ticket comprimido pode ter distorcido métricas de qualidade. Sinal de ação: queda de posição em qualquer um dos dois anúncios líderes nas próximas 48h. Escalar com Himmel se a queda persistir por 2 dias consecutivos.

Dia analisado: 16/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: Família Canequinhas com nome comercial específico (SKUs 914C_BAV / 914C_BAB)
- Origem do bloqueio: Condensadora
- Motivo: confidence medium por mapeamento genérico de SKU; Condensadora orientou usar formulação de "anúncio líder de canequinhas" ou "grupo de canequinhas" em vez de nome específico se houver risco de ambiguidade
- Agregado autorizado: sim — "anúncio líder de canequinhas" / "variação BAV" / "variação BAB"
- Tratamento aplicado: mantidos como variações nomeadas (BAV / BAB) com referência ao produto, preservando identificação sem usar SKU cru; o nome do produto visível no listing foi mantido pois é o título real do anúncio, não o SKU interno
- Aparece na mensagem final: sim, como título de listing com indicação de variação (BAV / BAB)

Nota: a Condensadora não determinou bloqueio total — determinou cautela de formulação. A decisão de usar o título real do listing com indicação de variação foi aplicada como tratamento seguro dentro do risco médio declarado.

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Granular`, `— base: Granular + Estratégica`) dos insights da Condensadora — metadados de pipeline não pertencem ao Slack
- Quebra de frase longa no insight 2 da análise — frase original era densa; quebrada em dois períodos mantendo todos os termos analíticos e a tese intacta, sem mudar conectivos
- Preservação do "provavelmente" e da estrutura condicional no insight 1 — a Condensadora classificou como hipótese; linguagem de indício mantida
- Preservação do "não tem cauda capaz de compensar" no insight 2 — alerta direto da Condensadora; não suavizado
- Estimativa de ~98 pedidos como volume basal omitida da análise — a Condensadora bloqueou explicitamente por ser hipótese inferencial sem dado primário confirmado
- Distribuição horária detalhada omitida — a Condensadora marcou como dado técnico interno; a concentração noturna foi referenciada em forma narrativa ("quase metade dos pedidos veio em uma janela de 5 horas à noite")
- Detalhamento dos 4 cancelamentos por produto omitido — sem dado disponível no pacote; Condensadora instruiu não citar
- IDs técnicos de listing (MLBs) omitidos — a Condensadora marcou como detalhe interno desnecessário ao receptor
- SKUs brutos omitidos — substituídos por título de produto e indicação de variação legível (BAV / BAB)
- Top Produtos: variações da família IMB501 mantidas separadas por cor de tampa (Preta, Vermelha, Cinza) — são variações vendáveis distintas; consolidar seria erro per regra de variação
- Top Produtos: família Canequinhas mantida como duas linhas distintas (BAV / BAB) com identificação por variação, não por SKU cru — tratamento seguro para risco médio de identificação
- Condições de confirmação/refutação e escalonamento preservadas em ambas as prioridades — vieram da Condensadora e são elementos táticos obrigatórios
- Seção VISÃO sem comparação temporal — comparações pertencem à análise; dados objetivos apenas
- Condensadora entregou 2 insights; usados 2 — sem preenchimento adicional, sem corte
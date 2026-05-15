# Fase 2 — Refatoração completa dos prompts DSA 7.1–7.8

Data: 2026-05-15
Escopo: refatorar prompts das camadas 1–7/6B do Daily Sales Analyst para preparar Slack Writer LLM + QA Gate LLM antes da Fase 3 shadow.

## Status

FECHADO.

## Prompts atualizados

- Camada 1 — Estratégica
- Camada 2 — Tática
- Camada 3 — Operacional
- Camada 4 — Granular
- Camada 5 — Condensadora
- Camada 6B — Consolidadora Shopee
- Camada 6 — Slack Writer
- Camada 7 — QA Gate

## Melhorias aplicadas

### 7.1 — Estratégica

- Uso explícito de memória semanal e memória mensal por conta quando existir.
- Marcação obrigatória de confiança: alta, média ou baixa.
- Separação entre queda estrutural, oscilação normal e dado insuficiente.
- Saída estratégica com tese, evidência, classificação, confiança e implicação para amanhã.

### 7.2 — Tática

- Cada decisão deve conter ação, evidência, risco e gatilho de revisão amanhã.
- Recomendações soltas/genéricas foram proibidas.
- Trade-offs devem ser declarados quando houver conflito entre volume, margem, tráfego, estoque ou risco operacional.

### 7.3 — Operacional

- Separação entre execução operacional e hipótese de tráfego.
- Distinção obrigatória entre mudou hoje, já era estrutural e não dá para afirmar.
- Uso de horário dos pedidos e estoque por SKU/listing/ASIN quando disponível.
- Falta de dado deve ser marcada como dado insuficiente.

### 7.4 — Granular

- Fontes granulares obrigatórias quando disponíveis: fonte horária, estoque, ADS, ranking, cupons, promoções, fulfillment, elegibilidade/Buy Box e cancelamentos.
- Status de investigação padronizado: respondida, hipótese fraca, bloqueada por falta de dado, precisa de fonte externa.
- Separação explícita entre evidência negativa real e não respondido por falta de dado.

### 7.5 — Condensadora

- Toda tese deve ser classificada como fato comprovado, hipótese, risco latente ou bloqueado por falta de dado.
- Prioridades condensadas devem conter ação, evidência, risco, gatilho de revisão amanhã e classificação da tese.
- Bloco Preservar obrigatoriamente passa a ser contrato para Slack Writer.

### 7.6 — Consolidadora Shopee

- Marcador de confiança obrigatório para termos fortes.
- Proibição de afirmar canibalização estrutural sem evidência direta e recorrente.
- Uso obrigatório de risco de canibalização quando for hipótese.
- Entrega obrigatória de análise consolidada + três análises individuais.
- Formato mantido em parágrafo curto e denso.

### 7.7 — Slack Writer

- Slack Writer LLM declarado como camada interna do DSA, não script paralelo.
- Input correto por plataforma:
  - Shopee/Lucas: 06B Shopee;
  - Mercado Livre/Yasmin: Condensadora ML;
  - Amazon/Leonardo: Condensadora Amazon.
- Proibição explícita de rediagnóstico.
- Hipótese nunca pode virar fato.
- Exclusões absolutas: Atacado, Bling, Resumo Geral, Vendas por Canal, produto/SKU não identificado, SKU cru quando houver nome comercial seguro.
- Determinístico permanece fallback controlado e validador mecânico.

### 7.8 — QA Gate

- QA Gate LLM declarado como camada interna do DSA.
- Comparação obrigatória contra pacote validado, Condensadora/6B, Preservar obrigatoriamente e regras finais de layout.
- Bloqueio ativo quando hipótese vira fato, risco latente vira problema confirmado, confiança baixa vira linguagem forte, dado insuficiente vira conclusão, falta de dado vira evidência negativa ou risco de canibalização vira canibalização estrutural.
- QA determinístico permanece trava mecânica final.
- Saída obrigatória inclui veredito, motivos, bloqueios, ressalvas, hipótese vs fato, fidelidade à Condensadora/6B e send_allowed.

## Artefatos before/after

Snapshots before/after foram salvos em `reports/daily-sales-report-v2/prompt-diffs/2026-05-15-fase2/` para comparação auditável.

## Validação

Validação textual 7.1–7.8: OK.

Checagens mecânicas dos scripts principais do DSA: OK.

## Bloqueios mantidos

- Envio real segue bloqueado.
- Cron Slack Funcionários segue desabilitado.
- Esta fase não executou shadow e não promoveu caminho principal.

## Próximo passo

Fase 3: rodar shadow em tempo real dentro do DSA com Slack Writer LLM + QA Gate LLM, gerar artefatos comparáveis e apresentar comparativo para decisão do Pedro.

<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 13/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 2.984,35
- Pedidos: 65
- Ticket médio: R$ 45,91
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — 29 pedidos
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml — 7 pedidos
- Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio Amarelo — 5 pedidos
- Kit 2 Potes Vidro 1520ml Tampa Hermético Travas Vedação Verde-escuro — 4 pedidos
- Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- O dia parece catastrófico comparado às terças históricas (-49%), mas essa leitura está inflada pelos picos de abril — o baseline real de terças normais é 84–87 pedidos, e hoje (65) representa -24%, decelação gradual e persistente, não colapso repentino. A conta está em acomodação pós-ciclo promocional, não em queda abrupta.
- O risco real hoje não está no número de pedidos — está na concentração: ~49% das unidades vendidas vieram de variações de uma única família de produto (Potes de Vidro) sem segundo vetor visível. Com volume já abaixo do patamar e conta classificada como vulnerável, qualquer disrupção de ranking ou disponibilidade nessa família impacta metade da operação imediatamente, sem cauda para absorver.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar posição dos anúncios líderes da família Potes de Vidro no ML e comparar com 7 dias atrás. Concentração de ~49% das unidades em uma família sem segundo vetor significa que queda de ranking nesse cluster explica sozinha grande parte do recuo de volume. Confirmar/refutar: posição caiu em 2 ou mais anúncios líderes → alinha com Himmel sobre ADS ML; posição estável → hipótese de normalização se fortalece, manter observação.
- Yasmin: checar reputação da conta e status dos anúncios do cluster principal (pausados, sem estoque, penalizados). Antes de investigar exposição ou acionar ADS, descartar causa operacional simples evita decisão errada. Confirmar/refutar: reputação ou disponibilidade degradada → causa identificada, ação corretiva direta; tudo em ordem → fortalece hipótese de exposição ou normalização.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs técnicos (IMB501P_T, CLR002, 914C_B, KIT2YW1520, 914C_BAV, IMB501PT, IMB501CT, KIT4YW1520, etc.)
  - Origem do bloqueio: Condensadora
  - Motivo: identificadores técnicos internos, não devem aparecer visivelmente no Slack
  - Agregado autorizado: não — substituídos por título real do anúncio
  - Tratamento aplicado: substituídos pelos títulos reais dos produtos
  - Aparece na mensagem final: não (como código); sim, como título real do anúncio

- Item bloqueado: comparação -49% vs mesmo dia da semana sem contexto de inflação promocional de abril
  - Origem do bloqueio: Condensadora
  - Motivo: induziria leitura de emergência incorreta
  - Agregado autorizado: sim — Condensadora aprovou uso do -49% apenas dentro do contexto de inversão (insight padrão C), com baseline real explicitado
  - Tratamento aplicado: mantido dentro do insight com contextualização completa, conforme aprovado
  - Aparece na mensagem final: sim, como parte do insight contextualizado

- Item bloqueado: hipótese de ticket estrutural (mix-shift) como fato confirmado
  - Origem do bloqueio: Condensadora
  - Motivo: ainda não confirmada; risco de transformar hipótese em certeza
  - Agregado autorizado: não
  - Tratamento aplicado: omitido da mensagem; ticket aparece apenas como dado objetivo na seção VISÃO, sem interpretação
  - Aparece na mensagem final: não como hipótese; sim como dado bruto (R$ 45,91) na VISÃO

---

### Decisões de formatação

- Remoção de metadados internos "— base: Estratégica + Operacional" e "— base: Estratégica + Granular (fallback)" nos dois insights — metadados internos de pipeline, não devem aparecer no Slack
- Consolidação de produtos equivalentes em Top Produtos: IMB501P_T + IMB501C_T + IMB501V_T (todos platform_item_id MLB3288536143, título idêntico) somados em 29 pedidos sob um único item — mesmo anúncio ML, variações de SKU interno; regra ML de consolidar equivalentes
- Faturamento por produto omitido dos Top Produtos — dado não disponível no pacote por produto; não inventar; formato reduzido a "[nome] — [pedidos] pedidos"
- Comparação temporal ausente na seção VISÃO ML — regra obrigatória: VISÃO mostra dados objetivos sem comparação; comparações pertencem à ANÁLISE
- Preservação do -49% com contextualização completa conforme aprovado pela Condensadora — padrão C (inversão negativa); remover o dado distorceria a utilidade do insight
- Prioridade de escalonamento para Himmel mantida como condicional ("confirmar/refutar: posição caiu → alinha com Himmel") — Himmel não é acionado diretamente pelo DSA; acionamento via Yasmin após confirmação de sinal
- Nota sobre Granular fallback não aparece na mensagem Slack — é metadado de pipeline; concentração de ~49% tratada como estimativa de dados brutos, não diagnóstico granular validado, conforme alerta da Condensadora
- Dois insights usados — Condensadora entregou exatamente 2; nenhum adicionado, nenhum removido
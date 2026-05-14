<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 13/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 2.984,35
- Pedidos: 65 pedidos
- Ticket médio: R$ 45,91
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — 29 itens
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida — 7 itens
- Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio Amarelo — 5 itens
- Kit 2 Potes Vidro 1520ml Tampa Hermético Travas Vedação Verde-escuro — 4 itens
- Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto — 3 itens

🔍 ANÁLISE DA CONTA
- A queda de hoje não é ruído de um dia — é o terceiro ponto consecutivo de declínio em terças (134→87→65), com a média da semana já abaixo do piso de 60 dias como bloco. O canal não teve um dia fraco; está em trajetória de enfraquecimento sem causa identificada ainda.
- A dependência operacional não é em três produtos distintos — é em um único anúncio da família Potes de Vidro que gerou 41% dos itens em três variantes de cor. Somando toda a família Potes no top-10, o canal operou com 57% dos itens concentrados numa única categoria, sem segundo vetor com massa para compensar qualquer falha nesse listing.
- O volume não caiu por falha de janela horária — os três picos canônicos (9h, 15h, 19h) estiveram ativos e seguiram o padrão esperado para o canal. A perda está distribuída ao longo de todo o dia, sem concentração anômala em nenhuma hora, o que aponta para redução geral de exposição ou tráfego, não problema localizado num período.

🎯 PRIORIDADES DO DIA
- Yasmin: checar posição dos anúncios da família Potes de Vidro no painel ML e comparar com 7 dias atrás, começando pelo anúncio líder da família. O anúncio líder concentrou 41% dos itens do dia — qualquer erosão de ranking nesse listing explica a queda distribuída de volume ao longo do dia, e é o pré-requisito para acionar ou não Himmel. Confirmar/refutar: posição caiu em 3 ou mais anúncios do cluster → acionar Himmel para alinhamento de ADS ML; posição estável → avançar para checagem de reputação e Full. Escalar se: queda de posição confirmada em 3 ou mais anúncios da família.
- Yasmin: checar reputação da conta e disponibilidade dos anúncios do cluster principal no painel ML antes de qualquer ajuste de exposição ou ADS. Confirmar/refutar: reputação verde e anúncios ativos → hipótese de exposição ganha peso; qualquer degradação operacional encontrada → é a causa primária e deve ser resolvida primeiro.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios nominais de produto recebidos da Condensadora ou Granular.
- SKUs técnicos (IMB501P_T, IMB501C_T, IMB501V_T, IMB501PT, IMB501CT, CLR002, 914C_B, etc.) omitidos por proibição estrutural de formatação — nunca aparecem no Slack.
- IDs de anúncio ML na forma MLB+número (MLB3288536143, MLB5322494954, MLB4535865317, etc.) omitidos por instrução explícita da Condensadora — substituídos por "anúncio da família Potes de Vidro" e "anúncio líder da família".
- Aparecem na mensagem final: não. Nenhum ID técnico visível.

---

### Decisões de formatação

- Consolidação das três variantes do anúncio líder (IMB501P_T: 19 itens, IMB501C_T: 5 itens, IMB501V_T: 5 itens) sob um único título "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — 29 itens" — títulos de pedido são idênticos e Granular/Condensadora confirmaram que se trata de um único listing ML com variantes internas; consolidação direta por título permitida pela regra de ML.
- Faturamento por produto omitido do Top Produtos — pacote de dados fornece apenas quantity (itens vendidos) por produto, sem receita individual; campo "R$ [faturamento]" suprimido para não inventar dado ausente.
- Tags de base interna removidas dos insights ("— base: Estratégica", "— base: Operacional + Granular") — metadados internos suprimidos, conteúdo analítico preservado integralmente.
- Linguagem hedgeada preservada ("aponta para", "sem causa identificada ainda") — confiança geral é média; componente causal é hipótese qualificada per Condensadora; não convertida em certeza.
- Comparação percentual vs mesmos dias da semana histórico omitida de todas as seções — Condensadora bloqueou explicitamente o uso da série de terças como comparação direta sem contexto (distorção por outliers de 15/04 e 29/04); o referencial usado nos insights é a trajetória descritiva (134→87→65), não o percentual.
- Média de 30 dias não usada como referência de normalidade — Condensadora bloqueou explicitamente; patamar de 60 dias é o referencial honesto, e mesmo esse aparece apenas na tese qualitativa, não como número absoluto na VISÃO.
- Hipótese de erosão de cauda (ticket elevado como evidência de perda desproporcional de anúncios de menor valor) omitida da ANÁLISE DA CONTA — Condensadora marcou como plausível mas sem base granular; não transmitida como diagnóstico.
- Sem decisões ambíguas de indicação de conta — destinatário é Yasmin (Mercado Livre, conta única); sem lógica de multi-conta Shopee aplicável.
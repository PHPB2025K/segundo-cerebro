<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.057,51
- Pedidos: 90 pedidos
- Ticket médio: R$ 56,19
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 22 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
- Kit 6 Canequinhas 100ml — 8 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml — 5 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
- Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 Preto — 3 pedidos
- Kit 4 Potes de Vidro 320ml Retangular Azul-petróleo — 3 pedidos
- Kit 06 Canequinhas 100ml Suporte Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- O dia não foi fraco — o volume ficou dentro da banda histórica (mesmos dias da semana: -2,7%) e o GMV fechou acima das referências de 30d e 60d exclusivamente por ticket mais alto. A leitura correta é expansão de patamar via mix de maior valor, não queda de conversão disfarçada de dia normal.
- Três anúncios ativos estão com estoque crítico no CD do ML — todos em fulfillment, fora do controle direto da Budamix: o menor provavelmente já zerou hoje, os outros dois têm cobertura de 2 a 4 dias. Quando o fulfillment zera, o ML penaliza o health do anúncio automaticamente e o ranking cai sem ação manual possível. O dia fechou dentro do padrão, mas o risco operacional iminente não aparece nos números de ontem.
- A queda de fulfillment Full ontem (57% vs 78% em 7 dias) não indica problema logístico — o líder de volume do dia opera em cross-docking e representou 24% dos pedidos sozinho; quando esse produto domina, o mix puxa o cross-docking para cima do padrão. Full dos produtos de maior valor rodou sem restrição.

🎯 PRIORIDADES DO DIA
- Yasmin: checar o anúncio de Canequinhas Suporte Acrílico com 3 unidades restantes em fulfillment — se ainda ativo, acionar reposição imediata; se já em out-of-stock, acionar reposição urgente e registrar a data de entrada em ruptura. Cada dia em out-of-stock acumula penalização de health que persiste mesmo após reabastecimento. Confirmar/refutar: anúncio aparece como indisponível ou health cai nos próximos 1-2 dias confirma materialização; reposição em trânsito até hoje refuta o risco imediato. Escalar para Himmel se o anúncio ficou mais de 2 dias em out-of-stock.
- Yasmin: checar os dois anúncios com estoque entre 19 e 20 unidades em fulfillment (Kit 2 Potes 1050ml Retangular e Canecas Porcelana Tulipa 250ml) e confirmar se há reposição em trânsito — sem reposição, ambos atingem ruptura em 2 a 4 dias. Confirmar/refutar: confirmação de reposição em trânsito refuta o risco; ausência de movimentação confirma risco ativo.
- Yasmin: registrar o ticket médio do dia até as 22h — hoje (R$ 56,19) é o primeiro ponto da série para validar a tese de ganho de patamar; a confirmação exige ticket acima de R$ 52,00 por 3 dias consecutivos.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Display name interno do TL6250 — "Kit 6 Tigelas de Vidro 250ml"
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** Identificação internamente incorreta — o produto real vendido é Kit 6 Canecas Porcelana Tulipa Lisa 250ml; usar o display_name interno contaminaria análise de família e mix
- **Agregado autorizado:** não — substituído pelo título real do anúncio
- **Tratamento aplicado:** substituído por "Kit 6 Canecas Porcelana Tulipa 250ml" com base no raw_title do pedido real e orientação da Granular/Condensadora
- **Aparece na mensagem final:** sim, como título real do anúncio "Kit 6 Canecas Porcelana Tulipa 250ml"

---

- **Item bloqueado:** Health do KIT4YW1050 (0.75) como alerta isolado e confirmado
- **Origem do bloqueio:** Condensadora
- **Motivo:** Sem snapshot anterior, impossível distinguir patamar estável de deterioração ativa — citar como risco a monitorar, não como sinal confirmado de queda
- **Agregado autorizado:** não — item omitido da mensagem principal; mencionado apenas nas prioridades como elemento de monitoramento futuro (via memória para amanhã), sem aparecer como alerta na análise da conta
- **Tratamento aplicado:** omitido da seção de análise da conta como alerta isolado
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Proporção de GMV via ADS (~60%) como anomalia ou benchmark
- **Origem do bloqueio:** Condensadora
- **Motivo:** Primeiro registro formal, sem baseline histórico para classificar como estrutural ou pontual
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** IDs técnicos MLB (platform_item_id) e SKUs crus
- **Origem do bloqueio:** Condensadora
- **Motivo:** Desnecessários para mensagem operacional
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitidos; usados apenas nomes dos produtos
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmação de health degradada do IMB501P
- **Origem do bloqueio:** Condensadora
- **Motivo:** health=null no pacote — não inferir problema onde não há dado
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (base: Estratégica, Granular, etc.) de todos os insights — motivo: regra de não expor bastidores do pipeline no Slack
- Preservação da ressalva de confiança média nos insights — especialmente nos pontos de risco de estoque, onde a Condensadora qualificou como "provavelmente já zerou" e não como fato confirmado; linguagem preservada: "provavelmente já zerou hoje"
- Uso do título real do anúncio para TL6250 ("Kit 6 Canecas Porcelana Tulipa 250ml") em vez do display_name interno incorreto — motivo: divergência confirmada pela Granular; raw_title prevalece por regra hierárquica
- Omissão da health do KIT4YW1050 como alerta isolado — motivo: bloqueio da Condensadora por ausência de histórico; preservado apenas como memória para amanhã, não como sinal de alerta no Slack
- Omissão do percentual de GMV via ADS (~60%) — motivo: bloqueio da Condensadora por ausência de baseline histórico
- Quebra dos insights da análise em três bullets separados, cada um correspondendo a um insight da Condensadora — motivo: clareza de leitura sem alterar tese, conforme diretriz Pedro 2026-05-17
- Kit 06 Canequinhas Suporte Acrílico (914C_BAV) referenciado pelo nome do produto na mensagem, sem SKU cru — motivo: regra de não usar SKU cru visível; produto identificável pelo nome
- Ranking de Top Produtos mantido em ordem decrescente por pedidos — motivo: regra estrutural obrigatória; produtos com empate em 5 pedidos (KIT10YW1050, IMB501V, TL6250) mantidos na ordem do pacote validado
- Seção VISÃO MERCADO LIVRE sem comparações temporais — motivo: regra da seção; comparações pertencem à análise da conta
- TL6250 referenciado como "Kit 6 Canecas Porcelana Tulipa 250ml" na seção Top Produtos — decisão de usar título real encurtado do anúncio sem truncamento que comprometa identificação; omissão de "Lisa Coloridas Xícara" por clareza, mantendo identificação do produto (caneca de porcelana, 250ml, Tulipa)
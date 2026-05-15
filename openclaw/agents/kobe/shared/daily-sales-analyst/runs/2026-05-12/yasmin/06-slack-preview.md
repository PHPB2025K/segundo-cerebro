<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 12/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.081,49
- Pedidos: 91 pedidos
- Ticket médio: R$ 44,85
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Jogo Potes de Vidro 5 Peças — Tampa Preta — 26 pedidos
- Jogo Potes de Vidro 5 Peças — Tampa Cinza — 15 pedidos
- Jogo Potes de Vidro 5 Peças — Tampa Vermelha — 11 pedidos
- Jogo 6 Canequinha 100ml Suporte Madeira Alumínio — 6 pedidos
- Kit 4 Potes Vidro Hermético 1520ml Verde-escuro — 6 pedidos
- Kit 6 Canecas de Porcelana 200ml Colorida — 5 pedidos
- Suporte Gamer 2 Controles e Headset Preto — 3 pedidos
- Kit 6 Potes Vidro Hermético Azul-petróleo — 3 pedidos
- Kit 2 Potes Vidro 1050ml Azul-petróleo — 3 pedidos
- Kit 6 Canequinhas 100ml Suporte Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- A leitura de "top 3 produtos" mascara o risco real: os 55,3% de concentração estão em um único anúncio (Jogo Potes de Vidro) com três variantes de cor — não há diversificação entre três produtos distintos, e qualquer oscilação de ranking, reputação ou estoque afeta as três variantes simultaneamente, sem hedge interno entre elas.
- O dia parece neutro em GMV, mas a estabilidade é frágil: o volume menor foi compensado pelo ticket mais alto, e toda a execução dependeu desse anúncio único sem segundo vetor com capacidade real de absorção na cauda — os produtos da posição 4 em diante somaram menos da metade do volume do anúncio principal.
- Os 4 cancelamentos ficaram sem localização de origem — se estiverem concentrados no anúncio principal (que carregou mais da metade dos itens do dia), o peso operacional é desproporcionalmente maior do que cancelamentos dispersos na cauda; a leitura ainda é limitada até que a origem seja confirmada.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar posição e saúde do anúncio Jogo Potes de Vidro (três variantes de cor) comparando com a semana anterior — ranking, reputação e disponibilidade de estoque em cada variante. Esse anúncio carregou mais da metade do volume do dia; volume abaixo dos pares de segunda-feira pode ter explicação operacional ali. Confirmar/refutar: posição estável vs semana passada e variantes disponíveis → mantém observação; ranking caiu visualmente ou variante com restrição → alinhar com Himmel sobre exposição antes do fim do dia. Escalar se: ranking caiu de forma visível ou qualquer variante apresentar sinal de restrição operacional.
- Yasmin: verificar a origem dos 4 cancelamentos do dia — se possível identificar em qual produto ou anúncio estão concentrados. Confirmar/refutar: cancelamentos dispersos em produtos diferentes → ruído normal, encerra checagem; dois ou mais no mesmo anúncio → sinal operacional ativo, registrar e observar nos próximos dias. Escalar se: dois ou mais cancelamentos confirmados no anúncio principal (Jogo Potes de Vidro).

Dia analisado: 12/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs internos (IMB501P_T, IMB501C_T, IMB501V_T)
- Origem do bloqueio: Condensadora
- Motivo: desnecessários na mensagem operacional — o anúncio é identificável pelo nome do produto
- Agregado autorizado: não aplicável (substituição por nome de produto)
- Tratamento aplicado: substituídos por descrição de cor da variante (Tampa Preta, Tampa Cinza, Tampa Vermelha) no Top Produtos
- Aparece na mensagem final: não como SKU; sim, como nome descritivo de variante

- Item bloqueado: Platform item ID MLB3288536143 em formato técnico
- Origem do bloqueio: Condensadora
- Motivo: ID técnico desnecessário para mensagem operacional
- Agregado autorizado: não — substituição por nome do produto
- Tratamento aplicado: substituído por "anúncio Jogo Potes de Vidro" em todas as ocorrências analíticas
- Aparece na mensagem final: não como ID técnico

- Item bloqueado: Pico de 16h como dado acionável
- Origem do bloqueio: Condensadora
- Motivo: sem histórico de distribuição horária para contextualização — citar como insight seria hipótese fraca disfarçada de fato
- Agregado autorizado: não
- Tratamento aplicado: omitido integralmente
- Aparece na mensagem final: não

- Item bloqueado: Hipótese de queda de ranking como causa definitiva do volume abaixo dos pares de segunda-feira
- Origem do bloqueio: Condensadora
- Motivo: não confirmada por falta de dado na Granular
- Agregado autorizado: sim — pode aparecer como pergunta a investigar, não como diagnóstico
- Tratamento aplicado: convertida em "pode ter explicação operacional ali" na prioridade de checagem, sem afirmar como causa
- Aparece na mensagem final: sim, como hipótese a verificar na prioridade 1

- Item bloqueado: Afirmação de que os cancelamentos são irrelevantes ou dispersos
- Origem do bloqueio: Condensadora
- Motivo: inconclusivo por falta de dado — a mensagem não pode assumir direção não confirmada
- Agregado autorizado: não aplicável
- Tratamento aplicado: terceiro insight carrega ressalva explícita de inconclusividade; prioridade 2 orienta verificação
- Aparece na mensagem final: não como afirmação; sim, como ponto em aberto com qualificador de limitação

---

### Decisões de formatação

- Separação das três variantes do Jogo Potes de Vidro em linhas distintas no Top Produtos — regra ML obrigatória: variantes de cor representam SKUs pais diferentes, não podem ser consolidadas em linha única; cores derivadas dos sufixos de SKU (P=preta, C=cinza, V=vermelha) confirmadas pelo exemplo explícito nas regras do prompt
- Remoção de todos os marcadores de fonte interna (`— base: Granular`, `— base: Operacional + Granular`) dos insights — metadados internos não pertencem ao Slack; teses preservadas integralmente
- Preservação do qualificador de inconclusividade no terceiro insight ("a leitura ainda é limitada") — Condensadora classificou confiança como média e exigiu ressalva explícita; não convertido para afirmação firme
- Substituição de "listing" por "anúncio" nas ocorrências de ANÁLISE DA CONTA e PRIORIDADES — termo "listing" é jargão técnico interno; "anúncio" é equivalente operacional claro para Yasmin
- Preservação do termo "hedge interno" — provém diretamente da tese da Condensadora; substituição alteraria o contraste analítico central
- Faturamento por produto omitido no Top Produtos — pacote não contém receita desagregada por SKU; dado não disponível, não inferido
- ITens com 3 pedidos mantidos no Top Produtos (posições 7–10) — todos presentes no ranking validado do pacote; nenhum bloqueado pela Granular ou Condensadora
- Pico de 16h não mencionado em nenhuma seção — bloqueio aplicado; omissão total sem substituição
- Hipótese de queda de ranking convertida para interrogação operacional na prioridade 1 — Condensadora autorizou aparição como pergunta a investigar, não como diagnóstico; linguagem ajustada para "pode ter explicação operacional ali"
- Escalonamento para Himmel mantido nas prioridades com condição explícita — Condensadora trouxe esse escalonamento via Tática; atribuição correta (via Yasmin, não direta)
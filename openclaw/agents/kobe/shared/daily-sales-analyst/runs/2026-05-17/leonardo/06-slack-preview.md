<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 17/05/2026 (Ontem)

📊 VISÃO AMAZON
• Faturamento: R$ 2.091,77
• Pedidos: 44 pedidos
• Ticket médio: R$ 47,54
• Cancelamentos: 2
• Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
• Jarra Medidora de Vidro 500ml — 16 pedidos
• Suporte Controle Gamer — 6 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 5 pedidos
• Kit 6 Canecas 250ml — 3 pedidos
• Kit 6 Canequinhas 100ml — 2 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 2 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 2 pedidos

🔍 ANÁLISE DA CONTA
• O dia foi forte, mas a saúde operacional por trás do resultado ainda não foi verificada: a Jarra Medidora de Vidro 500ml sustentou 36% dos pedidos com 100% via FBA, e nem Buy Box nem cobertura de estoque do ASIN líder estão confirmados — o volume é real, mas a condição que o gerou é desconhecida.
• O spike de hoje não está sobre uma base plana: as médias de 60d, 30d e 7d mostram volume crescendo progressivamente, então o dia é mais coerente com uma aceleração em curso do que com um evento aleatório — mas ainda é hipótese, não tendência confirmada, e precisa de 2–3 dias adicionais acima da banda para ser tratada como mudança real de patamar.
• A leitura de "segundo vetor ausente" precisa de um ajuste: individualmente nenhum produto além da Jarra Medidora se destaca, mas o grupo de potes de vidro redondos em três variações de cor soma 9 pedidos no dia — posicionando-se como segundo bloco real da conta, mais presente do que a leitura SKU a SKU sugere.

🎯 PRIORIDADES DO DIA
• Leonardo: checar Buy Box e cobertura de estoque FBA da Jarra Medidora de Vidro 500ml diretamente no console Amazon/Seller Central. Esse produto sustentou 36% dos pedidos com zero cobertura FBM de backup — sem essa validação não há base para interpretar o resultado como sustentável nem para qualquer decisão sobre ADS. Confirmar/refutar: Buy Box ≥ 85% e estoque FBA cobrindo 7–10 dias confirma operação saudável; abaixo disso, investigar causa antes de qualquer movimentação. Escalar para Pedro somente após diagnóstico, não antes.
• Leonardo: registrar o volume de hoje como ponto de referência e acompanhar os próximos 2–3 dias para distinguir spike isolado de aceleração real. A trajetória ascendente de 60d → 30d → 7d torna o spike plausível como parte de ganho de patamar, mas os próximos dias são o único mecanismo disponível para confirmar ou encerrar a hipótese. Confirmar/refutar: volume acima de 35 pedidos por 2 dias consecutivos reforça a tese; retorno à banda de 28–32 pedidos encerra a hipótese de aceleração.

Dia analisado: 17/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL250B — Kit 6 Canecas de Porcelana Tulipa 250ml Branco (ASIN B0GGTTMD4H)
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** display_name factualmente incorreto ("Tigela de Vidro 250ml") — citar com esse nome comunica categoria errada ao destinatário
- **Agregado autorizado:** não (Condensadora autorizou omissão; volume de 3 pedidos permite omissão sem perda de leitura)
- **Tratamento aplicado:** omitido da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** TL250P — Kit 6 Canecas de Porcelana Tulipa 250ml Preto (ASIN B0GGTY2BLT)
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** display_name factualmente incorreto ("Tigela de Vidro 250ml") — mesma situação de TL250B
- **Agregado autorizado:** não (Condensadora autorizou omissão; 1 pedido)
- **Tratamento aplicado:** omitido da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** TL250R — Kit 6 Canecas de Porcelana Tulipa 250ml Rosa (ASIN B0GGTVQQCJ)
- **Origem do bloqueio:** Granular (confidence medium, mapeamento por fallback)
- **Motivo:** mapeamento por fallback reduz certeza de identificação; 1 pedido, impacto mínimo
- **Agregado autorizado:** não (Condensadora orientou tratar como "provável" se necessário; volume permite omissão)
- **Tratamento aplicado:** omitido da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Cancelamentos por ASIN — distribuição entre produtos
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** dado ausente do pacote; não é possível afirmar se os 2 cancelamentos estão ou não concentrados no produto líder
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados apenas como total agregado na VISÃO (dado objetivo confirmado); nenhuma afirmação sobre distribuição por ASIN
- **Aparece na mensagem final:** sim, apenas como total (2 cancelamentos) na VISÃO, sem atribuição de origem

---

- **Item bloqueado:** Buy Box e cobertura FBA como fatos validados
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** dados ausentes do pacote; saúde operacional do dia não foi verificada
- **Agregado autorizado:** não (proibido afirmar que operação estava saudável)
- **Tratamento aplicado:** preservada a ressalva na ANÁLISE DA CONTA e nas PRIORIDADES DO DIA; nenhuma afirmação de operação validada
- **Aparece na mensagem final:** sim, como lacuna explícita na ANÁLISE e como ação de fechamento nas PRIORIDADES

---

- **Item bloqueado:** ASINs técnicos e raw_SKUs (ex.: B0G2CWWMGK, CK4742_BB, IMB501P_T)
- **Origem do bloqueio:** Condensadora
- **Motivo:** uso interno apenas; não vão para Slack
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitidos da mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Tática + Granular` etc.) dos três insights — motivo: regra do prompt; conteúdo analítico preservado integralmente.
- TL250B, TL250P e TL250R omitidos do ranking Top Produtos — motivo: bloqueio Granular/Condensadora confirmado; volume total dos três (5 pedidos) não altera leitura principal do dia.
- TL250R omitido do Top Produtos — motivo: confidence medium + mapeamento por fallback; 1 pedido; Condensadora autorizou omissão; nenhum agregado autorizado disponível.
- Ranking Top Produtos limitado a 7 itens (dos 10 no pacote) após omissão dos 3 bloqueados — motivo: bloqueios acima; ordem decrescente por pedidos preservada.
- Família IMB501 mantida em 3 linhas separadas por variação de cor (Tampa Preta 5, Tampa Cinza 2, Tampa Vermelha 2) — motivo: regra obrigatória de não agregar variações de cor em família genérica; cada variação com seu volume próprio.
- ASIN omitido de todos os produtos do Top Produtos — motivo: todos os itens remanescentes têm confidence high e títulos suficientemente identificáveis (não há ambiguidade de título igual para produtos diferentes); nenhum item com risco médio de identificação permaneceu no ranking após omissões.
- Quebra de frase no segundo insight da ANÁLISE — motivo: frase original era longa; aplicada quebra com ponto, mantendo todos os termos e a tese intacta.
- Prioridades do DIA formatadas com ação + por quê + confirmar/refutar + escalar se — motivo: estrutura exigida pelo prompt; conteúdo vindo diretamente das `prioridades_condensadas` da Condensadora sem adição analítica própria.
- `buy_box` não declarada como validada em nenhum ponto da mensagem — motivo: bloqueio Condensadora; preservada como lacuna aberta na ANÁLISE e como ação nas PRIORIDADES.
- Comparações temporais (+57% vs 30d, +93% vs mesmo dia da semana) ausentes da seção VISÃO AMAZON — motivo: regra do prompt; comparações pertencem à ANÁLISE; a trajetória ascendente foi mencionada na ANÁLISE, não na VISÃO.
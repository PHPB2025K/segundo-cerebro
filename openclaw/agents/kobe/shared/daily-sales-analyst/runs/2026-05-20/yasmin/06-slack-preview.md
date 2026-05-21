<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.057,51
- Pedidos: 90
- Ticket médio: R$ 56,19
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 22 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
- Kit 6 Canequinhas 100ml — 8 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos

🔍 ANÁLISE DA CONTA
- A dependência da conta não está num produto líder — está numa categoria inteira: as duas famílias de potes herméticos de vidro somaram 57% dos pedidos do dia em múltiplos anúncios. Uma ruptura de fornecimento ou mudança de regra ML nessa categoria atinge mais da metade do canal de uma vez — a leitura de concentração no top 3 subestima o risco real.
- A checagem do Kit 06 Canequinhas Acrílico não é preventiva — é possivelmente corretiva: o item tinha 3 unidades disponíveis e realizou 3 pedidos ontem em anúncio fulfillment ativo. A ruptura pode já ter ocorrido hoje — a ação é verificar se já rompeu e agir, não prevenir.
- O GMV ficou acima da banda histórica, mas a execução tem fragilidade nos líderes de fulfillment: o Kit 4 Potes 1050ml Retangular (2º em volume, 13 pedidos) e o Conjunto 5 Potes Tampa Vermelha (5º, 5 pedidos) operam com health abaixo do threshold de 0,85. O risco de erosão de exposição orgânica não está nos itens marginais — está nos que sustentaram o resultado.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar no painel ML o estoque real do Kit 06 Canequinhas Acrílico — o item tinha 3 unidades no snapshot e realizou 3 pedidos ontem em fulfillment ativo; ruptura pode já ter ocorrido. Se estoque em 0: pausar anúncio imediatamente para conter penalidade de reputação. Se acima de 3: agir ainda hoje, a janela é de ~1 dia. Verificar também o Kit 6 Canecas Porcelana Tulipa Lisa 250ml (~20 unidades, ~4 dias de cobertura com o ritmo atual): definir reposição antes da ruptura. Confirmar/refutar por: estoque real no painel vs snapshot de hoje. Escalar se: Kit 06 em 0 e reposição impossível hoje — pausar sem esperar.
- Yasmin: checar no painel ML a health atual do Kit 4 Potes 1050ml Retangular e do Conjunto 5 Potes Tampa Vermelha e comparar com a semana passada. Por quê: os dois operam com health abaixo de 0,75 em fulfillment e foram o 2º e 5º em volume ontem — se a health estiver caindo, a conta perde exposição orgânica nos produtos que sustentam o núcleo do canal. Confirmar/refutar por: se ambos estáveis ou melhorando, manter observação sem ação; se qualquer um caindo, avaliar listing e alinhar com Himmel para checar impacto em exposição. Escalar se: health de qualquer um dos dois cair por 2 dias seguidos.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL6250 — display_name interno "Kit 6 Tigelas de Vidro 250ml"
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** display_name interno incorreto — raw_title e platform_item_id identificam o produto real como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" (porcelana, não vidro; categoria comercial distinta)
- **Agregado autorizado:** não aplicável; a Granular autorizou explicitamente o uso do raw_title como referência correta
- **Tratamento aplicado:** citado na mensagem com o raw_title "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"
- **Aparece na mensagem final:** sim, como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"

---

- **Item bloqueado:** KIT10YW1050, SPC0111, KIT4YW320, 914C_BAV — quatro itens com confidence medium e mapping_reason generic_sku
- **Origem do bloqueio:** Condensadora
- **Motivo:** risco de nome comercial impreciso; Condensadora determinou não citar com precisão em análise de mix ou Top Produtos
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitidos do Top Produtos; 914C_BAV (Kit 06 Canequinhas Acrílico) aparece em PRIORIDADES com o nome usado explicitamente pela Condensadora em prioridades_condensadas — uso autorizado pelo próprio output da Condensadora naquele contexto
- **Aparece na mensagem final:** KIT10YW1050, SPC0111, KIT4YW320 — não. 914C_BAV — sim, somente em PRIORIDADES como "Kit 06 Canequinhas Acrílico"

---

- **Item bloqueado:** breakdown de cancelamentos por produto ou fulfillment
- **Origem do bloqueio:** Condensadora (dado não disponível no pacote)
- **Motivo:** pacote não contém detalhamento por platform_item_id dos 3 cancelamentos do dia
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados apenas como total (3) em VISÃO, sem atribuição
- **Aparece na mensagem final:** não, além do total objetivo

---

- **Item bloqueado:** variação de posição de ranking dos líderes vs últimos 7 dias
- **Origem do bloqueio:** Condensadora (dado não disponível no pacote)
- **Motivo:** histórico de posição de ranking não consta no pacote; afirmação seria especulação
- **Tratamento aplicado:** não citado
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** atribuição ADS vs orgânico do produto líder (Conjunto 5 Potes Tampa Preta, 22 pedidos)
- **Origem do bloqueio:** Condensadora (dado não disponível no pacote)
- **Motivo:** breakdown de revenue ADS por platform_item_id ausente no pacote
- **Tratamento aplicado:** não citado
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- `TL6250 citado como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" em vez do display_name interno — motivo: bloqueio do display_name incorreto respeitado; raw_title autorizado pela Granular como referência correta`
- `KIT10YW1050 omitido do Top Produtos apesar de 5 pedidos (empatado com IMB501V e TL6250) — motivo: confidence medium + mapping generic_sku; Condensadora não autorizou agregado para Top Produtos`
- `SPC0111, KIT4YW320 omitidos do Top Produtos — motivo: mesma regra; confidence medium + mapping generic_sku`
- `914C_BAV omitido do Top Produtos mas citado em PRIORIDADES como "Kit 06 Canequinhas Acrílico" — motivo: Condensadora usou esse nome explicitamente em prioridades_condensadas; a restrição da Condensadora é sobre análise de mix, não sobre ações operacionais nomeadas pela própria Condensadora`
- `Ranking do Top Produtos mantido em ordem decrescente por pedidos; omissão dos itens bloqueados não alterou ordem relativa dos itens incluídos`
- `Metadados internos removidos dos três insights ("base: Granular", "base: Operacional + Granular", "base: Granular + Tática") — motivo: regra de formatação; teses preservadas integralmente`
- `Insight 2 preservou contraste "não é preventiva — é possivelmente corretiva" e a nuance de confiança média ("pode já ter ocorrido") — motivo: regra de não trocar hipótese por fato e de não suavizar tom`
- `Insight 3 manteve "abaixo do threshold de 0,85" com os valores de health — motivo: métrica que apoia compreensão imediata da ação, não uso de métrica como manchete`
- `Comparações temporais (vs 7d, vs 30d, vs mesmo dia da semana) não incluídas em VISÃO MERCADO LIVRE — motivo: VISÃO contém apenas dados objetivos do dia; comparação é interpretação e pertence à ANÁLISE`
- `DADOS_PARCIAIS registrado: o status parcial é originado da Shopee Store (volume fora da banda 30d), não do ML; reconciliação e volume band do ML estão OK; nenhuma ressalva de dado parcial foi necessária na mensagem Yasmin`
- `IMB501V (Tampa Vermelha) e IMB501P (Tampa Preta) mantidos como linhas separadas — motivo: variações vendáveis distintas da família IMB501; regra proíbe agregar por família quando há variações reais`
- `Variação de posição de ranking dos líderes de health não citada — motivo: histórico de ranking ausente no pacote; dado bloqueado pela Condensadora como especulação`
<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 15/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 878,00
- Pedidos: 27
- Ticket médio: R$ 32,52
- Cancelamentos: 0
- Fulfillment: 27/27 FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml — 7 pedidos
- Suporte Controle Gamer — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 4 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml — 1 pedido
- Suporte de Controle PS5 PS4 Xbox Series X/S One e Headset (Cru) (ASIN: B0GTQXRDTM) — 1 pedido

🔍 ANÁLISE DA CONTA
A conta chegou a 27 pedidos — dentro da banda histórica em todas as janelas disponíveis — e ainda assim gerou R$ 878,00. Não é queda de demanda; é que cada venda vale ~20% menos do que o padrão da conta, e isso já aparecia no 60d, então não é ruído de hoje.

Os dois líderes do dia concentraram 44% dos pedidos com identificação de alta confiança — enquanto os oito produtos restantes com 1 pedido cada não formaram cauda suficiente para compensar. A conta não tem segundo vetor de volume com ticket mais alto funcionando: a estrutura confirma que o GMV está refém da composição dos dois líderes, e enquanto eles dominarem o mix, o ticket médio tende a ficar estruturalmente abaixo do histórico.

O diagnóstico recomendado — verificar Buy Box e elegibilidade nos ASINs de maior ticket — não pode ser concluído pelo relatório automático: esses dados precisam ser buscados diretamente na plataforma. A ausência não invalida a tese; confirma que a investigação é manual.

🎯 PRIORIDADES DO DIA
- Leonardo: verificar Buy Box e FBA dos ASINs com perfil de ticket historicamente mais alto — Conjunto 5 Potes de Vidro Tampa Preta, Kit 6 Xícaras Porcelana Paris e Kit 2 Potes de Vidro 1050ml Retangular são os candidatos prioritários. Se Buy Box ≥ 85% e FBA elegível nesses listings: o problema é mix/exposição orgânica. Se Buy Box baixa ou indisponível em algum deles: o problema é operacional e precede qualquer discussão de ADS. Checagem em até 24h. Escalar para Pedro apenas após consolidar o diagnóstico com evidência de qual ASIN tem problema operacional confirmado.
- Leonardo: registrar o ticket médio de hoje (R$ 32,52) e a tese inaugural da conta na memória semanal/mensal — sem esse registro, a análise de amanhã parte do zero e o padrão não pode ser confirmado ou refutado.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL250P — display_name "Tigela de Vidro 250ml" (ASIN B0GGTY2BLT)
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** Display_name incorreto — raw_title do pedido real indica "Kit 6 Canecas de Porcelana Tulipa 250ml"; categorias distintas (porcelana vs vidro, caneca vs tigela)
- **Agregado autorizado:** não — Condensadora não autorizou agregado explícito para este item
- **Tratamento aplicado:** omitido do ranking Top Produtos
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** TL6250 — display_name "Kit 6 Tigelas de Vidro 250ml" (ASIN B0GFPQD4G9)
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** Display_name incorreto — raw_title do pedido real indica "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas"; mesma família de erro de TL250P
- **Agregado autorizado:** não — Condensadora não autorizou agregado explícito para este item
- **Tratamento aplicado:** omitido do ranking Top Produtos
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos ("base: Estratégica + Operacional + Granular", "Padrão C/D/E", referências a "a Granular marcou", "a Tática recomenda") — regra de tom: nomes de camadas internas não aparecem no Slack
- TL250P e TL6250 omitidos do Top Produtos — bloqueio recebido da Granular/Condensadora; display_name incorreto; sem agregado autorizado pela Condensadora
- SPC013 mantido no ranking com ASIN visível — confiança média de identificação (mapping_reason: raw_sku_normalized_with_short_title_fallback); título truncado no pacote tornava a identificação ambígua sem o ASIN
- KIT2PANO800AZ omitido do Top Produtos — confidência média e título de baixa distintividade; com TL250P e TL6250 já omitidos, o ranking ficou com 5 itens naturalmente, sem necessidade de preencher com produto de confiança menor
- KJP0041 omitido do Top Produtos — confiança média; com 5 itens já no ranking (top 5 natural por volume), omissão não distorce o ranking
- TL6250 e TL250P representavam as posições 6 e 9 do ranking original — sua omissão não afetou o top 5 apresentado
- Preservação da nuance "sugere/parece/não invalida a tese" nos insights — Condensadora marcou confiança média; hipóteses de ticket por produto e Buy Box mantidas como hipóteses, não convertidas em fato
- Quebra de frases longas em dois pontos na seção de análise — mantidos todos os termos analíticos, tese intacta e conectivos originais (especialmente o "não é... é que" da inversão do insight 1)
- Seção VISÃO sem comparação temporal — valores objetivos do dia apenas; comparações permanecem na ANÁLISE DA CONTA conforme regra de seção
- Ticket médio na seção VISÃO sem casas decimais extras: R$ 32,52 (2 casas) — padrão numérico obrigatório aplicado
- Prioridade de registro de memória mantida como ação explícita para Leonardo — Condensadora marcou como "não aplicável para escalonamento" mas incluiu nas prioridades para Slack; mantida
- Rodapé com data de análise: 15/05/2026 — data do dia analisado (ontem em relação a 2026-05-16), não data de execução
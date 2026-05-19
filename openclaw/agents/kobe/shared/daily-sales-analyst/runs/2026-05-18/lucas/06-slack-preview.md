<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 18/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Total Shopee: 84 pedidos — R$ 4.768,84 — Ticket médio: R$ 56,77
• Cancelamentos: 3 (todos na Store)
• Budamix Store: 59 pedidos — R$ 2.497,44
• Budamix Oficial (Conta 2): 16 pedidos — R$ 1.570,30
• Budamix Shop (Conta 3): 9 pedidos — R$ 701,10

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 27 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 18 pedidos
• Kit 6 Canecas Tulipa 250ml — 15 pedidos
• Kit 4 Potes de Vidro 800ml Quadrado (Conta 2) — 4 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 4 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 3 pedidos
• Kit 9 Potes Vidro Quadrados (Conta 2) — 3 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* O resultado consolidado da Shopee é enganoso: quase 53% do GMV veio da Store com queda real sustentada, e as outras duas contas somaram apenas 25 pedidos com dado de confiança parcial — o que parece um canal fraco pode ser parcialmente artefato de coleta, e tratar as três contas como bloco único levaria a diagnóstico e ação errados. O único sinal cross-account confiável hoje é o Kit 6 Canecas Tulipa 250ml nos tops das três lojas simultaneamente, com 15 pedidos totais distribuídos de forma desproporcionalmente pesada nas contas menores — indício de sobreposição de mix entre contas que precisa de confirmação histórica antes de virar decisão.

🟠 *Budamix Store (Shopee 1):* A Store entregou o volume da plataforma rodando sobre dois produtos — Conjunto 5 Potes Redondos Tampa Preta (27 pedidos) e Jarra Medidora 500ml (18 pedidos) somaram 76% dos pedidos válidos, com uma cauda de 6 produtos respondendo por apenas 7 pedidos totais, o que não amortece nada em caso de qualquer oscilação nos campeões. A queda em todas as janelas históricas (7d, 30d, 60d, mesmos domingos) é consistente e não é ruído; o ticket levemente mais alto é efeito de mix comprimido, não de demanda qualificada — a conta está vulnerável, não acomodada, e a causa (exposição, ADS, demanda) ainda não está identificada.

🟠 *Budamix Oficial (Shopee 2):* A conta entregou o maior ticket do dia (R$ 98,14 vs histórico de ~R$ 60,00) sobre apenas 16 pedidos, com mix concentrado em kits de alto valor (Kit 4 Potes 800ml Quadrado, Kit 6 Canecas Tulipa, Kit 5 Potes Redondos Tampa Cinza e Kit 9 Potes Quadrados), o que estruturalmente sustenta ticket elevado — mas há sinalização de confiança parcial para esta conta e o volume -47% vs 30d pode ser dado incompleto tanto quanto colapso real. Sem confirmação de completude do dado, qualquer diagnóstico de queda ou de mix qualificado é desonesto: a conta está inconclusiva e nenhuma ação deve ser tomada com base no dado de hoje.

🟠 *Budamix Shop (Shopee 3):* A conta teve 9 pedidos distribuídos em exatamente 1 pedido por hora em 9 horas distintas — padrão incompatível com operação comprimida normal e mais próximo de piso residual ou dado incompleto (confiança parcial sinalizada na validação dos dados). Com -66% vs 30d e -62% vs mesmo domingo histórico, se o dado for completo é queda crítica que exige diagnóstico imediato de exposição; se for incompleto, é artefato — e essa distinção precisa ser resolvida antes de qualquer ação, porque os dois cenários têm respostas opostas.

🎯 PRIORIDADES DO DIA
• Lucas: confirmar se os dados de Oficial-2 e Shop-3 estão completos para 18/05 — checar no sistema de origem se houve sincronização pendente, janela de corte ou atraso de integração. É o pré-requisito que desbloqueia o diagnóstico das duas contas. Confirmar por: dado completo + volumes abaixo das bandas por mais 2 ciclos = queda real. Escalar se: queda confirmada → diagnóstico de exposição via Himmel, por conta, não de forma consolidada.
• Lucas: verificar nos painéis de listagem se a exposição do Conjunto 5 Potes Redondos Tampa Preta e da Jarra Medidora 500ml está normal na Store — são os dois produtos que sustentam 76% do volume da conta principal. Confirmar por: exposição normal → hipótese se desloca para demanda ou preço. Escalar se: exposição reduzida ou anúncios inativos → alinhar com Himmel especificamente sobre esses dois produtos na Store.
• Lucas: não acionar Himmel para nenhuma das três contas com base nos dados de hoje — Store sem causa identificada, Oficial-2 e Shop-3 com dado parcial. Qualquer ajuste de ADS agora é cego. Aguardar confirmação de completude de dado e checagem de exposição antes de qualquer escalada.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: produtos específicos associados aos 3 cancelamentos da Store
- Origem do bloqueio: Granular + Condensadora
- Motivo: dado de cancelamento por produto não disponível no pacote; citar produto cancelado seria invenção
- Agregado autorizado: não
- Tratamento aplicado: reportado apenas o total "3 cancelamentos (todos na Store)" na seção VISÃO SHOPEE, sem produto identificado
- Aparece na mensagem final: sim, como total agregado sem produto

---

- Item bloqueado: "Pote de Vidro Hermético 800ml" — display_name do SKU 098 (Oficial-2)
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name incorreto; produto real do pedido é "Kit 9 Potes Vidro Quadrados" conforme raw_title
- Agregado autorizado: sim, raw_title "Kit 9 Potes Vidro Quadrados"
- Tratamento aplicado: substituído por "Kit 9 Potes Vidro Quadrados" em Top Produtos e na análise da Oficial-2
- Aparece na mensagem final: sim, como "Kit 9 Potes Vidro Quadrados (Conta 2)"

---

- Item bloqueado: ITEM:57356981475 ("Conjunto 5 Potes Vidro Kit Vasilhas..." — Store)
- Origem do bloqueio: Granular + Condensadora
- Motivo: sem SKU interno, confiança medium, possível variação não mapeada de IMB501; 1 pedido residual
- Agregado autorizado: não (Condensadora autorizou apenas referência à "cauda da Store" de forma genérica, sem nomear produto)
- Tratamento aplicado: omitido do ranking de Top Produtos
- Aparece na mensagem final: não

---

- Item bloqueado: FITA500M ("Kit 6/12 Rolos de Fita Adesiva Transparente 45mm x 500m" — Store)
- Origem do bloqueio: Granular + Condensadora
- Motivo: produto fora de categoria principal, confiança medium, 1 pedido residual; não representa vetor real de vendas
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking de Top Produtos
- Aparece na mensagem final: não

---

- Item bloqueado: afirmação de canibalização confirmada entre contas via CTL002
- Origem do bloqueio: Condensadora (Granular)
- Motivo: é indício, não fato; peso proporcional alto nas contas menores é parcialmente efeito de denominador pequeno (9 e 16 pedidos)
- Agregado autorizado: sim, como "indício de sobreposição de mix entre contas que precisa de confirmação histórica"
- Tratamento aplicado: preservada a qualificação de hipótese no bloco Consolidado
- Aparece na mensagem final: sim, como indício qualificado (não como fato)

---

- Item bloqueado: diagnóstico afirmativo de queda real na Oficial-2 e na Shop-3
- Origem do bloqueio: Condensadora
- Motivo: ambas as contas com dado de confiança parcial; queda real e dado incompleto têm peso equivalente como hipóteses
- Agregado autorizado: sim, como "inconclusivo — dado parcial"
- Tratamento aplicado: preservado como inconclusivo nos blocos individuais de cada conta
- Aparece na mensagem final: sim, como inconclusivo (não como queda confirmada)

---

### Decisões de formatação

- Remoção do código SKU "CTL002" do bloco Consolidado da análise 06b — motivo: sem SKU cru visível em Shopee; produto citado pelo nome completo "Kit 6 Canecas Tulipa 250ml"
- Remoção dos códigos "IMB501P" e "CK4742" do bloco Store da análise 06b — mesmo motivo; produtos citados pelos nomes completos com contagem de pedidos preservada
- Remoção dos códigos "IMB501P" e "CK4742" da prioridade 2 da 06b — mesmo motivo; substituídos pelos nomes completos dos produtos
- Substituição de "runner sinalizou confiança parcial" por "há sinalização de confiança parcial" no bloco Oficial-2 — motivo: evitar referência a infraestrutura técnica interna
- Substituição de "confiança parcial confirmada pelo runner" por "confiança parcial sinalizada na validação dos dados" no bloco Shop-3 — mesmo motivo
- Uso de raw_title "Kit 9 Potes Vidro Quadrados" no lugar de display_name "Pote de Vidro Hermético 800ml" no ranking e na análise — conforme bloqueio Granular/Condensadora com agregado autorizado
- Formato monetário aplicado: "R$98" → "R$ 98,14", "~R$60" → "~R$ 60,00" no bloco Oficial-2 — padrão numérico obrigatório; valor preciso extraído do pacote de dados
- Cabeçalho da seção de análise ajustado para "🔍 ANÁLISE DAS CONTAS" — regra addendum v3.1: usar "ANÁLISE DAS CONTAS" quando 06b disponível
- Indicação de conta aplicada para produtos em apenas 1 conta: Conjunto 5 Potes Tampa Preta (Store), Jarra Medidora 500ml (Store), Kit 4 Potes 800ml Quadrado (Conta 2), Conjunto 5 Potes Tampa Cinza (Conta 2), Kit 9 Potes Vidro Quadrados (Conta 2) — regra: indicar conta quando produto vendeu em menos de 2 contas
- Sem indicação de conta para Kit 6 Canecas Tulipa 250ml (3 contas) e Kit 2 Potes 800ml Quadrado (Store + Shop-3) — regra: sem indicação quando vendido em 2 ou mais contas
- ITEM:57356981475 e FITA500M omitidos do ranking — bloqueio recebido sem agregado autorizado; cada um com 1 pedido residual e confiança medium
- Produtos com 2 pedidos ou menos (KIT3S099, 914C, KIT6CAR200, KIT6S097, KIT4YW1050) omitidos do ranking — sem representatividade suficiente para o top e abaixo do piso de 3 pedidos dos itens incluídos; nenhum deles bloqueado, apenas fora do corte de relevância
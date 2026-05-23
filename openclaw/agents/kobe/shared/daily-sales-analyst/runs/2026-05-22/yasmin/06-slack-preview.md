<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84 pedidos
- Ticket médio: R$ 55,02
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 11 pedidos
- Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha — 10 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 6 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 4 pedidos
- Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida — 3 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 3 pedidos
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 2 pedidos

🔍 ANÁLISE DA CONTA
- O GMV ficou dentro da banda esperada para sexta-feira, mas o mecanismo que entregou esse resultado dá sinais de deterioração: os dois principais anúncios em Full têm health abaixo do limiar do ML — Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (0,75) e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (0,71) — e ADS pode estar compensando a exposição orgânica que esses anúncios perderam, respondendo por 69,8% do GMV. O número parece normal; a estrutura que o gerou, não.
- O Kit 6 Canecas Porcelana Tulipa Lisa 250ml está com cobertura de aproximadamente 2 dias em modalidade Full (12 unidades ao ritmo de 6 pedidos/dia). Em Full, ruptura remove o anúncio da vitrine do ML imediatamente, sem possibilidade de reação no mesmo dia. O risco começa amanhã.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar na plataforma ML a direção do health do Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (modalidade Full, Catálogo, health atual 0,71) e checar se a posição de Buy Box foi afetada. Anúncio em Catálogo com health abaixo de 0,85 perde Buy Box — mecanismo mais grave e mais lento de reverter do que anúncio Clássico; a direção do health define se a conta segue em observação ou se é preciso acionar Himmel para cobertura preventiva nesse anúncio. Confirmar/refutar por: health estável ou em recuperação por 2 dias consecutivos → continuar observando sem ação; health abaixo de 0,65 ou perda de Buy Box confirmada nos próximos 2 dias → acionar decisão. Escalar se: health cair abaixo de 0,65 ou perda de Buy Box confirmada nas próximas 48h → alinhar com Himmel sobre cobertura preventiva nesse anúncio.
- Yasmin: confirmar se há reposição encaminhada para o Kit 6 Canecas Porcelana Tulipa Lisa 250ml (modalidade Full, 12 unidades pós-baixa) antes de D+2. Em Full, ruptura elimina a posição do anúncio no CD do ML sem reação possível no mesmo dia; confirmar reposição hoje é a única ação que neutraliza o risco antes da ruptura. Confirmar/refutar por: reposição confirmada ou em trânsito nas próximas 24h → risco neutralizado; ausência de plano → registrar data provável de ruptura como variável confundidora na leitura dos próximos dias.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de que a inversão de modalidade de envio no top10 (Cross-Docking 52,9% vs Full histórico 73,7%) indica mudança estrutural no mix da conta
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou que a divergência é produto-específica e episódica — gerada pela liderança pontual de Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta (20 de 68 pedidos no top10); padrão Full-dominante permanece estrutural nas janelas 7d e 30d
- **Agregado autorizado:** não
- **Tratamento aplicado:** item omitido da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmação sobre a direção do health dos campeões Full (caindo, estável ou em recuperação)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** apenas valores pontuais disponíveis no pacote — série temporal D-7 a D-1 ausente; declarar direção seria especulação não suportada pelos dados
- **Agregado autorizado:** não
- **Tratamento aplicado:** health mencionado apenas como valor pontual (0,75 e 0,71) sem qualquer afirmação de direção; direção preservada como incógnita nas prioridades ("verificar a direção do health")
- **Aparece na mensagem final:** não (como afirmação de direção)

---

- **Item bloqueado:** Afirmação de que ADS está priorizando produtos em Cross-Docking em detrimento dos campeões Full
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** hipótese em aberto — breakdown de revenue ADS por platform_item_id ausente do pacote; não confirmável nem descartável
- **Agregado autorizado:** não
- **Tratamento aplicado:** hipótese de priorização Cross-Docking omitida; insight preserva apenas o que está no aprovado pela L05 — compensação da exposição orgânica perdida pelos campeões Full, em linguagem de indício ("pode estar compensando")
- **Aparece na mensagem final:** não (como afirmação); o mecanismo de compensação orgânica — parte do insight L05 aprovado — aparece em linguagem de indício conforme exigido pela classificação "risco latente"

---

- **Item bloqueado:** Referência aos KIT6YW1050 (MLB4676751119) e KIT10YW1050 (MLB4676726433) pelo display_name compartilhado "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas"
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** dois produtos distintos com platform_item_ids, estoques e volumes independentes compartilham o mesmo alias interno; referência pelo display_name funde os dois e distorce volumes
- **Agregado autorizado:** não — diferenciador correto são os display_short individuais, que já incluem "6 Unidades" e "10 Unidades"
- **Tratamento aplicado:** usados os display_short verbatim de cada produto: "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" e "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"
- **Aparece na mensagem final:** sim, com nomes corretos e diferenciados por quantidade

---

- **Item bloqueado:** Uso de "Claro" como nome completo do IMB501V (MLB3288536143) sem mencionar "Tampa Vermelha"
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** "Claro" no título ML descreve o vidro transparente, não a cor da tampa; "Tampa Vermelha" é o diferenciador de variação confirmado por SKU IMB501V via convenção interna determinística
- **Agregado autorizado:** não aplicável — atributo confirmado deve aparecer pelo protocolo de confirmed_variation_attributes
- **Tratamento aplicado:** produto referenciado em todo o documento como "Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha" (display_short + confirmed_variation_attributes)
- **Aparece na mensagem final:** sim, como "Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha"

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — presentes no JSON L05; não expostos na mensagem Slack
- Linguagem de indício preservada nos dois insights (classificação "risco latente"): "dá sinais de deterioração", "pode estar compensando", "O número parece normal; a estrutura que o gerou, não" — tese e estrutura da L05 mantidas sem alteração
- Omissão de modalidade de envio na seção VISÃO — `fulfillment_mix_yesterday_top10` cobre 68 de 84 pedidos (~81%, apenas top10 weighted); L05 não autorizou exibição com ressalva de cobertura nessa seção; dado tratado exclusivamente na ANÁLISE via insight aprovado pela L05
- Simplificação "D+1" → "amanhã" no insight 2 — linguagem operacional direta sem perda de sentido; tese e urgência preservadas
- Atribuição de Yasmin como responsável em ambas as prioridades — L05 não atribui responsável; atribuição feita pela L06 conforme regra (Yasmin = responsável operacional ML)
- `display_short` usado verbatim em todos os 10 produtos do Top Produtos — nenhuma palavra alterada, nenhuma abreviação adicional
- `confirmed_variation_attributes` concatenados ao `display_short` em três itens: IMB501P ("Tampa Preta"), IMB501V ("Tampa Vermelha"), IMB501C ("Tampa Cinza") — atributos autoritativos via SKU, não inferência textual
- IMB501P e IMB501C compartilham o mesmo `display_short` ("Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças") — diferenciação garantida pelos `confirmed_variation_attributes` "Tampa Preta" e "Tampa Cinza" respectivamente; sem risco de fusão
- CLR002 `display_short` usado verbatim apesar do comprimento: "Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida" — nenhum `display_short` mais curto disponível; fallback não aplicável (campo preenchido)
- Quebra interna no insight 1: trecho com os dois produtos e seus valores de health isolado entre travessões ("— [produto A (0,75)] e [produto B (0,71)] —") para facilitar leitura sem alterar tese ou termos analíticos
- Convergência cross-layer confirmada: nomes dos produtos na ANÁLISE e PRIORIDADES coincidem com os nomes do Top Produtos — sem divergência de denominação entre seções
- Prioridade 2: campo `escalar_se` da L05 marcado como "Não aplicável" — linha "Escalar se" omitida da mensagem conforme a ausência de condição real de escalonamento
- Confiança média (L05): sem ressalva explícita de "leitura limitada" ou "sem base para cravar" — nível médio não exige linguagem de baixa confiança; nuance de risco latente preservada pela classificação dos insights
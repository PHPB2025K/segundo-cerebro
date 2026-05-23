<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84
- Ticket médio: R$ 55,02
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes 1050ml — 11 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Tulipa 250ml — 6 pedidos

🔍 ANÁLISE DA CONTA
- O GMV ficou praticamente no mesmo patamar de sextas anteriores (R$ 4.622,03 vs média de R$ 4.718,81 do mesmo dia da semana), mas quem sustentou o número foi o ticket médio (R$ 55,02 vs R$ 45,00 no 30d), não o volume — pedidos caíram em todas as janelas. A leitura correta é acomodação por mix qualificado, não queda de demanda.
- Mercado Ads carregou 69,9% do GMV (ROAS 10,87x, ACOS 4,57%) pelo segundo ciclo seguido. Os números são bons, mas o orgânico residual ficaria abaixo do ritmo mínimo do MercadoLíder Gold se as campanhas parassem. Os dois anúncios Full que historicamente sustentam a conta seguem com nível de qualidade do anúncio em Padrão inferior (0,75 e 0,71) — segundo ponto pontual, direção não confirmada; a base orgânica está deteriorando de forma silenciosa enquanto o ADS segura o resultado.
- O Kit 6 Canecas Tulipa 250ml em Full fechou com 7 unidades após 6 pedidos de ontem. A cobertura prospectiva é de cerca de 1 dia ao ritmo atual — se esgotar, o ML pausa o anúncio automaticamente e ele sai do ranking de categoria sem aviso prévio (sem health calculado, não há baseline para estimar o impacto). É o único ponto com janela curta real de hoje.

🎯 PRIORIDADES DO DIA
- Yasmin: checar o estoque atual do Kit 6 Canecas Tulipa 250ml em Full e confirmar se há reposição em trânsito para o CD do ML. Por quê: cobertura prospectiva de ~1 dia; ruptura em Full aciona pausa automática e remoção do ranking de categoria sem sinal prévio. Confirmar por: acima de 20 unidades com reposição confirmada em ≤72h = risco neutralizado; abaixo de 5 ou status pausado = registrar como variável confundidora e avaliar reposição emergencial. Escalar se: estoque ≤ 2 unidades sem reposição em trânsito confirmada.
- Yasmin: observar a direção do nível de qualidade dos dois campeões Full — Kit 4 Potes 1050ml Azul-petróleo (0,75) e Potes Vidro 5 Peças — Tampa Vermelha (0,71) — no próximo pacote, comparando com os valores atuais. Por quê: é o segundo ponto sequencial em Padrão inferior; a direção é o que transforma a hipótese de erosão orgânica em tendência confirmada ou a descarta. Confirmar por: health estável ou em recuperação em pelo menos um dos dois = manter observação sem ação por mais 2 ciclos; health caindo nos dois = alinhar com Himmel sobre cobertura ADS preventiva. Escalar se: health caindo nos dois anúncios simultaneamente no próximo ciclo.
- Yasmin: registrar os números de ADS de hoje como terceiro ponto da série — sem alterar campanha. Por quê: ROAS 10,87x e ACOS 4,57% em fase de leitura nascente não se tocam; o que importa agora é construir a série para distinguir flutuação de dependência estrutural. Confirmar por: ADS share acima de 65% pelo terceiro/quarto ciclo seguido = dependência confirmada como padrão operacional; share abaixo de 55% sem alteração por Himmel = sinal de tração orgânica crescente. Escalar se: ADS share acima de 65% por 4+ ciclos consecutivos com ROAS ainda acima de 5x.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de direção do health dos campeões Full (caindo/estável/recuperando)
- **Origem do bloqueio:** L04 Granular + L05 Condensadora
- **Motivo:** Pacote traz apenas valor pontual de health, sem série temporal — qualquer direção afirmada seria invenção
- **Agregado autorizado:** sim — `"segundo ponto pontual em Padrão inferior, direção não confirmada"`
- **Tratamento aplicado:** substituído pelo agregado autorizado; sem afirmação de trajetória
- **Aparece na mensagem final:** sim, como `"segundo ponto pontual em Padrão inferior (0,75 e 0,71) — direção não confirmada"`

---

- **Item bloqueado:** Atribuição de causa específica a ADS por anúncio (ex.: ADS empurrando Cross-Docking ou compensando Full penalizado)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** ads_summary é agregado total da conta; breakdown por platform_item_id ausente — pendência desde ciclo anterior
- **Agregado autorizado:** sim — apenas share agregado da conta (69,9%)
- **Tratamento aplicado:** reportado apenas share agregado (69,9% do GMV), ROAS e ACOS; sem atribuição por anúncio
- **Aparece na mensagem final:** sim, como share agregado

---

- **Item bloqueado:** Leitura alarmista do mix de modalidade de envio invertido (52,9% Cross-Docking)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Divergência produto-específica pelo cluster IMB501; Cross-Docking é modalidade legítima da Budamix
- **Agregado autorizado:** não aplicável — item simplesmente não gerou alerta na mensagem
- **Tratamento aplicado:** omitido como alerta; mix de modalidade de envio não foi citado na seção VISÃO (cobertura parcial do top10) nem como alerta na análise
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** MLB (platform_item_id) na narrativa
- **Origem do bloqueio:** L05 Condensadora + regra estrutural ML
- **Motivo:** Regra ML — usar nome comercial; MLB só em memória técnica
- **Agregado autorizado:** sim — nomes comerciais curtos (slack_short_name)
- **Tratamento aplicado:** todos os produtos referenciados por nome canônico curto; nenhum MLB visível
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Alerta sobre Kit 10 Potes Herméticos 320ml 10 Unidades em Cross-Docking (6 unidades)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Granular classificou como risco secundário com confiança baixa (amostra de 1 dia); Cross-Docking permite reposição mais ágil; não atinge limiar de Slack
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Discussão com Kobe sobre dependência estrutural de ADS
- **Origem do bloqueio:** L05 Condensadora (bloqueio tático)
- **Motivo:** Gatilho é 4+ ciclos consecutivos; hoje é segundo ponto — hipótese nascente, não padrão confirmado
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido; escalonamento para Kobe não incluído nas prioridades
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- **Metadados internos removidos** — campos `padrao`, `base` e `classificacao` não aparecem na mensagem; são metadados de pipeline
- **Insight 1 (fato):** escrito como fato, sem linguagem de indício — `classificacao: "fato"` preservado no tom
- **Insight 2 (risco latente):** linguagem de indício preservada — "está deteriorando de forma silenciosa", "segundo ponto pontual, direção não confirmada"; proibido transformar em certeza
- **Insight 3 (risco latente):** linguagem de indício preservada — "cobertura prospectiva de cerca de 1 dia"; sem afirmação retrospectiva de pedidos sem cobertura (risco é prospectivo)
- **Estoque como prospectivo (regra obrigatória):** texto redigido como risco futuro ("se esgotar, o ML pausa"); nenhuma afirmação retrospectiva de "pedidos sem cobertura" ou "déficit de estoque"
- **Nomes de produto traduzidos para slack_short_name (mapeamento canônico):**
  - IMB501P (Tampa Preta) → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - KIT4YW1050 → usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
  - IMB501V (Tampa Vermelha) → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501C (Tampa Cinza) → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - TL6250 → usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)
- **Top Produtos: exatamente os 5 primeiros** do `top_products` exibidos; posições 6-10 usadas apenas internamente pelas camadas analíticas
- **Faturamento por produto não incluído** — pacote não traz campo explícito de receita validada por produto/variação; formato usado: `[nome] — [pedidos] pedidos`
- **Modalidade de envio omitida da seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas 68 dos 84 pedidos (top 10, ~81% de cobertura); dado não representa a totalidade do dia sem ressalva; Condensadora não autorizou explicitamente inclusão com cobertura explícita
- **Nomes de produto nas seções Análise e Prioridades:** L05 usou títulos longos nos insights (ex.: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml", "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo", "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — Tampa Vermelha"); todos traduzidos para `slack_short_name` na mensagem final:
  - L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" → L06 usou "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico TL6250)
  - L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa Azul-petróleo" → L06 usou "Kit 4 Potes 1050ml Azul-petróleo" (mapeamento canônico KIT4YW1050, com atributo de cor mantido por relevância operacional no contexto de health)
  - L05 escreveu "Jogo Potes De Vidro 5 Peças Claro" / "Tampa Vermelha" → L06 usou "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico IMB501V)
- **Terminologia "nível de qualidade do anúncio"** usada no lugar de "health" — Yasmin não conhece o termo técnico; valores numéricos entre parênteses mantidos para contexto operacional nas prioridades
- **Responsável atribuído como Yasmin** em todas as prioridades — L05 não atribui responsável; L06 atribui conforme regra fixa
- **Escalonamento para Himmel preservado** nas prioridades 2 e 3, conforme `escalar_se` da L05; sem adição de escalonamento para Kobe (bloqueado pela L05)
- **Alternativas operacionais das prioridades preservadas** — "painel ML" e "fluxo logístico Budamix" mantidos como caminhos disponíveis para Yasmin na prioridade 1
- **Confiança média:** `alertas_de_confianca.nivel == "media"` — não requer ressalva global explícita, mas linguagem de indício nos insights de risco latente foi preservada rigorosamente
- **Seção DESTAQUES DO DIA:** não incluída (proibição estrutural)
- **Nome Pedro Broglio:** não incluído no cabeçalho (proibição estrutural)
- **Data do rodapé:** 22/05/2026, janela 00:00–23:59 BRT, conforme pacote (`timezone_brt: ok`)
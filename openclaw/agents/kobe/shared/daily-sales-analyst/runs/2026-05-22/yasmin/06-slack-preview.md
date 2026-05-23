<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.622,03
• Pedidos: 84
• Ticket médio: R$ 55,02
• Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 20 pedidos
• Kit 4 Potes 1050ml — 11 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 7 pedidos
• Kit 6 Canecas Tulipa 250ml — 6 pedidos

🔍 ANÁLISE DA CONTA
• O GMV ficou dentro da banda de sextas e até acima da média de 60 dias, mas o número está sendo sustentado por ticket mais alto, não por mais pedidos. Ticket subiu 22% em relação à média do mês e 30% em relação à média de 2 meses, enquanto pedidos caem em todas as janelas. Não é alcance crescendo — é mix mais caro segurando o faturamento.
• Os dois principais anúncios em modalidade de envio Full carregam nível de qualidade do anúncio em Padrão inferior (0,75 e 0,71) — mas há apenas um ponto medido. Não dá pra afirmar que estão em erosão. O que precisa acontecer é capturar a direção no próximo pacote; agir em campanha antes disso contamina o diagnóstico.
• O Kit 6 Canecas Tulipa 250ml está em risco concreto de pausa nas próximas 24-48h: 6 unidades pós-baixa após 6 pedidos ontem, sem nível de qualidade calculado pelo ML. Se o ML pausar antes da reposição chegar ao CD, vira variável confundidora que distorce a leitura de ranking, qualidade e GMV nos próximos ciclos. É o único ponto com janela de ação imediata.

🎯 PRIORIDADES DO DIA
• Yasmin: confirmar se há reposição programada do Kit 6 Canecas Tulipa 250ml para o CD do ML. Cobertura de ~1 dia — se pausar antes da reposição chegar, distorce a série de ranking e GMV dos próximos 3 ciclos. Confirmar/refutar por: próximo pacote com anúncio ativo e estoque reposto = risco neutralizado; anúncio pausado ou zerado sem reposição = registrar como variável confundidora e isolar leitura dos próximos 3 ciclos. Escalar se: anúncio pausar antes da reposição e o ritmo de pedidos se mantiver — alinhar com Himmel sobre reativação.
• Yasmin: verificar no próximo pacote o nível de qualidade do anúncio do Kit 4 Potes 1050ml e do Potes Vidro 5 Peças — Tampa Vermelha (hoje em Padrão inferior: 0,75 e 0,71) para definir a direção — caindo, estável ou em recuperação. Sem esse segundo ponto, a hipótese de erosão fica em aberto e não há base para acionar Himmel. Confirmar/refutar por: estável ou subindo em ambos = manter observação; qualquer um caindo, especialmente abaixo de 0,70 (faixa Básico) = alinhar com Himmel sobre cobertura ADS preventiva. Escalar se: qualquer dos dois cair para faixa Básico (<0,70) ou ambos saírem do top 5 por 2 ciclos consecutivos — alinhar com Himmel sobre cobertura ADS preventiva.
• Yasmin: registrar ADS share (69,9%), ROAS (10,87x), ACOS (4,57%) e gasto (R$ 296,96) como segundo ponto da série, sem acionar Himmel. Sem breakdown de receita ADS por anúncio, não dá pra separar se está amplificando os Cross-Docking saudáveis ou compensando a exposição perdida dos Full penalizados — a série de 2 a 3 ciclos resolve isso. Confirmar/refutar por: share acima de 65% com ROAS acima de 5x por mais 2 ciclos = dependência estrutural confirmada, abrir conversa com Kobe; share caindo abaixo de 50% sem queda de GMV = piso orgânico próprio validado. Escalar se: ROAS cair abaixo de 3x ou ACOS subir acima de 30% — acionar Himmel.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

`o_que_nao_pode_ir_para_slack` da L05 está vazio. Nenhum item foi bloqueado por L04 Granular ou L05 Condensadora neste ciclo.

---

### Decisões de formatação

**Top Produtos — tradução de nomes (item a item):**
- IMB501P — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- KIT4YW1050 — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
- IMB501V — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico; `confirmed_variation_attributes: ["Tampa Vermelha"]` já incorporado no nome canônico)
- IMB501C — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- TL6250 — usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)

**Tradução de nomes nas seções Análise e Prioridades:**
- Insight 3 (L05): "Tem um anúncio Full" (sem nome explícito) → L06 identificou como "Kit 6 Canecas Tulipa 250ml" a partir do contexto analítico (único produto Full no top com cobertura crítica de ~1 dia); padronizado com `slack_short_name` TL6250.
- Prioridade 1 (L05): "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" → "Kit 6 Canecas Tulipa 250ml" — padronização com `slack_short_name` TL6250 usado no Top Produtos.
- Prioridade 2 (L05): "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 4 Potes 1050ml" — padronização com `slack_short_name` KIT4YW1050 usado no Top Produtos.
- Prioridade 2 (L05): "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" → "Potes Vidro 5 Peças — Tampa Vermelha" — padronização com `slack_short_name` IMB501V usado no Top Produtos. Título ML genérico ("Claro") complementado por `confirmed_variation_attributes: ["Tampa Vermelha"]`, já incorporado no `slack_short_name`.

**Divergência de denominação cross-layer (nomes entre L05 e L06):**
- L05 prioridade 2 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo"; L06 escreveu "Kit 4 Potes 1050ml" — motivo: padronização com `slack_short_name` KIT4YW1050.
- L05 prioridade 2 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita"; L06 escreveu "Potes Vidro 5 Peças — Tampa Vermelha" — motivo: padronização com `slack_short_name` IMB501V; "Claro" é título ML enxuto, "Tampa Vermelha" é atributo confirmado por SKU (IMB501V → V = Vermelha).
- L05 insight 3 não nomeou o produto ("um anúncio Full"); L06 inseriu "Kit 6 Canecas Tulipa 250ml" — motivo: identificação única possível pelo contexto granular + cobertura crítica; `slack_short_name` TL6250.

**Metadados internos removidos:**
- `padrao`, `base` e `classificacao` omitidos da mensagem Slack em todos os insights conforme regra.
- Referências a camadas internas (Granular, Condensadora, L01-L05) não aparecem na mensagem.

**Preservação de nuance por classificação:**
- Insight 2 (`classificacao: "hipótese"`): mantida linguagem de indício — "não dá pra afirmar que estão em erosão"; evitado "estão em erosão" como fato. Os valores de nível de qualidade (0,75 e 0,71) são factuais (dados do snapshot) e escritos como tal; a erosão estrutural é hipótese e tratada como tal.
- Insight 3 (`classificacao: "risco latente"`): mantido caráter prospectivo — "está em risco concreto... se o ML pausar... vira variável confundidora". Nenhuma afirmação retrospectiva de pedidos não atendidos ou déficit de estoque.

**Modalidade de envio omitida da seção VISÃO:**
- `fulfillment_mix_yesterday_top10` cobre apenas os 10 anúncios mais vendidos ponderados por pedidos (68 de 84 pedidos do dia, ~81% de cobertura) — não representa dado objetivo universal do dia sem ressalva. L05 não autorizou mostrar com cobertura explícita. Dado omitido da VISÃO conforme regra; menção ao modal de envio aparece apenas na Análise e Prioridades, vinda da L05.

**Confiança média — impacto:**
- Nível "media" permite os 3 insights. Nenhum corte adicional aplicado além do que a L05 já realizou. Linguagem de hipótese preservada onde classificado.

**Yasmin como responsável:**
- Atribuída como responsável nas 3 prioridades do dia — L05 não atribui responsável; L06 atribui conforme regra de canal.

**Quantidade no Top Produtos:**
- Exatamente 5 produtos exibidos (primeiros 5 do `top_products`). Todos os 5 têm `slack_short_name` preenchido; nenhum fallback para `display_short` necessário neste ciclo.

**Cancelamentos na VISÃO:**
- 1 cancelamento incluído — campo disponível e relevante para visão objetiva do dia.
<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 02/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 9.210,85
- Pedidos: 197 pedidos
- Ticket médio: R$ 46,76
- Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 56 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 23 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 20 pedidos
- Kit 4 Potes 1050ml — 12 pedidos
- Kit 6 Canecas Lisas 200ml — 11 pedidos

🔍 ANÁLISE DA CONTA
- A conta entregou o melhor resultado de terça da série — R$ 9.210,85, quinta semana seguida de crescimento. Mas o número mascara três anúncios em Full com cobertura crítica ao mesmo tempo: Kit 4 Potes 1050ml fechou com 2 unidades após 12 pedidos (ruptura praticamente certa nas próximas horas), Kit 6 Canecas Tulipa 250ml repetiu pelo oitavo ciclo o padrão de pausar com estoque zero — 8 pedidos viraram cancelamentos prospectivos — e Kit 6 Canecas Lisas 200ml, único Catálogo no top 5, tem ~2,5 dias de cobertura restante. O nível de vendas está crescendo de verdade, mas a estrutura que o sustenta começa a ceder e exige reposição imediata.
- Embora a taxa de cancelamentos oficial ainda esteja em zero, a janela de promoção para MercadoLíder Platinum está no momento mais crítico: faltam R$ 11.621,68, progresso em 96,1%, prazo estimado de 2,5 dias ao ritmo médio — e hoje o Faturamento ficou 113% acima desse ritmo. O volume não é o problema. O risco é a qualidade: os cancelamentos prospectivos do Kit 6 Canecas Tulipa 250ml acumulam em série crescente (3→3→2→6→9→2→8 hoje), e com 6.390 transações completas cada ~32 cancelamentos movem 0,5 ponto percentual — exatamente o limite da medalha. A próxima leitura de reputação define se essa série já entrou na janela oficial antes de a promoção fechar.
- A proporção de modalidade de envio no top 10 ficou 48,1% Full / 51,9% Cross-Docking hoje, contra 80,9% Full nos últimos 30 dias. Isso não é mudança estrutural — é efeito de um único produto: Potes Vidro 5 Peças — Tampa Preta liderou o dia com 56 pedidos (28,4% do Faturamento) em Cross-Docking. Os anúncios Full não perderam espaço de forma estrutural; fluíram menos porque estão exatamente onde o risco operacional está concentrado. O que mudou foi o produto líder do dia, não a operação.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar imediatamente se há reposição em trânsito para o Kit 4 Potes 1050ml ao CD do ML e acelerar o abastecimento. Fechou com 2 unidades após 12 pedidos — ruptura em Full é praticamente certa nas próximas horas; remove um suporte do novo nível de vendas e gera cancelamentos automáticos que pressionam a janela de Platinum. Confirmar/refutar por: próxima leitura — status ativo com mais de 10 unidades = reposição entrou; pausado ou zerado = ruptura confirmada. Escalar se: sem prazo estimado de reposição em até 48h — Yasmin abre conversa com o Trader para recalibrar projeção de volume e priorizar o abastecimento ao CD.
- Yasmin: verificar se há estoque disponível para reativar o Kit 6 Canecas Tulipa 250ml; se houver, reativar em até 24h. Oitavo ciclo do mesmo padrão — pausada com estoque zero — desta vez na maior escala da série (8 cancelamentos prospectivos). Com o prazo estimado de Platinum em 2,5 dias, cada cancelamento que entrar na janela oficial aperta o limite de qualidade da medalha. Confirmar/refutar por: próxima leitura de reputação — taxa de cancelamentos saindo de zero = série entrou na janela oficial; reativação com estoque acima de zero e status ativo = ciclo interrompido. Escalar se: reposição inviável em 24h e taxa de cancelamentos acima de zero — Yasmin escalona para o Kobe sobre risco direto à promoção de Platinum.
- Yasmin: confirmar prazo estimado de reposição do Kit 6 Canecas Lisas 200ml (Catálogo) ao CD do ML. Cobertura em ~2,5 dias no único Catálogo do top 5 — ruptura derruba o Buy Box e a recuperação de posição é estruturalmente lenta. Confirmar/refutar por: prazo estimado de até 3 dias = risco coberto; acima de 5 dias ou indefinido = janela de ruptura aberta antes do reabastecimento. Escalar se: prazo acima de 5 dias ou indefinido — Yasmin escalona para o Trader com foco em prioridade de abastecimento ao CD.

Dia analisado: 02/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. A L05 entregou `o_que_nao_pode_ir_para_slack: []` (lista vazia). Todos os produtos citados nos insights e prioridades mantidos nominalmente com seus `slack_short_name` canônicos.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` removidos dos três insights; não aparecem na mensagem final.

**Preservação de nuance por classificação**
- Insights 1 e 2 (`risco latente`): linguagem prospectiva preservada — "ruptura praticamente certa", "cancelamentos prospectivos", "define se a série já entrou". Nenhuma hipótese convertida em fato.
- Insight 3 (`fato`): escrito de forma direta e assertiva conforme classificação.

**Termos técnicos traduzidos**
- `ETA` → "prazo estimado" (todas as ocorrências em Análise e Prioridades)
- `patamar` → "nível de vendas" / "nível" (todas as ocorrências)
- `cancellations_rate` → "taxa de cancelamentos"
- `threshold` → "limite da medalha"
- `snapshot` → "próxima leitura" / "leitura de reputação" (conforme contexto)
- `gap` → "faltam R$ [valor]"
- `pace` → "ritmo médio" / "ritmo necessário"
- `health` — não aparecia explicitamente nos insights da L05; sem ocorrência a traduzir no Slack

**Correção monetária: R$ 11.621,68**
- L05 arredondou para "R$ 11.621"; valor completo do ml_snapshot é R$ 11.621,679... Aplicada regra de 2 casas decimais obrigatórias em todos os valores monetários → R$ 11.621,68.

**Modalidade de envio omitida da seção 📊 VISÃO**
- Dado disponível é `fulfillment_mix_yesterday_top10`, que cobre apenas top 10 (135 de 197 pedidos = ~68,5% do dia). Sem autorização da Condensadora para exibir com ressalva explícita de cobertura, omitido da VISÃO conforme regra. Modalidade de envio tratada exclusivamente na 🔍 ANÁLISE via insight 3 da L05.

**Faturamento por produto não incluído no 🏆 TOP PRODUTOS**
- Pacote não traz receita validada por produto/variação. Formato padrão `[nome] — [pedidos] pedidos` aplicado em todos os cinco itens.

**Traduções de nome de produto — Top Produtos (slack_short_name, mapeamento canônico)**
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- CLR002 — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)

**Traduções de nome de produto — Análise e Prioridades (título longo L05 → slack_short_name L06)**
- L05: "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → L06: "Kit 4 Potes 1050ml" (slack_short_name KIT4YW1050; mapeamento canônico)
- L05: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → L06: "Kit 6 Canecas Tulipa 250ml" (slack_short_name TL6250; mapeamento canônico)
- L05: "Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida" → L06: "Kit 6 Canecas Lisas 200ml" (slack_short_name CLR002; mapeamento canônico)
- L05: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto" → L06: "Potes Vidro 5 Peças — Tampa Preta" (slack_short_name IMB501P; mapeamento canônico)

**Consolidação de variações no Top Produtos**
- Cluster IMB501 exibido como três variações separadas (Tampa Preta MLB4535865317 Cross-Docking / Tampa Cinza MLB3288536143 Full / Tampa Vermelha MLB3288536143 Full), conforme regra de variações reais com volumes e modalidades de envio distintos. Nenhuma agregação em família única aplicada.

**Atribuição de responsável nas Prioridades**
- Yasmin inserida como executora em cada prioridade conforme regra da L06 (a L05 não atribui responsável). Trader e Kobe mantidos como alvos de escalonamento exatamente como a L05 especificou.

**Confiança média**
- Nível "media" da L05 não exige ressalva explícita de limitação de dados na mensagem final. As ressalvas pertinentes já estão incorporadas na classificação "risco latente" dos insights 1 e 2 (linguagem prospectiva e condicional preservada).
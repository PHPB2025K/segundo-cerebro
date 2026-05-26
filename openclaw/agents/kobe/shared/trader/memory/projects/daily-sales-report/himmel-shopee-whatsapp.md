# Himmel — WhatsApp Shopee

Arquivo canônico para contexto operacional do grupo WhatsApp **[SHOPEE] BUDAMIX + 2**.

## Objetivo

Manter memória dedicada das interações com a Himmel sobre **Shopee**, cobrindo as três contas Budamix, para uso por Kobe, Trader, Spark e outros agentes em análises operacionais, Daily Sales Report v2, planejamento de conta, diagnósticos de ADS e hipóteses de causa/efeito.

## Fonte

- Canal: WhatsApp próprio do Kobe via Evolution API.
- Grupo: **[SHOPEE] BUDAMIX + 2**.
- Escopo: Shopee / planejamento operacional das 3 contas.
- Status de acesso: Kobe consegue localizar o grupo na instância WhatsApp e deve ingerir mensagens novas legíveis via rotina read-only.

## Regras de uso

- Usar como **contexto operacional e hipótese causal**, não como dado de performance por si só.
- Cruzar sempre com dados reais: vendas por shop_id, estoque, campanhas, exposição, ADS, preço, ranking, margem, afiliados, cupons e fulfillment.
- Não culpar agência/Himmel sem evidência quantitativa.
- Quando a mensagem falar apenas “Shopee” sem conta específica, tratar como contexto consolidado das 3 contas e separar impacto por conta nos reports quando os dados permitirem.
- Registrar decisões, planos, projeções, cobranças, responsáveis e janelas de validação.
- Não colar conversa inteira quando não for necessário; resumir o que muda decisão/análise.

## Campos por interação

- Data/hora BRT.
- Participantes relevantes.
- Tema.
- Plataforma/conta.
- Produtos/SKUs citados.
- Decisão/contexto.
- Impacto esperado.
- Como validar nos dados.
- Status: aberto / confirmado / refutado / encerrado.

---

## Interações

### 2026-05-26 09:13–09:47 BRT — Reunião Shopee remarcada com estrategista Himmel

- **Participantes:** Letícia (Himmel) e Lucas / PhaseTec.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix.
- **Tema:** alinhamento/reunião operacional Shopee do dia.
- **Contexto útil:** reunião originalmente confirmada para 10h foi remanejada para **16h BRT** porque será necessária a participação da estrategista da Himmel.
- **Produtos/SKUs citados:** nenhum.
- **Responsáveis/próximo passo:** Lucas aceitou o remanejamento; Himmel deve entrar com estrategista na reunião das 16h.
- **Como validar nos próximos reports:** aguardar ata/transcrição ou mensagens posteriores para identificar decisões de campanha, verba, produtos priorizados, cupons, afiliados ou janelas de teste que possam afetar o Daily Sales Report v2.
- **Status:** aberto — reunião agendada, ainda sem decisão operacional registrada.

### 2026-05-26 14:15–18:18 BRT — Alinhamento emergencial por queda expressiva de faturamento Shopee

- **Participantes:** Pedro Broglio, Lucas / PhaseTec, Letícia e Raphaella (Himmel).
- **Plataforma/conta:** Shopee consolidado; nenhuma conta específica foi nomeada, então aplicar como contexto das 3 contas Budamix até haver separação por shop_id.
- **Tema:** reunião de alinhamento com Pedro/Lucas por queda expressiva de faturamento e redução de performance em produtos principais.
- **Contexto útil:** Raphaella sinalizou que a reunião precisava ser alinhada diretamente com Pedro “devido à queda expressiva de faturamento da conta” e redução de performance em alguns dos principais produtos. Pedro não conseguiria entrar na reunião original das 16h, mas ajustou participação para 17h; a Himmel confirmou uso do mesmo link. Às 18:18, Raphaella informou que as informações da reunião foram compartilhadas e que havia “pontos alinhados e ações definidas” para recuperar a queda de faturamento das lojas, com acompanhamento das métricas nas próximas semanas.
- **Produtos/SKUs citados:** não houve produto/SKU nomeado no WhatsApp; tratar como alerta genérico sobre produtos principais até transcrição/ata detalhar quais itens caíram.
- **Decisão/contexto:** houve reunião de recuperação de performance Shopee no mesmo dia, com ações definidas pela Himmel/GB; os detalhes operacionais ainda não apareceram no grupo e devem ser buscados na gravação/transcrição ou com Lucas/Pedro antes de virar diagnóstico factual.
- **Impacto esperado:** tentativa de recuperar faturamento Shopee nas lojas e performance dos principais produtos ao longo das próximas semanas.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, comparar vendas, tráfego/conversão, investimento ADS, TACOS/ROAS, ranking/exposição e estoque das 3 contas Shopee; procurar inflexão a partir de 2026-05-26/27 e separar por shop_id. Se houver melhora/queda, registrar como hipótese ligada às ações da reunião, não como causa confirmada.
- **Responsáveis/próximo passo:** Himmel acompanhar evolução das ações e métricas; Lucas/Pedro devem repassar ou disponibilizar a gravação/ata para detalhar ações, produtos e janelas de validação.
- **Status:** aberto — reunião realizada e ações citadas, mas sem detalhamento operacional no WhatsApp.

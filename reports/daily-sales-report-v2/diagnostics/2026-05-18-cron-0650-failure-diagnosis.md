# Diagnóstico — Daily Sales Report v2 Cron 06:50 BRT — 2026-05-18

## Escopo
- Pedido do Pedro em 2026-05-18 20:42 BRT: investigar por que o Daily Sales Report v2 da manhã não completou, sem executar correção hoje.
- Cron analisado: `Daily Sales Report — Slack Funcionários`.
- Data analisada pelo report: 2026-05-17 BRT.

## Resultado executivo
O cron não completou a entrega porque o pipeline chegou até o DSA/QA com LLM em todas as camadas, mas o QA Gate do Lucas/Shopee bloqueou o recipient por duplicidade no Top Produtos. Como o bridge de entrega para o Slack pessoal do Pedro exige que os três recipients estejam não bloqueados e 100% LLM, a etapa final de envio abortou antes de emitir `SENT_TO_PEDRO_SLACK`.

## Camada específica do problema
- Camada impactada: `07-qa` do recipient Lucas/Shopee.
- Gate que falhou: Gate 5 — Top Produtos.
- Severidade: Crítico.
- Efeito: status de Lucas/Shopee = `BLOCKED`; status global do manifest = `PARTIAL`; envio Pedro-only bloqueado.

## Causa raiz
O Slack Writer de Lucas/Shopee gerou Top Produtos com o produto `Kit 6 Canecas Tulipa 250ml` duas vezes:

1. linha consolidada das 3 contas Shopee: 14 pedidos;
2. linha individual da Conta 3: 3 pedidos.

O QA detectou que os 3 pedidos da Conta 3 já estavam incluídos no consolidado de 14 pedidos. Isso criava risco real de Lucas interpretar o volume como 17 pedidos ou entender a linha individual como produto distinto.

A Slack Writer percebeu a ambiguidade nas decisões de formatação, mas não resolveu antes de entregar ao QA; deixou a decisão como “removível se QA entender”. O QA corretamente bloqueou.

## O que funcionou
- Data Readiness: `DADOS_PARCIAIS`, sem failed checks.
- Layer 0 package foi gerado em v1.3.
- DSA rodou com LLM ativo para Lucas, Yasmin e Leonardo.
- Todas as camadas LLM de Lucas rodaram sem fallback, incluindo 06B, Slack Writer e QA.
- Yasmin/Mercado Livre: `APPROVED_WITH_REMARKS`.
- Leonardo/Amazon: `APPROVED_WITH_REMARKS`.
- Nenhum envio para funcionários foi tentado.

## O que não funcionou
- Lucas/Shopee ficou `BLOCKED` no QA.
- A etapa `daily-sales-dsa-send-slack-pedro.py` abortou porque encontrou recipient bloqueado.
- O wrapper final não emitiu `SENT_TO_PEDRO_SLACK`.
- O resumo do cron registrou que Leonardo teria sido interrompido antes de concluir, mas os artefatos locais mostram Leonardo completo até o QA. Essa é uma divergência de diagnóstico do agente do cron, não a causa técnica real.

## Correção recomendada para amanhã
1. Ajustar a Slack Writer / 06B para resolver internamente duplicidade de produto consolidado Shopee antes do QA.
2. Regra prática: quando houver linha consolidada por variação vendável nas 3 contas, não manter também linha individual que já compõe o consolidado.
3. Substituir códigos de variação na análise por nomes comerciais, especialmente `IMB501P` e `CK4742`, para evitar ressalva menor de clareza.
4. Reexecutar somente Lucas/Shopee para 2026-05-17 com merge-existing e validar que o manifest global passa para aprovado/aprovado com ressalvas.
5. Só depois acionar entrega Pedro-only.

## Estado para Mission Control
- `manifest.global_status`: `PARTIAL`.
- `manifest.data_readiness.status`: `DADOS_PARCIAIS`.
- `lucas.status`: `BLOCKED`.
- `yasmin.status`: `APPROVED_WITH_REMARKS`.
- `leonardo.status`: `APPROVED_WITH_REMARKS`.
- `send_real_allowed`: false.
- Bloqueio operacional imediato: QA Gate Lucas/Shopee, duplicidade no Top Produtos.

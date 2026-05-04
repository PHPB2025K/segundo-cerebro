---
title: "Decisões"
created: 2026-05-01
type: context
status: active
tags:
  - memory
  - context
  - decisions
---

# Decisões — Índice Operacional

_Este arquivo existe para cumprir o contrato operacional `memory/context/decisions.md`. O histórico detalhado continua em `memory/context/decisoes/`._

## 2026-05-01 — Fechamento financeiro abril/2026

- Relatórios financeiros não devem chamar `SETTLEMENT`/extrato financeiro de faturamento bruto sem qualificador.
- Usar **faturamento bruto comercial** para pedidos válidos do mês e **receita liquidada em extrato** para settlement/financeiro.
- Abril/2026 validado: faturamento comercial R$ 405.839,65; receita liquidada em extrato R$ 354.992,67.
- Para Shopee Ads abril/2026, usar o número oficial de plataforma informado manualmente pelo Pedro: R$ 9.460, vendas via Ads R$ 165.600, ROAS 17,51. Wallet API fica como conciliação/alerta, não como consumo oficial.
- Amazon Ads abril/2026 via API Sponsored Products validado: gasto R$ 2.478,95; vendas atribuídas R$ 11.749,58; ROAS 4,74; ACOS 21,10%.
- DRE da GB deve seguir estrutura clássica completa, não apuração simplificada de marketplace.

## 2026-05-01 — Fiscal / NFs internas abril/2026

- Orientação v2.1 da Suellen/FOUR permanece como fonte de verdade para transferência Matriz SC → Filial SP: CFOP 6.152, CST ICMS 90, ICMS sem destaque, IPI suspenso CST 55, origem Matriz=1 e Filial=2.
- Venda interna Filial SP → CNPJs Simples SP é operação distinta: CFOP 5.102, origem 2, ICMS interno 18% e IPI conforme NCM quando aplicável.
- NFs internas de abril/2026 devem cobrir apenas produtos importados próprios GB; excluir nacionais, MDF, cerâmica, livros, fita, pseudo-itens, SEM_SKU, terceiros e Jarra Clink/CK4742.
- Antes de emitir NF interna mensal, reconciliar estoque fiscal por SKU/componente: saldo inicial Matriz/Filial, entradas/transferências do mês, vendas do mês, aliases Bling, kits e fatores de conversão.
- Para abril/2026, emissão validada integralmente pela Filial porque a Filial cobria os componentes após corrigir conversões de caixas/conjuntos. A inconsistência histórica de YW1520 na Matriz fica como ressalva separada.
- Vendas B2B/atacado emitidas pela Matriz devem abater estoque fiscal da Matriz antes de qualquer uso de saldo Matriz como excedente.
- NFs internas abril/2026 autorizadas: 000031, 000032, 000033, total R$ 77.065,09.
- NFs de transferência abril/2026 000649 e 000653 foram enviadas à FOUR/financeiro em 01/05/2026 com observação de que saíram antes da orientação fiscal atualizada.


## 2026-05-02 — Guarani Sistemas / distrato contratual

- Guarani Sistemas: estratégia aprovada para contestar a cobrança integral, exigir suspensão de protesto e memória de cálculo aberta, e negociar distrato **sem reconhecimento de dívida** com âncora/teto técnico inicial de **R$ 7.002,30**, condicionado a quitação total, baixa dos boletos/NFs 2384–2390 e inexistência de saldo remanescente.

## 2026-05-02 — Budamix Central / Live Sales

- Meta diária exibida no Budamix Central/Live Sales passa de **R$ 12.000** para **R$ 20.000**. Configuração aplicada em produção e fallback do endpoint atualizado.

## 2026-05-02 — Amazon Ads / otimização abril fechado

- Rodada de otimização Amazon Ads deve usar **abril/2026 fechado (01/04 a 30/04)** como baseline; não misturar últimos 30 dias móveis nem dados parciais de maio.
- Mudanças de campanha/keyword/target continuam exigindo aprovação explícita por grupo antes de execução.
- Para o grupo **Potes Redondos Plástico**, considerar o produto como potes redondos de vidro com tampa plástica; termos de vidro são core/aderentes, não conflito semântico.
- Acompanhamento obrigatório D+7 para todos os grupos executados em 02/05/2026 antes de nova rodada de cortes/escala baseada em impacto.

## 2026-05-03 — Amazon Ads / framework de revisão por grupo

- Pedro aprovou que a revisão de cada grupo de Amazon Ads deve seguir sempre 3 blocos: **cortar desperdício**, **promover winners validados de Auto/Broad para Exact com negativa na origem quando fizer sentido**, e **escalar winners Exact comprovadas** para aumentar vendas sem perder controle de ACoS/ROAS.
- Keywords recém-promovidas para Exact **não devem ser escaladas no mesmo momento**; precisam primeiro acumular histórico próprio na Performance antes de receber aumento de bid.
- Próximo grupo na fila após as execuções de 02/05 ficou **Suporte Controle Gamer**; a análise está pronta e a execução depende de aprovação do Pedro.

## 2026-05-03 — Amazon Ads / grupos finais e experimentos de tração

- Para grupos sem entrega ou sem vendas suficientes (**Abraçadeiras Nylon**, **Redinha Frutas**, **Kit Jardinagem**), diferenciar otimização de ACoS de experimento de tração. Sem dados, o objetivo é diagnosticar entrega/relevância/listing/Buy Box, não prometer melhora de ACoS.
- **Abraçadeiras Nylon** teve experimento de tração aprovado após confirmação de estoque FBA no ASIN ativo `KIT200BR10P` / `B0CN9PPC17`. Medição obrigatória em D+7: impressões, CTR, CPC, cliques, vendas, Buy Box e estoque FBA.
- **Redinha Frutas** e **Kit Jardinagem** não devem receber aumento de bid antes de validar product ads, estoque/FBA, listing ativo e Buy Box; se não houver estrutura ativa, manter/assumir inativo.

## 2026-05-03 — Paper.design / Templates Carrossel Budamix

- Templates oficiais de carrossel Budamix no Paper.design ficam organizados em 5 famílias × 3 versões cromáticas (CLARA/NORMAL/ESCURA), totalizando 96 artboards 1080×1080 no arquivo `01KQMVPNGXW4ZWQPVE1KDPMBN3`.
- Versão CLARA usa fundo areia e títulos teal `#004D4D`; não usar grafite para títulos principais em fundo claro porque fica lavado.
- Paper Shaders não são acionáveis via MCP; qualquer uso de Mesh Gradient/Grain/Liquid Metal exige aplicação manual pela UI do Paper Desktop.

## 2026-05-02 — Skills locais / ElevenLabs

- Para `video-use`, a API key ElevenLabs deve ser restrita ao mínimo necessário: apenas **Speech to Text**. Sanity check seguro: `POST /v1/speech-to-text` sem payload esperando HTTP 422 como prova de auth OK; não usar `/v1/user` porque exige permissão administrativa.

## Ver também

- `memory/context/decisoes/kobe-permanentes.md`
- `memory/context/decisoes/2026-04.md`
- `memory/context/decisoes/2026-05.md`

## 2026-05-04 — Relatório mensal Trader / rota de execução e notificação

- Geração direta do relatório mensal deve rodar como job realmente direcionado ao **Trader**, não como `main` tentando delegar via cron.
- Conclusão ou falha desse job deve ser avisada no mesmo tópico **Marketplaces** do Telegram onde o Pedro pediu o acompanhamento.

---
title: "Digest Builder — 2026-06-13"
date: 2026-06-13
agent: builder
status: active
---

# Digest Builder — 2026-06-13

## Resumo executivo
- Builder consolidou avanços em Estoque: Envios Full voltou a rodar silenciosamente com baixa física real e sem mensagem própria.
- O processamento de Envios Full terminou sem divergências após fallback por descrição para item que o SKU/alias não resolvia corretamente.
- Granola/Himmel rodou contexto, mas a captura de notas novas segue bloqueada por assinatura inativa do workspace.

## Decisões novas
- Envios Full deve aparecer apenas dentro do Controle de Estoque diário, sem mensagem própria no Telegram.
- Envios Full baixa estoque físico do galpão; vendas marketplace Full/FBA não baixam novamente o físico.
- Quando SKU/alias não resolver item físico baixável, descrição pode ser usada como fallback conservador.

## Lições / riscos
- Risco mitigado em Estoque: diferenciar envio para Full/FBA de venda Full/FBA evita subbaixa ou baixa duplicada.
- Risco ativo: Granola/Himmel não consegue garantir ingestão de reuniões novas enquanto a assinatura do workspace estiver inativa.

## Pendências novas ou alteradas
- Monitorar próximos ciclos de Envios Full para confirmar idempotência, baixa real silenciosa e seção correta no Controle de Estoque.
- Renovar/corrigir assinatura do workspace Granola para retomar captura de notas novas.

## Entregas / ações executadas
- Envios Full reativado em modo silencioso com baixa física real.
- Backfill/reprocessamento seguro consolidou 94 unidades baixadas desde 10/06, 5 movimentos aplicados e 0 divergências restantes.
- Fallback por descrição corrigiu o caso da Caneca Paris 170ml Branca que antes caía em SKU inexistente.
- Memória interna do Builder atualizada: sessão diária, decisões, lições e pendências técnicas.

## Kobe precisa saber
- Estoque avançou bem: a rotina de Envios Full está novamente aplicando baixa física e sem pendência operacional conhecida nesta frente.
- O bloqueio de Granola/Himmel é externo/assinatura; sem correção, novas reuniões podem ficar fora do contexto diário.

## Possível decisão do Pedro
- Corrigir/renovar a assinatura do workspace Granola para restaurar a ingestão automática de novas notas.

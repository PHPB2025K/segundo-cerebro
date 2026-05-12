---
name: trader-daily-sales-cron-orchestrator
description: Orquestra o cron Daily Sales Report v2 do Trader de ponta a ponta. Use quando o cron diário executar, quando for rodar preview/manual, ou ao revisar a sequência correta de skills: data readiness, memória, análise por conta, Slack writer, QA/escalation e registro final.
---

# Trader — Daily Sales Cron Orchestrator

## Objetivo
Executar o Daily Sales Report v2 na ordem correta, chamando as skills certas em cada etapa e impedindo atalhos perigosos.

## Ordem obrigatória do cron
1. **Data readiness**
   - Usar `trader-daily-sales-data-readiness`.
   - Se bloqueado, parar e escalar para Kobe.

2. **Memória por conta**
   - Usar `trader-daily-sales-memory-cycle`.
   - Carregar pacote enxuto de cada conta.

3. **Análise profunda por conta**
   - Usar `trader-daily-sales-account-analysis`.
   - Gerar e salvar análise interna das 5 unidades.

4. **Contextos especiais**
   - Se houver mudança de regra/taxa: usar `trader-marketplace-rules-watch`.
   - Se houver reunião/decisão Himmel relevante: usar `trader-himmel-context-ingestion`.

5. **Mensagem Slack**
   - Usar `trader-daily-sales-slack-writer`.
   - Gerar 3 mensagens individuais.

6. **QA e escalonamento**
   - Usar `trader-daily-sales-qa-escalation`.
   - Se aprovado, enviar/registrar conforme modo.
   - Se falhar, não enviar report normal.

7. **Registro final**
   - Salvar cópia do enviado/preview em `sent-reports.md`.
   - Registrar alertas para Kobe quando necessário.

## Modos
- `preview`: gera tudo, não envia Slack.
- `send`: gera, valida e envia Slack.
- `memory-only`: gera apenas análises internas.
- `qa-only`: valida outputs já gerados.

## Regras invioláveis
- Nunca enviar Slack antes de salvar análise interna por conta.
- Nunca enviar se data readiness estiver bloqueado.
- Nunca usar Shopee consolidada para diagnóstico de Lucas.
- Nunca incluir Atacado/Bling.
- Nunca estimar dado faltante.
- Nunca sobrescrever memória antiga sem motivo explícito.

## Quando chamar Kobe
- Qualquer bloqueio.
- Qualquer falha de Slack.
- Qualquer mudança estratégica.
- Qualquer inconsistência que possa afetar decisão do Pedro.

## Gate de qualidade antes de produção
O cron só pode enviar se todos estes gates passarem:
1. Data readiness = `DADOS_OK` ou `DADOS_PARCIAIS` explicitamente aceito.
2. Análises internas das 5 contas salvas.
3. Slack writer sem SKU cru e com prioridades profundas.
4. QA escalation = PASS; se `BLOQUEADO_QUALIDADE`, não enviar.
5. Preview/payload gerado com dados oficiais estabilizados.
6. Registro em `sent-reports.md` após envio real.

## Skills opcionais inexistentes
Se `trader-marketplace-rules-watch` ou `trader-himmel-context-ingestion` não existirem no workspace, não inventar. Usar os arquivos gerais `marketplace-rules-watch.md` e `himmel-context.md` dentro da memória do Daily Sales Report.


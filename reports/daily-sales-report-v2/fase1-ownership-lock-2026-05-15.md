# Fase 1 — Ownership Lock Daily Sales Report Slack

Data: 2026-05-15
Escopo: confirmar e travar a cadeia oficial de execução do Daily Sales Report v2 para funcionários no Slack.

## Resultado

Status: FECHADO

A cadeia oficial fica travada como:

Cron → Trader → Daily Sales Analyst (DSA) → Trader → Kobe

Kobe não executa o pipeline como executor direto. Kobe governa bloqueios, aprovações e QA estratégico.

## Configuração DSA

- `enabled`: true
- `llm_layers_enabled`: true
- `allow_llm_in_shadow`: true
- `send_real_enabled`: false
- `require_kobe_approval_for_real_send`: true

Interpretação: o DSA está habilitado para execução LLM, mas envio real segue bloqueado até aprovação formal do Pedro na Fase 4/5.

## Cron Slack Funcionários

Job: Daily Sales Report — Slack Funcionários

- Estado atual: desabilitado
- Delivery: tópico Telegram Daily Sales Report - SLACK
- Prompt do cron: orientado para a cadeia Trader → DSA → Trader → Kobe
- Envio real: bloqueado até promoção final

## Classificação dos scripts

### Executor oficial do DSA

- `scripts/daily-sales-analyst-runner.py`
  - Runner oficial do Daily Sales Analyst.
  - Executa Layer 0 + camadas 1–7, incluindo 6B Shopee quando aplicável.
  - Gera artefatos auditáveis por data/destinatário.
  - Respeita kill switch, rollback, LLM, shadow, preview e bloqueios de envio.

### Componentes internos do DSA

- `scripts/daily-sales-data-builder.py`
  - Layer 0 determinística.
  - Gera pacote validado e Data Readiness.
  - Não envia nada.

- `scripts/daily-sales-v2-build-package.py`
  - Monta pacote validado por plataforma para o pipeline em camadas.
  - Não chama LLM e não envia nada.

- `scripts/daily-sales-v2-shopee-consolidator-runner.py`
  - Componente da Camada 6B Shopee.
  - Usa condensadoras das 3 contas Shopee como input.
  - Não envia Slack.

- `scripts/daily-sales-compare-packages.py`
  - Ferramenta read-only de comparação de pacotes.
  - Não modifica arquivos e não envia nada.

### Orquestração/rotina do Trader

- `scripts/daily-sales-v2-analyzer.py`
  - Motor de análise profunda/memória por conta.
  - Deve ser tratado como etapa do Trader antes/de apoio ao DSA.

- `scripts/daily-sales-v2-consolidate-memory.py`
  - Consolidação semanal/mensal da memória do Trader.
  - Não envia Slack para equipe.

- `scripts/daily-sales-v2-himmel-granola-context.py`
  - Sync de contexto Himmel/Granola para alimentar memória do Trader.
  - Não envia Slack para equipe.

- `scripts/daily-sales-v2-marketplace-rules-watch.py`
  - Atualiza contexto de regras/taxas/políticas para o Trader.
  - Não envia Slack para equipe.

### Fallback determinístico controlado / legado sem envio real

- `scripts/send-daily-sales-v2-slack-funcionarios.py`
  - Wrapper legado v2 mantido por compatibilidade.
  - Não executa Slack Writer, QA Gate, 6B nem envio por conta própria.
  - Delega ao DSA em preview/shadow.
  - `--send-real` bloqueado.

- `scripts/send-daily-sales-slack-funcionarios.py`
  - Script v1 legado.
  - Agora bloqueado para envio real para Lucas/Yasmin/Leonardo.
  - Permitido apenas como dry-run ou preview explícito para Pedro.

- `scripts/daily-sales-v2-generate-slack.py`
  - Gerador legado de previews/payloads Slack.
  - Pode ser usado como fallback/validador determinístico de layout durante auditoria.
  - Não deve ser caminho principal de execução após promoção DSA.

- `scripts/daily-sales-v2-layered-preview.py`
  - Runner preview determinístico antigo.
  - Sem LLM, sem envio, sem memória.
  - Mantido apenas para comparação/auditoria.

### Fora do escopo do Slack funcionários

- `scripts/send-daily-sales-whatsapp-socios.py`
  - Rotina separada de resumo para sócios via WhatsApp.
  - Não pertence ao pipeline Slack funcionários.

## Bloqueios ativos confirmados

- Envio real pelo wrapper v2: bloqueado.
- Envio real pelo script v1: bloqueado nesta Fase 1.
- Cron Slack Funcionários: desabilitado.
- DSA real send: bloqueado por `send_real_enabled=false` e aprovação Kobe/Pedro obrigatória.

## Próximo passo

Fase 2: refatorar os prompts das camadas 1–7/6B com as melhorias 7.1–7.8, começando por consolidar as lacunas em Camadas 1–6B e depois revisar Slack Writer + QA Gate.

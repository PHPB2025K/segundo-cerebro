# Promoção DSA LLM — Lucas, Yasmin e Leonardo

Data: 2026-05-15
Status: PROMOVIDO_TECNICAMENTE

## Decisão do Pedro
Pedro decidiu que os três reports do Daily Sales Report Slack devem usar LLM como caminho principal:
- Lucas / Shopee
- Yasmin / Mercado Livre
- Leonardo / Amazon

## Validação final
- lucas: LLM_OK — APPROVED_WITH_REMARKS
- yasmin: LLM_OK — APPROVED_WITH_REMARKS
- leonardo: LLM_OK — APPROVED_WITH_REMARKS

## Configuração pós-promoção
- llm_layers_enabled: True
- fallback_deterministic_allowed: False
- send_real_enabled: False
- require_kobe_approval_for_real_send: True

## Regra operacional
Slack Writer LLM + QA Gate LLM são o caminho principal dos três recipients. Fallback determinístico não é caminho aprovado; se uma camada LLM falhar, o recipient deve ficar bloqueado em vez de ser mascarado como aprovado.

## Segurança
Envio real continua bloqueado até autorização explícita de Pedro/Kobe para produção.

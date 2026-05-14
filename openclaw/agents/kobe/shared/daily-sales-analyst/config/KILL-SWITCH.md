# Kill Switch — Daily Sales Analyst

## O que é

O kill switch permite desativar total ou parcialmente o Daily Sales Analyst sem alterar código. Basta editar `daily-sales-analyst.json`.

## Campos de controle

| Campo | Efeito quando `false` |
|---|---|
| `enabled` | Pipeline inteira desligada. Runner aborta imediatamente. |
| `send_real_enabled` | Bloqueia qualquer envio real (Slack/Telegram). Artefatos ainda são gerados. |
| `preview_to_kobe_enabled` | Desativa geração de preview local para Kobe/Pedro. |
| `lucas_enabled` | Pula processamento do Lucas. |
| `yasmin_enabled` | Pula processamento da Yasmin. |
| `leonardo_enabled` | Pula processamento do Leonardo. |
| `data_builder_enabled` | Desativa Data Builder. Pipeline bloqueia sem dados. |
| `llm_layers_enabled` | Desativa camadas LLM. Runner usa fallback determinístico. |
| `fallback_deterministic_allowed` | Se `false` e LLM desabilitado, pipeline aborta em vez de gerar fallback. |

## Como desligar tudo (emergência)

```json
{
  "enabled": false
}
```

Runner retorna imediatamente com mensagem `ABORT: Config enabled=false`.

## Como desligar envio real mantendo pipeline

```json
{
  "send_real_enabled": false
}
```

Artefatos continuam sendo gerados para auditoria, mas nenhum envio externo ocorre.

## Como desligar um recipient específico

```json
{
  "lucas_enabled": false
}
```

## Quem pode operar o kill switch

- **Kobe** (governança final)
- **Pedro** (owner do Trader)
- Em emergência, qualquer operador com acesso ao arquivo de config.

## Verificação

Após alterar, rodar:
```bash
python3 scripts/daily-sales-analyst-runner.py YYYY-MM-DD --preview-to-kobe
```
E verificar que o manifest reflete a mudança.

# Rollback — Daily Sales Analyst

## Rollback de Prompt Version

Para reverter para uma versão anterior dos prompts:

```json
{
  "rollback_to_version": "v2.0",
  "pinned_prompt_version": "v2.0"
}
```

- `rollback_to_version`: indica que houve rollback e qual versão alvo.
- `pinned_prompt_version`: fixa a versão usada pelo runner (sobrepõe `prompt_version`).

Para desfazer o rollback, setar ambos para `null` e o runner usará `prompt_version`.

## Rollback de Data Builder

```json
{
  "rollback_data_builder_version": "v0.9",
  "data_builder_version": "v0.9"
}
```

Mesma lógica: `rollback_data_builder_version` registra que houve rollback.

## Rollback de LLM → Fallback

Se camadas LLM estiverem causando problemas:

```json
{
  "llm_layers_enabled": false,
  "fallback_deterministic_allowed": true
}
```

Runner volta a gerar artefatos determinísticos sem LLM.

## Rollback completo (modo seguro)

```json
{
  "send_real_enabled": false,
  "llm_layers_enabled": false,
  "fallback_deterministic_allowed": true,
  "rollback_to_version": "v3.0",
  "pinned_prompt_version": "v3.0"
}
```

## Histórico de rollbacks

Cada rollback deve ser registrado em commit com mensagem clara:
```
rollback: DSA prompt v3.1 → v3.0 (motivo: ...)
```

## Quem autoriza rollback

- Rollback de emergência: Kobe ou Pedro.
- Rollback planejado: Trader propõe, Kobe aprova.

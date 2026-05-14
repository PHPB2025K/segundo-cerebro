# Registro de Relatórios Enviados — Daily Sales Analyst

## Status

**Nenhum relatório foi enviado para destinatários reais até o momento.**

O envio real está desabilitado (`send_real_enabled=false`) e permanecerá assim até:
1. Integração LLM profunda estar implementada e validada.
2. Rollout supervisionado completar Etapas 1 e 2.
3. Kobe aprovar explicitamente o avanço para Etapa 3.

## Formato do registro (futuro)

Quando envios reais começarem, cada entrada terá:

```
### YYYY-MM-DD
- **Recipient:** nome
- **Plataforma:** shopee/mercado_livre/amazon
- **Modo:** production-send
- **Status:** SENT / FAILED / ROLLED_BACK
- **Aprovado por:** Kobe
- **Prompt version:** vX.Y
- **Data builder version:** vX.Y
- **LLM layers:** true/false
- **Observações:** ...
```

## Histórico

_(vazio — primeiros envios serão registrados após rollout supervisionado)_

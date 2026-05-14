# PLAN.md — Shadow LLM Runner para Daily Sales v2 Layered Cycle

## Status: PROPOSTA — aguardando aprovação de Pedro/Kobe

## Contexto

O pipeline atual (`daily-sales-v2-layered-preview.py`) executa as camadas 3–7 de forma
**determinística/rule-based**. Os prompts das camadas 1–7 existem em `prompts/daily-sales/`
mas não são consumidos por nenhum script — foram escritos para um futuro runner LLM.

Não há padrão interno de chamada LLM nos scripts do `segundo-cerebro`. Implementar chamadas
diretas à API sem padrão aprovado seria inseguro (risco de token exposto, custo descontrolado,
output não auditável).

## Proposta: menor alteração segura

### Opção A — Runner LLM via Claude API (recomendada)

1. Criar `scripts/daily-sales-v2-layered-llm-runner.py` que:
   - Lê `package.json` validado (Fase 1)
   - Para cada destinatário, executa sequencialmente camadas 1→7
   - Cada camada: monta prompt (lê `.md` de `prompts/daily-sales/`) + contexto da camada anterior
   - Chama `anthropic.Anthropic().messages.create()` com `model="claude-sonnet-4-6"`
   - Salva output bruto + parsed em `runs/YYYY-MM-DD/<recipient>/camada-N-*.md|json`
   - **Nunca envia Slack** — `send_real_allowed=false` hardcoded
   - Aceita `--shadow` (roda e salva) e `--preview` (roda, salva e printa)

2. Dependências:
   - `pip install anthropic` (SDK oficial)
   - `ANTHROPIC_API_KEY` em variável de ambiente (nunca hardcoded)
   - Custo estimado: ~7 chamadas × 3 destinatários × ~4k tokens = ~84k tokens/dia ≈ US$ 0.25/dia

3. Segurança:
   - Token lido de `os.environ["ANTHROPIC_API_KEY"]` — nunca salvo em disco
   - Output 100% auditável em disco antes de qualquer envio
   - QA Gate (camada 7) roda sobre output LLM e bloqueia se necessário
   - Modo `--send-real` não implementado — só `--shadow`/`--preview`

### Opção B — Runner via Trader (agente existente)

Se o Trader já tem acesso à API Claude, o runner pode ser um "job" que o Trader executa:
1. Trader recebe package.json como contexto
2. Trader executa prompts 1–7 em sequência
3. Trader salva artefatos no mesmo formato

Vantagem: reutiliza infra existente. Desvantagem: acoplamento ao Trader.

### Opção C — Manter determinístico endurecido (fallback atual)

O `daily-sales-v2-layered-preview.py` continua como runner determinístico com:
- QA endurecido (bloqueio de análise rasa/genérica)
- Insights baseados em regras quantitativas
- Suficiente para shadow/preview enquanto LLM não é aprovado

## Recomendação

Aprovar **Opção A** como próximo passo. A Opção C já está implementada e funcional como
fallback. A migração é incremental: basta trocar o runner no cron sem alterar package ou QA.

## Pré-requisitos para Opção A

- [ ] Pedro/Kobe aprovam uso de API Claude para daily sales
- [ ] `ANTHROPIC_API_KEY` disponível no ambiente do cron
- [ ] Budget mensal aprovado (~US$ 7.50/mês para 30 dias)
- [ ] Primeiro run shadow com LLM revisado manualmente antes de habilitar

## Arquivos que seriam criados/alterados

| Arquivo | Ação |
|---------|------|
| `scripts/daily-sales-v2-layered-llm-runner.py` | CRIAR — runner LLM |
| `scripts/daily-sales-v2-layered-preview.py` | MANTER — fallback determinístico |
| `prompts/daily-sales/camada-*.md` | MANTER — já prontos para consumo |

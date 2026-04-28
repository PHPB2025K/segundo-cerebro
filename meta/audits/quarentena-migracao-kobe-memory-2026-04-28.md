# Quarentena — Migração memória Kobe

_Gerado em: 2026-04-28 06:35 BRT_

Arquivos deliberadamente não migrados automaticamente para `openclaw/agents/kobe/memory/` durante a Fase 3 por risco de conter credenciais, tokens, logs brutos, transcripts extensos ou material sensível:

- `memory/.dreams/events.jsonl` — log/event stream bruto.
- `memory/2026-04-02-bling-credentials.md` — nome indica credenciais Bling; requer revisão manual/sanitização.
- `memory/2026-04-07-context-restore.md` — transcript/context restore extenso; migrar só resumo seguro se necessário.
- `memory/2026-04-27-blog-automation.md` — transcript/log bruto com discussão de credenciais; requer sanitização.
- `memory/2026-04-27-job-monitor.md` — transcript/log bruto com discussão de tokens/integrações; requer sanitização.
- `memory/2026-04-27-wf4-images.md` — transcript/log bruto com discussão de tokens, 1Password, GitHub/Vercel/N8N; requer sanitização.
- `memory/2026-04-28-blog-fix.md` — transcript/log bruto de execução; requer sanitização.
- `memory/core-audit-snapshot.tsv` e `.core-audit-snapshot/` — artefatos internos de auditoria, não memória durável.

Regra: se algum conteúdo desses for importante para memória durável, extrair apenas resumo seguro, sem segredo, token, identificador sensível ou log bruto.

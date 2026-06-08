---
title: "MEMORY"
created: 2026-04-14
type: memory-config
agent: fisco
status: active
tags:
  - agent/fisco
---

# MEMORY.md - Long-Term Memory

_Último update: 2026-06-07_

## Estado operacional recente
- 2026-06-07: Refresh OAuth do Bling manteve bloqueio crítico pelo vigésimo quarto dia da Filial com HTTP 403 “empresa inativa”. Matriz conectou nas cinco execuções úteis observadas; ainda exige teste controlado antes de qualquer operação/draft. Alerta WhatsApp seguiu falhando com HTTP 403. Uma rodada teve bloqueio inicial por política/allowlist, mas rerun útil na mesma janela capturou o resultado fiscal. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-06: Refresh OAuth do Bling manteve bloqueio crítico pelo vigésimo terceiro dia da Filial com HTTP 403 “empresa inativa”. Matriz conectou nas quatro execuções úteis observadas; ainda exige teste controlado antes de qualquer operação/draft. Alerta WhatsApp seguiu falhando com HTTP 403. Uma rodada teve bloqueio inicial por política/allowlist, mas rerun útil na mesma janela capturou o resultado fiscal. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-05: Refresh OAuth do Bling manteve bloqueio crítico pelo vigésimo segundo dia da Filial com HTTP 403 “empresa inativa”. Matriz conectou nas três execuções úteis observadas; ainda exige teste controlado antes de qualquer operação/draft. Alerta WhatsApp seguiu falhando com HTTP 403 e houve rodada sem validação útil por política/allowlist. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-04: Refresh OAuth do Bling manteve bloqueio crítico pelo vigésimo primeiro dia da Filial com HTTP 403 “empresa inativa”. A Matriz voltou a conectar nas execuções úteis observadas de 17:17 e 22:17 BRT, após o agravamento do dia anterior; ainda exige teste controlado antes de qualquer operação/draft. Alerta WhatsApp seguiu falhando com HTTP 403 e houve rodada sem validação útil por timeout/aborto. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-03: Refresh OAuth do Bling confirmou agravamento: Matriz e Filial retornaram HTTP 403 “empresa inativa” nas execuções úteis observadas do dia; alerta WhatsApp também falhou com HTTP 403 e houve rodada sem validação útil por timeout/aborto. A consolidação diária posterior abortou por timeout e foi regularizada no ciclo seguinte. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-02: Refresh OAuth do Bling agravou o risco operacional pelo décimo nono dia de HTTP 403 na Filial: a Matriz conectou de manhã, mas também passou a retornar HTTP 403 “empresa inativa” nas execuções úteis de 13:33 e 18:33 BRT. Filial continuou bloqueada, alerta WhatsApp seguiu falhando com HTTP 403, uma rodada foi bloqueada por approvals/allowlist e uma teve fechamento abortado por timeout após captura do resultado. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-06-01: Refresh OAuth do Bling manteve o padrão crítico pelo décimo oitavo dia: Matriz OK nas execuções úteis observadas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403. Uma rodada foi bloqueada por allowlist/política de execução sem validação fiscal útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-31: Refresh OAuth do Bling manteve o padrão crítico pelo décimo sétimo dia: Matriz OK em todas as execuções observadas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-30: Refresh OAuth do Bling manteve o padrão crítico pelo décimo sexto dia: Matriz OK em todas as execuções observadas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403. Houve bloqueio inicial por allowlist em uma rodada, mas com rerun útil na mesma checagem. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-29: Refresh OAuth do Bling manteve o padrão crítico pelo décimo quinto dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada abortada por timeout sem validação fiscal útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-28: Refresh OAuth do Bling manteve o padrão crítico pelo décimo quarto dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de rodada bloqueada/abortada e uma resposta final abortada após captura de resultado. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-27: Refresh OAuth do Bling manteve o padrão crítico pelo décimo terceiro dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada abortada por SIGTERM após bloqueio inicial e uma rodada bloqueada por política/allowlist sem validação útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-24: Refresh OAuth do Bling manteve o padrão crítico pelo décimo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada bloqueada por allowlist/política de aprovação. Uma execução pós-consolidação anterior foi absorvida neste ciclo para não deixar lacuna. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-23: Refresh OAuth do Bling manteve o padrão crítico pelo nono dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada bloqueada por allowlist/política de aprovação e sessão abortada após captura parcial do resultado. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-22: Refresh OAuth do Bling manteve o padrão crítico pelo oitavo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de rodadas abortadas por timeout e bloqueadas por allowlist/política de execução. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-21: Refresh OAuth do Bling manteve o padrão crítico pelo sétimo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de bloqueios iniciais por allowlist e sessões abortadas antes de resposta consolidada. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-20: Refresh OAuth do Bling manteve o padrão crítico pelo sexto dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403 e uma rodada abortada antes de resultado fiscal útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-19: Refresh OAuth do Bling manteve o padrão crítico: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de bloqueios/abortos de automação. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- Bloqueio atual: qualquer fluxo dependente da Filial no Bling deve aguardar correção do token/status da empresa, validação de conectividade e estabilização da execução automática. A Matriz conectou nas execuções úteis observadas de 2026-06-04 a 2026-06-07, mas ainda precisa de teste controlado antes de operações/drafts.

## Estrutura de memória
- `memory/sessions/YYYY-MM-DD.md` — diário operacional do Fisco.
- `memory/context/decisions.md` — decisões fiscais vigentes registradas pelo Fisco.
- `memory/context/lessons.md` — aprendizados e riscos operacionais.
- `memory/pending.md` — pendências próprias do Fisco.

## 2026-03-31
- Primeira conversa. Workspace "fisco". Escolhi o nome **Fisco**.
- Idioma preferido do usuário: português (BR).

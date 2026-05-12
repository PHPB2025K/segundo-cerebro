# Auditoria de Skills — Daily Sales Report v2 — 2026-05-12

## Veredito
As skills existiam e cobriam o fluxo correto, mas não tinham gates suficientemente duros para impedir saída rasa. O problema de qualidade da Fase 4 não foi causado apenas por falta das próximas fases; foi principalmente falta de régua objetiva no Slack writer, account analysis e QA.

## Causa da queda de nível
1. **Fase 4 condensou demais**: o gerador pegou métricas da Fase 3 e transformou em resumo operacional raso.
2. **Skills diziam “profundo”, mas sem critério de bloqueio**: faltava definir que diagnóstico sem causa/evidência/risco/ação deve ser reprovado.
3. **Produto por SKU não estava bloqueado em QA**: havia regra de top produtos consolidado, mas não gate explícito para proibir SKU cru em mensagem individual.
4. **Memória ainda está no início**: ainda não há weekly/monthly madura, mas isso não justifica o nível raso; mesmo com 1 dia já dava para usar 30d/60d/mesmo-dia-semana e hipóteses melhores.

## Skills auditadas

### daily-sales-report
- Status antes: boa como skill operacional, mas ainda apontava o script legado como canônico e não reforçava v2 suficientemente.
- Ajuste: adicionada seção de scripts canônicos v2 + v1 legado/fallback.
- Risco resolvido: evitar que o Trader use o fluxo antigo quando deveria rodar v2.

### trader-daily-sales-memory-cycle
- Status antes: boa estrutura de memória, mas faltava cobrar uso ativo da memória para elevar inteligência.
- Ajuste: adicionada seção “Como a memória deve elevar inteligência”.
- Risco resolvido: impedir memória virar arquivo morto sem impacto na análise.

### trader-daily-sales-data-readiness
- Status antes: checks básicos bons, mas reconciliação `v_daily_sales` × `orders` ainda genérica.
- Ajuste: classificação de divergência e regra de freshness/estabilização.
- Risco resolvido: não aprovar preview com número oficial mudando sem regenerar.

### trader-daily-sales-account-analysis
- Status antes: listava métricas e heurísticas, mas sem régua de análise sênior.
- Ajuste: adicionada régua obrigatória: o que mudou, onde mudou, por que importa, hipótese provável e como confirmar/refutar amanhã.
- Risco resolvido: impedir análise interna que só lista números.

### trader-daily-sales-slack-writer
- Status antes: principal ponto fraco. Faltava padrão explícito para síntese acionável.
- Ajuste: bloqueios de baixa qualidade, proibição de SKU visível e modelo de prioridade boa.
- Risco resolvido: impedir mensagem do tipo “acompanhar volume/verificar anúncios”.

### trader-daily-sales-qa-escalation
- Status antes: bom QA geral, mas insuficiente contra saída rasa.
- Ajuste: `BLOQUEADO_QUALIDADE` para SKU cru, diagnóstico descritivo, prioridade genérica, ausência de temporalidade e títulos fora do padrão.
- Risco resolvido: QA passa a poder reprovar inteligência baixa, não só erro factual.

### trader-daily-sales-cron-orchestrator
- Status antes: ordem correta, mas citava skills opcionais que podem não existir e não tinha gate de qualidade pré-produção.
- Ajuste: gate de qualidade antes de produção e fallback para arquivos gerais quando skills opcionais não existirem.
- Risco resolvido: impedir cron de enviar automaticamente conteúdo fraco.

## Decisão operacional
A Fase 5 fica bloqueada até a Fase 4.1 gerar previews com:
- nomes comerciais de produtos;
- prioridades profundas;
- diagnóstico por conta com leitura temporal e hipótese;
- títulos Slack no padrão aprovado;
- QA `PASS` real, não apenas sintático.

## Arquivos endurecidos
- `skills/daily-sales-report/SKILL.md`
- `skills/trader-daily-sales-memory-cycle/SKILL.md`
- `skills/trader-daily-sales-data-readiness/SKILL.md`
- `skills/trader-daily-sales-account-analysis/SKILL.md`
- `skills/trader-daily-sales-slack-writer/SKILL.md`
- `skills/trader-daily-sales-qa-escalation/SKILL.md`
- `skills/trader-daily-sales-cron-orchestrator/SKILL.md`

# Lições — Fisco

_Atualizado: 2026-05-28_

## 2026-05-28
- Persistência do HTTP 403 da Filial por quatorze dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; rodadas sem validação por allowlist/SIGTERM continuam reduzindo a confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Quando o resultado fiscal é capturado mas a resposta final aborta por timeout, consolidar o achado operacional e registrar a falha de fechamento separadamente.

## 2026-05-27
- Persistência do HTTP 403 da Filial por treze dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; rodadas bloqueadas por política/allowlist e abortos/SIGTERM seguem reduzindo confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Rodadas abortadas ou bloqueadas antes de validação devem ser registradas como ausência de validação fiscal útil, mesmo quando outras rodadas do dia confirmam o padrão Matriz OK / Filial bloqueada.

## 2026-05-26
- Persistência do HTTP 403 da Filial por doze dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; rodadas bloqueadas por política/allowlist seguem reduzindo confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Rodadas em que a execução é bloqueada sem rerun útil devem ser registradas como ausência de validação fiscal, não como recuperação do Bling.

## 2026-05-25
- Persistência do HTTP 403 da Filial por onze dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Rodadas com allowlist miss e aborto por SIGTERM no mesmo dia mostram que a confiabilidade do cron segue sendo risco independente do erro fiscal principal; ausência de validação não pode ser lida como estabilidade.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade separado e ainda não foi mitigada.
- Quando uma rodada recupera execução após allowlist miss, consolidar o resultado fiscal útil; quando não há rerun ou o processo aborta antes do retorno, registrar explicitamente como rodada sem validação útil.

## 2026-05-24
- Persistência do HTTP 403 da Filial por dez dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; rodadas bloqueadas por política/allowlist continuam reduzindo a confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Rodadas pós-consolidação anterior precisam ser absorvidas no ciclo seguinte quando ocorrerem antes da virada BRT, para não abrir lacuna operacional.

## 2026-05-23
- Persistência do HTTP 403 da Filial por nove dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; ainda assim, rodadas bloqueadas por política/allowlist ou abortadas reduzem a confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Quando a rodada do refresh não executa por bloqueio de aprovação/allowlist, registrar como ausência de validação fiscal útil; não inferir melhora nem piora do Bling.

## 2026-05-22
- Persistência do HTTP 403 da Filial por oito dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco fiscal principal permanece concentrado na Filial; ainda assim, rodadas sem validação por timeout/allowlist reduzem a confiabilidade do monitoramento.
- A falha recorrente do alerta WhatsApp com HTTP 403 continua sendo risco de visibilidade independente da falha da Filial.
- Sessões abortadas sem captura de resultado fiscal útil precisam ser registradas como evento operacional separado: não confirmam recuperação nem piora da Filial, apenas ausência de validação.

## 2026-05-21
- Persistência do HTTP 403 da Filial por sete dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco principal permanece concentrado na Filial, no canal de alerta e na confiabilidade da automação.
- Bloqueios iniciais por allowlist e sessões abortadas antes de resposta consolidada seguem como riscos independentes do erro fiscal principal: mesmo quando o refresh roda e captura resultado, a resposta final do cron pode ficar incompleta.
- Sincronizar metadado de falha da Filial ajuda rastreabilidade, mas não reduz o bloqueio fiscal; a operação dependente da Filial continua parada até validação real de conectividade.

## 2026-05-20
- Persistência do HTTP 403 da Filial por seis dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- Matriz segue estável nas execuções completas do refresh, então o risco principal permanece concentrado na Filial, no canal de alerta e na confiabilidade da automação.
- Abortos/timeouts do cron podem impedir resposta consolidada e, em uma rodada, impedir até a captura de resultado fiscal útil; a consolidação diária precisa considerar sessões incompletas como risco operacional.
- Respostas de cron fiscal devem sempre incluir horário em BRT quando exibirem horário; padronizar isso evita mistura de UTC/BRT em auditoria operacional.

## 2026-05-19
- Persistência do HTTP 403 da Filial por cinco dias confirma bloqueio operacional formal; qualquer fluxo Filial → Simples deve continuar parado até correção do status/vínculo/token e teste controlado.
- A automação do refresh tem três riscos independentes: Filial inacessível, alerta WhatsApp falhando e política de execução/allowlist bloqueando rodadas do cron.
- Matriz segue majoritariamente renovando/conectando; um HTTP 403 pontual na validação da Matriz deve ser observado, mas ainda não muda o diagnóstico principal porque execuções posteriores conectaram normalmente.
- Sessões abortadas após captura de erro podem deixar o cron sem resposta final consolidada; a consolidação diária precisa absorver tool output relevante mesmo quando a resposta do worker não completou.

## 2026-05-18
- Persistência do HTTP 403 da Filial por quatro dias confirma bloqueio operacional contínuo; qualquer fluxo Filial → Simples deve continuar parado até correção formal e teste controlado.
- Matriz segue renovando/conectando, então o risco principal está isolado no vínculo/status da Filial e no canal de alerta, não no Bling como um todo.
- Falha recorrente do alerta WhatsApp cria risco de baixa visibilidade operacional; erro fiscal-operacional e erro de notificação devem ser tratados como pendências separadas.

## 2026-05-17
- Persistência do HTTP 403 da Filial por três dias confirma bloqueio operacional de cadastro/vínculo/token; qualquer fluxo Filial → Simples deve continuar parado até correção formal.
- A automação do refresh ainda tem dois riscos independentes: falha fiscal-operacional da Filial e bloqueio eventual por allowlist, que pode impedir até a checagem.
- Alerta WhatsApp permanece falhando com HTTP 403 quando o refresh detecta erro, então a visibilidade automática do problema não é confiável.

## 2026-05-16
- Repetição do HTTP 403 da Filial em todas as execuções observadas confirma bloqueio persistente de cadastro/vínculo/token; não tratar como oscilação de API.
- Alerta WhatsApp do refresh falhou junto com o problema principal em todas as execuções observadas do dia, reduzindo capacidade de notificação automática.

## 2026-05-15
- Cron fiscal não pode depender de aprovação interativa: quando a política de execução bloqueia comandos, o refresh Bling falha antes de validar Matriz/Filial.
- Erro recorrente HTTP 403 de Filial inativa no Bling deve ser tratado como bloqueio operacional, não instabilidade temporária; sem Filial ativa, fluxos de NF interna Filial → Simples ficam indisponíveis.
- Alerta WhatsApp também retornou HTTP 403 em pelo menos uma execução; falha de alerta não deve mascarar falha principal do refresh.

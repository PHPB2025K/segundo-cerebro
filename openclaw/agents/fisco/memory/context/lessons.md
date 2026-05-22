# Lições — Fisco

_Atualizado: 2026-05-21_

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

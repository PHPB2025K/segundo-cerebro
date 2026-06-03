# Pendências — Fisco

_Atualizado: 2026-06-02_

## 🔴 Prioridade Alta
- [ ] Bling Matriz: investigar agravamento HTTP 403 “empresa vinculada ao token está inativa” observado em 2026-06-02 às 13:33 e 18:33 BRT, antes de qualquer operação/draft dependente da Matriz.
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-06-02.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Matriz/Filial com HTTP 403, alertas WhatsApp com HTTP 403, bloqueios por allowlist/política de execução/aprovação e abortos/timeouts antes de fechamento consolidado. Reconfirmado em 2026-06-02.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-06-02.
- [ ] Após normalizar Bling Matriz e Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.
- [ ] Padronizar e estabilizar respostas do cron fiscal com horário em BRT quando houver horário visível; em 2026-06-02 houve uma rodada bloqueada sem validação útil e uma rodada com fechamento abortado por timeout.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

# Pendências — Fisco

_Atualizado: 2026-06-01_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-06-01.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Filial inativa, alertas WhatsApp com HTTP 403, bloqueios por allowlist/política de execução/aprovação e abortos/SIGTERM/timeout antes de validação ou resposta consolidada. Reconfirmado em 2026-06-01.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-06-01.
- [ ] Após normalizar Bling Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.
- [ ] Padronizar e estabilizar respostas do cron fiscal com horário em BRT quando houver horário visível; em 2026-06-01 houve respostas em BRT, mas uma rodada bloqueada ficou sem validação fiscal útil.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

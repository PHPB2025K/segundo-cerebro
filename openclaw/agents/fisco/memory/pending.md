# Pendências — Fisco

_Atualizado: 2026-06-04_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-06-04.
- [ ] Bling Matriz: validar recuperação e estabilidade após HTTP 403 “empresa vinculada ao token está inativa” observado em 2026-06-02 e 2026-06-03; voltou a conectar nas execuções úteis observadas de 2026-06-04, mas ainda exige teste controlado antes de qualquer operação/draft dependente da Matriz.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Filial com HTTP 403, histórico recente de Matriz com HTTP 403, alertas WhatsApp com HTTP 403 e abortos/timeouts antes de validação ou fechamento consolidado. Reconfirmado em 2026-06-04.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-06-04.
- [ ] Após normalizar Bling Matriz e Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.
- [ ] Regularizar lacunas de consolidação/monitoramento quando houver timeout/aborto; em 2026-06-03/2026-06-04 houve consolidação anterior abortada e rodadas de refresh sem validação útil.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

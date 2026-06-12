# Pendências — Fisco

_Atualizado: 2026-06-11_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-06-11.
- [ ] Bling Matriz: validar recuperação e estabilidade após HTTP 403 “empresa vinculada ao token está inativa” observado em 2026-06-02 e 2026-06-03; conectou nas execuções úteis observadas de 2026-06-04 a 2026-06-11, mas ainda exige teste controlado antes de qualquer operação/draft dependente da Matriz.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Filial com HTTP 403, histórico recente de Matriz com HTTP 403, alertas WhatsApp com HTTP 403 e bloqueios/lacunas por política de execução ou timeout. Reconfirmado em 2026-06-11.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-06-11.
- [ ] Após normalizar Bling Matriz e Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.
- [ ] Regularizar lacunas de consolidação/monitoramento quando houver timeout/aborto/bloqueio por política; em 2026-06-10 houve lacuna sem validação útil às 08:17 BRT por bloqueio de execução.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

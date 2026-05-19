# Pendências — Fisco

_Atualizado: 2026-05-18_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-05-18.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Filial inativa e bloqueio eventual por allowlist.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-05-18.
- [ ] Após normalizar Bling Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

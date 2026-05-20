# Pendências — Fisco

_Atualizado: 2026-05-19_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-05-19.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falhas atuais incluem Filial inativa, bloqueios por política de execução/allowlist e sessões abortadas após captura de erro.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que segue retornando HTTP 403 nas execuções observadas até 2026-05-19.
- [ ] Matriz Bling: observar se o HTTP 403 pontual em uma validação de 2026-05-19 se repete; execuções posteriores conectaram normalmente.
- [ ] Após normalizar Bling Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

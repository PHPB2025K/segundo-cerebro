# Pendências — Fisco

_Atualizado: 2026-05-16_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial. Reconfirmado em 2026-05-16.
- [ ] Refresh Bling cron: manter execução automática estável e monitorada; falha principal atual é a Filial inativa, com uma resposta parcial abortada em 16:16 BRT.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que retornou HTTP 403 em 2026-05-15 e novamente em todas as execuções observadas de 2026-05-16.
- [ ] Após normalizar Bling Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

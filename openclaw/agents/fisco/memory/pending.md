# Pendências — Fisco

_Atualizado: 2026-05-15_

## 🔴 Prioridade Alta
- [ ] Bling Filial: resolver erro HTTP 403 “empresa vinculada ao token está inativa” antes de qualquer emissão/draft dependente da Filial.
- [ ] Refresh Bling cron: ajustar execução para não depender de aprovação interativa e reduzir abortos por timeout.

## 🟡 Prioridade Média
- [ ] Alertas do refresh Bling: validar canal WhatsApp, que retornou HTTP 403 em 2026-05-15.
- [ ] Após normalizar Bling Filial, executar teste controlado de conectividade Matriz + Filial sem expor tokens/credenciais.

## 🟢 Backlog
- [ ] Estruturar logs auditáveis para futuras execuções de NF-e/drafts, distribuição e conciliação fiscal.

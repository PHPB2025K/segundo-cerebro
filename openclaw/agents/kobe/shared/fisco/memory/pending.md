# Pendências — [[agents/fisco/IDENTITY|Fisco]]

_Atualizado: 2026-05-01 23:30 BRT_

## 🔥 URGENTE

- [ ] **Roteamento direto do Fisco no OpenClaw** — `sessions_spawn agentId=fisco` retornou `allowed: none` em 01/05, apesar de Fisco estar cadastrado. Diagnosticar policy/runtime e restaurar delegação direta.
- [ ] **Ajuste histórico YW1520 na Matriz** — abril/2026 ficou coberto pela Filial, mas a Matriz aparece com inconsistência histórica de -315 un após março. Investigar saldo anterior, vendas B2B/atacado ou regra extraordinária.

## 🟡 MÉDIO PRAZO

- [ ] **Processo mensal de abatimento Matriz** — antes de usar saldo Matriz como excedente, consultar NFs B2B/atacado emitidas pela Matriz no período e abater estoque fiscal por SKU/componente.
- [ ] **product-packaging.json** — preencher pesos e volumes dos SKUs ativos; emissões futuras ainda dependem de aproximações quando pesos reais faltam.
- [ ] **Cadastro Bling Filial** — validar origem 2 nos produtos importados próprios e manter cadastros unitários/caixa coerentes.
- [ ] **29 produtos origem=0/mal classificados na Matriz** — limpar pseudo-itens e classificar kits/vasos/itens importados com input Suellen quando necessário.
- [ ] **Monitorar DFC Filial pós-regime v2.1** — sem crédito ICMS/IPI na transferência, acompanhar 60–90 dias antes de revisar margem interna de 5%.
- [ ] **Atualizar PDF oficial estratégia fiscal v2.0 → v2.1** — vault já tem regra, mas PDF oficial precisa incorporar orientação Suellen 24/04.

## 📋 BACKLOG

- [ ] **Deletar NFs de teste antigas** — Filial 011–027 e Matriz 611–616, se ainda existirem como rascunho.
- [ ] **Monitor Simples Nacional** — Módulo E: acompanhar faturamento acumulado 2026 por CNPJ vs teto R$4,8M/ano.
- [ ] **Faturamento B2B mensal da Filial/Matriz** — levantar parcela B2B para calibrar distribuição e conciliação.

## Resolvido em 2026-05-01

- ✅ NFs internas abril/2026 emitidas e autorizadas: 000031, 000032, 000033.
- ✅ PDFs/XMLs das NFs internas enviados à FOUR e ao financeiro.
- ✅ NFs de transferência abril/2026 000649 e 000653 localizadas, baixadas e enviadas à FOUR com CC financeiro.
- ✅ Escopo CK4742/Jarra Clink definido como fora de importação própria GB.

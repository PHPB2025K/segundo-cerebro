---
title: "nfe log"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Log de Auditoria Fiscal — NF-e

_Append-only. Nunca deletar entradas._

---

## 2026-03-30 — Testes / Rascunhos

| NF# | Conta | Destinatário | CFOP | Valor | Status | Obs |
|-----|-------|-------------|------|-------|--------|-----|
| 000611–000616 | Matriz | Testes | — | — | Rascunho | NFs de teste. Deletar manualmente. |
| 000011–000027 | Filial | Testes | — | — | Rascunho | NFs de teste. Deletar manualmente. |
| 000613 | Matriz | Filial (0002-24) | 6152 | R$ 690,97 | Rascunho | Primeiro draft de transferência. Incompleto (sem volumes). |

---

## 2026-03-31 — Venda Interna Março/2026 ✅ EMITIDAS

### FILIAL (58.151.616/0002-24) → CNPJs Simples | CFOP 5102 | ICMS 18%

| NF# | Destinatário | CNPJ | Valor | Status | Chave |
|-----|-------------|------|-------|--------|-------|
| 000028 | GB Comércio | 07.194.128/0001-82 | R$ 15.905,61 | ✅ Autorizada SEFAZ | 35260358151616000224550010000000281517660484 |
| 000029 | Trades | 45.200.547/0001-79 | R$ 3.726,67 | ✅ Autorizada SEFAZ | 35260358151616000224550010000000291517673079 |
| 000030 | Broglio | 63.922.116/0001-06 | R$ 3.580,91 | ✅ Autorizada SEFAZ | 35260358151616000224550010000000301517685620 |

**Subtotal Filial: R$ 23.213,19**

### MATRIZ (58.151.616/0001-43) → CNPJs Simples | CFOP 6102 | ICMS 4% (excedente)

| NF# | Destinatário | CNPJ | Valor | Status | Chave |
|-----|-------------|------|-------|--------|-------|
| 000617 | GB Comércio | 07.194.128/0001-82 | R$ 3.023,23 | ✅ Autorizada SEFAZ | 42260358151616000143550010000006171254514874 |
| 000618 | Trades | 45.200.547/0001-79 | R$ 716,86 | ✅ Autorizada SEFAZ | 42260358151616000143550010000006181254514871 |
| 000619 | Broglio | 63.922.116/0001-06 | R$ 2.402,57 | ✅ Autorizada SEFAZ | 42260358151616000143550010000006191254514879 |

**Subtotal Matriz: R$ 6.142,66**

---

**TOTAL VENDA INTERNA MARÇO/2026: R$ 29.355,85**

---

### Contatos criados na Filial (31/03/2026)

| Empresa | CNPJ | ID Bling Filial |
|---------|------|----------------|
| GB Comércio | 07.194.128/0001-82 | 18049415386 |
| Trades | 45.200.547/0001-79 | 18049415397 |
| Broglio | 63.922.116/0001-06 | 18049415404 |

### IEs dos destinatários (confirmadas via API Bling Matriz)

| Empresa | IE |
|---------|-----|
| GB Comércio | 519097120117 |
| Trades | 519087807114 |
| Broglio | 519001780113 |

### Artefatos

- XMLs: máquina Pedro → Downloads/NOTAS FISCAIS DE TRANSFERENCIA GB/
  - Subpasta: NOTAS VENDA INTERNA FILIAL/ (NFs 028–030)
  - Subpasta: NOTAS VENDA INTERNA MATRIZ/ (NFs 617–619)
- Relatório PDF: RELATORIO_NFs_VENDA_INTERNA_MARCO_2026.pdf
- Docx resumo: `shared/fisco/reference/resumo-nfs-venda-interna-marco-2026.docx`

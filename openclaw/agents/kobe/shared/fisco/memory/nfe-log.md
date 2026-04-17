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

---

## 2026-04-17 — GB25011 container Itajaí→Pedreira via Qualilog (Módulo B 90/10)

### Rascunhos criados via API Bling Matriz ✅ (aguardando aprovação Pedro para /enviar)

| NF# | Tipo | Destinatário | CFOP item | Valor | Situação | ID Bling | Obs |
|-----|------|-------------|-----------|-------|----------|----------|-----|
| 000648 | Entrada | Open Trade (07.104.810/0001-37) | 1949 | R$ 76.222,43 | 1 (rascunho) | 25595124221 | Registra NF 580012 da OT (chave 42260407104810000137550010005800121011014742). Natureza "Compra de mercadoria" (15106994869) como **fallback** — não existe natureza específica de entrada por importação por conta e ordem cadastrada. |
| 000649 | Saída | Filial SP (58.151.616/0002-24) | 6152 | R$ 68.192,51 | 1 (rascunho) | 25595135504 | 21 itens × 90% (floor), preço unit = v.unit NF 580012. Retenção Matriz: 123 cx (10%). Natureza 15107242313 "TRANSFERÊNCIA DE MERCADORIA". Transportador Qualilog id 17617371612. 1044 cx / 15.136,07 kg bruto. |

**Artefatos:** `~/Documents/01-Importacao/GB25011-NF-TRANSFERENCIA/` (build_payloads.py + dois JSONs). Na VPS: `/tmp/GB25011-NF-TRANSFERENCIA/`.

**Ordem obrigatória para emissão SEFAZ:**
1. Aprovar e enviar a entrada 000648 primeiro — sem ela, 2 SKUs (KIT9S098 saldo 17 / pedido 90, KIT6S100 saldo 25 / pedido 45) ficam com estoque negativo.
2. Depois aprovar e enviar a transferência 000649.

**Pendências decorrentes (não bloqueantes para esta operação):**
- NCM e origem dos 21 SKUs estão vazios no cadastro Bling → PATCH /produtos preenchendo NCM=70134900 origem=2.
- `product-packaging.json` vazio para todos os SKUs → preencher pesos reais (payload atual usa rateio proporcional do peso total da 580012).
- Criar natureza de operação específica "Entrada por importação por conta e ordem" (CFOP 1949) no painel Bling — Suellen valida depois, mas evita reuso de "Compra de mercadoria" como fallback em próximas importações.
- Qualilog está cadastrada como "QUALILOG TRANSPORTES LTDA EM RECUPERACAO JUDICIAL" — informativo.
- Bug Bling API v3: GET /nfe/{id} e GET /naturezas-operacoes/{id} retornam null/404 mesmo para IDs válidos. Listagem com filtros funciona.

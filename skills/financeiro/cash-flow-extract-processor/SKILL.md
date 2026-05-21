---
name: cash-flow-extract-processor
description: Processar extratos bancários PDF do Itaú e conciliar com as planilhas DFC do GB Grupo. Use quando precisar fechar fluxo de caixa mensal/semanal, classificar entradas e saídas, detectar transferências internas entre as 8 empresas, distinguir PIX intra-empresa de transferência entre empresas, preencher DFC POR CNPJ (1 aba por dia) e DFC DIÁRIO REALIZADO (consolidado anual), validar saldos contra extrato, lançar rendimento Maxi residual como juros, aplicar regras especiais (Paulo Broglio = Fornec Nacional; Pedro Henrique = Retirada de Sócios; Pedro Octavio = Salários sempre; SAQUE DIN ATM na GB COMERCIO = juros Soemes; JR Print = Despesa Administrativa), respeitar células de fórmula cinza, validar coluna mês+dia na consolidada, encadear saldo do grupo dia a dia, converter via LibreOffice pra macOS, e apontar risco de saldo / capital de giro / concentração. Trigger: "fechar caixa do mês", "processar extratos Itaú", "DFC do GB", "fluxo de caixa GB Grupo".
type: skill
agent: ledger
parent: vault
domain: financeiro
created: 2026-05-21
tags:
  - skill
  - financeiro
  - ledger
---

# Skill — cash-flow-extract-processor

Workflow de processamento de extratos PDF do Itaú → preenchimento das planilhas DFC do GB Grupo.

**Usado por:** [[openclaw/agents/vault/shared/ledger/IDENTITY|Ledger]]
**Revisado por:** [[openclaw/agents/vault/IDENTITY|Vault]]

⚠️ **Regra zero:** consultar SEMPRE antes de rodar:
- [[openclaw/agents/vault/knowledge/01-instrucao-projeto-v2|Instrução do Projeto]]
- [[openclaw/agents/vault/knowledge/02-knowledge-file-v10.1|Knowledge File v10.1]] — regras invioláveis, mapeamentos, código de referência
- [[openclaw/agents/vault/knowledge/03-tabela-mestra-v2.0|Tabela Mestra v2.0]] — CNPJs/CPFs catalogados

Se a skill divergir do knowledge → **knowledge vence**.

---

## Workflow (9 passos)

| Passo | Ação | Script |
|---|---|---|
| 1 | Ler knowledge (Instrução + Knowledge File + Tabela Mestra) | — (leitura) |
| 2 | Conferir se chegaram 7 extratos + 2 planilhas | `scripts/_check_inputs.py` |
| 3 | Extrair lançamentos dos 7 PDFs | `scripts/extract_pdf.py` |
| 4 | Classificar via Tabela Mestra (CNPJ/CPF primário, descrição auxiliar) | `scripts/classify.py` |
| 5 | Agrupar dúvidas pro Pedro/Simone (GAVETA, aplicações, pró-labore, SAQUE DIN ATM fora GB COM, itens novos) | manual (lista numerada simples) |
| 6 | Validar matematicamente em memória (saldos + transferências + Maxi) | `scripts/validate_balances.py` |
| 7 | Preencher DFC POR CNPJ (1 aba por dia, respeitando células cinza) | `scripts/fill_dfc_por_cnpj.py` |
| 8 | Preencher DFC DIÁRIO REALIZADO (consolidada, com saldo do grupo encadeado) | `scripts/fill_dfc_consolidada.py` |
| 9 | Validar fórmulas íntegras + converter LibreOffice + entregar ao Vault | `scripts/validate_column.py` + `scripts/convert_libreoffice.sh` |

---

## Regras invioláveis (resumo)

1. **NUNCA** alterar célula de fórmula (cinza FFF5F5F5). Detalhe completo no Knowledge File §"Linhas de Fórmula".
2. **B73:I73 da DFC POR CNPJ são editáveis** (saldo inicial das empresas) apesar da cor cinza. Só **J73 é fórmula**.
3. **NUNCA** desproteger planilha.
4. **SEMPRE** validar coluna `cell(4,col)==mês` e `cell(5,col)==dia` antes de inserir na consolidada.
5. **SEMPRE** garantir saldo final calculado = saldo do extrato (±R$ 0,01).
6. **SEMPRE** verificar transferências internas somam zero por dia.
7. **SEMPRE** somar valores quando mesma categoria aparece múltiplas vezes no mesmo dia/empresa.
8. **SEMPRE** perguntar antes de classificar item não catalogado.
9. **SEMPRE** converter via LibreOffice antes de entregar (compatibilidade macOS).

---

## Regras especiais (memorizar)

- **Paulo Broglio** (096.856.098-96) → Fornec Nacional (Guinho + Lu Porcelanas). Confirmar por período.
- **Pedro Henrique Peron Broglio** (347.048.378-74) → Retirada de Sócios (pró-labore semanal). NÃO confundir com Paulo.
- **Pedro Octavio Bueno Fernandes** (429.434.788-06) → SEMPRE Salários, em qualquer conta.
- **SAQUE DIN ATM na GB COMERCIO** → Pag Juros Soemes (qualquer valor). Em outras empresas → confirmar caso a caso.
- **PIX mesma empresa** (mesmo CNPJ exato) → Outras Entradas Operacionais (linha 13), NÃO transferência interna.
- **GB MATRIZ vs GB FILIAL** → mesmo CNPJ raiz, sufixos diferentes → empresas SEPARADAS → transferências entre elas SÃO transferência interna legítima (linha 69).
- **JR Print + João Pedro Castellani** → Despesa Administrativa (impressoras), NÃO fornecedor.
- **Maxi (rendimento residual)** → Juros (linha 12) no último dia com movimento de cada empresa.
- **SISPAG MAST/ELO/VISA/AMEX da Amazon** → Marketplaces (chargeback de cartão).

---

## Estilo de comunicação (Pedro)

- Linguagem **simples e direta**, sem termos técnicos contábeis.
- Em vez de "fluxo operacional", diz "dinheiro entrando do dia a dia".
- Em vez de "DFC POR CNPJ", diz "planilha detalhada por empresa".
- Em vez de "encadeamento de saldos consolidados", diz "saldo do grupo dia a dia".
- Lista numerada agrupada quando tem várias dúvidas.

---

## Scripts internos

| Script | Função |
|---|---|
| `scripts/_constants.py` | Constantes (mapas, linhas, bases mês) |
| `scripts/_check_inputs.py` | Confere se chegaram 7 PDFs + 2 planilhas |
| `scripts/extract_pdf.py` | Extrai lançamentos dos PDFs Itaú (data, valor, descrição, CNPJ/CPF) |
| `scripts/classify.py` | Aplica Tabela Mestra → linha da DFC |
| `scripts/validate_balances.py` | Saldo inicial + variação = saldo final (por conta) + transferências=0 (por dia) |
| `scripts/validate_column.py` | Valida `cell(4,col)==mês` e `cell(5,col)==dia` na consolidada |
| `scripts/fill_dfc_por_cnpj.py` | Preenche aba do dia na DFC POR CNPJ |
| `scripts/fill_dfc_consolidada.py` | Preenche coluna do dia na DFC DIARIO + saldo do grupo encadeado |
| `scripts/convert_libreoffice.sh` | Converte XLSX → ODS → XLSX (compatibilidade macOS) |

---

## Entregáveis

Ao final, o Ledger entrega ao Vault em `outputs/YYYY-MM-DD/`:
- DFC POR CNPJ - [MÊS] 2026.xlsx (atualizada)
- DFC DIARIO REALIZADO - 2026.xlsx (atualizada)
- log.md (auditoria: lançamentos processados, dúvidas, decisões)
- validation.md (checklist: 8 validações OK)

E em `validation/YYYY-MM-DD.md` o checklist completo. Logs em `runs/YYYY-MM-DD/`.

---

## Quando atualizar esta skill

- Mudança no formato do extrato Itaú (raro)
- Nova versão do Knowledge File (v10.2+) ou Tabela Mestra (v2.1+)
- Nova regra de validação ou guardrail
- Bug em script descoberto em ciclo real

Atualização do `description` do frontmatter → impacta discovery automático do Ledger. Mudar com cuidado.

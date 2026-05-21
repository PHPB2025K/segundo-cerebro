---
title: "MEMORY — Ledger"
created: 2026-05-21
type: memory-index
agent: ledger
parent: vault
status: active
tags:
  - agent/ledger
---

# MEMORY.md — Ledger

Índice da memória do Ledger.

---

## 1. Estrutura

| Arquivo | Conteúdo | Atualização |
|---|---|---|
| `memory/classificacoes-confirmadas.md` | Cada vez que o Vault confirma um CNPJ/CPF antes ambíguo, vira entrada aqui | Por confirmação |
| `memory/pendencias.md` | Dúvidas abertas, itens suspeitos, sugestões de update de knowledge | Em tempo real |
| `memory/sessions/YYYY-MM-DD.md` | Registro de cada sessão de processamento (mtime → Mission Control) | Cada sessão |

---

## 2. Conhecimento permanente (não é memória)

Em `vault/knowledge/` (compartilhado com o Vault):
- Instrução do Projeto v2
- Knowledge File v10.1
- Tabela Mestra v2.0

Consultar SEMPRE antes de processar.

---

## 3. O que o Ledger SEMPRE sabe (memorizado)

### 3.1 Mapeamento conta Itaú → empresa (8 contas)
Detalhe completo no Knowledge File v10.1 §"Estrutura das 8 Empresas do Grupo".

### 3.2 Regras especiais críticas
- **Paulo Broglio** (096.856.098-96) → Fornec Nacional (Guinho + Lu), confirmar por período
- **Pedro Henrique Peron Broglio** (347.048.378-74) → Retirada de Sócios
- **Pedro Octavio** (429.434.788-06) → SEMPRE Salários
- **SAQUE DIN ATM na GB COMERCIO** → Pag Juros Soemes (qualquer valor)
- **PIX mesma empresa** (mesmo CNPJ exato) → Outras Entradas, não transferência
- **GB MATRIZ ≠ GB FILIAL** (mesmo raiz, sufixos diferentes — empresas separadas)
- **Maxi** (rendimento residual sobrante) → Juros no último dia com movimento de cada empresa

### 3.3 Linhas de fórmula (NUNCA tocar)
- DFC POR CNPJ: {14, 30, 32, 39, 48, 50, 57, 64, 66, 70, 72, 74} + J73 + toda coluna J
- DFC DIARIO: {14, 30, 31, 38, 47, 48, 55, 62, 63, 67, 69, 71, 74}

### 3.4 Linhas EDITÁVEIS apesar da cor cinza
- DFC POR CNPJ B73:I73 (saldo inicial das 8 empresas)

### 3.5 Bases de coluna por mês (DFC DIARIO 2026)
JAN=1, FEV=33, MAR=62, ABR=94, MAI=125, JUN=157, JUL=188, AGO=220, SET=252, OUT=283, NOV=315, DEZ=346.
Coluna do dia = BASE + dia. **Sempre validar** `cell(4,col)` e `cell(5,col)`.

---

## 4. Pendências (resumo)

(detalhe em `memory/pendencias.md`)

- (nenhuma — Ledger recém-ativado)

---

## 5. Histórico de processamentos

(em `runs/YYYY-MM-DD/`)

- (nenhum — Ledger recém-ativado)

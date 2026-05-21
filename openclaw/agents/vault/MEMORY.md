---
title: "MEMORY"
created: 2026-05-21
type: memory-index
agent: vault
status: active
tags:
  - agent/vault
---

# MEMORY.md — Vault

Índice da memória do Vault. Conteúdo detalhado vive nos arquivos referenciados.

---

## 1. Estrutura de memória

| Arquivo | Conteúdo | Atualização |
|---|---|---|
| `memory/decisions.md` | Decisões financeiras tomadas (com data, contexto, owner) | Cada decisão nova |
| `memory/lessons.md` | Lições aprendidas em fechamentos passados | Quando algo der errado e for generalizável |
| `memory/posicao-caixa/YYYY-MM.md` | Snapshot mensal do fechamento (saldo, variação, pontos) | Mensal |
| `memory/sessions/YYYY-MM-DD.md` | Registro de cada sessão de trabalho (mtime usado pelo Mission Control) | Cada sessão |

---

## 2. Conhecimento permanente (NÃO é memória, é referência)

Em `vault/knowledge/`:
- **Instrução do Projeto v2** — passo a passo + estilo de comunicação
- **Knowledge File v10.1** — regras, estrutura das planilhas, mapeamentos, código de referência
- **Tabela Mestra v2.0** — CNPJs/CPFs catalogados por categoria

Estes 3 arquivos são **versionados**. Quando há atualização significativa, o Ledger gera nova versão e o Vault aprova a substituição.

---

## 3. O que o Vault SEMPRE sabe (memorizado)

### 3.1 Estrutura do grupo
- 8 empresas (mapeamento CNPJ ↔ conta Itaú ↔ coluna na DFC no Knowledge File §"Mapeamento Contas Itaú")
- GB MATRIZ ≠ GB FILIAL (mesmo CNPJ raiz, sufixos diferentes — empresas separadas)
- DFC POR CNPJ = só conta principal Itaú; não consolida todas as contas bancárias da empresa

### 3.2 Regras especiais críticas (não esquecer)
- Paulo Broglio → Fornec Nacional (Guinho + Lu); confirmar a cada período com Simone
- Pedro Henrique Peron Broglio → Retirada de Sócios (NÃO confundir com Paulo)
- Pedro Octavio → SEMPRE Salários
- SAQUE DIN ATM na GB COMERCIO → Pag Juros Soemes (qualquer valor)
- PIX mesma empresa → mesma empresa (mesmo CNPJ exato) → Outras Entradas, não transferência
- JR Print + João Pedro Castellani → Despesa Administrativa (não fornecedor)
- Maxi (rendimento residual) → Juros no último dia com movimento de cada empresa

### 3.3 Estilo de comunicação com Pedro
- Linguagem simples, sem jargão contábil
- Foto curta + leitura + ação
- Agrupar perguntas em lista numerada
- Quantificar impacto em R$ sempre

---

## 4. Pendências de governança financeira

(seção atualizada conforme surgirem)

- [ ] (nenhuma ainda — Vault recém-ativado)

---

## 5. Histórico de fechamentos

(snapshots em `memory/posicao-caixa/YYYY-MM.md` à medida que forem feitos)

- (nenhum fechamento ainda — Vault recém-ativado)

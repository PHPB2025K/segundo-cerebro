---
title: "Pilares Financeiros — Fontes Canônicas"
created: 2026-05-23
type: knowledge
agent: vault
status: active
version: "1.0"
tags:
  - agent/vault
  - agent/ledger
  - financeiro
  - paths
---

# 04 — Pilares Financeiros: Fontes Canônicas

> **Regra absoluta para Vault, Ledger e Kobe.**
> Toda pergunta envolvendo **Fluxo de Caixa**, **DRE** ou **Balanço Patrimonial** da GB Importadora deve ser respondida consultando EXCLUSIVAMENTE os arquivos abaixo. Não inferir de Supabase, não usar versões antigas, não pedir ao Pedro o que já está aqui.

---

## Origem e propagação

- **Fonte da verdade:** Mac do Pedro em `~/Documents/03-Financeiro/PILARES-FINANCAS/`
- **Espelho na VPS (read-only):** `/root/.openclaw/workspace/financeiro/PILARES-FINANCAS/`
- **Sincronização:** unidirecional Mac → VPS via `launchd` a cada **1 hora** (job `com.pedro.financeiro-sync`)
- **Defasagem máxima esperada:** 60 minutos
- **Nenhum agente pode escrever** nesse espelho. Output do Ledger/Vault vai para pasta separada de derivados.

---

## Raiz canônica (na VPS, onde Vault/Ledger leem)

```
/root/.openclaw/workspace/financeiro/PILARES-FINANCAS/ORÇAMENTO 2026/
```

## Mapa por pilar (com versão ativa)

### 1. FLUXO DE CAIXA (DFC)

**Consolidado diário do ano (todas as empresas):**
- `ORÇAMENTO 2026/FLUXO DE CAIXA/DFC DIARIO REALIZADO - 2026.xlsx`

**Detalhado por CNPJ (1 arquivo por mês):**
```
ORÇAMENTO 2026/FLUXO DE CAIXA - POR CNPJ/
├── DFC POR CNPJ - JANEIRO/DFC POR CNPJ - JANEIRO 2026.xlsx
├── DFC POR CNPJ - FEVEREIRO/DFC_POR_CNPJ_-_FEVEREIRO_2026.xlsx
├── DFC POR CNPJ - MARÇO/DFC_POR_CNPJ_-_MARCO_2026.xlsx
├── DFC POR CNPJ - ABRIL/DFC_POR_CNPJ_-_ABRIL_2026.xlsx
├── DFC POR CNPJ - MAIO/DFC POR CNPJ - MAIO 2026.xlsx
└── DFC POR CNPJ - JUNHO..DEZEMBRO/  (pastas vazias aguardando o mês)
```

### 2. DRE

```
ORÇAMENTO 2026/DRE/
├── 02_DRE_GB_PROCESSADO (7).xlsx   ← VERSÃO ATIVA
└── FORMULARIO_DRE_GB.xlsx          (template — não consultar para dados)
```

### 3. BALANÇO PATRIMONIAL

```
ORÇAMENTO 2026/BALANÇO/
├── 03_BALANCO_GB_PARCIAL (2).xlsx                       ← VERSÃO ATIVA
├── BALANÇO PATRIMONIAL - GB IMPORTADORA - 2026.xlsx     (versão anterior — só para comparação)
└── MANUAL DE PREENCHIMENTO - BALANÇO.pdf
```

### 4. FINANÇAS MARKETPLACE (auxiliar)

```
ORÇAMENTO 2026/FINANÇAS MARKETPLACE/
└── DRE_Fevereiro_2026.xlsx   (uso pontual; NÃO substitui o DRE consolidado)
```

---

## Regras de leitura (Vault e Ledger)

1. **Versão ativa = arquivo de maior data de modificação** dentro de cada pilar.
2. **Padrão de nomenclatura "ativo":** prefixo `0X_` + sufixo `_PROCESSADO` ou `_PARCIAL` com número entre parênteses → essas são as versões trabalhadas.
3. **DFC consolidado** (`FLUXO DE CAIXA/`) é a fonte única para perguntas agregadas. **DFC POR CNPJ** só quando a pergunta especificar empresa ou mês isolado.
4. **Ignorar sempre:** arquivos `~$*.xlsx` (locks do Excel) e `.DS_Store`.
5. **Histórico 2025:** `ORÇAMENTO 2025/` — só usar para comparação histórica explícita.
6. **Se um arquivo esperado não existe:** consultar log `/var/log/budamix-financeiro-sync.log` na VPS; se sync OK e arquivo ausente, perguntar ao Pedro via Kobe antes de assumir.

---

## Pseudocódigo de roteamento

```
SE pergunta envolve (fluxo de caixa | DRE | balanço | DFC | resultado financeiro GB):
    BASE = "/root/.openclaw/workspace/financeiro/PILARES-FINANCAS/ORÇAMENTO 2026/"
    pilar = identificar(pergunta)  # DFC | DRE | BALANÇO
    arquivo = mais_recente_em(BASE + pilar)
    SE arquivo não acessível → reportar ao Kobe "espelho desatualizado, último sync em X"
    SENÃO → ler e responder
SENÃO:
    seguir rota padrão do agente
```

---

## Frescor e saúde do espelho

- **Log local (Mac):** `~/Library/Logs/budamix-financeiro-sync.log`
- **Log remoto (VPS):** `/var/log/budamix-financeiro-sync.log`
- **Última linha do log = `[YYYY-MM-DD HH:MM:SS] sync OK from Mac`** → espelho está fresco.
- Se a última entrada tiver mais de 2 horas, o Mac provavelmente está desligado/dormindo — declarar essa incerteza antes de responder.

---

## Histórico de mudanças

| Data | Mudança | Versão |
|---|---|---|
| 2026-05-23 | Criação. Sync Mac→VPS a cada 1h via launchd. | 1.0 |

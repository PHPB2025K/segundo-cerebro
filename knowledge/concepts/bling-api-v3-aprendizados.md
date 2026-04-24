---
title: "Bling API v3 — Aprendizados operacionais"
created: 2026-04-24
type: concept
status: active
tags:
  - knowledge
  - bling
  - api
  - fisco
  - nfe
---

# Bling API v3 — Aprendizados operacionais

> Comportamentos não-óbvios da API v3 do Bling descobertos emitindo NF de transferência GB25010 (#000653, 24/04/2026). Complementa a skill `shared/fisco/skills/bling-nfe/SKILL.md` no OpenClaw.

## 1. `PUT /nfe/{id}` não aceita patch parcial

A API v3 **substitui o recurso inteiro** no PUT — não faz merge de campos enviados com o estado atual.

**Sintoma:** enviar só `{"observacoes": "..."}` retorna 400 com 4 erros:
```
- "A nota deve ter ao menos um item"
- "É necessário informar o número da nota fiscal"
- "Data de operação inválida"
- "O número do documento do contato não foi informado."
```

**Solução:**
- Adicionar/alterar campos no rascunho → recuperar estado completo via GET, mesclar no cliente, enviar o payload inteiro no PUT.
- OU: usar o painel web do Bling para ajustes pequenos pós-criação.

**Impacto prático:** para NFs em rascunho, é mais rápido reemitir uma v2 (DELETE + POST com payload correto) do que tentar PUT incremental.

---

## 2. CFOP e tributos no payload da API são **ignorados**

Confirmado na emissão da NF 000653. Campos como `cfop`, `impostos.icms.*`, `impostos.pis.*`, `impostos.cofins.*`, `impostos.ipi.*` enviados no payload da NF **não são persistidos** — o Bling preenche tudo a partir da regra fiscal configurada na Natureza de Operação (painel web).

**Sintoma:** item enviado sem `cfop` aparece no GET com `cfop: 6152` (veio da Natureza ID 15107242313 cadastrada no painel).

**Pré-requisito obrigatório (1x no painel):** cada Natureza de Operação usada precisa ter regra fiscal configurada (CFOP, CST, alíquota, base cálculo). Sem isso, a SEFAZ rejeita a NF na hora de enviar.

**Payload mínimo do item (suficiente):**
```json
{
  "codigo": "IMB501C",
  "descricao": "Conjunto de 5 Potes, Tampa Cinza",
  "unidade": "CX",
  "quantidade": 334,
  "valor": 64.42,
  "tipo": "P",
  "pesoBruto": 14.54,
  "pesoLiquido": 13.62,
  "classificacaoFiscal": "70134900",
  "origem": 2
}
```

**NÃO enviar:** `cfop`, `impostos` (qualquer subcampo), `cst`.

---

## 3. Código do SKU em NF ≠ necessariamente o código interno do cadastro

Padrão GB Importadora descoberto em 24/04/2026:

| Código Bling | Unidade de cadastro | Uso em NF |
|--------------|:-------------------:|-----------|
| `IMB501C` | UN (indefinida na API) | Emissão de NF de transferência **em CX** com preço R$/CX |
| `CXIMB501C` | — | Produto separado: "Caixa Conjunto de 5 Potes, Tampa Cinza 12UN" (cadastro de embalagem) |

A hipótese inicial (prefixo `CX` era obrigatório na emissão) estava **errada**. A NF de transferência anterior do Bling confirmou que:
- Código usado: SEM prefixo CX (`IMB501C`, `YW640RC`, etc.)
- Unidade exibida: CX
- Preço: R$ por CX

**Implicação:** ao mapear SKUs da DANFE para IDs do Bling, buscar sempre o código SIMPLES primeiro; o cadastro com prefixo CX é produto distinto (embalagem).

---

## 4. Busca por código usa query param `codigo`, não `pesquisa`

```
GET /produtos?pesquisa=YW640RC
```
→ Retorna primeiros 10 produtos genéricos, ignora o filtro.

```
GET /produtos?codigo=YW640RC
```
→ Retorna match exato pelo campo `codigo`.

Para busca textual por nome/descrição, `pesquisa` funciona; para código interno, usar sempre `codigo`.

---

## 5. Rate limit 3 req/s por conta

Bling v3 aceita no máximo 3 requisições por segundo por conta. Em lote (ex: buscar 9 produtos por código), usar `sleep 0.4` entre calls para ficar folgado e evitar 429. Se 429 acontecer: aguardar 2s e retry (máx 3 tentativas) — conforme skill `bling-nfe`.

---

## 6. Tokens OAuth Matriz/Filial têm refresh automático via cron (5h)

No VPS OpenClaw:
- `/root/.openclaw/workspace/scripts/bling-oauth/tokens-matriz.json` e `tokens-filial.json`
- Refresh via `refresh-tokens.py` (cron)
- `refreshed_at` confirma última execução

Na prática, token Matriz estava válido na sessão (refreshed_at 12:14 UTC mesma manhã, expires_in 21600s = 6h). Fluxo de integração não precisa se preocupar com expiração dentro de uma sessão típica; se expirar mid-session, rodar `refresh-tokens.py` manualmente.

---

## 7. Clone de SKU por herança de linha

Para cadastrar um SKU novo via `POST /produtos` preservando metadados fiscais consistentes:

1. GET /produtos/{id_irmao_linha} — pegar categoria, marca, NCM, origem, tipoProducao
2. Montar payload mínimo trocando apenas `nome` e `codigo`
3. POST /produtos

Exemplo: YW1520RC clonado a partir de YW1050RC (mesma linha YW, categoria 11053878, NCM 7013.49.00, origem 2 importado, marca "GB Importadora") — preserva consistência fiscal sem configurar caso a caso.

---

## 8. Regra inviolável: rascunho-primeiro

`POST /nfe` cria com `situacao: 1` (pendente/rascunho). Pode ser **deletado** via DELETE /nfe/{id}. É seguro criar, conferir no painel, iterar.

`POST /nfe/{id}/enviar` transmite à SEFAZ → `situacao: 6` (autorizada) → **irreversível**. Cancelamento pós-autorização vira CC-e (carta de correção) ou NF de ajuste, com prazo legal e processo próprio.

**Nunca chamar `/enviar` sem aprovação explícita do Pedro após validação visual no painel.**

---

## Referências
- Doc oficial: https://developer.bling.com.br/referencia
- Skill detalhada: `~/.openclaw/workspace/shared/fisco/skills/bling-nfe/SKILL.md` (VPS)
- Skill transferência: `~/.openclaw/workspace/shared/fisco/skills/nf-transfer/SKILL.md` (VPS) — espelhada em `skills/fiscal/nf-transfer/`
- Log de auditoria: `shared/fisco/memory/nfe-log.md` (VPS) — registra toda emissão
- Fonte de verdade fiscal: [[business/importacao/estrategia-fiscal-gb]]

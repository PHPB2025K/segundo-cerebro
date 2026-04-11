---
name: spreadsheet-pricing
description: Preenchimento da planilha de precificacao e estoque no Google Drive. Mapeia campos INPUT vs FORMULA por aba (MELI, SHOPEE, AMAZON, ESTOQUE). Nunca toca em formulas. Aceita precos diferentes por marketplace.
triggers:
  - "adicionar produto na planilha"
  - "cadastrar sku na planilha"
  - "preencher planilha de estoque"
  - "planilha de precificacao"
  - "inserir na planilha"
metadata:
  openclaw:
    emoji: "\U0001F4CA"
    last_updated: "2026-04-08"
    spreadsheet_id: "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI"
    spreadsheet_name: "PLANILHA DE ESTOQUE"
---

# Skill: Spreadsheet Pricing — Budamix

> Preenche a planilha de precificacao e estoque no Google Drive.
> So toca colunas INPUT — NUNCA sobrescreve formulas.
> Aceita precos diferentes por marketplace.

---

## 1. ACESSO

| Parametro | Valor |
|-----------|-------|
| Spreadsheet ID | `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI` |
| Nome | PLANILHA DE ESTOQUE |
| Ferramenta | `gog sheets` (CLI) |
| Account | `pehpbroglio@gmail.com` |
| Env vars | `GOG_KEYRING_PASSWORD` + `GOG_ACCOUNT` (do systemd override) |

**Comando base:**
```bash
export GOG_KEYRING_PASSWORD=$(cat /proc/$(pgrep -f "openclaw$" | head -1)/environ | tr "\0" "\n" | grep GOG_KEYRING_PASSWORD | cut -d= -f2-)
export GOG_ACCOUNT=pehpbroglio@gmail.com
SSID="1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI"
```

---

## 2. ESTRUTURA DAS ABAS

| Aba | Headers row | Dados a partir de | Colunas |
|-----|-------------|-------------------|---------|
| MELI | 6 | 7 | A-AA |
| SHOPEE | 6 | 7 | A-Z |
| AMAZON | 6 | 7 | A-V |
| ESTOQUE | 8 | 9 | A-K |

---

## 3. FLUXO DE INSERÇÃO

### Fase 1 — Receber dados do produto
Dados obrigatorios:
- SKU, nome resumido, custo unitario
- Preco por marketplace (ML, Shopee, Amazon — podem ser diferentes)
- Tipo anuncio ML ("Classico" ou "Premium")
- Estoque, EAN, NCM, marca, peso
- Caixa (R$), embalagem (R$), Full (R$ — opcional)

### Fase 2 — SEMPRE inserir na aba ESTOQUE primeiro
A aba ESTOQUE e a fonte de verdade. As abas de marketplace puxam NCM, PESO e MARCA via VLOOKUP a partir do ESTOQUE (por EAN ou SKU). Se ESTOQUE nao tiver o produto, as formulas dos marketplaces vao retornar erro.

### Fase 3 — Localizar ultima linha com dados
```bash
gog sheets get "$SSID" "{ABA}!D6:D200" --plain | grep -n "." | tail -1
```
A nova linha = ultima linha com dados + 1.

### Fase 4 — Verificar se a nova row tem formulas
Ler a row de destino. Se estiver vazia, as formulas precisam ser copiadas da row anterior.

**Metodo:** Ler as colunas de FORMULA da row anterior e copiar para a nova row.

### Fase 5 — Escrever APENAS colunas INPUT
Usar `gog sheets update` celula por celula para cada campo INPUT.

### Fase 6 — Validar
Ler a row completa de volta e confirmar:
- Campos INPUT tem os valores corretos
- Campos FORMULA calcularam (nao estao vazios ou com erro)
- STATUS (col C) mostra valor correto baseado no estoque

---

## 4. MAPEAMENTO DE COLUNAS

### Regra absoluta
**Colunas marcadas FORMULA = NUNCA TOCAR.**
Se o skill escrever numa coluna de formula, vai sobrescrever o calculo e quebrar a planilha.

### Mapeamento detalhado
Ver arquivos em `maps/`:
- `maps/meli-columns.md`
- `maps/shopee-columns.md`
- `maps/amazon-columns.md`
- `maps/estoque-columns.md`

### Resumo rapido

**INPUT por aba:**
| Aba | Colunas INPUT |
|-----|---------------|
| ESTOQUE | A, C, E, F, G, H, I |
| MELI | A, B, D, E, F, G, H, M, N, P, X |
| SHOPEE | A, D, E, F, G, I, L, O, P, Q, W |
| AMAZON | D, E, F, G, I, K, L, M, S |

**FORMULA por aba (NUNCA TOCAR):**
| Aba | Colunas FORMULA |
|-----|-----------------|
| ESTOQUE | D, J, K |
| MELI | C, I, J, K, L, O, Q, R, S, T, U, V, W, Y, Z, AA |
| SHOPEE | B, C, H, J, K, M, N, R, X, Y, Z |
| AMAZON | C, H, J, N, O, Q, R, T, U, V |

---

## 5. CASCATA DE VLOOKUP

As abas MELI e SHOPEE puxam NCM, PESO e MARCA via VLOOKUP pelo **EAN** na aba ESTOQUE.
A aba AMAZON puxa NCM, PESO e MARCA via VLOOKUP pelo **SKU** na aba ESTOQUE.

**Consequencia:** Ao cadastrar produto novo, preencher ESTOQUE primeiro. Se o EAN estiver preenchido no ESTOQUE, os VLOOKUPs das abas de marketplace vao funcionar automaticamente.

Se o produto NAO tem EAN: os VLOOKUPs de MELI e SHOPEE vao retornar erro. Nesse caso, pode ser necessario preencher manualmente ou ajustar a formula.

---

## 6. REGRAS DE FORMATO

### Numeros
- Separador decimal no `gog sheets update`: usar PONTO (1.04, 19.90)
- O Google Sheets BR converte automaticamente para virgula na exibicao
- NUNCA enviar "R$" como texto — enviar so o numero (1.04, nao "R$ 1,04")
- O Sheets aplica formatacao de moeda da coluna automaticamente

### Texto
- Nomes de produtos: resumidos, sem caracteres especiais
- SKU: maiusculas, padrao Budamix (PCM001, XCP001, SPC001)
- Tipo anuncio ML: exatamente "Classico" ou "Premium" (sem acento funciona tambem)

### EAN
- Enviar como texto (string), nunca como numero (para preservar zeros a esquerda)
- Se nao tem EAN: deixar celula vazia

---

## 7. TRATAMENTO DE FORMULAS NA NOVA ROW

### Cenario 1: Nova row ja tem formulas (row existia antes, so sem dados)
Nesse caso: so preencher os campos INPUT. As formulas ja estao la.

### Cenario 2: Nova row esta completamente vazia
Nesse caso: ANTES de preencher INPUT, copiar as formulas da row anterior.

**Colunas que precisam de formula copiada:**

MELI: C, I, J, K, L, O, Q, R, S, T, U, V, W, Y, Z, AA
SHOPEE: B, C, H, J, K, M, N, R, S, T, U, V, X, Y, Z
AMAZON: C, H, J, N, O, Q, R, T, U, V

**Como copiar formulas via gog:**
Nao e possivel copiar formulas diretamente via `gog sheets`. Alternativas:
1. Usar Google Sheets API diretamente (copyPaste request via batchUpdate)
2. Escrever as formulas como texto (ex: `=G59*0.28`) via update
3. Pedir ao Pedro para inserir uma linha manualmente no Sheets (copy-paste da row anterior) e o skill so preenche os INPUT

**Recomendacao:** Opcao 3 e a mais segura. Ou: inserir as formulas conhecidas (documentadas nos maps/) via update como texto prefixado com `=`.

---

## 8. ORDEM DE PREENCHIMENTO

**SEMPRE nesta ordem:**
1. ESTOQUE (fonte de verdade — VLOOKUPs dependem dele)
2. MELI
3. SHOPEE
4. AMAZON

---

## 9. DADOS NECESSARIOS DO PEDRO

Para inserir um novo SKU, o Pedro precisa fornecer:

| Dado | Obrigatorio | Usado em |
|------|-------------|----------|
| SKU | SIM | Todas as abas |
| Nome resumido | SIM | Todas as abas |
| Custo unitario (R$) | SIM | Todas as abas |
| Preco ML (R$) | SIM se vende no ML | MELI col G |
| Preco Shopee (R$) | SIM se vende na Shopee | SHOPEE col G |
| Preco Amazon (R$) | SIM se vende na Amazon | AMAZON col G |
| Tipo anuncio ML | SIM | MELI col H |
| Estoque | SIM | ESTOQUE col A, marketplaces col A |
| EAN | OPCIONAL | ESTOQUE col G, marketplaces (VLOOKUP) |
| NCM | SIM | ESTOQUE col H |
| Marca | SIM | ESTOQUE col I |
| Peso | RECOMENDADO | ESTOQUE (VLOOKUP) |
| Caixa (R$) | RECOMENDADO | MELI col M, SHOPEE col O, AMAZON col K |
| Embalagem (R$) | RECOMENDADO | MELI col P, SHOPEE col P, AMAZON col L |
| Full (R$) | OPCIONAL | MELI col N |
| Tarifa FBA (R$) | SIM para Amazon | AMAZON col I |
| Taxa transacao Shopee (R$) | SIM para Shopee | SHOPEE col I |
| Frete Shopee (R$) | SIM para Shopee | SHOPEE col L |
| Bilhete Shopee (R$) | OPCIONAL | SHOPEE col Q |
| SKU referencia ML | OPCIONAL | MELI col B |
| Frete Amazon (R$) | OPCIONAL | AMAZON col M |

---

## 10. LICOES APRENDIDAS

1. `gog sheets append` com planilhas que tem celulas mescladas no header pode inserir em colunas erradas. Preferir `gog sheets update` celula por celula.
2. Valores com "R$" no texto sao interpretados como string, nao numero. Enviar so o numero.
3. A virgula no `gog sheets` e separador de linha/celula, nao decimal. Usar ponto como decimal.
4. Colunas Y, Z, AA (NCM, PESO, MARCA) nas abas de marketplace sao VLOOKUP — NUNCA preencher manualmente.
5. Coluna Q (ADS) no MELI e FORMULA (=G*0.06), nao INPUT. Mesmo para coluna S (COMISSAO AFILIADO = G*0.1).
6. Coluna I (TAXA TRANSACAO) no SHOPEE e INPUT (valor fixo). Coluna L (FRETE) tambem e INPUT.
7. AMAZON col A (ESTOQUE) pode ser formula ou input — verificar antes de escrever.
8. Ao inserir nova row, verificar se formulas existem. Se nao, copiar da row anterior.

---

## Changelog

| Data | Mudanca |
|------|---------|
| 2026-04-08 | Criacao da skill com mapeamento corrigido pelo Pedro (16 correcoes vs mapeamento original) |
| 2026-04-08 | Documentacao de formulas reais por coluna em cada aba |
| 2026-04-08 | Regras de cascata VLOOKUP (ESTOQUE -> marketplaces) |

---

## Notas relacionadas

- [[skills/marketplace/amazon-fees-rules/SKILL|Taxas Amazon]]
- [[skills/marketplace/ml-fees-rules/SKILL|Taxas ML]]
- [[skills/marketplace/shopee-fees-rules/SKILL|Taxas Shopee]]

---
## Referências
- [[skills/spreadsheet-pricing/maps/amazon-columns|Mapa Amazon]]
- [[skills/spreadsheet-pricing/maps/estoque-columns|Mapa Estoque]]
- [[skills/spreadsheet-pricing/maps/meli-columns|Mapa MELI]]
- [[skills/spreadsheet-pricing/maps/shopee-columns|Mapa Shopee]]
- [[skills/spreadsheet-pricing/rules/format-rules|Regras de Formato]]
- [[skills/spreadsheet-pricing/rules/formula-protection|Proteção de Fórmulas]]

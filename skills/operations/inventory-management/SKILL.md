---
name: inventory-management
description: >
  Gestão de estoque — consulta, análise e controle de inventário via Planilha de Estoque no Google Drive.
  Use quando Pedro perguntar sobre estoque, quantidades, SKUs, EANs, custo, reposição ou qualquer dado
  de produto. Triggers: "estoque de", "quantos temos", "qual o SKU", "qual o EAN", "confere o estoque",
  "produto em falta", "preciso repor", "estoque mínimo", "valor de estoque".
---

# Gestão de Estoque — GB Importadora

## Descrição

Consulta e análise do inventário físico da GB Importadora via Planilha de Estoque no Google Drive. Fonte única e oficial de dados de estoque do armazém.

## Fonte de Dados

**Planilha:** PLANILHA DE ESTOQUE
**Google Sheets ID:** `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`
**Conta:** `gb.ai.agent@gbimportadora.com`

### Abas disponíveis

| Aba | Conteúdo | Linhas |
|---|---|---|
| **ESTOQUE** | Inventário do armazém físico (fonte principal) | 432 |
| RESUMO | Dashboard resumido | — |
| SHOPEE | Dados Shopee | 706 |
| MELI | Dados Mercado Livre | 600 |
| AMAZON | Dados Amazon | 611 |
| MIMO STYLE | Fornecedor Mimo Style | 1864 |
| SAÍDA | Registro de saídas | — |
| ENTRADA | Registro de entradas | — |

### Estrutura da aba ESTOQUE (linha 8 = header)

| Coluna | Campo | Exemplo |
|---|---|---|
| A | Quantidade em estoque | 3 |
| B | (vazio) | — |
| C | SKU | FYTR001-QPG002_T |
| D | Status estoque | ESTOQUE MÍNIMO / REPOR ESTOQUE |
| E | Descrição do produto | Pote Hermético Cilíndrico de Vidro... |
| F | Preço de custo | R$ 9,87 |
| G | EAN | 7898972482077 |
| H | NCM | 7013.42.90 |
| I | Marca | GB IMPORTADORA |
| J | Valor de estoque | R$ 29,61 |

**Dados começam na linha 9** (linha 8 é header).

## ⚠️ Limitação Conhecida

A planilha reflete APENAS o estoque do **armazém físico** em Pedreira-SP. **NÃO inclui:**
- Estoque na **Amazon FBA** (fulfillment Amazon)
- Estoque no **Mercado Livre Full** (fulfillment ML)
- Estoque na **Shopee** (fulfillment Shopee)

Quando Pedro perguntar sobre estoque total, SEMPRE avisar que o número é só do armazém e que pode haver estoque adicional nos fulfillments.

## Quando Usar

- Pedro perguntar "quantos X temos em estoque?"
- Verificar SKU ou EAN de um produto
- Conferir preço de custo
- Identificar produtos pra reposição (coluna D)
- Calcular valor total do inventário
- Cruzar dados de estoque com dados de vendas

## Inputs Necessários

| Input | Obrigatório | Descrição |
|---|---|---|
| Produto ou SKU | Sim | Nome, SKU parcial ou EAN pra buscar |
| Aba | Não | Default: ESTOQUE |

## Passo a Passo de Execução

```bash
# 1. Sempre usar conta gb.ai.agent
export GOG_KEYRING_PASSWORD=$(cat /root/.openclaw/.gog-keyring-pass)

# 2. Ler dados da planilha
gog sheets get "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI" "ESTOQUE!A9:J432" --json --account gb.ai.agent@gbimportadora.com

# 3. Parsear e filtrar por SKU/nome/EAN
# 4. Apresentar resultado formatado
# 5. SEMPRE avisar sobre limitação de fulfillments
```

## Composição dos 18 Kits de Potes Herméticos 4 Travas

### Quadrados (320ml / 520ml / 800ml)

| SKU Kit | Descrição | Composição | Potes Unitários (SKU) |
|---|---|---|---|
| KIT2YW320 | 2x 320ml quadrado | 2 potes 320ml | YW320SQ × 2 |
| KIT4YW320 | 4x 320ml quadrado | 4 potes 320ml | YW320SQ × 4 |
| KIT2YW520SQ | 2x 520ml quadrado | 2 potes 520ml | YW520SQ × 2 |
| KIT4YW520SQ | 4x 520ml quadrado | 4 potes 520ml | YW520SQ × 4 |
| KIT2YW800SQ | 2x 800ml quadrado | 2 potes 800ml | YW800SQ × 2 |
| KIT4YW800SQ | 4x 800ml quadrado | 4 potes 800ml | YW800SQ × 4 |
| 096 | 1x cada quadrado | 1×320 + 1×520 + 1×800 | YW320SQ + YW520SQ + YW800SQ |
| 097 | 2x cada quadrado | 2×320 + 2×520 + 2×800 | YW320SQ×2 + YW520SQ×2 + YW800SQ×2 |
| 098 | 3x cada quadrado | 3×320 + 3×520 + 3×800 | YW320SQ×3 + YW520SQ×3 + YW800SQ×3 |

### Retangulares (640ml / 1050ml / 1520ml)

| SKU Kit | Descrição | Composição | Potes Unitários (SKU) |
|---|---|---|---|
| KIT2YW640 | 2x 640ml retangular | 2 potes 640ml | YW640 × 2 |
| KIT4YW640 | 4x 640ml retangular | 4 potes 640ml | YW640 × 4 |
| KIT2YW1050 | 2x 1050ml retangular | 2 potes 1050ml | YW1050 × 2 |
| KIT4YW1050 | 4x 1050ml retangular | 4 potes 1050ml | YW1050 × 4 |
| KIT2YW1520 | 2x 1520ml retangular | 2 potes 1520ml | YW1520 × 2 |
| KIT4YW1520 | 4x 1520ml retangular | 4 potes 1520ml | YW1520 × 4 |
| 099 | 1x cada retangular | 1×640 + 1×1050 + 1×1520 | YW640 + YW1050 + YW1520 |
| 101 | 2x cada retangular | 2×640 + 2×1050 + 2×1520 | YW640×2 + YW1050×2 + YW1520×2 |
| 102 | 3x cada retangular | 3×640 + 3×1050 + 3×1520 | YW640×3 + YW1050×3 + YW1520×3 |

## Critérios de Qualidade

- SEMPRE consultar a planilha atualizada — nunca usar dados de cache ou memória
- SEMPRE informar que dados são do armazém físico apenas
- Se coluna D mostrar "REPOR ESTOQUE" ou "ESTOQUE MÍNIMO", alertar proativamente
- Apresentar valores monetários em R$ com 2 casas decimais
- Se cruzar com dados de vendas, indicar dias de estoque restante (estoque ÷ vendas diárias)

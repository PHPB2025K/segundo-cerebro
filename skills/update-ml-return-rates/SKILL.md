# Skill: update-ml-return-rates

Atualiza a coluna DEVOLUÇÕES (Col O) da aba MELI na planilha de estoque Budamix com taxas reais de devolução por SKU.

## Quem usa
- **Kobe** (agente principal)
- **Trader** (sub-agente marketplace)

## Quando usar
- Quando receber um arquivo xlsx/json com taxas de devolução reais dos anúncios MLB
- Periodicamente (sugestão: quinzenal) para manter a precificação atualizada
- Após mudanças significativas em logística ou embalagem que afetem devoluções

## Input
Um arquivo com os dados de devolução. Aceita dois formatos:

### Formato 1: xlsx (taxa_devolucao_MLB_perdas_reais.xlsx)
Estrutura esperada:
| Coluna | Campo |
|--------|-------|
| A | Código MLB |
| B | SKU |
| C | Descrição |
| D | Vendas |
| E | Devoluções Reais |
| F | Taxa Devolução (fórmula) |
| G | Faturamento |
| H | Perda Financeira |
| I | % Perda s/ Fat. |
| J | Principal Motivo |

### Formato 2: JSON
```json
{
  "SKU_AQUI": {"vendas": 100, "devolucoes": 10, "taxa": 10.0},
  ...
}
```

## Output
1. Coluna O da aba MELI atualizada com fórmula `=G{row}*{taxa}/1000` para cada SKU
2. SKUs sem dados no arquivo mantêm o default de 4%
3. Relatório no Telegram (Thread 3: Marketplaces) com:
   - Quantos SKUs atualizados com taxa real
   - Quantos mantidos em default
   - SKUs em PREJUÍZO (margem <0%)
   - SKUs em ALERTA (margem 0-5%)

## Execução
```bash
python3 ~/.openclaw/workspace/skills/update-ml-return-rates/update-return-rates.py <caminho_arquivo>
```

Exemplo:
```bash
python3 ~/.openclaw/workspace/skills/update-ml-return-rates/update-return-rates.py /tmp/taxa_devolucao_MLB_perdas_reais.xlsx
python3 ~/.openclaw/workspace/skills/update-ml-return-rates/update-return-rates.py /tmp/return-rates.json
```

## Planilha de referência

| Campo | Valor |
|-------|-------|
| SSID | `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI` |
| Aba | MELI |
| Headers | Row 6 |
| Dados | Rows 7+ (dinâmico, itera até SKU vazio) |
| Col D | SKU ANUNCIO (chave de match) |
| Col G | PREÇO DE VENDA |
| Col O | DEVOLUÇÕES (target) |
| Col T | MARGEM (recalcula automaticamente) |
| Col U | LUCRO LIQ (recalcula automaticamente) |

### Fórmulas dependentes (NÃO TOCAR)
- Col T (MARGEM): `=(U*100)/G/100`
- Col U (LUCRO LIQ): `=G-F-J-K-L-M-P-R-Q-O-N`
- Col W (MARGEM AFILIADO): `=(W*100)/G/100` — usa mesma Col O

### Regra de locale
Google Sheets PT-BR usa `,` como decimal. Para evitar problemas:
- Nunca usar ponto decimal em fórmulas
- Para taxas fracionárias (ex: 8.5%): `=G*85/1000` (não `=G*0.085`)
- Para taxas inteiras (ex: 10%): `=G*10%`
- Para 0%: valor literal `0`

## Match de SKUs — mapeamento conhecido

Alguns SKUs no xlsx usam sufixos ou nomes diferentes do SKU na planilha:

| SKU no xlsx | SKU na planilha | Nota |
|-------------|----------------|------|
| IMB501PT | IMB501P_T | Sufixo _T |
| IMB501CT | IMB501C_T | Sufixo _T |
| KIT2YW1520AZ | KIT2YW1520 | Variante cor |
| KIT4YW1520AZ | KIT4YW1520 | Variante cor |
| KIT4YW800SQ_T | KIT4YW800SQ | Sufixo _T |
| 096 | KIT3S096 | Prefixo KIT3S |
| 097 | KIT6S097 | Prefixo KIT6S |
| 099 | KIT3S099 | Prefixo KIT3S |
| 102 | KIT9S098 | Código diferente |

O script resolve esses aliases automaticamente.

## Dependências
- Python 3 com `openpyxl` (para xlsx) ou `json` (para json)
- `gog` CLI com credenciais configuradas
- Variáveis de ambiente: `GOG_KEYRING_PASSWORD`, `GOG_ACCOUNT`

---

*Criada: 09/04/2026*
*Autor: Pedro (via Claude Code)*

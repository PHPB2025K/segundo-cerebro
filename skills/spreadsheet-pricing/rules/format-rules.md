# Regras de Formato — Spreadsheet Pricing

## Numeros

| Regra | Exemplo correto | Exemplo errado |
|-------|----------------|----------------|
| Decimal com ponto no gog | `1.04` | `1,04` |
| Sem prefixo R$ | `19.90` | `R$ 19,90` |
| Sem aspas em numeros | `19.90` | `"19.90"` |
| Inteiros sem decimal | `50` | `50.0` |
| Zero como numero | `0` | `` (vazio) |

O Google Sheets BR converte ponto para virgula na exibicao automaticamente.

## Texto

| Regra | Exemplo correto | Exemplo errado |
|-------|----------------|----------------|
| SKU em maiusculas | `PCM001` | `pcm001` |
| Titulo resumido | `Kit 6 Porta Copos MDF 6mm c/ Suporte` | `Kit 6 Porta-Copos de MDF 6mm com Suporte Organizador - Design Solaris` |
| Tipo anuncio ML | `Classico` ou `Premium` | `classico`, `CLASSICO`, `Clássico` |
| Marca | `BUDAMIX` ou `Budamix` | `budamix` |
| NCM com pontos | `4411.12.10` | `44111210` |

> ⚠️ **ATENCAO:** Amazon SP-API exige NCM SEM pontos (`44111210`). Ao copiar NCM da planilha para Amazon, remover os pontos. Ver [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]].

## EAN

| Regra | Motivo |
|-------|--------|
| Enviar como texto | Preservar zeros a esquerda |
| Se nao tem EAN | Deixar celula vazia (nao "N/A", nao "SEM") |

## Celulas vazias

| Quando | O que fazer |
|--------|------------|
| Campo opcional sem valor | Deixar vazio (nao escrever nada) |
| Campo obrigatorio sem dado | Pedir ao Pedro antes de inserir |
| Campo com formula | NUNCA escrever — a formula ja existe ou sera copiada |

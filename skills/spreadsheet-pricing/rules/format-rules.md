---
title: "format rules"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
  - pricing
---

# Regras de Formato — Spreadsheet Pricing

## Numeros — REGRA ABSOLUTA PEDRO 2026-05-27

Sempre que inserir ou atualizar qualquer valor na **PLANILHA DE ESTOQUE**, em qualquer aba, usar padrão brasileiro de moeda/número: `R$ 00,00`, com vírgula decimal.

| Regra | Exemplo correto | Exemplo proibido |
|-------|----------------|------------------|
| Moeda em padrão brasileiro | `R$ 6,75` | `6.75` |
| Decimal com vírgula | `R$ 6,21` | `6.21` |
| Centavos sempre com 2 casas | `R$ 5,00` | `5.0` ou `5.00` |
| Preço de venda/custo/frete/taxa | `R$ 66,90` | `66.90` |
| Inteiro monetário | `R$ 50,00` | `50` quando o campo for valor financeiro |

Nunca usar ponto (`.`) como separador decimal em valores enviados para a planilha. Se uma ferramenta/API exigir formato técnico diferente, fazer teste isolado e validar visualmente/diretamente no Sheets antes de considerar a atualização concluída.

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

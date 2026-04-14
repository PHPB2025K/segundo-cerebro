---
title: "validation rules"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
  - amazon
---

# Regras de Validacao — Amazon Listing Creator

> Verificar ANTES de submeter. Se qualquer regra falhar, corrigir primeiro.

## 1. Titulo
| Regra | Validacao |
|-------|-----------|
| Max 200 chars | len(title) <= 200 |
| Contem "Budamix" | "Budamix" in title |
| Sem ALL CAPS total | Nao todo uppercase |
| Sem preco | Sem "R$", "reais" |
| Sem promocao | Sem "gratis", "desconto", "melhor" |
| Keywords nos primeiros 80 chars | Produto + material + spec |

## 2. Bullet Points
| Regra | Validacao |
|-------|-----------|
| Exatamente 5 | len(bullets) == 5 |
| Cada um <= 500 chars | Todos dentro do limite |
| Primeira palavra CAPS | Keyword principal destacada |
| Sem HTML | Texto puro |
| Sem precos | Sem "R$" |

## 3. Backend Keywords
| Regra | Validacao |
|-------|-----------|
| Max 250 bytes | len(keywords.encode()) <= 250 |
| Sem repetir titulo | Palavras complementares |
| Sem marca propria | Nao repetir "Budamix" |
| Sem ASINs | Sem codigos de concorrentes |

## 4. Imagens
| Regra | Validacao |
|-------|-----------|
| Min 7 fotos | len(images) >= 7 |
| Foto 1: fundo branco | Verificacao visual |
| Foto 1: 85%+ frame | Produto centralizado |
| Foto 1: sem texto | Sem overlays |
| Todas >= 1000px | Lado maior >= 1000 |
| Formato JPEG/PNG | Extensao correta |

## 5. Preco
| Regra | Validacao |
|-------|-----------|
| > R$0 | price > 0 |
| Paridade cross-channel | Mesmo preco ML/Shopee (Amazon Buy Box!) |
| Margem positiva | preco - referral_fee - fba_fee - cmv > 0 |

## 6. Dimensoes
| Regra | Validacao |
|-------|-----------|
| item_dimensions preenchido | 3 valores (L/W/H) |
| item_length_width preenchido | 2 valores (L/W) — campo separado! |
| item_package_dimensions | 3 valores embalagem |
| item_package_weight | Peso em grams |
| Unidades corretas | "centimeters" e "grams" |

## 7. Campos Especiais
| Regra | Validacao |
|-------|-----------|
| unit_count.type e objeto | Nao string, tem value + language_tag |
| number_of_items e inteiro | Nao float |
| power_source_type preenchido | "does_not_require_power" para nao-eletronicos |
| GTIN ou exemption | Um dos dois, nunca ambos |
| browse_node valido | ID numerico como string |
| NCM sem pontos | "44111210" nao "4411.12.10" |

## 8. Calculo de Custos Amazon BR
```
Referral Fee = preco * 0.15 (Home & Kitchen)
FBA Fee = ~R$6 (item pequeno/leve)
Custo total Amazon = Referral + FBA
Receita = preco - custo_total
Lucro = receita - CMV
Margem = lucro / preco * 100
```

## 9. Buy Box
| Regra | Impacto |
|-------|---------|
| Preco <= outras plataformas | Amazon suprime Buy Box se preco maior |
| Estoque disponivel | Sem estoque = fora da Buy Box |
| FBA ativo | Vantagem sobre FBM |
| Metricas OK (ODR < 1%) | Elegibilidade automatica |

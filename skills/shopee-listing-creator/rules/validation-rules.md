# Regras de Validacao — Shopee Listing Creator

> Verificar ANTES de publicar. Se qualquer regra falhar, corrigir e re-validar.

## 1. Titulo

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Max 120 chars | `len(title) <= 120` | Encurtar removendo palavras menos relevantes do final |
| Contem "Budamix" | `"Budamix" in title` | Adicionar no inicio |
| Contem material | verificar manualmente | Adicionar apos nome do produto |
| Sem caracteres proibidos | Sem emojis, !!!, $$$, ALL CAPS total | Remover |
| Sem preco no titulo | Sem "R$", "reais", "desconto" | Remover |
| Sem URL no titulo | Sem "http", "www", ".com" | Remover |

## 2. Imagens

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| 9 fotos | `len(images) == 9` | Adicionar fotos faltantes |
| Todas 1:1 | `width == height` para cada imagem | Redimensionar/cropar |
| Todas < 2MB | `file_size < 2097152` | Comprimir: `sips -s format jpeg -s formatOptions 85` |
| Foto 1 lifestyle | verificacao visual: cenario real, produto em uso | NUNCA fundo branco na capa Shopee — trocar por lifestyle |
| Formato JPG/PNG | extensao .jpg ou .png | Converter |

## 3. Preco

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Nao e R$80,00 | `price != 80.00` | Ajustar para R$79,90 ou R$89,90+ |
| Nao e fronteira | `price not in [8.00, 100.00, 200.00]` | Ajustar -R$0,10 ou +R$10 |
| Margem positiva | `preco - custos_shopee - cmv > 0` | Aumentar preco ou reduzir CMV |
| Margem minima 30% | `margem >= 30` | Reavaliar preco ou canal |

### Calculo de custos por faixa

```
Se preco < 8:
  custo = preco * 0.50 + preco * 0.02
Se 8 <= preco < 80:
  custo = preco * 0.20 + 4.00 + preco * 0.02
Se 80 <= preco < 100:
  custo = preco * 0.14 + 16.00 + preco * 0.02
Se 100 <= preco < 200:
  custo = preco * 0.14 + 20.00 + preco * 0.02
Se 200 <= preco < 500:
  custo = preco * 0.14 + 26.00 + preco * 0.02
Se preco >= 500:
  custo = preco * 0.14 + 26.00 + preco * 0.02
```

## 4. Especificacoes

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Marca = Budamix | `brand == "Budamix"` | Corrigir |
| 100% preenchido | Nenhum attr vazio | Preencher com dados do produto |
| Valores reais | Nada generico tipo "N/A" | Preencher com valor correto |

## 5. Descricao

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Max 3.000 chars | `len(desc) <= 3000` | Encurtar secoes menos importantes |
| Min 500 chars | `len(desc) >= 500` | Expandir com mais detalhes |
| Objetivo 500-800 chars | `500 <= len(desc) <= 800` | Sussinto e focado em conversao |
| Sem HTML | Sem `<`, `>`, `&amp;` | Remover tags |
| Sem markdown | Sem `**`, `##`, `[]()` | Converter para texto puro |
| Usa → para secoes | Sem ◾ | Trocar ◾ por → |
| Usa ▪ para sub-itens | Apenas em specs | Manter |
| Contem dimensoes | verificar | Adicionar secao ESPECIFICACOES |
| Sem secoes redundantes | Nao repetir info | Condensar em menos blocos |

## 6. Tags

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Min 15 tags | `len(tags) >= 15` | Gerar mais sinonimos/keywords |
| Max 20 tags | `len(tags) <= 20` | Remover menos relevantes |
| Sem duplicatas | `len(set(tags)) == len(tags)` | Remover duplicatas |
| Relevantes | verificar manualmente | Substituir por keywords de busca |

## 7. Logistica

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Shopee Xpress ativo | logistic_id 91003 enabled | Habilitar no payload |
| Peso preenchido | `weight > 0` | Preencher em kg |
| Dimensoes preenchidas | L, W, H > 0 | Preencher em cm |

## 8. Pos-publicacao

| Regra | Validacao | Acao se falhar |
|-------|-----------|----------------|
| Diagnostico verde | Score "Qualificado" | Identificar e corrigir campos faltantes |
| Item ativo | status = NORMAL | Verificar se nao foi barrado por moderacao |
| Supabase registrado | Item existe na tabela products | Inserir via upsert |
| Sync captura | Rodar sync-shopee-prices.py manualmente | Verificar shop_id no script |

---
name: shopee-listing-creator
description: Criacao de anuncios na Shopee com 100% dos campos preenchidos. Garante diagnostico "Qualificado" desde o primeiro cadastro. Aplica regras de precificacao, validacao de imagens, template de descricao e preenchimento completo de especificacoes.
triggers:
  - "criar anuncio shopee"
  - "publicar na shopee"
  - "cadastrar produto shopee"
  - "listing shopee"
  - "novo anuncio shopee"
metadata:
  openclaw:
    emoji: "\U0001F6CD\uFE0F"
    last_updated: "2026-04-07"
    sources:
      - "Shopee Open API v2 documentation"
      - "skill shopee-fees-rules"
      - "skill shopee-ranking (marketplace-optimization)"
    related_skills:
      - shopee-fees-rules
      - shopee-extrato
      - marketplace-optimization
---

# Skill: Shopee Listing Creator — Budamix

> Cria anuncios na Shopee com 100% das especificacoes preenchidas.
> Objetivo: diagnostico "Qualificado" (barra verde) desde o primeiro cadastro.
> Nunca publicar anuncio incompleto — Shopee penaliza no ranking.

---

## 1. CHECKLIST OBRIGATORIO (NUNCA publicar sem)

Antes de chamar `POST /api/v2/product/add_item`, TODOS os itens abaixo devem estar preenchidos:

| Campo | Regra | Exemplo |
|-------|-------|---------|
| Titulo | Ate 120 chars. Formato: [Marca] + [Produto] + [Material] + [Specs] + [Quantidade] | Budamix Kit 6 Porta Copos MDF 6mm Com Suporte Corte Laser Design Solaris |
| Categoria | Buscar via `get_category`, usar a mais especifica (leaf node). Validar com item existente se possivel | 101247 (Placemats & Coasters) |
| Marca | SEMPRE "Budamix". NUNCA "Sem marca" ou "No Brand" | Budamix |
| Especificacoes | Obter via `get_attributes` (ou teste iterativo se API suspensa). Preencher 100% | Ver secao 3 |
| Descricao | Ate 3.000 chars. Usar template padrao (secao 5). Sem HTML/markdown | Ver template |
| Fotos | 9 fotos em 1200x1200px JPG/PNG, TODAS abaixo de 2MB. Foto 1: fundo limpo | Comprimir com `sips -s format jpeg -s formatOptions 85` |
| Tags | 20 slots. Minimo 15 preenchidas com keywords relevantes | porta copos mdf, kit porta copos, descanso de copo... |
| Preco | Verificar faixa Shopee. NUNCA R$80,00 (ver secao 4) | R$39,90 |
| Estoque | Quantidade real disponivel | 50 |
| SKU | Codigo interno Budamix | PCM001 |
| Frete | Shopee Xpress (91003) habilitado. Retirada (90024) opcional | logistic_info com enabled=True |
| Garantia | Tipo + duracao. Padrao: "Garantia do vendedor - 90 dias" | attr 100131 |
| Peso | Em kg (campo weight) | 0.194 |
| Dimensoes | package_length, package_width, package_height em cm | 25x16x5 |

---

## 2. LOJAS SHOPEE BUDAMIX

Ordem de publicacao (sempre nesta sequencia):

| # | Nome | Shop ID | Token File | Prioridade |
|---|------|---------|------------|------------|
| 1 | budamix.store | 448649947 | .shopee-tokens-budamix-store.json | Principal |
| 2 | budamix-store2 | 860803675 | .shopee-tokens-budamix-store2.json | Budamix Oficial |
| 3 | budamix-shop | 442066454 | .shopee-tokens-budamix-shop.json | Budamix Shop |

**Marca Budamix:** `brand_id = 5014011`. Usar SEMPRE no payload:
```json
"brand": {"brand_id": 5014011, "original_brand_name": "Budamix"}
```
NUNCA usar `brand_id: 0` (fica como "NoBrand").

Tokens OAuth em: `/root/.openclaw/workspace/integrations/shopee/`
OAuth auto-refresh a cada 3h30 via `shopee_oauth.py`

---

## 3. ATRIBUTOS POR CATEGORIA

### Como obter atributos

**Metodo 1 (preferido):** API `GET /api/v2/product/get_attributes?category_id={id}&language=pt`
- Retorna lista completa com `is_mandatory`, `input_type`, `attribute_value_list`
- Se retornar 403 (api_suspended): usar Metodo 2

**Metodo 2 (fallback):** Teste iterativo
- Enviar `update_item` com um atributo de cada vez
- Se retornar "not mapped with the category" = atributo invalido
- Se aceitar ou retornar erro de valor = atributo valido
- Rate limit: 0.3s entre tentativas

### Atributos conhecidos por categoria

**101247 — Placemats & Coasters (Porta-Copos)**
| Attr ID | Nome | Tipo | Exemplo Budamix |
|---------|------|------|-----------------|
| 100130 | Features | Multi-value | Corte a Laser, Acabamento Carbonizado, Suporte Incluso |
| 100131 | Warranty Type | Single | Garantia do Vendedor - 90 dias |
| 100134 | Material | Single | MDF 6mm Alta Densidade |
| 100162 | Pattern | Single | Design Solaris - Gravacao Radial a Laser |
| 100169 | Style | Single | Modern |
| 100942 | Dimensions | Single | Porta-copos: 8cm diametro x 6mm / Suporte: 10cm x 8cm |
| 100999 | Pieces | Single | 7 |

**101220 — Food Storage (Potes)**
| Attr ID | Nome | Exemplo |
|---------|------|---------|
| 100037 | Country of Origin | Brasil |
| 100134 | Material | Silicone, Plastic, Glass |
| 100942 | Dimensions | 14x14x7 / 16x16x7 |
| 100999 | Pieces | 11 |
| 100130 | Features | Armazenamento, BPA Free, Hermetic |
| 100162 | Pattern | Nenhum |
| 100169 | Style | Modern |
| 100278 | Volume Capacity | 1520, 520, 800 |
| 100761 | Food Type | Alimentos |
| 100794 | Food Feature | Air Tight, Dishwasher Safe, Freezer Safe |

**101239 — Canecas / Cups**
(Mapear quando criar primeiro anuncio nesta categoria)

> Quando entrar em categoria nova: SEMPRE rodar teste iterativo e registrar os attr IDs aqui.

---

## 4. REGRAS DE PRECIFICACAO SHOPEE

### Tabela de comissoes (CNPJ, abril 2026)

| Faixa | Preco | Comissao | Taxa Fixa | Transacao |
|-------|-------|----------|-----------|-----------|
| 1 | R$0-7,99 | 50% | 50% preco | ~2% |
| **2** | **R$8-79,99** | **20%** | **R$4,00** | **~2%** |
| 3 | R$80-99,99 | 14% | R$16,00 | ~2% |
| 4 | R$100-199,99 | 14% | R$20,00 | ~2% |
| 5 | R$200-499,99 | 14% | R$26,00 | ~2% |
| 6 | R$500+ | 14% | R$26,00 | ~2% |

### ALERTAS DE PRECIFICACAO

- **NUNCA R$80,00** — taxa fixa salta de R$4 para R$16 (+R$12!)
- **Faixas seguras:** ate R$79,90 OU a partir de R$100
- **Fronteiras perigosas:** R$7,99/R$8, R$79,99/R$80, R$99,99/R$100, R$199,99/R$200

### Formula de margem
```
Receita = Preco - (Preco * Comissao%) - Taxa_Fixa - (Preco * 0.02)
Lucro = Receita - CMV
Margem = Lucro / Preco * 100
```

### Comparacao rapida Shopee vs ML (a R$39,90)
| | Shopee | ML (gold_special) |
|---|---|---|
| Custos totais | R$12,78 (32%) | R$11,45 (28,7%) |
| Frete vendedor | R$0 (subsidiado) | R$6,85 |
| Receita liquida real | R$27,12 | R$21,60 |
| **Shopee e melhor por** | | **+R$5,52/venda** |

---

## 5. TEMPLATE DE DESCRICAO BUDAMIX

Limite: 3.000 chars. Objetivo: ~1.200-1.500 chars (ninguem le mais).
Formato: texto puro, sem HTML/markdown. Usar ◾ e ▪ para estrutura.

```
[Nome do Produto] | Budamix
[Linha/Design] - [Conceito em 1 frase]

[Frase de abertura - 1 linha, beneficio principal]

◾ O QUE VEM NO KIT
  ▪ [item 1 com spec]
  ▪ [item 2 com spec]
  ▪ Total: [N] pecas

◾ DIFERENCIAIS
  ▪ [diferencial 1]
  ▪ [diferencial 2]
  ▪ [diferencial 3]

◾ FABRICACAO
  ▪ [metodo de fabricacao]
  ▪ [acabamento]
  ▪ Fabricacao propria em Pedreira-SP
  ▪ Controle de qualidade individual

◾ IDEAL PARA
  ▪ [uso 1]
  ▪ [uso 2]
  ▪ [uso 3]
  ▪ Presente funcional e decorativo

◾ DIMENSOES
  ▪ [dimensao produto principal]
  ▪ [dimensao acessorio]
  ▪ Peso: [peso]g

◾ GARANTIA
  ▪ 90 dias contra defeito de fabricacao

◾ BUDAMIX
Marca brasileira de Pedreira-SP especializada em utilidades domesticas de design com tecnologia de corte a laser.
```

---

## 6. REGRAS DE IMAGEM

| Regra | Valor |
|-------|-------|
| Resolucao recomendada | 1200 x 1200 px |
| Resolucao minima | 500 x 500 px |
| Proporcao | 1:1 (obrigatoria) |
| Formatos | JPG, PNG |
| Tamanho maximo | **2.0 MB** |
| Quantidade | **9 imagens** (usar todas) |
| Foto 1 (capa) | Fundo limpo, produto centralizado, sem texto |
| Video | 1 por listing, 10-60s, max 30MB, MP4 |

### Compressao automatica (quando > 2MB)
```bash
sips -s format jpeg -s formatOptions 85 input.png --out output.jpg
```
Verificar pos-compressao: `stat -f%z output.jpg` deve ser < 2097152 bytes.

### Ordem das fotos (padrao Budamix)
1. Hero shot (fundo limpo)
2. Lifestyle (produto em uso)
3. Dimensoes/escala
4. Design/conceito
5. Infografico features
6. Cenario aspiracional
7. Produto em contexto
8. Comparativo/beneficio
9. Flat lay (kit completo)

---

## 7. FLUXO DE CRIACAO (passo a passo)

### Fase 1 — Receber dados
- Nome do produto, material, dimensoes, peso
- Preco alvo, quantidade em estoque
- SKU interno, fotos (paths)
- CMV para calculo de margem

### Fase 2 — Descobrir categoria
```
GET /api/v2/product/get_category?language=pt
```
- Navegar ate leaf node mais especifica
- Se tiver item existente similar, usar mesma categoria
- Registrar categoria nova na secao 3 deste SKILL.md

### Fase 3 — Obter e preencher atributos
```
GET /api/v2/product/get_attributes?category_id={id}&language=pt
```
- Se 403: usar teste iterativo (Metodo 2)
- Preencher 100% dos atributos validos
- NUNCA deixar "Selecione" ou vazio

### Fase 4 — Formatar descricao
- Usar template da secao 5
- Maximo 3.000 chars, objetivo ~1.500
- Sem HTML, sem markdown, sem acentos problematicos
- Usar ◾ e ▪ para estrutura visual

### Fase 5 — Gerar 20 tags
- Extrair do titulo: marca, produto, material, specs
- Adicionar sinonimos: porta copos = descanso de copo = bolacha
- Adicionar keywords de busca: "decoracao mesa", "organizador", "presente"
- Minimo 15, ideal 20

### Fase 6 — Validar
Checar TODOS os itens do checklist (secao 1) antes de publicar.
Se qualquer item falhar, corrigir ANTES de prosseguir.

### Fase 7 — Comprimir fotos e upload
```bash
# Comprimir se necessario
sips -s format jpeg -s formatOptions 85 input.png --out output.jpg

# Upload via API
POST /api/v2/media_space/upload_image
```
- Enviar as 9 fotos na ordem correta
- Guardar os image_ids retornados

### Fase 8 — Criar item
```
POST /api/v2/product/add_item
```
Payload deve conter:
- item_name, description, category_id
- original_price, normal_stock
- image.image_id_list (9 IDs na ordem)
- weight, dimension
- condition: "NEW"
- item_sku
- brand: {brand_id: 0, original_brand_name: "Budamix"}
- attribute_list (100% preenchido)
- logistic_info: [{logistic_id: 91003, enabled: true}] (Shopee Xpress)
- seller_stock: [{stock: N}]

### Fase 9 — Verificar diagnostico
- Acessar Seller Center ou via API
- Score deve ser "Qualificado" (barra verde)
- Se nao: identificar campos faltantes e atualizar via `update_item`

### Fase 10 — Registrar e confirmar sync
- Registrar no Supabase (tabela products) com platform=shopee
- Confirmar que sync-shopee-prices.py captura o novo item
- Notificar Pedro no Telegram (Thread 3: Marketplaces)

---

## 8. INTEGRACAO COM STACK

| Componente | Path | Funcao |
|------------|------|--------|
| Tokens OAuth | /root/.openclaw/workspace/integrations/shopee/ | 3 lojas, auto-refresh |
| sync-shopee-prices.py | /root/.openclaw/workspace/scripts/ | Sync precos -> Supabase |
| sync-shopee-orders.py | /root/.openclaw/workspace/scripts/ | Sync pedidos -> Supabase |
| sync-inventory-shopee.py | /root/.openclaw/workspace/scripts/ | Sync estoque -> Supabase |
| shopee-fees-rules | /root/.openclaw/workspace/skills/marketplace/ | Regras de taxas |
| shopee-ranking | /root/.openclaw/workspace/skills/marketplace/marketplace-optimization/references/ | Fatores de ranking |
| Supabase | sqbkoprcmnznmzbwdrmf.supabase.co | Budamix Central |

---

## 9. ERROS COMUNS E SOLUCOES

| Erro | Causa | Solucao |
|------|-------|---------|
| error_invalid_logistic_info | Falta logistic_info no payload | Adicionar [{logistic_id: 91003, enabled: true}] |
| attribute not mapped | Attr ID invalido para a categoria | Remover e usar teste iterativo para encontrar IDs validos |
| api_suspended (get_attributes) | App sem permissao para este endpoint | Usar teste iterativo (Metodo 2) |
| image > 2MB | Foto muito grande | Comprimir: sips -s format jpeg -s formatOptions 85 |
| family_name required (ML) | ML exige family_name em vez de title | Trocar title por family_name no payload |

---

## Changelog

| Data | Mudanca |
|------|---------|
| 2026-04-07 | Criacao da skill com dados reais da primeira publicacao (Kit Porta-Copos PCM001) |
| 2026-04-07 | Mapeamento de atributos validos para categoria 101247 via teste iterativo |
| 2026-04-07 | Regras de precificacao importadas da skill shopee-fees-rules |

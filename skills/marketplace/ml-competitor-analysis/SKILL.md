---
name: ml-competitor-analysis
description: Análise de concorrência no Mercado Livre para qualquer produto. Coleta dados via Bright Data Web Unlocker, classifica concorrentes (idêntico/similar/diferente), gera relatório com pricing e recomendações.
triggers:
  - "analisa concorrência no ML"
  - "preço dos concorrentes"
  - "como tá o mercado de"
  - "análise competitiva ML"
  - "concorrentes no mercado livre"
  - "monitora concorrência"
metadata:
  openclaw:
    emoji: 🔍
    requires:
      tools: [exec, web_search, image]
      secrets:
        - name: Bright Data Web Unlocker
          vault: OpenClaw
          fields: [api_key]
        - name: Mercado Livre API - Openclaw.agent
          vault: OpenClaw
          fields: [username, password]
---

# Análise de Concorrência — Mercado Livre

## Objetivo

Protocolo completo e reutilizável para análise de concorrência no ML. Funciona para **qualquer produto**. Coleta dados reais via Bright Data Web Unlocker + ML API, classifica concorrentes por similaridade visual e gera relatório acionável.

---

## FASE 0 — Inputs Obrigatórios

Antes de iniciar, coletar do Pedro (ou inferir do contexto):

| Input | Obrigatório | Fonte |
|---|---|---|
| **Nome do produto** | ✅ | Pedro informa |
| **SKU/MLB ID de referência** | ✅ | Pedro informa ou buscar no seller_id 532562281 |
| **Preço atual** | ✅ | ML API (`/items/{id}`) |
| **Link do anúncio** | ✅ | Pedro fornece ao pedir a análise → extrair MLB ID → puxar fotos via API |
| **Categoria de kit** | ✅ | Kit 2, kit 4, unitário, etc. |
| **Diferenciais do nosso produto** | Desejável | Material, marca, travas, cor, etc. |

### Referência visual

O Pedro sempre fornece o **link do anúncio** ao pedir a análise. A partir disso:

1. Extrair MLB ID do link
2. Puxar fotos via ML API (`GET /items/{id}` → campo `pictures`)
3. Usar as 3 primeiras fotos como referência visual para classificação
4. **Não precisa pedir confirmação** — o Pedro já enviou o link correto
5. Se o token ML expirou, refreshar antes (ver Fase 3.3)

Obs: Imagens de referência podem ser salvas em `reference-images/{produto}/` para contexto futuro, mas não é obrigatório. O link do anúncio é a fonte de verdade.

---

## FASE 1 — Geração de Termos de Busca

### Regra: mínimo 5 termos por análise

Gerar variações cobrindo como o comprador busca:

| Tipo | Exemplo (pote 1520ml kit 2) |
|---|---|
| **Exato** | `kit 2 potes vidro hermético 1520ml retangular` |
| **Genérico** | `pote vidro hermético 1520ml` (sem "kit 2") |
| **Popular** | `marmita vidro hermética 1520ml 2 unidades` |
| **Por marca concorrente** | `click glass pote 1520ml kit 2` |
| **Por uso** | `pote vidro geladeira marmita grande kit 2` |
| **Variação de volume** | `kit 2 potes vidro 1.5 litros hermético` |
| **Sem especificação técnica** | `kit 2 potes vidro grandes hermético` |

### Regras de geração

- Incluir termos COM e SEM especificação de quantidade (ex: "pote vidro 1520ml" vs "kit 4 potes vidro 1520ml")
- Incluir pelo menos 1 termo com nome de marca concorrente conhecida
- Incluir pelo menos 1 termo genérico que o comprador leigo usaria
- Não usar termos que retornem categorias completamente diferentes
- **Documentar TODOS os termos usados no relatório final**

---

## FASE 2 — Coleta de Dados via Bright Data

### Infraestrutura

- **Ferramenta:** Bright Data Web Unlocker API
- **Zone:** `web_unlocker1`
- **País:** `br` (IP residencial brasileiro obrigatório)
- **Credenciais:** 1Password vault "OpenClaw" → "Bright Data Web Unlocker" → campo `api_key`

### Protocolo de coleta

```
Para cada termo de busca:
  Para cada página (1 a 3, mínimo):
    1. Montar URL: https://lista.mercadolivre.com.br/{termo-urlizado}_Desde_{offset}_NoIndex_True
       - Página 1: sem offset
       - Página 2: _Desde_49
       - Página 3: _Desde_97
    2. Fazer request via Bright Data:
       POST https://api.brightdata.com/request
       Body: {"zone": "web_unlocker1", "url": "<URL>", "format": "raw", "country": "br"}
    3. Parsear HTML: extrair title, price, free_shipping, fulfillment, sold_qty, link, MLB_ID, thumbnail
    4. Deduplicar por MLB_ID (mesmo anúncio pode aparecer em múltiplos termos)
```

### Paginação ML

| Página | Offset URL |
|---|---|
| 1 | (sem offset) |
| 2 | `_Desde_49` |
| 3 | `_Desde_97` |
| 4 | `_Desde_145` |
| 5 | `_Desde_193` |

### Rate limiting

- **Máximo 2 requests por segundo** ao Bright Data
- Inserir `sleep 1` entre requests
- Se receber 429: esperar 5s e retry (max 3 tentativas)
- **Custo estimado:** ~$0.01-0.03 por request. Análise completa (5 termos × 3 páginas) ≈ $0.15-0.45

### Parsing HTML

Usar o script `scripts/parse_ml_search.py` (referência). Campos a extrair por resultado:

```python
{
    "mlb_id": "MLB1234567890",
    "title": "...",
    "price": 78.90,
    "original_price": 99.90,      # se tiver desconto (preço riscado)
    "free_shipping": True,         # selo "Frete Grátis" universal na busca
    "fulfillment": False,          # FULL = fulfillment (frete grátis pra Meli+)
    "shipping_class": "universal", # derivado: "universal" | "meli_plus" | "none"
    "sold_quantity": "500+",       # texto como aparece
    "rating": 4.8,
    "reviews_count": 150,
    "thumbnail_url": "https://...",
    "permalink": "https://...",
    "position": 3,                 # posição na página
    "search_term": "...",          # termo que retornou este resultado
    "page": 1
}

# Derivar shipping_class:
# if free_shipping: "universal"
# elif fulfillment: "meli_plus"
# else: "none"
```

---

## FASE 3 — Enriquecimento via ML API

Para os top 20 anúncios mais relevantes (após deduplicação):

### 3.1 Dados do catálogo

```
GET /products/search?status=active&site_id=MLB&q={termo}&limit=20
Authorization: Bearer {token}
```

- Mapear catalog_product_id de cada item
- Identificar buy_box_winner quando disponível

### 3.2 Dados do vendedor

```
GET /users/{seller_id}
```

Extrair:
- nickname
- seller_reputation.level_id (1_red → 5_green)
- seller_reputation.power_seller_status
- seller_reputation.transactions.total
- seller_reputation.metrics (claims, cancellations, delayed)
- address.city, address.state

### 3.3 Token refresh

Se token expirou (401/403):

```bash
curl -X POST "https://api.mercadolibre.com/oauth/token" \
  -d "grant_type=refresh_token&client_id={app_id}&client_secret={secret}&refresh_token={refresh_token}"
```

Credenciais em 1Password → "Mercado Livre API - Openclaw.agent":
- client_id = campo `username`
- client_secret = campo `password`
- refresh_token = `/root/.openclaw/.ml-tokens.json`

---

## FASE 4 — Classificação Visual: Idêntico / Similar / Diferente

### Objetivo

Separar os resultados em 3 categorias baseado na análise visual do produto:

| Categoria | Definição | Peso na análise |
|---|---|---|
| **🟢 Idêntico** | Mesmo produto físico — mesma fábrica, mesmo formato, mesmas travas. Pode ter marca/cor/tampa diferentes. | Alto — concorrentes DIRETOS |
| **🟡 Similar** | Mesmo tipo de produto com variações relevantes (formato diferente, material diferente, com/sem divisória). | Médio — concorrentes indiretos |
| **🔴 Diferente** | Produto de outra categoria que apareceu na busca (tampa de bambu, plástico, tamanho muito diferente). | Baixo — ignorar na análise de pricing |

### Protocolo de classificação

1. Baixar thumbnails dos top 30-40 anúncios únicos
2. Usar `image` tool para analisar em batch comparando com as imagens de referência do nosso produto
3. Prompt de classificação:

```
Analise estas imagens de produtos do Mercado Livre. 
A imagem de REFERÊNCIA é o nosso produto: [descrição].
Para cada imagem numerada, classifique:
- IDÊNTICO: mesmo produto físico (mesma forma, travas, proporções), pode ter cor/marca diferente
- SIMILAR: mesmo tipo de produto mas com diferenças visíveis (formato, material, design)
- DIFERENTE: produto de outra categoria/tipo
Responda APENAS com o formato: [número]: [IDÊNTICO|SIMILAR|DIFERENTE]
```

4. Se a thumbnail não for suficiente, acessar a página do produto via Bright Data para fotos maiores
5. **Em caso de dúvida, classificar como SIMILAR (nunca como IDÊNTICO)**

### Nota sobre limitação

- A classificação visual depende da qualidade das thumbnails
- Fotos com fundo branco institucional são mais fáceis de comparar
- Fotos estilizadas (lifestyle) podem dificultar — nesse caso, analisar múltiplas fotos do anúncio

---

## FASE 4.5 — Dados Internos (OBRIGATÓRIO antes de recomendar)

### Objetivo

Antes de qualquer recomendação de pricing, OBRIGATORIAMENTE consultar os dados internos reais do produto.

### 4.5.1 Consultar Planilha do Drive

```bash
gog sheets get "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI" "MELI!A6:Z100" --json
```

Buscar o SKU do produto e extrair:
- Preço de custo
- Preço de venda atual
- Tipo de anúncio (Clássico/Premium)
- Comissão ML (valor real, não estimativa)
- Frete (valor real cobrado)
- Custo fixo
- Imposto
- Caixa
- Devoluções
- Embalagem
- Ads
- Frete cheio
- Comissão afiliado
- Margem atual
- Lucro líquido atual

### 4.5.2 Identificar kits do mesmo produto

Na planilha, procurar se existem kits (Kit 2, Kit 4, etc.) do mesmo produto. Comparar margens:
- Se o kit tem margem significativamente maior, considerar recomendar foco no kit

### 4.5.3 Consultar skill ml-fees-rules

Cruzar com `skills/marketplace/ml-fees-rules/SKILL.md` para:
- Validar se a comissão da planilha bate com a tabela oficial
- Verificar impacto de mudar tipo de anúncio (Clássico ↔ Premium)
- Calcular custo de frete em diferentes faixas de preço
- Simular cenários com dados reais

### 4.5.4 Simular cenários

Para cada recomendação, calcular com dados REAIS:

```
Cenário = {
    preço_venda,
    tipo_anúncio,       # Clássico ou Premium
    comissão,           # % da categoria × preço
    custo_frete,        # tabela ml-fees-rules (peso × preço)
    custo_fixo,         # se preço < R$79
    imposto,            # ~7% do preço
    ads,                # ~6% do preço (ou valor real)
    devoluções,         # ~4% do preço (ou valor real)
    embalagem,          # R$0,50
    caixa,              # R$0-1,20
    comissão_afiliado,  # 10% do preço (cenário com afiliado)
    armazenagem_full,   # se aplicável
}

lucro = preço_venda - custo_produto - comissão - frete - custo_fixo - imposto - ads - devoluções - embalagem - caixa - armazenagem
margem = lucro / preço_venda × 100
```

### Regras de recomendação

1. **NUNCA recomendar sem dados da planilha.** Se não conseguir acessar, informar que a recomendação é baseada em estimativas e pedir ao Pedro pra validar.

2. **Não defaultar "subir preço + frete grátis".** Isso pode ser ótimo ou péssimo — depende de quanto o frete pesa na margem. Sempre simular antes.

3. **Considerar kits como alternativa.** Se o kit tem margem melhor, pode ser a melhor recomendação em vez de mudar preço da unidade.

4. **Comparar Clássico vs Premium em R$.** A diferença não é só na comissão — o frete muda drasticamente entre faixas de preço.

5. **Mostrar sempre o cenário atual como baseline.** O Pedro precisa ver "quanto ganho hoje" vs "quanto ganharia no cenário proposto".

6. **Considerar cenário com afiliado.** Vendas via afiliados pagam ~10% extra. Margem de 13% vira 3% com afiliado — pode ser inviável.

7. **Volume importa.** Margem menor pode compensar se o volume crescer significativamente. Mas NUNCA assumir crescimento de volume sem evidência.

---

## FASE 5 — Análise e Relatório

### Estrutura do relatório

```markdown
# Análise de Concorrência ML — [Nome do Produto]
Data: [YYYY-MM-DD]
Referência: [MLB ID do nosso anúncio]
Nosso preço: R$XX,XX

## Metodologia
- Termos de busca usados: [lista completa]
- Páginas varridas por termo: X
- Total de resultados brutos: X
- Após deduplicação: X
- Classificação visual: X idênticos, X similares, X diferentes

## Concorrentes Diretos (Produto Idêntico)
| # | Vendedor | Preço | Frete | Full | Vendas | Rating | Reputação | Link |
|---|---|---|---|---|---|---|---|---|

## Concorrentes Indiretos (Produto Similar)
| # | Vendedor | Preço | Frete | Tipo de diferença | Link |
|---|---|---|---|---|---|

## Distribuição de Preço (Idênticos)
- Mínimo: R$XX
- Máximo: R$XX
- Mediana: R$XX
- Média: R$XX
[Histograma de faixas de preço]

## Distribuição de Frete
- Com frete grátis: XX%
- Sem frete grátis: XX%

## Nosso Posicionamento
- Nosso preço vs mediana: X% acima/abaixo
- Nosso preço vs mínimo: X% acima/abaixo
- Reputação vs concorrentes: [análise]
- Diferenciais: [o que nos diferencia]

## Dados Internos (Planilha GB)
[Tabela com dados reais do SKU extraídos da planilha]
- Preço de custo | Comissão | Frete | Imposto | Ads | Devoluções | Embalagem | Caixa | Margem | Lucro líquido
- Tipo de anúncio atual (Clássico/Premium)
- Dados de kits do mesmo produto (se existirem)

## Simulação de Cenários
[Cenários calculados com dados REAIS da planilha, não estimativas]
| Cenário | Preço | Tipo | Frete vendedor | Margem | Lucro | vs Atual |
- Sempre incluir cenário atual como baseline

## Recomendação de Pricing
- [Recomendação fundamentada com dados REAIS + contexto de mercado]
- [Justificativa baseada em margem real, não estimativa]

## Vieses e Limitações
- [Listar qualquer limitação da análise]
```

### Vieses a evitar (checklist)

- [ ] Analisou mais de 1 página por termo?
- [ ] Usou mais de 1 termo de busca?
- [ ] Separou idênticos de similares?
- [ ] Considerou frete no preço final percebido pelo comprador?
- [ ] Verificou se vendedores de baixa reputação distorcem a mediana?
- [ ] Identificou se há vendedores vendendo o MESMO produto com outra marca?
- [ ] Considerou sazonalidade?
- [ ] **Tratou corretamente a relação FULL vs Frete Grátis?** (ver regra abaixo)

### Regra: FULL ≠ Frete Grátis Universal

**NUNCA afirmar que um anúncio "não tem frete grátis" só porque `free_shipping: false` na API, se ele tem Fulfillment.**

A lógica correta é:

| Situação | O que acontece |
|---|---|
| `free_shipping: true` | Selo "Frete Grátis" aparece pra TODOS na busca |
| `free_shipping: false` + `fulfillment` | Frete grátis para **compradores Meli+**. Sem selo universal na busca. |
| `free_shipping: false` + sem fulfillment | Sem frete grátis. Comprador paga frete. |

**No relatório, classificar como:**
- `free_shipping: true` → "✅ Frete grátis (universal)"
- `free_shipping: false` + FULL → "⚠️ Frete grátis parcial (Meli+ apenas)"
- `free_shipping: false` + sem FULL → "❌ Sem frete grátis"

**Na análise de preço percebido:**
- Considerar que parcela relevante dos compradores ML tem Meli+ (~30-40% estimado)
- Não comparar diretamente "nosso preço + frete" vs "concorrente com frete grátis" sem ressalvar que parte dos nossos compradores também tem frete grátis via Meli+
- Quando o nosso anúncio tem FULL mas sem selo universal, apontar como desvantagem **parcial**, não absoluta

---

## FASE 6 — Persistência

### Salvar resultados

- Relatório completo: `cases/{produto}-{YYYY-MM-DD}.md`
- Dados brutos (JSON): `cases/{produto}-{YYYY-MM-DD}-raw.json`
- Imagens de referência: `reference-images/{produto}/`

### Atualizar memória

- `memory/projects/gb-importadora.md` — registrar análise feita
- `memory/sessions/{YYYY-MM-DD}.md` — nota diária

---

## Referência Rápida

### Credenciais necessárias

| Serviço | 1Password Item | Campos |
|---|---|---|
| Bright Data | Bright Data Web Unlocker | api_key |
| ML API (Vendas) | Mercado Livre API - Openclaw.agent | username (client_id), password (client_secret) |
| ML Tokens | `/root/.openclaw/.ml-tokens.json` | access_token, refresh_token |

### IDs úteis

| Dado | Valor |
|---|---|
| Seller ID GB | 532562281 |
| Nickname | GAMMAOFICIAL |
| Marca | Budamix |
| Categoria Potes | MLB244658 |

### Script de parsing

Ver `scripts/parse_ml_search.py` para a implementação do parser HTML.

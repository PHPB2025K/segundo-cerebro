---
title: "audience-targeting"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/meta-ads
---
# Segmentação e Públicos — Meta Ads
**Conta:** act_323534883953033 | **Mercado:** Brasil

---

## Tipos de Segmentação

| Tipo | Fonte | Qualidade | Escala |
|---|---|---|---|
| Core Targeting | Meta (interesses, demográfico) | Média | Alta |
| Custom Audience | Pixel, lista, engajamento | Alta | Média |
| Lookalike | Baseado em Custom Audience | Alta | Alta |
| Advantage+ Audience | IA do Meta | Alta (com dados) | Máxima |

---

## 1. Core Targeting (Manual)

### Demográfico básico
```json
{
  "targeting": {
    "age_min": 25,
    "age_max": 55,
    "genders": [1, 2],
    "geo_locations": {
      "countries": ["BR"]
    },
    "locales": [6]
  }
}
```
> `genders`: 1=Masculino, 2=Feminino. Omitir para ambos.
> `locales`: 6=Português (BR). Útil para excluir imigrantes.

### Por Estado (região)
```json
{
  "geo_locations": {
    "countries": ["BR"],
    "regions": [
      {"key": "3459"},
      {"key": "3460"},
      {"key": "3461"}
    ]
  }
}
```
> Keys de regiões: SP=3459, RJ=3460, MG=3461, RS=3462, PR=3463, SC=3464, BA=3466

### Por Cidade com raio
```json
{
  "geo_locations": {
    "cities": [
      {
        "key": "1031897",
        "radius": 50,
        "distance_unit": "kilometer"
      }
    ]
  }
}
```
> Key de São Paulo: 1031897

### Interesses (para contas sem histórico)
```json
{
  "targeting": {
    "flexible_spec": [
      {
        "interests": [
          {"id": "6003107902433", "name": "Cooking"},
          {"id": "6002925366585", "name": "Home organization"},
          {"id": "6003543765735", "name": "Kitchen"},
          {"id": "6003382917498", "name": "Home appliances"}
        ]
      }
    ]
  }
}
```

> **Buscar IDs de interesse:**
> ```bash
> curl -s "https://graph.facebook.com/v21.0/search?type=adinterest&q=cozinha&locale=pt_BR&access_token=$TOKEN"
> ```

### ⚠️ Mudança importante 2025
Meta removeu as exclusões de interesses/demográfico em março 2025.
**Exclusões só funcionam para Custom Audiences:**
```json
{
  "targeting": {
    "exclusions": {
      "custom_audiences": [
        {"id": "{COMPRADORES_RECENTES_ID}"},
        {"id": "{CLIENTES_ATIVOS_ID}"}
      ]
    }
  }
}
```

---

## 2. Custom Audiences

### Tipos e quando usar para GB Importadora

| Tipo | Fonte | Janela | Uso GB |
|---|---|---|---|
| Website Visitors | Pixel | 1–180 dias | Retargeting |
| Purchasers | Pixel - Purchase | 1–180 dias | LAL source, exclusão |
| Add to Cart | Pixel - AddToCart | 30–90 dias | Retargeting mid-funnel |
| Customer List | Upload email/tel | N/A | Clientes existentes |
| Page Engagement | Interagiram com Page | 1–365 dias | Mid-funnel |
| Video Views | Assistiram vídeos | 1–365 dias | Engajados com conteúdo |

### Criar via API

```bash
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/token")
AC="act_323534883953033"

# Compradores dos últimos 180 dias
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - Compradores - 180d" \
  -d 'rule={
    "inclusions":{"operator":"or","rules":[{
      "event_sources":[{"id":"{PIXEL_ID}","type":"pixel"}],
      "retention_seconds":15552000,
      "filter":{"operator":"and","filters":[
        {"field":"event","operator":"eq","value":"Purchase"}
      ]}
    }]}
  }' \
  -d "access_token=$TOKEN"

# Add to Cart (últimos 30 dias) — excluindo compradores
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - Add to Cart sem compra - 30d" \
  -d 'rule={
    "inclusions":{"operator":"or","rules":[{
      "event_sources":[{"id":"{PIXEL_ID}","type":"pixel"}],
      "retention_seconds":2592000,
      "filter":{"operator":"and","filters":[
        {"field":"event","operator":"eq","value":"AddToCart"}
      ]}
    }]},
    "exclusions":{"operator":"or","rules":[{
      "event_sources":[{"id":"{PIXEL_ID}","type":"pixel"}],
      "retention_seconds":2592000,
      "filter":{"operator":"and","filters":[
        {"field":"event","operator":"eq","value":"Purchase"}
      ]}
    }]}
  }' \
  -d "access_token=$TOKEN"

# Visitantes do site (últimos 30 dias)
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - Visitantes Site - 30d" \
  -d 'rule={
    "inclusions":{"operator":"or","rules":[{
      "event_sources":[{"id":"{PIXEL_ID}","type":"pixel"}],
      "retention_seconds":2592000,
      "filter":{"operator":"and","filters":[
        {"field":"url","operator":"i_contains","value":"budamix.com.br"}
      ]}
    }]}
  }' \
  -d "access_token=$TOKEN"

# Listar audiences
curl -s "https://graph.facebook.com/v21.0/$AC/customaudiences?\
fields=id,name,subtype,approximate_count,time_created&access_token=$TOKEN"
```

### Upload de Customer List
```bash
# 1. Criar audience
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - Clientes CRM" \
  -d "subtype=CUSTOM" \
  -d "customer_file_source=USER_PROVIDED_ONLY" \
  -d "access_token=$TOKEN"
# Retorna audience_id

# 2. Fazer upload dos dados (emails em SHA256)
# Formato: hashed_emails.csv
# email_sha256
# abc123def456...
# ...

curl -X POST "https://graph.facebook.com/v21.0/{AUDIENCE_ID}/users" \
  -d 'schema=EMAIL_SHA256' \
  -d 'data=[["abc123hash"], ["def456hash"]]' \
  -d "access_token=$TOKEN"
```

> **Match rate típico:** 40–70% para emails brasileiros.
> **Mínimo para Lookalike:** 100 matches após hashing.

---

## 3. Lookalike Audiences

### Tamanhos e quando usar

| Tamanho | Precisão | Alcance | Quando usar |
|---|---|---|---|
| 1% | Máxima | ~2M BR | Conversão, alta performance |
| 2–3% | Alta | ~4–6M BR | Escala inicial |
| 4–5% | Média | ~8–10M BR | Volume com qualidade |
| 6–10% | Baixa | ~12–20M BR | Awareness, budget alto |

### Melhores fontes (em ordem de qualidade)
1. **Compradores recentes** — Melhor sinal
2. **High-Value Customers** (top 25% por LTV) — Se você tiver dados de ticket
3. **Lista de clientes (CRM)** — Compradores históricos
4. **Add to Cart** — Intenção alta
5. **Visitantes do site (30d)** — Volume maior, qualidade média

### Criar via API
```bash
# LAL 1% a partir de compradores
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - LAL 1% - Compradores - BR" \
  -d "subtype=LOOKALIKE" \
  -d "origin_audience_id={COMPRADORES_AUDIENCE_ID}" \
  -d 'lookalike_spec={"type":"similarity","starting_ratio":0.0,"ratio":0.01,"country":"BR"}' \
  -d "access_token=$TOKEN"

# LAL 1-3% (range)
curl -X POST "https://graph.facebook.com/v21.0/$AC/customaudiences" \
  -d "name=GB - LAL 1-3% - Compradores - BR" \
  -d "subtype=LOOKALIKE" \
  -d "origin_audience_id={COMPRADORES_AUDIENCE_ID}" \
  -d 'lookalike_spec={"type":"similarity","starting_ratio":0.01,"ratio":0.03,"country":"BR"}' \
  -d "access_token=$TOKEN"
```

### Targeting com Lookalike no Ad Set
```json
{
  "targeting": {
    "custom_audiences": [
      {"id": "{LAL_AUDIENCE_ID}"}
    ],
    "geo_locations": {"countries": ["BR"]},
    "age_min": 25,
    "age_max": 55,
    "exclusions": {
      "custom_audiences": [
        {"id": "{COMPRADORES_AUDIENCE_ID}"}
      ]
    }
  }
}
```

---

## 4. Advantage+ Audience

### O que é
Sistema da Meta que usa IA para expandir o targeting além das sugestões fornecidas.
Você dá "sugestões", não restrições rígidas (exceto país e idade).

### Quando usar
✅ Conta com >50 compras/mês (algoritmo tem dados)
✅ Campanhas de conversão com Pixel maduro
✅ Advantage+ Shopping Campaigns (obrigatório)
✅ E-commerce com catálogo estruturado

### Quando não usar
❌ Conta nova sem histórico de dados
❌ Produto muito nichado (B2B específico)
❌ Budget muito baixo (não deixa o algoritmo explorar)
❌ Quando precisa de público muito específico

### Ativação via API
```json
{
  "targeting": {
    "advantage_audience": 1,
    "age_min": 18,
    "age_max": 65,
    "geo_locations": {"countries": ["BR"]}
  }
}
```
> `age_min/max` e `geo_locations` são os únicos campos respeitados como restrições.
> Interesses e outros campos viram "sugestões" quando `advantage_audience=1`.

---

## 5. Estratégia de Funil — GB Importadora

### Estrutura recomendada (quando tiver loja própria com Pixel)

```
TOPO DE FUNIL (Prospecção)
├── Broad targeting (25–55, BR) → Awareness ou Sales
├── LAL 3–5% de compradores → Sales
└── Interesse em organização/cozinha → Sales ou Traffic

MEIO DE FUNIL (Consideração)
├── Visitantes site 30–90 dias → Retargeting leve
├── ViewContent 14 dias → Sales
└── Engajamento Page 30 dias → Traffic/Sales

FUNDO DE FUNIL (Conversão)
├── Add to Cart 14 dias (sem compra) → Sales com urgência
├── Initiate Checkout 7 dias → Sales com oferta
└── Compradores 180 dias → Upsell/cross-sell
```

### Distribuição de budget sugerida (ROAS otimizado)
- **Topo:** 40–50% — Volume de novos usuários
- **Meio:** 20–30% — Nutrir consideração
- **Fundo:** 20–30% — Conversão de quentes (ROAS alto)

> Retargeting sozinho tem ROAS alto mas volume baixo. Topo abastece o funil.

---

## 6. Públicos a Criar Agora (Prioridade)

Quando o Pixel estiver instalado, criar imediatamente:

1. `GB - Compradores - 180d` → Fonte do Lookalike + exclusão
2. `GB - Compradores - 30d` → Exclusão em prospecção
3. `GB - Visitantes - 30d` → Retargeting geral
4. `GB - Add to Cart - 14d` → Retargeting quente
5. `GB - LAL 1% - Compradores - BR` → Prospecção qualificada
6. `GB - LAL 3% - Compradores - BR` → Volume

---

## Dicas de Segmentação para Produtos da GB

### Potes Herméticos de Vidro (carro-chefe)
- **Perfil:** Mulheres 28–50, classe média, interessadas em organização doméstica
- **Interesses sugeridos:** Cooking, Home organization, Kitchen, Meal prep, Glass containers
- **Melhor horário:** Noite (19h–22h) e fins de semana
- **Broad funciona bem:** Produto com ampla apelação

### Kits e Combos
- **Estratégia:** Retargeting de compradores de itens avulsos
- **Sazonalidade:** Datas comemorativas (Dia das Mães, Natal, Ano Novo)
- **ROAS esperado:** 15–20% acima de produtos avulsos

### Produtos de Fabricação Própria (MDF laser)
- **Nicho mais específico:** Pode justificar targeting por interesses
- **Interesses:** Home decor, DIY, Artesanato, Personalização


## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — agente proprietário desta skill
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis do agente
- [[openclaw/agents/kobe/AGENTS]] — orquestração com sub-agentes
- [[meta/mocs/MOC - Governanca OpenClaw]] — governança da plataforma
- [[projects/budamix-ecommerce]] — referência canônica detectada no conteúdo

---
title: "WhatsApp Estoque + Atacado Processor — baixa em tempo real"
created: 2026-05-29
type: project-status
status: producao
project: estoque-gb-fase2
tags:
  - estoque
  - whatsapp
  - tempo-real
  - producao
---

# WhatsApp Estoque + Atacado Processor — Daemon de baixa em tempo real

> Implementado 29/05/2026. Cobre passo (b) da arquitetura v2 do estoque.

## Fontes processadas

| Grupo | Área (operation_groups) | sourceType (stock_movements) | Tipo movimento |
|---|---|---|---|
| Estoque - GB Importadora | `estoque` | `whatsapp_estoque` | entrada ou saida (via header) |
| Devoluções - GB Importadora | `devolucoes` | `whatsapp_estoque` | mesmo parser do Estoque |
| Vendas atacado - GB Importadora | `atacado` | `atacado_whatsapp` | saida (cliente) |

## Cabeçalhos reconhecidos (grupo Estoque)

**Entrada:** `entrada`, `devolução`, `chegada`, `recebimento`, `compra` (+ plurais/sem acento)

**Saída:** `baixa`, `saída`, `avaria`, `retirada`, `perda` (+ plurais/sem acento)

Header é case-insensitive, asteriscos do markdown WhatsApp são removidos. Mensagens **sem cabeçalho reconhecido são ignoradas** (não adivinha tipo).

## Formato esperado

### Grupo Estoque (livre, múltiplos separadores)

```
ENTRADA (ou Avarias:, Baixa, Devolução, etc.)
SKU [separador] [nome opcional] [separador] qty
SKU [separador] qty
...
```

Separadores aceitos: `|` `-` `—` `–` `;` `<tab>`

Exemplos reais:
```
Avarias:
TL250R — 7
TL250P — 5
CAC250B — 1
```
```
ENTRADA
YW1520RC | Pote Hermético 1520ml | 50
SPC011 | Suporte Gamer | 10
```

### Grupo Atacado (padronizado)

```
*PEDIDO DE VENDA ATACADO NÚMERO:*968
- Estoque (x) 2024 ...
- *Nome da Empresa:* X
- *CNPJ da Empresa:* X
- Descrição do Produto/SKU: <texto>
- *Quantidade:* <num>
- Descrição do Produto/SKU: <texto>  (múltiplos produtos aceitos)
- *Quantidade:* <num>
...
```

Regex extrai N pares `Descrição/SKU + Quantidade` mesmo intercalados com outras linhas.

## Resolução de SKU multicamadas

1. **`resolver_sku()` Postgres function** — tenta direto: catálogo, alias, kit_bom
2. **`atacado_product_aliases`** — fallback texto livre → SKU canônico (para Atacado)
3. Se nada bate → divergente + alerta Telegram com sugestão de cadastro

Tabela `atacado_product_aliases`:
```sql
alias_text text PRIMARY KEY  -- normalizado: lowercase + sem acentos + colapsado
sku text                      -- SKU canônico (passa por resolver_sku depois)
confidence numeric
added_by text
notes text
active boolean
```

Seed inicial: `'caixa de fita 300' → KIT12FIT300M`.

## Arquitetura

```
Grupos WhatsApp (3)
   ↓ (whatsapp-operacao-poller, 30s)
operation_messages (Supabase)
   ↓ (operacao-dispatcher, 10s — Fase 4)
   memoriza pra Kobe + agent_owner
   ↓
whatsapp-estoque-processor (NOVO, 10s)
   ├─ Parser estoque (header + linhas livres)
   ├─ Parser atacado (regex Produto + Quantidade)
   ├─ Resolver SKU (resolver_sku + atacado_aliases)
   └─ POST /api/stock-movements/ingest-safe-outbound (apply=true)
                ↓
   stock_movements (ledger) + planilha ESTOQUE (baixa real)
                ↓
   marca operation_messages.routed_to_agents += 'whatsapp-estoque-processor'
   alerta Telegram tópico Estoque se houver divergente/erro
```

## Rota motor (estendida)

`/api/stock-movements/ingest-safe-outbound` agora aceita 5 sourceTypes:
- `marketplace` (já existente)
- `full_sheet` (já existente)
- `whatsapp_estoque` ← novo
- `whatsapp_devolucoes` ← novo
- `atacado_whatsapp` ← novo

E campo opcional `movementType` no evento (override pra entrada/saida/transferencia/ajuste).
Default por sourceType: full_sheet=transferencia, whatsapp_devolucoes=entrada, demais=saida.

Para **entrada**, motor SOMA na planilha (não subtrai); para saída, decrementa com guard `previousQty - quantity ≥ 0`.

## Idempotência (3 camadas)

1. Lockfile fcntl em `/var/run/whatsapp-estoque-processor.lock`
2. `operation_messages.routed_to_agents` array — pula mensagens já processadas
3. `external_event_id` UNIQUE em `stock_movements` (motor TS descarta)

## Alertas Telegram

Tópico **Estoque** (`thread 11932`) do Kobe Hub recebe alerta SOMENTE quando:
- Mensagem tem item divergente
- Mensagem do Atacado tem produto não-resolvido (sugere cadastro em `atacado_product_aliases`)

Mensagens 100% OK não geram notificação (regra Pedro: silêncio é sucesso).

## Coexistência com pipelines existentes

- **wholesale-evolution-poller** (PM2 existente) continua chamando Mission Control `/api/fisco/pedidos-venda-gb/ingest` para criação Bling. NÃO MEXIDO.
- O novo `whatsapp-estoque-processor` faz baixa de estoque em paralelo. Mesma mensagem alimenta os 2 pipelines independentes.

## Smoke test em produção (29/05 ~14:55 BRT)

```json
{
  "smoke-wpp-1 TL250R saida 3":           {"prev":44, "new":41, "status":"simulado"},
  "smoke-wpp-2 YW1520RC entrada 50":      {"prev":0,  "new":50, "status":"simulado"},
  "smoke-ataq-1 KIT12FIT300M atacado":    {"prev":3282, "new":3270, "kit_bom":"FIT300M qty=12"}
}
```

3/3 corretos. Entrada SOMA, saída SUBTRAI, kit_bom EXPANDE.

## Serviços PM2 finais (16 daemons)

```
estoque-budamix              # motor TS (build novo com 5 sourceTypes)
whatsapp-estoque-processor   # NOVO — baixa em tempo real
operacao-dispatcher          # roteia operation_messages → memory
whatsapp-operacao-poller     # captura 9 grupos WhatsApp GB
slack-dm-poller              # captura 3 DMs analistas
wholesale-evolution-poller   # legado, pipeline Bling Atacado
+ outros 10 (RH, central, etc.)
```

## Arquivos novos / modificados

| Path | Tipo |
|---|---|
| `/var/www/mission-control/scripts/whatsapp-estoque-processor.py` | NOVO |
| `/var/www/estoque-budamix/src/app/api/stock-movements/ingest-safe-outbound/route.ts` | extendido |
| `public.atacado_product_aliases` (Supabase) | NOVO |
| `/var/run/whatsapp-estoque-processor.lock` | runtime |

## Pendente (não-bloqueante)

- **(c) Cron marketplaces tempo real** — próximo na fila. ML primeiro (Yasmin), depois Shopee/Amazon
- **Confirmação inline no grupo Atacado** — hoje só alerta no Telegram. Se Pedro quiser confirmação visível pra equipe vendas, vira (b.2)
- **Métricas no dashboard** — número de baixas WhatsApp/Atacado por dia

## Atualização — 2026-06-01 — descrição livre em avarias e baixa total segura

Pedro definiu que o mapeamento deve decifrar descrições de produto também nas mensagens de avarias, não apenas no grupo de Atacado.

Regra operacional:
- Atacado: descrição livre continua resolvendo para SKU canônico antes da baixa.
- Estoque/Avarias: descrição livre com quantidade explícita pode resolver para SKU canônico.
- Estoque/Avarias: descrição livre sem quantidade só pode virar baixa automática se a frase indicar de forma inequívoca baixa total/zerar estoque e o SKU for resolvido com confiança.
- Caso concreto autorizado: caneca reta rosa / Caneca Porcelana Reta 200ml Rosa resolve para `CAR200R`; em avaria com comando de zerar estoque, baixar o saldo atual inteiro desse SKU.
- Se a descrição for ambígua ou curta demais, o item deve ficar como divergente/alerta, sem mexer no saldo.

Validação: mensagem teste “Avarias: Caneca reta rosa - zerar estoque” gerou evento para `CAR200R` com quantidade igual ao saldo físico atual consultado, mantendo trilha auditável em `rawPayload.zero_stock=true`.

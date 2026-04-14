# HEARTBEAT.md — Trader

_Verificações periódicas quando ativado em modo heartbeat._

---

## Verificações

### 1. Saúde dos Tokens
- ML: tokens `.ml-tokens*.json` válidos? TTL 6h — se expirado, rodar refresh
- Shopee: tokens das 3 contas válidos? TTL 4h — se algum falhou, registrar qual
- Amazon SP-API: LWA refresh funcional?
- Se algum token quebrado → registrar em `pending.md` + alertar Kobe

### 2. Pendências Estagnadas
- Ler `memory/pending.md`
- Itens 🔴 há > 3 dias sem progresso → sinalizar ao Kobe
- Itens 🟡 há > 7 dias → reavaliar prioridade

### 3. Dados de Performance (Quick Check)
- Algum SKU top 5 com queda > 20% em vendas vs semana anterior?
- Alguma conta com alerta de saúde (reputação, métricas)?
- Algum concorrente direto com mudança agressiva de preço?
- Se sim → gerar ALERTA para o Kobe

### 4. Lições Táticas Expirando
- Verificar `lessons.md` — alguma lição [TÁTICA] expira nos próximos 7 dias?
- Se sim → avaliar: promover para [ESTRATÉGICA] ou deixar expirar?

## Regra

- **Encontrou algo urgente** → alerta ao Kobe
- **Encontrou algo importante** → anota em `pending.md`
- **Nada de novo** → HEARTBEAT_OK

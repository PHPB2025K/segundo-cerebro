# HEARTBEAT.md — Builder

_Verificações periódicas quando ativado em modo heartbeat._

---

## Verificações

### 1. Saúde dos Projetos Ativos
- Algum deploy em produção com erro? (health check endpoints)
- Algum serviço Docker parado no VPS?
- Algum SSL expirando nos próximos 30 dias?
- Se sim → alertar Kobe

### 2. Pendências Estagnadas
- Ler `memory/pending.md`
- Hotfixes (🔴) há > 1 dia sem resolução → sinalizar ao Kobe
- Dívida técnica acumulando há > 14 dias → reavaliar prioridade

### 3. Dependências e Segurança
- Alguma dependência com vulnerabilidade crítica nos projetos ativos?
- Algum token/credencial expirando nos próximos 7 dias?
- Se sim → registrar em `pending.md` + alertar Kobe

### 4. Lições Táticas Expirando
- Verificar `lessons.md` — lições [TÁTICA] expirando nos próximos 7 dias?
- Promover para [ESTRATÉGICA] ou deixar expirar?

## Regra

- **Encontrou algo urgente** → alerta ao Kobe
- **Encontrou algo importante** → anota em `pending.md`
- **Nada de novo** → HEARTBEAT_OK

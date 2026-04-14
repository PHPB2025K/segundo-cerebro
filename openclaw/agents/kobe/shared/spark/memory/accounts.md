# Contas de Anúncio — Spark v2.0

_Atualizado: 2026-03-20_

---

## Meta Ads

| Item | Valor |
|---|---|
| **Ad Account** | `act_323534883953033` (GB Distribuição) |
| **Business Manager ID** | `7723008527787239` |
| **App** | KOBE.OPENCLAW (`3582660568568553`) |
| **API Version** | `v21.0` |
| **Base URL** | `https://graph.facebook.com/v21.0/` |
| **Token tipo** | Long-lived (60 dias) |
| **Token criado em** | ~2026-03-15 |
| **Token expira em** | ~2026-05-15 |
| **Token localização** | 1Password → Vault "OpenClaw" → "Meta Ads API - KOBE.OPENCLAW" |
| **Pixel ID** | [PREENCHER] |
| **Pixel status** | [PREENCHER — instalado e disparando? quais eventos?] |
| **Conversões configuradas** | [PREENCHER — Purchase, AddToCart, ViewContent, etc.] |
| **Domínio verificado** | [PREENCHER — domínio verificado no BM para iOS 14+?] |

### Protocolo de Token Meta

```
⏱️ MONITORAMENTO DE TOKEN
━━━━━━━━━━━━━━━━━━━━━━━━

Token expira: ~2026-05-15

🟢 > 30 dias restantes → Monitoramento normal
🟡 < 30 dias restantes → Incluir aviso no relatório semanal ao Kobe
🔴 < 7 dias restantes  → ALERTA IMEDIATO ao Kobe: "Token Meta expira em X dias. Pedro precisa renovar."
⛔ Expirado            → ALERTA CRÍTICO: "Token Meta EXPIRADO. Campanhas sem monitoramento. Ação urgente."
```

**Renovação:** Pedro gera novo token → Kobe atualiza 1Password → Spark confirma acesso.

### Sunset de API Meta

- Versão atual: `v21.0`
- Meta deprecia versões a cada ~2 anos
- Próxima verificação: 2026-06-17 (registrado em `lessons.md`)
- Quando migrar: atualizar Base URL + testar endpoints + registrar em `decisions.md`

### Skill disponível
- `skills/marketing/meta-ads/SKILL.md` — scripts de relatório, criação e regras automatizadas

---

## Google Ads

| Item | Valor |
|---|---|
| **Customer ID** | [PREENCHER] |
| **Manager Account (MCC)** | [PREENCHER — se houver] |
| **Developer Token** | [PENDENTE — Pedro precisa solicitar no API Center] |
| **OAuth Client ID** | [PENDENTE — criar no Google Cloud Console] |
| **OAuth Client Secret** | [PENDENTE] |
| **Refresh Token** | [PENDENTE] |
| **Conversion Tracking** | [PREENCHER — Google Tag instalado? quais conversões?] |
| **Linked Analytics** | [PREENCHER — GA4 conectado?] |

### Status de integração
- ❌ API não integrada ainda
- Dependência: Developer Token (1-7 dias úteis após solicitação)
- Após token: criar OAuth credentials → gerar refresh token → testar conexão

### Roadmap de integração Google Ads

| Etapa | Status | Dependência | Responsável |
|---|---|---|---|
| 1. Solicitar Developer Token | ⏳ Pendente | Pedro precisa acessar API Center | Pedro via Kobe |
| 2. Criar OAuth Client | ⏳ Pendente | Developer Token aprovado | Kobe |
| 3. Gerar Refresh Token | ⏳ Pendente | OAuth Client criado | Kobe |
| 4. Configurar Conversion Tracking | ⏳ Pendente | Token funcionando | Spark + Kobe |
| 5. Conectar GA4 | ⏳ Pendente | Conversion Tracking ok | Spark + Kobe |
| 6. Criar skill Google Ads | ⏳ Pendente | Etapas 1-5 completas | Kobe |
| 7. Primeiro relatório Google Ads | ⏳ Pendente | Skill criada | Spark |

---

## Cross-Platform

| Item | Status | Prioridade |
|---|---|---|
| UTM padrão definido | [PREENCHER] | Alta — precisa antes de lançar campanhas |
| Atribuição configurada | [PREENCHER] | Média — importante para cross-platform |
| GA4 unificado | [PREENCHER] | Alta — necessário para visão consolidada |
| Padrão UTM proposto | `utm_source=[plataforma]&utm_medium=cpc&utm_campaign=[naming_convention]` | — |

### Padrão UTM Recomendado (aguardando aprovação)

```
utm_source    = meta / google
utm_medium    = cpc / cpm / social
utm_campaign  = [naming convention da campanha]
utm_content   = [id do criativo ou variação do teste]
utm_term      = [palavra-chave — apenas Google Search]
```

---

## Checklist de Integridade (verificar semanalmente)

- [ ] Token Meta válido e funcional? (testar chamada simples)
- [ ] Pixel Meta disparando corretamente?
- [ ] Google Ads: alguma etapa do roadmap avançou?
- [ ] UTMs configuradas nas campanhas ativas?
- [ ] Algum acesso revogado ou expirado?

---

_Campos [PREENCHER] serão completados pelo Pedro via Kobe conforme configuração avançar._

---
title: "ml ads next steps"
created: 2026-04-14
type: project
status: active
tags:
  - project
---

# Próximos Passos — ML Ads Automation

## Correções aplicadas

- **[CORRIGIDO]** Bug crítico nos collectors: endpoints eram construídos em import-time com `ML_ADVERTISER_ID` vazio. Agora usam funções runtime `_get_campaigns_endpoint()` e `_get_ads_endpoint()` que leem env vars a cada chamada e validam presença do ID.
- **[CORRIGIDO]** Evolution API migrada de EasyPanel para Cloudfy (`https://trottingtuna-evolution.cloudfy.live`). URL e API key atualizadas no .env.

---

## 1. Deploy no Railway

### Criar projeto no Railway

1. Acesse https://railway.app e faça login
2. Clique em **New Project** → **Deploy from GitHub repo**
3. Conecte o repositório `ml-ads-automation` (ou use **Deploy from local** com CLI)

### Deploy via CLI (alternativa)

```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Criar projeto
railway init

# Linkar ao projeto
railway link

# Deploy
railway up
```

### Configurar variáveis de ambiente no Railway

No painel do projeto Railway, vá em **Variables** e adicione TODAS as variáveis:

```
ML_APP_ID=5960290698150493
ML_CLIENT_SECRET=ZtBkmIP778Az6qRSxG7DhGsUEtUIAgie
ML_REDIRECT_URI=https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/callback
ML_ADVERTISER_ID=              (preencher após primeira auth)
ML_SITE_ID=MLB

SUPABASE_URL=https://cckfkvqblvundnyphole.supabase.co
SUPABASE_KEY=<service_role_key>

ANTHROPIC_API_KEY=<sua_chave>

EVOLUTION_API_URL=https://trottingtuna-evolution.cloudfy.live
EVOLUTION_API_KEY=<sua_chave>
EVOLUTION_INSTANCE_NAME=MERCADO LIVRE ADS AUTOMATION

WHATSAPP_RECIPIENT=5511940457862

RAILWAY_ENVIRONMENT=production
```

### Verificar deploy

Após o deploy, acesse:
```
https://SEU-DOMINIO-RAILWAY.railway.app/health
```
Deve retornar: `{"status":"ok","service":"ml-ads-automation"}`

---

## 2. Atualizar Redirect URI no DevCenter do ML

1. Acesse https://developers.mercadolivre.com.br/devcenter
2. Vá em **Minhas Aplicações** → selecione o app (ID: 5960290698150493)
3. Na seção **Redirect URI**, atualize de `https://www.google.com` para:
   ```
   https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/callback
   ```
4. Salve as alterações
5. Atualize também a variável `ML_REDIRECT_URI` no Railway com a mesma URL

---

## 3. Primeira Autorização OAuth

### Passo 1 — Gerar URL de autorização

Abra no browser (substitua a redirect_uri pela URL real do Railway):

```
https://auth.mercadolibre.com.br/authorization?response_type=code&client_id=5960290698150493&redirect_uri=https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/callback
```

### Passo 2 — Autorizar o aplicativo

- Faça login com a conta do Mercado Livre da Gb Importadora
- Autorize as permissões solicitadas
- Você será redirecionado para a redirect_uri com um parâmetro `?code=TG-xxxx`

### Passo 3 — Trocar o code por tokens

Copie o `code` da URL de redirect e faça a chamada:

```bash
curl -X POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/callback \
  -H "Content-Type: application/json" \
  -d '{"code": "TG-XXXXX-XXXXX"}'
```

Resposta esperada:
```json
{"status": "success", "expires_at": "2026-...", "user_id": "12345"}
```

### Passo 4 — Obter Advertiser ID

Após ter o token, descubra o advertiser_id:

```bash
curl -s "https://api.mercadolibre.com/advertising/advertisers?product_id=PADS" \
  -H "Authorization: Bearer ACCESS_TOKEN_AQUI" \
  -H "Api-Version: 1"
```

Copie o `id` retornado e atualize a variável `ML_ADVERTISER_ID` no Railway.

### Passo 5 — Verificar

```bash
curl https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/status
```

Deve retornar `{"status": "valid", "remaining_minutes": ..., "user_id": "..."}`.

---

## 4. Configuração do Workflow N8N

### Criar workflow no N8N

Crie um novo workflow com os seguintes nós (na ordem):

```
1. Cron Trigger
   → Expressão: 0 30 10 * * 1-5
   → (10:30 BRT, segunda a sexta)

2. HTTP Request — Refresh Token
   → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/auth/refresh
   → Timeout: 30s

3. IF — Verificar refresh
   → Condição: {{$json.status}} == "success"
   → Se falhar: ir para nó de alerta (passo 3b)

3b. HTTP Request — Alerta WhatsApp (falha refresh)
    → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/notify
    → (ou enviar alerta direto via Evolution API)
    → STOP

4. HTTP Request — Coletar Campanhas
   → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/collect/campaigns

5. HTTP Request — Coletar Ads
   → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/collect/ads

6. IF — Verificar coleta
   → Condição: pelo menos um dos dois retornou status "success"
   → Se ambos falharam: alertar e STOP

7. HTTP Request — Analisar (Claude AI)
   → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/analyze
   → Timeout: 120s (a análise pode demorar)

8. IF — Verificar análise
   → Condição: {{$json.status}} == "success"
   → Se falhar: alertar e STOP

9. HTTP Request — Notificar WhatsApp
   → POST https://SEU-DOMINIO-RAILWAY.railway.app/ml/notify

10. Log de conclusão
    → Nó de Set para registrar timestamp e métricas do ciclo
```

### Configuração do Cron

- **Horário:** 10:30 AM BRT (13:30 UTC no horário de verão / 12:30 UTC fora)
- **Dias:** Segunda a Sexta
- **Razão:** O ML atualiza métricas diárias às 10:00 BRT, então coletamos 30 min depois

---

## 5. Teste do Ciclo Completo

### Checklist de validação end-to-end

Execute cada endpoint na ordem e valide:

```bash
# URL base (substitua pela real)
BASE=https://SEU-DOMINIO-RAILWAY.railway.app

# 1. Health check
curl $BASE/health
# Esperado: {"status":"healthy"}

# 2. Status do token
curl $BASE/ml/auth/status
# Esperado: {"status":"valid", ...}

# 3. Refresh do token
curl -X POST $BASE/ml/auth/refresh
# Esperado: {"status":"success", "expires_at":"..."}

# 4. Coletar campanhas (ontem)
curl -X POST $BASE/ml/collect/campaigns
# Esperado: {"status":"success", "campaigns_collected": N}

# 5. Coletar ads (ontem)
curl -X POST $BASE/ml/collect/ads
# Esperado: {"status":"success", "ads_collected": N}

# 6. Coleta completa (campanhas + ads)
curl -X POST $BASE/ml/collect/all
# Esperado: {"status":"success", "campaigns":{...}, "ads":{...}}

# 7. Análise Claude AI
curl -X POST $BASE/ml/analyze
# Esperado: {"status":"success", "report_id": N, "analysis_preview":"..."}
# (pode levar 30-60s)

# 8. Ver relatório
curl $BASE/ml/reports/latest
# Esperado: relatório completo com analysis_text

# 9. Enviar WhatsApp
curl -X POST $BASE/ml/notify
# Esperado: {"status":"success", "messages_sent": N}
```

### Verificar no Supabase

Após os testes, confirme no Supabase Dashboard que os dados foram salvos:

1. Tabela `ml_tokens` — deve ter registro(s) de tokens
2. Tabela `ml_campaigns_daily` — dados de campanhas com métricas
3. Tabela `ml_ads_daily` — dados de anúncios com métricas
4. Tabela `ml_optimization_reports` — relatório gerado com `sent_via_whatsapp = true`

### Verificar no WhatsApp

Confirme que a mensagem chegou no número 5511940457862 com o relatório formatado.

---

## Troubleshooting

### Token expirado ou refresh falha
- O `refresh_token` é de uso único. Se o refresh falhar, será necessário refazer o fluxo OAuth completo (Seção 3).
- O token expira em 6 horas. O refresh_token expira em 6 meses.

### Coleta retorna 0 campanhas
- Verifique se `ML_ADVERTISER_ID` está correto.
- Verifique se a conta tem campanhas Product Ads ativas.
- Tente com datas explícitas: `POST /ml/collect/campaigns?date_from=2026-02-26&date_to=2026-02-26`

### Análise do Claude falha
- Verifique `ANTHROPIC_API_KEY` no Railway.
- Confirme que há dados nas tabelas `ml_campaigns_daily` ou `ml_ads_daily`.

### WhatsApp não envia
- A Evolution API está hospedada no Cloudfy: `https://trottingtuna-evolution.cloudfy.live`
- Verifique se a instância Evolution API está online e conectada.
- Execute: `python scripts/create_evolution_instance.py` para verificar/criar a instância.
- Confirme que `WHATSAPP_RECIPIENT` tem o formato correto (DDI+DDD+número, sem +).

## Notas relacionadas

- [[projects/ml-ads-automation]]
- [[openclaw/agents/trader/IDENTITY]]

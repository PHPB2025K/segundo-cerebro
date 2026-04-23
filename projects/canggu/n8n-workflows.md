---
tipo: referencia
projeto: Canggu
status: ativo
tags:
  - canggu
  - n8n
  - workflows
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# N8N Workflows

> 5 workflows exportados em `~/Documents/05-Projetos-Codigo/budamix-ai-agent/n8n/`.
> N8N live em `https://trottingtuna-n8n.cloudfy.live`.
> 2 workflows com drift estrutural, 3 com drift de `active` state.

## Tabela de workflows

| Workflow | ID Live | Local Nodes | Live Nodes | Local active | Live active | Status |
|---|---|---:|---:|:-:|:-:|---|
| Budamix WhatsApp Agent (Principal) | `KE7YVXayl5ntjwQk` | 16 | **17** | false | true | ⏳ **Em depreciação** (ADR-007) — drift +1 node |
| Budamix WhatsApp Health Check | `DEjLkJcllQEmrcLF` | 11 | **2** | false | true | 🟡 Refactor massivo não sincronizado — restaurar em B2 |
| Budamix ML Questions | `g4JxNpC2sP9K8c71` | 8 | 8 | true | true | ✅ Sincronizado |
| Budamix ML Messages | `sg2yU46R9EQq3a2v` | 5 | 5 | false | **true** | 🟡 Só drift de `active` |
| Budamix Relatório Diário | `g7HBVeBRGPA29goW` | 4 | 4 | false | false | ✅ Sincronizado (inativo) |

Cobertura live↔local: 100% por nome (zero workflows órfãos ou com drift de nome).

## Propósito de cada workflow

### Principal (KE7YVXayl5ntjwQk)
Pipeline WhatsApp completo: webhook Evolution → parse → upsert customer/conversation → INSERT message → debounce 12s → consolidate → /functions/v1/[[edge-functions|process-message]] (com service_role Bearer hardcoded no node 12 — [[decisoes#ADR-001]]) → send WhatsApp response.

**Status pós-ADR-007:** em depreciação. Evolution será redirecionada para a edge function [[edge-functions|webhook-whatsapp]] (canônico). Plano em [[debitos-tecnicos#B4]].

### Health Check (DEjLkJcllQEmrcLF)
Schedule 15min. Verifica: Supabase auth, Ana responsividade, Evolution connection state, erros do principal <30min. Alerta via WhatsApp para número pessoal (5519993040768).

**Drift:** 11 nodes local → 2 nodes live. Lógica SMTP de alerting removida no live sem commit. Em B2 será restaurado em nova versão com canal Slack ([[decisoes#ADR-005]]).

### ML Questions (g4JxNpC2sP9K8c71)
Polling 2min. Puxa perguntas novas do Mercado Livre → chama /functions/v1/[[edge-functions|process-ml-question]] → posta resposta via ML API. Restaurado em 17/04 após fix de placeholders `YOUR_*` (ver DP-04 em [[decisoes]]).

### ML Messages (sg2yU46R9EQq3a2v)
Polling 1min. Processa mensagens do chat ML. Fonte canônica de credenciais OAuth ML.

### Relatório Diário (g7HBVeBRGPA29goW)
Cron 21h. Gera relatório do dia + salva no Supabase. Desativado no live e no local.

## Padrão de credenciais (Setup Credentials, Opção A)

Padrão estabelecido em 17/04/2026 para evitar cascata de falhas como o downtime de 09–17/04 (8 dias de Ana fora do ar). Motivação: garantir que nodes Code do N8N leiam credentials via guard clauses explícitas em vez de assumir presença, detectando placeholders acidentais no deploy.

**Setup Credentials node** (primeiro Code node do workflow) exporta constantes via `$json`:

```js
const SUPABASE_URL = 'https://jpacmloqsfiebvagfomt.supabase.co';
const SRK          = '<service_role_key>';
const EVO_URL      = 'https://trottingtuna-evolution.cloudfy.live';
const EVO_KEY      = '<evolution_api_key>';
const INSTANCE     = 'BUDAMIX AI AGENT';
return [{ json: { ...$input.first().json, SUPABASE_URL, SRK, EVO_URL, EVO_KEY, INSTANCE } }];
```

**Downstream Code nodes** consomem via `$('Setup Credentials').item.json.*` com guard clause obrigatório:

```js
const cfg = $('Setup Credentials').item.json;
const serviceKey = cfg.SRK;
if (!serviceKey || /PLACEHOLDER|YOUR_|FAKE/i.test(serviceKey)) {
  throw new Error('[GUARD] SRK inválida — verificar Setup Credentials');
}
```

No workflow principal (`KE7YVXayl5ntjwQk`): 7 Code nodes + Send WhatsApp Response leem chaves de um único Setup Credentials. Ocorrências de SRK no JSON: 9 → 1 após refactor. WAK: 2 → 1.

**Fonte integral:** [[_historico#Integração N8N]] (linhas 166–189 do histórico)

### Opção B (planejada, não executada)
Extrair os 7 Code nodes para uma Edge Function `ana-pipeline-step` que usa `Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')`. Eliminaria a chave 100% do JSON do workflow. ~4-6h de refactor. Registrada como pendência pré-auditoria em [[_historico#Pendências]].

**Relação com ADR-007:** Opção B é essencialmente o que ADR-007 resolve pela raiz — depreciar o N8N principal pra favor da edge function canônica já elimina todo o JS do workflow.

## Credentials referenciadas (apenas nomes — sem valores)

| Workflow | Credential | Tipo |
|---|---|---|
| Principal | `Budamix Supabase (Ana)` | httpHeaderAuth (Bearer service_role) |
| Principal | `Evolution API (budamix)` | httpHeaderAuth (apikey) |
| Health Check | (SMTP credential — status incerto após refactor 11→2 nodes) | smtp |
| Health Check | `Evolution API (budamix)` | httpHeaderAuth |
| ML Questions | `ML OAuth` | OAuth2 (ver ML Messages — fonte canônica) |
| ML Messages | `ML OAuth` (client_id + client_secret) | OAuth2 |
| Relatório Diário | `Budamix Supabase (Ana)` | httpHeaderAuth |

⚠️ **`workflow-principal.json:231`** contém **service_role JWT literal** — não via credential. Endereçado em [[decisoes#ADR-001]] passo 8.
⚠️ **`workflow-ml-questions.json` node 6** contém placeholder `YOUR_SUPABASE_SERVICE_ROLE_KEY` não substituído (inoperante).

## Drift vs repo — plano

- **Principal:** depreciar pós-ADR-007. Re-exportar uma última vez após atualizações para histórico, mas não é mais source-of-truth.
- **Health Check:** refazer completamente em B2 (11 nodes originais → novo design com Slack). Source-of-truth passa a ser a nova versão.
- **ML Questions / ML Messages:** rodar `scripts/sync-n8n-workflows.sh` (plano em [[debitos-tecnicos#B5]]) para trazer live → local e commitar.
- **Relatório Diário:** sincronizado, nada a fazer.

## Evidência completa

- Summary da análise: `~/audit-canggu-forensics/RAW/D_n8n/01_summary.md`
- Exports locais: `~/Documents/05-Projetos-Codigo/budamix-ai-agent/n8n/*.json`
- Padrão Credentials original: [[_historico#Integração N8N]]

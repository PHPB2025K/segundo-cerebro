---
title: "pending"
created: 2026-04-26
type: memory
agent: kobe
status: active
tags:
 - agent/kobe
 - memory
---
# Pendências — Aguardando Input/Ação

_Atualizado: 2026-04-29 23:30 BRT — consolidação diária pós Blog Pipeline v2 e Refactor Full Budamix Central_

## 🚨 URGENTE — Operação / Dados

- [ ] **Budamix Central Full — analistas preencherem custos zerados na planilha de precificação** em 30/04:
  - Lucas: Shopee — 11 SKUs únicos
  - Leonardo: Amazon — 11 SKUs únicos
  - Yasmin: Mercado Livre — 4 SKUs únicos
  Após cadastro, Kobe deve rodar `sync-costs.py` manualmente e validar: `zero_cost < 25` e custo real ≥ R$145k.
- [ ] **Budamix Central Full — Etapa 2D `sku_mapping` fallback** para 8 SKUs já mapeados: 098→KIT9S098, IMB501T-cores→IMB501C/V/P_T, 096→KIT3S096, CTL002→TL6250, KIT2YW1520AZ→KIT2YW1520. Cuidado com `quantity_multiplier`.
- [ ] **Budamix Central Full — Etapa 1E monitoramento Shopee**: criar healthcheck/alerta Telegram se alguma das 3 contas Shopee passar de 6h sem sync.
- [ ] **Budamix Central Full — validação cruzada ML Full e Amazon FBA** equivalente à validação Shopee 1D. Confiança atual média; Amazon tem 22 rupturas concentradas.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio

- [ ] **Blog Budamix — inspeção visual manual do post de teste** id `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` (pilar `receber-visitas`) no `/admin/blog`; após Pedro inspecionar cover/supports/pins, deletar o post de teste.
- [ ] **Blog WF0 — polir payload de resposta**: hoje retorna `pillar_focus=null` no response mesmo quando o foco foi aplicado internamente. Cosmético; funcional OK.
- [ ] **Social Studio — QA autenticado do preview**: testar fluxo completo até Fase 5 (criar ideia, gerar copy, editar carrossel, adicionar slides, renderizar PNGs).
- [ ] **Social Studio — decidir merge/deploy produção** da branch `feat/social-studio-phase2`/estado atual após QA do Pedro.
- [ ] **Social Studio — refactor wizard step-by-step**: briefing já existe para transformar `/admin/social` em fluxo guiado (Início → Ideia → Briefing → Copy → Slides → Visual → Revisão).
- [ ] **Vercel Token - Budamix Ecommerce** — item no 1Password `notesPlain` ainda incompleto; Kobe segue sem deploy autônomo. Mac/CC local continua como deployer.
- [ ] **Vercel Preview Env** — configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas.

## 🚨 Infraestrutura e autenticações degradadas

- [ ] **Google Ads API - Spark** — credenciais existem no 1Password, mas validação OAuth em 26/04 13:40 BRT retornou `invalid_grant`; refresh token precisa ser reautorizado/gerado novamente.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password.
- [ ] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; se Pedro quiser reativar essa rota, precisa reescanear QR Code. Evolution API/histórico segue separado e funcional.
- [ ] **Bling Token Refresh / Filial** — Matriz OK, mas Filial segue com bloqueio de empresa inativa/401/403; validar empresa Filial no painel Bling e reautorizar OAuth se necessário.
- [ ] **Vercel/GitHub webhook Budamix E-commerce** — GitHub→Vercel inexistente; todo push futuro exige `vercel --prod --yes` manual até reconectar o repo no dashboard Vercel.

## 🟡 Observação / estabilidade

- [ ] **Vault-as-SSoT — observar 48–72h**: confirmar sem conflitos git, sem dupla escrita e cron/autosave limpo.
- [ ] **Watchdog/Monitor Ponto/RH crons** — revisar timeouts/fallbacks em jobs com histórico de falha por timeout/model not found.

## 🟡 Futuro aprovado / não imediato

- [ ] **Budamix Blog — Pinterest API/OAuth** — ativar postagem automática no Pinterest quando padrão de artigos e imagens estiver validado. Por enquanto pins ficam como assets no Admin.
- [ ] **Budamix E-commerce — conteúdo real das páginas stub** `/faq`, `/contato`, `/termos`, `/trocas-e-devolucoes`; hoje são Coming Soon/noindex.
- [ ] **Newsletter Budamix** — formulário ainda não persiste email; precisa backend real.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **PCM001 Amazon** — ASIN pendente desde lançamento 07/04. Verificar status na Amazon BR quando voltar para frente de catálogo.
- [ ] **PCM001 peso embalado / foto 9 / custos refinados** — dados finais ainda pendentes.
- [ ] **SimulImport — validar cenários reais** — Pedro testar com importações dele.
- [ ] **Links Amazon da base Ana + campos [VERIFICAR]** — pendência estrutural sem avanço material desde 06/04.
- [ ] **Canggu/Ana** — pendências B1/B2/B4, Railway/deploy, sync product_listings, correções/embeddings e auditoria pós-fixes seguem aguardando repriorização.
- [ ] **Fisco** — product-packaging.json, limpeza de produtos origem=0, CC-e/NFs antigas e validações Bling Filial seguem abertas.
- [ ] **Amazon Ads/BidSpark** — revisões D+7, tickets Leonardo, TargetsV3, compute-results blind spots e groups follow-up seguem aguardando janela.
- [ ] **Mission Control DNS/customização**, **RH WhatsApp próprio**, **Security hardening extra**, **Lovable sync**, **Stripe live key**, **LinkedIn integração** seguem fora da fila imediata.

---
_Última organização: 2026-04-29 23:30 BRT._

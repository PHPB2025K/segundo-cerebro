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

_Atualizado: 2026-05-01 10:55 BRT — flush financeiro/DRE_

## 🚨 URGENTE — Operação / Dados

- [ ] **Budamix Central — Estoque Fase 1.5: validação visual do Pedro** em `/estoque/fisico` e `/estoque/consolidado` (KPIs premium, badge sync, donut FULL×FÍSICO, Top 10 SKUs). Se aprovado, seguir para Fase 2.
- [ ] **Budamix Central — Estoque Fase 2: movimentações**: tabela `physical_movements`, trigger `apply_physical_movement`, role `operator`, form modal, histórico por contramov e sync app→planilha a cada 2min.
- [ ] **Budamix Central — Estoque Fase 3/4**: import CSV/XLSX com template e validação em lote; import PDF com Vision/Claude quando virar prioridade.
- [ ] **Budamix Central — investigar SKU duplicado na aba ESTOQUE**: `physical_inventory_summary` ficou R$ 552.191,35 vs `physical_inventory_items` R$ 552.167,57 por deduplicação SKU-level.
- [ ] **Budamix Central Full — Etapa 1E monitoramento Shopee**: criar healthcheck/alerta Telegram se alguma das 3 contas Shopee passar de 6h sem sync.
- [ ] **Budamix Central Full — validação cruzada ML Full e Amazon FBA** equivalente à validação Shopee 1D. Confiança atual média; Amazon teve fantasmas removidos e precisa validação defensiva.

## 🚨 Canggu / Ana

- [ ] **Canggu — trocar senha temporária do admin** no login do admin. Ação do Pedro.
- [ ] **Canggu — adicionar instruções no system prompt da Ana** para `[Sticker recebido]`, `[Localização compartilhada: ...]` e `[Contato compartilhado: ...]`, evitando respostas genéricas.
- [ ] **Canggu — B1 segurança**: service_role JWT em arquivos tracked, ghost function `test-search`, `LOVABLE_API_KEY` legado, CORS aberto, `verify_jwt` em funções internas. Estimativa ~3 dias.
- [ ] **Canggu — B3 resiliência restante**: retry em `classifyIntent`/`generateResponse`, UNIQUE index `whatsapp_message_id`, dedup e fallback textual.
- [ ] **Canggu ML — monitorar próxima pergunta real do ML** para confirmar hard-block contra “entre em contato conosco”. Se escapar, ampliar regex/padrões.

## 🚨 RH / Ponto Certo

- [ ] **Ponto Certo — deploy produção do módulo Conversas RH** se ainda estiver apenas local: build, publicar na VPS e reiniciar PM2 `ponto-certo`.
- [ ] **RH — acompanhar feedback da Yasmin** sobre recebimento correto dos 2 chunks da mensagem inaugural.
- [ ] **RH — acompanhar primeiras respostas dos funcionários** às mensagens inaugurais; `rh-poller` e `rh-stuck-detector` devem capturar falhas silenciosas.
- [ ] **RH — Monitor Ponto Semanal real em 04/05 10h BRT**: primeira execução com agente RH operacional, polling e Conversas RH.
- [ ] **RH — datas de admissão dos funcionários** para cálculo futuro de férias.
- [ ] **RH — padrão do contador FOUR/Suellen** para espelho de ponto.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **DRE Abril/2026 — completar planilha padrão com dados faltantes**: Pedro vai usar Claude com a planilha `02_DRE_GB_PROCESSADO.xlsx` para preencher coluna `U` (Total Mês de Abril) com valores já validados. Ainda faltam coletar/confirmar: atacado, impostos sobre vendas, devoluções/cancelamentos contábeis, descontos, despesas administrativas, D&A, resultado financeiro e IRPJ/CSLL.
- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio

- [ ] **Blog Budamix — inspeção visual manual do post de teste** id `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` (pilar `receber-visitas`) no `/admin/blog`; após Pedro inspecionar cover/supports/pins, deletar o post de teste.
- [ ] **Blog WF0 — polir payload de resposta**: hoje retorna `pillar_focus=null` no response mesmo quando o foco foi aplicado internamente. Cosmético; funcional OK.
- [ ] **Social Studio — QA autenticado do preview**: testar fluxo completo até Fase 5 (criar ideia, gerar copy, editar carrossel, adicionar slides, renderizar PNGs).
- [ ] **Social Studio — decidir merge/deploy produção** da branch `feat/social-studio-phase2`/estado atual após QA do Pedro.
- [ ] **Social Studio — refactor wizard step-by-step**: briefing já existe para transformar `/admin/social` em fluxo guiado (Início → Ideia → Briefing → Copy → Slides → Visual → Revisão).
- [ ] **Vercel Token - Budamix Ecommerce** — item no 1Password `notesPlain` ainda incompleto; GitHub→Vercel auto-deploy já reduz bloqueio, mas token ainda é útil para rollback/hotfix CLI.
- [ ] **Vercel Preview Env** — configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas.

## 🚨 Infraestrutura e autenticações degradadas

- [ ] **core-audit cron** — último run em 29/04 03:02 BRT falhou com “Agent couldn't generate a response”. Investigar no próximo bloco operacional; histórico recente tem falhas intermitentes nesse job.
- [ ] **Google Ads API - Spark** — credenciais existem no 1Password, mas validação OAuth em 26/04 13:40 BRT retornou `invalid_grant`; refresh token precisa ser reautorizado/gerado novamente.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password.
- [ ] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; se Pedro quiser reativar essa rota, precisa reescanear QR Code. Evolution API/histórico segue separado e funcional.
- [ ] **Bling Token Refresh / Filial** — Matriz OK, mas Filial segue com bloqueio de empresa inativa/401/403; validar empresa Filial no painel Bling e reautorizar OAuth se necessário.

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
- [ ] **Canggu/Ana B2/B5/B6** — blocos não urgentes de observabilidade, governança e cleanup seguem aguardando repriorização.
- [ ] **Fisco** — product-packaging.json, limpeza de produtos origem=0, CC-e/NFs antigas e validações Bling Filial seguem abertas.
- [ ] **Amazon Ads/BidSpark** — revisões D+7, tickets Leonardo, TargetsV3, compute-results blind spots e groups follow-up seguem aguardando janela.
- [ ] **Mission Control DNS/customização**, **Security hardening extra**, **Lovable sync**, **Stripe live key**, **LinkedIn integração** seguem fora da fila imediata.

---
_Última organização: 2026-04-30 23:30 BRT._

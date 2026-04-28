---
title: "pendencias"
created: 2026-04-14
type: tracker
status: active
tags:
  - memory
  - context
---

# Pendências Ativas

> Formato: `[DATA] Aguardando [QUEM] sobre [O QUÊ]`
> Atualizar: sempre que uma pendência for criada ou resolvida.
> ✅ = resolvida (mover para "Resolvidas" no final do mês)

---

## 🔴 Críticas (bloqueiam progresso)

## 🔴 Delta Kobe/OpenClaw — importado em 28/04/2026

> Bloco conservador importado de `openclaw/agents/kobe/memory/pending.md` durante a Fase 3 da unificação. Resolver/deduplicar item a item nas próximas consolidações; não sobrescrever pendências históricas do vault.

### Infraestrutura e saúde do sistema

- [27/04] [[openclaw/agents/spark/IDENTITY|Spark]] — **Google Ads API**: OAuth retornou `invalid_grant`; refresh token precisa ser reautorizado/gerado novamente.
- [27/04] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token exposto em screenshot; integração operacional usa user token read-only no 1Password.
- [27/04] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; reativar exige QR Code. Evolution API/histórico segue funcional.
- [27/04] **Watchdog - Monitor de Crons** — revisar escopo/timeout após falha por timeout de 3min.
- [27/04] **Monitor Ponto Semanal** — falhas consecutivas por timeout de 300s; revisar escopo/timeout.
- [27/04] **RH Monitor Ponto Saída** — corrigir fallback/model not found antes da próxima execução.
- [27/04] **Bling Token Refresh / Filial** — Matriz OK; Filial segue com empresa inativa/401/403; validar painel Bling e reautorizar se necessário.

### Financeiro e marketplaces

- [27/04] **Ads spend março** — levantar gasto real por plataforma antes de fechar consolidado.
- [27/04] **Refazer fechamento de março** — DRE operacional + planilha + HTML com 5 extratos completos e ads spend correto.
- [27/04] **Mapeamento semanal DRE março** — separar semanas 01-07, 08-14, 15-21, 22-31.
- [27/04] **OAuth rotation 3 contas Shopee** — garantir refresh automático para `budamix-shop` e `budamix-store2`.

### Budamix Central / PCM001 / Blog

- [27/04] **PCM001 Amazon** — ASIN pendente desde 07/04; verificar status na Amazon BR.
- [27/04] **PCM001 peso embalado** — Pedro precisa informar peso final do kit embalado para NF-e.
- [27/04] **PCM001 foto 9** — Pedro precisa enviar hero image de encerramento.
- [27/04] **PCM001 custos refinados** — substituir estimativas por custo real.
- [27/04] **57 SKUs sem cost_price** em `fulfillment_inventory` e **9 Amazon SKUs sem preço** — investigar.
- [27/04] [[projects/budamix-ecommerce|Budamix E-commerce]] — **Supabase REST keys** salvas no 1Password retornaram 401; corrigir/rotacionar antes de workflows N8N dependerem delas.
- [27/04] **Budamix Blog — Pinterest API/OAuth** — futuro aprovado; ativar quando padrão de artigos/imagens estiver validado.

### SimulImport e backlog estagnado

- [27/04] [[projects/simulimport|SimulImport]] — Pedro validar cenários reais com importações dele.
- [27/04] **Backlog estagnado >14d** — links Amazon da base Ana, revisão `[VERIFICAR]`, sync Amazon de links/platform IDs, 3 SKUs ML sem mapeamento, teste motor SimulImport, NFs teste, product-packaging, B2B março, WhatsApp RH, Mission Control DNS, Canggu/Railway, Bidspark CLAUDE.md e webhooks marketplaces.


- [26/04 noite] [[projects/budamix-ecommerce|Bling]] — **Filial CNPJ 58.151.616/0002-24 retorna HTTP 403 "empresa inativa"** mesmo após rotação do Client Secret 26/04. Confirmado: NÃO é problema de credencial. **Pedro precisa investigar no painel Bling**: plano Mercúrio cobre Filial? CNPJ secundário ativado/suspenso? Pode ser financeiro/contratual. Sem isso, NF-e da Filial e operações fiscais via API ficam bloqueadas. → [[memory/context/decisoes/2026-04#[26/04]]]
- ✅ [26/04 noite → 28/04] **Vault como single source of truth — Fase 4 (vault-as-SSoT) concluída** em 28/04/2026. `openclaw.json` migrado pra `workspace: /root/segundo-cerebro` (Kobe + 5 subagentes). Symlinks raiz no vault apontando pra `openclaw/agents/kobe/`. Cleanup adicional pelo CC local: removido clone aninhado `workspace/segundo-cerebro/`, arquivados core files stale em `_archive/pre-vault-switch-20260428/`, cron legado `sync-segundo-cerebro.sh` desabilitado, README-DEPRECATED.md no workspace. Protocolo Git seguro implementado em `meta/scripts/safe-write.sh` (lockfile + pull --rebase + abort em conflito). Skill `/cerebro` Fase 0a + `/salve` Passo 5 refatorados. Tag de rollback `pre-vault-cleanup-20260428` em ambos repos. Teste bidirecional aceito (CC local → push → autosave Kobe puxou ed0c73d). Janela observação 48h.
- [22/04] **Reuniões semanais presenciais marketplace** — 22/04 Leonardo (Amazon) HOJE 14:30, 23/04 Lucas (Shopee) 14:30, 24/04 Yasmin (Mercado Livre) 14:30. Local: Escritório Budamix Pedreira-SP. Convidado `marketplace@gbimportadora.com`. Criados no calendar Trabalho via `gog` do VPS.
- [20/04 6h BRT] [[projects/amazon-ads-automation|Amazon Ads]] — **Validar N8N Ciclo Diário rodou limpo** após fix `continueOnFail` no node `Send Health Alert WhatsApp` aplicado em 19/04 22h. Workflow `U8MCTTkNEJnD75aV`. Primeiro teste real do fix é amanhã 6h. Se falhar, PARAR migração BidSpark-3 nos 5 grupos restantes e diagnosticar. Comando: `curl -s -H "X-N8N-API-KEY: $KEY" "$URL/api/v1/executions?workflowId=U8MCTTkNEJnD75aV&limit=3"`
- [23/04 noite] ✅ ~~[[projects/budamix-ecommerce|Budamix Ecommerce]] — ~106 commits locais à frente de `origin/main`~~ → **RESOLVIDO.** Em 5 fases: (1) backup branch `backup-pre-push-20260423-200452`, (2) 6 commits lógicos do WIP (feat pdp/admin/home + style/chore), (3) `git merge -s ours origin/main` integrou os 2 "behind" (cherry-pick redundante + empty trigger) sem aceitar diff de -8030 linhas, (4) `git push origin main` direto — `135570e..9ab138a` (HEAD válido bastou — doc `vercel-hobby-commit-author-block` confirmado), (5) **descoberta: webhook GitHub→Vercel NÃO EXISTE** (`GET /hooks → []`); deploy foi `vercel --prod --yes` manual (ID `dpl_3Gaz38ULNsddwhawDsZCQvEKypov`, 32s). 111 commits em prod. 2 commits extras mesma sessão: `a2c525b` (remove slide potes-vidro) + `5a1837b` (SoonBadge + 4 rotas stub ComingSoon). Prod servindo last-modified 24/04 01:12 UTC.
- [17/04] ✅ ~~Instalar Apps Script na planilha de estoque~~ → **Substituído por cron VPS `*/5 * * * *` em `/opt/budamix-stock-sync/sync.py`** (187.77.237.231). Primeiro run: 25 variants atualizados, 0 erros. Scripts em `scripts/stock-sync-cron.{py,sh}`.
- [17/04] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Testes manuais de pagamento MP real** pendentes: cartão aprovado/recusado, PIX completo, simulador webhook MP Developers, estoque insuficiente, frete zerado via DevTools. Suite em `AUDITORIA-CHECKOUT-MP.md` §5.

- [06/04] VPS disco 63.4% usado de 47GB — monitorar crescimento. Logs de memory, backups e Chrome cache podem encher. Limpeza necessária em breve.
- [06/04] VPS memória 80% + swap 52% — processo zombie detectado. Requer investigação.
- [06/04] Aguardando **Pedro** publicar Budamix Central no Lovable (destacques visuais campos IA, envio WhatsApp corrigido)
- [22/04] [[projects/canggu|Canggu]] — **B1 iniciado e pausado 22/04 noite** ([[projects/canggu/perguntas-abertas#Execução em andamento (pausada)]]). Zero mutação em produção. Feito: tag defensiva `b1-pre-rotation-20260422-211653`, 3 fontes JWT confirmadas (mesma key), baseline em `~/audit-canggu-forensics/RAW/_b1_baseline.md`. NÃO feito: nenhuma key gerada, zero ALTER DATABASE, zero edit em migrations/workflow. **Retomar 23/04 como primeira tarefa.** Antes: ler [[projects/canggu/decisoes#ADR-001]] + [[projects/canggu/debitos-tecnicos#B1]]. Ainda falta: rotação service_role + deletar ghost function `test-search` + `verify_jwt=true` nas 11 edge functions internas + remover `LOVABLE_API_KEY` órfão. Esforço M (5-7d). Destrava o resto. → [[openclaw/agents/builder/IDENTITY|Builder]]
- [22/04 noite] [[projects/canggu|Canggu]] — **Leak de JWT service_role no transcript de sessão Claude Code** (workspace `planejamento-importacao-2026`). Durante B1 Passo 0.3, `grep -n 'eyJ\|current_setting' <migration>` imprimiu linha inteira com token completo. Violação da regra "primeiros 15 chars apenas". Não muda plano B1 — intensifica urgência do passo 7 (revogação da key antiga). Chave ainda válida até B1 completar.
- [22/04] [[projects/canggu|Canggu]] — **B2 (Observabilidade) em paralelo** — restaurar Health Check N8N (hoje 2 nodes live vs 11 local — SMTP removido) com **Slack** como canal ([[projects/canggu/decisoes#ADR-005]]). Cron `embedding IS NULL` watcher. Escalation automático em áudio com placeholder. Esforço M (3-5d).
- [22/04] [[projects/canggu|Canggu]] — **ADR-006 pendente** (bloqueia B4): portar `process-ml-question` pra `searchProductsEnriched`/base_products ou adiar? Default se não decidir = adiar. → Pedro reflete antes de iniciar B4.
- [22/04] [[projects/canggu|Canggu]] — **Working copy dirty em produção**: 12 M + 5 untracked em `budamix-ai-agent`, incluindo 2 migrations já aplicadas ao banco (`20260417120000_auto_embed_trigger_base_products.sql` + `20260417120100_search_corrections_function.sql`) sem commit correspondente. Commitar ou stashar em B5. Feature em andamento: loop de correções semânticas (+237 LOC em `process-message`).
- [17/04] ✅ ~~[[projects/canggu|Ana]] — Opção B de credentials (7 Code nodes → edge function `ana-pipeline-step`)~~ → **Superado por [[projects/canggu/decisoes#ADR-007]]** — pipeline WhatsApp canônico passa a ser `webhook-whatsapp` edge function; workflow N8N Principal será depreciado em B4. Padrão Setup Credentials (Opção A) segue relevante pros outros 4 workflows N8N (ML Questions, ML Messages, Health Check, Relatório Diário).
- [17/04] ✅ ~~[[projects/gb-import-hub|GB Import Hub]] — GB25010 numerário R$64.136,40 vence 20/04~~ → **Container nacionalizou 22/04/2026** (DI 26BR0000441488-9, dólar 4,9844). NF de entrada Open Trade #580119 emitida 23/04 10:17 (R$ 97.142,03 total NF / R$ 91.213,17 produtos). NF de transferência Matriz→Filial #000653 criada rascunho no Bling 24/04 (aguarda validação Pedro).
- [22/04 noite] [[projects/planejamento-importacao-2026|Planejamento Importação 2026]] — ⚠️ **PLANO EM RECALIBRAÇÃO (25/04).** Fase 3.1 modelou "lotes de 4 containers a cada X meses". Pedro corrigiu o pressuposto: pipeline real é **lotes de 2 containers, pedido a cada ~40-45 dias, 3 lotes vivos simultâneos** (fabricando / em trânsito / chegando). Modelo Cenário E subdimensionou capacidade. Bloco de números operacionais já extraído (sessão 25/04, output só no chat — sem arquivo): receita líq média fev-abr/26 R$ 104k/mês (anterior nov25-jan26 ≈ R$ 0,4k pós-ruptura), abr/26 normalizado R$ 142k, top 10 SKUs concentram 84,6% do trimestre, IMB501P bate 24,3 un/dia (3 canais). **Próximo passo:** refazer simulação Fase 3.1 com nova cadência. Resultado anterior (Cenário E vencedor com receita 18m R$ 2.634k / OD máx R$ 231k / caixa final R$ 866k) preservado como baseline em `data/03-flywheel.xlsx` + `04-plano.md` para comparação. **Antes de 01/05/2026:** as 6 ações imediatas pré-pedido permanecem válidas (caixa, overdraft, composição L1, descontinuar zumbis, IMB501V_T Shopee).
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **CC-e da NF 000649** (transferência GB25011) a ser colada manualmente no painel Bling web pelo Pedro. Texto pronto (680 chars) corrige volumes zerados (1.044 cx / 15.136,07 kg bruto / 13.279,29 kg líq). Bling v3 API não expõe endpoint CC-e. → imprimir e enviar com Qualilog na segunda.
- [24/04 tarde] ✅ ~~NF 000653 (transferência GB25010) aguardando validação + envio SEFAZ~~ → **RESOLVIDA.** NF **AUTORIZADA SEFAZ** às 11:45:21 BRT de 24/04/2026 (chave `42260458151616000143550010000006531440066894`) no regime antigo (ICMS 4% destacado + IPI + origem 2). Decisão Pedro: **Opção 2** — manter como está, aplicar novo regime (CST 90/55 + origem 1) apenas a partir da próxima transferência. Alinhado com orientação literal Suellen ("próximas emissões" — sem retroação). NF 000653 = último ato do regime antigo. Blocos A+B+C (parametrização novo regime) executados em paralelo.
- [24/04 tarde] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **Monitorar DFC Filial pós-novo regime (60-90 dias).** Sem crédito ICMS da transferência (LC 204/2023 — Suellen 24/04/2026), Filial paga 18% cheio na venda aos Simples. Antes recebia ~4% de crédito embutido. Observar impacto no DFC pelos próximos 60-90 dias antes de decidir se revisa margem interna de 5% (Filial→Simples). Métrica: comparar ICMS pago Filial / faturamento Filial antes e depois de 24/04/2026.
- [24/04 tarde] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **29 produtos origem=0 (Nacional) mal-classificados** na Matriz Bling. KIT3S096/6S097/9S098/3S099/6S100/9S101 + KIT2/4 YW320/520SQ/800SQ + YW320SQC/520SQC/800SQC/1050RCC/1520RCC/640RCC + vasos 128M_B/127B_B/130P_B/511C_B + árvores artificiais + taças F0205 + pseudo-itens (Frete/Embalagem Papelão/Complemento IPI). Alguns são importados direto (deveriam ser origem 1), outros são pseudo-itens sem NCM. Limpeza separada com input Suellen — não bloqueia transferência GB25010.
- [24/04 tarde] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **Cadastro Bling Filial (conta separada) — validar origem 2 nos produtos**. Suellen orientou "Filial: origem 2". Hoje só temos OAuth Matriz; Filial tem conta Bling própria. Acessar e validar que os produtos cadastrados lá têm origem 2. Se houver descasamento, ajustar.
- [24/04 tarde] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **Atualizar PDF oficial v2.0 → v2.1 da estratégia fiscal**. O arquivo `business/importacao/estrategia-fiscal-gb-v2.0.pdf` está desatualizado pós-orientação Suellen. Agendar sessão com Suellen/FOUR para v2.1 oficial (incluir LC 204/2023 + RIPI art. 43 X + origem 1/2 por estabelecimento). Vault já está em v2.1 (24/04). Prioridade baixa — documentação acompanha operação.
- [24/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **product-packaging.json quase vazio** (`shared/fisco/config/` no VPS). Só 3 SKUs cadastrados (CXIMB501C/V/P) todos com `_preenchido: false` e pesos zerados. NFs de transferência dependem de pesos reais por SKU — hoje rateio por valor como aproximação documentada. Preencher os 9 SKUs da GB25010 (+ restante dos SKUs ativos) com peso bruto/líquido unitário + dimensões + unidades_por_volume. Prioridade média (não bloqueia, mas emissões futuras ficam mais precisas). → Pedro ou Fisco via Builder.
- [07/04] ~~OpenClaw — rate limit cascata: todos os crons falhando por fallback = mesmo provider.~~ → Movido para ✅

## 🟡 Importantes (não bloqueiam mas precisam de ação)

- [27/04] [[knowledge/concepts/kg-wikilinks-auditoria-metodo|KG Auditoria]] — **Fase 2 da auditoria de wikilinks: zerar os 91 stubs remanescentes**. Stubs vivos (todos referenciados, nenhum órfão) representam dívida documental: 126 edges Canggu apontam pra headings `debitos-tecnicos#B1..B6`, `decisoes#ADR-001..007`, `_historico#Pendências`, `edge-functions#Secrets` etc. que não foram escritos nos arquivos canggu/. + 85 edges OpenClaw incluindo placeholder `_stub/reply_to_current.md` (Kobe). Esforço estimado: 2-3h pra criar headings nos arquivos canggu/. Prioridade BAIXA — stubs vivos são aceitáveis. → [[memory/sessions/2026-04-27]]
- [27/04] [[knowledge/concepts/kg-wikilinks-auditoria-metodo|KG Auditoria]] — **Detecção contínua de novos isolados** (proposta). Hoje só aparecem quando algum agente cria arquivo novo no VPS (ex: 30 sessões do Kobe surgiram durante esta auditoria e ficaram isoladas). Considerar cron ou hook que detecte isolados periodicamente e alerte. Esforço S (1-2h). Prioridade BAIXA.
- [26/04 noite] **Fase 4 — arquivar `PHPB2025K/tobias-workspace`**. ~5 min. Adicionar `README-DEPRECATED.md` apontando pra `segundo-cerebro/openclaw/agents/kobe/` + Settings GitHub → Archive repository. Não deletar. Só após Fase 2B-FULL validada. → [[knowledge/concepts/disaster-recovery-vault]]
- [26/04 noite] ✅ ~~**Fase 5 — DR drill**~~ → **CONCLUÍDA** (commit `eeda5e8`). 7/7 testes não-destrutivos OK em `/tmp/dr-drill/`. Cenários A/C/D/E/F cobertos. Cenário B (2ª VPS bootstrap) adiado — componentes individuais já testados. Recovery time medido: <1 min Mac novo do zero, ~5s restauração granular. Arquitetura **verified resilient ✅**. Detalhes em [[knowledge/concepts/disaster-recovery-vault#Validação 26/04 — DR drill executado]]
- [26/04 noite] [[knowledge/concepts/disaster-recovery-vault|DR Plan]] — **Drill completo cenário B (VPS destruída)** ainda pendente. Provisionar 2ª VPS efêmera, fazer `git clone segundo-cerebro` + bootstrap Kobe, validar arranque limpo. Esforço ~4h + custo VPS por algumas horas. Componentes testados separadamente (#4 + #6 do drill 26/04), mas o end-to-end completo seria validação final.
- [26/04 noite] **Polish do vault** (não-urgente) — corrigir 1 frontmatter malformed em `skills/marketplace/shopee-fees-rules/SKILL.md` + 2 wikilinks ambíguos legados (`[[agents/kobe/IDENTITY]]`, `[[skills/superpowers/dispatching-parallelopenclaw/agents/SKILL]]` sem path completo). Detectados pelo KG rebuild durante drill. Resolver caso a caso quando passar pelos arquivos.
- [26/04 noite] **Validação 48h da 2B-LITE** — observar (sem ação) que sync workspace → vault gera commits `kobe-auto: sync memory ...` autônomos via cron (`7,22,37,52`) e que daily-vault-backup roda 06:00 UTC sem erro. Em 28/04 validar logs `/root/sync-memory-to-vault.log` e `/root/vault-backup.log`. Após OK, propor 2B-FULL.
- [26/04 noite] [[projects/budamix-ecommerce|Budamix E-commerce]] — **Webhook GitHub→Vercel inexistente** (`GET /repos/PHPB2025K/budamix-ecommerce/hooks → []`). Toda atualização futura exige `vercel --prod --yes` manual após push. Candidato a missão separada (~15 min OAuth: Vercel Dashboard → budamix-ecommerce → Settings → Git → Connect Git Repository → GitHub).
- [22/04 ~21:45] [[projects/canggu|Canggu]] — **Backlog de 3 features pedidas para Ana** registrado em [[projects/canggu/backlog-features]]. F1 (humanização e não-repetição), F2 (multimodal/imagens), F3 (histórico completo após hiato). Priorização preliminar sugerida F3 → F1 → F2, mas decisão de encaixe no roadmap B1-B6 fica para sessão pós-B1. Cada feature traz paths concretos que toca + dependências técnicas + esforço S/M/L.
- [19/04] ✅ ~~**Migração BidSpark-3 pendente em 5 grupos**~~ → **Fila fechada 22/04.** 5 grupos executados em 20-21/04 (Canequinhas 20+DEFERRED, Potes Redondos 5+DEFERRED, Kits Microfibra 3+DEFERRED, Canelada 10+DEFERRED, Jarra 12+DEFERRED). Total 50 EXECUTED + 24 DEFERRED. Próxima revisão D+7 em **27/04**.
- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Investigação de listing Tampa Bambu** (delegada a **Leonardo** em 22/04 — focal point Amazon). 7 ASINs: B0F2GHQHRN, B0F2GKSHYW, B0F2GQNT81, B0F2GKZZ43, B0F2GM9HMW, B0FN4PGK4M, B0FN4PW4SS. Pergunta: por que buscas "bambu" específico geram clique mas zero venda? Confirmar com Pedro se já foi feita antes de re-delegar. Destrava reativação do Alcance + M2 pleno do grupo.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Ticket 7 — Investigação listing Performance Canequinhas Café** (delegada a **Leonardo**). Performance 143 clicks / 1 pedido 30d (conv 0,7%). Mesma keyword EXACT vende 2× na Alcance, 0× na Perf. Hipótese: ASIN divergente ou listing degradado. Deadline 27/04. Bloqueia B2-P4/P5/B2-B4.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Ticket 10 — Destravar bootstrap Potes Redondos Plástico** (delegada a **Leonardo**). 3 ASINs B0GSWRMDRG/B0GSWJ91JM/B0GSWLK5F3. Grupo com 0 vendas 30d. Verificar: título contém "plástico"? (produto é vidro), ASINs vinculados nas 3 campanhas, Buy Box, estoque, fotos, margem IMB501T. Deadline 27/04. **Prioridade ALTA.**
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Ticket 11 — Anomalia 7d=0 em Kits Microfibra Carro** (delegada a **Leonardo**). Grupo parou de receber impressões ~06-08/04. Hipótese 2 (PHRASE remanescentes) refutada em 21/04. Restam: listing degradado, estoque esgotado, re-calibração Amazon pós-limpeza 10/04. Deadline 27/04.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Ticket 9 — `TargetsV3` helper** (código). Bid reduction em targeting expressions Auto Descoberta (Canequinhas, Canelada). Bloqueia B2-B1 real desses 2 grupos. Sem ele, só paliativos (cortar budget). Deadline 27/04. Impacto ~R$ 80-120/mês economia.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Ticket 12 — compute-results blind spots** (código). 47/47 REMOVER_NEGATIVA com NOT_TRACKED + 2/2 AJUSTAR_BID com NO_RESULT. Proposta fix: baseline por campanha em vez de entidade. Sem ele, revisão 27/04 cega para ~50% das ações. Deadline antes de 27/04.
- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Revisitar Canecas Porcelana Tulipa em ~03/05** (14d após Bloco 3 de 19/04 que removeu 39 NEG_PHRASE destrutivas). Medir: (a) Descoberta voltou a converter (30d atual: R$38 / 0 vendas); (b) ACoS consolidado caiu abaixo de 20% target; (c) novos winners emergiram para Bloco 2 que ficou vazio.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **22 commits local-only pendentes de push** em `main` (cresceu de 4 em 19/04 para 22 em 22/04). Inclui: 5 scripts executor bidspark3_* + 5 scripts analysis_* + 5 reports + 1 financeiro + updates TICKETS.md + knowledge file vault. Push fica pra Pedro decidir — eventualmente após revisão 27/04.
- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Revisão D+7 conjunta dos 5 grupos BidSpark-3** em **27/04/2026**. Medir `result_after_7d` de 103 ações (50 EXECUTED sessão 20-21 + 53 anteriores pós-10/04). Com ressalva do Ticket 12 (blind spots em REMOVER_NEGATIVA e AJUSTAR_BID).
- [06/04] ~~OpenClaw — migração de modelos para GPT 5.4 / GPT 5.1-mini.~~ → Movido para ✅
- [06/04] Budamix Central — Fase 4 cleanup pendente: remover campos antigos (marketplace_links, available_kits, price_marketplace) e dropar tabela marketplace_product_mapping. Só executar quando tudo estiver estável nas tabelas novas. → [[openclaw/agents/builder/IDENTITY|Builder]]
- [06/04] Budamix Central — ~14 Session Extractors do [[openclaw/agents/kobe/AGENTS|OpenClaw]] desabilitados (timeout 120s insuficiente para Opus 4.6). Precisam de 300s+. Reavaliar após migração GPT 5.4.
- [06/04] Budamix Central — Analistas devem preencher campos ricos (descrição completa, sugestões de uso, diferenciais, tags) dos 44 produtos ativos. Guia entregue. Top 10 primeiro. → [[memory/context/people|People]]
- [06/04] [[openclaw/agents/kobe/AGENTS|OpenClaw]] — 3 crons com timeouts: job-monitor (30s), Contingency Guard (30s), Organização Noturna (180s). Todos precisam de aumento.
- [06/04] ~~OpenClaw — Amazon Request Review overloaded. Haiku 3.5 possivelmente depreciado.~~ → ✅ Resolvido 13/04: migrado para Opus 4.6, fix delivered_at, backfill executado
- [06/04] [[openclaw/agents/kobe/AGENTS|OpenClaw]] — GitHub Backup com timeouts. Aumentar de 120s para 300s.
- [06/04] Segurança — Porta 8084 (Evolution API?) aberta na UFW. Verificar necessidade.
- [06/04] Segurança — Tailscale/WireGuard não implementado. Recomendado.
- [07/04] Shopee — 3 anúncios Kit Porta-Copos precisam preencher campos no Seller Center (GTIN, NCM, Cor, Garantia) para diagnóstico verde. Checklist enviado ao [[openclaw/agents/kobe/IDENTITY|Kobe]]. → [[skills/shopee-listing-creator/SKILL|shopee-listing-creator]]
- [07/04] Bright Data — API key do web_unlocker1 (e0f949a4-2599-4a02-a0a2-1063ed8fe364) precisa ser salva no 1Password do [[openclaw/agents/kobe/IDENTITY|Kobe]] (substituir a antiga bc468a8b...). Zona criada 07/04.
- [07/04] [[openclaw/agents/kobe/AGENTS|OpenClaw]] — Skills [[skills/shopee-listing-creator/SKILL|shopee-listing-creator]] e [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]] precisam ser importadas pelo Kobe (openclaw skills import).
- [07/04] Amazon BR — ASIN do PCM001 pendente (ACCEPTED com 0 erros, processando). Verificar. Após ASIN: upload de fotos via Seller Central + registrar no Supabase. → [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]]
- [08/04] [[memory/projects/gb-import-hub-schema|GB Import Hub]] — Frontend no Lovable ainda aponta pro Supabase antigo. Precisa atualizar env vars no painel do Lovable OU usar somente deploy VPS (import.budamix.com.br).
- [09/04] Budamix Central — Domínio antigo `central.gbformulario.com` desativado. Considerar redirect para `central.budamix.com.br` se alguém ainda usa o link antigo.
- [08/04] [[memory/projects/gb-import-hub-schema|GB Import Hub]] — MarineTraffic API key não configurada (fetch-vessel-position retorna dados vazios). Não bloqueante — tracking funciona via Terminal49.
- [08/04] PCM001 — Preço alterado na planilha (R$19,90) mas NÃO alterado nos marketplaces (ML, Shopee, Amazon ainda com R$39,90). Sincronizar se intencional. → [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]]
- [08/04] GB25009 — 70% balanço R$72.232 PENDENTE, vencimento 16/04. Container já finished. **Pagar.**
- [08/04] ~~GB25011 — Numerário R$60.000 vence 11/04~~ → ✅ Pago 11/04. Próximo: 70% balanço R$71.419 vence 24/05.
- [08/04] GB26001/GB26002 — Numerário e 70% sem datas de vencimento definidas no sistema.
- [08/04] GB26002 — Numerário e 70% sem valores registrados no sistema.
- [08/04] Skill [[skills/gb-import-hub/SKILL|gb-import-hub]] instalado e validado (14/15 testes OK). terminal49-fetch-shipment com bug (HTTP 500).

- [09/04] ~~MELI — 22 SKUs com margem negativa após correção com dados reais.~~ → ✅ Superado pela atualização de Ads ACOS real (15/04). Margens recalculadas com dados reais.
- [15/04] Ads ACOS real — 12 SKUs NOVOS negativos após atualização: MELI (4: Kit3Potes, 914A_B, XCP002, SPC013), Amazon (5: 914C_BB, K6CAN250, KIT2CK4742_B, KIT4YW520SQ, KIT4YW800SQ), Shopee (3: KIT2YW320, CNCOL48, CNCOL24/LIVCOL1). **Ação: revisar preços ou pausar Ads desses SKUs.**
- [15/04] Amazon — 26 de 46 SKUs sem ASIN preenchido na planilha. Preencher para poder diferenciar SKUs com/sem Ads corretamente.
- [15/04] ML Ads — 34 de 37 items anunciando SEM buy box. Desperdício potencial de R$8.625/60d. Revisar estratégia Ads com Spark.
- [15/04] ML Ads — 17 items com gasto mas ZERO receita em 60 dias. Pausar ou revisar.
- [15/04] Amazon Ads — KIT2YW520SQ com ACOS 64,8% (R$244 gasto, 7 vendas em 60d). **Pausar urgente.**
- [15/04] ml-ads-automation — Projeto pronto (FastAPI + Supabase `cckfkvqblvundnyphole`) mas nunca deployado. Deploy no Railway + cron N8N pendente.
- [15/04] Shopee Ads — API de Ads inacessível (sem scope "Marketing" no app partner_id 2031533). Solicitar no Shopee Open Platform ou usar export manual CSV.
- [09/04] MELI — Coluna R (FRETE) tem 5-6 células com formatação texto (ex: `08.01`, `09.01`) em vez de moeda. Não afeta cálculo mas visual incorreto. → [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]]
- [09/04] Skill [[skills/update-ml-return-rates/SKILL|update-ml-return-rates]] — validada mas Telegram report ainda não testado (usou --no-telegram). Testar na próxima execução. → [[openclaw/agents/trader/AGENTS|Trader]]
- [10/04] MELI — Custos Full extraídos (57 SKUs, 2866 pedidos). Pendente: atualizar Col N (FULL) da planilha com valores reais por SKU. → [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]]
- [10/04] MELI — API do ML não separa manuseio/armazenagem. O `shp_fulfillment` do MP é o custo único. Documentar na skill [[skills/marketplace/ml-fees-rules/SKILL|ml-fees-rules]].

- [10/04] ✅ ~~DPM001 ML — Cadastrado: MLB6600435126, R$29,90, 150 un, Clássico, Full~~
- [10/04] ✅ ~~DPM001 Shopee — Cadastrado nas 3 lojas (R$39,90, marca Budamix brand_id=5014011)~~
- [10/04] ✅ ~~DPM001 Amazon — ACCEPTED, ASIN B0GWS1151L, DISCOVERABLE~~
- [10/04] ✅ ~~DPM001 — Inserido na planilha nova (4 abas)~~
- [10/04] ✅ ~~Planilha migrada: sync-costs.py atualizado para novo SSID `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU`~~
- [10/04] DPM001 Amazon — Enviar estoque ao CD FBA (inbound shipment via Seller Central). Produto não aparece sem estoque físico.
- [10/04] DPM001 ML — Título auto-gerado "Budamix Redondo Quebra-cabeça Modular Bege" — avaliar se ajusta
- [10/04] Excluir planilha antiga do Drive (`1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`) — **Pedro manualmente** (agente sem permissão)
- [10/04] Documentar product type TRIVET na skill [[skills/amazon-listing-creator/SKILL|amazon-listing-creator]]
- [10/04] ✅ ~~Atualizar skill [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] com novo SSID da planilha~~ → Resolvido 17/04: 3 ocorrências trocadas (`1u74a...` → `1dUoZ...`) em `~/.claude/skills/planilha-precificacao/SKILL.md` (linhas 13, 14, 199).
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — SKILL.md da planilha-precificacao: **SSID atualizado** ✅ 17/04. Ainda pendente no arquivo: documentar conta `gb.ai.agent@gbimportadora.com`, nota sobre `gog` CLI na VPS e scope insuficiente do token local (apenas spreadsheets+drive.file — sem gmail).
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — Bling Matriz: criar natureza de operação "Entrada por importação por conta e ordem" (CFOP 1949) no painel web. Hoje só há "Compra de mercadoria" — usei como fallback para NF 000648. Evita ambiguidade fiscal em próximas importações.
- [17/04] [[projects/canggu|Ana]] — **Auditoria 48 conversas / 151 msgs** concluída (`auditoria-ana-whatsapp-abril2026.md` na raiz do projeto). 60% ✅ / 18% ⚠️ / 18% ❌ / 4% 🔄. **4 dos 5 padrões top já corrigidos** (fantasy product, forbidden promise, away_message, empty-msg loop, meta leak). **Residual ativo**: loop de pergunta sobre canal (site/ML/Shopee) mesmo com cliente já respondendo. → aplicar **Rec 4.1** (anti-loop canal no Passo 4a do BLOCO 4 do `system_prompt`) na próxima janela de ajuste.
- [17/04] [[projects/canggu|Ana]] — **Próxima auditoria: 19/04** (meta <20% erro, pós-fixes de 12/04). Monitorar se fixes (`carry-over threshold 0.2`, `detectEscalationInResponse`, `checkConsecutiveEmptyMessages`, debounce 12s, Regras 13-18) entregaram a redução esperada.
- [17/04] [[projects/gb-import-hub|GB Import Hub]] — **Bling API Matriz OAuth EXPIRADO** — `refresh_token 5936b0387456...` retorna `invalid_grant`. Reautorizar via browser (authorize_url → callback → novo code). Bloqueia integrações Bling Matriz via API (ex: download CC-e, consulta NF). → item OpenClaw Vault 1Password: `Bling API - Matriz (58.151.616/0001-43)`.
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — PATCH /produtos nos 21 SKUs do Bling Matriz (IMB501[CVP] + 18 KITs) preenchendo `classificacaoFiscal: 70134900` e `origem: 2`. Hoje estão vazios no cadastro — o payload da NF injetou no item, mas próximas NFs automáticas falhariam sem esses dados.
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — Preencher `/root/.openclaw/workspace/shared/fisco/config/product-packaging.json` na VPS com peso bruto/líquido por SKU. Arquivo está todo `null`. Bloqueador explícito da skill `bling-nfe` em emissões automáticas futuras.
- [17/04] Bling v3 API — bugs conhecidos a reportar/contornar: `GET /nfe/{id}` e `/naturezas-operacoes/{id}` retornam null mesmo para IDs válidos (listagem com filtros funciona); API **não expõe** CC-e nem cancelamento (só pelo painel web); `POST /nfe` descartou bloco `transporte.volumes[]` do payload (DANFE 000649 saiu com volumes zerados, corrigir por CC-e).
- [10/04] Amazon — SKUs duplicados: IMB501*_T e IMB501T-{cor} apontam para os mesmos ASINs. Investigar e consolidar.
- [10/04] Obsidian — Auditoria profunda de conexões semânticas pendente. Prompt recebido, executar em sessão dedicada.
- [14/04] ✅ ~~Vault — Implementar estrutura proposta para centralização~~ → Executado: 5 fases completas (reestruturação, migração, frontmatter, taxonomia, conexões)
- [14/04] ✅ ~~Máquina — Limpar duplicatas de projetos~~ → Executado: SIMULIMPORT deletado, 4 projetos consolidados em 05-Projetos-Codigo/
- [14/04] ✅ ~~Vault — Migrar vault antigo~~ → Vault antigo scanneado (37 notas), 1 nota migrada (Trades Up), 36 descartadas (calendário obsoleto/leads mortos)
- [14/04] ✅ ~~Vault — Converter Word docs~~ → 6 docs convertidos via pandoc (3 atendimento, 2 OpenClaw briefings, 1 memoria tobias)
- [14/04] Downloads — Limpeza necessária (31 GB acumulados: 1723 PDFs, 1400+ planilhas, 5000+ imagens, 469 vídeos). Maioria são históricos que podem ser arquivados ou deletados.
- [15/04] E-commerce — Testar redesign no mobile real (celular físico). Verificar StickyAddToCart, AnnouncementBar dismiss, fontes Satoshi/Bricolage carregando.
- [15/04] ~~E-commerce — Code-splitting: chunk JS 895KB.~~ → ✅ Resolvido 16/04: React.lazy em 12 rotas (admin, checkout, auth, account, search, tracking). Chunk principal 255KB → 195KB gzip (meta <300KB batida). Commit `ebfebc1`
- [14/04] Vault — Análise semântica profunda (subfase 5.3): ler todos os batches de notas e encontrar conexões ocultas. Adiada para sessão futura.
- [13/04] Amazon Request Review — Monitorar taxa de sucesso pós-fix por 7 dias. Meta: >70% sucesso. Verificar logs diários até 20/04. Backfill de ~4866 pedidos em execução.
- [13/04] ~~Budamix Central Live Sales — Validar layout TV na TV física do escritório.~~ → ✅ Resolvido 13/04: fix dvh viewport (desconta chrome browser), compressão seções desktop, min-h gráfico
- [13/04] ~~Estoque Budamix — Conectar com planilha real e testar fluxo completo.~~ → ✅ Resolvido 13/04: planilha conectada, fix parseInt milhar, fix col_brand, 4 operações reprocessadas
- [13/04] Estoque Budamix — Validar layout mobile (equipe usa celular no armazém)
- [13/04] DPM002 ML (MLB6611643028, R$34,90 Premium) — Registrar no Supabase (item_id, SKU, categoria, preço, data). Aguardando aprovação Pedro.
- [14/04] ✅ ~~DPM002 Amazon — ACCEPTED, ASIN B0GX7RN9FS, DISCOVERABLE~~
- [14/04] ✅ ~~DPM002 Amazon — 8 fotos uploadadas (Supabase Storage → Amazon CDN, todas processadas)~~
- [14/04] DPM002 Amazon — Enviar estoque ao CD FBA (inbound shipment via Seller Central). Produto não aparece sem estoque físico.
- [15/04] ✅ ~~Ponto Certo — Timer Android não funciona (não aparece ou não atualiza)~~ → Fix: loading error path + startTime race condition + visibilitychange. Deploy VPS via SCP
- [15/04] Ponto Certo — Token GitHub na VPS inválido (`gh auth` expired). `git pull` falha em `/var/www/ponto-certo`. Deploy feito via SCP como workaround. Reautenticar: `ssh root@187.77.237.231 "gh auth login -h github.com"`
- [15/04] Ponto Certo — Projeto copiado de `/tmp/` para `~/Documents/05-Projetos-Codigo/ponto-certo/` (repositório persistente)

- [15/04] ✅ ~~Amazon — Custos suspeitamente baixos em 4 SKUs~~ → PCM001 (R$1,04) e DPM001 (R$2,39) confirmados corretos (MDF). KIT4YW520SQ e KIT4YW800SQ corrigidos.
- [15/04] ✅ ~~Amazon — Verificação custos AMAZON vs ESTOQUE~~ → 11 custos corrigidos na Col F. TL250x confirmados como kits de 6 (R$22,80 correto).
- [15/04] Amazon — **3 SKUs com MARGEM NEGATIVA após correção de custos.** Decisão pendente do Pedro:
  - KIT4YW520SQ: custo R$21,70, venda R$39,90, lucro **-R$1,00 (-3%)**
  - KIT4YW800SQ: custo R$27,11, venda R$39,90, lucro **-R$6,41 (-16%)**
  - KIT4YW1520: custo R$44,39, venda R$64,90, lucro **-R$7,64 (-12%)**
  Opções: aumentar preço, reduzir kit, migrar pra DBA/FBM, ou descontinuar FBA.
- [15/04] Amazon — 914C_BB com margem 6% (custo corrigido R$0→R$18,48). Avaliar preço.
- [15/04] Amazon — Linha 28 (KIT2WX11975_) sem preço de venda. Preencher ou remover. Marcada com fundo amarelo na planilha.
- [15/04] Amazon — Quando promoção FBA+ expirar (jul/2026): trocar flag I1 para PADRAO e criar tabela de lookup com tarifas FBA padrão por peso×preço. Produtos <R$40 ficam inviáveis no FBA sem promoção.

- [15/04] Amazon Ads — Mapeamento completo: 139 campanhas (48 ativas, 91 pausadas), 12 grupos × 4 camps, ACOS geral 22,9%, R$4.884 gasto 60d, R$21.317 vendas 60d. Relatório: `investigacao_estrategia_150426.json`
- [15/04] ✅ ~~Amazon Ads — Otimização cirúrgica 4 ações executadas:~~
  - ✅ AÇÃO 1: Canequinhas Café bids reduzidos (58 keywords: Descoberta -50%, Alcance -50%, Exact -40%)
  - ✅ AÇÃO 2: 16 negativas campaign-level adicionadas (caneca, xicara, xícara, marmita, marmita de vidro) em 8 campanhas. Override G1 autorizado (termos protegidos com R$270 gasto zero vendas)
  - ✅ AÇÃO 3: Potes Tampa Bambu Alcance PAUSADA (ACOS 62,8%)
  - ✅ AÇÃO 4: Abraçadeiras Nylon (4 camps) + Redinha Frutas (4 camps) PAUSADAS (zero vendas/tráfego 60d)
  - 83 ações logadas no Supabase `amazon_ads_actions_log`
  - Campanhas ativas: 48→39. Budget diário: R$315→~R$274
- [15/04] Amazon Ads — **Revisão 29/04/2026**: Medir impacto das ações 1-3 (meta ACOS ≤19%)
- [15/04] Amazon Ads — **Revisão 15/06/2026**: Reavaliar Abraçadeiras e Redinha (Ação 4)
- [15/04] Amazon Ads — Canequinhas Café ACOS 45,5% — monitorar queda pós-bid reduction (meta ≤25% em 14d)
- [15/04] Amazon Ads — 91 campanhas pausadas são lixo histórico (Era 1: 2022-2025). Considerar arquivar
- [15/04] Amazon Ads — 157 keywords PHRASE ainda existem — possível resquício legacy problem
- [16/04] Amazon Ads — **BidSpark-3 Piloto** rodando no grupo Suporte Controle Gamer. Revisão formal 30/04. Metas: ACOS <15%, 0 bleeders, funil normalizado, budget utilization >30%
- [16/04] Amazon Ads — Fase 1 Escalação executada: 3 bids subidos (suporte para controle ps5 R$0,55→R$0,80, suporte controle R$0,35→R$0,45, porta controle R$0,35→R$0,45). Monitorar: utilização Performance >80% → subir budget pra R$35. ACOS >17% 3d → revisar
- [16/04] Amazon Ads — SPC013 (B0GTQXRDTM, ASIN novo cru) adicionado às 3 campanhas, mesmo ad group que SPC002. Product ad duplicata PAUSED no Alcance (sem impacto)
- [16/04] Amazon Ads — Coleta diária falhando em 2 dias (12/04, 15/04). Investigar cron N8N
- [17/04] [[projects/gb-import-hub|GB Import Hub]] — Edge Function `poll-terminal49` não atualiza `vessel_tracking.pod_ata` quando recebe milestone `vessel_arrived` e não bumpa `last_api_call`. Milestones são gravados OK, só os campos derivados ficam stale. Descoberto ao rodar poll no GB25010 (17/04 15:35 UTC). Não bloqueia operação, mas confunde dashboards que leem `pod_ata` como sinal de chegada.
- [17/04] [[projects/gb-import-hub|GB Import Hub]] — Skill `skills/gb-import-hub/SKILL.md` tem comando errado para extrair credencial do 1Password (`--fields password` retorna vazio em itens tipo "API Credential"). Corrigir para `--fields credential`. Descoberto ao rodar PNI do GB25010.
- [17/04] [[projects/canggu|Ana]] — Tarefa 4 pendente: sync `product_listings` ↔ ML. 13 MLBs stale no banco (ML desativou mas `is_active=true` no DB) + 44 MLBs ativos no ML sem entry no banco. Inclui os 7 MLBs da família Canelada 250ml (CAC250) que agora tem base_product no banco. Script precisa fazer de-para título→product_id + UPSERT. ~30-60min.
- [17/04] [[projects/canggu|Ana]] — Cadastrar 12 SKUs individuais por cor que só existem na planilha, não em `products`: CAR200 (B,P,VD,AZ,AM,R) e TL250 (V,P,Z,R,A,B). Sem cadastro, impossível criar `color_variant` relations para essas 2 famílias. Hoje a cor para a Ana vem só via `base_products.color` (texto), não dá pra recomendar SKU específico. ~15min.
- [17/04] [[projects/canggu|Ana]] — Criar trigger pg_net para `response_corrections` análogo ao `trg_base_product_embedding_sync` (criado 17/04). Hoje re-embedding das correções só dispara via chamada manual à Edge Function `process-correction-embedding`. Risco: correção editada via SQL fica stale. ~10min.
- [17/04] Budamix E-commerce — Sync estoque planilha → Supabase: script Apps Script criado mas falta instalar na planilha. Pedro precisa colar a service_role key e rodar installTrigger(). Doc em docs/SETUP-STOCK-SYNC.md. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Testes de pagamento real pendentes: cartão aprovado, cartão recusado, PIX, estoque insuficiente, frete zerado via DevTools, webhook spoofing. Checklist completo em AUDITORIA-CHECKOUT-MP.md seção 5. → [[projects/budamix-ecommerce]]
- [17/04] ✅ ~~Budamix E-commerce — Reviews reais dos marketplaces~~ → **Feito**: tabelas `product_reviews` + `review_photos` + RLS + bucket Storage `reviews` + 42 fotos uploadadas + 15 reviews seedados (7 SKUs). Home + PDP consumindo via queries React Query. Seção PDP unificada bg-primary teal + cards white/[0.08], fotos clicáveis → MediaLightbox. Commits `54fbef3`, `a0f95a9`, `2742168`, `ebcd852`, `1fb243e`.
- [23/04 noite] ✅ ~~[[projects/budamix-ecommerce|Budamix Ecommerce]] — Páginas /faq, /contato, /termos, /trocas-e-devolucoes eram NotFound mascarado (200 via SPA mas conteúdo 404)~~ → **Resolvido em `5a1837b`.** Criadas como stubs `<ComingSoon>` (lazy-loaded, `noindex,nofollow`, hero Teal + `<SoonBadge variant="card">` + CTA `/loja`). Conteúdo real ainda pendente (🟡 bloqueia Meta Ads). → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Páginas com conteúdo real pendentes: /sobre (hoje só 2 linhas placeholder), busca melhorada, dark mode. Issues detalhadas em budamix-issues-fase7.md. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — variant.name ainda é 'Padrão' em 19 variants. Se frontend usar pra seletor de cor/volume na PDP, precisa sincronizar nomes descritivos. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Stock placeholder (=100) em 19 variants. Sync inicial da planilha vai zerar os sem quantidade. Confirmar que planilha está atualizada antes de rodar. → [[projects/budamix-ecommerce]]
- [23/04 noite] ✅ ~~Budamix E-commerce — Push pendente: ~80 commits locais à frente de origin/main~~ → **RESOLVIDO.** Ver bloco 🔴 Críticas acima. 113 commits totais em prod nesta sessão (111 do push inicial + 2 ajustes mesmo dia).
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Integração GitHub→Vercel inexistente** (`GET /repos/PHPB2025K/budamix-ecommerce/hooks → []`). Toda atualização futura exige `vercel --prod --yes` manual após push. Candidato a missão separada (Opção B do Pedro — 15 min OAuth: Vercel Dashboard → budamix-ecommerce → Settings → Git → Connect Git Repository → GitHub). → [[projects/budamix-ecommerce]]
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Newsletter form não persiste email**: `src/components/home/NewsletterSection.tsx` submit handler usa `console.log('[newsletter] subscribe', { email })` + `toast.success` fake. Email nunca chega a backend. Hook `useEffect` + supabase insert (ou Resend/ConvertKit) pendente. → [[projects/budamix-ecommerce]]
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Conteúdo real das 4 páginas stub** (/faq, /contato, /termos, /trocas-e-devolucoes). Hoje renderizam `<ComingSoon>` com `noindex`. Bloqueia Meta Ads e gateways. Quando escrever, remover `setNoIndex()` da ComingSoon e migrar cada uma para página própria. → [[projects/budamix-ecommerce]]
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Bundle 708 kB ainda acima do limite de 500 kB.** Chunk principal `index-*.js` 708.21 kB (gzip 206.70 kB). Vite warning persistente. Features novas (reviews, admin drag-n-drop, HeroBanner carousel) podem lazy-load para reduzir. → [[projects/budamix-ecommerce]]
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Slide 2 HeroBanner "potes-vidro" removido temporariamente** em `a2c525b`. Código do carousel preservado, array `SLIDES` reduzido a 1 entrada, asset `public/images/hero-potes-vidro.png` mantido no repo. Para reativar: restaurar o objeto removido do array. → [[projects/budamix-ecommerce]]
- [23/04 noite] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Backup branch `backup-pre-push-20260423-200452`** preservada por 24-48h. Pode deletar após validação visual (`git branch -D backup-pre-push-20260423-200452`). → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — FREE_SHIPPING_THRESHOLD hard-coded em 4 lugares do frontend (19900). Deveria ler do site_settings. Hook useSiteSettings pendente. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Reversão de estoque em cancelamento/reembolso não implementada. Se order muda pra refunded/cancelled após paid, stock não volta. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Fluxo de avaliação pós-entrega: e-mail automático após entrega com link pra avaliar cada produto (estrelas + texto + upload fotos), token sem login, moderação no admin (active=false→true). Implementar após lançamento. → [[projects/budamix-ecommerce]]
- [17/04] [[projects/canggu|Ana]] — `supabase/seed.sql` do repo `budamix-ai-agent` está stale: nome "Giovana", ~7727 chars. Fonte de verdade (banco `jpacmloqsfiebvagfomt` agent_config.system_prompt) tem "Ana" e 19454 chars após aplicação das 3 recomendações da auditoria 17/04. Sincronizar seed pra evitar regressão se alguém rodar `supabase db reset` local.

## ⚪ Backlog (sem urgência imediata)

- Antidumping cerâmicas chinesas — pesquisar Vietnam e Índia como alternativas de sourcing
- TikTok Shop — definir estratégia de outreach MCN/afiliados
- ~~Stripe — ativar modo produção (está em teste)~~ → ✅ Stripe removido, migrado para Mercado Pago (14/04)
- Container isolation — OpenClaw roda direto no host, considerar Docker
- ~~E-commerce budamix.com.br — Migrado para Vercel + Supabase próprio.~~ → ✅ DNS propagado, MP produção ativo, checkout testado (Pix + Cartão + Débito). **Pendente:** configurar webhook MP manualmente no painel Developers. → [[projects/budamix-ecommerce]]
- [14/04] E-commerce — Configurar webhook URL `https://ioujfkrqvporfbvdqyus.supabase.co/functions/v1/mp-webhook` no painel MP Developers. **Pedro manualmente.**
- [14/04] E-commerce — Testar pagamento Pix real (valor baixo) para validar QR code + webhook + order no Supabase
- Fornecedores China — triagem emails Yiwu automatizada
- Kit duplo porta-copos (12 peças + 2 suportes) a R$69,90-79,90 para Shopee — diluir taxa fixa

---

## ✅ Resolvidas (Abril 2026)

- [20/04] ✅ **PDP em prod não renderizava** (React error #310, Rules of Hooks) — cherry-pick do fix 17/04 (`62aa9e1`) em branch hotfix saindo de `origin/main` → PR #1 → merge → deploy via `vercel --prod` após resolver bloqueio de commit author (git config global + empty commit). Prod DESBLOQUEADA 20/04 14:04 UTC. 3/3 PDPs renderizando com 0 console errors. Commits `1dd78cb` + `135570e` em origin/main. Knowledge: [[knowledge/concepts/vercel-hobby-commit-author-block]].
- [20/04] ✅ **Admin não salvava imagem de diferenciais** — coluna `products.differentials_image_url` não existia no Supabase remoto (migration local `20260418_product_differentials_image.sql` nunca aplicada). DDL aplicado direto via Supabase Management API. Admin volta a salvar.
- [20/04] ✅ **3 produtos MDF cadastrados** — PCM001, DPM001, DPM002 via API ML no Supabase Budamix. 24 fotos em Storage, descrições reescritas no padrão Budamix (Proteja/Organize + bullets técnicos). Commit `10861d6` em `main` local.
- [17/04] ✅ Estratégia fiscal v2.0 (90/10) instalada como fonte de verdade — PDF oficial atualizado + nota-índice `business/importacao/estrategia-fiscal-gb.md` + propagado em CLAUDE.md vault/global e Fisco IDENTITY/skills. Commit `c124771`.
- [17/04] ✅ NF Transferência GB25011 Matriz→Filial emitida — 000648 (entrada 580012) + 000649 (transferência 90/10, CFOP 6152) autorizadas SEFAZ-SC cStat=100. DANFE PDF + XML em `~/Documents/01-Importacao/GB25011-NF-TRANSFERENCIA/`. Log em `openclaw/agents/kobe/shared/fisco/memory/nfe-log.md` (commits `3779898`, `226469f`).
- [17/04] ✅ Planilha oficial de estoque atualizada com GB25011 — 21 SKUs (+9.984 un). Fonte de verdade confirmada: SSID `1dUoZ...` "PLANILHA DE ESTOQUE / PREÇO", acesso via `gb.ai.agent@gbimportadora.com` + `gog` na VPS. Guardrail aplicado: validação de SKU real na col B antes de writes evitou corromper saldo (Pedro havia passado linhas com offset +14).
- [15/04] ✅ Investigação ACOS real por SKU — 3 plataformas auditadas. ML Ads API funcional (345 ads, ACOS 11,4%), Amazon Ads API funcional (47 ASINs, ACOS 20,4%), Shopee sem acesso API Ads.
- [15/04] ✅ Ads flats atualizados nas 3 abas — MELI Col Q 6%→11%/0%, AMAZON Col N 8,9%→20%/0%, SHOPEE Col O 5%→7%. Backups criados. Skill planilha-precificacao atualizada.
- [15/04] ✅ Auditoria MELI — 43 SKUs auditados, Col J 11,5%/13%, Col R 3 zerados, Col U padronizada (43 linhas), Col R formatação corrigida.
- [15/04] ✅ Auditoria Amazon — 46 SKUs auditados, 7 correções aplicadas no Google Sheets via API: Col H 12% (23 de 20%→12%, 2 de 14%→12%, 10 hardcoded→fórmula), Col N ads corrigido (6 #REF!, 24 refs fantasma, 9 refs cruzadas), Col O devoluções padronizado, Col P parcelamento criada (1,5% ≥R$40), Col I flag promo FBA+ (IF ≥100→0, <100→5), backup AMAZON_BACKUP_150426
- [15/04] ✅ Skill planilha-precificacao atualizada com estrutura aba AMAZON + regras de negócio Amazon 2026
- [15/04] ✅ Auditoria Shopee — 72 SKUs auditados, 4 correções aplicadas direto no Google Sheets via API (Col H escalonada, Col I zerada, Col S taxas reais, Col U unificada com afiliado)
- [15/04] ✅ Google Sheets OAuth — Acesso de escrita configurado, token persistente em ~/.config/google-sheets-claude/token.json
- [15/04] ✅ Skill planilha-precificacao criada (~/.claude/skills/planilha-precificacao/SKILL.md)
- [15/04] ✅ SOP upload Drive documentado (segundo-cerebro/automacoes/sops/upload-planilha-drive.md)
- [15/04] ✅ E-commerce budamix.com.br — Redesign completo com identidade Budamix (Granado + Great Jones inspired). 5 agentes, 39 arquivos, deploy Vercel produção. → [[projects/budamix-ecommerce]]
- [15/04] ✅ Skills frontend/e-commerce — 5 agentes multi-agent criados (.claude/agents/) para redesign pipeline reutilizável
- [06/04] ✅ Budamix Central — Reestruturação dados produtos completa (5 fases)
- [06/04] ✅ Budamix Central — Pipeline vetorial da Ana funcionando (5/5 testes)
- [06/04] ✅ Budamix Central — Bug envio WhatsApp humano→cliente corrigido
- [06/04] ✅ Budamix Central — Links de marketplace adicionados ao formulário de produto
- [06/04] ✅ Budamix Central — Guia de preenchimento para analistas criado e entregue
- [06/04] ✅ Segundo Cérebro — Setup inicial configurado
- [06/04] ✅ OpenClaw — Migração completa dos 5 sub-agentes para GPT 5.4 / GPT 5.1-mini
- [06/04] ✅ OpenClaw — Atualizado de v2026.4.2 para v2026.4.5
- [07/04] ✅ OpenClaw — Fix fallback cascata: todos agentes com anthropic/claude-haiku-4-5 como fallback
- [07/04] ✅ ML — Anúncio Kit Porta-Copos MDF Budamix criado (MLB6583127234, R$39,90, gold_special)
- [07/04] ✅ Shopee — Anúncio replicado nas 3 lojas (budamix-store, budamix-store2, budamix-shop)
- [07/04] ✅ Shopee — Skill shopee-listing-creator criada no workspace do Kobe
- [07/04] ✅ Shopee — Análise completa de taxas + concorrência salva em memory/projects/shopee-porta-copos-analise.md
- [07/04] ✅ Bright Data — Zona web_unlocker1 criada e testada (API key: e0f949a4...)
- [07/04] ✅ Amazon BR — Listing PCM001 ACCEPTED via SP-API (0 erros, ASIN pendente)
- [07/04] ✅ Amazon BR — Skill amazon-listing-creator criada e deployada na VPS
- [07/04] ✅ Shopee — Anúncio atualizado com 6 atributos + descrição formatada (budamix-store)
- [07/04] ✅ Shopee — Replicado para budamix-store2 (48508383354) e budamix-shop (41429832718)
- [08/04] ✅ GB Import Hub — Migração completa para Supabase externo (schema + dados + functions + storage + SSL)
- [08/04] ✅ GB Import Hub — 17 Edge Functions deployadas, 10 secrets configurados
- [08/04] ✅ GB Import Hub — Webhook Terminal49 atualizado para novo endpoint
- [08/04] ✅ GB Import Hub — 27 documentos do storage migrados com URLs atualizadas
- [08/04] ✅ GB Import Hub — Frontend online em https://import.budamix.com.br (SSL Let's Encrypt)
- [08/04] ✅ GB Import Hub — Login criado (pehpbroglio@gmail.com)
- [08/04] ✅ GB Import Hub — Mapbox token fix (get-mapbox-token deployada com --no-verify-jwt)
- [08/04] ✅ Skill spreadsheet-pricing criada e deployada (mapeamento 4 abas, 40 fórmulas protegidas)
- [08/04] ✅ PCM001 inserido na planilha de estoque (4 abas: MELI, SHOPEE, AMAZON, ESTOQUE)
- [08/04] ✅ Skill gb-import-hub v2 — regras de negócio (ciclos independentes, status derivado, alertas financeiros)
- [08/04] ✅ Sync unidirecional Segundo Cérebro → Kobe configurado (cron 06:45 BRT, git pull read-only)
- [08/04] ✅ AGENTS.md do Kobe atualizado com instrução de boot para ler segundo-cerebro
- [08/04] ✅ Live Sales — Gráfico dual axis (Pedidos Hoje/Ontem + Faturamento R$)
- [08/04] ✅ Live Sales — Thumbnails no ranking (11 SKUs populados via ML API, 100% cobertura)
- [08/04] ✅ Live Sales — Estoque com alertas visuais (<10 warning, <3 danger)
- [08/04] ✅ Live Sales — Indicador pulsante vermelho (CSS animation)
- [08/04] ✅ Live Sales — API route expandida (dados ontem, thumbnails, estoque)
- [09/04] ✅ Zero Anthropic — Limpeza completa: AGENTS.md (18), IDENTITY.md (5), MEMORY.md (5), SOUL.md (4), Builder (2), handler.ts (1), RH workspace (8). Total: 43 refs removidas
- [09/04] ✅ Fallback chain — Opção C: gpt-5.1-mini → haiku (todos 6 agentes + defaults)
- [09/04] ✅ Doctor warnings — chmod 600, 108 orphans arquivados, WhatsApp OK
- [09/04] ✅ RH — Auditoria completa + deploy v2 (SOUL, AGENTS, SKILL comunicacao)
- [09/04] ✅ RH — Cron Monitor Ponto Semanal criado (segunda 10h BRT)
- [09/04] ✅ RH — Tabela comunicacoes_rh criada no Supabase Ponto Certo
- [09/04] ✅ RH — Migração Ponto Certo confirmada (10 tabelas, 855 registros, config updated)
- [09/04] ✅ Amazon Request Review — Fix: batch 35, timeout 420s, persistência review_requested_at, tratamento timing
- [09/04] ✅ Amazon Request Review — Migration SQL: coluna review_requested_at + index
- [13/04] ✅ Amazon Request Review — Fix definitivo: delivered_at + Opus 4.6 + timeout 600s + alertas + backfill
- [13/04] ✅ Budamix Central Live Sales — Layout TV zero-scroll (h-screen + overflow-hidden + flex)
- [13/04] ✅ Budamix Central Live Sales — Fix mobile regression (classes condicionais lg:)
- [09/04] ✅ Budamix Central — Login Simone criado (simoneperon@uol.com.br, role viewer)
- [09/04] ✅ Budamix Central — Role-based access implementado (admin/viewer, middleware + API)
- [09/04] ✅ Budamix Central — Domínio migrado para central.budamix.com.br (SSL Let's Encrypt)
- [09/04] ✅ Budamix Central — Report enviado no Thread 13 Telegram
- [14/04] ✅ E-commerce budamix.com.br — DNS propagado (76.76.21.21), HTTP 200, Vercel GRU
- [14/04] ✅ E-commerce — MP credenciais produção ativadas (Supabase secrets + Vercel env vars)
- [14/04] ✅ E-commerce — .env removido do git tracking + adicionado ao .gitignore (segurança)
- [14/04] ✅ E-commerce — Fix public key whitespace (SDK MP rejeitava)
- [14/04] ✅ E-commerce — SPA routing corrigido (vercel.json com rewrites)
- [14/04] ✅ E-commerce — Pix habilitado no Payment Brick (bankTransfer: 'all')
- [14/04] ✅ E-commerce — Checkout testado: Pix (formulário + e-mail), Cartão (iframe MP), Débito Virtual CAIXA
- [14/04] ✅ Skills frontend/e-commerce — 105 skills auditadas e instaladas (63 designer, 29 designpowers, 4 ui-skills, 3 Vercel, 1 Medusa, 1 Stripe, 4 custom)
- [14/04] ✅ Skills — 4 custom skills criadas (ecommerce-design-system, product-page, checkout, seo)
- [14/04] ✅ Skills — Documentação no Obsidian (inventário + auditoria + guia de uso)
- [14/04] ✅ CLAUDE.md global atualizado com pipeline de skills frontend/e-commerce
- [17/04] ✅ Ana restaurada após 8 dias de downtime — 9 placeholders `SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER` / `WHATSAPP_API_KEY_PLACEHOLDER` hardcoded nos 8 Code nodes do workflow `KE7YVXayl5ntjwQk` foram substituídos por chaves reais. Última msg antes: 09/04 19:31. Execução 93145 em 17/04 09:49 UTC confirmou recuperação (Ana respondeu em 9.2s, 12.586 tokens). Evolution Cloudfly + Supabase Cloud + Anthropic/Groq todos saudáveis — problema era só de placeholders nunca substituídos no deploy de 12-13/04.
- [17/04] ✅ ML Questions workflow `g4JxNpC2sP9K8c71` restaurado — 8 placeholders (`YOUR_SUPABASE_SERVICE_ROLE_KEY` x4, `YOUR_ML_APP_ID` x2, `YOUR_ML_CLIENT_SECRET` x2) substituídos por valores reais do workflow irmão `sg2yU46R9EQq3a2v` (ML Messages). O 401 "token ML expirado" era na verdade Supabase 401 por placeholder. Execução 93166 success em 17/04 10:02 UTC. Polling 2min voltou a funcionar; refresh OAuth automático via `marketplace_tokens` intacto.
- [17/04] ✅ Ana `linkPreview: true` → `false` nos 2 `axios.post('/message/sendText/...')` do node Send WhatsApp Response. Elimina a bolha de loading que aparecia quando msg da Ana contém URL (preview OG atrasava renderização).
- [17/04] ✅ Health Check `DEjLkJcllQEmrcLF` refatorado de 11 nodes → 2 (Schedule 15min + Run Health Checks). 4 checks concretos agora: Supabase auth (upsert probe), Ana sem responder há 2h+, Evolution state, erros do workflow principal <30min. Alerta via **WhatsApp** (5519993040768, pessoal do Pedro, NÃO o da Ana 5519992979490). Dedup 30min. Validado happy path (exec 93174 success silencioso) + failure simulada (exec 93178 com `alert_sent=true`).
- [17/04] ✅ Ana — RPC `search_corrections(vector, float, int)` criada no Supabase via migration `20260417120100`. Antes chamada por `process-ml-question` retornava 404; agora retorna matches. 9 correções cadastradas e 100% com embedding.
- [17/04] ✅ Ana — Feedback loop integrado no pipeline WhatsApp. `_shared/embeddings.ts` ganhou `searchCorrections()`. `_shared/context-builder.ts` chama threshold 0.85. `_shared/response-generator.ts` injeta bloco "CORREÇÕES APRENDIDAS". Deploy confirmado: pergunta "Voces tem o pote 1050ml na cor branca?" → Ana responde exatamente com o conteúdo da correção cadastrada ("disponível apenas na tampa azul-petróleo").
- [17/04] ✅ Ana — Trigger `trg_base_product_embedding_sync` (pg_net) criado via migration `20260417120000`. Antes re-embedding de `base_products` só acontecia quando analista salvava pelo Budamix Central UI. Agora UPDATE de qualquer origem (SQL, seed, API) dispara `sync-base-product-embedding` (extendida para aceitar `{baseProductId}` além do batch). Validado: hash do embedding muda em 3s após PATCH em `description_short`.
- [17/04] ✅ Ana — Opção A da migração N8N Credentials aplicada no workflow `KE7YVXayl5ntjwQk`. Credential `Budamix Supabase (Ana)` (httpHeaderAuth, id `Yc25vX9mtZ8oM018`) criada via API. Novo node "Setup Credentials" lê as 5 chaves; 7 Code nodes + Send WhatsApp Response leem via `$('Setup Credentials').item.json.*` com guard clause `[GUARD]`. `Process Message (AI)` HTTP node usa credential (chave sai 100% desse node). SRK ocorrências no JSON: 9→1, WAK: 2→1. Backup em `~/budamix-wf-pre-credentials-20260417-0837.json`.

---

- [17/04] ✅ GB25010 PNI registrada — 22 itens inseridos em `finance_numerario_itens` somando R$64.136,40 (bate exato com total geral). `finance_pagamentos` atualizado (value 72.305,25→64.136,40; USD 13.515,00→12.876,64; rate 5,35→4,9806). Mapeamento categórico validado. Próximo: pagar 20/04.
- [17/04] ✅ GB25010 status atualizado `maritime`→`customs` após poll Terminal49 confirmar `vessel_arrived` 15/04 12:30 UTC + `vessel_discharged` 16/04 11:57 UTC em BRIOA (Itapoá). Container em zona primária, aguardando desembaraço.
- [17/04] ✅ Ana — 2 correções canequinha 100ml azul **reescritas** após descoberta de que azul não existe para essa família (confirmado via ML API em MLB3343832496: `variations=0`, attr COLOR=Amarelo + planilha oficial: só B/BAB/BAV/BAP). Novo conteúdo redireciona para Tulipa 250ml Azul ou Canelada 250ml Azul (ambas têm estoque). Risco de Ana prometer produto inexistente neutralizado.
- [17/04] ✅ Ana — Mapeamento ML completo: 52 anúncios ativos, só 5 usam `variations[]` internas (Palmeira Yucca, Bambu, Jogo Potes 5 Claro, Suporte Gamer, Livro Colorir); padrão dominante é anúncios separados por cor. 13 MLBs stale no banco e 44 MLBs no ML sem entry no DB — pendência de sync criada.
- [17/04] ✅ Ana — Cores populadas em 5 base_products (`color` + tag "múltiplas cores" + linha em description_short). BP_CAN100 com 4 cores (sem azul, conforme planilha), BP_CAR200/TL250 com 6 cada, BP_SPC com 3. Hash do embedding mudou em todos os 5 = re-embedding disparado automaticamente pelo trigger criado hoje.
- [17/04] ✅ Ana — `BP_CAC250` (Canelada Porcelana 250ml) criado do zero — não existia como base_product desde a Fase 2 da reestruturação (06/04). 7 products linkados (K6CAN250 kit + 6 cores individuais CAC250 B/P/R/AZ/VD/AM reativados de inativos). Embedding gerado (hash fda34a19b0).
- [17/04] ✅ Ana — 3 products 914C reativados (BAB/BAV/BAP, estoque 4/10/2 un na planilha) + linkados a BP_CAN100 (base_product_id estava NULL).
- [17/04] ✅ Ana — 8 relations `color_variant` criadas em `product_relations`: BP_CAN100 pivô=914C_B (3 relations) + BP_CAC250 pivô=CAC250B (5 relations). Total color_variant no banco: 8 → 16.

---

*Atualizado: 22/04/2026 — sessão tarde 2 (Fase 1 INVESTIGAR B0GWG2HL56 Porta-Copos MDF)*

---

## 🟡 Importantes — adicionados 22/04 tarde 2

- [22/04] [[projects/amazon-ads-automation|Amazon Ads]] — **BidSpark-3 novo grupo "Porta-Copos MDF" (ASIN B0GWG2HL56)** pausado na Fase 1→2. Produto: kit 6 porta-copos + suporte MDF, R$19.90 (de R$39.90) no site Budamix. Bloqueadores pendentes com Pedro antes de Fase 2 PLANEJAR: (a) **Listing ACTIVE + estoque ≥30 FBA/FBM** na Seller Central — forte suspeita de inativo (ausente tanto em `amazon_ads_catalog` quanto em Central `products` apesar de Central ter sync contínuo); (b) **SKU interno real + margin_pct real** da planilha de precificação — tabela `products` do budamix-ecommerce não tem colunas sku/asin, Central tampouco tem listing Amazon desse produto. Decisões de budget/seed do Pedro (20/04 tarde 2): budget R$30/d (não R$20), seed broad 8-12 keywords obrigatória (sem seed queima 2-3 semanas), ACoS target 20% default, nome grupo `Porta-Copos MDF`. Sem (a) e (b), criar campanha é desperdício. Seed sugerida: porta copo mdf, descanso copo madeira, porta copo decorativo, porta copos mesa, porta copo madeira, base copo mdf, suporte copo decorativo, porta copo artesanal.

---

## Ver também

- [[memory/context/deadlines|Deadlines — Prazos relevantes]]
- [[memory/context/decisoes/2026-04|Decisões — Abril 2026]]

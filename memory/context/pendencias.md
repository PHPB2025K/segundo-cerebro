---
title: "pendencias"
created: 2026-04-26
type: tracker
agent: kobe
status: active
tags:
 - agent/kobe
 - memory
---
# Pendências Ativas

> Marco operacional definido por Pedro em 04/05/2026: remover completamente das pendências/inconformidades tudo referente a abril/2026. Pedro vai regularizar abril; a fila passa a contar a partir de 04/05, primeiro dia útil pós-refatoração. Registros históricos permanecem apenas em sessões/decisões, não como pendência ativa.

_Atualizado: 2026-06-08 ~11h BRT — Meta Ads Budamix Campanha 1 ATIVADA em produção com R$20/dia (vídeo v2 safezone + copy v4 multiuso, público mulheres BR). Campanhas 2 e 3 PAUSED aguardando vídeos 2 e 3._

## 🟢 Meta Ads Budamix — Campanha 1 ATIVA, Camps 2+3 pendentes

- ✅ ~~**Pedro coloca app KOBE.OPENCLAW em modo Live**~~ → **RESOLVIDO 08/06** — pré-requisito pra criar creative via Marketing API (estava em Development e bloqueava). URL privacidade `https://budamix.com.br/` + categoria "Negócio e Páginas" + portfólio Budamix conectado.
- ✅ ~~**Upload vídeo 1 + criar ad Campanha 1 + ativar**~~ → **RESOLVIDO 08/06** — Claude fez end-to-end via API: vídeo v2 (`1765886834776880`, overlays safezone 1:1), creative v4 (`4446773825645879`, copy multiuso sem borossilicato), ad `120248522531400402` ATIVO. Budget reduzido R$37 → R$20/dia conforme pedido do Pedro.
- ✅ ~~**Pedro revisa criativo + público**~~ → **APROVADO 08/06** — vídeo aprovado (após 1 iteração de safezone) + copy ajustada 2x (sem borossilicato + foco multiuso) + targeting mulheres aplicado.
- [ ] **Pedro produz vídeos 2 e 3** (UGC Testemunho ~18s + Antes/Depois 12-15s). Tentativa inicial com IA (Veo 3 / Higgsfield); fallback é gravar com celular vertical. Pedro disse "vou finalizar e te envio aqui". Sem deadline rígido.
- [ ] **Quando vídeos 2 e 3 chegarem:** Claude faz upload via API + cria 3 ads na Camp 2 (3:2:2 ou simplificado) + 1 ad na Camp 3 + ativa as duas. Token Graph Explorer expira ~1h — Pedro precisa gerar novo no momento.
- [ ] **Criar 2 Custom Audiences (WCA)** pra Campanha 3: ViewContent 14d + Purchase 30d. Tool MCP estava bloqueada em 06/06 e 08/06 ("This tool is new and is being gradually rolled out across ad accounts"); tentar de novo com token user no próximo ciclo. Se ainda bloquear, Pedro cria manual no Audience Manager.
- [ ] **NÃO TOCAR na Campanha 1 nos próximos 7-14 dias** (até 22/06). Mudança >20% em budget/público/criativo reseta fase de aprendizado. Próxima janela pra ajustar budget é depois que sair da fase.
- [ ] **(Futuro 2-3 sem)** Lista de compradores de marketplace (Amazon BR + ML + Shopee) pra criar Custom Audience DFCA + Lookalike 1-3% — Pedro vai conseguir via empresa parceira na semana de 09/06.
- [ ] **(Futuro mês 3+)** Migrar Campanha 3 de WCA pra DPA (Dynamic Product Ads com catálogo dinâmico) quando pixel tiver maturidade (~30-50 vendas/mês).
- [ ] **(Futuro/opcional)** Trocar token User do Graph Explorer (expira 1h) por System User Token permanente — caminho B que ficou em aberto. Vale fazer antes da próxima sessão de mexer em ads pra evitar refresh manual.

## 🟡 Estoque GB — Fase 2 mapeamento de SKUs (próximos passos 29/05)

- [ ] **Receber dos analistas (29/05) a lista de IDs dos envios FULL criados em 28/05.** Mensagens prontas para Slack já entregues pra Pedro (Leonardo/FBA AMAZON, Lucas/FULL SHOPEE 1-3, Yasmin/FULL ML). Pedro envia hoje, recebe respostas amanhã.
- [ ] **Corrigir `/var/www/estoque-budamix/src/lib/envios-full.ts` linha 20:** remover `"AMAZON FULL"` e `"FULL MAGALU"` do array `FULL_SHEET_NAMES` (abas não existem na planilha oficial `1zfll5bvkIUqY56y0YcJ-ZP1GoMupcj_f`).
- [ ] **Limpar do banco** os 53 movimentos com `source_channel='amazon_full'` (vieram de planilha errada que o Kobe baixou).
- [ ] **Aplicar baixa filtrada** em `stock_movements` por `external_event_id LIKE '%:ENVIO_ID:%'` quando receber a lista, executando via rota `ingest-safe-outbound` com `apply=true` ou re-rodando o resolver sobre subset.
- [ ] **Decidir fluxo de controle "novo vs antigo"** depois desse 1º ciclo: Pedro avaliou 3 opções (A pedir analistas, B fingerprint, C coluna STATUS_SISTEMA) e decidirá após volume baseline. Provavelmente combinação B+C.
- [ ] **Passo 2 da implementação Fase 2:** especificar as decisões humanas por família (Pedro quer detalhe — kits_diversos 197 SKUs, FYTR001 13 SKUs alta-frequência, MANT, BR, BF, PUMP). Adiado para depois do ciclo de baixa de amanhã.
- [ ] **RLS desabilitado em 13 tabelas** do Supabase Budamix Central (`stock_movements`, `stock_movement_evidences`, `sku_aliases`, `kit_bom` + 9 outras). Advisor crítico. Tratar quando puder.

## 🟢 Canggu/Ana — auditoria 25/05 fechada (4 fixes em prod)

- ✅ ~~**Pergunta ML "Pode ser usado na air fryer?" recebeu resposta proibida do Bloco 17**~~ → **RESOLVIDO 25/05** — INSERT correção air fryer em `response_corrections` (id 5362537f, embedding processado) + `ml-response-validator.ts` estendido com `FORBIDDEN_ADMIN_LEAK_PATTERNS` (10 regex Bloco 17). Validado end-to-end via invocação real do `process-ml-question` v18: resposta agora correta usando RAG. Commit 7d93e78.
- ✅ ~~**Ana mandou "Pra eu resolver isso pra você... rapidinho" em reclamação (Grace Kelly)**~~ → **RESOLVIDO 25/05** — `response-validator.ts` (WhatsApp) ganhou `COMPLAINT_OVERPROMISE_PATTERNS` com cleanup inline (5 regex Unicode-aware). "Vou resolver" → "vou encaminhar pra equipe". Validado via node: 5 casos PASS + controle neutro não dispara. Commits 127f379 + 12ba9f4 (bugfix regex `\b` ASCII vs `(?!\p{L})` Unicode).
- ✅ ~~**Escalation gravada com `reason` em inglês**~~ → **RESOLVIDO 25/05** — `intent-classifier.ts` reescrito 100% em PT-BR com REGRA CRÍTICA DE IDIOMA + exemplos correto/errado. Enum `intention/sentiment` preservados (chaves de branching). Validado via Anthropic API direta: escalation_reason agora em PT-BR. Commit 127f379. Pendência satélite: 39/49 escalations históricas têm reason em inglês (não vou backfill — só novas).
- ✅ ~~**Ana mandou 2 saudações em 26s no caso Grace**~~ → **RESOLVIDO 25/05** — detector de poll do `webhook-whatsapp/index.ts` agora busca QUALQUER agent msg com `metadata->>'origin_poll' = 'true'` na conversa (não só a última). Quando match → atualiza source + `skipAiPipeline=true`. Commit 78c7833 → webhook-whatsapp v40. Impacto histórico: 16 customers com `source=NULL` apesar de poll enviado serão destravados na próxima interação.

## 🔴 Bug — Loja desktop tela em branco (investigar)

- [ ] **Clicar em "LOJA" no header desktop do `budamix.com.br` leva à tela em branco.** Relatado por Pedro em 25/05 noite. Investigação iniciada e interrompida.
  - **Onde olhar:** `budamix-ecommerce/src/pages/Shop.tsx` (90 linhas, simples). Rota `/loja` em `App.tsx:68` via lazy import (`App.tsx:40`). Link em `components/layout/Header.tsx:11`.
  - **Próximo passo:** abrir `https://budamix.com.br/loja` em desktop, abrir DevTools console e capturar o erro real antes de mexer no código.
  - **Hipóteses iniciais (sem confirmação):**
    - `useQuery` em `Shop.tsx:14` não desestrutura `error` — query falhando silenciosamente (RLS, coluna ausente, ou `product_images` mal-relacionada).
    - Erro de runtime em filho de `Shop` (`ProductCard`, `Layout`) só em viewport desktop.
    - Chunk de lazy import 404 pós-deploy (mas `ChunkErrorBoundary` deveria pegar).
  - **Sintoma desktop-only:** estranho — mobile parece funcionar. Pode estar relacionado a algum componente condicional do header/layout desktop ou a um asset (imagem hero?) que só carrega em desktop.

## 🟡 Budamix.com.br — pivot 100% vidro

- [ ] **Decisão sobre Jarra Medidora de Vidro 500ml** (slug `jarra-medidora-vidro-budamix-500ml`) — desativada em 25/05 junto com os outros não-(potes herméticos 4 travas + potes redondos). É vidro, mas não se encaixa nas 2 categorias específicas. Pedro precisa decidir se reativa como SKU avulso ou mantém de fora. Reativação: 1 UPDATE no Supabase.
- [ ] **Trocar fotos placeholder dos 2 combos novos** (IMB501_KIT2 + IMB501_KIT3) — hoje usam fotos do unitário IMB501 Tampa Preta como fallback. Pedro vai **gerar manualmente** as 24 fotos (6 por combinação × 4 combinações) usando os prompts e referências definidos hoje 25/05 — descartou batch via nano-banana. Quando concluir, basta `UPDATE product_images SET image_url = ...` mantendo `variant_id`. Frontend já pronto pra trocar visual ao selecionar combinação. Continuação amanhã 26/05.
- [ ] **Ajustar estoque inicial dos 2 combos** — hoje em 10 unidades cada. Pedro cadastra na planilha de Precificação (SKUs `IMB501_KIT2` e `IMB501_KIT3`) e o sync.py propaga.
- [ ] **Atualizar conteúdo de marca (blog, ads, fotografia) pra refletir foco 100% vidro** — pivot é estratégico, afeta posicionamento.

## 🟢 Pipeline DSA / ML — resolvido em 23/05

- ✅ ~~**Probe ML Ads agendado pra 23/05 09:30 BRT**~~ → **RESOLVIDO 23/05** — bug do dia 22 (ADS zerado às 03:50 BRT) foi anomalia pontual. 5 probes rodaram (em UTC, não BRT como planejado — VPS está em UTC) e todas as 5 amostras (04:00, 04:30, 05:00, 05:30, 06:00 BRT) mostraram ADS já consolidado pra 22/05. Cron do pipeline ML movido pra `50 9 * * *` UTC = 06:50 BRT real. Sanity check `build_ads_block.suspect_zero_spend` NÃO implementado (não foi mais necessário; pode ficar como rede de segurança futura).

## 🟢 Canggu/Ana — pipeline validado E2E 22/05 (operação fechada)

- ✅ ~~**Ana muda em escalação (caso Carolina Michelsen)**~~ → **RESOLVIDO 22/05** — `dispatchEscalation → escalate` chamava com `Bearer SERVICE_ROLE_KEY` e era rejeitada com 401 (mesmo bug do JWT desalinhado de ontem em outra fronteira). Fix: `escalate STEP 0 valida X-Internal-Token` + `dispatchEscalation manda header` + GHA workflow com `NO_JWT_FUNCTIONS list` que passa `--no-verify-jwt` em redeploys. Versões em prod: webhook-whatsapp v37, process-message v44, escalate v18, ml-webhook v15.
- ✅ ~~**Notification_phone era a própria Ana**~~ → **RESOLVIDO 22/05** — `agent_config.notification_phone = 5519992979490` era o número da instância da Ana (Evolution Cloudfly), não do Pedro. Desde o cutover, todas as notifs iam pra própria Ana em loop silencioso. Pedro nunca recebeu nenhuma. Fix: UPDATE pra `5519993040768` + DEFAULT_NOTIFICATION_PHONE hardcoded também atualizado. Pedro confirmou visualmente recebimento.
- ✅ ~~**7/7 cenários E2E**~~ → **VALIDADO 22/05** — Kobe rodou matriz completa: pergunta normal / origin poll typo / imagem / áudio / burst debounce / reclamação grave / pedido humano. Todos PASS no banco + notif visual confirmada. Conv de teste: `2c5b29ea-6751-4110-b4e1-46d9c755b39f`.

## 🔴 Canggu/Ana — pendências carryover (backlog médio prazo)

- [ ] **Pós-mortem do JWT desalinhado** — sintoma corrigido em 3 functions via X-Internal-Token (process-message, escalate, ml-webhook), causa raiz exata desconhecida. Hipótese de rotação de chave não bate com memória do Kobe (sem registro de rotação em 07-08/05). Investigar: comparar `JWT_SECRET` do projeto vs `SUPABASE_SERVICE_ROLE_KEY` decodificado, auditar acessos painel em 07-08/05. Bypass atual com X-Internal-Token é workaround.
- [ ] **Trazer `verify_jwt=true` de volta nas 3 functions** — depois do pós-mortem da causa raiz do 401. Hoje (22/05) `process-message`, `escalate`, `ml-webhook` rodam com `verify_jwt=false` + validação manual de `X-Internal-Token` (secret 384 bits em env `INTERNAL_DISPATCH_TOKEN`). Segurança equivalente, mas idealmente JWT padrão deveria voltar.
- [ ] **Health check Canggu — substituir N8N por script versionado na VPS** — workflow `DEjLkJcllQEmrcLF` (Budamix WhatsApp Health Check) parou de gravar em `whatsapp_health_checks` em 07/05 10:45 BRT após refactor não-comitado (11 nodes git → 2 nodes live). Kobe sem acesso ao N8N por Cloudflare 1010 + export sumiu do repo. Plano: Python/bash cron na VPS gravando direto no Supabase. Defaults sugeridos: Telegram alert + 15min. Bug de Ana muda só foi pego visualmente porque esse monitor estava cego.
- [ ] **Validador automatizado pós-deploy de edge functions** — cada deploy deveria disparar teste sintético (mensagem fake → conferir resposta no banco em 30s). Cron 5min. Teria pegado o 401 em minutos, não 13 dias.
- [ ] **WhatsApp Cloud API (Meta oficial) — discussão estratégica** — Pedro perguntou hoje se valia migrar. Decisão: NÃO migrar como reação ao caso da Edneia (bug era pipeline interno, não transporte). Mas vale como projeto deliberado de médio prazo (3-4 semanas) pela estabilidade + observabilidade. Reabrir discussão depois de Health Check + Validador resolvidos.
- [ ] **Bling Filial OAuth — re-autorização** — adiado por decisão do Pedro (21/05): "não estou usando esse Bling de qualquer maneira". Confirmado refresh manual retorna 400 "client_id inválido" → app OAuth foi deletado/desativado no painel Bling. Quando retomar uso, criar novo app, atualizar `marketplace_tokens.platform='bling_filial'` com novo `app_id` + `client_secret`. Bling Matriz continua funcionando normal.

## 🟡 OpenClaw / Kobe — pendências da sessão de 07/05

- [ ] **Adicionar Anthropic ao fallback chain do Kobe**: perfil `anthropic:default` (token Claude válido) já configurado em `/root/.openclaw/agents/main/agent/auth-profiles.json` mas **fora** do `agents.defaults.model.fallbacks` (hoje só `openai-codex/gpt-5.4`). Se cota Pro estourar em pico futuro, ainda morre. Adicionar `anthropic/claude-sonnet-4-6` (ou modelo equivalente atualizado) como 3º fallback. Não urgente agora que cota é Pro 5x.
- [ ] **CLAUDE.md global do Pedro desatualizado** sobre OpenClaw: ainda diz `Modelo: migrando para GPT 5.4 (default) + GPT 5.1-mini (crons)` e `Custo: ~$120/mês Anthropic (em migração para OpenAI)`. Realidade atual (07/05): `primary: openai-codex/gpt-5.5`, `fallback: openai-codex/gpt-5.4`, assinatura ChatGPT Pro 5x. Atualizar no Mac local em `~/.claude/CLAUDE.md` quando houver janela.

## 🟡 Social Studio Reborn — Fase C em andamento

- ✅ ~~**Social Studio Reborn — Pedro revisar e mergear PR #3**~~ → **CONCLUÍDO 07/05** (commit `32c22bd` na main).
- ✅ ~~**Social Studio Reborn — Fase B**~~ → **CONCLUÍDO 07/05** (commit `dfb9dda` na main, PR #4 mergeado após smoke E2E real validado).
- [ ] **Social Studio Reborn — Fase C em progresso (C1 ✅ fechado)**: branch `feature/social-studio-reborn-fase-c`, PR aguarda C2 fechar. C1 = lib OAuth helpers + types Supabase regenerados (commit `d6384bd`). Próximos: C2 (página `/admin/social/conta` + OAuth start), C3 (edge `meta-oauth-callback`), C4 (edge `publish-instagram-post`), C5 (tick mock→real com trava `TESTE INTERNO`), C5b (remover trava após smoke validado), C6 (UI pós-publicação + retry + banner), C7 (refresh token cron mensal), C8 (smoke + PR final).
- [ ] **Social Studio Reborn — pré-requisitos manuais Meta antes do C3**: Pedro vai precisar criar app Business no `developers.facebook.com` (Instagram Graph API + Facebook Login), pegar `META_APP_ID` + `META_APP_SECRET`, configurar redirect URIs (`http://localhost:8080/admin/social/conta/callback` + `http://localhost:8081/...` + `https://budamix.com.br/...`), adicionar Pedro como tester em modo Development, e setar os 2 secrets no Supabase Studio Edge Functions Secrets. CC vai guiar passo a passo quando chegar — Pedro precisa estar disponível pra responder dúvidas em cada tela do Meta Developers (primeira vez que ele mexe ali).
- [ ] **Social Studio Reborn — Fase D** (depende Fase C): edge `collect-instagram-metrics` + Dashboard de métricas + recharts + export CSV.
- [ ] **Social Studio — branches preservadas até 05/06/2026** (30 dias): `feature/social-studio-pr2` (PR2 cancelado), `feature/social-studio-pivot-copy-only` (Pivot 1 descartado). Avaliar deletar quando Reborn estiver estável em prod.

## 🚨 URGENTE — Operação / Dados

- [x] ~~**Estoque Budamix — retomar deploy em produção**~~ ✅ **Resolvido 20/05/2026.** Deploy via rsync direto (não GitHub). Commits `42dbeec` + `eeab9c5` + `9f980cc` + `2a38f57` em prod desde 19:11 BRT. Build via `--webpack` (turbopack quebra externals do pdf-parse). Checkpoint encerrado. → [[projects/estoque-budamix#Decisões-chave]]
- [ ] **Estoque Budamix — limpar operações de teste do banco** (opcional, sem urgência): `DELETE FROM estoque_operations WHERE operation_name LIKE 'TESTE QA Claude%';` — 14 linhas geradas na validação end-to-end de 20/05.
- [ ] **Estoque Budamix — webhook n8n descontinuado**: `trottingtuna-n8n.cloudfy.live/webhook/estoque-upload` substituído por parser local Next em 20/05/2026. Pode ser desativado no painel n8n sem impacto.
- ✅ ~~**Budamix E-commerce — módulo de preview mobile no admin**~~ → **ENTREGUE 21/05 noite** em prod. Rota `/admin/preview-mobile` com 3 devices (iPhone SE/14, Pixel 5), URL bar editável, refresh, atalhos pra rotas principais + 6 produtos ativos recentes. Entry points: sidebar + header dashboard + Ações Rápidas. Commit `a0f50e9`. → [[projects/budamix-ecommerce#Decisões-chave]]
- [ ] **Banner triplo Budamix — Pedro escolher versão final da Capa 01**: `capa-01.png` (v1, 4 linhas) vs `capa-01-v2.png` (v2, 3 linhas). Output em `~/Documents/05-Projetos-Codigo/banner-triplo-budamix/output/`. Depois importar no Canva e inserir foto dos potes (Capa 2) + foto da Morgana (Capa 3) nos placeholders.
- [ ] **Estoque Budamix — POT1BB duplicado na aba ESTOQUE da planilha de Precificação** (`1u74a...`): L8 com Trava est=24, L9 sem Trava est=2, mesmo SKU. `find()` sempre pega L8, baixas em "sem Trava" caem na linha errada. Solução proposta: renomear L9 → `POT1BB_ST`. Aguardando OK do Pedro pra aplicar via gspread.
- [ ] **Estoque Budamix — lista de aliases editável em `/tmp/pr3-cadastro-cleanup.md`** (5 famílias: POT1BB, IMB501, YW, KIT, série 914). Pedro precisa preencher os termos coloquiais reais da equipe (anilão? montado? caneca bola?) e devolver pra aplicar.
- [ ] **Estoque Budamix — KFJ003 SKU não encontrado** apareceu 1x no histórico Supabase. Pedro vai consultar a equipe se é fantasma (excluir) ou cadastro retroativo necessário.
- [ ] **Estoque Budamix — PR4 kits/BOM (bug #5/#6 estrutural)**: 75% dos erros reais (12 de 16 nas últimas 500 ops) são "Estoque insuficiente" — sintoma de sistema que não decompõe kit em componentes na baixa. Mudança estrutural com schema novo. Tocar só depois de fechar PR1+PR2+PR3a em produção + cleanup cadastro acima.
- [ ] **Budamix Central — Estoque Fase 1.5: validação visual do Pedro** em `/estoque/fisico` e `/estoque/consolidado` (KPIs premium, badge sync, donut FULL×FÍSICO, Top 10 SKUs). Se aprovado, seguir para Fase 2.
- [ ] **Budamix Central — Estoque Fase 2: movimentações**: tabela `physical_movements`, trigger `apply_physical_movement`, role `operator`, form modal, histórico por contramov e sync app→planilha a cada 2min.
- [ ] **Budamix Central — Estoque Fase 3/4**: import CSV/XLSX com template e validação em lote; import PDF com Vision/Claude quando virar prioridade.
- [ ] **Budamix Central — investigar SKU duplicado na aba ESTOQUE**: `physical_inventory_summary` ficou R$ 552.191,35 vs `physical_inventory_items` R$ 552.167,57 por deduplicação SKU-level.
- [ ] **Budamix Central Full — Etapa 1E monitoramento Shopee**: criar healthcheck/alerta Telegram se alguma das 3 contas Shopee passar de 6h sem sync.
- [ ] **Budamix Central Full — validação cruzada ML Full e Amazon FBA** equivalente à validação Shopee 1D. Confiança atual média; Amazon teve fantasmas removidos e precisa validação defensiva.

## 🚨 Mercado Ads — internalização (Pedro assume gestão direta)

- [ ] **Mercado Ads — Pedro vai internalizar a gestão** atualmente feita por agência terceirizada. Briefing baseline entregue em 08/05 em `~/Documents/05-Projetos-Codigo/planejamento-importacao-2026/ml-ads-briefing/` (5 arquivos: briefing.md, actions.md, campaigns.csv, ads_by_item.csv, monthly_metrics.csv). Conta GAMMAOFICIAL (advertiser_id 172453), 16 campanhas (10 ativas + 6 pausadas), só Product Ads. Performance 30d: investido R$ 5.942 → vendas atribuídas R$ 59.938 → ROAS 10,1x (efetivo c/ halo orgânico ~19x). ACOS evolução: Fev 21,7% → Mar 11,3% → **Abr 9,7% (melhor)** → 7d Mai 10,6%.
- [ ] **Mercado Ads — ações imediatas do briefing (08/05)**: (a) pausar manualmente anúncios com estoque ≤5 ainda recebendo gasto (queima de orçamento identificada — lista em `actions.md` §🔴); (b) revisar Buy Box dos 15 anúncios perdendo BB com gasto ≥ R$ 20; (c) escalar orçamento das top 5 campanhas com ACOS < 8% em 30% (uma por vez, observar 3 dias entre cada). Decisão de execução fica com Pedro caso a caso.
- [ ] **ml-ads-automation — ativar cron de coleta diária no Railway/N8N** para começar a acumular histórico próprio em Supabase (`ml_campaigns_daily` + `ml_ads_daily`). Sem isso, análise histórica fica travada nos 90 dias retroativos que a API ML expõe. Workflow N8N já documentado em [[projects/ml-ads-next-steps]] § 4. Refresh diário já roda (10:30 BRT); falta apenas o restante do pipeline.

## 🚨 Amazon Ads / BidSpark

- [ ] **Amazon Ads — D+7 da rodada 02/05/2026**: medir impacto dos ajustes em Potes Herméticos Vidro, Jogo Canequinhas Café, Potes Herméticos Tampa Bambu, Canecas Canelada, Canecas Porcelana Tulipa, Kit Xícaras Porcelana Paris, Suporte Controle Gamer, Jarra Medidora e Potes Redondos Plástico.
- [ ] **Amazon Ads — D+7 dos experimentos 03/05/2026**: medir Kits Microfibra Carro (ACoS base 7,6%, gasto R$3,62, vendas R$47,70, 3 pedidos) e Abraçadeiras Nylon (experimento de tração com ASIN ativo `KIT200BR10P`/`B0CN9PPC17`, 24 un FBA).
- [ ] **Amazon Ads — Abraçadeiras Nylon**: no D+7 medir impressões, CTR, CPC, cliques, vendas, Buy Box e estoque FBA; objetivo é diagnóstico de tração, não otimização de ACoS ainda.
- [ ] **Amazon Ads — Potes Herméticos Vidro**: validar no Seller Central qual ASIN recebe tráfego de `pote hermetico vidro` e investigar preço, Buy Box, imagem, título ou variação.
- [ ] **Amazon Ads/BidSpark — revisar logs de action_type**: diferenciar escala Exact vs Broad/Alcance/Auto/Product Targeting para auditoria D+7.

## 🚨 Canggu / Ana

- [ ] **Canggu — trocar senha temporária do admin** no login do admin. Ação do Pedro.
- [ ] **Canggu ML — editar manualmente resposta com frase forbidden no produto MLB3343832496** ("Jogo 6 Canequinha 100ml"). Resposta atual contém "Por favor entre em contato conosco para conhecer outros modelos disponíveis!" enviada às ~15:00 BRT de 05/05 antes do hard-block estar ativo em produção. Não é possível remover via API; só edit manual no painel ML. Sugestão de texto novo já dada na sessão (~187 chars, sem frases forbidden).
- [ ] **Canggu ML — marcar 👎 na resposta do MLB3343832496 e colar correção** no painel Canggu pra alimentar `process-correction-embedding`. Vira embedding e blinda perguntas semelhantes futuras (ex: "tem maior?", "tem com mais ml?").
- [ ] **Canggu — decidir redirect www↔apex em `canggu.com.br`**. Hoje ambos servem conteúdo idêntico (duplicate content, ruim pra SEO). Recomendação CC: www → apex. Configurável via `vercel.json` ou settings de domínio Vercel.
- [ ] **Canggu — atualizar GitHub Actions Node 20 → 24** em `.github/workflows/deploy-edge-functions.yml`. Deadline forçada: Node 20 removido dos runners em **16/09/2026**. Mudança trivial (1 linha por action). Sem urgência mas registrar.
- [ ] **Canggu — adicionar instruções no system prompt da Ana** para `[Sticker recebido]`, `[Localização compartilhada: ...]` e `[Contato compartilhado: ...]`, evitando respostas genéricas.
- [ ] **Canggu — B1 segurança**: service_role JWT em arquivos tracked, `LOVABLE_API_KEY` legado, CORS aberto, `verify_jwt` em funções internas. Estimativa ~3 dias. (Ghost function `test-search` ✅ removida em 05/05.)
- [ ] **Canggu — B3 resiliência restante**: retry em `classifyIntent`/`generateResponse`, UNIQUE index `whatsapp_message_id`, dedup e fallback textual.
- [ ] **Canggu — estender ajuste de tom pra `process-message`** (Ana no WhatsApp). Tom natural já aplicado no ML; equalizar no WhatsApp se Pedro confirmar que lá também soa formal.
- [ ] **Canggu ML — monitorar próxima pergunta real do ML** com prompt v13 (tom natural). Confirmar que (a) Ana não usa mais frases tipo "entre em contato conosco" e (b) tom realmente saiu do nível telemarketing. Se escapar, ampliar regex ou ajustar prompt.
- ✅ ~~**Canggu — smoke test pós-recovery 13/05 18h**~~ → **RESOLVIDO 17/05.** Rotação de chave + Opus 4.6 só tratou sintoma; bug real era arquitetural (item abaixo). Após fix do `EdgeRuntime.waitUntil()` em 17/05 noite, Ana voltou a responder. → [[memory/sessions/2026-05-20#Canggu / Ana — auditoria ML + regra 17 sceptical-but-gentle (16:30–17:00 BRT)]]
- ✅ ~~**Canggu — fix arquitetural fire-and-forget no webhook-whatsapp**~~ → **RESOLVIDO 17/05** com commit `f063738`, webhook-whatsapp v33. `fetch('/functions/v1/process-message')` envolvido em `EdgeRuntime.waitUntil()`. Edge runtime agora mantém função viva até o invoke completar. Log explícito `invoke_process_message_ok` adicionado pra regressões futuras serem visíveis. Lição arquitetural geral: TODO `fetch()` sem await dentro de edge function precisa de `waitUntil()`. → [[memory/context/decisoes/2026-05#[17/05 noite] Canggu — fix arquitetural do silêncio de 9 dias da Ana (EdgeRuntime.waitUntil)]]
- ✅ ~~**Canggu — auditoria de respostas da Ana no ML**~~ → **RESOLVIDO 20/05.** 25 respostas analisadas, 3 padrões críticos identificados (cadastro/verificar internamente, "entre em contato conosco", "vamos atualizar anúncio"). Causa raiz no system_prompt corrigida via regra 17 "sceptical-but-gentle". 3 correções modelo seedadas com embedding em `response_corrections`. 3 perguntas marcadas no painel. Migration `20260520200000` + `20260520210000` em `PHPB2025K/canguu`. → [[memory/context/decisoes/2026-05#[20/05 tarde] Canggu — auditoria ML + regra 17 "sceptical-but-gentle" + 3 correções modelo]]
- [ ] **Canggu — hard-block adicional no `response-validator.ts` para frases de cadastro/processo interno**: camada defensiva análoga à do horário 24/7. Adicionar regex para `cadastro do produto`, `verificar internamente`, `atualizar o anúncio`, `nossa equipe técnica` — substitui ou avisa. Não urgente porque regra 17 do system_prompt já cobre, mas é defesa em profundidade caso a regra escape pontualmente. ~3h de trabalho (1h código + 2h testes Deno).
- [ ] **Canggu — reauditoria semanal automática das respostas da Ana no ML**: opcional. Cron rodando query similar a `SELECT question_text, answer_text, feedback FROM marketplace_questions WHERE answered_at > NOW() - INTERVAL '7 days' AND answered_by ILIKE '%ai%'` + Claude classificando padrões problemáticos + relatório no Telegram. Pedro decide se quer agendar.
- [ ] **Canggu — investigar N8N principal `KE7YVXayl5ntjwQk` que segue `active=true`** mesmo após cutover ADR-007 pra `webhook-whatsapp`. Pode estar disputando processamento de mensagens com a edge function (criando o poll duplicado / divergência). Decidir: desativar de vez ou tornar oficial como fallback. MOC fala "em depreciação" mas live ainda está ligado.
- [ ] **Canggu — `verify_jwt: true` em webhook-whatsapp e process-message**: descoberta hoje em `list_edge_functions`. Pode estar bloqueando Evolution se ela não mandar Bearer válido. Conflita com o documentado em `projects/canggu/edge-functions.md` (todas com false). Investigar se Evolution está mandando anon_key como Bearer (passa verify_jwt) ou se algo está rejeitado em 401 silencioso. Reverter para `false` em `webhook-whatsapp` (é webhook externo, deve ser público).

## 🚨 RH / Ponto Certo

- [ ] **RH — guard de WhatsApp proativo ESTENDIDO INDEFINIDAMENTE (até 2027-01-01)** em `/tmp/rh-whatsapp-block.json`. Pedro pediu 05/05 14:04 BRT que nenhum cron/agente RH dispare proativos a funcionários até liberação explícita. Em 11/05 10:15 BRT, Pedro liberou **apenas o escopo específico** dos problemas de ponto reportados no Monitor Ponto Semanal de 11/05 sobre a semana 04/05–09/05, até resolução completa com Fran, Leonardo, Lucas, Mateus e Sandra. Exceções técnicas: `--allow-rh-reply` permite respostas inbound; `--allow-rh-approved-case` permite follow-ups desse lote aprovado. Proativo genérico segue bloqueado. Crons em risco que continuam habilitados mas inofensivos enquanto o guard ativo: `RH Compliance Check` (diário 19h BRT), `Monitor Ponto Semanal` (segundas 10h BRT), `Ponto Certo - QR Code Refresh` (diário 03h, não envia WhatsApp). Validado: proativo → `BLOCKED_RH`; reply → `SENT`; caso aprovado → `SENT`.
- ✅ ~~**Ponto Certo — DNS do domínio novo**: criar/apontar A record de `ponto.budamix.com.br` para `187.77.237.231`~~ → **RESOLVIDO 05/05.** Pedro criou A record no Registro.br, DNS propagou nos resolvers públicos, CC local restartou Traefik na VPS pra forçar reemissão do cert ACME (1ª tentativa havia falhado em 04/05 12:39 UTC com NXDOMAIN). Cert Let's Encrypt emitido, servidor responde HTTPS 200. Cache de DNS em provedores brasileiros pode levar horas pra atualizar — workaround: trocar pra DNS Cloudflare/Google ou tentar via 4G. Pendência menor: deletar entrada órfã `pontocerto.budamix.com.br` criada por engano. → [[memory/sessions/2026-05-05#Ponto Certo — DNS + cert SSL `ponto.budamix.com.br` resolvidos (CC local)]]
- ✅ ~~**Ponto Certo — deploy produção do módulo Conversas RH**~~ → **RESOLVIDO 13/05.** Painel `/admin/conversas` (WhatsApp Web split-view real-time) + `/admin/equipe/:id` (FuncionarioDetalhe com 4 tabs) deployados em `/var/www/ponto-certo/`. Build + pm2 restart. Realtime habilitado em 5 tabelas. → [[memory/sessions/2026-05-13#Ponto Certo + Agente RH]]
- [ ] **RH — lote semana 04–09/05: aguardando Sandra, Mateus, Leonardo responderem** à saudação cordial reenviada 13/05 10:04 BRT ("Olá, X. Tudo bem?"). Histórico apagado e recomeçado por pedido do Pedro. Cron diário (`rh-cron-followup-lote-20260511.py`, seg-sex 10h BRT) cuida do desenrolar com regra 18 (abertura 2 etapas). Após 5 dias úteis sem resposta, escala automaticamente via Telegram tópico RH. Fran + Lucas já estão resolved (cobertura via app aprovada por Pedro).
- [ ] **Pedro — trocar senha admin temporária do Ponto Certo** (`*d8tzMJ=EvtLfGxD7&`) pelo app em Configurações → Senha quando puder.
- [ ] **RH — acompanhar feedback da Yasmin** sobre recebimento correto dos 2 chunks da mensagem inaugural reenviada com `linkPreview: false`.
- [ ] **RH — datas de admissão dos funcionários** para cálculo futuro de férias.
- [ ] **RH — padrão do contador FOUR/Suellen** para espelho de ponto.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.
- [ ] **Obter contrato social da Concept (58.818.245/0001-00)** — capital social não localizado nos PDFs locais. Empresa aberta 13/01/2025; localmente só há Cartão CNPJ + CLI/JUCESP. Pedir à contabilidade ou puxar Certidão de Inteiro Teor em jucesponline.sp.gov.br. Necessário para fechar capital social consolidado do grupo (hoje em R$ 889.000 sem Concept). Ver [[business/empresa/capital-social-grupo-2026-05]].
- [ ] **Obter alteração contratual que abre a filial GB Importadora (58.151.616/0002-24)** — filial inscrita em 23/01/2025 mas o ato de alteração não foi encontrado localmente. Capital não muda (é único da matriz), mas o documento é importante para a regularidade. Pedir à contabilidade ou Certidão de Inteiro Teor JUCESC do NIRE 42208840944.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio

- [ ] **Blog Budamix — inspeção visual manual do post de teste** id `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` (pilar `receber-visitas`) no `/admin/blog`; após Pedro inspecionar cover/supports/pins, deletar o post de teste.
- [ ] **Blog WF0 — polir payload de resposta**: hoje retorna `pillar_focus=null` no response mesmo quando o foco foi aplicado internamente. Cosmético; funcional OK.
- [ ] **Social Studio — PR2 ~95% (C1-C6 entregues)**: C1+C1.5 migrations + 21 slides backfillados; C2 helpers (`resolveSlotColor` + `updateSlideElementStyle`); C3 ColorTokenPicker swatches inline; **C4** templates usando padrão conservador `colorOverrideForSlot(slot, ...) ?? palette.X` (visual 100% preservado quando sem custom); **C5** edge function `social-generate-image` v10 com append + truncate em 5 versões (deploy 05/05 17:44 BRT); **C6** ImageVersionsPopover.tsx (badge clicável + thumbs + restore zero-custo + regenerar inline com guard de quota >80%). Validado visualmente em 05/05 noite. **Falta apenas:** bug visual cover-numeric (linha abaixo). Tags defensivas: typecheck limpo nos arquivos do PR (erros pré-existentes só em `types.ts` por banner do Supabase CLI vazado em geração antiga).
- [ ] **Social Studio — bug cover-numeric não recebe imageUrl**: descoberto em 05/05 noite. `SlideRenderer.tsx:143` instancia `<CoverNumeric>` sem `imageUrl={img}`, mas `CoverNumeric.tsx` renderiza trans inferior 480px se receber. Slide 1 do template `lista` tem imagem gerada (~$0.04 desperdiçado por carousel) que nunca renderiza. Bug colateral: `'cover-numeric'` está em `noImage` do `needsImage()` em `Editor.tsx:777` — inconsistente com o template real. **Fix mínimo (2 linhas):** passar `imageUrl={img}` no SlideRenderer + tirar `'cover-numeric'` do `noImage`. Tech debt lateral (não no fix mínimo): `'item'` posições 2/6 do `lista` ganham imagem que nunca renderiza (~$0.08 por carousel) — solução boa exigiria edge function aceitar lista de slide_ids do frontend em vez de gerar pra todos. Pedro decide entre 3 opções (a/b/c) na próxima sessão. Diagnóstico completo na sessão de 05/05.
- [ ] **Reload VSCode pra carregar MCP Supabase**: ✅ desbloqueado em 05/05 noite — MCP Supabase usado extensivamente (queries, deploy de 2 edge functions, seed de paletas). Marcar como resolvido na próxima consolidação noturna.
- [ ] **Rotacionar PAT Supabase exposto em chat**: token `sbp_1d24...` em `~/.mcp.json` continua exposto no transcript da sessão de 05/05 (Pedro escolheu pular a rotação pra destravar primeiro o fluxo do C4). Pedro decidiu não rotacionar; dívida anotada. Revogar em https://supabase.com/dashboard/account/tokens quando tiver janela. Risco prático: PAT dá acesso total a todos projetos Supabase do Pedro.
- [ ] **Social Studio — PR3 (depois do PR2)**: escopo expandido em 05/05 noite. Vira módulo coeso de "controle manual de imagens": modo manual default (slides em branco; usuário decide quando gerar imagem) + `ImageGenerationDialog` com prompt editável + foto de referência + preview de custo + **geração individual em slide vazio** (botão "Gerar imagem" antes não existia em slide sem `image_versions`); botão "Delegar tudo à IA" como atalho pro fluxo legado. Estimativa ~1-2 dias.
- [ ] **Social Studio — Fase 4 publish IG**: Pedro identificar app Meta existente da Budamix e gerar long-lived token IG; Kobe coloca no Supabase Vault. Posterior aos PR2/PR3.
- [ ] **Social Studio — Fase 5 hardening backlog**: container warm para cold start render, JPG encoder, QA visual diff CI, rate limiting + audit log, tradução de erros Meta.
- [ ] **Social Studio — drag-and-drop com zonas**: cortado do MVP em 05/05; reavaliar depois dos PR2/PR3. Provavelmente cancelado se UX dos presets de paleta + cor/fonte/tamanho por elemento já satisfizer.
- [ ] **Social Studio — drift edge functions vs frontend (paletas)**: descoberto em 05/05 durante PR2. Frontend é fonte da verdade dos presets desde 05/05 18:00 BRT (decouple da FK). **Resolvido em 05/05 noite:** (a) `generate-social-copy` (v11 deploy) reescrito com 2 queries separadas em vez de embedded join `palette:social_palettes(*)` — evita PGRST200 por FK ausente; (b) `social-generate-image` JÁ estava no padrão correto (query separada por key); (c) seed das 4 chaves novas em `social_palettes` mantém retrocompat com qualquer fluxo legado que ainda dependa da tabela. CHECK constraint legacy `social_palettes_key_check` droppada (só aceitava clara/normal/escura). Total: 7 rows (4 novas + 3 legacy aliases) todas `active=true`. Drift do Canggu B5 segue sendo problema separado (mesmo padrão arquitetural).
- [ ] **Supabase CLI — investigar perms da conta**: `supabase link --project-ref jtczupudieeogzspdqae` falhou em 05/05 com "Your account does not have the necessary privileges". Migration do Social Studio rodada via Dashboard manualmente. Resolver se virar fluxo recorrente.
- [ ] **Vercel Token - Budamix Ecommerce** — item no 1Password `notesPlain` ainda incompleto; GitHub→Vercel auto-deploy já reduz bloqueio, mas token ainda é útil para rollback/hotfix CLI.
- [ ] **Vercel Preview Env** — configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas.

## 🎨 Design / Skills locais

- [ ] **Paper Design — carrossel Profundo Budamix**: terminar Cards 6 e 7 no Paper (`Scratchpad`, page `1-0`) usando o briefing salvo na sessão CC local de 02/05. Não confundir com os 96 templates oficiais concluídos em 03/05.
- [ ] **Budamix Marca — validar uso dos 96 templates oficiais** em projeto real e manter nota `business/marketing/marca/templates-carrossel-paper.md` como referência canônica.
- [ ] **ElevenLabs / video-use — higiene de keys**: deletar/revogar as duas keys antigas que circularam no transcript, manter key válida restrita a Speech to Text e rotacioná-la nas próximas semanas.

## 🚨 Infraestrutura e autenticações degradadas

- [ ] **Security Audit - Semanal** — último run conhecido em 03/05 06h BRT falhou com timeout/status `error`; investigar no próximo bloco operacional.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password.
- [ ] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; se Pedro quiser reativar essa rota, precisa reescanear QR Code. Evolution API/histórico segue separado e funcional.
- [ ] **Fisco / OpenClaw** — diagnosticar o bloqueio do `sessions_spawn` com `agentId=fisco` retornando `allowed: none` e restaurar o roteamento direto do agente.
- [ ] **Fisco — processo mensal de abatimento Matriz**: antes de usar saldo Matriz como excedente, consultar NFs B2B/atacado emitidas pela Matriz no período e abater por SKU/componente.

## 🟡 Observação / estabilidade

- [ ] **Watchdog/Monitor Ponto/RH crons** — revisar timeouts/fallbacks em jobs com histórico de falha por timeout/model not found.

## 🟡 Futuro aprovado / não imediato

- [ ] **Budamix Blog — Pinterest API/OAuth** — ativar postagem automática no Pinterest quando padrão de artigos e imagens estiver validado. Por enquanto pins ficam como assets no Admin.
- [ ] **Budamix E-commerce — conteúdo real das páginas stub** `/faq`, `/contato`, `/termos`, `/trocas-e-devolucoes`; hoje são Coming Soon/noindex.
- [ ] **Newsletter Budamix** — formulário ainda não persiste email; precisa backend real.

## 🔥 Budamix E-commerce — pós-sessão 21/05 noite (cupons + catálogo Tulipa + aba SITE)

- [ ] **Validar webhook MP em produção com BUDAMIX10** — quando alguém pagar usando o cupom, conferir se `coupon_redemptions` recebeu INSERT e `coupons.redemption_count` do BUDAMIX10 incrementou. Visível no `/admin/cupons` (3 cards de stats).
- [ ] **Investigar causa do preço Tulipa ter virado R$ 55,90** (deveriam ser R$ 64,90; uma variante com R$ 55,91 — centavo solto sugere edição manual). Corrigido via SQL em 21/05, mas causa não identificada — risco de regredir.
- [ ] **Hero por anúncio nos 6 produtos novos Tulipa** — cada um ainda usa o mesmo set de fotos gerais clonadas; substituir manualmente a hero de cada cor pelo destaque da cor do título.
- ✅ ~~**Trigger sync estoque por SKU compartilhado nos 7 Tulipa**~~ → **RESOLVIDO 22/05** indiretamente pelo `decrement-planilha.py`. Loop fechado: venda decrementa planilha em até 2min → `sync.py` propaga pro Supabase em até 5min → todos os produtos com mesmo SKU recebem o estoque novo simultaneamente. Latência total ≤7min. Trigger AFTER UPDATE no banco continua sendo um nice-to-have pra latência zero, mas não é mais bloqueante.
- ✅ ~~**Venda no site sobrescrita pelo cron sync.py em 5min (oversell)**~~ → **RESOLVIDO 22/05.** Antes: `decrement_stock` do mp-webhook baixava `product_variants.stock` mas a planilha ESTOQUE não sabia da venda, e o próximo cron sync.py (≤5min) reescrevia o stock antigo. Agora: novo cron `/opt/budamix-stock-sync/decrement-planilha.py` (a cada 2min) lê `orders WHERE status='paid' AND planilha_decremented=false`, decrementa col A da aba ESTOQUE em `qty × und_por_kit` pra cada SKU base (suporta compostos) via `gog sheets update`, marca order como processada (idempotente via coluna nova `orders.planilha_decremented`). Testado end-to-end com pedido fake. Wrapper cron `/root/scripts/decrement-planilha-cron.sh` + crontab `*/2 * * * *`. Log `/var/log/budamix-decrement-planilha.log`.
- [ ] **Conferir se Mercado Pago absorve juros do parcelamento** — col PARCELAMENTO da aba SITE assume 1,5% (mesma fórmula AMAZON). Se MP absorve, ajustar pra 0.
- [ ] **Investigar quem desativou variantes "espelho" dos 6 Tulipa novos** entre 14:50–14:57 do dia 21/05. Reativadas via SQL — entender o caminho de edição pra não voltar a acontecer.

## 🟡 Daily Sales Report Shopee — STANDBY (04/06)

> **Fase 1 validada (smoke 03/06 APROVADO, 13 gates, 0 críticos) — em standby por decisão do Pedro pra lapidação futura.** Não tocar sem solicitação explícita. Painel em https://mission.budamix.com.br/reports/daily-sales-shopee. Ficha: [[projects/daily-sales-shopee]].

- [ ] **Aplicar regra de densidade de 4 elementos em L02/L03/L04** — hoje só L01 + L05 + L06 ganharam a regra (commit `79517168`). L02 (tática), L03 (operacional) e L04 (granular) ainda podem produzir insights rasos em gaps estruturais.
- [ ] **Smoke das Contas 2 e 3** — Conta 1 (Budamix Store) rodou OK. Falta Budamix Oficial (shopee-budamix-oficial-2) e Budamix Shop (shopee-budamix-shop-3) com inputs reais.
- [ ] **3 gaps de fetcher Shopee** — (a) `shop_performance` HTTP 404 na Open API (endpoint legado descontinuado, precisa Seller Center scraping ou alternativa); (b) `ads_summary` HTTP 403 (Pedro precisa autorizar escopo de ads no OAuth); (c) `fulfillment_mix` retorna 100% `logistic_type=null` (backfill cron de orders precisa popular esse campo).
- [ ] **L06b Consolidadora cross-account não implementada** — quando as 3 contas rodarem em paralelo, falta prompt L06b que recebe os 3 L05 (1 por conta) e produz comparativo cross-account (papel por loja, tese seed agregada).
- [ ] **Cron 07:00 BRT não ativado** — runner pronto em `/root/segundo-cerebro/scripts/daily-sales-runner-shopee.py` mas crontab da VPS não tem entrada. ML continua em 06:00 BRT (não conflita). Ativar só depois da regra de densidade aplicada e smokes 2/3 OK.
- [ ] **Mission Control L06b placeholder** — página `/reports/daily-sales-shopee` está com card cross-account vazio aguardando L06b real.
- [ ] **Evoluir L08/L09 (semanal/mensal) com densidade equivalente** — hoje L08 (167 linhas) e L09 (157 linhas) seguem o padrão v3.0; podem se beneficiar da regra de 4 elementos quando agregação semanal aumentar superfície de gaps.

## 🚨 Jurídico / Contratos

- [ ] **Guarani Sistemas — enviar o email formal de contestação/distrato** com pedido de suspensão de protesto, memória de cálculo aberta e proposta **sem reconhecimento de dívida**.
- [ ] **Guarani Sistemas — reunir prova do congelamento/prorrogação com o Junior** (emails, WhatsApp, histórico) para sustentar contestação forte e eventual redução adicional/teses de cobrança zero.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **PCM001 peso embalado / foto 9 / custos refinados** — dados finais ainda pendentes.
- [ ] **SimulImport — validar cenários reais** — Pedro testar com importações dele.
- [ ] **Canggu/Ana B2/B5/B6** — blocos não urgentes de observabilidade, governança e cleanup seguem aguardando repriorização.
- [ ] **Fisco** — product-packaging.json, limpeza de produtos origem=0, CC-e/NFs antigas e validações Bling Filial seguem abertas.
- [ ] **Mission Control** — **11 módulos com PRD fechado** (13/05: Dashboard, System Monitor, Files, Agents, Memory, Office 3D; 14/05: Activity, Cron, Sessions, Skills, Costs). Pendentes: PRDs dos **12 módulos restantes** (tasks, agents-detail, logs, terminal, git, workflows, search, analytics, reports, settings, calendar, about, actions); `configured-skills.json` foi substituído por scan automático (resolvido); refinar regex botToken em `auth-profiles.json`; **KG sync Mac→VPS** via cron rsync 1h (ativa busca semântica no /memory); filtro `/memory?agent=<id>` por workspace (drawer linka mas filtro não implementado); **PRD futuro "Minhas Aplicações"** (cross-host VPS + Vercel + Supabase + Railway). **15/05**: `/api/agents` refatorado para varrer `vault/openclaw/agents/*/shared/*/IDENTITY.md` — sub-agentes (ex: Daily Sales Analyst sob Trader) agora aparecem no organograma como 3º nível (Kobe→top-level→sub-agentes); detecção via parentHint no IDENTITY ou fallback pra pasta-pai do vault.
- [ ] **Mission Control / Costs — integração n8n usage tracking (RETOMAR 15/05)**: n8n está em `https://trottingtuna-n8n.cloudfy.live` (Cloudfy.live, externo à VPS). API key disponível em `~/Documents/05-Projetos-Codigo/N8N-BUILDER/mcp-tools-export.json`. 3 workflows ativos com LLM: (1) **FLUXO ATENDIMENTO COMPLETO - GB Importadora** [`cIp0Aoxh7JVc3sfs`] usa OpenAI `gpt-5.2` em 6 sub-agentes + Whisper + TTS + embeddings + Cohere — via **OpenAI API key (custo real, NÃO subscription)**; (2) **CRIADOR DE RAG** [`5TGN6vUa07fYxHD3`] usa `gpt-5` + embeddings; (3) **Budamix Blog Article Generator (Kobe)** [`IG9KBmrEGts3CDp8`] usa **Claude Sonnet 4.6 via Anthropic API (custo real)**. Bloqueio atual: workflows estão com `saveDataSuccessExecution: None` (default n8n = não salvar success), API retorna 0 execs LLM. Plano em 4 passos: (1) habilitar `saveDataSuccessExecution: 'all'` nos 3 workflows via PUT API; (2) criar `scripts/collect-n8n-usage.ts` cron 15min que puxa execs success, extrai tokenUsage do output dos nodes `lmchatopenai`/`lmchatanthropic`, calcula via `pricing.ts` e grava em `usage-tracking.db` com `agent_id='n8n:<workflow_name>'`; (3) adicionar `gpt-5.2`, `gpt-5`, `text-embedding-3-small`, `tts-1-hd` no `pricing.ts` como `api_billing`; (4) /costs ganha categoria "n8n" no breakdown por agente.
- [ ] **Security hardening extra**, **Lovable sync**, **Stripe live key**, **LinkedIn integração** seguem fora da fila imediata.

---
_Última organização: 2026-05-20 — sessão Claude Code consolidada (14-20/05): Mission Control Activity/Cron/Sessions/Skills/Costs (5 módulos fechados) + organograma com sub-agentes (Daily Sales Analyst visível) + carrossel Budamix-nativo no Paper.design (4 artboards 1080×1080, DS v2.1) + tracking n8n com plano de 4 passos (em aberto)._

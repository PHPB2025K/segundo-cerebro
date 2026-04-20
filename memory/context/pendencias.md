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

- [20/04 6h BRT] [[projects/amazon-ads-automation|Amazon Ads]] — **Validar N8N Ciclo Diário rodou limpo** após fix `continueOnFail` no node `Send Health Alert WhatsApp` aplicado em 19/04 22h. Workflow `U8MCTTkNEJnD75aV`. Primeiro teste real do fix é amanhã 6h. Se falhar, PARAR migração BidSpark-3 nos 5 grupos restantes e diagnosticar. Comando: `curl -s -H "X-N8N-API-KEY: $KEY" "$URL/api/v1/executions?workflowId=U8MCTTkNEJnD75aV&limit=3"`
- [17/04] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **~102 commits locais à frente de `origin/main`** (atualizado 19/04 noite: +fix ordering product_images `4ad4937`, +revert harmonização visual `9ca005a`). Vercel ainda sem receber reescritas de 16/04 → 19/04 (header/footer/hero/PDP/cart/checkout/páginas novas/marquee/favicon/confetes/frete grátis auto/audit MP/SKU remap/stock sync/sort_order fix). Preview só no localhost + túnel cloudflared temporário. Push pendente.
- [17/04] ✅ ~~Instalar Apps Script na planilha de estoque~~ → **Substituído por cron VPS `*/5 * * * *` em `/opt/budamix-stock-sync/sync.py`** (187.77.237.231). Primeiro run: 25 variants atualizados, 0 erros. Scripts em `scripts/stock-sync-cron.{py,sh}`.
- [17/04] [[projects/budamix-ecommerce|Budamix Ecommerce]] — **Testes manuais de pagamento MP real** pendentes: cartão aprovado/recusado, PIX completo, simulador webhook MP Developers, estoque insuficiente, frete zerado via DevTools. Suite em `AUDITORIA-CHECKOUT-MP.md` §5.

- [06/04] VPS disco 63.4% usado de 47GB — monitorar crescimento. Logs de memory, backups e Chrome cache podem encher. Limpeza necessária em breve.
- [06/04] VPS memória 80% + swap 52% — processo zombie detectado. Requer investigação.
- [06/04] Aguardando **Pedro** publicar Canggu no Lovable (destacques visuais campos IA, envio WhatsApp corrigido)
- [17/04] [[projects/budamix-ai-agent|Ana]] — Opção B de credentials pendente: extrair os 7 Code nodes do workflow `KE7YVXayl5ntjwQk` para uma Edge Function `ana-pipeline-step` que usa `Deno.env.get`, tirando a chave 100% do JSON do workflow. Opção A (Setup Credentials + guards + credential no HTTP node) aplicada hoje reduziu SRK de 9→1 ocorrência mas não elimina. Refactor ~4-6h. → [[openclaw/agents/builder/IDENTITY|Builder]]
- [17/04] [[projects/gb-import-hub|GB Import Hub]] — **GB25010 numerário R$64.136,40 vence 20/04** (3 dias). Container já descarregado em Itapoá 16/04, aguarda desembaraço. PNI oficial registrada no sistema (22 itens). Pagar à Open Trade antes do prazo pra não travar nacionalização.
- [17/04] [[openclaw/agents/fisco/IDENTITY|Fisco]] — **CC-e da NF 000649** (transferência GB25011) a ser colada manualmente no painel Bling web pelo Pedro. Texto pronto (680 chars) corrige volumes zerados (1.044 cx / 15.136,07 kg bruto / 13.279,29 kg líq). Bling v3 API não expõe endpoint CC-e. → imprimir e enviar com Qualilog na segunda.
- [07/04] ~~OpenClaw — rate limit cascata: todos os crons falhando por fallback = mesmo provider.~~ → Movido para ✅

## 🟡 Importantes (não bloqueiam mas precisam de ação)

- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Migração BidSpark-3 pendente em 5 grupos** (4/8 feitos hoje: Bambu, Vidro, Paris, Tulipa). Restantes na ordem: Canequinhas Café → Potes Redondos Plástico → Kits Microfibra Carro (edge: órfã) → Canecas Canelada (edge: split 81/10/8) → Jarra Medidora (edge: Defesa-ASIN). Um por dia. Amanhã: Canequinhas (hipótese criado 01/03 pode ter escapado do legado destrutivo).
- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Investigação de listing Tampa Bambu** (Pedro manual no Seller Central). 7 ASINs: B0F2GHQHRN, B0F2GKSHYW, B0F2GQNT81, B0F2GKZZ43, B0F2GM9HMW, B0FN4PGK4M, B0FN4PW4SS. Pergunta: por que buscas "bambu" específico (`potes hermeticos bambu`, `pote hermetico bambu`, `potes de vidro com tampa de bambu`, `porta temperos bambu`) geram clique mas zero venda? Verificar: preço vs concorrentes, Buy Box, ranking orgânico, fotos, reviews, título contém "bambu"?, estoque. Destrava reativação do Alcance + M2 pleno do grupo.
- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **Revisitar Canecas Porcelana Tulipa em ~03/05** (14d após Bloco 3 de 19/04 que removeu 39 NEG_PHRASE destrutivas). Medir: (a) Descoberta voltou a converter (30d atual: R$38 / 0 vendas); (b) ACoS consolidado caiu abaixo de 20% target; (c) novos winners emergiram para Bloco 2 que ficou vazio.
- [19/04] [[projects/amazon-ads-automation|Amazon Ads]] — **4 commits locais pendentes de push** em `main`: `19a6638` (skill v4.0), `5489ae0` (skill v4.1 + tickets), `e1d56cd` (Ticket 3), `c7b95d9` (skill v4.2). Push fica pra o final da migração dos 8 grupos.
- [06/04] ~~OpenClaw — migração de modelos para GPT 5.4 / GPT 5.1-mini.~~ → Movido para ✅
- [06/04] Canggu — Fase 4 cleanup pendente: remover campos antigos (marketplace_links, available_kits, price_marketplace) e dropar tabela marketplace_product_mapping. Só executar quando tudo estiver estável nas tabelas novas. → [[openclaw/agents/builder/IDENTITY|Builder]]
- [06/04] Canggu — ~14 Session Extractors do [[openclaw/agents/kobe/AGENTS|OpenClaw]] desabilitados (timeout 120s insuficiente para Opus 4.6). Precisam de 300s+. Reavaliar após migração GPT 5.4.
- [06/04] Canggu — Analistas devem preencher campos ricos (descrição completa, sugestões de uso, diferenciais, tags) dos 44 produtos ativos. Guia entregue. Top 10 primeiro. → [[memory/context/people|People]]
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
- [17/04] [[projects/budamix-ai-agent|Ana]] — **Auditoria 48 conversas / 151 msgs** concluída (`auditoria-ana-whatsapp-abril2026.md` na raiz do projeto). 60% ✅ / 18% ⚠️ / 18% ❌ / 4% 🔄. **4 dos 5 padrões top já corrigidos** (fantasy product, forbidden promise, away_message, empty-msg loop, meta leak). **Residual ativo**: loop de pergunta sobre canal (site/ML/Shopee) mesmo com cliente já respondendo. → aplicar **Rec 4.1** (anti-loop canal no Passo 4a do BLOCO 4 do `system_prompt`) na próxima janela de ajuste.
- [17/04] [[projects/budamix-ai-agent|Ana]] — **Próxima auditoria: 19/04** (meta <20% erro, pós-fixes de 12/04). Monitorar se fixes (`carry-over threshold 0.2`, `detectEscalationInResponse`, `checkConsecutiveEmptyMessages`, debounce 12s, Regras 13-18) entregaram a redução esperada.
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
- [17/04] [[projects/budamix-ai-agent|Ana]] — Tarefa 4 pendente: sync `product_listings` ↔ ML. 13 MLBs stale no banco (ML desativou mas `is_active=true` no DB) + 44 MLBs ativos no ML sem entry no banco. Inclui os 7 MLBs da família Canelada 250ml (CAC250) que agora tem base_product no banco. Script precisa fazer de-para título→product_id + UPSERT. ~30-60min.
- [17/04] [[projects/budamix-ai-agent|Ana]] — Cadastrar 12 SKUs individuais por cor que só existem na planilha, não em `products`: CAR200 (B,P,VD,AZ,AM,R) e TL250 (V,P,Z,R,A,B). Sem cadastro, impossível criar `color_variant` relations para essas 2 famílias. Hoje a cor para a Ana vem só via `base_products.color` (texto), não dá pra recomendar SKU específico. ~15min.
- [17/04] [[projects/budamix-ai-agent|Ana]] — Criar trigger pg_net para `response_corrections` análogo ao `trg_base_product_embedding_sync` (criado 17/04). Hoje re-embedding das correções só dispara via chamada manual à Edge Function `process-correction-embedding`. Risco: correção editada via SQL fica stale. ~10min.
- [17/04] Budamix E-commerce — Sync estoque planilha → Supabase: script Apps Script criado mas falta instalar na planilha. Pedro precisa colar a service_role key e rodar installTrigger(). Doc em docs/SETUP-STOCK-SYNC.md. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Testes de pagamento real pendentes: cartão aprovado, cartão recusado, PIX, estoque insuficiente, frete zerado via DevTools, webhook spoofing. Checklist completo em AUDITORIA-CHECKOUT-MP.md seção 5. → [[projects/budamix-ecommerce]]
- [17/04] ✅ ~~Budamix E-commerce — Reviews reais dos marketplaces~~ → **Feito**: tabelas `product_reviews` + `review_photos` + RLS + bucket Storage `reviews` + 42 fotos uploadadas + 15 reviews seedados (7 SKUs). Home + PDP consumindo via queries React Query. Seção PDP unificada bg-primary teal + cards white/[0.08], fotos clicáveis → MediaLightbox. Commits `54fbef3`, `a0f95a9`, `2742168`, `ebcd852`, `1fb243e`.
- [17/04] Budamix E-commerce — Fase 7 páginas pendentes: /loja (catálogo, 🟡 bloqueia tráfego pago), /termos e /trocas (🟡 legal/gateway), /sobre, /faq, /contato, busca melhorada, dark mode. Issues detalhadas em budamix-issues-fase7.md. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — variant.name ainda é 'Padrão' em 19 variants. Se frontend usar pra seletor de cor/volume na PDP, precisa sincronizar nomes descritivos. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Stock placeholder (=100) em 19 variants. Sync inicial da planilha vai zerar os sem quantidade. Confirmar que planilha está atualizada antes de rodar. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Push pendente: ~80 commits locais à frente de origin/main. Fazer push + deploy no Vercel quando pronto pra produção. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — FREE_SHIPPING_THRESHOLD hard-coded em 4 lugares do frontend (19900). Deveria ler do site_settings. Hook useSiteSettings pendente. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Reversão de estoque em cancelamento/reembolso não implementada. Se order muda pra refunded/cancelled após paid, stock não volta. → [[projects/budamix-ecommerce]]
- [17/04] Budamix E-commerce — Fluxo de avaliação pós-entrega: e-mail automático após entrega com link pra avaliar cada produto (estrelas + texto + upload fotos), token sem login, moderação no admin (active=false→true). Implementar após lançamento. → [[projects/budamix-ecommerce]]
- [17/04] [[projects/budamix-ai-agent|Ana]] — `supabase/seed.sql` do repo `budamix-ai-agent` está stale: nome "Giovana", ~7727 chars. Fonte de verdade (banco `jpacmloqsfiebvagfomt` agent_config.system_prompt) tem "Ana" e 19454 chars após aplicação das 3 recomendações da auditoria 17/04. Sincronizar seed pra evitar regressão se alguém rodar `supabase db reset` local.

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
- [06/04] ✅ Canggu — Reestruturação dados produtos completa (5 fases)
- [06/04] ✅ Canggu — Pipeline vetorial da Ana funcionando (5/5 testes)
- [06/04] ✅ Canggu — Bug envio WhatsApp humano→cliente corrigido
- [06/04] ✅ Canggu — Links de marketplace adicionados ao formulário de produto
- [06/04] ✅ Canggu — Guia de preenchimento para analistas criado e entregue
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
- [17/04] ✅ Ana — Trigger `trg_base_product_embedding_sync` (pg_net) criado via migration `20260417120000`. Antes re-embedding de `base_products` só acontecia quando analista salvava pelo Canggu UI. Agora UPDATE de qualquer origem (SQL, seed, API) dispara `sync-base-product-embedding` (extendida para aceitar `{baseProductId}` além do batch). Validado: hash do embedding muda em 3s após PATCH em `description_short`.
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

*Atualizado: 17/04/2026 — sessão noite (correções canequinha + mapeamento ML + cores base_products + relations)*

---

## Ver também

- [[memory/context/deadlines|Deadlines — Prazos relevantes]]
- [[memory/context/decisoes/2026-04|Decisões — Abril 2026]]

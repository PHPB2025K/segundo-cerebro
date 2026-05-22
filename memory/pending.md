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

> Marco operacional definido por Pedro em 04/05/2026: remover completamente das pendências/inconformidades tudo referente a abril/2026. Pedro vai regularizar abril; a fila passa a contar a partir de 04/05, primeiro dia útil pós-refatoração. Registros históricos permanecem apenas em sessões/decisões, não como pendência ativa.

_Atualizado: 2026-05-22 18:37 BRT — pendências segunda reviews + pedidos atacado_

## 🔥 PRIORIDADE — Operação imediata

- [ ] **Segunda-feira — pedir para Leonardo coletar avaliações dos kits de potes 4 travas nos marketplaces**: Pedro pediu por áudio em 22/05 18:34 BRT para cobrar o Leonardo na segunda-feira (25/05). Escopo: coletar reviews/avaliações reais de clientes na Shopee, Mercado Livre e Amazon especificamente dos kits de potes 4 travas; enviar fotos anexadas pelos clientes nas avaliações, comentários, quantidade de estrelas e identificação do marketplace/produto quando disponível. Objetivo: usar avaliações reais no site da Budamix nesses produtos.
- [ ] **Segunda-feira — retomar automação dos pedidos de atacado via WhatsApp**: Pedro pediu por áudio em 22/05 18:37 BRT para puxar e retomar na segunda-feira (25/05) o status da automação dos pedidos de atacado que chegam no WhatsApp de pedidos. Status atual consolidado: workflow N8N `GB — Pedidos de Venda WhatsApp → Bling Matriz (Fisco)` / ID `T7WT4vGaRuWd0N0Q` está configurado, porém inativo por segurança; Evolution WhatsApp Kobe já foi configurada para `MESSAGES_UPSERT`; rota Fisco/Mission Control `/api/fisco/pedidos-venda-gb` está ativa com segredo, LLM, aliases SKU, validação determinística, idempotência persistente e dry-run validado; pedido real teste 954 foi criado e excluído com sucesso; pendente decidir/reativar teste real controlado, validar resposta no grupo, ampliar aliases e só depois liberar criação automática contínua.
- [ ] **PRIORIDADE MÁXIMA — Planejamento de reposição das canecas + futuro Agente de Compras**: Pedro pediu por áudio em 14/05 18:49 BRT e detalhou em 15/05 18:52 BRT o modelo de trabalho. Escopo: quatro modelos (Tulipa, Paris, Canelada, Reta), seis cores por modelo (rosa, preto, branco, azul, verde, amarelo), histórico dos últimos 3 meses por plataforma e, idealmente, por cor; projeção de compras semanais para os próximos 2 meses, considerando pedido semanal e lead time de 3 a 8 dias. Yasmin entrega Mercado Livre, Lucas entrega Shopee, Leonardo entrega Amazon. Kobe deve cruzar as projeções da equipe com dados reais de marketplace/estoque e produzir versão independente consolidada. Decisão posterior de 15/05 18:56 BRT: primeira rodada será feita manualmente pelo Kobe, mas Pedro já decidiu que quer criar o **Agente de Compras** depois que o processo estiver validado, para uso em vários outros produtos. Projeto registrado em `memory/projects/compras-canecas.md`.
- [ ] **Automação Pedidos de Venda GB — retomar PDF oficial do pedido Bling amanhã**: tratar obrigatoriamente no tópico Telegram **Pedidos Atacado Automação** (`thread_id 10494`). Foco correto definido por Pedro em 14/05: não gerar NF-e/DANFE; precisa baixar o **PDF oficial do pedido de venda**. Mecanismo descoberto via DevTools: formulário web `direcionador`, POST `relatorios/venda.impressao.php`, campos `idVenda=<ID Bling>`, `imprimeDetalhado=N`, `imprimeOrdem=I`, `desmembrarEstrutura=N`. Script criado em `/var/www/mission-control/scripts/bling-order-print-pdf.py` e commitado (`9cdebc3`). Bloqueio restante: rota exige sessão web autenticada do painel Bling; OAuth/API v3 não serve. Amanhã: Pedro fazer logout/login no Bling por cookies terem aparecido no chat, salvar sessão web nova em 1Password como `Bling Web Session - Matriz` ou decidir alternativa segura; Kobe testar com pedido 658/659, validar PDF e integrar no pipeline para envio WhatsApp.
- [ ] **Automação Pedidos de Venda GB — retomar teste controlado amanhã**: tratar obrigatoriamente no tópico Telegram **Pedidos Atacado Automação** (`thread_id 10494`). Workflow N8N `T7WT4vGaRuWd0N0Q` está pausado/inativo; Evolution do WhatsApp Kobe segue configurada para o webhook. Pedido teste real **954** foi criado no Bling Matriz e excluído com sucesso (DELETE 204; verificação 404). Correção já aplicada: N8N envia texto bruto, Fisco/LLM interpreta com mapa SKU/aliases e prompt reforçado para opções marcadas com `(x)`; dry-run posterior confirmou `Estoque 2025`, `Caixa de fita 300` → `CXFIT300M`, cliente/produto encontrados. Amanhã: reativar workflow só quando Pedro pedir, mandar novo teste real, validar estoque/checkbox, alias SKU e resposta no grupo para bloqueios; ampliar `sku-aliases.json` antes de produção contínua.
- [ ] **Meta Business — finalizar configuração da Segunda Venda**: Pedro precisa configurar no Meta Business o número de WhatsApp que será usado com a empresa **Segunda Venda**. Onboarding em andamento; fazer o quanto antes amanhã pela manhã para dar sequência.
- [ ] **Instagram Budamix — finalizar carrosséis fixos no Canva**: concluir os carrosséis fixos que vão no Instagram da Budamix e que já estão sendo feitos pelo Canva.
- [ ] **Corretora OS/OSA — criar grupo WhatsApp com Davi para teste de câmbio**: reunião Granola de 18/05 apresentou corretora com spread abaixo de 1%, atendimento até 21h e Swift/contrato no mesmo dia. Próximo passo combinado: criar grupo WhatsApp com Davi e testar operações menores antes de migrar volume relevante de importação.

## 🚨 URGENTE — Operação / Dados

- [ ] **Estoque Budamix — limpar ops de teste QA no Supabase se Pedro quiser**: teste E2E de 20/05 gerou 14 operações de auditoria reversível com nome `TESTE QA Claude%`; planilha voltou ao estado original, limpeza é opcional/estética.
- [ ] **Estoque Budamix — desativar webhook n8n antigo de PDF quando conveniente**: parser PDF local já substituiu o endpoint n8n quebrado; webhook antigo pode ser pausado/removido no painel para evitar uso acidental.
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

## 🚨 Amazon Ads / BidSpark

- [ ] **Meta Ads — validar renovação/funcionamento após 18/05/2026**: digest Spark de 18/05 registrou que a data estimada de expiração do token Meta Ads foi atingida. Antes de depender da API para análise/automação, validar se o token foi renovado/segue funcional; se falhar, escalar correção de autenticação.

- [ ] **Amazon Ads/BidSpark — corrigir auditoria interna de ações**: execução Tulipa 12/05 deu 7/7 success na API, mas `amazon_ads_actions_log` falhou por FK/constraints (`round_id`/`entity_id`). Corrigir fluxo/schema antes da próxima rodada manual para não perder trilha oficial no BidSpark.

- [ ] **Amazon Ads — analisar grupo crítico Potes Redondos Plástico**: D+7 mostrou piora (ACoS 13,3% → 32,3%), provável escala forte demais principalmente Exact.
- [ ] **Amazon Ads — ajuste fino Jarra Medidora e Potes Herméticos Vidro**: Jarra ainda dentro da meta mas piorou; Potes Vidro melhorou eficiência mas ainda acima da meta.
- [ ] **Amazon Ads — não cortar mais Potes Tampa Bambu por enquanto**: eficiência melhorou, mas gasto/venda diária caíram; risco de ter apertado volume demais.
- [ ] **Amazon Ads — investigar elegibilidade/listing/Buy Box/categoria de Kits Microfibra e Abraçadeiras Nylon**: experimentos 03/05 ficaram com 0 impressões/0 cliques/0 vendas; problema parece estrutura/elegibilidade, não bid.
- [ ] **Amazon Ads/BidSpark — revisar logs de action_type**: diferenciar escala Exact vs Broad/Alcance/Auto/Product Targeting para auditoria das ações.

## 🚨 Canggu / Ana

- [ ] **Canggu/Ana — reabrir investigação do dispatch em conversas reais após falsa recuperação**: em 22/05 ficou claro que o fluxo não está 100% recuperado. As mensagens reais de clientes entram na Canggu/Supabase, a mensagem automática inicial de origem/canal é enviada e até há análise de imagem registrada, mas não nasce a resposta LLM posterior em casos reais. Casos confirmados: **Edneia** (21/05 ~15:16–15:18 BRT, avaria de canecas) e **Carolina** (21/05 ~23:17–23:56 BRT, canecas quebradas/rachadas, TikTok Shop) ficaram sem follow-up. Teste controlado do Kobe respondeu, então o bug parece intermitente ou dependente do caminho real (burst de mensagens, imagens, debounce/buffer, escalonamento ou divergência entre produção e repo). Próximos passos: reproduzir com número controlado simulando o fluxo completo real, auditar `webhook-whatsapp` → `process-message` → dispatcher nesses casos, e só declarar recovery quando houver `sender=agent` posterior com `tokens_used` em conversa real. Manter também a pendência anterior de adicionar camada defensiva no validador contra frases tipo “cadastro do produto”, “verificar internamente” e “atualizar o anúncio”.
- [ ] **Canggu — manter repo canônico reconciliado após hotfix ML**: repo `PHPB2025K/canguu` recebeu commit `eb76d3f`; quando Pedro voltar o repo para privado, garantir que a VPS/token mantém acesso de leitura/escrita para próximos patches e CI/CD.
- [ ] **Canggu — trocar senha temporária do admin** no login do admin. Ação do Pedro.
- [ ] **Canggu — corrigir type TS pré-existente em `_shared/evolution-api.ts`**: `EvolutionMessageContent` é referenciado mas o tipo real chama `EvolutionMessageData`. Detectado no `deno check` durante incidente Ana 24/7; edge deploya mesmo com warning, mas limpar no próximo bloco Canggu.
- [ ] **Canggu ML — editar manualmente resposta com frase forbidden no produto MLB3343832496** ("Jogo 6 Canequinha 100ml"). Resposta atual contém "Por favor entre em contato conosco para conhecer outros modelos disponíveis!" enviada às ~15:00 BRT de 05/05 antes do hard-block estar ativo em produção. Não é possível remover via API; só edit manual no painel ML. Sugestão de texto novo já dada na sessão (~187 chars, sem frases forbidden).
- [ ] **Canggu ML — marcar 👎 na resposta do MLB3343832496 e colar correção** no painel Canggu pra alimentar `process-correction-embedding`. Vira embedding e blinda perguntas semelhantes futuras (ex: "tem maior?", "tem com mais ml?").
- [ ] **Canggu — decidir redirect www↔apex em `canggu.com.br`**. Hoje ambos servem conteúdo idêntico (duplicate content, ruim pra SEO). Recomendação CC: www → apex. Configurável via `vercel.json` ou settings de domínio Vercel.
- [ ] **Canggu — atualizar GitHub Actions Node 20 → 24** em `.github/workflows/deploy-edge-functions.yml`. Deadline forçada: Node 20 removido dos runners em **16/09/2026**. Mudança trivial (1 linha por action). Sem urgência mas registrar.
- [ ] **Canggu — adicionar instruções no system prompt da Ana** para `[Sticker recebido]`, `[Localização compartilhada: ...]` e `[Contato compartilhado: ...]`, evitando respostas genéricas.
- [ ] **Canggu — B1 segurança**: service_role JWT em arquivos tracked, `LOVABLE_API_KEY` legado, CORS aberto, `verify_jwt` em funções internas. Estimativa ~3 dias. (Ghost function `test-search` ✅ removida em 05/05.)
- [ ] **Canggu — B3 resiliência restante**: retry em `classifyIntent`/`generateResponse`, UNIQUE index `whatsapp_message_id`, dedup e fallback textual.
- [ ] **Canggu — estender ajuste de tom pra `process-message`** (Ana no WhatsApp). Tom natural já aplicado no ML; equalizar no WhatsApp se Pedro confirmar que lá também soa formal.
- [ ] **Canggu ML — monitorar próximas perguntas reais após hotfix `ml-webhook`**: confirmar que nenhuma rota volta a enviar “entre em contato”, “fale conosco”, “para mais detalhes” ou “nossa equipe técnica”. Se escapar, auditar todas as Edge Functions Supabase que postam no ML e ampliar o guard determinístico.

## 🚨 RH / Ponto Certo

- [ ] **RH — criar/corrigir política canônica de sábado/domingo**: digest RH de 16/05 apontou que a regra de sábado/domingo está sendo confirmada por materiais operacionais alternativos, mas o documento canônico não está disponível. Formalizar quando a frente de governança RH entrar no bloco.

- [ ] **RH — acompanhar lote aprovado do Monitor Ponto Semanal 11/05 e casos bloqueados 18/05–20/05**: follow-up deve cobrar apenas itens realmente abertos após pré-checagem de cobertura por ajuste, justificativa ou batida real. Em 18/05, validação indicou Leonardo 1/2 coberto, Mateus 5/6 coberto e Sandra 0/5 coberto; digest RH também registrou Guilherme, Lucas, Mateus e Sandra bloqueados para contato semanal até orientação/aprovação do Pedro. Em 19/05, compliance adicionou Guilherme com marcações incompletas, Lucas e Leonardo com intervalo <1h e Franciele com marcações atípicas. Em 20/05, novas pendências: Franciele/Geziele/Guilherme sem saída registrada e Guilherme/Leonardo/Lucas com intervalo <1h. Se inbounds continuarem invisíveis mesmo após suporte `@lid`, investigar sincronização da instância Evolution RH.
- [ ] **RH — compliance 15/05 intervalos abaixo de 1h**: Geziele, Guilherme, Leonardo e Lucas tiveram intervalo de almoço abaixo de 1h no check de 15/05; tratar como risco trabalhista/operacional no acompanhamento, sem liberar WhatsApp proativo genérico.
- [ ] **RH — guard de WhatsApp proativo ESTENDIDO INDEFINIDAMENTE (até 2027-01-01)** em `/tmp/rh-whatsapp-block.json`. Pedro pediu 05/05 14:04 BRT que nenhum cron/agente RH dispare proativos a funcionários até liberação explícita. Em 11/05 10:15 BRT, Pedro liberou **apenas o escopo específico** dos problemas de ponto reportados no Monitor Ponto Semanal de 11/05 sobre a semana 04/05–09/05, até resolução completa com Fran, Leonardo, Lucas, Mateus e Sandra. Exceções técnicas: `--allow-rh-reply` permite respostas inbound; `--allow-rh-approved-case` permite follow-ups desse lote aprovado. Proativo genérico segue bloqueado. Crons em risco que continuam habilitados mas inofensivos enquanto o guard ativo: `RH Compliance Check` (diário 19h BRT), `Monitor Ponto Semanal` (segundas 10h BRT), `Ponto Certo - QR Code Refresh` (diário 03h, não envia WhatsApp). Validado: proativo → `BLOCKED_RH`; reply → `SENT`; caso aprovado → `SENT`.
- [ ] **Ponto Certo — deploy produção do módulo Conversas RH** se ainda estiver apenas local: build, publicar na VPS e reiniciar PM2 `ponto-certo`.
- [ ] **RH — acompanhar feedback da Yasmin** sobre recebimento correto dos 2 chunks da mensagem inaugural reenviada com `linkPreview: false`.
- [ ] **RH — acompanhar primeiras respostas dos funcionários** às mensagens inaugurais; `rh-poller` e `rh-stuck-detector` devem capturar falhas silenciosas.
- [ ] **RH — datas de admissão dos funcionários** para cálculo futuro de férias.
- [ ] **RH — padrão do contador FOUR/Suellen** para espelho de ponto.

## 🚨 Gestão / Jurídico / Contratos

- [ ] **Daily Sales Report v2 — aguardar liberação explícita para envio real aos funcionários**: envio real para Lucas/Yasmin/Leonardo continua bloqueado até liberação explícita. Execução Trader de 21/05 analisando 20/05 BRT terminou em preview `APPROVED_WITH_REMARKS`, sem envio externo. Total marketplaces: R$ 11.973,29, 222 pedidos, ticket médio R$ 53,93. Lucas/Shopee ficou bloqueado por erro factual de percentual Store (~45% correto vs 49% escrito); Yasmin/ML aprovado; Leonardo/Amazon aprovado com ressalva menor. Manter `fallback_deterministic_allowed=false` e bloqueio fail-closed se camada LLM falhar.
- [ ] **Daily Sales Report v2 — corrigir/reexecutar Lucas/Shopee e decidir critério de promoção**: corrigir Store para ~45% do GMV Shopee, recalcular percentuais derivados contra pacote validado, reprocessar Slack Writer e QA; registrar omissões de Top Produtos/residuais quando existirem; decidir se produção exige ciclo `APPROVED` sem ressalvas ou aceita `APPROVED_WITH_REMARKS` sem críticos/maiores. Revalidar Shopee/Amazon Rules Watch antes de usar regra/taxa como causa forte.

- [ ] **Adapta — aguardar retorno sobre cobranças recorrentes**: Pedro recebeu mensagem pronta em 07/05 para enviar como PEDRO HENRIQUE PERON BROGLIO. Se a empresa negar cancelamento/estorno, próxima frente é contestação pelo banco/cartão usando descritor `TAR PLANO ADAPT` e valores R$ 497,00/R$ 126,75.
- [ ] **Guarani Sistemas — preparar minuta de distrato e só pagar após aceite/assinatura**: em 13/05, Guarani aceitou a proposta global de **R$ 7.500,00 à vista** e confirmou baixa/quitação dos 7 títulos/NFs em aberto, sem protesto/negativação/cobrança externa, com isenção do aviso prévio. Próximo passo: enviar minuta de distrato para análise. Ponto crítico: a minuta deve preservar **quitação integral e definitiva**, **sem saldo remanescente/cobrança futura**, **sem reconhecimento de dívida**, e evitar que a cláusula “distrato parte da sua empresa por ausência de mão de obra” vire admissão ampla de culpa. Recomendação: não pagar antes de distrato aprovado/assinado ou, no mínimo, aceite escrito inequívoco dos termos finais.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **DRE abril/2026 — fechar U15 (Descontos Concedidos) com critério estrito por marketplace**: prioridade alta definida por Pedro em 05/05. ML já ficou consistente em **R$ 5.061,14 (4,19%)**; Amazon precisa fechar por `item-promotion-discount` sem frete promocional; Shopee precisa reclassificação porque o parcial amplo de `seller_discount`/promoções explodiu para **R$ 63.715,45 (24,79%)** e foi marcado como suspeito. **Não usar** o consolidado provisório de **R$ 68.776,59** no DRE até concluir a triagem.


## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio

- [ ] **Budamix E-commerce — reativar kits de potes 4 travas quando Pedro liberar**: em 20/05 22:12 BRT, Pedro pediu para manter temporariamente desativados 8 kits de potes 4 travas no site. Reativar somente com liberação explícita, nos mesmos slugs/produtos.
- [ ] **Banner triplo Instagram Budamix — Pedro escolher Capa 01 v1/v2 e inserir fotos no Canva**: projeto HTML/CSS foi criado com 3 capas 4:5; Capa 01 tem duas versões e Capa 02/03 aguardam fotos dos potes e da Morgana via Canva.
- [ ] **Social Studio Reborn — Fase C C2**: construir página `/admin/social/conta` (status da conta, botão OAuth, callback handler). C1 já fechado em 07/05 (`d6384bd`).
- [ ] **Social Studio Reborn — pré-requisitos Meta antes do C3**: Pedro criar App Business novo no Meta Developers, adicionar Instagram Graph API + Facebook Login, configurar redirect URIs/permissões e setar `META_APP_ID`/`META_APP_SECRET` nos Edge Secrets do Supabase. Kobe/CC deve guiar tela-a-tela quando Pedro chamar.
- [ ] **Social Studio Reborn — Fase C publicação real**: C3-C8 (OAuth callback, executor Meta Graph, tick real com trava temporária `TESTE INTERNO`, C5b remove trava, UI pós-publicação, refresh token e smoke final).
- [ ] **Social Studio Reborn — Fase D Métricas + Dashboard** (~2-3 dias): edge `collect-instagram-metrics`, dashboard, KPIs/tabela/gráfico/export CSV.
- [ ] **Social Studio — avaliar delete das branches antigas em 2026-06-05**: `feature/social-studio-pr2` e `feature/social-studio-pivot-copy-only` preservadas por 30 dias após pivot; apagar só depois se não houver necessidade histórica.
- [ ] **Blog Budamix — inspeção visual manual do post de teste** id `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` (pilar `receber-visitas`) no `/admin/blog`; após Pedro inspecionar cover/supports/pins, deletar o post de teste.
- [ ] **Blog WF0 — polir payload de resposta**: hoje retorna `pillar_focus=null` no response mesmo quando o foco foi aplicado internamente. Cosmético; funcional OK.
- [ ] **Rotacionar PAT Supabase exposto em chat**: token `sbp_1d24...` em `~/.mcp.json` continua exposto no transcript da sessão de 05/05 (Pedro escolheu pular a rotação pra destravar primeiro o fluxo do C4). Pedro decidiu não rotacionar; dívida anotada. Revogar em https://supabase.com/dashboard/account/tokens quando tiver janela. Risco prático: PAT dá acesso total a todos projetos Supabase do Pedro.
- [ ] **Supabase CLI — investigar perms da conta**: `supabase link --project-ref jtczupudieeogzspdqae` falhou em 05/05 com "Your account does not have the necessary privileges". Migration do Social Studio rodada via Dashboard manualmente. Resolver se virar fluxo recorrente.
- [ ] **Vercel Token - Budamix Ecommerce** — item no 1Password `notesPlain` ainda incompleto; GitHub→Vercel auto-deploy já reduz bloqueio, mas token ainda é útil para rollback/hotfix CLI.
- [ ] **Vercel Preview Env** — configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas.

## 🎨 Design / Skills locais

- [ ] **Paper Design — carrossel Profundo Budamix**: terminar Cards 6 e 7 no Paper (`Scratchpad`, page `1-0`) usando o briefing salvo na sessão CC local de 02/05. Não confundir com os 96 templates oficiais concluídos em 03/05.
- [ ] **Budamix Marca — validar uso dos 96 templates oficiais** em projeto real e manter nota `business/marketing/marca/templates-carrossel-paper.md` como referência canônica.
- [ ] **ElevenLabs / video-use — higiene de keys**: deletar/revogar as duas keys antigas que circularam no transcript, manter key válida restrita a Speech to Text e rotacioná-la nas próximas semanas.

## 🚨 Infraestrutura e autenticações degradadas

- [ ] **Mission Control — n8n usage tracking em `/costs` (retomar 15/05)**: investigação de 14/05 confirmou que OpenClaw/GPT-5.x roda via subscription Pro 5x, mas n8n usa API keys reais. Próximos passos: habilitar `saveDataSuccessExecution='all'` nos 3 workflows LLM, criar coletor `collect-n8n-usage` com cron 15min, adicionar pricing de `gpt-5.2`, `text-embedding-3-small`, `tts-1-hd` e `claude-sonnet-4-6`, e criar categoria n8n em `/costs`.
- [ ] **Mission Control — ativar painel Daily Sales Pipeline em produção**: Builder concluiu em 17/05 painel visual para o pipeline Daily Sales v2/Slack com timeline de 9 etapas, filtros por data/recipient, visualização prompt/output, edição segura allowlisted com backup e auto-refresh. Build validado; falta restart controlado do Mission Control e smoke test das rotas novas.
- [ ] **Mission Control — 12 módulos restantes sem PRD próprio**: após 14/05, 11/23 módulos estão fechados (Dashboard, System, Files, Agents, Memory, Office 3D, Activity, Cron, Sessions, Skills, Costs). Restam: Tasks, Agents detail, Logs, Terminal, Git, Workflows, Search, Analytics, Reports, Settings, Calendar, About/Actions.
- [ ] **Mission Control — refinamentos pós-14/05**: KG sync Mac→VPS via cron rsync 1h para liberar busca semântica; filtro `/memory?agent=`; refinar regex de detecção de `botToken` em `auth-profiles.json`.

- [ ] **OpenClaw fallback — adicionar Anthropic como 3º fallback**: `anthropic:default` está configurado, mas fora de `agents.defaults.model.fallbacks`; após upgrade para ChatGPT Pro não é urgente, mas evita queda total se o mesmo auth profile OpenAI estourar em pico.
- [ ] **WhatsApp Health Check — substituir N8N quebrado por script VPS versionado**: Pedro pausou Bling Filial em 21/05 por não estar usando esse Bling. Próximo ponto ativo é a tabela `whatsapp_health_checks`, sem escrita desde 07/05. Workflow N8N original ficou inutilizável após refactor 11 nodes → 2 nodes, export versionado original sumiu, e acesso ao N8N/Evolution a partir da VPS está bloqueado por Cloudflare 1010. Decisão operacional recomendada: criar script Python versionado em cron na VPS, gravando direto no Supabase. Defaults aprovados salvo ajuste do Pedro: alerta no Telegram/tópico Alertas e frequência 15min. Evolution-specific checks podem continuar degradados enquanto Cloudflare bloquear, mas o health check geral deixa de depender do N8N.
- [ ] **Bling Token Refresh — Filial ADIADO por decisão do Pedro**: em 21/05, Pedro decidiu deixar essa integração como está porque não está usando esse Bling no momento. Não gastar bloco operacional nisso agora. Manter apenas como risco conhecido: Filial segue com erro 403/inativa e fluxos fiscais dependentes da Filial não devem avançar até reabrirem essa frente. Próximo foco de infra/automações é o WhatsApp Health Check.
- [ ] **Security Audit / Firewall VPS** — auditoria de 10/05 06:01 BRT executou e substituiu a pendência antiga de timeout. Achados: `ufw` não instalado/disponível; Fail2ban OK (`sshd`, maxretry=5); SSH sem senha; portas públicas além de 22/80/443 incluem 3000, 3050, 3091, 8084 e 8090. Próximo passo: definir política de firewall/Traefik sem risco de lockout antes de qualquer mudança.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password.
- [ ] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; se Pedro quiser reativar essa rota, precisa reescanear QR Code. Evolution API/histórico segue separado e funcional.
- [ ] **Fisco / OpenClaw** — diagnosticar o bloqueio do `sessions_spawn` com `agentId=fisco` retornando `allowed: none` e restaurar o roteamento direto do agente.
- [ ] **Fisco — processo mensal de abatimento Matriz**: antes de usar saldo Matriz como excedente, consultar NFs B2B/atacado emitidas pela Matriz no período e abater por SKU/componente.

## 🟡 Observação / estabilidade


- [ ] **Daily GitHub Backup — investigar timeout de 22/05 00:02 BRT**: cron falhou por timeout (`cron: job execution timed out`). Últimos crons recorrentes posteriores checados às 02:00 BRT estavam OK, e o Watchdog GitHub Sync das 01:42 BRT rodou em status OK com alerta já enviado; investigar no próximo bloco se o backup voltar a falhar.
- [x] ~~**Organização Noturna Silenciosa — investigar timeout da rodada anterior**~~ → **RESOLVIDO 21/05.** A falha isolada de 19/05 02:00 BRT não se repetiu: as rodadas de 20/05 e 21/05 concluíram, e os últimos crons recorrentes recentes estavam OK. Manter apenas monitoramento normal; reabrir se houver novo timeout.
- [ ] **Watchdog/Monitor Ponto/RH crons** — revisar timeouts/fallbacks em jobs com histórico de falha por timeout/model not found.

## 🟡 Futuro aprovado / não imediato

- [ ] **Budamix Blog — Pinterest API/OAuth** — ativar postagem automática no Pinterest quando padrão de artigos e imagens estiver validado. Por enquanto pins ficam como assets no Admin.
- [ ] **Budamix E-commerce — conteúdo real das páginas stub** `/faq`, `/contato`, `/termos`, `/trocas-e-devolucoes`; hoje são Coming Soon/noindex.
- [ ] **Newsletter Budamix** — formulário ainda não persiste email; precisa backend real.


## Nota para briefing matinal — itens estagnados >7 dias
_Gerado pela organização noturna de 22/05 02:00 BRT._

- Revalidar no briefing apenas os itens que continuam bloqueados por decisão/input do Pedro: reposição de canecas/Agente de Compras, Pedidos Atacado/PDF oficial Bling, teste controlado da automação de pedidos, Meta Business Segunda Venda, carrosséis fixos do Instagram Budamix, grupo OS/OSA com Davi, escolha da Capa 01 do banner triplo, aliases/POT1BB/KFJ003 do Estoque Budamix, Social Studio Meta App/secrets, Canggu senha/admin + hard-block defensivo, DRE abril U15, Guarani distrato, Bling Filial 403 pausado, firewall VPS e rotação de tokens expostos.
- Crons recorrentes mais recentes checados em 22/05 02:00 BRT: Claude Contingency Guard (01:55 BRT), job-monitor (01:54 BRT) e Watchdog — GitHub Sync Segundo Cérebro (01:42 BRT) estavam em status OK. O Watchdog GitHub Sync gerou alerta, mas não falhou.
- Falha nova a investigar sem interromper Pedro: Daily GitHub Backup às 00:02 BRT terminou em timeout. Se repetir, tratar como frente de estabilidade/backup; por ora ficou anotado em Observação/estabilidade.
- Sessões antigas >30 dias por data de arquivo verificadas: 14/04, 15/04-audit, 16/04, 17/04, 19/04, 20/04 e 21/04 foram mantidas por falta de marcação inequívoca de consolidação completa; não deletar até a consolidação diária/profunda confirmar.
- Não reabrir pendências antigas de abril/2026 que Pedro já mandou limpar; manter histórico fora da fila ativa.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **PCM001 peso embalado / foto 9 / custos refinados** — dados finais ainda pendentes.
- [ ] **SimulImport — validar cenários reais** — Pedro testar com importações dele.
- [ ] **Canggu/Ana B2/B5/B6** — blocos não urgentes de observabilidade, governança e cleanup seguem aguardando repriorização.
- [ ] **Fisco** — product-packaging.json, limpeza de produtos origem=0, CC-e/NFs antigas e validações Bling Filial seguem abertas.
- [ ] **Security hardening extra**, **Lovable sync**, **Stripe live key**, **LinkedIn integração** seguem fora da fila imediata.
- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem movimentação material >14 dias; manter como backlog financeiro antes de refazer março.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto. Sem movimentação material >14 dias.
- [ ] **Mapeamento semanal DRE março** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE. Sem movimentação material >14 dias.


---
_Última organização: 2026-05-22 02:00 BRT._

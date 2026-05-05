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

_Atualizado: 2026-05-05 ~21:30 BRT — sessão Social Studio PR2 C4-C5-C6_

## 🚨 URGENTE — Operação / Dados

- [ ] **Estoque Budamix — retomar deploy em produção** (pause em 05/05 22h aguardando decisão de credencial GitHub na VPS). PR1+PR2+PR3a no repo `PHPB2025K/estoque-budamix` mas produção ainda roda build de 13/04. Backup feito em `/var/www/estoque-budamix.backup-20260505-2143/`, `.env` preservado, plano de remediação aprovado com 5 salvaguardas. Bloqueado no Bloco 4 (`git fetch` falhou com 403). Recomendação: Deploy Key SSH read-only no repo. Ver [[memory/sessions/2026-05-05]] Session Extract estoque-budamix + memory local `estoque_budamix_deploy_checkpoint.md`.
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

## 🚨 RH / Ponto Certo

- [ ] **RH — guard de WhatsApp proativo ESTENDIDO INDEFINIDAMENTE (até 2027-01-01)** em `/tmp/rh-whatsapp-block.json`. Pedro pediu 05/05 14:04 BRT que nenhum cron/agente RH dispare proativos a funcionários até liberação explícita. Exceção mantida: `--allow-rh-reply` permite respostas inbound. Crons em risco que continuam habilitados mas inofensivos enquanto o guard ativo: `RH Compliance Check` (diário 19h BRT), `Monitor Ponto Semanal` (segundas 10h BRT), `Ponto Certo - QR Code Refresh` (diário 03h, não envia WhatsApp). Quando liberar: editar `until_epoch` ou deletar arquivo. Validado via dry-run: proativo → `BLOCKED_RH`; reply → passa.
- ✅ ~~**Ponto Certo — DNS do domínio novo**: criar/apontar A record de `ponto.budamix.com.br` para `187.77.237.231`~~ → **RESOLVIDO 05/05.** Pedro criou A record no Registro.br, DNS propagou nos resolvers públicos, CC local restartou Traefik na VPS pra forçar reemissão do cert ACME (1ª tentativa havia falhado em 04/05 12:39 UTC com NXDOMAIN). Cert Let's Encrypt emitido, servidor responde HTTPS 200. Cache de DNS em provedores brasileiros pode levar horas pra atualizar — workaround: trocar pra DNS Cloudflare/Google ou tentar via 4G. Pendência menor: deletar entrada órfã `pontocerto.budamix.com.br` criada por engano. → [[memory/sessions/2026-05-05#Ponto Certo — DNS + cert SSL `ponto.budamix.com.br` resolvidos (CC local)]]
- [ ] **Ponto Certo — deploy produção do módulo Conversas RH** se ainda estiver apenas local: build, publicar na VPS e reiniciar PM2 `ponto-certo`.
- [ ] **RH — acompanhar feedback da Yasmin** sobre recebimento correto dos 2 chunks da mensagem inaugural reenviada com `linkPreview: false`.
- [ ] **RH — acompanhar primeiras respostas dos funcionários** às mensagens inaugurais; `rh-poller` e `rh-stuck-detector` devem capturar falhas silenciosas.
- [ ] **RH — datas de admissão dos funcionários** para cálculo futuro de férias.
- [ ] **RH — padrão do contador FOUR/Suellen** para espelho de ponto.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.

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

## 🚨 Jurídico / Contratos

- [ ] **Guarani Sistemas — enviar o email formal de contestação/distrato** com pedido de suspensão de protesto, memória de cálculo aberta e proposta **sem reconhecimento de dívida**.
- [ ] **Guarani Sistemas — reunir prova do congelamento/prorrogação com o Junior** (emails, WhatsApp, histórico) para sustentar contestação forte e eventual redução adicional/teses de cobrança zero.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **PCM001 peso embalado / foto 9 / custos refinados** — dados finais ainda pendentes.
- [ ] **SimulImport — validar cenários reais** — Pedro testar com importações dele.
- [ ] **Canggu/Ana B2/B5/B6** — blocos não urgentes de observabilidade, governança e cleanup seguem aguardando repriorização.
- [ ] **Fisco** — product-packaging.json, limpeza de produtos origem=0, CC-e/NFs antigas e validações Bling Filial seguem abertas.
- [ ] **Mission Control DNS/customização**, **Security hardening extra**, **Lovable sync**, **Stripe live key**, **LinkedIn integração** seguem fora da fila imediata.

---
_Última organização: 2026-05-04 23:30 BRT._

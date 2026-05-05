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

_Atualizado: 2026-05-05 02:00 BRT — organização noturna silenciosa_

## 🚨 URGENTE — Operação / Dados

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
- [ ] **Canggu — adicionar instruções no system prompt da Ana** para `[Sticker recebido]`, `[Localização compartilhada: ...]` e `[Contato compartilhado: ...]`, evitando respostas genéricas.
- [ ] **Canggu — B1 segurança**: service_role JWT em arquivos tracked, ghost function `test-search`, `LOVABLE_API_KEY` legado, CORS aberto, `verify_jwt` em funções internas. Estimativa ~3 dias.
- [ ] **Canggu — B3 resiliência restante**: retry em `classifyIntent`/`generateResponse`, UNIQUE index `whatsapp_message_id`, dedup e fallback textual.
- [ ] **Canggu ML — monitorar próxima pergunta real do ML** para confirmar hard-block contra “entre em contato conosco”. Se escapar, ampliar regex/padrões.

## 🚨 RH / Ponto Certo

- [ ] **RH — 05/05 reativação/normalização segura**: remover/expirar guard temporário de 04/05 apenas para proativos autorizados/rotina normal; manter exceção `--allow-rh-reply` para respostas inbound e não disparar alinhamentos retroativos sem aprovação.
- [ ] **Ponto Certo — DNS do domínio novo**: criar/apontar A record de `ponto.budamix.com.br` para `187.77.237.231`; Traefik já aceita o host e validação local retornou HTTP 200.
- [ ] **Ponto Certo — deploy produção do módulo Conversas RH** se ainda estiver apenas local: build, publicar na VPS e reiniciar PM2 `ponto-certo`.
- [ ] **RH — acompanhar feedback da Yasmin** sobre recebimento correto dos 2 chunks da mensagem inaugural reenviada com `linkPreview: false`.
- [ ] **RH — acompanhar primeiras respostas dos funcionários** às mensagens inaugurais; `rh-poller` e `rh-stuck-detector` devem capturar falhas silenciosas.
- [ ] **RH — datas de admissão dos funcionários** para cálculo futuro de férias.
- [ ] **RH — padrão do contador FOUR/Suellen** para espelho de ponto.

## 🔥 PRIORIDADE IMEDIATA — Financeiro

- [ ] **DRE Abril/2026 — U15 Descontos Concedidos PRIMEIRO**: concluir apuração de U15 com Shopee/Amazon em batch antes de mexer na v4 da U44. Prioridade definida pelo Pedro em 05/05.
- [ ] **DRE Abril/2026 — U44 v4 limpa DEPOIS do U15**: refatorar U44 atual R$ 115.531,68 em duas linhas: U44 limpa (comissão + taxa fixa + frete líquido seller quando aplicável) e nova “Outras Taxas Marketplace”. Regras: mover ML R$ 6.156,26 (disputas/cancelamentos R$ 3.769,11 + taxas reembolso R$ 2.387,15) para Outras; manter Shopee R$ 60.132,34 em U44 sem linha separada de frete; reconciliar residual Amazon (~R$120–258); soma das duas linhas deve bater R$ 115.531,68 ±R$100 e EBITDA não pode mudar.
- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio

- [ ] **Blog Budamix — inspeção visual manual do post de teste** id `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` (pilar `receber-visitas`) no `/admin/blog`; após Pedro inspecionar cover/supports/pins, deletar o post de teste.
- [ ] **Blog WF0 — polir payload de resposta**: hoje retorna `pillar_focus=null` no response mesmo quando o foco foi aplicado internamente. Cosmético; funcional OK.
- [ ] **Social Studio Carrossel — decidir próxima fase**: Pedro escolhe entre Fase 4 publish IG (1 semana) ou Fase 5 hardening (1 semana). Recomendação técnica: Fase 5 primeiro se o objetivo for estabilidade; Fase 4 primeiro se publicação automática virar prioridade comercial.
- [ ] **Social Studio Carrossel — Pedro rodar smoke E2E manual pela UI** após o fechamento da Fase 1 para validar a experiência real ponta a ponta no app.
- [ ] **Social Studio Carrossel — Pedro identificar app Meta existente da Budamix e gerar long-lived token IG**; Kobe coloca no Supabase Vault quando recebido.
- [ ] **Social Studio Carrossel — Fase 5 backlog**: container warm para cold start render, JPG encoder, QA visual diff CI, rate limiting + audit log, tradução de erros Meta.
- [ ] **Vercel Token - Budamix Ecommerce** — item no 1Password `notesPlain` ainda incompleto; GitHub→Vercel auto-deploy já reduz bloqueio, mas token ainda é útil para rollback/hotfix CLI.
- [ ] **Vercel Preview Env** — configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas.

## 🎨 Design / Skills locais

- [ ] **Paper Design — carrossel Profundo Budamix**: terminar Cards 6 e 7 no Paper (`Scratchpad`, page `1-0`) usando o briefing salvo na sessão CC local de 02/05. Não confundir com os 96 templates oficiais concluídos em 03/05.
- [ ] **Budamix Marca — validar uso dos 96 templates oficiais** em projeto real e manter nota `business/marketing/marca/templates-carrossel-paper.md` como referência canônica.
- [ ] **ElevenLabs / video-use — higiene de keys**: deletar/revogar as duas keys antigas que circularam no transcript, manter key válida restrita a Speech to Text e rotacioná-la nas próximas semanas.

## 🚨 Infraestrutura e autenticações degradadas

- [ ] **Security Audit - Semanal** — último run conhecido em 03/05 06h BRT falhou com timeout/status `error`; investigar no próximo bloco operacional.
- [ ] **core-audit** — boot check de 05/05 09:01 BRT encontrou último run com status `error`; investigar junto com o Security Audit antes de tratar auditoria como saudável.
- [ ] **Bling Token Refresh** — heartbeat de 05/05 13:52 BRT encontrou último run com timeout; execuções anteriores indicavam Matriz OK e Filial com HTTP 403/empresa inativa. Investigar com Fisco antes de depender de refresh automático da Filial.
- [ ] **ML Fees Monitor** — último run conhecido em 04/05 10h BRT falhou com timeout/status `error`; investigar se foi timeout de web fetch/modelo e ajustar timeout/escopo antes do próximo run semanal.
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
_Última organização: 2026-05-05 02:00 BRT._

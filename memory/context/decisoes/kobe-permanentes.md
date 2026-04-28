---
title: "Decisões permanentes importadas do Kobe"
created: 2026-04-28
type: context
status: active
tags:
  - memory
  - context
  - kobe-import
---

# Decisões Permanentes

_Decisões do Pedro que não mudam. Consultar antes de sugerir algo que contradiga._

## Negócio
- **Estratégia de mix:** Poucos produtos, alto volume. Kits, combos e variações para ranqueamento. (não sugerir "ampliar catálogo com 50 SKUs novos")
- **Marca própria:** Budamix. Registrada no INPI. Usar em tudo que for produto próprio.
- **Verticalização MDF:** Comprou máquina laser para fabricação própria. Decisão tomada, não precisa validar de novo.


## Blog Budamix — Diretriz Editorial Permanente (2026-04-27)
- O Blog Budamix é um canal consultivo sobre **vida doméstica prática**, não um catálogo de produtos disfarçado.
- Posicionamento: **blog de casa prática, bonita e bem cuidada**. A Budamix aparece como marca curadora; venda é consequência da confiança, não objetivo do artigo.
- Público principal: mulheres 25–45 anos, classe B/C, urbanas, muitas em apartamento, buscando praticidade, custo-benefício e soluções acessíveis para casa/cozinha/rotina familiar.
- Produto Budamix só aparece quando for natural e relevante. `related_products` é opcional e pode ficar vazio.
- Meta editorial: no máximo **30–40%** dos artigos publicados mencionam produto/categoria diretamente; o restante deve ser 100% consultivo.
- Cozinha é centro de gravidade (~55%), mas casa geral também é território (~45%).
- Pilares oficiais: (1) Cozinha prática do dia a dia, (2) Conservação/aproveitamento de alimentos, (3) Marmita/lancheira/comida fora, (4) Organização de espaços, (5) Limpeza/manutenção do lar, (6) Casa pequena/apartamento, (7) Rotina familiar/crianças/pets, (8) Receber em casa/momentos especiais, (9) Consumo consciente/economia doméstica, (10) Datas sazonais/presentes úteis.
- Regras WF0: cada rodada deve cobrir pelo menos 3 pilares diferentes; no máximo 1 pauta por rodada sobre potes/despensa/organização direta de cozinha; remover qualquer instrução de “priorize produtos Budamix”.
- Tom: consultivo, útil, humano, direto, sem publieditorial disfarçado. CTA leve: “Conheça mais ideias para sua casa na Budamix”, sem empurrar SKU.
- Documento completo: `openclaw/agents/kobe/memory/projects/budamix-blog-editorial.md`.

## Importação
- **Trading China:** Skiway (Yiwu). Relação consolidada. Não sugerir trocar sem motivo forte.
- **Trading Brasil:** Open Trade (Itajaí). Relação consolidada (~2 anos).
- **Rota:** Yiwu → Shanghai → Itapoá → Pedreira. CNPJ em Itajaí para benefícios fiscais de SC.

## Operação
- **Formatação visual no Telegram (2026-04-26):** Respostas devem ser bonitas, bem espaçadas e organizadas, com **negrito** em títulos, nomes, pontos importantes, números/status/decisões e bullets quando ajudarem. Não exagerar no negrito; objetivo é clareza visual e leitura agradável.
- **Comunicação:** Bullet points + estrutura + profundidade. Nunca genérico, nunca raso.
- **Blocos de foco 7h–10h:** Sagrados. Não interromper com coisas não urgentes.
- **Horários sempre em Brasília (2026-04-01):** TODOS os horários mencionados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de mostrar. Vale pra crons, heartbeats, logs, timestamps, relatórios, qualquer comunicação.
- **Arquivos = sendDocument, nunca fatiar (2026-04-01):** Quando Pedro pedir arquivo/relatório/briefing/export, enviar como documento via Telegram Bot API (sendDocument). NUNCA fatiar em mensagens de texto. Vale pra .md, .pdf, .csv, .xlsx, .json, .png — qualquer tipo.
- **Restauração de contexto pós-troca de modelo (2026-04-07):** Depois de trocar modelo principal, fallback chain ou bootstrap, SEMPRE executar reindexação forçada da memória, warm-up do contexto e teste curto de recall antes de confiar em tarefa crítica. Memória existente sem warm-up pode parecer “presente” mas responder pior.

## Email
- **gb.ai.agent@gbimportadora.com (Tobias):** Livre para usar em comunicação operacional sem pedir permissão.
- **pehpbroglio@gmail.com (Pedro):** SEMPRE pedir permissão antes de enviar, responder ou qualquer ação. Leitura livre, ação NUNCA.
- **Assinatura:** SEMPRE usar assinatura HTML "GB IMP PORTUGUES" ao enviar emails do Pedro. Arquivo: /root/.openclaw/.gmail-signature-pedro.html. Enviar com --body-html incluindo a assinatura no final.

## Modelos de LLM
- **2026-04-25 — Diretriz nova do Pedro:** migrar Kobe, Trader, Spark, Builder, Fisco, RH e todos os crons para usar **exclusivamente GPT-5.5 da OpenAI via assinatura ChatGPT Pro**, aposentando Anthropic como provider default.
- **Execução condicionada:** a migração deve seguir fluxo com backup prévio, autenticação via Codex CLI, validação completa, e **rollback imediato se qualquer step falhar**. Não improvisar workaround parcial.
- **OpenAI Embeddings e Whisper:** permanecem como estão.
- **Status desta decisão:** aprovada por Pedro em 2026-04-25, pendente de execução operacional completa.

## SKUs — Padronização (Março 2026)
- 18 kits de potes com SKUs padronizados
- Nomenclatura: KIT{qtd}YW{tamanho} (unitários) ou KIT{qtd}S{código} (compostos)
- Mapeamento antigo→novo documentado em openclaw/agents/kobe/memory/sessions/2026-03-21.md
- Amazon: SKU é imutável — NÃO tentar renomear (perde histórico/ranking)
- Upseller: SKU do armazém é imutável — usar Apelido ou Regras de Mapeamento

## Margem — Cálculo Correto
- Margem SEMPRE vem da planilha de precificação (Google Sheets), NÃO calculada por script
- Cada aba (SHOPEE, MELI, AMAZON) já considera TODOS os custos individuais
- Margem consolidada = média ponderada por VOLUME de venda em cada plataforma
- Se não tem dado de volume, usar plataforma indicada no relatório como 100%

## Marketplaces — Regras operacionais de cadastro e precificação (2026-04-07)
- **Mercado Livre:** Para anúncios Budamix de ticket próximo de R$39,90, usar `gold_special` (Clássico, 11%) em vez de `gold_pro` (Premium, 16%) quando não houver justificativa comercial forte para subir de modalidade. No PCM001 isso preserva cerca de R$2 por venda.
- **Shopee:** Evitar precificação em R$80,00 nos produtos Budamix sujeitos à taxa fixa. Nesse degrau a taxa sobe de R$4 para R$16. Para o kit duplo de porta-copos planejado, trabalhar em R$69,90 ou no máximo R$79,90.
- **Amazon BR:** O product type `DRINK_COASTER` com GTIN exemption e fulfillment FBA já foi validado para produto Budamix (PCM001). Esse caminho pode ser reutilizado em lançamentos similares.

## Estoque — Fonte de Dados
- Fonte única de estoque do armazém: Planilha de Estoque no Google Drive (aba ESTOQUE)
- Sheets ID: 1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI
- Conta: gb.ai.agent@gbimportadora.com
- Planilha NÃO inclui estoque nos fulfillments (Amazon FBA, ML Full, Shopee)
- Skill de gestão: skills/operations/inventory-management/SKILL.md
- Sempre consultar a planilha atualizada antes de responder sobre estoque
- NUNCA usar cache ou dados de memória — sempre a planilha em tempo real

## Comunicação entre Canais (2026-03-26)
- **Regra:** Responder SEMPRE no mesmo canal que recebeu a mensagem. Nunca cruzar canais.
- Telegram → responde no Telegram (tópico correto do Hub)
- WhatsApp (número do Kobe) → responde pelo WhatsApp
- NUNCA responder no Telegram algo perguntado pelo WhatsApp e vice-versa
- Tarefa iniciada pelo WhatsApp → todas atualizações pelo WhatsApp até Pedro mudar de canal
- Tarefa iniciada pelo Telegram → todas atualizações pelo Telegram
- **Exceções:**
  - Alertas críticos do sistema (crons falhando, segurança) → sempre Telegram (tópico Operacional)
  - Briefings matinais e relatórios agendados → sempre Telegram (como já é)
- **Canal principal:** Telegram (Kobe Hub)
- **Canal adicional:** WhatsApp (número do Kobe +55 19 99845-8149)

## Telegram — Debounce de Mensagens
- Timer padrão: 8 segundos de silêncio antes de processar
- Mensagens acumuladas chegam como itens separados (uma por linha), nunca concatenadas
- Override: mensagem terminando em ! processa imediatamente
- Reação ⏳ indica que está aguardando mais mensagens
- Reação 🧠 indica que começou a processar
- Config: `routing.queue.mode: "collect"`, `debounceMs: 8000`, `cap: 20`

## Relatórios — Design System (Março 2026)
- Output de relatórios é HTML (não mais PDF via wkhtmltopdf)
- Design system está em skills/design/report-design-system/SKILL.md
- Template base está em templates/report-base.html
- Antes de gerar qualquer relatório, ler a skill de design system
- CSS nunca fica inline no Python — sempre no template
- Paleta: dark theme (purple/cyan/green sobre fundo #0a0b10)
- Fontes: Inter (texto) + JetBrains Mono (código)
- Se Pedro precisar de PDF, ele converte pelo browser

## Skills
- **Padrão de qualidade:** Toda skill criada pelo Tobias deve seguir altos padrões de qualidade — estrutura profissional, documentação clara, scripts robustos, referências organizadas. Buscar níveis cada vez mais elevados de competência.
- **Estrutura obrigatória:** Toda skill DEVE seguir o padrão `skills/[categoria]/[nome-da-skill]/SKILL.md` contendo:
  1. **Descrição** — o que a skill faz
  2. **Quando usar** — triggers e contextos de uso
  3. **Inputs necessários** — parâmetros, dados, credenciais
  4. **Passo a passo de execução** — fluxo completo com comandos
  5. **Critérios de qualidade** — o que define um resultado bem feito
- **Categorias existentes:** marketplace, financeiro, comunicacao, integracao, analise (expandir conforme necessário)

## Melhoria Contínua (INVIOLÁVEL)
- **Princípio:** Tobias aprende, evolui e melhora a cada dia. Nunca estático. Segundo cérebro operacional.
- **Ciclo obrigatório:** CAPTURA → PROCESSAMENTO → INCORPORAÇÃO → REGISTRO
- **Ao final de cada sessão significativa:**
  1. Identificar: padrões, erros, preferências, otimizações, edge cases, feedbacks
  2. Classificar: atualizar skill / criar seção / criar skill / atualizar memória
  3. Incorporar: alterar SKILL.md com blocos `<!-- MELHORIA [DATA] -->` rastreáveis, no local correto
  4. Registrar: atualizar CHANGELOG.md com o que mudou e por quê

### Feedback Loops
- 4 domínios: `openclaw/agents/kobe/memory/feedback/content.json`, `tasks.json`, `recommendations.json`, `digest.json`
- Máximo 30 entradas por arquivo (FIFO — mais antigo sai quando chega a 30)
- **Registrar imediatamente** quando Pedro corrigir, rejeitar ou redirecionar
- **Consultar antes** de fazer sugestões em qualquer domínio
- Mensalmente: consolidar padrões recorrentes como lições em lessons.md, limpar entradas originais

### Gatilhos automáticos (sem Pedro pedir):
- Erro cometido e corrigido pelo Pedro → incorporar IMEDIATAMENTE
- Pedro pede pra refazer diferente → capturar preferência
- Descoberta de forma melhor durante execução → aplicar e documentar
- API retorna erro inesperado e solução encontrada → registrar

### Gatilhos por comando:
- "revise suas skills" → auditoria completa, gaps e melhorias pendentes
- "o que você aprendeu hoje?" → resumo de aprendizados e melhorias
- "evolua" → ciclo completo CAPTURA → PROCESSAMENTO → INCORPORAÇÃO → REGISTRO
- "changelog" → histórico de evoluções recentes

### Regras inegociáveis:
1. **Nunca perder aprendizado** — se aconteceu, registra. Não existe pequeno demais.
2. **Nunca degradar skill** — melhorias são aditivas. Conflito → documentar ambos e consultar Pedro.
3. **Sempre proativo** — percebeu melhoria → faz e informa brevemente.
4. **Priorizar por impacto** — tarefas frequentes e erros recorrentes primeiro.
5. **Manter clareza** — cada melhoria compreensível por si só.
6. **Respeitar estrutura** — inserir no local correto, não jogar no final.

### Gate de Encerramento (BLOQUEIO OBRIGATÓRIO)
Antes de QUALQUER "boa noite" ou encerramento de sessão significativa, CONFIRMAR CADA item:
- [ ] Lições da sessão extraídas → lessons.md
- [ ] Decisões da sessão extraídas → decisions.md
- [ ] Pendências atualizadas → pending.md
- [ ] Feedbacks da sessão registrados (se houve correções)
- [ ] Session do dia consolidada → sessions/YYYY-MM-DD.md
- [ ] Blocos <!-- MELHORIA --> atualizados (se houve melhorias em skills)
- [ ] CHANGELOG atualizado
- [ ] Commit + push

**Se qualquer item desmarcado → NÃO encerrar. Avisar Pedro: "Não posso encerrar — falta X".**
Se Pedro autorizar pular → registrar em lessons.md que o gate foi pulado e o motivo.

### Meta:
- 30 dias: incomparavelmente mais competente
- 90 dias: skills = manual operacional que levaria meses pra um humano criar
- Objetivo: impossível substituir sem perder o conhecimento acumulado

## Workspace / Tobias
- **Nome do agente:** Tobias. Escolhido em 2026-03-14.
- **Backup:** GitHub (PHPB2025K/tobias-workspace). Cron diário às 03h UTC.

## Bidspark — Validação antes de test users
- **Decisão:** Pedro quer acumular semanas de dados de otimização real (Amazon Ads) antes de abrir para test users. Comprovar redução de ACOS e melhoria de ROAS com case próprio primeiro.
- **Bloqueio atual:** Zero testes unitários — precisa de suite mínima antes de produção.
- **Status:** ~90% pronto tecnicamente. Bloqueio = validação de resultados, não código.

## 2026-03-18: Direcionamento de crons por tópico Telegram
- Crons relacionados a ML → tópico **🛒 Marketplaces (thread 3)**
- Crons operacionais genéricos → ⚙️ Operacional
- Não misturar domínios nos tópicos

## 2026-03-18: Estratégia de operação — Alto giro, poucos SKUs
- **Prioridade:** Alto volume de vendas em poucos produtos (~50 SKUs)
- **Margem:** Saudável, mas NÃO é prioridade maximizar margem
- **Lógica:** Poucos produtos × alto giro > muitos produtos × baixo giro
- **Impacto em análises:** Recomendações devem priorizar posicionamento que maximize volume/giro, não necessariamente margem unitária
- **Impacto em pricing:** Preço competitivo pra garantir giro > preço premium pra maximizar margem por unidade
- **Impacto em anúncios:** Posicionamento que garanta visibilidade e velocidade de venda

## ⛔ WhatsApp — REGRA INVIOLÁVEL (Incidente 2026-03-25)

**NUNCA MAIS dmPolicy "open" no OpenClaw/Baileys.** O módulo web-auto-reply responde automaticamente quando dmPolicy é "open". Isso causou resposta não autorizada ao Alexandre Novaes. É uma bomba.

**Arquitetura definitiva (INVIOLÁVEL):**
- **OpenClaw/Baileys** = APENAS leitura passiva. dmPolicy=allowlist, groupPolicy=allowlist (só número do Pedro). NUNCA abrir.
- **Enviar mensagem** → EXCLUSIVAMENTE via Evolution API Cloudfy, com aprovação explícita do Pedro
- **Ler histórico** → EXCLUSIVAMENTE via Evolution API Cloudfy (PostgreSQL)
- **NUNCA usar OpenClaw pra enviar ou ler WhatsApp**

**Evolution API Cloudfy (canal único de envio + leitura):**
- URL: `https://trottingtuna-evolution.cloudfy.live`
- Instância: `WHATSAPP PESSOAL PEDRO`
- API Key: vault 1Password (item "Evolution API Cloudfy")
- Endpoints: `POST /message/sendText/{instance}`, `POST /message/sendMedia/{instance}`, `POST /chat/findMessages/{instance}`, `GET /group/fetchAllGroups/{instance}`
- Flags: DATABASE_SAVE_DATA_NEW_MESSAGE, OLD_MESSAGE, HISTORIC, MESSAGE_UPDATE = todas true
- syncFullHistory: ativado
- Status: conectado, 41k+ mensagens, 900 chats

## WhatsApp — Arquitetura Definitiva (2026-03-25, pós-incidente)

**⛔ INCIDENTE 2026-03-25:** OpenClaw respondeu automaticamente Alexandre Novaes (+5519997978437) via módulo web-auto-reply quando dmPolicy estava "open". Mensagens não autorizadas enviadas do número pessoal do Pedro.

### Número do Pedro (5519993040768) — LEITURA PASSIVA APENAS
- **OpenClaw/Baileys:** dmPolicy=allowlist, groupPolicy=allowlist (só número do Pedro). NUNCA abrir.
- **Uso:** APENAS receber mensagens inbound passivamente. NUNCA enviar por este canal.
- **Leitura de histórico:** EXCLUSIVAMENTE via Evolution API Cloudfy (PostgreSQL, 41k+ msgs)
- **Envio de mensagens:** EXCLUSIVAMENTE via Evolution API Cloudfy, com aprovação explícita do Pedro

### Número próprio do Kobe (✅ ATIVO — 2026-03-25)
- **Número:** +55 19 99845-8149
- **Instância Evolution:** WHATSAPP PRÓPRIO KOBE
- **Instance ID:** af2e881f-265b-417d-885a-7516f3174ee6
- **Credenciais:** 1Password → "Evolution API Cloudfy - WhatsApp Kobe"
- **Uso:**
  - Enviar mensagem pro Pedro → este canal
  - Enviar para terceiros quando Pedro autorizar → este canal
  - Identidade: Kobe / Assistente do Pedro (NUNCA se passar pelo Pedro neste número)
  - Receber mensagens de qualquer pessoa
- Elimina definitivamente o risco de resposta automática no número pessoal

### Regras de Segurança WhatsApp (INVIOLÁVEIS)

**LEITURA — livre (via Evolution API):**
- Pode ler qualquer mensagem de qualquer grupo ou conversa individual
- Pode processar, resumir, analisar qualquer conteúdo
- Se encontrar dados sensíveis (cartões, senhas, CPFs, dados bancários, contratos confidenciais) → NUNCA armazenar em arquivos de memória, NUNCA incluir em resumos, NUNCA mencionar em logs

**ENVIO — sempre com aprovação (via Evolution API ou futuro número Kobe):**
- NUNCA enviar mensagem sem comando explícito do Pedro
- Quando Pedro pedir pra enviar, confirmar: destinatário, conteúdo exato, e aguardar "envia" antes de disparar
- Única exceção: regra automática específica criada pelo Pedro

**PROIBIÇÕES ABSOLUTAS:**
- NUNCA abrir dmPolicy no OpenClaw/Baileys (módulo web-auto-reply dispara automaticamente)
- NUNCA alterar dmPolicy ou groupPolicy sem autorização explícita do Pedro
- NUNCA usar OpenClaw pra enviar mensagens WhatsApp (só Evolution API ou futuro número Kobe)
- NUNCA enviar mensagem espontaneamente sem comando do Pedro
- NUNCA encaminhar conteúdo de uma conversa para outra
- NUNCA armazenar em memória: números de cartão, senhas, tokens bancários, dados médicos, documentos pessoais (CPF, RG)
- NUNCA compartilhar conteúdo de conversas privadas em nenhum arquivo acessível por terceiros
- Se alguém perguntar algo no WhatsApp e Pedro não estiver disponível → silêncio total


## Budamix E-commerce — Blog (2026-04-26)
- **Arquitetura aprovada:** Blog Budamix segue o fluxo **N8N → Supabase → Site Budamix**.
- **Aprovação humana:** Nenhum post deve ser publicado automaticamente. Pautas/artigos passam por módulo Admin com preview e ação humana antes de publicação.
- **Repo fonte de verdade:** Entregas do Budamix E-commerce precisam estar no repo principal privado `PHPB2025K/budamix-ecommerce`; workspace isolado do Builder não é entrega final.
- **Imagens:** Fluxo futuro pode usar Nano Banana Pro/Gemini (`gemini-3-pro-image-preview`) para imagens editoriais/lifestyle. Não depender de PNG com transparência real; usar fundo sólido/paleta Budamix.

### 2026-04-27 — Admin Blog v2: automação até edição/preview; publicação segue manual
- **Decisão:** O fluxo do Blog Budamix deve deixar de ser manual por etapa, mas respeitando a SPEC v2.0: pauta `nova` → artigo `gerando` → `em_edicao` → `preview` → `publicado`.
- **Regra:** O WF4 gera artigo e imagens em background e finaliza o artigo em `em_edicao`. `ready_to_publish` foi usado na primeira fase, mas ficou obsoleto para o fluxo final.
- **Publicação:** continua manual/humana no Admin e só acontece na aba Preview. O workflow automatiza preparo, não a publicação final.
- **Motivo:** eliminar a operação manual de “gerar artigo” e “gerar imagem” por etapa sem abrir mão da aprovação humana antes de publicar.
- **Pedro aprovou:** Sim ("ótimo, pode seguir com o WF4 - BLOG ORCHESTRATOR") e depois refinou a SPEC v2.0.

## E-commerce Budamix — Decisões Fase 1 (2026-04-01)

- **Gateway de pagamento:** Mercado Pago Checkout Transparente com Bricks. Pix (QR inline) + Cartão (até 3x sem juros) + Boleto. Stripe descartado (público brasileiro, Pix nativo obrigatório).
- **Parcelamento:** Até 3x sem juros absorvido pelo vendedor (custo ~6-8% total). 4x+ com juros pro cliente. Pedro aprovou.
- **CNPJ operador e-commerce:** 45.200.547/0001-79 (Simples Nacional). Recebe via MP, emite NF. Regras fiscais: CSOSN (não CST), CFOP 5.102 (SP) / 6.102 (interestadual). Bling separado dos Bling Matriz/Filial.
- **Visual checkout:** Dark theme + CSS custom com cores Budamix (Deep Teal #004D4D, Graphite #132525, Amber Gold #C7A35A).
- **Pipeline N8N:** 5 workflows separados (Receptor IPN → Processador → Bling Token Manager → NF Tardia → Stock Sync). Nunca tudo num workflow só (timeout MP 22s).
- **Email transacional:** Resend (API REST). Remetente: pedidos@budamix.com.br. DNS: SPF + DKIM + DMARC no Cloudflare. N8N envia (não Bling, não frontend).
- **Autenticação cliente:** Guest checkout (sem cadastro obrigatório). RLS por email + mp_payment_id, não auth.uid().
- **Frete:** Tabela fixa 5 regiões (R$12,90 a R$29,90). CFOP determinado pela UF de entrega. Frete grátis acima de R$___: PENDENTE decisão Pedro.
- **Pre-rendering:** Entra na Fase 1 via vite-ssg (~28 páginas). OG tags funcionais desde o início.
- **Plataforma:** Manter React/Vite no Lovable. NÃO migrar pra Shopify. Evoluir o existente.
- **Briefing:** v1.2 aprovada como base pro Builder. Salvo em reports/budamix-ecommerce-fase1-briefing-v1.2.md.

## Meta Ads API (2026-03-19)
- **App:** KOBE.OPENCLAW (ID: 3582660648568553)
- **Business Manager:** GB Distribuição (ID: 7723008527787239)
- **Conta principal:** act_323534883953033
- **Token:** Long-lived 60 dias — renovar em 15/05
- **Skill:** skills/marketing/meta-ads/

## Team Agents (2026-03-19, atualizado 2026-04-04)
- **Trader** — Agente especializado ML/Shopee/Amazon
- **Spark** — Agente especializado ADS (ML Ads, Amazon Ads, Meta Ads)
- **Builder** — Agente especializado dev/MicroSaaS
- **Fisco** — Agente especializado faturamento/NF-e/conciliação fiscal (registrado openclaw.json 2026-03-31)
- **RH** — Agente especializado RH/ponto/salários/compliance (registrado openclaw.json 2026-03-31)
- Cada um com memória própria em shared/
- Infra documentada em shared/TEAM.md
- **Todos 6 agentes registrados no openclaw.json** (main, trader, spark, builder, fisco, rh)
- **Desde 04/04/2026, todo o time roda em Opus 4.6** por decisão explícita do Pedro (Kobe, Trader, Spark, Builder, Fisco, RH)

## Agentes RH e Fisco — Registro Independente (2026-03-31)
- **Pedro decidiu** que RH e Fisco devem rodar como agentes independentes no OpenClaw, não como subagentes do main
- **Modelo:** Opus 4.6 para ambos (dados sensíveis de funcionários e decisões fiscais)
- **RH:** workspace=/root/.openclaw/workspaces/rh, agentDir=/root/.openclaw/agents/rh/agent
- **Fisco:** workspace=/root/.openclaw/workspaces/fisco, agentDir=/root/.openclaw/agents/fisco/agent
- **Crons migrados:** 5 crons RH (Monitor Ponto Entrada/Saída, Compliance, Boas-Vindas, QR Code) → agente `rh`; Bling Token Refresh → agente `fisco`
- **Princípio:** Agentes especializados operam por conta própria, não como funções executadas pelo Kobe

## Proatividade do Kobe (2026-03-19)
- **Decisão:** Kobe opera proativamente com 3 níveis: checagem (3x/dia), organização noturna silenciosa (1x/dia), briefing matinal (1x/dia)
- **Horários de silêncio:** 22h-06:45 (madrugada), Sáb 13h-Dom 23:59 (descanso), 07h-10h seg-sex (foco)
- **Regra de ouro:** urgente = avisa, importante = anota pro briefing, nada = HEARTBEAT_OK, organização = faz sozinho sem avisar
- **Modelo:** Haiku pra tudo automático (~$1.50/mês total)
- **Nome:** Renomeado de Tobias para Kobe em 2026-03-19

## SKUs — Padronização nos Marketplaces (2026-03-21)
- **Shopee:** SKUs atualizados via API (budamix-store2 + budamix-shop). budamix-store pendente (token expirado)
- **Mercado Livre:** 14 anúncios com seller_custom_field atribuído (antes vazio). 5 kits não encontrados ativos.
- **Amazon:** NÃO mexer — SKU é imutável. Renomear = deletar listing + perder histórico/ranking.
- **Upseller:** SKU do armazém é imutável — usar campo "Apelido do SKU" nos Produtos do Armazém

## Margem — Cálculo Correto (2026-03-21, complementa decisão anterior)
- Margem consolidada real da GB: **13,7%** (abaixo do mínimo 15%)
- CK4742_B (Jarra Medidora, 33% faturamento): 9% Shopee vs 31% ML
- IMB501P_T: 5% Shopee — quase empate
- Grosso do volume na Shopee onde margens são menores
- **Ação pendente:** Estratégia de redirecionamento de volume ou reajuste de pricing Shopee

## HTML Relatórios — Versões Iterativas (2026-03-21)
- v2.1: Tabelas compactas, font 0.76rem, container 1280px
- v2.2: Margens ponderadas reais da planilha de precificação
- v2.3: "Classe" → "Curva" + tabela B corrigida
- Pedro aprova iterativamente — não precisa entregar versão perfeita de primeira

## Formato de Entrega de Relatórios (2026-03-20)
- **HTML** = versão de leitura/apresentação (principal)
- **Excel** = source of truth / dados brutos (complementar)
- Sempre enviar ambos juntos

## Separação Financeiro vs Performance (2026-03-20)
- **Financeiro** = dinheiro (receita, custos, margens, fluxo de caixa) → skill consolidado-financeiro
- **Performance** = operação (vendas, conversão, ranking, ads, reputação) → skill marketplace-report
- Complementares, sem sobreposição
- Financeiro: data de liquidação. Performance: data de venda.

## Curva ABC no Consolidado (2026-03-20)
- Remover Top 10 Shopee individual, substituir por Curva ABC consolidada (3 plataformas)
- Posicionar após detalhamento das 3 plataformas, antes de Insights

## Largura HTML Relatórios (2026-03-20)
- Aumentar de 860px → 1120px para tabelas caberem

## Strategic Planner Skill (2026-03-20)
- **Arquitetura:** Skill interna (não agente separado) — contexto real-time > overhead de coordenação
- **3 níveis:** Lite (tarefas simples), Standard (multi-fase), Deep (projetos complexos)
- **Gate de aprovação:** Apenas no Deep. Lite e Standard executam direto.
- **Hard Rules invioláveis:**
  1. Modelo obrigatório: claude-opus-4-6 (sem fallback)
  2. Extended thinking sempre ativo
  3. Nunca steps vagos — cada step tem O QUÊ, ONDE, COMO, ENTREGÁVEL
  4. Default pt-BR
  5. Profundidade > velocidade sempre
- **Integração memória:** Consultar decisions, lessons, feedback ANTES de planejar. Salvar plano aprovado em openclaw/agents/kobe/memory/projects/.
- **Trigger implícito:** Apenas ativa Lite. Standard/Deep requerem trigger explícito ou escalação justificada.

### 2026-03-24 — Consolidação de memória SEMPRE em Opus 4.6
- **Decisão:** Os crons "Consolidação Diária" e "Consolidação Profunda" SEMPRE rodam em Opus 4.6. NUNCA rebaixar o modelo. Se precisar economizar rate limits, economizar nos heartbeats e job-monitor — nunca na consolidação.
- **Contexto:** Sem memória robusta, todo o trabalho do dia se perde. É o cron mais crítico do sistema.
- **Pedro aprovou:** Sim, explicitamente.
- **Regra INVIOLÁVEL.**

### 2026-03-24 — Refatoração do sistema de consolidação: 5 crons → 2
- **Decisão:** Substituir 5 crons fragmentados (Ciclo de Melhoria, Session Guard, Multi-agent Distill, Spark Consolidação, Consolidação Quinzenal) por 2 crons robustos (Consolidação Diária 23:30 SP + Consolidação Profunda 1º/15º 04:00 SP).
- **Motivo:** Redundância, fragilidade (Haiku fraco), prompts genéricos, falta de correlação cross-agent.
- **Pedro aprovou:** Sim, definiu os prompts detalhados.

### 2026-03-24 — Builder promovido a Opus 4.6
- **Decisão:** Builder roda em Opus 4.6 (não mais Sonnet). Qualidade de output em frontends complexos justifica o custo.
- **Contexto:** Spark Ads v1 (Sonnet) = amador. v2 (Opus 4.6) = profissional. Diferença gritante.
- **Pedro aprovou:** Sim.

### 2026-03-24 — Briefings de frontend DEVEM referenciar design system
- **Decisão:** Todo briefing de frontend para o Builder DEVE incluir: templates/BRIEFING-TEMPLATE.md + 4 skills de design. Sem design system explícito, output fica genérico.
- **Pedro aprovou:** Sim.

### 2026-03-24 — Budamix Central prioritário sobre Spark Ads Fase 1
- **Decisão:** Budamix Central (dashboard operacional unificado) é prioridade antes do Spark Ads Fase 1.
- **Pedro aprovou:** Sim.

### 2026-03-24 — Rate limits para automated budget management
- **Decisão:** Métricas a cada 1h, ajuste de budget a cada 6h, máximo 3 retries. Rate limits conservadores.
- **Contexto:** Spark Ads automated budget feature — Pedro não quer ações agressivas automáticas.
- **Pedro aprovou:** Sim.

### 2026-03-25 — Hierarquia de memória em 3 camadas
- **Decisão:** Implementar captura de memória em 3 níveis: (1) Session Extractor a cada 30min — captura granular imediata; (2) Consolidação Diária 23:30 — consolida + limpa pending + commit; (3) Consolidação Profunda quinzenal — segunda passagem + expiração.
- **Contexto:** Pedro identificou gap de 14h entre sessão da manhã e consolidação noturna, onde contexto podia se perder por compactação.
- **Pedro aprovou:** Sim (definiu a arquitetura).

### 2026-03-25 — Limpeza obrigatória de pending.md na consolidação
- **Decisão:** Consolidação Diária DEVE limpar pending.md antes de adicionar novos itens. Itens resolvidos são REMOVIDOS (não apenas marcados [x]). Itens >14 dias sem movimentação vão para "Backlog Estagnado".
- **Contexto:** Pending acumulava itens resolvidos que nunca eram limpos. Passo 1.5 existia mas não funcionava na prática.
- **Pedro aprovou:** Sim.

### 2026-03-25 — Shopee sync migrado para VPS (não mais Edge Functions)
- **Decisão:** Sync da Shopee roda no VPS (IP fixo 187.77.237.231), não nas Edge Functions do Supabase. Grava no Supabase via REST API com service_role key.
- **Motivo:** Edge Functions usam IPs variáveis da AWS. Shopee exige IP whitelist. Adicionar IP por IP é inviável.
- **Pedro aprovou:** Sim ("vai com a opção 2 direto").

### 2026-03-25 — Syncs de orders: backfill 6 meses + cron incremental a cada 30min
- **Decisão:** (1) Backfill único de 180 dias (desde out/2025) para ML, Shopee (3 lojas) e Amazon. (2) Cron incremental a cada 30min (minutos 5 e 35) com janela de 1 dia, upsert no Supabase.
- **Detalhes:** Shopee = script VPS com token refresh automático. Amazon = script VPS (mesmo padrão). ML = script VPS com auto-refresh de token via 1Password. Script unificado `sync-orders-cron.sh`.
- **Logs:** `/var/log/budamix-sync/` com rotação 7 dias.
- **Pedro aprovou:** Sim ("Configura os crons enquanto roda").

### 2026-03-25 — Amazon sync migrado para VPS (não mais Edge Function)
- **Decisão:** Amazon orders sync roda no VPS via script Python (mesmo padrão do Shopee), não mais via Edge Function do Supabase que dava timeout.
- **Contexto:** Edge Function dava timeout por rate limit da SP-API + volume alto. Script VPS pode rodar em background sem timeout.
- **Pedro aprovou:** Sim (implícito — faz parte da definição dos syncs).

### 2026-03-25 — Budamix Central Live Sales: módulo prioridade com 8 skills de design
- **Decisão:** Novo módulo Live Sales do Budamix Central — dashboard de vendas em tempo real para TV no escritório + mobile.
- **Rotas:** `/live` (principal) e `/live/ranking` (ranking de anúncios). Rota pública, sem login.
- **Skills obrigatórias (8):** lovable-quality, animated-financial-display, lb-motion-skill, financial-design-systems, data-visualization-2, superdesign, frontend-design-ultimate, shadcn-ui.
- **Specs:** Fundo escuro, números gigantes, count-up com spring physics, auto-refresh 30s, breakdown por canal com cores de marca, meta diária configurável, comparativo semanal, ranking com scroll automático na TV.
- **Timeout Builder:** 120min. Briefing revisado e aprovado por Pedro antes do dispatch.
- **Pedro aprovou:** Sim ("Briefing revisado e aprovado. Dispara pro Builder.").

### 2026-03-25 — Session Extractor em Opus 4.6
- **Decisão:** Session Extractor roda em Opus 4.6 (mesmo da consolidação). Memória não economiza modelo.
- **Contexto:** Pedro explicitou: "é memória, não economiza".
- **Pedro aprovou:** Sim.

### 2026-03-26 — Cron sync-costs diário 06:00 SP
- **Decisão:** Sync de custos da planilha Google Sheets para Supabase roda 1x/dia às 06:00 SP (antes do briefing matinal).
- **Script:** `scripts/sync-costs.py` — puxa 4 abas (ESTOQUE > MELI > SHOPEE > AMAZON), aplica custo em todas as plataformas.
- **Pedro aprovou:** Sim ("coloca num cron 1x por dia, 06:00 SP").

### 2026-03-26 — Builder promovido para L2 (Contributor)
- **Decisão:** Builder promovido de L1 (Observer) para L2 (Contributor) na review semanal.
- **Justificativa:** 8 entregas aprovadas pelo Pedro (critério = 5+), 0 rejeições, evolução clara, em produção ativa.
- **Pedro aprovou:** Pendente confirmação (review feita internamente pelo Kobe).

### 2026-03-26 — Builder promovido L2 — CONFIRMADO por Pedro
- **Decisão:** Builder promovido de L1 (Observer) para L2 (Contributor).
- **Pedro aprovou:** Sim ("Concordo com a promoção do Builder pra L2. Merece — entregou consistentemente.")
- **Ação:** Delegar mais tarefas ao Trader e Spark na próxima semana.

### 2026-03-27 — Sistema de contingência para rate limit (Cron Haiku)
- **Decisão:** Cron "Claude Contingency Guard" (ID: 9b973881) roda a cada 5min no Haiku. Detecta 429/503 e mantém Haiku ativo + notifica Pedro.
- **Contexto:** Kobe ficou fora o dia inteiro (551 errors, cooldown cascade). Pedro operou sozinho.
- **Pedro criou:** Sim, implementou diretamente via Claude Code.

### 2026-03-27 — Módulo Preços v2 usa sku_mapping como fonte de verdade cross-channel
- **Decisão:** Tabela `sku_mapping` (68 entradas) é a fonte de verdade para unificar SKUs entre ML, Shopee (3 lojas) e Amazon no módulo de preços.
- **Pedro implementou:** Sim, via Claude Code.

### 2026-03-27 — Amazon pending = venda real no Live Sales
- **Decisão:** Pedidos Amazon FBA com status "pending" e total_amount > 0 contam no faturamento e ranking do Live Sales. Na Amazon FBA, pending = cliente já pagou, só aguarda processamento. ML e Shopee continuam excluindo pending.
- **Pedro pediu:** Sim, com explicação de negócio.

### 2026-03-27 — Classificação Curva ABC é global, não por plataforma
- **Decisão:** A classificação A/B/C é calculada sobre o faturamento TOTAL (todas as plataformas). Quando filtra por plataforma, mostra os SKUs daquela plataforma mantendo a classificação global.
- **Pedro confirmou:** Sim.

### 2026-03-27 — UX padrão: cache agressivo + prefetch + skeleton
- **Decisão:** Todo módulo novo deve ter: (1) cache server-side com TTL 5min na API route, (2) prefetch via TanStack Query no hover do sidebar, (3) skeleton loaders durante carregamento, (4) staleTime de 5min no hook.
- **Contexto:** Preços v2 levava 5s para carregar (18k+ orders paginados). Com cache, 0.009s.
- **Pedro pediu:** Sim ("Pedro prefere UX rápida").

### 2026-03-28 — Agente Fisco é o 4º agente do time
- **Decisão:** Criar agente Fisco para automatizar faturamento interno. 5 módulos: (A) distribuição proporcional de estoque entre CNPJs, (B) NF transferência Matriz→Filial, (C) NFs venda interna Filial→Simples, (D) conciliação fiscal, (E) monitor limites Simples Nacional.
- **Pedro definiu:** Briefing completo com mapa de sistemas, regras fiscais e integrações.

### 2026-03-28 — Fisco consome dados do Trader, não duplica integrações
- **Decisão:** O Fisco puxa dados de faturamento por marketplace via Trader (que já tem ML, Shopee, Amazon conectados). Sem criar integrações duplicadas.
- **Pedro confirmou:** Sim, explicitamente no briefing.

### 2026-03-28 — Bling Plano Mercúrio, API v3 disponível
- **Decisão:** Bling é o ERP da Matriz/Filial (Lucro Presumido). Plano Mercúrio (enterprise), API v3 REST totalmente disponível.
- **Pedro confirmou:** Sim.

### 2026-03-28 — Contador FOUR Contabilidade (Suellen) valida regras fiscais
- **Decisão:** Toda parametrização tributária (CST, CFOP, alíquotas, NCM) passa pela Suellen antes do Fisco executar. O agente NÃO toma decisões fiscais autônomas.
- **Pedro confirmou:** Sim.

### 2026-03-28 — Regras fiscais configuráveis, não hardcoded
- **Decisão:** TTD 409 (2,6% → 1%), margem interna (5%), ICMS SP (18%), CFOP, teto Simples — tudo em config JSON, alterável sem código. Mudanças nesses parâmetros exigem validação do contador.
- **Pedro definiu:** Sim, explicitamente ("esses parâmetros devem ser configuráveis, não hardcoded").

### 2026-03-28 — Fisco Fase 1 em modo draft
- **Decisão:** Na fase inicial, o Fisco gera NFs mas NÃO emite na SEFAZ. Pedro valida manualmente antes de ativar emissão real.
- **Contexto de segurança:** Erro fiscal tem impacto financeiro e legal direto.

### 2026-03-29 — Crons job-monitor e Contingency Guard de 5min → 15min
- **Decisão:** Reduzir frequência dos crons job-monitor e Contingency Guard de 5min para 15min para economizar ~$78/mês em API calls.
- **Contexto:** Análise de custos Anthropic mostrou $120/mês real. 576 chamadas/dia → 192.
- **Pedro aprovou:** Sim (pediu a otimização após ver breakdown de custos).

### 2026-03-29 — SimulImport reativado, sprint ativo
- **Decisão:** SimulImport saiu de "em pausa" para sprint ativo. Auditoria + 4 Builder jobs executados no mesmo dia.
- **Pedro iniciou:** Sim, pediu para retomar no domingo à noite.

### 2026-03-29 — TIPI/TEC oficiais são fonte de verdade para alíquotas NCM
- **Decisão:** Base NCM do SimulImport deve usar alíquotas da TIPI (IPI) e TEC (II) oficiais da Receita Federal, não estimativas genéricas por capítulo da BrasilAPI.
- **Contexto:** Comparação das 7 NCMs-chave mostrou que tanto seed quanto Builder estavam errados. Pedro enviou TIPI (462 páginas) e TEC (10.302 NCMs).
- **Pedro confirmou:** Sim, enviou os documentos oficiais.

### 2026-03-29 — Antidumping MDIC como próxima etapa de alíquotas
- **Decisão:** Após corrigir IPI (TIPI) e II (TEC), incorporar lista de antidumping do MDIC (por produto/país com NCMs afetados).
- **Pedro pediu:** Sim, enviou link da lista do MDIC.

### 2026-03-29 — Framer Motion removido da landing page SimulImport
- **Decisão:** Framer Motion causava opacity:0 em todos os elementos da landing page (animações não disparavam em serve estático). Removido completamente e substituído por CSS puro.
- **Contexto:** Múltiplas tentativas de fix (CSS fallback, vite preview) falharam. Remoção total resolveu.

## Regra de Frequência — Agente RH WhatsApp (2026-03-30)
Decisão do Pedro sobre frequência de mensagens do agente RH para funcionários:
- Mensagem inicial: máximo 1 por dia por funcionário (consolidar múltiplas irregularidades)
- Conversa ativa (funcionário respondeu): sem limite de mensagens
- Sem resposta: lembrete diário às 10h SP (1 msg/dia), por até 5 dias
- Após 5 dias sem resposta: escala pro Pedro via Telegram (tópico RH), para de enviar
- Horário: apenas 08h–18h SP, seg-sex
- Referência: SOUL.md do agente RH + SKILL monitor-ponto

## Modo Supervisão — Agente RH (2026-03-30)
Ativado em 30/03/2026. Toda mensagem enviada a funcionário gera notificação no Telegram (tópico RH, thread 10) com: nome, irregularidade, mensagem exata, horário. Desativa APENAS quando Pedro confirmar explicitamente. Sem prazo fixo — Pedro decide quando está confortável.

## WhatsApp Próprio do Agente RH (2026-03-30)
Número dedicado: 5519992997273 (separado do Kobe). RH responde direto aos funcionários sem intermediação. Kobe continua orquestrador, RH reporta apenas escalamentos. Pendente: pareamento na Evolution API (precisa Global API Key ou painel Cloudfy).

## Escopo Expandido Agente RH (2026-03-30)
4 áreas de atendimento: (1) Banco de horas e registro de ponto, (2) Salários e remuneração, (3) Políticas e regras da empresa, (4) Solicitações e processos de RH. Knowledge File `shared/rh/knowledge/regras-ponto-certo.md` é fonte de verdade para regras de ponto. Documentos adicionais pendentes da contadora FOUR/Suellen.

## Wrapper Anti-Duplicata WhatsApp (2026-03-30)
`scripts/send-whatsapp.py` — obrigatório para TODO envio WhatsApp do sistema. Deduplicação por SHA256(numero+mensagem), janela 5min. Causa: retry de LLM (errors 500 do Anthropic) re-executava curl → mensagem duplicada. NUNCA chamar Evolution API diretamente via curl.

### 2026-03-30 — Fisco NF-e Módulo B validado com draft real
- **Decisão:** Fisco Módulo B (NF transferência Matriz SC → Filial SP) validado com NF #613 como draft correto no Bling. CFOP 6152, R$690,97. Pronto para emissão após Pedro validar.
- **Pedro confirmou:** Pendente validação do draft. Fase 1 = modo draft (não emite na SEFAZ).

### 2026-03-30 — Mission Control (TenacitOS) deployado como painel visual
- **Decisão:** TenacitOS deployado em `mission.gbformulario.com` como dashboard visual do Kobe (crons, agentes, custos, health).
- **Pedro solicitou:** Sim, PRD criado durante sessão.

### 2026-03-30 — Superpowers (14 skills de workflow dev) incorporadas
- **Decisão:** Coleção Superpowers instalada (brainstorming, dispatching-parallel-agents, test-driven-development, etc.) + skill excel-generation.
- **Contexto:** Workflow dev completo para Builder e subagents.

### 2026-03-30 — Builder jobs: máximo 2 simultâneos no VPS
- **Decisão:** VPS tem 3.8GB RAM. 4 processos Claude Code simultâneos causam OOM killer. Máximo 2 por vez.
- **Pedro confirmou:** Sim (observou a falha e ajustou).

### 2026-03-30 — Fisco auto-refresh tokens Bling a cada 5h
- **Decisão:** Cron de auto-refresh de tokens Bling (Matriz + Filial) a cada 5h via Haiku. Script `scripts/bling-token-refresh.sh`. Filial tem bug de refresh (403 "empresa inativa") — token funciona mas refresh não. Re-autorização manual quando expirar até Bling resolver.
- **Pedro aprovou:** Sim (pediu pra avançar na mesma sessão).

### 2026-03-30 — Excel generation skill como padrão obrigatório
- **Decisão:** Toda planilha gerada pelo sistema segue `skills/excel-generation/SKILL.md` (1018 linhas, openpyxl, paleta corporativa, 10 estilos). Pedro rejeitou planilha Google Sheets simples e pediu refeita no padrão profissional.
- **Pedro pediu:** Sim ("Lê essa skill inteira agora, incorpora como referência permanente, e refaz a planilha").

### 2026-03-30 — Planilha de pesos: apenas 22 potes unitários Budamix
- **Decisão:** Planilha de peso/embalagem para NF-e contém APENAS potes unitários da Budamix (22 SKUs: 6 tamanhos × 3 cores + 4 variantes). Kits são calculados automaticamente somando os componentes. Inicialmente eram 52 SKUs, Pedro reduziu para os essenciais.
- **Pedro definiu:** Sim ("apenas os potes oficiais da budamix, apenas os potes unitários, sem incluir kits").

### 2026-03-30 — Mission Control: subdomínio, deploy imediato, manter 3D
- **Decisão:** (1) Subdomínio `mission.gbformulario.com` aprovado. (2) Deploy imediato (noite do dia 30/03). (3) Manter office 3D (fun, +20MB RAM aceitável). Pedro aprovou plano de 4 etapas (Kobe prep → Builder deploy → Kobe polish → amanhã crons).
- **Pedro aprovou:** Sim ("1- subdominio está ok, 2- agora, 3- manter").

### 2026-03-31 — Mapeamento CNPJ × Marketplace (DEFINITIVO)
- **GB Comércio (07.194.128/0001-82):** ML + Amazon + Shopee shop_id 448649947
- **Trades (45.200.547/0001-79):** Shopee shop_id 860803675
- **Broglio (63.922.116/0001-06):** Shopee shop_id 442066454
- **Pedro confirmou:** Sim (31/03/2026)

### 2026-03-31 — NF Bling: NÃO enviar impostos no payload da API
- **Decisão:** O Bling preenche CFOP/ICMS/PIS/COFINS automaticamente a partir da regra fiscal da Natureza de Operação. Enviar no payload apenas: codigo, quantidade, valor, NCM, origem. Enviar campos de imposto → Bling ignora.
- **Causa:** Investigação de 31/03 — 5 abordagens testadas até encontrar a causa raiz.

### 2026-03-31 — NFs Venda Interna Março/2026 emitidas com sucesso
- **6 NFs autorizadas SEFAZ** (3 Filial CFOP 5102 + 3 Matriz CFOP 6102)
- **Total: R$ 29.355,85** (Filial R$23.213,19 + Matriz R$6.142,66)
- **Excedente via Matriz** quando vendas superam estoque transferido (pote 800ml e 1520ml)
- Arquivos salvos em `shared/fisco/openclaw/agents/kobe/memory/nfe-log.md`

### 2026-04-01 — Sessão Budamix Central + Bling (via Claude Code)

- **Bling OAuth restaurado:** Tokens Matriz e Filial re-autorizados. Bug Filial era falta de redirect_uri (NÃO "empresa inativa"). Callback server reescrito com suporte Matriz + Filial via state.
- **Bling refresh-tokens.py melhorado:** Sync automático → Supabase marketplace_tokens. Alerta WhatsApp se falhar 2x. Contador em failures.json.
- **Curva ABC corrigida:** (1) Paginação adicionada (fetchAllOrdersPaginated, PAGE_SIZE=1000). (2) Amazon unit_price corrigido (÷ QuantityOrdered). 634 orders Amazon corrigidos. (3) SKU mapping integrado (sku_child → sku_parent cross-platform).
- **Live Sales sort toggle corrigido:** React key sem índice.
- **Crontab consolidado:** :05/:35 Orders, :15/:45 Inventory, :25/:55 Shopee Prices, 09:00 Costs. Timeout 300s em todos os scripts.
- **Auditoria BRT completa:** 21/21 crons + 6/6 agentes em Brasília.
- **Nenhuma operação de escrita no Supabase sem aprovação do Pedro.**
- **Sempre fazer sanity check em valores monetários antes de aceitar.**
- **Credenciais Bling salvas permanentemente na memória do Claude Code.**

### 2026-04-02 — Cron Request Review Amazon diário 20:30 BRT
- **Decisão:** Automação de Request Review diário. Janela 5-7 dias, inicialmente com exclusão SKU SPC002.
- **Cron ID:** 11201dfa-e6ee-4123-8023-abb0d65a1962
- **Horário:** 20:30 BRT (23:30 UTC), todos os dias
- **Script:** `scripts/amazon-request-reviews.py --min-days 5 --max-days 7`
- **Delivery:** Telegram tópico Marketplaces. Se 0 elegíveis → silêncio.
- **Fallback chain:** Haiku → Sonnet 4.6 → Opus 4.6.
- **Atualização 2026-04-10:** Pedro removeu a exclusão do SKU SPC002 para pedidos futuros que ainda não tiveram solicitação.
- **Pedro aprovou:** Sim.

### 2026-04-01 — Baseline Curva ABC validado
- Receita 30 dias: R$ 377.640
- SKUs ativos: 64
- Top 1: CK4742_B (R$ 75.752, 20,1%)
- Sanity check KIT2PANO800AM_T: R$ 1.939 (avg R$ 15,90/un) ✅

### 2026-04-01 — Plano de preços em tempo real (≤2 min polling)
- **Decisão:** Todas as plataformas terão sync de preço de anúncio a cada 2 min.
- **Amazon:** sync-amazon-prices.py (novo) — Listings Items API (getListingsItem, includedData=offers). 59 SKUs, 15s/ciclo. Aguardando deploy.
- **ML:** sync-ml-prices.py (a criar) — 26 SKUs.
- **Shopee:** Adaptar cron existente de 30 min → 2 min com cache de item IDs.
- **Ordem:** Amazon → ML → Shopee.
- **Pedro aprovou:** Sim.

### 2026-04-01 — sync-inventory-amazon.py NÃO toca em unit_price
- **Decisão:** Removida linha `unit_price: 0` do payload de upsert. Campo unit_price gerenciado exclusivamente por sync-amazon-prices.py.
- **Contexto:** Bug: sync de inventário sobrescrevia preço com 0, invalidando dados de preço.

### 2026-04-02 — Cron Request Review Amazon diário 20:30 BRT
- **Decisão:** Automação de Request Review diário. Janela 5-7 dias, excluir SKU SPC002, Haiku com fallback Sonnet.
- **Cron ID:** 11201dfa-e6ee-4123-8023-abb0d65a1962
- **Horário:** 20:30 BRT (23:30 UTC), todos os dias
- **Script:** scripts/amazon-request-reviews.py com --min-days 5 --max-days 7 --exclude-sku SPC002
- **Delivery:** Telegram tópico Marketplaces. Se 0 elegíveis → silêncio.
- **Pedro aprovou:** Sim.

### 2026-04-02 — Preços em tempo real ≤2min OPERACIONAL (todas as plataformas)
- **Decisão:** Deploy concluído. Amazon, ML e Shopee com sync de preços a cada 2 min via crontab VPS.
- **9 cron jobs ativos** no VPS para syncs (preços, orders, inventory, custos, Mission Control).
- **Pedro aprovou:** Sim (via sessão Claude Code).

### 2026-04-02 — Regras operacionais Budamix Central (6 regras)
- (1) Nenhuma escrita Supabase sem aprovação Pedro — sem exceção
- (2) Sanity check obrigatório em valores monetários
- (3) Backup antes de UPDATE em massa
- (4) Horários sempre BRT
- (5) Credenciais em memória persistente
- (6) sku_mapping reservado para módulo futuro (Estoque/Compras) — NÃO usar em Curva ABC nem Preços v2

### 2026-04-02 — cBenef não requer ação para transferências atuais
- **Decisão:** Transferências Bling (CRT 3, CST 00, ICMS 4%) não precisam de cBenef. Aviso do ML refere-se ao emissor de vendas SN (UpSeller), não ao Bling.
- **Contexto:** Sefaz-SP ativa rejeição em 06/04/2026 (Portaria SRE 70/2025), mas só para operações com desoneração de ICMS.

### 2026-04-04 — Trader e Spark promovidos para Opus 4.6
- **Decisão:** Pedro pediu para mover Trader e Spark para Opus 4.6. Agora TODO o time (Kobe, Trader, Spark, Builder, Fisco, RH) roda em Opus 4.6.
- **Pedro aprovou:** Sim, explicitamente (duas mensagens separadas).

### 2026-04-04 — Catálogo Ana: Supabase é fonte consolidada, NÃO ir no Bling
- **Decisão:** Para extração de catálogo/dados de produtos, usar Supabase (Budamix Central) como fonte única. Os crons de sync já cruzam Bling + marketplaces + planilha e jogam tudo lá. Builder não entra em tarefas de catálogo — se dado faltante no Supabase, é problema de cron, não motivo pra ir no Bling direto.
- **Pedro corrigiu:** Sim ("O Supabase já é a fonte consolidada").

### 2026-04-04 — Catálogo Ana: todos os 71 SKUs entram (não só Budamix)
- **Decisão:** Ana atende sobre TUDO que a GB Importadora vende, não só marca Budamix. Manter todos os SKUs no catálogo.
- **Pedro decidiu:** Sim ("todos entram").

### 2026-04-04 — K6CAN250 descontinuado
- **Decisão:** Kit 6 Canecas Porcelana 250ml (K6CAN250) está descontinuado. No catálogo: "Produto descontinuado. Não disponível para venda. Alternativas: TL6250 ou 914C_B."
- **Pedro decidiu:** Sim.

### 2026-04-04 — 9 SKUs sem preço removidos do CSV catálogo
- **Decisão:** Remover do CSV: 403_B, 0063_, 1201602800019, 213_BB, CK4818V_B, KIT12AL011__, KIT24FIT100M, KIT2PANO800AZ_T, PRA03P. Se tiverem vendas relevantes depois, adicionar de volta com dados completos.
- **Pedro decidiu:** Sim.

### 2026-04-04 — Regras de [VERIFICAR] vs [INFERIDO] para dados técnicos de produto
- **Decisão:** Dados técnicos que dependem de especificação do produto físico (material tampa, compatibilidade micro-ondas/freezer/forno/lava-louças, dimensões exatas, peso, conteúdo embalagem, capacidade exata, temperatura máxima) → [VERIFICAR]. Dados genéricos inferíveis (sugestões de uso, descrição curta, diferenciais, cuidados genéricos da categoria) → [INFERIDO]. Se Ana disser algo errado sobre compatibilidade → reclamação, devolução, risco segurança.
- **Pedro definiu:** Sim (com exemplos por categoria: potes vidro, canecas, suporte gamer, kits jardinagem, porta modem).

### 2026-04-04 — Briefing de delegação para agentes: Pedro valida ANTES de disparar
- **Decisão:** Para tarefas complexas delegadas a agentes (Trader, Builder etc), Kobe gera briefing completo e envia pro Pedro validar ANTES de disparar. "Prefiro validar uma vez do que corrigir depois."
- **Pedro pediu:** Sim, explicitamente. Definiu 7 pontos obrigatórios do briefing (tabelas, mapeamento, queries, regras faltantes, links, formato output, timeout/modelo).

### 2026-04-06 — Default HIGH em todos os agentes e chats
- **Decisão:** O thinking default do OpenClaw passa a ser HIGH em todos os agentes e chats novos.
- **Implementação correta:** Persistir via `defaultThinkingLevel` nos `settings.json` dos agentes e via settings de workspace/chat. Não depender de `openclaw.json` para isso.
- **Ressalva operacional:** Sessões antigas com override próprio de `thinkingLevel` mantêm o valor salvo até reset ou limpeza explícita.
- **Pedro aprovou:** Sim, explicitamente.

### 2026-04-06 — Vibe do Kobe endurecida no SOUL
- **Decisão:** O SOUL do Kobe incorpora uma seção `Vibe` com regras explícitas de brevidade, opinião forte, zero linguagem corporativa, crítica útil sem sugarcoat, humor só quando natural e prosa acima de lista quando couber.
- **Impacto:** Passa a orientar permanentemente a forma de resposta do Kobe.
- **Pedro aprovou:** Sim, explicitamente.

### QA Financeiro — 5 Regras INVIOLÁVEIS (2026-04-03)
- **Contexto:** Consolidado março usou extrato Shopee parcial (01-20/03) como mês completo. Invalidou relatório + DRE.
- **Decisão Pedro:**
  1. Validação de período obrigatória (primeiro pedido >= dia 1, último >= dia 28+; se incompleto → para)
  2. Nunca reutilizar extratos antigos sem validar período
  3. Carimbo obrigatório (data/hora extração, período real, totais por status)
  4. Sanity check antes de entregar (vendas vs histórico, período completo, dados frescos, totais batendo)
  5. Aplica-se a Kobe + Trader, todo extrato/relatório financeiro, permanente
- **Registrado em:** AGENTS.md (Kobe), etapa5-agents.md (Trader), MEMORY.md (Kobe), etapa3-memory.md (Trader)

### 2026-04-27 — Amazon Request Review diário com janela conservadora 7–12 dias
- **Decisão:** Cron diário de Request Review Amazon deve usar janela de pedidos entregues há 7 a 12 dias, não 5 a 7.
- **Motivo:** Auditoria confirmou que os envios via SP-API funcionam, mas muitos pedidos filtrados por `delivered_at` local ainda são rejeitados pela Amazon por timing. A janela 7–12 reduz rejeições e mantém folga dentro do limite Amazon 5–30 dias.
- **Cron:** `Amazon Request Review Diário` atualizado para executar `scripts/amazon-request-reviews.py --min-days 7 --max-days 12`.
- **Regra:** Não voltar para 5–7 sem nova evidência de que o campo de entrega local está perfeitamente alinhado à janela real da Amazon.

## Budamix Blog — DNA Visual aprovado (2026-04-27)
- DNA visual aprovado por Pedro: **casa possível + bom gosto + organização bonita + produtos em uso real**.
- Público: classe B brasileira com bom gosto; nunca luxo, showroom, render, casa de influencer americana ou casa popular improvisada.
- Estética: reforma simples bonita, crível e copiável; ambientes compactos/reais, com pequenas imperfeições controladas.
- Paleta: base neutra brasileira (`off-white`, branco, bege claro, cinza claro, madeira mel/carvalho claro). **Não usar armários verdes como base**; verde fica em plantas ou acentos pequenos.
- Objetos: priorizar objetos de uso que são bonitos (cafeteira real, caneca simpática, pote Budamix em uso, fruta solta, pano de prato natural, geladeira visível, escorredor discreto, planta pequena). Evitar props cenográficos.
- Pessoa na capa: rosto visível, brasileira, bem cuidada, casual arrumada, com bom gosto; sem parecer modelo, elegante/formal demais, nem simples/largada demais.
- Luz: janela brasileira real com persiana/cortina simples e sombras naturais; evitar golden hour perfeita, glow editorial ou stock photo.

### 2026-04-27 — Blog Budamix: pins Pinterest são assets por enquanto
- **Decisão:** Pins Pinterest gerados pelo pipeline ficam como assets reaproveitáveis no Admin Blog, sem postagem automática por enquanto.
- **Futuro:** Ativar Pinterest API/OAuth só depois que o padrão de artigos, imagens e operação do blog estiver validado.
- **Pedro aprovou:** Sim, após perguntar a utilidade dos pins sem integração de postagem.

### 2026-04-27 — Blog Budamix: artigos mais curtos e fluídos
- **Decisão:** Artigos do Blog Budamix devem ser menores, fáceis e prazerosos de ler, sem perder qualidade.
- **Regra editorial:** Padrão 550–750 palavras; máximo normal 900–950 quando necessário. Parágrafos de 2–4 linhas, frases diretas, subtítulos claros, listas curtas e sem encher linguiça para SEO.
- **Pedro aprovou:** Sim, pediu explicitamente leitura mais fluida e menos cansativa.

### 2026-04-27 — Blog Budamix: DNA emocional positivo das imagens
- **Decisão:** Realismo sim, baixo astral não. Pessoas nas imagens, especialmente capas, devem parecer normais, brasileiras, críveis, bem cuidadas, simpáticas e comercialmente agradáveis.
- **Evitar:** expressão triste, cansada, preocupada, melancólica, abatida, largada, sofrida ou visual comercialmente fraco.
- **Desejado:** alegria calma, satisfação, acolhimento, orgulho da casa, alívio positivo e prazer em cozinhar/organizar/receber.
- **Pedro aprovou:** Sim, refinou e aprovou essa direção como regra permanente do DNA visual.

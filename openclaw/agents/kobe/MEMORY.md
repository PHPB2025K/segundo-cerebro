---
title: "MEMORY"
created: 2026-04-14
type: memory-config
agent: kobe
status: active
tags:
  - agent/kobe
---

# MEMORY.md — Índice Central de Memória

_Último update: 2026-05-28 23:45 BRT (consolidação diária em camadas)._

---

## Estrutura

```
memory/
├── context/
│   ├── decisions.md       ← Decisões permanentes (NUNCA contradizer)
│   ├── lessons.md         ← Erros e aprendizados [ESTRATÉGICA|TÁTICA]
│   ├── people.md          ← Contatos importantes
│   ├── business-context.md ← Vocabulário, números de referência
│   └── writing-as-pedro.md ← Tom padrão para WhatsApp/e-mail escritos no nome do Pedro
├── projects/
│   ├── gb-importadora.md  ← Operação principal
│   ├── simulimport.md     ← MicroSaaS — simulador de importação
│   ├── bidspark.md        ← MicroSaaS — automação de ADS (Amazon + ML)
│   ├── canguu.md          ← MicroSaaS — agente IA atendimento
│   ├── atlas-finance.md   ← Sistema financeiro GB (contas a pagar/receber)
│   └── gestao-funcionarios.md ← Acompanhamento semanal de performance via atas do Slack
├── sessions/
│   └── YYYY-MM-DD.md      ← Notas diárias (expira 30 dias após consolidação)
├── integrations/
│   ├── tools-map.md       ← Ferramentas, IDs, acessos
│   ├── telegram-map.md    ← Grupo Kobe Hub — tópicos e thread IDs
│   ├── github-repos.md    ← Mapeamento completo repos GitHub (23 ativos, 7 arquivados)
│   ├── whatsapp-integration.md  ← Status e regras do WhatsApp
│   ├── whatsapp-allowlist.md    ← Contatos/grupos autorizados (READ vs READ+SEND)
│   └── whatsapp-groups-full.md  ← Listagem completa dos 39 grupos
├── feedback/
│   ├── content.json       ← Rejeições de conteúdo/design
│   ├── tasks.json         ← Rejeições de tarefas/execução
│   ├── recommendations.json ← Rejeições de recomendações
│   └── digest.json        ← Rejeições de resumos/digestos
└── pending.md             ← Aguardando input do Pedro
```

## Carregamento por sessão

### Sempre carregado (automático via workspace context)
- `SOUL.md`, `USER.md`, `AGENTS.md`, `IDENTITY.md`
- `MEMORY.md` (este arquivo)

### Carregado no boot
- `memory/sessions/` de hoje + ontem
- `memory/pending.md`

### Sob demanda (memory_search → memory_get)
- `memory/context/*` — decisões, lições, pessoas
- `memory/projects/*` — projetos específicos
- `memory/integrations/*` — dados de ferramentas
- `memory/feedback/*` — consultar ANTES de fazer sugestões

## Integrações Ativas

| Ferramenta | Status | Credenciais |
|---|---|---|
| Telegram | ✅ Bot @TOBIAS_USER_BOT + Grupo Kobe Hub (11 tópicos) | Config OpenClaw |
| Brave Search | ✅ Pesquisa web | Config + 1Password |
| 1Password CLI | ✅ Service Account, vault "OpenClaw" | Systemd override |
| Google (gog) | ✅ Gmail + Calendar + Drive + Sheets (2 contas) | OAuth tokens |
| GitHub (gh) | ✅ CLI autenticado, PHPB2025K (23 ativos, 7 arquivados) | PAT no 1Password |
| OpenAI Whisper | ✅ Transcrição de áudio | API key no systemd |
| Instagram | ✅ Via RapidAPI (instagram120) | RapidAPI key |
| Mercado Livre | ✅ 3 apps (Vendas, Financeiro, Métricas) | Tokens em .ml-tokens*.json |
| Shopee OAuth Multi-Account | ✅ 3 contas gerenciadas automaticamente | Server porta 8901, auto-refresh 3h30 |
| Amazon Ads | ✅ Via Supabase do Bidspark | Refresh token no Supabase |
| Amazon SP-API | ✅ Integração completa. Endpoint NA, marketplace BR (A2Q3Y263D00KWC) | Tudo no 1Password |
| Stripe | ✅ Conectado (modo teste) | sk_test no 1Password + systemd |
| RapidAPI | ✅ Conta gb.ai.agent | Key no 1Password |
| AWS | ✅ IAM User sp-api-tobias + Role SpApiRole | Credentials em ~/.aws/ |
| Google Chrome | ✅ Headless no VPS | Config OpenClaw browser |
| Bright Data | ⚠️ Instável / billing suspende intermitentemente | API key no 1Password |
| Evolution API Cloudfy | ✅ WhatsApp Pedro + WhatsApp Kobe | API Key em 1Password |
| Bling ERP | ✅ Plano Mercúrio (Matriz + Filial) | OAuth tokens refresh automático |
| Supabase | ✅ Projeto Budamix Central + Budamix E-commerce | Service role key via env/credencial N8N |
| Slack | ✅ Read-only workspace GB Importadora | User token no 1Password |
| N8N Cloudfy | ✅ Workflows Blog Budamix; ⚠️ API key nova ainda não localizada no 1Password | Credentials internas no N8N + pendência de item `N8N Cloudfy API Key` |
| Perplexity API | ✅ Radar de pautas Blog Budamix | Credential N8N via 1Password |

## Skills

```
skills/
├── marketplace/
│   ├── marketplace-report/
│   ├── consolidado-financeiro/
│   ├── ml-competitor-analysis/
│   ├── ml-extrato/
│   ├── ml-ads/
│   ├── shopee-extrato/
│   ├── shopee-fees-rules/
│   ├── amazon-extrato/
│   ├── amazon-request-reviews/
│   └── inventory-management/
├── amazon-listing-creator/
├── shopee-listing-creator/
├── integracao/
│   └── instagram/
├── design/
│   ├── lovable-quality/
│   ├── superdesign/
│   ├── frontend-design-ultimate/
│   ├── shadcn-ui/
│   ├── report-design-system/
│   ├── excel-design-system/
│   └── excel-generation/
├── coaching-corrida/
└── financeiro/
    └── stripe-api/
```

## Agentes

| Agente | Especialidade | Workspace | Status |
|---|---|---|---|
| **main (Kobe)** | Orquestração, análise, memória | ~/.openclaw/workspace | ✅ L3 Estratégico |
| **Trader** | Marketplace — ML, Shopee, Amazon | shared/trader | ✅ Operacional |
| **Spark** | ADS — ML, Amazon, Meta | shared/spark | ✅ Operacional |
| **Builder** | Dev — MicroSaaS, APIs, UI | shared/builder | ✅ L2 Contributor |
| **Fisco** | Faturamento — NF-e, tributário | agents/fisco | ✅ Operacional |
| **RH** | Ponto, salários, compliance | agents/rh | ✅ Operacional |
| **Vault** | Finanças, tesouraria, caixa | agents/vault | ✅ Operacional |
| **Scout** | Reposição, demanda, estoque, compras semanais | agents/compras | ✅ Fundação criada + Radar |

## Status do Sistema (28/05/2026 23:45 BRT — consolidação diária em camadas)

### 🚨 Crítico
- **Telegram Alertas:** tópico Alertas confirmado no thread **10204**; todo conteúdo relacionado a alertas deve ir para lá (watchdogs, guards, audits, monitores, failure alerts, resumos e avisos de risco/problema). Thread 8 permanece Urgente e não deve receber alertas técnicos de rotina.
- **Planejamento de reposição das canecas / Compras:** prioridade máxima do próximo bloco operacional. Pedro pediu em 25/05 retomar a criação do Diretor de Compras; fundação do agente **Scout** criada com subagente **Radar**. Pedro aprovou estrutura enxuta Scout → Radar por enquanto e regra do cron semanal: recalcular o pipeline inteiro do zero com dados até D-1, comparar contra o plano aprovado e só atualizar se houver mudança relevante. O piloto de canecas segue como primeiro playbook antes de ampliar para outras famílias; todo assunto de compras vai no tópico Compras.
- **Daily Sales Report Slack / DSA:** envio real para funcionários segue bloqueado até liberação explícita. O DSA ML amadureceu em 23/05 com sistema MercadoLíder, memory ingest diário, consolidações semanal/mensal e decisão de modelo por camada. Em 25/05, L06 foi lapidada para linguagem natural no Slack da Yasmin. Pacotes 23/05 e 24/05 seguem com DADOS_PARCIAIS; o pacote de 25/05 veio com **DADOS_OK** nas três plataformas, mas a entrega temporária localizada ficou só Mercado Livre/Yasmin. Em 27/05, o Daily Sales de 26/05 reportou R$ 12.864,40 em 253 pedidos, com data readiness parcial por Shopee Conta 2 fraca e 6 cancelamentos na Amazon. Em 28/05, o Daily Sales de 27/05 reportou R$ 12.622,97 em 238 pedidos nos marketplaces; Shopee recebeu ações Ramp Up para potes nas três contas e precisa leitura D+1/D+3/D+7. Validar se o ciclo ML-only recorrente é desenho ou lacuna antes de qualquer promoção; envio real para Yasmin/Lucas/Leonardo continua bloqueado.
- **Estoque GB / Budamix:** em 28/05, Pedro aprovou o modelo de livro/motor de movimentações auditáveis antes de escrever saldo na planilha. Grupos WhatsApp Estoque e Devoluções e tópicos Telegram correspondentes foram criados. Fase 1 foi implementada como camada segura sem escrita automática nova; Fase 2 avançou com resolver canônico de SKU, aliases, BOM de kits homogêneos e smoke test 5/5. Próximos bloqueios: validar migrações/tabelas reais, corrigir fonte oficial de ENVIOS FULL, receber IDs dos envios criados em 28/05, limpar movimentos vindos de planilha errada e decidir fluxo permanente. Pendências antigas ainda existem: POT1BB duplicado, aliases manuais, PR4 kits/BOM, cleanup opcional das ops de teste e webhook n8n antigo.
- **DRE Abril:** U15 Descontos Concedidos continua prioridade antes da U44 v4 limpa. ML aceito em R$ 5.061,14; Amazon precisa fechar item-promotion sem frete promocional; Shopee segue suspeita/reclassificação.
- **Mission Control:** 11/23 módulos fechados; módulos Activity, Cron, Sessions, Skills e Costs consolidados, com separação de custo real API vs equivalente API vs subscription. Próxima prioridade técnica segue n8n usage tracking em `/costs`, painel Daily Sales Pipeline pendente de restart/smoke e PRDs dos módulos restantes.
- **Social Studio Reborn:** Fase A/PR #3 e Fase B/PR #4 mergeadas; Fase C em andamento. C1 fechado; próximo C2 `/admin/social/conta`; antes do C3 Pedro precisa criar/configurar App Meta e secrets.
- **Fechamento março continua aberto:** ads spend real, consolidado novo e DRE semanal seguem pendentes.

### ⚠️ Importante
- **Meta Ads:** token atingiu a data estimada de expiração em 18/05/2026; Spark ficou quieto em 23/05. Antes de depender da API, validar renovação/funcionamento e escalar correção se falhar.
- **Canggu/Ana:** silêncio de 9 dias e falha de dispatch foram fechados em 21/05 com validação E2E real: WhatsApp → webhook → process-message → dispatcher voltou a gerar mensagem LLM com tokens; parser de origem `Shoppe` → `shopee` também validado. Regra 17 “resposta cética mas gentil” segue aplicada no ML. Pendentes: hard-block adicional contra linguagem de cadastro/processo interno, correção manual ML antiga, redirect www↔apex e resiliência restante.
- **RH/Ponto Certo:** `ponto.budamix.com.br` ativo com SSL; WhatsApp RH proativo bloqueado indefinidamente até liberação explícita, inbound permitido.
- **Budamix Central Estoque:** Fase 1.5 visual precisa validação do Pedro antes da Fase 2.
- **Amazon Ads:** tópico oficial passou a ser Amazon ADS. Nova régua aprovada: grupo alvo <10% e limite 15%, com tolerância refinada por função de campanha. Rodada de 24/05 executou ajustes em Tulipa, Suporte Controle Gamer, Potes Herméticos Vidro, Canecas Canelada, MDFs, Jarra Medidora e Jogo Canequinhas Café; D+7 obrigatório para medir efeito.
- **Shopee Full+:** Trader registrou em 26/05 que Full+ deve ser tratado como contexto de margem/mix logístico e rebate, não como causa automática de conversão diária. Conta 3 está abaixo do corte mínimo de 40% de pedidos Full no MTD; calcular impacto financeiro por conta para junho antes de recomendar ação.
- **Bling/Fisco:** Filial segue com HTTP 403/empresa-token inativo no refresh OAuth pelo 14º dia em 28/05; Pedro decidiu pausar essa frente em 21/05 porque não está usando esse Bling. Matriz OK nas execuções completas e Filial 403; não gastar bloco operacional agora e não avançar fluxos fiscais que dependam da Filial até reabrirem a frente. Atenção: cron refresh segue com risco separado de rodadas sem validação útil por política/allowlist, e alertas WhatsApp do refresh seguem falhando com HTTP 403. WhatsApp Health Check continua sendo o próximo foco de infra.
- **RH/Ponto Certo:** follow-up tem pré-checagem determinística de cobertura por ajuste, justificativa ou batida real. Em 28/05, QR Code diário foi rotacionado e validado; compliance registrou Sandra sem marcações em dia útil, Mateus sem saída final, Guilherme e Lucas com intervalo abaixo de 1h; backlog RH segue em 16 comunicações abertas, com 9 casos exigindo aprovação/orientação do Pedro. WhatsApp proativo segue bloqueado fora do escopo autorizado; Pedro precisa orientar casos antes de nova cobrança.
- **Blog Budamix Pipeline v2:** em produção; resta inspeção visual humana do post de teste e cleanup.

### ✅ Operacional
- **Vault / segundo-cérebro:** regra operacional nova: toda escrita no vault deve passar pelo `safe-write.sh commit`; `git commit` direto só em diagnóstico controlado autorizado. Bug raiz de commits stuck foi corrigido no script com catch-up automático de commits locais já feitos.
- **Planilha de Precificação/Estoque:** regra global de formato definida por Pedro em 27/05: qualquer valor inserido/atualizado deve usar padrão brasileiro de moeda/número (`R$ 00,00`, vírgula decimal). Rodada de pricing de canecas aplicou desconto de 10%, atualizou custos nas abas SHOPEE/AMAZON/MELI, taxas reais de devolução nas três plataformas e novas linhas Amazon.
- **Daily Sales Report v2:** pipeline individual por funcionário em produção: análise profunda por conta, memória Trader diária/semanal/mensal, Slack DM 06:50 BRT, Granola/Himmel 20:37 BRT e Marketplace Rules Watch 06:23 BRT.
- **Vault como SSoT** segue válido: OpenClaw aponta para `/root/segundo-cerebro`, sync Mac↔GitHub↔VPS funcionando.
- **Social Studio Carrossel/PR2/Pivot 1** viraram referência histórica; o produto ativo agora é Reborn (publicador + métricas, sem IA).
- **Canggu** tem 13/13 Edge Functions com auto-deploy validado; `process-message` v39 e `webhook-whatsapp` v31 já carregam o fix 24/7.
- **Ponto Certo** responde HTTPS 200 no domínio oficial; fallback legado permanece disponível.


## Qualidade da Memória (Criação do Compras — 25/05 19:25 BRT)
- Pedro pediu no tópico Compras para retomar a criação do agente de compras como Diretor.
- Fundação do agente top-level `compras` criada com nome humano **Scout** em `openclaw/agents/compras`, com IDENTITY/AGENTS/MEMORY/SOUL/TOOLS/USER/HEARTBEAT. Em seguida, subagente **Radar** criado em `openclaw/agents/compras/shared/radar`.
- Guardrail principal: Scout recomenda e planeja, mas não envia pedido a fornecedor, não negocia e não assume compromisso financeiro sem autorização explícita via Kobe/Pedro.
- Primeiro playbook canônico segue sendo a reposição de canecas: Tulipa, Paris, Canelada e Reta × seis cores, com kit colorido desmembrado em 1 unidade de cada cor.

## Qualidade da Memória (Consolidação Profunda 15/05)
- Últimos 15 dias revisados para main, Trader, Spark e Builder.
- Lições táticas expiradas removidas quando tinham `Expira` anterior a 15/05; auditorias registradas nos arquivos de lessons.
- Decisões/lessons perdidas promovidas: Amazon Ads em 5 camadas, Guarani aceite do acordo final, n8n usage tracking e Mission Control/PWA network-first.
- Agent memories de Trader, Spark e Builder atualizadas para refletir Daily Sales v2, Amazon Ads 5 camadas, Mission Control/Social Studio Reborn/Canggu.






## Qualidade da Memória (Consolidação Diária em Camadas 25/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos definidos para o ciclo; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Import Hub ganhou checagem anti-duplicação antes de alertas; Guarani passou a ter alerta específico de minuta/distrato/acordo assinado no inbox cleanup; DSA ML lapidou linguagem natural para Yasmin sem alterar a máquina analítica; Scout foi criado como Diretor de Compras com Radar como analista; Pedro aprovou estrutura Scout → Radar e cron semanal de canecas recalculando do zero; Budamix.com.br pivotou para 100% utensílios de vidro com combos IMB501 novos.
- Riscos críticos vindos dos digests: Daily Sales v2 segue sem condição de envio externo e pacote 24/05 foi parcial/ML-only; Shopee Store e Conta 3 precisam monitoramento; Bling Filial segue 403 pelo 11º dia e cron refresh teve rodadas sem validação útil; RH precisa orientação do Pedro para Guilherme, Leonardo, Mateus e Sandra antes de contato adicional.

## Qualidade da Memória (Consolidação Diária em Camadas 24/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Amazon Ads ganhou tópico oficial dedicado e nova régua de ACoS; rodada operacional executou ajustes em múltiplos grupos com validação live; Trader registrou Daily Sales v2 parcial para 23/05 sem Slack Writer/QA final; Fisco manteve Bling Filial 403 pelo 10º dia.
- Riscos críticos vindos dos digests: Daily Sales v2 sem condição de envio externo; Meta Ads ainda precisa validação; auditoria interna Amazon Ads/BidSpark segue pendente; Bling Filial bloqueia fluxos fiscais dependentes; backlog RH antigo permanece sem mudança.

## Qualidade da Memória (Consolidação Diária em Camadas 23/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: DSA ML amadureceu com sistema MercadoLíder, memory ingest diário, consolidações semanal/mensal, cron 06:50 BRT real e decisão híbrida Sonnet/Opus por camada; auditoria Ponto Certo confirmou ajustes sem duplicidade e refinou regras contra falsos positivos de jornada individual.
- Riscos críticos vindos dos digests: Fisco mantém Bling Filial 403 pelo 9º dia e alerta WhatsApp degradado; Spark mantém validação pendente do token Meta Ads e auditoria Amazon Ads/BidSpark; Trader/Builder/RH ficaram quietos sem novo risco crítico.

## Qualidade da Memória (Consolidação Diária em Camadas 22/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Import Hub/Terminal49 avançou em GB26001/GB26002; loop de estoque site↔planilha do e-commerce foi fechado; Vault/Ledger entraram em produção como área financeira; Ana/Canggu foi validada 7/7 E2E com notificações reais para Pedro; IMB501 e destaques do e-commerce foram ajustados; Gestão de Funcionários rodou consolidação semanal.
- Riscos críticos vindos dos digests: Trader não encontrou pacote completo do Daily Sales v2 para 21/05 BRT; Shopee/Amazon Rules Watch estão vencidos; Meta Ads ainda precisa validação de token; Bling Filial segue bloqueado/403; RH adicionou compliance 22/05 e backlog de 12 comunicações abertas.

## Qualidade da Memória (Consolidação Diária em Camadas 21/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Budamix E-commerce entregou preview mobile no admin e polimentos PDP; Canggu/Ana voltou a responder via fluxo real WhatsApp após v36/v42; Bling Filial foi pausado por decisão do Pedro; WhatsApp Health Check virou prioridade de substituição do N8N por script versionado; sync do segundo cérebro na VPS passou por escrita segura; reunião semanal de Yasmin foi registrada.
- Riscos críticos vindos dos digests: Daily Sales v2 segue sem envio real e Lucas/Shopee bloqueou por erro factual de percentual Store; Meta Ads precisa validação; Bling Filial continua risco conhecido porém adiado; RH agravou recorrência de Lucas sem almoço e Guilherme com intervalo de 51min.

## Qualidade da Memória (Consolidação Diária em Camadas 20/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: WhatsApp Himmel/Shopee criado e frequência Himmel reduzida para 3x/dia; Canggu/Ana corrigida contra silêncio e linguagem de cadastro/processo interno; Budamix E-commerce ganhou variações estruturadas e kits 4 travas temporariamente desativados; Estoque Budamix retomou deploy por rsync e substituiu parser PDF n8n por parser local validado; Gestão de Funcionários ganhou memórias individuais.
- Riscos críticos vindos dos digests: Daily Sales v2 ficou `PARTIAL` por bloqueio Lucas/Shopee em CTL002; envio aos funcionários segue bloqueado; Meta Ads precisa validação; Bling Filial 403 segue bloqueante; RH trouxe novas pendências de saída/intervalo em 20/05.

## Qualidade da Memória (Consolidação Diária em Camadas 19/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Daily Sales v2 passou os três recipients no QA com ressalvas e removeu o bloqueio crítico anterior de Lucas/Shopee; Spark e Builder ficaram quietos; Fisco manteve Filial Bling 403 e alerta WhatsApp degradado; RH registrou novos riscos de compliance em 19/05.
- Riscos críticos vindos dos digests: envio Daily Sales para funcionários ainda bloqueado; decisão pendente sobre aceitar `APPROVED_WITH_REMARKS` sem críticos/maiores; token Meta Ads ainda precisa validação; Filial Bling segue impedindo fluxos fiscais dependentes; RH precisa orientação do Pedro para Guilherme/Lucas e validação de marcações atípicas.

## Qualidade da Memória (Consolidação Diária em Camadas 18/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: reunião OS/OSA de câmbio para importação; diagnóstico do Daily Sales v2 com bloqueio correto de Lucas/Shopee por duplicidade de Top Produtos; correção RH contra cobrança de pendências já cobertas; Meta Ads atingiu janela estimada de expiração do token; Bling Filial 403 persistiu.
- Riscos críticos vindos dos digests: envio Daily Sales para funcionários ainda bloqueado; Lucas/Shopee precisa reexecução localizada antes de nova tentativa Pedro-only; Meta Ads precisa validação de token; Bling Filial segue impedindo fluxos fiscais dependentes; RH precisa decisão do Pedro para Guilherme, Lucas, Mateus e Sandra.

## Qualidade da Memória (Consolidação Diária em Camadas 17/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Daily Sales v2 teve correção de ressalvas, envio controlado ao Slack pessoal do Pedro e diretriz ajustada para clareza sem mudar formato/profundidade; Mission Control ganhou painel visual do pipeline Daily Sales; Bling Filial 403 e Meta Ads token seguem riscos operacionais.
- Riscos críticos vindos dos digests: envio Daily Sales para funcionários ainda bloqueado; Lucas/Shopee segue com ressalva numérica menor na 6B; Shopee Rules Watch está vencido e não deve sustentar hipótese causal forte; painel Mission Control precisa restart/smoke; Bling Filial bloqueia fluxos fiscais dependentes.

## Qualidade da Memória (Consolidação Diária em Camadas 16/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Daily Sales v2 em preview aprovado com ressalvas e sem envio externo; Meta Ads com token a renovar antes de 18/05; Bling Filial 403 recorrente com alerta WhatsApp degradado; RH sem violação nova no sábado, mas com lacuna documental de política sábado/domingo.
- Riscos críticos vindos dos digests: envio Daily Sales para funcionários ainda bloqueado; Bling Filial impede fluxos fiscais dependentes; próxima rodada Amazon Ads/BidSpark não deve ocorrer antes da auditoria interna de logs; token Meta Ads vence em janela curta.

## Qualidade da Memória (Consolidação Diária em Camadas 15/05 — 23:45 BRT)
- Kobe consolidou apenas o próprio dia/main e os digests dos agentes diretos; não varreu memória interna de Trader, Spark, Builder, Fisco ou RH.
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Nenhum digest ausente neste fechamento.
- Marcos globais incorporados: Alertas no thread 10204, Daily Sales Report - SLACK no thread 10222, Gestão de Funcionários no thread 10469, Pedidos Atacado Automação no thread 10494, Compras no thread 11, Daily Sales v2 com LLM principal/Pedro-only, e piloto do futuro Agente de Compras.
- Riscos críticos vindos dos digests: Bling Filial 403/inativa, pendências RH de ponto/intervalos, Shopee Rules Watch vencido e necessidade de validar a primeira execução real do Daily Sales v2 sem fallback determinístico.

## Qualidade da Memória (Pipeline em Camadas 15/05)
- Consolidação Diária deixou de ser monolítica: Trader, Spark, Builder, Fisco e RH consolidam suas próprias memórias.
- Cada agente direto gera digest diário para Kobe em `memory/agent-digests/YYYY-MM-DD/<agent>.md`.
- Kobe consolida apenas o próprio dia + digests dos agentes diretos; subagentes internos sobem via agente-pai.
- Fechamento técnico às 00:05 BRT centraliza commit/push/indexação para reduzir conflitos e timeouts.

## Qualidade da Memória (Consolidação Diária 30/04)
- **sessions/2026-04-30.md:** consolidado com Budamix Central Full/Estoque, Canggu, RH/Ponto Certo, GitHub→Vercel e pendências finais.
- **pending.md:** limpo; removidas pendências resolvidas de cadastro de SKU base/2D; adicionadas Estoque Fase 2-4, Canggu, RH e validações reais.
- **decisões:** já registradas em `memory/context/decisoes/2026-04.md` para RH, Canggu, Ponto Certo, Vercel, Full/Estoque.
- **lessons.md:** atualizado com fonte canônica, guardrails determinísticos, mensagens interativas Evolution/Baileys, parser BR e SSoT de repo.
- **shared/trader/spark/builder/rh:** sessões 30/04 criadas; Builder/RH receberam decisões/lições e pendências atualizadas.
- **feedbacks:** registrada rejeição parcial de design do Estoque Fase 1 funcional porém abaixo do padrão visual.

## Timeline Recente
- **2026-05-28:** Estoque GB virou frente central: Pedro aprovou motor de movimentações auditáveis antes da planilha, criou grupos WhatsApp/tópicos Telegram de Estoque e Devoluções, Fase 1 foi implementada e Fase 2 avançou com resolver de SKU, aliases, BOM de kits e smoke test 5/5. A aba ESTOQUE foi redefinida para SKUs pai/unitários com exceções explícitas; QCB002 e xícaras RR foram corrigidos; a limpeza expôs dependências em SHOPEE/AMAZON e parte das margens/lucros foi recuperada. Daily Sales de 27/05 reportou R$ 12.622,97 em 238 pedidos; Shopee recebeu Ramp Up de potes e exige leitura D+1/D+3/D+7. RH manteve backlog sensível e Fisco manteve Bling Filial 403 pelo 14º dia.
- **2026-05-27:** Regra operacional do vault foi endurecida após Watchdog detectar 3 commits stuck: toda escrita no segundo-cérebro deve usar escrita segura, e o script ganhou catch-up automático. Planilha de Estoque/Precificação recebeu regra global de valores em padrão brasileiro e rodada grande de pricing: custos de canecas com desconto de 10%, devoluções reais por anúncio em MELI/Shopee/Amazon e 19 linhas Amazon novas. Daily Sales de 26/05 reportou R$ 12.864,40 em 253 pedidos, mas segue com ciclo final ML-only e data readiness parcial por Shopee Conta 2 fraca e 6 cancelamentos Amazon.
- **2026-05-25:** Compras ganhou o 7º diretor top-level Scout, com Radar como analista e estrutura Scout → Radar aprovada; cron semanal de canecas deve recalcular planejamento do zero com dados até D-1. Budamix.com.br pivotou para 100% utensílios de vidro, com hero retina-safe, swipe, combos IMB501 novos e correções mobile/cache. DSA ML refinou a comunicação final da Yasmin para linguagem natural, enquanto Daily Sales v2 continuou parcial/ML-only no pacote 24/05. Import Hub ganhou alerta anti-duplicação e Guarani entrou no radar específico de minuta/distrato/acordo assinado.
- **2026-05-23:** DSA ML virou pipeline maduro com MercadoLíder, memory ingest diário, consolidações semanal/mensal, cron corrigido para 06:50 BRT real e modo híbrido Sonnet/Opus por camada; auditoria Ponto Certo validou ajustes aprovados sem duplicidade e incorporou regra de contexto individual para Mateus/Tiro de Guerra e intervalos <1h.
- **2026-05-22:** Import Hub anexou documentos e ativou Terminal49 para GB26001/GB26002; e-commerce fechou loop de estoque site↔planilha e reparou IMB501/destaques; Vault/Ledger entraram em produção como área financeira; Ana/Canggu fechou 7/7 E2E com escalação/notificação real; Daily Sales v2 ficou com lacuna operacional para 21/05; RH registrou novos riscos de compliance.
- **2026-05-21:** Budamix E-commerce ganhou preview mobile no admin e polimentos de PDP; Canggu/Ana voltou a responder via fluxo real WhatsApp após pacote v36/v42; Pedro pausou Bling Filial e priorizou WhatsApp Health Check versionado; sync da VPS passou a usar escrita segura; Gestão de Funcionários registrou reunião semanal com Yasmin; Daily Sales v2 ficou em preview `APPROVED_WITH_REMARKS`, mas Lucas/Shopee bloqueou por erro factual de percentual Store.
- **2026-05-20:** Canggu/Ana teve correção estrutural do silêncio de 9 dias e regra 17 contra respostas de cadastro/processo interno; WhatsApp Himmel/Shopee foi integrado e ambos os grupos Himmel passaram a 3 ingestões diárias; Estoque Budamix voltou a produção via rsync com parser PDF local validado; Budamix E-commerce ganhou variações estruturadas e desativou temporariamente kits 4 travas; Gestão de Funcionários ganhou memórias individuais; Daily Sales v2 ficou PARTIAL por bloqueio Lucas/Shopee.
- **2026-05-19:** Daily Sales v2 recuperou a falha de Lucas/Shopee do dia anterior e aprovou os três recipients com ressalvas em preview Pedro-only, sem envio real aos funcionários. Spark e Builder ficaram quietos; Fisco manteve Bling Filial 403 + alerta WhatsApp degradado; RH adicionou riscos de compliance para Guilherme/Lucas/Leonardo/Franciele.
- **2026-05-18:** Daily Sales v2 falhou de forma segura no cron 06:50: Lucas/Shopee bloqueou no QA por duplicidade de Top Produtos, enquanto Yasmin/ML e Leonardo/Amazon chegaram ao QA com ressalvas; próximo passo é corrigir/reexecutar apenas Lucas. RH recebeu trava determinística contra cobrança de pendências já cobertas. Reunião OS/OSA abriu possível alternativa de câmbio para importações. Meta Ads precisa validação pós-expiração estimada do token; Bling Filial 403 segue bloqueante.
- **2026-05-17:** Daily Sales v2 avançou em validação controlada: Pedro recebeu versões finais no Slack pessoal, corrigiu a diretriz para manter formato/profundidade e simplificar a comunicação, e o rerun completo Shopee ficou aprovado com ressalva numérica menor. Mission Control ganhou painel visual do pipeline Daily Sales; Spark/RH ficaram quietos; Fisco manteve Bling Filial 403; envio real aos funcionários segue bloqueado.
- **2026-05-16:** Consolidação em camadas rodou com os 5 digests presentes. Daily Sales v2 teve preview dos três reports aprovado com ressalvas, sem envio externo e sem liberação para funcionários; Spark manteve risco de token Meta Ads expirar em 18/05; Fisco confirmou Bling Filial 403 recorrente e alerta WhatsApp degradado; RH não trouxe violação nova no sábado, mas apontou lacuna de política canônica sábado/domingo.
- **2026-05-15:** Consolidação diária em camadas entrou em operação com digests dos 5 agentes diretos. Alertas técnicos foram fixados no tópico Alertas (thread 10204); Daily Sales Report Slack ganhou tópico próprio (10222), LLM como caminho principal aprovado tecnicamente para os 3 recipients e produção temporária Pedro-only; Compras/Agente de Compras nasceu com piloto de reposição das canecas; Gestão de Funcionários (10469) e Pedidos Atacado Automação (10494) ganharam tópicos dedicados; WhatsApp Himmel/ML passou a alimentar contexto read-only do Trader.
- **2026-05-14:** Mission Control avançou forte: `/activity`, `/cron`, `/sessions`, `/skills` e `/costs` fechados, totalizando 11/23 módulos. `/cron` e `/sessions` foram reescritos para ler arquivos JSON direto do disco em vez de depender do CLI travando no PM2; `/skills` passou a scan automático de 118 skills; `/costs` separou custo real API vs equivalente API vs subscription. Validação crítica: OpenClaw/GPT-5.x roda coberto pela subscription Pro 5x (custo real zero nos crons), enquanto n8n usa OpenAI/Anthropic API keys e precisa tracking próprio.
- **2026-05-12:** Daily Sales Report v2 virou a frente central do dia: Fases 1–8 implementadas (mapeamento por `shop_id`, memória em camadas do Trader, motor de análise profunda, Slack individual, wrapper/cron real, consolidações semanal/mensal, Granola/Himmel e Marketplace Rules Watch). Pedro rejeitou previews rasos e travou templates finais por plataforma com análise densa, nome comercial obrigatório e títulos Slack rich_text. Integração Granola foi criada via API Key e ajustada para sync diário 20:37 BRT. Shopee Fees Monitor ganhou política `OFICIAL_FIRST`. Planilha de avaliações Amazon foi gerada/corrigida. Mission Control retomou com domínio `mission.budamix.com.br`, visual Budamix e dashboard real. Amazon Ads Tulipa executou 7/7 bids, com pendência de log interno BidSpark.
- **2026-05-11:** Dia com incidentes e rotinas novas: Daily Sales Report para equipe administrativa aprovado via Slack DM às 06:50 BRT; RH recebeu liberação específica para resolver o lote de ponto 04/05–09/05 e ganhou hardening `@lid` no inbound; Canggu/Ana teve regressão grave no ML “entre em contato conosco” corrigida em produção e no repo canônico `PHPB2025K/canguu` (`eb76d3f`); Amazon Ads D+7 foi retomado com grupos críticos identificados; Budamix Central passou a filtrar pedidos Amazon de remoção FBA como não-venda.
- **2026-05-09:** Dia enxuto e jurídico/operacional: Pedro formalizou o tom padrão para mensagens escritas em nome dele (profissional, objetivo, sem cordialidade excessiva); Guarani avançou com e-mail autorizado e enviado à Priscilla reforçando que R$ 7.500,00 à vista é proposta global/all-in para quitação integral e definitiva; Daily Sales Report do Trader teve primeira execução registrada como OK e prompt endurecido para não exibir produto/SKU não identificado no Top Produtos.
- **2026-05-08:** Dia mais de consolidação do que construção: Daily Sales Report — Trader aprovado e criado para rodar diariamente às 06:30 BRT no tópico Marketplaces, consolidando ML, Shopee 3 contas, Amazon BR e Bling Matriz como Atacado - GB Matriz. Gestão de Funcionários rodou leitura semanal via Slack com atas formais de Lucas e Leonardo e pontos operacionais de Yasmin. Canggu/Ana voltou a aparecer como risco P0 por resposta de horário comercial/origin poll, sem falso positivo de correção por ausência de acesso ao repo canônico na sessão atual.
- **2026-05-07:** Dia de correções estruturais e avanço de produto: Guarani consolidada em contraproposta final de R$7,5k; Adapta teve busca profunda no Gmail e mensagem de contestação; Gestão de Funcionários criada com Slack como fonte oficial; Canggu/Ana teve webhook Evolution sem auth corrigido e backfill controlado; Kobe/OpenClaw ganhou invisibilidade de bootstrap, debounce inbound 8s e ChatGPT Pro 5x; GB Import Hub voltou após habilitar nginx; Social Studio Reborn teve Fase B mergeada e Fase C iniciada com C1 fechado.
- **2026-05-06:** Social Studio passou por dois pivots e renasceu como Reborn: publicador + métricas Instagram, sem IA, com Fase A/PR #3 concluída e 5 Edge Functions legacy removidas da produção via Supabase REST API. Canggu/Ana teve incidente 24/7 resolvido em produção com prompt reforçado, guardrail determinístico e origin poll defensivo; DRE abril recebeu arquivo atual no vault e regra de canônico contínuo; U15 segue aberta com ML validado, Amazon/Shopee pendentes.
- **2026-05-05:** Dia pesado de correção de drift e produto: Ponto Certo ganhou DNS+SSL oficial em `ponto.budamix.com.br`; RH WhatsApp proativo foi bloqueado indefinidamente; Canggu migrou para `canggu.com.br`, eliminou drift de 13 Edge Functions com GitHub Actions e ajustou o tom/hard-block da Ana no ML; Social Studio avançou PR1+PR2 com paletas, swatches, histórico/restore de imagens e edge functions corrigidas, restando bug `cover-numeric`; Estoque Budamix ganhou repo canônico e PR1+PR2+PR3a, mas deploy pausou por falta de credencial GitHub na VPS; DRE abril confirmou U15 antes da U44 v4 limpa.
- **2026-05-04:** Dia de reset operacional pós-refatoração: Pedro mandou limpar pendências/inconformidades de abril da fila ativa; DRE abril corrigida para devolução estrita pós-recebimento (0,62%, ou 0,70% conservador com retorno em trânsito); Ponto Certo teve rota Traefik corrigida para `ponto.budamix.com.br` e ficou bloqueado apenas por DNS; RH WhatsApp foi bloqueado para proativos, reativado para inbound com guard `--allow-rh-reply`, `linkPreview:false` e reenvios autorizados para Yasmin/Leonardo; Budamix Live Sales mudou meta para R$15k; Social Studio Carrossel fechou Fase 1 em produção com pipeline E2E, export PNG/PDF e custo ~$0,31/carrossel.
- **2026-05-03:** Amazon Ads fechou a cobertura dos grupos finais de abril: Kits Microfibra executado com criação de Exact `pano microfibra` e escala de Auto; Abraçadeiras Nylon virou experimento de tração após confirmação de 24 un FBA no ASIN ativo; Redinha Frutas e Kit Jardinagem ficaram sem bid por falta de entrega/estrutura. Pedro consolidou o framework obrigatório de 3 blocos para Ads. No CC local, templates Budamix no Paper.design foram concluídos em 96 artboards (5 famílias × 3 paletas), com decisões de CLARA teal/fundo areia e limitação de shaders via MCP registrada.
- **2026-05-02:** Budamix Central/Live Sales teve meta diária alterada para R$20k em produção. Amazon Ads virou frente principal do dia: abril fechado usado como baseline, com cortes/harvesting/escala em 9 grupos (Potes Vidro, Canequinhas, Bambu, Canelada, Tulipa, Paris, Suporte Gamer, Jarra Medidora e Potes Redondos), D+7 pendente e Kits Microfibra aguardando aprovação. CC local instalou `epic-paper` e `video-use`, primeiro carrossel Profundo Budamix ficou 5/7 cards, e Guarani Sistemas teve estratégia de contestação/distrato com teto técnico R$7.002,30 sem reconhecimento de dívida.
- **2026-05-01:** Fechamento financeiro abril revisado: faturamento comercial R$405,8k separado de settlement R$355,0k; Ads reais validados (ML R$5.441,44, Shopee R$9.460, Amazon R$2.478,95) e DRE profissional clássica definida como padrão obrigatório. Fisco emitiu NFs internas abril Filial→Simples 000031–000033 (R$77.065,09) após reconciliação fiscal por SKU/componente, exclusão CK4742/Jarra Clink e validação IPI; PDFs/XMLs enviados à FOUR e financeiro. NFs de transferência 000649/000653 também enviadas à FOUR com ressalva sobre orientação Suellen v2.1.
- **2026-04-30:** Budamix Central Full fechado com `zero_cost=0` após planilha oficial, matching multi-fonte e filtro de fantasmas Amazon; módulo Estoque criado/refinado com capital total ~R$709k; Canggu consolidado em repo único/edge pipeline + mídia visível + guard ML; RH entrou em operação com mensagens inaugurais, polling anti-webhook-fail e Conversas RH; GitHub→Vercel auto-deploy ativado.
- **2026-04-29:** Blog Budamix Pipeline v2 fechado em produção (7 fases: `blog_pillars`, WF0 Perplexity, WF2 Sonnet 4.6 como diretor de arte, WF3 aspect ratio, WF4 validações, Admin com PillarSelect/AddPinManualDialog e validação E2E 6/6). Budamix Central ganhou baseline GitHub/tag rollback e refactor Full: Shopee 3 contas sincronizando, `sync-costs.py` corrigido, KPI Custo filtrável, Live Sales alinhado à Home por `v_daily_sales`. Social Studio seguiu em preview até render PNG, ainda sem merge produção.
- **2026-04-28:** Vault-as-SSoT validado 8/8 e workspace antigo deprecado; Blog Budamix/Admin corrigiu falso erro de geração, separou Em geração/Rascunhos, endureceu WF4 por estado real no Supabase e deployou via VPS/Vercel; Social Studio nasceu com SPEC, persistência Supabase, preview Vercel, geração de copy, editor manual, render PNG e wizard. Trader/Spark sem execução delegada; Builder sem RESULT.md novo.
- **2026-04-27:** Blog Budamix/Admin v2 virou a frente principal: WF4 Orchestrator, Admin Blog SPEC v2.0, WF0/WF2/WF4 corrigidos, fluxo final `gerando` → `em_edicao` → `preview` → `publicado`, UX de preview/editor, reset de pipeline, DNA editorial/visual/emocional aprovado, template de artigos encurtado e Amazon Request Review ajustado para 7–12 dias. GitHub do ecommerce destravado via PAT nas Observações do 1Password.
- **2026-04-26:** Integração Slack read-only criada, Google Sheets e WhatsApp histórico validados, e Blog Budamix avançou de placeholder para fundação no repo principal + N8N Draft Generator + WF0 Perplexity + Admin Blog Review em produção. No delta pós-consolidação, houve retrofit dos 3 artigos legados e SEO técnico deployado, com pendência de push GitHub/keys REST Supabase/N8N API key. Lições críticas registradas: Builder em repo privado precisa validar repo principal e deploy frontend exige smoke test renderizado amplo.
- **2026-04-25:** Pedro formalizou a diretriz de migração total para GPT-5.5 via ChatGPT Pro, com guardrails de backup, validação e rollback. Consolidação diária limpou o pending, reposicionou GPT-5.5 como prioridade atual e registrou ausência de atividade nova de Trader, Spark e Builder.
- **2026-04-23:** Consolidação diária silenciosa com revalidação integral do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção fiel do estado operacional do sistema.
- **2026-04-20:** Consolidação diária silenciosa com revalidação integral do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção do índice central sem mudanças estruturais artificiais.
- **2026-04-17:** Consolidação diária silenciosa com limpeza conservadora do pending principal, registro explícito de ausência de atividade nova dos agentes e manutenção do índice central sem mudanças estruturais artificiais.
- **2026-04-15:** Consolidação profunda quinzenal seguida de consolidação diária silenciosa. Pending principal foi limpo de forma conservadora, com itens antigos sem movimentação migrados para backlog estagnado. Trader, Spark e Builder fecharam o dia sem atividade nova e com sessões explícitas registradas.
- **2026-04-04:** Trader e Spark promovidos para GPT 5.4. Catálogo da Ana consolidado em CSV com 62 SKUs. Canggu conferido com 87/87 embeddings OK.
- **2026-04-06:** Planilha Excel de composição de kits entregue, arquivo `PRE PACKING LIST - GB25008.xlsx` recuperado do Gmail, base Ana avançada, seção Vibe incorporada ao SOUL e HIGH aplicado como default persistido para agentes/chats novos.
- **2026-04-07:** PCM001 lançado no Mercado Livre, nas 3 lojas Shopee e na Amazon BR com submission aceita e ASIN pendente. Playbook de restauração de contexto pós-troca de modelo reforçado. Kit de segundo cérebro avaliado como sólido para Claude Code local e incompleto para a camada OpenClaw/VPS.
- **2026-04-08:** Dia de baixa atividade operacional nova. Pending foi limpo de itens resolvidos já marcados, a skill `shopee-fees-rules` recebeu clarificações de abril/2026, e os alertas técnicos reais foram mantidos enxutos.
- **2026-04-09:** Dia de manutenção silenciosa. Sem execução nova relevante de Trader, Spark ou Builder. A consolidação reforçou o estado real das pendências e preservou a memória sem criar falsos avanços.
- **2026-04-14:** Nova manutenção silenciosa consolidada, com revalidação do pending principal, confirmação de ausência de atividade nova dos agentes especializados e permanência do bloqueio de autenticação GitHub para push/backup.

---

_Próximas ações: (1) validar motor de estoque em tabelas reais, corrigir ENVIOS FULL e receber IDs dos envios criados em 28/05, (2) diagnosticar pollings WhatsApp GB e extração Slack funcionários, (3) confirmar se Daily Sales v2 deve continuar ML-only/Pedro-only ou voltar ao ciclo completo Lucas/Shopee e Leonardo/Amazon, (4) acompanhar Ramp Up Shopee potes em D+1/D+3/D+7 e investigar conta a conta, (5) acompanhar primeira consolidação semanal DSA ML em 02/06 e adicionar sanity check `suspect_zero_spend`, (6) fechar reposição de canecas após Pedro enviar pedidos em trânsito/já feitos, (7) implementar WhatsApp Health Check/validador Canggu versionado e pós-mortem do JWT, (8) orientar RH nos casos Sandra/Mateus/Guilherme/Lucas sem liberar proativo genérico, (9) validar token Meta Ads pós-18/05, (10) decidir Jarra Medidora e ajustar fotos/estoque/conteúdo do Budamix.com.br pós-pivot._

---
## Contexto
- [[openclaw/agents/kobe/memory/context/decisions|Decisões]]
- [[openclaw/agents/kobe/memory/context/lessons|Lições]]
- [[openclaw/agents/kobe/memory/context/people|Pessoas]]
- [[openclaw/agents/kobe/memory/context/business-context|Contexto do Negócio]]
- [[openclaw/agents/kobe/memory/projects/gb-importadora|GB Importadora]]
- [[openclaw/agents/kobe/memory/integrations/tools-map|Ferramentas e Integrações]]
- [[openclaw/agents/kobe/memory/integrations/telegram-map|Telegram — Kobe Hub]]
- [[openclaw/agents/kobe/memory/pending|Pendências]]

## Outputs dos Agentes
- [[openclaw/agents/kobe/shared/outputs/trader-platforms|Output Trader Platforms]]
- [[openclaw/agents/kobe/shared/outputs/trader-IDENTITY|Output Trader IDENTITY]]
- [[openclaw/agents/kobe/shared/outputs/trader-IDENTITY-v2|Output Trader IDENTITY v2]]
- [[openclaw/agents/kobe/shared/outputs/trader-SOUL|Output Trader SOUL]]
- [[openclaw/agents/kobe/shared/outputs/trader-AGENTS|Output Trader AGENTS]]
- [[openclaw/agents/kobe/shared/outputs/trader-MEMORY|Output Trader MEMORY]]
- [[openclaw/agents/kobe/shared/outputs/trader-decisions|Output Trader Decisions]]
- [[openclaw/agents/kobe/shared/outputs/trader-lessons|Output Trader Lessons]]
- [[openclaw/agents/kobe/shared/outputs/trader-pending|Output Trader Pending]]

## Workspaces dos Agentes
- [[openclaw/agents/kobe/shared/builder/MEMORY|Builder Workspace]]
- [[openclaw/agents/kobe/shared/fisco/MEMORY|Fisco Workspace]]
- [[openclaw/agents/kobe/shared/spark/MEMORY|Spark Workspace]]
- [[openclaw/agents/kobe/shared/rh/SOUL|RH Workspace]]
- [[openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao|Reforma Tributária (SimulImport)]]



## Qualidade da Memória (Consolidação em Camadas — 28/05 23:45 BRT)
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Digests ausentes: nenhum.
- Escopo respeitado: Kobe/main + digests dos agentes diretos definidos no cron; sem varrer memória interna de agentes, subagentes, workers ou analysts temporários.
- Marcos globais incorporados: Estoque GB aprovado como motor de movimentações auditáveis; grupos WhatsApp e tópicos Telegram de Estoque/Devoluções criados; Fase 1 e Fase 2 do motor de estoque avançaram; aba ESTOQUE redefinida para SKUs pai/unitários com exceções; correções QCB002/xícaras RR; Daily Sales de 27/05 com R$ 12.622,97 em 238 pedidos e Ramp Up Shopee para potes.
- Riscos críticos vindos dos digests: Daily Sales v2 segue com risco ML-only; Shopee precisa leitura por conta em D+1/D+3/D+7; Bling Filial segue 403 pelo 14º dia e alerta WhatsApp degradado; RH precisa orientação para Sandra, Mateus, Guilherme, Lucas e backlog de 16 comunicações.

## Qualidade da Memória (Consolidação em Camadas — 27/05 23:45 BRT)
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Digests ausentes: nenhum.
- Escopo respeitado: Kobe/main + digests dos agentes diretos; sem varrer memória interna de agentes, subagentes, workers ou analysts temporários.
- Marcos globais incorporados: regra obrigatória de escrita segura no vault após alarme de commits stuck; regra de formato brasileiro para valores na planilha de estoque/preço; rodada de pricing das canecas com desconto de 10%, devoluções reais por anúncio em MELI/Shopee/Amazon e novas linhas Amazon; Daily Sales de 26/05 com R$ 12.864,40 em 253 pedidos, mas data readiness parcial.
- Riscos críticos vindos dos digests: Daily Sales v2 segue recorrente em ML-only/Pedro-only e precisa decisão se isso é desenho ou lacuna; Shopee Conta 2 caiu forte em 26/05; Amazon teve 6 cancelamentos; Bling Filial segue 403 pelo 13º dia; RH precisa orientação para Sandra, Mateus, Leonardo, Lucas e backlog de 16 comunicações.

## Qualidade da Memória (Consolidação em Camadas — 26/05 23:45 BRT)
- Digests lidos: Trader, Spark, Builder, Fisco e RH. Digests ausentes: nenhum.
- Escopo respeitado: Kobe/main + digests dos agentes diretos; sem varrer memória interna de agentes, subagentes, workers ou analysts temporários.
- Marcos globais incorporados: Daily Sales v2 com pacote 25/05 DADOS_OK mas ciclo final ainda ML-only/Pedro-only; Shopee Full+ como risco de margem/mix; Bling Filial 403 pelo 12º dia; RH com Sandra sem marcações e backlog de 16 comunicações.
- Nenhuma decisão global nova do Pedro; uma lição global adicionada sobre interpretação de Shopee Full+.

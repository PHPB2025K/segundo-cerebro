---
title: "Lições aprendidas"
created: 2026-04-28
type: context
status: active
tags:
  - memory
  - context
  - lessons
  - kobe-import
---

# Lições Aprendidas

_Erros e aprendizados. Consultar antes de repetir algo que já deu errado._
_Tags: [ESTRATÉGICA] = permanente | [TÁTICA] = expira em 30 dias_
_Última Consolidação Profunda: 2026-04-15_

---

## Lições Estratégicas (Permanentes)

### [ESTRATÉGICA] 1Password/GitHub: token válido pode estar nas Observações, não no password (2026-04-27)
**Contexto:** Push do `PHPB2025K/budamix-ecommerce` falhou porque o primeiro teste leu apenas o campo `password` do item `GitHub PAT - Budamix Ecommerce`, que continha valor inválido. Pedro confirmou que costuma guardar PAT nas Observações do item.
**Lição:** Ao usar PATs do GitHub no 1Password, testar candidatos nesta ordem: campos `Observações`/`notesPlain` dentro de `fields`, nota top-level e só depois `password`/`token`. Nunca concluir que o token está inválido sem verificar Observações.

### [ESTRATÉGICA] Budamix E-commerce: entrega final só vale no repo principal privado (2026-04-26)
**Contexto:** Builder job do blog criou arquivos em workspace isolado porque o clone anônimo falhou no repo privado `PHPB2025K/budamix-ecommerce`.
**Lição:** Para Budamix E-commerce, nunca tratar workspace isolado/artefato Builder como entrega final. Validar remote do repo principal, credencial correta do 1Password, build, commit e push no GitHub antes de anunciar conclusão.

### [ESTRATÉGICA] Deploy frontend: validar experiência visível, não só build/rota principal (2026-04-26)
**Contexto:** `/blog` estava funcionando com posts reais, mas a seção de blog da home ainda mostrava “Em breve”.
**Lição:** Após deploy de frontend, fazer smoke test renderizado da rota afetada e também das seções relacionadas da home/header/footer/CTAs. Build OK + rota OK não garante que a experiência pública refletiu a mudança.

### [ESTRATÉGICA] Consolidado financeiro com dados parciais apresentados como completos (2026-04-03)
- **Erro:** Entreguei consolidado de março usando extrato Shopee budamix-store de 01-20/03 (gerado em 20/03) como se fosse mês completo. Diferença: R$3.224 e 100+ pedidos.
- **Causa raiz:** Reusei arquivo antigo sem validar que o período não cobria o mês inteiro. Não havia carimbo de período real no arquivo.
- **Impacto:** Relatório consolidado, DRE e decisões tomadas com base em números errados.
- **Fix:** 5 regras de QA financeiro permanentes implementadas em 4 arquivos core (AGENTS Kobe + Trader, MEMORY Kobe + Trader).
- **Regra:** NUNCA entregar relatório financeiro sem validar que TODOS os extratos cobrem o período completo. Dado parcial ≠ dado completo.

### [ESTRATÉGICA] Edit tool falha por race condition em arquivos compartilhados (2026-04-02)
**Contexto:** Erro "Edit: in openclaw/agents/kobe/memory/sessions/... failed" recorrente em crons (Consolidação Profunda, Session Extractor).
**Erro:** Edit exige oldText exato. Se outra sessão modifica o arquivo entre leitura e edit, o match falha.
**Lição:** Em arquivos que múltiplas sessões escrevem (lessons.md, sessions/*.md, pending.md), usar Read → Write completo em vez de Edit cirúrgico. Edit é seguro apenas para arquivos que só uma sessão toca por vez.
**Ação:** Crons instruídos a usar Read+Write. Consolidação Profunda 2026-04-04 executada com sucesso usando Write.

### [ESTRATÉGICA] Arquivos = sendDocument, nunca fatiar em texto (2026-04-01)
**Contexto:** Pedro pediu briefing .md e Kobe fatiou em 7 mensagens de texto em vez de enviar o arquivo.
**Lição:** A Bot API do Telegram suporta sendDocument via curl. Qualquer entregável (briefing, relatório, CSV, PDF, Excel, JSON) deve ser enviado como documento — nunca fatiado em mensagens. Capacidade registrada em TOOLS.md.

### [ESTRATÉGICA] Troca de modelo sem reindexação e warm-up degrada recall operacional (2026-04-07)
**Contexto:** Na migração para zero Anthropic, parte da aderência do Kobe caiu mesmo com a memória em disco preservada.
**Lição:** Depois de qualquer troca estrutural de modelo/fallback, o playbook correto é: reindexação forçada da memória, warm-up do bootstrap e teste rápido de recall antes de tarefa crítica.
**Ação:** Tratar restauração de contexto como etapa operacional obrigatória, não detalhe opcional.

### [ESTRATÉGICA] SP-API Solicitations: endpoint correto é productReviewAndSellerFeedback (2026-04-02)
**Contexto:** Script de Request Review retornava 403 Unauthorized em todos os pedidos.
**Lição:** O endpoint correto é `productReviewAndSellerFeedback` (nome completo). Sempre validar com GET `/solicitations/v1/orders/{id}` primeiro.

### [ESTRATÉGICA] SP-API Orders API: usar Supabase como fonte, não chamar API direto (2026-04-02)
**Contexto:** Script de Request Review ficou em loop infinito de 429 tentando buscar orders via API.
**Lição:** Pedidos já estão sincronizados no Supabase (tabela orders, cron a cada 30min). Sempre usar Supabase como fonte de dados quando possível, e a SP-API apenas para ações (solicitations, inventory updates, etc).

### [ESTRATÉGICA] Amazon SP-API ItemPrice.Amount é total do line item, NÃO preço unitário (2026-04-01)
**Contexto:** Curva ABC mostrava receita inflada em orders com qty > 1. 447 + 179 orders corrigidos.
**Lição:** Sempre dividir ItemPrice.Amount pela quantidade para obter preço unitário. Para preço do anúncio, usar Listings Items API (getListingsItem com includedData=offers), não getPricing (não retorna preço do seller no marketplace Brasil).

### [ESTRATÉGICA] Amazon getPricing não retorna preço do seller pro Brasil — usar getListingsItem (2026-04-01)
**Contexto:** Investigação de fontes de preço pra módulo Preços v2.
**Lição:** Para preço de anúncio Amazon BR, usar getListingsItem com includedData=offers → offers[0].price.amount. Rate limit 5 req/s, 59 SKUs em ~15s.

### [ESTRATÉGICA] Cron de relatório financeiro: validar tokens ANTES de executar (2026-04-01)
**Contexto:** Cron do relatório mensal rodou às 03h BRT, executou em ~1min37s (muito rápido), não gerou arquivos, delivery falhou.
**Lição:** Relatórios que dependem de APIs externas precisam de pré-validação de tokens. Se qualquer token falhar, abortar e notificar — não executar parcialmente em silêncio.

### [ESTRATÉGICA] Amazon SP-API: armadilhas recorrentes (2026-04-01) ⬆️ Promovida
**Contexto:** 5+ ocorrências (2026-03-25 a 2026-03-27): timeouts, rate limits, dependências circulares, nextToken em payload, OrderTotal vazio em Pending.
**Checklist obrigatório:**
1. nextToken fica em `payload`, NÃO em `pagination`
2. OrderTotal = null para pedidos Pending (montar catálogo de preços)
3. getOrderItems tem rate limit agressivo (200ms+, backfill leva horas)
4. Edge Functions do Supabase não aguentam syncs Amazon (migrar para VPS)
5. sync-prices depende de products populada — rodar catalog primeiro
6. Brasil usa endpoint NA (`advertising-api.amazon.com`), NÃO SA

### [ESTRATÉGICA] Mock data como fallback = bomba silenciosa (2026-04-01) ⬆️ Promovida
**Contexto:** 3 ocorrências (2026-03-25, 2026-03-26).
**Lição:** NUNCA usar dados mock/fake como fallback em dashboards financeiros. API crashou → mostrar skeleton/erro, NÃO dados inventados. Mock data mascara bugs, gera confiança falsa nos números, e consome tempo debugando o lugar errado.

### [ESTRATÉGICA] Deploy/preview na VPS: SEMPRE via Traefik HTTPS (2026-04-01) ⬆️ Promovida
**Lição consolidada:** NUNCA servir previews em portas custom ou HTTP puro. SEMPRE usar subdomínio dedicado `*.srv1480018.hstgr.cloud` via Traefik com HTTPS automático (Let's Encrypt). Subpath → subdomínio. UFW → Traefik. HTTP → HTTPS. Framer Motion → CSS puro em landing pages.

### [ESTRATÉGICA] Bling OAuth: armadilhas conhecidas (2026-04-01) ⬆️ Promovida
**Lição consolidada:** Bling API v3 tem gotchas cumulativos:
1. "Conta inativada" na OAuth → verificar certificado digital PRIMEIRO
2. OAuth code expira em ~30s → auto-exchange obrigatório no callback
3. Refresh token Filial retornava 403 "empresa inativa" → causa real: falta de redirect_uri no token exchange. Corrigido em callback-server.js (2026-04-01)
4. Impostos no payload são IGNORADOS → tributação vem da Natureza de Operação
5. Contatos devem existir na conta Bling EMITENTE antes de criar NF
**Workflow:** `shared/fisco/skills/bling-nfe/SKILL.md`.

### [ESTRATÉGICA] Custo real Anthropic API: $120/mês com prompt caching ativo (2026-03-30)
**Lição:** Sempre usar dados reais do dashboard (usage.anthropic.com) pra análise de custos. Prompt caching está ativo e reduz custo em ~50%. Estimativas baseadas em "requests × preço tabela" inflam significativamente.

### [ESTRATÉGICA] Supabase REST API cap 1000 rows — SEMPRE paginar com .range() (2026-03-27)
**Lição:** SEMPRE usar `.range(start, end)` para paginação no Supabase. Nunca confiar em `.limit()` para volumes grandes. Supabase ignora `.limit()` acima de 1000 e retorna apenas 1000 rows silenciosamente.

### [ESTRATÉGICA] Cooldown de auth profile bloqueia TODOS os modelos simultaneamente (2026-03-27)
**Lição:** Rate limit da Anthropic não é por modelo, é por conta/profile. Um burst em um modelo derruba todos. Sistema de contingência (Haiku monitor) é essencial para detectar e alertar.

### [ESTRATÉGICA] React keys duplicadas causam bug fantasma em reordenação (2026-03-27)
**Lição:** Quando um sort/filter "funciona na primeira vez mas falha na segunda": verificar React keys duplicadas PRIMEIRO. Garantir que a chave de agregação na API seja a mesma usada como React key.

### [ESTRATÉGICA] Pedro consegue operar diretamente quando Kobe fica indisponível (2026-03-27)
**Lição:** O sistema precisa de resiliência — quando o Kobe trava, Pedro tem que poder operar. O Contingency Guard detecta e avisa, mas o fluxo de contingência (Pedro + Claude Code) é a rede de segurança real.

### [ESTRATÉGICA] Sync de custos deve puxar das 4 abas da planilha, não só ESTOQUE (2026-03-26)
**Lição:** Planilha tem SKUs distribuídos em 4 abas (ESTOQUE, MELI, SHOPEE, AMAZON). SEMPRE mapear todas. Prioridade: ESTOQUE > MELI > SHOPEE > AMAZON.

### [ESTRATÉGICA] Sessões perdidas por timeout/reset prejudicam session extractor (2026-03-26)
**Lição:** Quando há muitos resets/timeouts num dia produtivo, consolidação manual é obrigatória. O session extractor só captura sessões com conteúdo suficiente.

### [ESTRATÉGICA] Não disparar Builder sem briefing revisado pelo Pedro (2026-03-25)
**Lição:** Quando Pedro envia um briefing grande, ESPERAR que ele confirme que terminou antes de disparar. "Me manda pra revisar antes de disparar" = respeitar literalmente.

### [ESTRATÉGICA] Builder failures no 1º try = briefing incompleto (2026-03-25)
**Lição:** Quando o Builder falha no primeiro try, a causa raiz geralmente é briefing incompleto. Checklist pré-dispatch: validar que todos os campos do BRIEFING-TEMPLATE.md estão preenchidos.

### [ESTRATÉGICA] dmPolicy "open" no WhatsApp do OpenClaw = bomba (2026-03-25)
**Lição:** OpenClaw/Baileys = APENAS leitura passiva. Todo envio e leitura de histórico = Evolution API Cloudfy. NUNCA mais abrir dmPolicy. O módulo web-auto-reply dispara respostas automáticas quando dmPolicy está "open".

### [ESTRATÉGICA] Skills de design obrigatórias em briefings de frontend (2026-03-24)
**Lição:** Todo briefing de frontend DEVE usar templates/BRIEFING-TEMPLATE.md + 4 skills: lovable-quality, superdesign, frontend-design-ultimate, shadcn-ui.

### [ESTRATÉGICA] Spark Ads v1 ficou amador por briefing sem design system (2026-03-24)
**Lição:** Qualidade visual do output é diretamente proporcional à qualidade do briefing. Design system (globals.css + tailwind.config.ts com tokens) deve ser criado ANTES de qualquer componente.

### [ESTRATÉGICA] Auditar agentes novos comparando com Spark (padrão-ouro) (2026-03-29)
**Lição:** Usar Spark como referência (gold standard) para identificar gaps em novos agentes.

### [ESTRATÉGICA] BrasilAPI NCM NÃO inclui alíquotas de II/IPI (2026-03-30)
**Lição:** BrasilAPI = código + descrição. TIPI = IPI. TEC = II. Para alíquotas, SEMPRE usar fontes oficiais da Receita Federal. Nunca estimar por capítulo.

### [ESTRATÉGICA] WhatsApp duplicado por retry de LLM (2026-03-30)
**Solução:** Wrapper centralizado `scripts/send-whatsapp.py` com deduplicação por hash (SHA256). NUNCA chamar Evolution API via curl direto.

### [ESTRATÉGICA] Knowledge Files do Lovable como fonte de verdade (2026-03-30)
**Lição:** Lovable gera documentação de regras de negócio muito completa. Copiar pro workspace dos agentes como fonte de verdade.

### [ESTRATÉGICA] Instância dedicada na Evolution API por agente (2026-03-30)
**Lição:** Cada agente com WhatsApp próprio precisa de instância dedicada. Tokens de instância NÃO criam novas instâncias — precisa da Global API Key.

### [ESTRATÉGICA] Margem consolidada 13,7% — volume concentrado onde margem é pior (2026-03-21)
**Lição:** Margem média simples mascara o problema. Sempre ponderar por volume e plataforma. O grosso do faturamento GB está na Shopee onde as margens são as menores.

### [ESTRATÉGICA] Multi-agente funciona: Kobe coordena, Trader executa (2026-03-20)
**Lição:** Modelo Kobe (Opus, coordenação) → Agentes (Opus, execução) funciona bem. Pedro aprovou.

### [ESTRATÉGICA] Shopee março 2026 — reajuste massivo (2026-03-19)
**Lição:** Fim do teto R$100 comissão + taxa fixa até 550% maior. Precificação ficou mais complexa (5+ faixas). Taxa de transação (~2%) não aparece na planilha do Pedro.

### [ESTRATÉGICA] FULL ≠ Frete Grátis Universal (2026-03-18)
**Lição:** free_shipping:false + fulfillment = frete grátis apenas para Meli+. Classificar shipping como: universal / meli_plus / none.

### [ESTRATÉGICA] Planilha > Estimativas para Pricing (2026-03-18)
**Lição:** Sempre consultar planilha real do Drive antes de recomendar pricing. Estimativas baseadas só em % de comissão ignoram frete real, Ads, devoluções, caixa, embalagem.

### [ESTRATÉGICA] Credenciais no CLAUDE.md do Bidspark — risco de segurança (2026-03-17)
**Lição:** Arquivos de contexto de IA (CLAUDE.md, .cursorrules, etc.) não devem conter credenciais.

### [ESTRATÉGICA] Enforcement > Documentação (2026-03-17)
**Lição:** Estrutura no papel sem enforcement real é inútil. Gate de bloqueio > guideline. Cron automático > boa intenção.

### [ESTRATÉGICA] Bidspark: zero testes é o bloqueio real pra produção (2026-03-17)
**Lição:** Qualquer projeto que mexe com dinheiro real precisa de testes de regressão antes de produção.

### [ESTRATÉGICA] Ciclo de melhoria deve rodar ANTES de encerrar (2026-03-17)
**Lição:** O ciclo CAPTURA → PROCESSAMENTO → INCORPORAÇÃO → REGISTRO deve ser a ÚLTIMA coisa antes de encerrar. Gate de encerramento obrigatório.

### [ESTRATÉGICA] Consultar feedbacks antes de sugerir (2026-03-16)
**Lição:** Antes de fazer sugestões em qualquer domínio, consultar openclaw/agents/kobe/memory/feedback/ pra não repetir padrão já rejeitado.

### [ESTRATÉGICA] Emails do Pedro SEMPRE com assinatura HTML (2026-03-16)
**Lição:** Sempre enviar emails do pehpbroglio@gmail.com com --body-html e incluir a assinatura. Arquivo: `/root/.openclaw/.gmail-signature-pedro.html`.

### [ESTRATÉGICA] Não sugerir fechar sessão repetidamente (2026-03-16)
**Lição:** Pedro trabalha em blocos longos. Só sugerir encerrar sessão após 4+ horas seguidas.

---

## Lições Táticas (Expiram em 30 dias)

### [TÁTICA] Bootstrap: nunca declarar 100% completo quando arquivos esperados não existem (2026-04-28)
**Lição:** Em bootstrap pendente, validar o que foi de fato restaurado e tratar ausência real de nota do dia/arquivo de pendências como bloqueio explícito. Melhor reportar "quase completo" do que fingir contexto carregado.
**Expira:** 2026-05-28

### [TÁTICA] Google/gog: diagnosticar pelo fluxo real, não por caminho quebrado de keyring (2026-04-26)
**Lição:** Se um teste de autenticação Google falhar por caminho específico de keyring, validar também pelo comando real/ambiente atual antes de concluir que Sheets/Gmail/Calendar estão indisponíveis. Em 26/04, Sheets funcionava nas contas do agente e do Pedro apesar de um diagnóstico inicial ruim.
**Expira:** 2026-05-26

### [TÁTICA] N8N + Supabase REST: insert seguro exige apikey + Authorization Bearer (2026-04-26)
**Lição:** Para workflows N8N que inserem no Supabase via REST, enviar `apikey` e `Authorization: Bearer <service_role>`. Service role deve ficar em credential/env seguro do N8N/1Password, nunca hardcoded no JSON do workflow.
**Expira:** 2026-05-26

### [TÁTICA] Não inferir conteúdo de áudio falho nem inventar incidente/configuração (2026-04-25)
**Lição:** Se a transcrição de áudio falhar, ficar incompleta ou ambígua, NUNCA preencher lacunas com inferência e muito menos afirmar que um incidente/configuração já foi verificado ou corrigido sem validação real. Primeiro transcrever corretamente ou pedir clarificação.
**Expira:** 2026-05-25

### [TÁTICA] Mercado Livre: gold_special = Clássico 11%, gold_pro = Premium 16% (2026-04-07)
**Lição:** Em anúncios Budamix de ticket próximo de R$39,90, `gold_special` costuma ser a escolha certa. No PCM001, usar `gold_pro` queimaria cerca de R$2 por venda sem ganho proporcional.
**Expira:** 2026-05-07

### [TÁTICA] Amazon Listings: `unit_count` precisa ser objeto com `language_tag` (2026-04-07)
**Lição:** Na SP-API da Amazon, `unit_count` não aceita string simples. O formato validado foi: `{"value": 7.0, "type": {"value": "count", "language_tag": "pt_BR"}}`.
**Expira:** 2026-05-07

### [TÁTICA] Shopee categoria 101247: API só edita parte das especificações (2026-04-07)
**Lição:** Em `Placemats & Coasters` (101247), apenas 7 atributos ficam realmente editáveis via API. O restante precisa ser completado no Seller Center para o anúncio sair com diagnóstico qualificado.
**Expira:** 2026-05-07

### [TÁTICA] Amazon BR aceitou GTIN exemption para DRINK_COASTER Budamix (2026-04-07)
**Lição:** O product type `DRINK_COASTER` funcionou com `supplier_declared_has_product_identifier_exemption` ativo e zerou erros no cadastro do PCM001. Vale repetir esse padrão em produtos MDF equivalentes da Budamix.
**Expira:** 2026-05-07

### [TÁTICA] Shopee: nunca encostar em R$80,00 sem recalcular a taxa fixa (2026-04-07)
**Lição:** Na Shopee, a taxa fixa do anúncio pode saltar de R$4 para R$16 ao cruzar o degrau de R$80. Para kits de ticket médio, isso destrói margem rápido se o preço for definido no chute.
**Expira:** 2026-05-07

### [TÁTICA] Dados técnicos de catálogo só podem ser inferidos quando o risco é baixo (2026-04-04)
**Lição:** Em catálogos de atendimento, só inferir com segurança descrições curtas, sugestões de uso, diferenciais genéricos e cuidados amplos da categoria. Material exato, compatibilidades, dimensões, peso, embalagem específica e capacidade só entram como valor real se a fonte confirmar; caso contrário, usar [VERIFICAR].
**Expira:** 2026-05-04

### [TÁTICA] Shopee multi-store OAuth: servidor só gerencia 1 de 3 contas (2026-04-01)
**Lição:** Todo token OAuth com refresh automático precisa cobrir TODAS as contas. Token morto = relatório incompleto sem aviso.
**Expira:** 2026-05-01

### [TÁTICA] Amazon Request Review: janela de elegibilidade usa data de ENTREGA (2026-04-02)
**Lição:** A Amazon calcula a janela 5-30 dias pela data de entrega ao cliente, não pela data de compra.
**Expira:** 2026-05-02

### [TÁTICA] SP-API Solicitations: 403 "Unauthorized" pode ser endpoint errado, não permissão (2026-04-10)
**Lição:** Antes de concluir que faltou scope/role no app, validar o path exato da Solicitations API. O path correto que funcionou foi `productReviewAndSellerFeedback`; o uso de `productReview` gerou falso diagnóstico de permissão.
**Expira:** 2026-05-10

### [TÁTICA] Ponto Certo pós-migração VPS: problemas são de adoção, não de sistema (2026-04-01)
**Lição:** Na transição de sistema, checar primeiro se é adoção (falta de uso) antes de assumir bug técnico.
**Expira:** 2026-05-01

### [TÁTICA] SKU mapping cross-platform: resolver sku_child → sku_parent antes de agregar (2026-04-01)
**Expira:** 2026-05-01

### [TÁTICA] React key com índice causa unmount+remount ao reordenar (2026-04-01)
**Lição:** Key sem índice (${sku}-${platform}) permite React mover componente sem recriar.
**Expira:** 2026-05-01

### [TÁTICA] Timeout 300s nos scripts de sync (2026-04-01)
**Lição:** Todos os 6 scripts de sync (orders + inventory) precisam de timeout 300s. sync-shopee-prices.py adicionado ao crontab (:25/:55).
**Expira:** 2026-05-01

### [TÁTICA] Excedente de vendas sobre estoque transferido → fatura pela Matriz (2026-03-31)
**Lição:** CFOP 6102, ICMS 4%. Kits devem ser decompostos em unidades antes de cruzar com estoque.
**Expira:** 2026-04-30

### [TÁTICA] Bling NF-e: destinatário precisa de todos os campos preenchidos (2026-03-30)
**Lição:** API aceita criar NF sem dados completos, mas NF fica inválida para emissão. SEMPRE preencher nome, IE, tipoPessoa, endereço.
**Expira:** 2026-04-30

### [TÁTICA] 4 Builder jobs simultâneos estouram memória — máximo 2 (2026-03-30)
**Lição:** VPS tem 3.8GB RAM. Máximo 2 Builder jobs simultâneos. Disparar em lotes de 2.
**Expira:** 2026-04-30

### [TÁTICA] Tolerância desatualizada frontend vs backend (2026-03-30)
**Lição:** Ao migrar sistema, conferir constantes hardcoded no frontend que podem ter ficado defasadas.

### [TÁTICA] Shopee sync on_conflict: parâmetro condicional por tabela (2026-04-02)
**Contexto:** `sync-shopee-prices.py` falhava com HTTP 409/400 há 8 dias (desde 25/03). `supabase_upsert` sem `on_conflict` para `products` (409 em duplicatas), e com `on_conflict` errado para `price_history` (400 em tabela sem constraint).
**Lição:** `products` usa `on_conflict=platform,platform_item_id`. `price_history` NÃO usa on_conflict (tabela de log append-only). Tornar on_conflict parâmetro opcional na função de upsert genérica.
**Expira:** 2026-05-02

### [TÁTICA] Builder falha em bugs complexos de estado React + animação (2026-03-27)
**Lição:** Bugs que envolvem estado React complexo (TanStack Query cache + animações + sort) → resolver direto no Claude Code interativo.
**Expira:** 2026-04-27

### [TÁTICA] getBRTDayRange: converter UTC→BRT antes de calcular range do dia (2026-03-25)
**Lição:** Em qualquer cálculo de "range do dia" em BRT, PRIMEIRO converter a data atual para BRT.
**Expira:** 2026-04-25

### [TÁTICA] Next.js build falha silenciosamente com pouca RAM — usar NODE_OPTIONS (2026-03-25)
**Lição:** Sempre usar `NODE_OPTIONS="--max-old-space-size=2048"` antes de build no VPS.
**Expira:** 2026-04-25

### [TÁTICA] Bot do Kobe só lê grupos Telegram onde está adicionado (2026-03-25)
**Expira:** 2026-04-25

### [TÁTICA] Budamix Central: schema real ≠ nomes de colunas nas rotas da API (2026-03-25)
**Lição:** Validar nomes de colunas contra schema real. Builder gera nomes plausíveis mas incorretos.
**Expira:** 2026-04-25

### [TÁTICA] Supabase Edge Functions usam IPs variáveis da AWS (2026-03-25)
**Lição:** Para APIs que exigem IP whitelist (Shopee), migrar sync para VPS com IP fixo.
**Expira:** 2026-04-25

### [TÁTICA] Shopee API limita range de datas a 15 dias máximo (2026-03-25)
**Expira:** 2026-04-25

### [TÁTICA] Amazon SP-API rate limit brutal para backfill (2026-03-25)
**Lição:** getOrderItems muito restritivo. Backfill = processo longo em background. Sync incremental (1 dia) = viável a cada 30min.
**Expira:** 2026-04-25

### [TÁTICA] Builder job "failed" pode ter entregado — verificar RESULT.md (2026-03-24)
**Expira:** 2026-04-24

### [TÁTICA] Supabase CLI requer access token pessoal (sbp_) (2026-03-24)
**Expira:** 2026-04-24

### [TÁTICA] Traefik ocupa 80/443 — usar file provider, não Nginx (2026-03-24)
**Expira:** 2026-04-24

### [TÁTICA] Upseller ERP: CAPTCHA + SPA = automação inviável (2026-03-21)
**Expira:** 2026-04-21

### [TÁTICA] budamix-store Shopee: refresh_token pode expirar (2026-03-21)
**Expira:** 2026-04-21

### [TÁTICA] Hostinger bloqueia Let's Encrypt em domínios custom (2026-03-20)
**Expira:** 2026-04-20

### [TÁTICA] Shopee access_token expira em 4h (2026-03-20)
**Expira:** 2026-04-20

### [TÁTICA] Shopee extrato multi-conta: ~13 min para 3.300 pedidos (2026-03-20)
**Expira:** 2026-04-20

### [TÁTICA] Meta Ads: system user limitado por Business Manager (2026-03-19)
**Lição:** Usar Long-lived token (60 dias) com cron de renovação. Lembrete em 15/05.
**Expira:** 2026-04-19

### [TÁTICA] OAuth Google: app em Produção evita expiração 7 dias (2026-03-19)
**Expira:** 2026-04-19

### [TÁTICA] Shopee é SPA — scraping limitado (2026-03-19)
**Expira:** 2026-04-19

### [TÁTICA] Bright Data Premium Domains — propagação (2026-03-19)
**Expira:** 2026-04-19

### [TÁTICA] Bright Data + ML Scraping (2026-03-18)
**Lição:** URLs ML com `_Desde_49`, `_NoIndex_True` bloqueadas. Usar `?page=N`.
**Expira:** 2026-04-18

### [TÁTICA] ML Ads: seção 5 do marketplace-report funciona com dados reais (2026-03-17)
**Expira:** 2026-04-17

### [TÁTICA] Bidspark: Amazon Ads ainda em sandbox (2026-03-17)
**Expira:** 2026-04-17

### [TÁTICA] ML API: MLB IDs ≠ seller SKUs, mapear via attributes (2026-03-26)
**Expira:** 2026-04-26

### [TÁTICA] Gateway bloqueia heredocs grandes como obfuscação — usar Write + scripts curtos (2026-04-06)
**Contexto:** Na coleta de links dos marketplaces para a base da Ana, duas execuções aprovadas expiraram com `approval-timeout (obfuscation-detected)` porque o comando tentava criar scripts longos via heredoc.
**Lição:** Quando precisar rodar automação via gateway, criar arquivos com `Write`/`Edit` e quebrar em scripts curtos por etapa/marketplace. Evitar `cat <<'PY'` e blocos longos inline.
**Expira:** 2026-05-06

### [TÁTICA] Cruzamento de links do ML: listar não casados com motivo acelera revisão manual (2026-04-06)
**Contexto:** A base da Ana tinha 61 produtos e o ML só cruzou parcialmente porque vários anúncios ativos vieram sem `seller_custom_field` ou com títulos ambíguos.
**Lição:** Depois do match automático, gerar lista de `ML_ID | título | SKU | motivo` dos não cruzados. Isso permite Pedro confirmar manualmente em minutos e destrava atualização da planilha sem insistir em fuzzy matching inseguro.
**Expira:** 2026-05-06

### [TÁTICA] Amazon catálogo por SKU pode falhar mesmo com listing ativo; manter fallback por keyword (2026-04-06)
**Contexto:** Na base Ana, a tentativa de recuperar links Amazon por extratos não trouxe ASIN utilizável por SKU para os 61 produtos.
**Lição:** Para catálogo Amazon, tentar primeiro `identifiersType=SKU` com sellerId. Se não resolver, cair para busca por keyword/SKU e tratar o restante como cruzamento manual, em vez de assumir ausência de listing cedo demais.
**Expira:** 2026-05-06

---


### [TÁTICA] Supabase/N8N: validar keys REST reais antes de assumir que a credencial serve (2026-04-26)
**Lição:** No Budamix Ecommerce, as anon/service role keys salvas no 1Password retornaram 401 via REST, enquanto a conexão direta PostgreSQL funcionou. Antes de montar workflow N8N ou diagnóstico de RLS, testar `apikey` + `Authorization` contra endpoint real do Supabase. Se REST falhar, corrigir/rotacionar as keys no 1Password antes de automatizar.
**Expira:** 2026-05-26

### [TÁTICA] Deploy feito com código não pushado cria dívida invisível (2026-04-26)
**Lição:** No SEO técnico do Blog Budamix, o deploy Vercel foi validado, mas `git push origin main` retornou HTTP 403 e o repo local ficou ahead. Deploy em produção não substitui commit/push no repo principal; sempre validar `git status` e upstream limpo antes de encerrar.
**Expira:** 2026-05-26



### [TÁTICA] N8N Cloudfy: Code node não tem `fetch`; webhooks encadeados pedem parse tolerante (2026-04-27)
**Lição:** No N8N Cloudfy, o Code node não expõe `fetch` global, e workflows chamados por webhook podem responder `200` com corpo vazio/timeout mesmo concluindo o trabalho. Para orquestrar WF2/WF3, usar helper HTTP do próprio N8N ou HTTP Request com resposta tratada como texto, e validar o sucesso pelo estado final no banco/workflow — não só pelo corpo JSON da chamada.
**Expira:** 2026-05-27


### [TÁTICA] N8N/WF2: validador rígido demais vira loading infinito no Admin (2026-04-27)
**Lição:** Validações de brand/DNA em workflow de geração devem corrigir automaticamente pequenos desvios seguros quando possível (ex.: completar “no text/no logos”, aceitar acento verde/teal discreto sem exigir hex fixo). Só devem falhar em violação crítica real. Validador rígido demais parece bug de frontend e deixa artigo preso em `gerando`.
**Expira:** 2026-05-27

### [TÁTICA] Admin async: criar rascunho imediatamente e rodar orquestrador em background (2026-04-27)
**Lição:** Em fluxo longo N8N, não prender a UI em loading global aguardando webhook terminar. Criar o registro `gerando`, mover o admin para Rascunhos imediatamente, limpar loading da pauta clicada e acompanhar por polling silencioso.
**Expira:** 2026-05-27

### [TÁTICA] Feedback UX: modal/card separado ≠ expandir inline; ícones discretos ≠ CTAs textuais (2026-04-27)
**Lição:** Quando Pedro pedir “abrir em card/modal” ou “discreto”, interpretar literalmente. No Admin Blog, expandir texto dentro da lateral e botões textuais grandes foram corrigidos para modal separado e ícones discretos.
**Expira:** 2026-05-27

### [TÁTICA] Blog público deve usar tokens do design system, não hex/fontFamily hardcoded (2026-04-27)
**Lição:** Componentes públicos do Blog Budamix devem usar tokens/classes do design system (`bg-background`, `text-foreground`, `font-display`, `font-body`, `primary`, `accent`, etc.). Hex hardcoded e `style fontFamily` criam drift visual com o site.
**Expira:** 2026-05-27

## Auditoria de Qualidade — Consolidação Profunda 2026-04-04

### Duplicatas removidas nesta consolidação:
- "Amazon SP-API: nextToken fica em payload" (2026-03-26) — subsumed by "Amazon SP-API: armadilhas recorrentes" strategic item 1
- "Amazon SP-API não retorna OrderTotal para pedidos Pending" (2026-03-27) — subsumed by strategic item 2
- "Mock data como placeholder mascara problemas reais" (2026-03-26) — subsumed by "Mock data como fallback = bomba silenciosa" strategic
- "Bling API ignora impostos" (2026-03-31) — subsumed by "Bling OAuth: armadilhas" item 4
- "Contatos dos destinatários Bling" (2026-03-31) — subsumed by "Bling OAuth: armadilhas" item 5
- "Bug refresh token Filial" (2026-03-31 + 2026-04-01) — subsumed by "Bling OAuth: armadilhas" item 3
- "Amazon unit_price" (2026-04-01 sessão) — duplicate of top-level strategic entry
- "Queries Supabase sem .range()" (2026-04-01 sessão) — duplicate of "Supabase REST API cap 1000 rows"

### Lição adicionada:
- "Shopee sync on_conflict" (2026-04-02) — padrão identificado na sessão Budamix Central mas não capturado pela consolidação diária
- "Dados técnicos de catálogo só podem ser inferidos quando o risco é baixo" (2026-04-04)

### Observações:
- 2 lições wkhtmltopdf marcadas OBSOLETA (sistema migrou para HTML)
- 1 lição Amazon Ads endpoint NA incorporada na lição consolidada de armadilhas
- Próxima expiração natural: 2026-04-17 (Bidspark sandbox e seção 5 de ML Ads).

_Consolidação Profunda executada em 2026-04-04 08:19 BRT._

### [TÁTICA] Vercel token do Budamix pode usar prefixo `vcp_`, não só `vercel_` (2026-04-28)
**Lição:** Ao extrair token da Vercel do 1Password, aceitar os formatos `vcp_...` (novo) e `vercel_...` (legado). Regex limitada a `vercel_` gera falso diagnóstico de token inválido/incompleto mesmo com credencial válida em `notesPlain`.
**Expira:** 2026-05-28

### [TÁTICA] Blog Budamix: status editorial só libera após validar texto + slots obrigatórios no banco (2026-04-28)
**Lição:** No fluxo do Blog Budamix, `em_edicao`/rascunho não pode depender só do término aparente do workflow. Validar no Supabase se `cover`, `support_1`, `support_2` e `pinterest_1` têm `image_url` e status `generated`; caso contrário, manter `gerando` ou marcar erro.
**Expira:** 2026-05-28

### [ESTRATÉGICA] Geração longa não pode depender de resposta HTTP síncrona (2026-04-28)
**Contexto:** Admin Blog marcou erro falso porque o webhook/N8N perdeu ou estourou resposta enquanto o backend continuou processando e concluiu o artigo no Supabase.
**Lição:** Para processos longos, o Admin deve criar job/receber ACK rápido e acompanhar estado persistido no banco. Sucesso/erro vem de `generation_status`/Supabase, não de resposta HTTP final.

### [ESTRATÉGICA] Estado persistido no Supabase é fonte de verdade do Blog Budamix (2026-04-28)
**Contexto:** Artigos podiam parecer prontos no frontend antes de todas as imagens obrigatórias fecharem, ou parecer falhos mesmo já completos.
**Lição:** Blog só libera `em_edicao` depois de texto + slots `cover`, `support_1`, `support_2`, `pinterest_1` com URL e `image_status=generated`. Admin deve reconciliar UI com banco antes de exibir erro final.

### [TÁTICA] Vercel CLI preview do Budamix precisa envs públicas explícitas (2026-04-28; expira 2026-05-28)
**Contexto:** Preview do Social Studio retornava 200 mas ficava tela branca porque o bundle foi buildado sem `VITE_SUPABASE_URL`/`VITE_SUPABASE_PUBLISHABLE_KEY`.
**Lição:** Ao gerar preview pela CLI, passar envs públicas de build extraídas do 1Password ou configurar Preview Environment no dashboard Vercel. Smoke test precisa verificar bundle inicial, não só HTTP 200.

### [ESTRATÉGICA] Supabase remoto com histórico de migrations não marcado: não usar db push (2026-04-28)
**Contexto:** Social Studio precisava migration remota, mas `supabase db push` empurraria várias migrations antigas porque o histórico remoto não estava marcado.
**Lição:** Em projeto Supabase com histórico desalinhado, aplicar migration específica de forma controlada e fazer backup/smoke REST. Nunca rodar `db push` amplo no impulso.

### [ESTRATÉGICA] Secrets de N8N não podem viver hardcoded em Code nodes (2026-04-28)
**Contexto:** WF4 do Blog tinha service role hardcoded em Code nodes.
**Lição:** Migrar service role/API keys para credentials/env do N8N e referenciar em runtime. Segredo em workflow exportável vira risco operacional e de auditoria.

### [TÁTICA] Social Studio: fluxo de criação precisa ser wizard guiado, não dashboard técnico (2026-04-29)
**Lição:** Para criação de posts/carrosséis, não empilhar pipeline, editor, slides, render e preview na mesma tela. A UX correta é step-by-step em tela cheia, com uma decisão principal por etapa, complexidade técnica escondida e progressão guiada por dados reais do conteúdo.
**Expira:** 2026-05-29

---
title: "Budamix Meta Ads — Paid Social"
created: 2026-06-06
modified: 2026-06-13
type: project
status: active
path: "Meta Ads Manager — conta Budamix (1140258596603533)"
tags:
  - project
  - marketing
  - paid-social
  - meta-ads
  - budamix
---

# Budamix Meta Ads — Paid Social

> Primeira investida de tráfego pago no Meta (Facebook/Instagram) pro e-commerce budamix.com.br.
> Estrutura de 3 campanhas focada no HERO IMB501 (Conjunto 5 Potes Redondos de Vidro).
> **Status 08/06/2026:** Campanha 1 (Cold ASC) ATIVA com R$20/dia — vídeo v2 safezone + copy v4 multiuso, público mulheres BR. Campanhas 2 e 3 ainda PAUSED aguardando vídeos 2 e 3 do Pedro.

## Coordenadas Meta

| Item | Valor |
|---|---|
| **Business Manager** | Budamix (`836285430695962`) |
| **Conta de Anúncios** | Budamix - Conta de anúncios (`1140258596603533`) |
| **Pixel + CAPI** | Budamix - Pixel da Meta (`460889899401645`) |
| **Catálogo** | Budamix Catálogo (`1973158136897277`) — 23 produtos via feed |
| **Página** | Budamix (`106066888942641`) |
| **Feed XML** | https://budamix.com.br/feeds/meta-catalog.xml |
| **Moeda** | BRL |

## Estratégia consolidada (versão 2026)

3 campanhas com jobs específicos, alinhadas à pesquisa de paid social 2026 (Andromeda, fim dos interesses detalhados, Advantage+ como padrão).

```
CAMPANHA 1 — ASC (Advantage+ Sales) — 65% verba (R$37/dia, CBO)
  → Motor de aquisição fria
  → 1 ad set: BR mulheres 25-55, Advantage+ Audience ON
  → Otimização: ATC inicialmente, migra pra Purchase quando volume sustentar
  → Criativos: vídeos UGC + demo (até 15 ativos quando maduro)

CAMPANHA 2 — Teste de Criativos (ABO Manual) — 20% verba (R$11/dia)
  → Laboratório de criativos
  → 1 ad set 3:2:2: 3 vídeos × 2 títulos × 2 textos
  → Vencedores graduam pra ASC semanalmente

CAMPANHA 3 — Retargeting WCA (ABO) — 15% verba (R$9/dia)
  → Recupera quem visitou mas não comprou
  → 1 ad set: ViewContent 14d EXCLUI Purchase 30d (WCAs pendentes — pixel novo)
  → Otimização: Purchase direto
  → Migrar pra DPA (Dynamic Product Ads) no mês 3+ quando catálogo tiver maturidade
```

## IDs das entidades criadas

| Campanha | Campaign ID | Ad Set ID | Budget atual | Status (08/06) |
|---|---|---|---|---|
| 1 — `2026-06-06_Cold_ASC_IMB501_25-55` | `120248423500010402` | `120248423502930402` (Cold_BR_25-55_IMB501_ATC) | CBO **R$20/dia** | **ACTIVE** |
| 2 — `2026-06-06_Cold_TEST_IMB501_25-55` | `120248423500320402` | `120248423503880402` (Cold_Test_3x2x2_IMB501_ATC) | ABO R$11/dia | PAUSED |
| 3 — `2026-06-06_Warm_DPA_IMB501_Retargeting` | `120248423500930402` | `120248423510550402` (Warm_Retargeting_VC14_NoPurchase30_PURCHASE) | ABO R$9/dia | PAUSED |

### Ads ativos (Campanha 1)

| Ad ID | Creative ID atual | Vídeo ID | Status |
|---|---|---|---|
| `120248522531400402` | `4446773825645879` (v4 copy multiuso) | `1765886834776880` (v2 safezone overlays) | ACTIVE |

Histórico de creatives no Ad (todos arquivados, não deletados):
- v1 `1521588869499661` — copy original com "borossilicato" + video v1 (overlays fora da safezone)
- v2 `868261775779008` — copy original com "borossilicato" + video v2 (safezone)
- v3 `1446563367484264` — copy sem borossilicato (linha "tampa que veda") + video v2
- v4 `4446773825645879` — copy sem borossilicato (linha "Multiuso") + video v2 → **ATIVO**

Thumbnail hash (reusada em todas as versões — frame 0.5s do vídeo): `815ac9c52a74b340aff9f398faf33e51`

## HERO Product — IMB501

**Conjunto 5 Potes Redondos de Vidro Budamix** (`/produto/conjunto-5-potes-redondos-vidro-budamix`)

- 3 variantes (cor da tampa): IMB501C_T (cinza R$24,90), IMB501V_T (vermelha R$24,90), IMB501P_T (preta R$29,90)
- Combos: KIT2 (10 peças R$47,90), KIT3 (15 peças R$67,90)
- Estoque: 21.707 unidades (ranking #1 de receita 90d com R$289.186 — 96% das vendas das 3 linhas de vidro)
- 5,0⭐ / 18 reviews

Critério de escolha: maior receita acumulada + estoque infinito + reviews ótimas. Decisão de focar APENAS no IMB501 nos primeiros 1-2 meses (não pulverizar pras outras 2 linhas — retangulares/quadrados vendem 20x menos).

## URL de destino do anúncio (com UTM)

```
https://budamix.com.br/produto/conjunto-5-potes-redondos-vidro-budamix?utm_source=meta&utm_medium=paid_social&utm_campaign=2026-06-06_Cold_ASC_IMB501&utm_content=video-v2-15s&utm_term=hero-fria
```

Para retargeting (Campanha 3): trocar `utm_campaign=2026-06-06_Warm_DPA_IMB501` + `utm_term=retargeting-warm`.

## Criativos

| Vídeo | Status | Localização |
|---|---|---|
| 1 v2 safezone — Demonstração produto (15s) | ✅ ATIVO no anúncio | `~/Downloads/Videos IA Potes Hermeticos Budamix/budamix-imb501-meta-ads-FINAL-v2-safezone.mp4` |
| 2 — UGC Testemunho (~18s) | ⏳ Pedro produzindo (tentando IA primeiro, fallback gravar com celular) | — |
| 3 — Antes/Depois (12-15s) | ⏳ Pedro produzindo | — |

**Vídeo 1 v2 specs:** 1080×1920, 15s, 7.9MB, Antonio Bold + paleta oficial Budamix (Deep Teal/Teal/Burnt Terracotta/Lima Sutil/Ivory Mist), trilha sintética 110 BPM. Overlays nos tempos:
- 0-3s: hook "DESPENSA BAGUNÇADA?" (centro)
- 3-9s: sticker "CONJUNTO 5 POTES DE VIDRO" — **subiu de y=1590 → y=1100 (safezone 1:1)**
- 9-12s: preço "R$24,90 / ECONOMIZE 37%" (centro)
- 12-15s: CTA "FRETE GRÁTIS + EM PEDIDOS ACIMA DE R$199 + BUDAMIX.COM.BR" — **subiu de y=1370 → y=900 (safezone 1:1)**

Pipeline de build em `/tmp/imb501_edit/` (build_overlays.py + segments/ + output/final_v2.mp4). Não é versionado — efêmero por sessão. Source video em `/tmp/imb501_edit/source.mp4`.

## Copy atualizada (creative v4 ativo)

```
Despensa bagunçada nunca mais. ✨

Conjunto com 5 potes de vidro em tamanhos diferentes — perfeito pra grãos, café, açúcar, farinha e tudo que você quiser organizar.

✅ Multiuso no dia a dia — guardar, servir, organizar tudo
⭐ 5,0 / 18 avaliações de clientes Budamix
🚚 Frete grátis acima de R$199

Garanta o seu agora 👇
```

- **Headline:** "Conjunto 5 Potes de Vidro"
- **Descrição:** "R$24,90 — Frete grátis acima de R$199"
- **CTA:** SHOP_NOW
- **UTMs:** `utm_source=meta&utm_medium=paid_social&utm_campaign=2026-06-06_Cold_ASC_IMB501&utm_content=video-v2-15s-safezone&utm_term=hero-fria`

⚠️ Importante: NÃO usar "borossilicato" (o vidro não é) nem claim de "freezer/micro-ondas" (depende de borossilicato pra ser claim seguro).

## Orçamento e expectativa de resultados

Pedro reduziu Campanha 1 de R$37 → R$20/dia logo após ativação em 08/06/2026 (antes da fase de aprendizado começar — sem reset). Total planejado abaixo do original mas com mesma estrutura.

| Item | Valor |
|---|---|
| **Budget Campanha 1 (ativa)** | R$20/dia = R$600/mês |
| **Budget Campanhas 2+3 (planejado quando ativar)** | R$11 + R$9 = R$20/dia = R$600/mês |
| **Total quando 3 ativas** | R$40/dia = R$1.200/mês |
| **Otimização** | Campanhas 1+2 = AddToCart, Campanha 3 = Purchase |
| **Mês 1** | Sai do aprendizado em ~10-12 dias com R$20/dia + ATC (~R$2 CPA → 50 ATCs/sem) |
| **Mês 2** | Transição pra Purchase quando volume sustentar |
| **Mês 3+** | Escala vertical +20% a cada 3-4 dias quando ROAS ≥ break-even |

## Pré-requisitos técnicos JÁ resolvidos

- ✅ Pixel client-side instalado e disparando (`VITE_META_PIXEL_ID=460889899401645` em Vercel)
- ✅ CAPI server-side ativo (`/api/meta-capi` + `META_CAPI_ACCESS_TOKEN` em Vercel)
- ✅ Dedup via event_id (`crypto.randomUUID()` + `eventID` no fbq + mesmo ID no POST do CAPI)
- ✅ Email/telefone hasheados no Purchase (server-side SHA-256)
- ✅ Domínio `budamix.com.br` verificado no BM
- ✅ Pixel conectado à Conta de Anúncios + Catálogo
- ✅ Feed XML com 23 produtos válidos, `<g:id>` = variant_id (alinhado com pixel `content_ids`)

## Spark integrado (08/06/2026 noite)

Spark agora monitora Camp 1 com infraestrutura completa:

- **Token Meta permanente** (System User, NEVER expira) em 1P vault OpenClaw, item `hxvgwjrdluw4yblo4lbktatoyy`, campo `notesPlain`. 42 scopes incluindo `ads_management`, `instagram_basic`, `instagram_manage_insights`, `catalog_management`.
- **Schema Supabase dedicado:** `meta.*` no projeto SPARK ADS (`wzhmrpskiscassbixurr`). 3 tabelas: `actions_log`, `recommendations`, `daily_pulses`. Exposto via PostgREST. Regra: schemas separados por plataforma (Amazon ficará em `amazon.*`, ML em `ml.*`).
- **Daily pulse 10:20 BRT:** cron `20 13 * * *` UTC. Script `/var/www/mission-control/scripts/spark-meta-daily-pulse.py`. Coleta insights last 24h + 7d Camp 1, calcula KPIs, detecta anomalias básicas, insere em `meta.daily_pulses`, posta no Telegram thread 9 (Marketing) do grupo Tobias Hub. Alertas críticos vão pro thread 8 (Urgente).
- **Guardrail nos scripts Meta Ads:** `meta-ads-report.py`, `meta-ads-create.py`, `meta-ads-rules.py` refusam executar sem `META_AD_ACCOUNT` explícito (whitelist apenas Budamix). Mitigação contra operação na conta legacy GB Distribuição.
- **Skills refatoradas:** SKILL.md global + Spark agora Budamix-first com Strategy 2026 + regras invioláveis (sem borossilicato, sem claim freezer/micro-ondas, paleta oficial, safezone 1:1, freeze Camp 1 até 22/06).
- **Spark continua L1 Observer.** Janela pra promover ajustes pequenos auto-execução: pós-22/06 (saída fase aprendizado), após 1-2 ciclos sem erro. Estruturais sempre via aprovação Pedro no tópico Marketing.

## Próximos passos

1. **Pedro entrega vídeos 2 e 3** (UGC + Antes/Depois). Quando chegarem: Claude faz upload via API + cria 3 ads na Camp 2 (3:2:2) e 1 ad na Camp 3, ativa tudo.
2. **Criar 2 Custom Audiences (WCA)** pra Campanha 3 (ViewContent 14d + Purchase 30d). Tool MCP estava bloqueada na sessão de 06/06; tentar de novo via API com token novo quando Pedro mandar vídeos. Se ainda bloquear, Pedro cria manual.
3. **NÃO TOCAR na Campanha 1 nos próximos 7-14 dias** — qualquer mudança >20% em budget/público/criativo reseta fase de aprendizado.

## Decisões estruturais tomadas

- Estratégia D atualizada pra versão 2026 (3 campanhas em vez de 2)
- HERO único: IMB501 (não pulverizar entre redondos/retangulares/quadrados)
- Retargeting começa WCA-based + vídeo, NÃO DPA (migrar mês 3+)
- Sem ferramentas pagas de pesquisa de interesses (AdTargeting etc) — interesses do nicho cobertos via Advantage+ Audience signals
- **08/06:** Campanha 1 ativada com R$20/dia (reduzido de R$37) — Pedro pediu cautela inicial. Margem pra escalar conforme performance.
- **08/06:** Público restrito a mulheres (genders=[2]) na Campanha 1. Idade ficou 18-65 por LIMITAÇÃO TÉCNICA — Advantage+ Audience exige age_max ≥ 65; restringir 25-55 requereria desligar Advantage+ Audience (não vale o trade-off em 2026).
- **09/06:** **Audience Network EXCLUÍDO** da Campanha 1 — `publisher_platforms: ["facebook", "instagram"]`. Primeira análise revelou que 73% do budget (R$29 de R$40 em 30h) foi pro AN (Rewarded Video + Classic) com CTR inflado 37-54% e ATCs falsos. 65+ feminino consumiu 43% do budget porque AN entregava CTR alto. Quebrou o freeze deliberadamente pra parar de queimar dinheiro em cliques falsos. **Nova janela freeze: até ~23/06**. Pra Camps 2 e 3 já criar sem AN desde o setup.

## Audiências de outras contas — descartadas como audience signal

Os 2 lookalikes da conta GB Distribuição (`323534883953033`) que tínhamos como plano B estão **INACTIVE** (operation_status_code 433, desde 2024) — não reativáveis:
- `120220400359220456` — Semelhante (BR, 1%) Visitantes Site
- `120219003397950456` — Semelhante (BR, 3%) Engajados Página

Pra pixel novo (sem volume), só Advantage+ Audience até maturar (~30-50 vendas Purchase/mês).

## Plano futuro de expansão (mês 3+)

Quando IMB501 atingir ROAS ≥ 2 consistente:
1. Replicar estrutura pros 3 kits retangulares (KIT DESPENSA + KIT ESSENCIAL + KIT COMPLETO)
2. Mês 5+: kits quadrados (KIT SOLO + KIT FAMÍLIA + KIT PRÁTICO)
3. Migrar Campanha 3 de WCA pra DPA (Dynamic Product Ads com catálogo completo)
4. Considerar customer list de compradores marketplace (Pedro vai conseguir lista via empresa parceira semana que vem)

## Campanha de Seguidores — TOFU Reels (criada 13/06/2026)

Nova frente de **topo de funil**: promover os reels orgânicos do @budamix.br pra ganhar **seguidores + engajamento** (decisão do Pedro: seguidores primeiro; vendas seguem via Camp 1 ASC + halo/retargeting). Roda na MESMA conta da Camp 1 de vendas. **ATIVADA 14/06** (campanha+conjunto ACTIVE; 3 anúncios em revisão IN_PROCESS). Construída via Graph API com o token Budamix (1P item `hxvgwjrdluw4yblo4lbktatoyy`), nomenclatura nova (ver [[business/marketing/nomenclatura-ads]]).

- **Campanha** (`120248910294770402`): `BDMX | TRAF | TOPO | seguidores-reels | 2026-06`
  - Objetivo OUTCOME_TRAFFIC → otimização **VISIT_INSTAGRAM_PROFILE** (visitas ao perfil = seguidores). CBO **R$40/dia**.
- **Conjunto** (`120248910295500402`): `FRIO | amplo-18-65 | SP-MG-RJ-PR-RS-SC | IG | VISITA-PERFIL`
  - Geo: SP(460) MG(449) RJ(454) PR(452) RS(456) SC(459) · idade 18-65 · `publisher_platforms:["instagram"]` (AN excluído por padrão).
- **Instagram:** @budamix.br (`17841466202361418`) — **2.934 seguidores em 13/06** (baseline pra medir crescimento).
- **Anúncios (4 criativos/posts):**
  - `120248910298190402` — `REEL | pote-vidro | chega-inteiro` — post IG promovido direto (mantém prova social) — IG media `18111478753782026`
  - `120248912033870402` — `REEL | enviado-af9a` — vídeo enviado — FB video `2541114302997076` (arquivo `copy_AF9A1841`)
  - `120248912034610402` — `REEL | enviado-7efc` — vídeo enviado — FB video `2129319420977614` (arquivo `copy_7EFCC766`)
  - `120248963210260402` — `REEL | dia-de-jogo-potes | post-existente` — post IG promovido direto (mantém prova social) — IG media `18102514687864184` / post `https://www.instagram.com/p/DZiGXdNIP-1/`

**Notas técnicas:**
- 2 reels ("o antes" e "40 min na cozinha") foram **barrados como post existente** (erro 1815279 — música licenciada). Resolvido subindo o arquivo `.MOV` direto via `/advideos`. Custo: perdem curtidas/comentários do post original; **risco de reprovação na revisão Meta por música ao ativar**. Confirmar no preview qual arquivo (af9a/7efc) é qual reel e renomear o slug.
- Receita correta pra promover reel orgânico: criativo **minimal** `{name, source_instagram_media_id}` — incluir `object_story_spec` dispara exigência de `link`. O `meta-ads-create.py` do Spark **não cobre** esse caso (só image/link) → candidato a upgrade.
- 14/06 14:18 BRT: Pedro pediu adicionar interesses também no anúncio com legenda herdada do post original; como interesses são configurados no conjunto, o ad set `120248910295500402` recebeu sinais de interesse inicialmente amplos. Pedro corrigiu a premissa: Budamix vende apenas potes de vidro para armazenamento de alimentos, majoritariamente usados na cozinha; portanto, **não faz sentido usar Decoração/Receitas como sinais principais**. Ajuste aplicado às 14:22 BRT: remover sinais genéricos e priorizar armazenamento/conservação/cozinha. Às 14:27 BRT, Pedro pediu usar **Potes Herméticos**; o Meta não oferece esse interesse em português, então foi aplicado o equivalente disponível **Food storage container**. Targeting final preserva estados SP-MG-RJ-PR-RS-SC, idade 18-65, Instagram-only e Advantage+ Audience; interesses finais: **Food storage container, Conservação de alimentos, Tupperware e Cozinha**. Evitar daqui pra frente sinais genéricos de conteúdo/decor; priorizar armazenamento, conservação e organização de cozinha.
- 14/06 14:35 BRT: Pedro enviou prints das legendas originais dos 2 reels enviados sem legenda. Criativos recriados e aplicados: `REEL | enviado-af9a` recebeu legenda da sopa/freezer (`creative_id` novo `1662388848355938`); `REEL | enviado-7efc` recebeu legenda do antes/depois geladeira (`creative_id` novo `1044005144804780`). Verificação pós-update confirmou que os 3 anúncios da campanha têm legenda. Os 2 anúncios atualizados entraram em `IN_PROCESS` por revisão automática do Meta após troca de criativo.
- 14/06 15:41 BRT: Pedro avaliou que Advantage+ Audience estava desperdiçando orçamento e pediu remover dos 3 anúncios. Como Advantage+ Audience é configuração do conjunto, foi desligado no ad set `120248910295500402` (`targeting_automation.advantage_audience=0`), afetando todos os anúncios do conjunto. Estados, Instagram-only, idade 18-65 e interesses foram preservados. A Meta exigiu remover o campo técnico `age_range` ao desligar Advantage+; `age_min`/`age_max` ficaram mantidos. Após mudança, campanha segue `ACTIVE`, conjunto/anúncios entraram em `IN_PROCESS` temporário por revisão automática e depois voltaram a `ACTIVE`.
- 14/06 17:09 BRT: Pedro pediu adicionar o post `https://www.instagram.com/p/DZiGXdNIP-1/` à campanha de seguidores. Post resolvido via IG media `18102514687864184` (imagem feed, legenda “Torcida organizada começa pela cozinha…”). Criado creative `1729581294724038` e anúncio `120248963210260402` no mesmo ad set `120248910295500402`, status configurado `ACTIVE`, effective `IN_PROCESS` por revisão automática. A campanha passou a ter 4 anúncios; os outros 3 estavam `ACTIVE` na validação pós-criação.
- 14/06 17:13 BRT: Pedro autorizou subir orçamento da campanha de seguidores de R$40/dia para **R$50/dia**. Alteração aplicada no nível campanha (`daily_budget=5000`), mantendo CBO, mesmo conjunto e mesmos 4 anúncios.
- "Vendas via Insta" medidas por **cupom INSTA** (marketplaces + site) + UTM na bio. Pixel ainda com **0 Purchase em 28d** → não otimizar pra venda ainda.

## Acompanhamento / Dashboard (criado 14/06/2026)

Stack de monitoramento de Meta Ads, em 3 camadas:

1. **Daily pulse generalizado** — `mission-control/scripts/spark-meta-daily-pulse.py` agora cobre **todas as campanhas** (antes só Camp 1 hardcoded): totais da conta (today+7d) + breakdown por campanha + anomalias por campanha. Grava em `meta.daily_pulses` (Supabase Spark ADS) e posta no Telegram thread Marketing. Flags novas: `--dry` (não grava/não envia) e `--no-telegram`. Cron 10:20 BRT mantido. Backup `.bak-20260614`.
2. **RLS habilitado** nas 3 tabelas `meta.*` (`daily_pulses`, `recommendations`, `actions_log`) — antes expostas via anon. Pulse migrado pra **service_role** (`SPARK_ADS_SERVICE_ROLE_KEY` no env do mission-control, do 1P "Supabase - Spark Ads"); service_role ignora RLS, anon trancado. Upsert idempotente via `on_conflict=account_id,pulse_date`.
3. **Módulo "Meta Ads" no GB HUB** (`budamix-central`, Next.js) — rota `(dashboard)/meta-ads` + API `api/meta-ads`. Consulta a **Meta Marketing API ao vivo** (token Budamix no `.env` do app): **seletor de conta de anúncios** (data-driven via `/me/adaccounts`), seletor de período (hoje/7/14/30/90d/máx), multi-seleção de campanhas, KPI cards (spend, impressões, alcance, CTR, CPM, CPC, freq, ATC, compras, ROAS), gráfico de tendência diária (recharts) e tabela por campanha. Item "Ads" da sidebar habilitado → "Meta Ads". Build validado.
   - ⚠️ **Seletor de conta** lista só o que o token enxerga. O System User Budamix (`Fat_User_CRM`, `122135358765059107`) hoje só acessa a conta Budamix → dropdown com 1 conta. Pra outras aparecerem: liberar acesso do System User às ad accounts em **Business Settings → Usuários do Sistema → Adicionar Ativos → Contas de Anúncio** (contas da GB Distribuição exigem compartilhamento cross-business). O token legacy KOBE.OPENCLAW (que via as contas da GB) **expirou em 18/05** — renovar se quiser. Liberou acesso → as contas surgem sozinhas, sem código novo.

## Notas relacionadas

- [[business/marketing/nomenclatura-ads]] — padrão de nomes de campanhas/conjuntos/anúncios
- [[knowledge/concepts/facebook-page-api-budamix]] — integração FB Page API (token + scopes)
- [[memory/context/decisoes/2026-06]] — decisões de junho
- [[business/marketing/marca]] — paleta oficial Budamix
- [[projects/budamix-ecommerce]] — site de destino

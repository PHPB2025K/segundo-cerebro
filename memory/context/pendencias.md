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

- [06/04] VPS disco 63.4% usado de 47GB — monitorar crescimento. Logs de memory, backups e Chrome cache podem encher. Limpeza necessária em breve.
- [06/04] VPS memória 80% + swap 52% — processo zombie detectado. Requer investigação.
- [06/04] Aguardando **Pedro** publicar Canggu no Lovable (destacques visuais campos IA, envio WhatsApp corrigido)
- [07/04] ~~OpenClaw — rate limit cascata: todos os crons falhando por fallback = mesmo provider.~~ → Movido para ✅

## 🟡 Importantes (não bloqueiam mas precisam de ação)

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

- [09/04] MELI — 22 SKUs com margem negativa após correção com dados reais. Piores: CNCOL-80 PCS (-22%), KIT2YW320 (-21%), SPC011 (-19%), EMB01T (-19%). **Ação necessária: revisar preços ou descontinuar.** → [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] [[skills/marketplace/ml-fees-rules/SKILL|ml-fees-rules]]
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
- [10/04] Atualizar skill [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] com novo SSID da planilha
- [10/04] Amazon — SKUs duplicados: IMB501*_T e IMB501T-{cor} apontam para os mesmos ASINs. Investigar e consolidar.
- [10/04] Obsidian — Auditoria profunda de conexões semânticas pendente. Prompt recebido, executar em sessão dedicada.
- [14/04] ✅ ~~Vault — Implementar estrutura proposta para centralização~~ → Executado: 5 fases completas (reestruturação, migração, frontmatter, taxonomia, conexões)
- [14/04] ✅ ~~Máquina — Limpar duplicatas de projetos~~ → Executado: SIMULIMPORT deletado, 4 projetos consolidados em 05-Projetos-Codigo/
- [14/04] ✅ ~~Vault — Migrar vault antigo~~ → Vault antigo scanneado (37 notas), 1 nota migrada (Trades Up), 36 descartadas (calendário obsoleto/leads mortos)
- [14/04] ✅ ~~Vault — Converter Word docs~~ → 6 docs convertidos via pandoc (3 atendimento, 2 OpenClaw briefings, 1 memoria tobias)
- [14/04] Downloads — Limpeza necessária (31 GB acumulados: 1723 PDFs, 1400+ planilhas, 5000+ imagens, 469 vídeos). Maioria são históricos que podem ser arquivados ou deletados.
- [15/04] E-commerce — Testar redesign no mobile real (celular físico). Verificar StickyAddToCart, AnnouncementBar dismiss, fontes Satoshi/Bricolage carregando.
- [15/04] E-commerce — Code-splitting: chunk JS 895KB (warning Vite). Considerar dynamic import() nas páginas admin e checkout.
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

---

*Atualizado: 15/04/2026*

---

## Ver também

- [[memory/context/deadlines|Deadlines — Prazos relevantes]]
- [[memory/context/decisoes/2026-04|Decisões — Abril 2026]]

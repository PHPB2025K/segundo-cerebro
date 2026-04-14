---
title: "CHANGELOG"
created: 2026-04-14
type: changelog
agent: kobe
status: active
tags:
  - agent/kobe
---

# CHANGELOG — Evolução Contínua do Kobe

_Registro cronológico de todas as melhorias aplicadas nas skills, aprendizados capturados e evolução de competência._

---

## 2026-04-07

### Entregas do dia:
- **PCM001 lançado** nas 5 frentes operacionais: Mercado Livre, 3 lojas Shopee e Amazon BR com submissão aceita e ASIN pendente.
- **Custos e margens mapeados** para os 3 canais do PCM001, incluindo custo fixo do kit, margem por canal e custo real de frete grátis no ML.
- **Skills novas registradas:** `amazon-listing-creator` e `shopee-listing-creator` incorporadas como referência operacional do workspace.

### Memória:
- **Decisões registradas:** 3 regras operacionais novas de cadastro/precificação para ML, Shopee e Amazon.
- **Lições registradas:** 5 lições táticas novas sobre `gold_special`, formato `unit_count`, limitações da API Shopee, GTIN exemption e degrau de taxa fixa em R$80.
- **Projeto GB atualizado:** PCM001 passou a constar com IDs de anúncios, custos e margens por plataforma.
- **Pendências abertas:** verificação do ASIN, registro no Supabase, confirmação dos scripts Amazon, peso embalado, foto 9 e refinamento de custos.

---

## 2026-03-31

### Entregas do dia:
- **6 NFs Venda Interna Março/2026** emitidas e autorizadas SEFAZ (R$ 29.355,85): 3 Filial CFOP 5102 + 3 Matriz CFOP 6102 (excedente)
- **Causa raiz bug tributação Bling** descoberta: API ignora impostos no payload, tributação vem da Natureza de Operação
- **Mission Control** — 5 fixes aplicados (Pedro via Claude Code), Evolution API corrigida (Kobe)
- **Auditoria axios npm** — VPS seguro, nenhuma versão comprometida
- **8 prints** configuração Bling Filial salvos em reference/

### Memória:
- Fisco: 4 decisões, 7 lições, 6 NFs no log, 7 pendências, 3 contatos Bling
- Kobe: 3 decisões, 4 lições registradas
- Mapeamento CNPJ × Marketplace definitivo confirmado pelo Pedro

### Limpeza pending.md:
- Removido: Certificado digital Filial (✅ resolvido 30/03), NF #613 validação (✅ emitida), SOUL.md RH reescrita
- Reorganizado por prioridade (Fisco subiu para topo por urgência fiscal)

---

## 2026-03-25 (consolidação diária — 02:30 UTC)

### Consolidação completa do dia 24/03
- **Sessão 2026-03-24:** Reescrita com cobertura completa (7 Builder jobs, 8 decisões, 4 lições, deploy Budamix + Spark + Security)
- **Decisões extraídas:** 4 novas (Builder Opus 4.6, briefings design system, Budamix prioridade, rate limits budget)
- **Lições já capturadas:** 4 (briefing sem design system, RESULT.md em failed, Supabase CLI token, Traefik file provider)
- **Pendências atualizadas:** Cross-channel price check adicionado, consolidação timeout corrigido
- **Builder sessions:** Criada primeira sessão própria (2026-03-24.md)
- **Trader sessions:** Criada sessão com cross-references
- **Spark sessions:** Atualizada com detalhes completos

---

## 2026-03-24 (ciclo multi-agente — 07:30 UTC)

### Ciclo de compactação e indexação — todos os agentes
- **Memory index forçado:** main, trader, spark, builder — ✅ todos indexados com sucesso
- **Sessões revisadas:** 2026-03-24 (main + spark) — sem atividade relevante, nada novo para extrair
- **Trader sessions:** diretório vazio (sem sessões individuais ainda)
- **Builder:** sem sessões de memória próprias (opera via workspace Kobe)
- **Lições extraídas:** 0 novas (período 23-24/03 sem interação ativa)
- **Decisões extraídas:** 0 novas
- **Pending:** sem alterações necessárias (última atualização 02:30 UTC correta)
- **Arquivos core:** sem mudanças necessárias

---

## 2026-03-24 (ciclo melhoria 23/03)

### Atividades consolidadas do dia 23/03 (segunda — feriado?)
- **Pedro descansando:** Sem interações diretas. Silêncio respeitado (sábado 13h–domingo 23h59).
- **Crons automáticos:** Backup GitHub (03h), heartbeat tokens (10h30).
- **Manutenção silenciosa:** pending.md contadores atualizados, nada crítico.

### Lições novas capturadas (0):
- Sem erros ou descobertas técnicas (dia de descanso Pedro).

### Decisões registradas (0):
- Sem interação com Pedro.

### Skills criadas (0):
- Nenhuma.

### Skills atualizadas (0):
- Nenhuma.

### Pendências atualizadas:
- Contadores de estagnação: Rômulo/Bidspark/Canguu em 🔴🔴 (~9 dias), budamix-store em 🔴 (~5 dias)

### Métricas:
- Skills criadas: 0
- Skills atualizadas: 0
- Lições novas: 0
- Decisões novas: 0
- Agentes capacitados: 0 (Trader já ✅ no 23/03)
- Gate de encerramento: 8/8 itens ✅

---

## 2026-03-23 (ciclo melhoria 22/03)

### Atividades consolidadas do dia 22/03 (domingo):
- **Skill coaching-corrida criada:** Coach de corrida pessoal do Pedro. SKILL.md + knowledge-base.md (793 linhas). Zonas de pace calibradas, protocolos de lesão, periodização. Planilha plano-unificado.xlsx incluída.
- **Trader capacitado completo:** 5 etapas finalizadas — SOUL.md, IDENTITY.md v2, memória (decisions, lessons, platforms, pending, reviews), skills referenciadas, TEAM.md atualizado. Falta cron de consolidação diária.
- **Manutenção noturna:** Tokens Shopee refreshados, contadores de estagnação atualizados.
- **Sem interação com Pedro:** Domingo de descanso.

### Lições novas capturadas (0):
- Dia sem erros ou descobertas técnicas.

### Decisões registradas (0):
- Sem interação com Pedro.

### Skills criadas (1):
- `skills/coaching-corrida/` — Coach de corrida pessoal (meta: meia maratona julho/2026)

### Skills atualizadas (0):
- Nenhuma.

### Pendências atualizadas:
- Contadores de estagnação incrementados (+1 dia)
- Bidspark CLAUDE.md e Canguu Railway agora em 🔴🔴 ESTAGNADO (~7-8 dias)
- budamix-store OAuth: 🟡→🔴 (~4 dias)
- Trader: Etapas 1-5 ✅, falta cron consolidação diária

### Métricas:
- Skills criadas: 1
- Skills atualizadas: 0
- Lições novas: 0
- Decisões novas: 0
- Agentes capacitados: 1 (Trader completo)

---

## 2026-03-22 (ciclo melhoria 21/03)

### Atividades consolidadas do dia 21/03:
- **Consolidado Financeiro v2.0–v2.3:** 4 iterações com Pedro. Adicionados: margem por produto (planilha real), fluxo de caixa semanal, alertas automáticos, tabelas compactas, nomenclatura "Curva" corrigida.
- **Margem consolidada GB revelada:** 13,7% — abaixo do mínimo 15%. Insight crítico: volume concentrado na Shopee onde margens são piores (CK4742_B 9%, IMB501P_T 5%).
- **Connectors Amazon + Shopee implementados:** Amazon SP-API (192 orders/5 dias) e Shopee API v2 (249 orders/2 dias). Throttling + retry + backoff.
- **Padronização de SKUs:** 27 SKUs renomeados na planilha de estoque. 9 SKUs atualizados na Shopee via API. 14 anúncios ML com seller_custom_field. Amazon: não mexer (imutável).
- **Upseller ERP:** Tentativa de automação descartada (CAPTCHA + SPA). Pedro configurando manualmente.
- **budamix-store:** refresh_token expirado. Reautorização pendente.

### Lições novas capturadas (3):
- Upseller ERP: CAPTCHA + SPA = automação inviável [TÁTICA]
- budamix-store: refresh_token pode expirar silenciosamente [TÁTICA]
- Margem consolidada 13,7% — volume concentrado onde margem é pior [ESTRATÉGICA]

### Decisões registradas (3):
- SKUs: Amazon é imutável, Upseller usar Apelido
- Margem real 13,7%, ação pendente (redirecionar volume ou reajustar pricing)
- HTML iterativo: Pedro aprova versão por versão, não precisa entregar perfeito de primeira

### Skills atualizadas (1):
- `skills/marketplace/consolidado-financeiro/SKILL.md` — Bloco MELHORIA com v2.0–v2.3 (margem, fluxo de caixa, alertas, compactação, nomenclatura)

### Pendências atualizadas:
- budamix-store OAuth: adicionado como pendência
- Upseller mapeamento SKU: adicionado
- Itens de estagnação atualizados (+1 dia cada, Sara e Rômulo em 🔴)

### Métricas:
- Skills criadas: 0
- Skills atualizadas: 1
- Connectors criados: 2 (Amazon + Shopee)
- Relatórios: 4 versões iterativas do consolidado (v2.0, v2.1, v2.2, v2.3)

---

## 2026-03-21 (ciclo melhoria 20/03)

### Atividades consolidadas do dia 20/03:
- **Shopee Open Platform aprovado:** App "Openclaw Agent" aprovado. Live Partner ID: 2031533. OAuth server ativo com auto-refresh a cada 3h30. 3 contas conectadas (budamix-store, budamix-store2, budamix-shop).
- **Extratos financeiros completos:** Shopee (R$118k bruto, 2.739 pedidos), ML (R$64k bruto, 998 vendas), Amazon (R$15k bruto, 435 vendas). Consolidado: R$197k bruto, R$131k líquido, 66,7% margem.
- **Skill shopee-extrato criada:** Script multi-conta (`--conta todas`), 23 colunas padrão, ~13 min para 3 contas.
- **Skill amazon-extrato criada:** Via python-amazon-sp-api (SP-API), 23 colunas padrão.
- **Skill consolidado-financeiro criada:** HTML + Excel, 7 seções, design system dark mode editorial.
- **Excel Design System criado:** Paleta dark mode para todos os Excels da operação.
- **Nomenclatura financeira unificada:** Mapeamento ML ↔ Shopee ↔ Amazon de termos financeiros.
- **Multi-agente validado:** Trader executou extrato Amazon + ML + consolidado com sucesso. Pedro aprovou modelo de delegação.
- **DNS configurado:** `api.importadoragb.com.br` → VPS (mas SSL bloqueado por firewall Hostinger, usando hstgr.cloud).
- **Relatório consolidado entregue:** HTML (1120px) + Excel, design aprovado pelo Pedro.

### Lições novas capturadas (4):
- Hostinger bloqueia Let's Encrypt em domínios custom — usar hstgr.cloud [TÁTICA]
- Shopee access_token expira em 4h — auto-refresh a cada 3h30 [TÁTICA]
- Multi-agente funciona: Kobe coordena, Trader executa [ESTRATÉGICA]
- Shopee extrato multi-conta: ~13 min para 3.300 pedidos [TÁTICA]

### Decisões registradas (4):
- Formato entrega: HTML (leitura) + Excel (source of truth) — sempre ambos
- Separação: Financeiro (liquidação) vs Performance (venda)
- Curva ABC consolidada (3 plataformas) substitui Top 10 individual
- Largura HTML: 860px → 1120px

### Skills criadas (4):
- `skills/marketplace/shopee-extrato/` — Extrato financeiro Shopee multi-conta
- `skills/marketplace/amazon-extrato/` — Extrato financeiro Amazon SP-API
- `skills/financeiro/consolidado-financeiro/` — Consolidado 3 plataformas
- `skills/design/excel-design-system.md` — Paleta Excel dark mode

### Skills atualizadas (0):
- Nenhuma skill anterior atualizada (dia focado em criação)

### Pendências atualizadas:
- Shopee Open Platform: ✅ aprovado e integrado
- Shopee App Approval: ✅ concluído
- Gaps consolidado financeiro: margem por produto, fluxo de caixa, alertas, ads no breakdown — mantidos para próximo ciclo

### Métricas:
- Skills criadas: 4
- Skills atualizadas: 0
- Relatórios: 6 (3 extratos + 1 consolidado HTML + 1 consolidado Excel + design system)
- Commits: múltiplos
- Lições novas: 4
- Decisões novas: 4
- Integrações finalizadas: 1 (Shopee Open Platform completa)

---

## 2026-03-20 (ciclo melhoria 19/03)

### Atividades consolidadas do dia 19/03:
- **Shopee Open Platform:** App "Openclaw Agent" submetido pra Go Live. Test Partner ID: 1228462. Aprovação pendente (~24h). Dashboard fake gerada pra screenshot.
- **Shopee fees skill:** `skills/marketplace/shopee-fees-rules/SKILL.md` criada com 14 seções, 8 fontes, 5 URLs de monitoramento. Mudanças massivas março 2026 documentadas.
- **Meta Ads API integrada:** App KOBE.OPENCLAW, 14 contas encontradas, 16 campanhas (todas pausadas). Long-lived token 60 dias. Credenciais no 1Password.
- **Skill meta-ads:** `skills/marketing/meta-ads/` — SKILL.md + 3 scripts + 6 references. Testada contra conta real.
- **Skill fullstack-dev:** `skills/dev/fullstack-dev/` — SKILL.md + 3 scripts + 9 references + starter template. ~100KB de pesquisa base.
- **Análise concorrência Shopee:** 50 resultados via JSON-LD + screenshot. Mediana ~R$37 vs ML ~R$46 (Shopee ~20% mais barato).
- **LinkedIn API pesquisada:** Postagens automatizadas ✅, Messages/Invitations ❌ (parceiros só). 5 perfis Shopee BR mapeados.
- **WhatsApp pareado:** Aparelho vinculado ao número do Pedro. Chips próprios a caminho.
- **Renomeação Tobias→Kobe:** IDENTITY.md, SOUL.md, Telegram Hub atualizados.
- **Proatividade implementada:** HEARTBEAT.md reescrito, checagem 3x/dia, organização noturna silenciosa, horários de silêncio definidos.
- **Team agents:** Trader + Spark + Builder criados com memória própria em shared/.
- **Gmail reautenticado:** OAuth do pehpbroglio@gmail.com refreshado via túnel SSH.
- **Relatório diário:** `reports/daily-report-2026-03-19.html` gerado.

### Lições novas capturadas (5):
- Shopee é SPA — scraping limitado, usar JSON-LD ou screenshot [TÁTICA]
- Bright Data Premium Domains — propagação pode demorar [TÁTICA]
- Shopee março 2026 — reajuste massivo de taxas [ESTRATÉGICA]
- Meta Ads: system user limitado por BM, usar long-lived token [TÁTICA]
- OAuth Google: app em Produção evita expiração 7 dias [TÁTICA]

### Decisões registradas (4):
- WhatsApp: mesmo cuidado que email do Pedro (pedir permissão)
- Meta Ads: conta principal act_323534883953033, renovar token 15/05
- Team agents: Trader, Spark, Builder com memória própria
- Proatividade: 3 níveis (checagem, organização, briefing) com horários de silêncio

### Skills criadas (2):
- `skills/marketplace/shopee-fees-rules/` — Regras de taxas Shopee 2026
- `skills/marketing/meta-ads/` — Meta Ads API completa
- `skills/dev/fullstack-dev/` — Bootstrapper Next.js + FastAPI

### Pendências atualizadas:
- Shopee app: aguardando aprovação Go Live
- Chips Vivo: chegam 20/03
- Meta Ads token: renovar 15/05
- Sessão movida de memory/ pra memory/sessions/ (correção estrutural)

### Métricas:
- Skills criadas: 3
- Skills atualizadas: 0
- Relatórios: 3 (shopee fees, auditoria shopee pricing, daily report)
- Commits: 7
- Lições novas: 5
- Decisões novas: 4
- Integrações novas: 3 (Meta Ads, WhatsApp, Shopee Open Platform)

---

## 2026-03-19 (ciclo melhoria 18/03)

### Atividades consolidadas do dia 18/03:
- **Skill ml-competitor-analysis:** Criada do zero — metodologia 5+ termos × 3+ páginas via Bright Data, classificação visual, relatório padronizado. Primeiro case: Jogo 5 Potes (314 únicos, 73 idênticos)
- **Skill ml-fees-rules:** Deep research completo — comissões, taxas, frete, Full, armazenagem. Mudança crítica março/2026 documentada (abolição taxa fixa, tabela frete grátis compulsória)
- **Skill inventory-management:** Fonte única estoque, composição 18 kits mapeada, Sheet ID documentado
- **Skill report-design-system:** Dark mode theme, template base HTML, fontes Inter + JetBrains Mono
- **Bright Data integrado:** Web Unlocker com CAPTCHA solver, paginação ML via `?page=N`
- **Report engine refatorado:** PDF→HTML, CSS via template externo, removido wkhtmltopdf
- **Análise competitiva Jogo 5 Potes:** 21 páginas, 314 produtos, relatório dark mode 41KB
- **Análise de precificação real:** Dados da planilha do Drive vs estimativas — diferença brutal (Clássico 32% vs Premium 13%)
- **Debounce 8s Telegram:** Modo collect configurado
- **Perplexity API + deep-research skill:** Integrada e testada

### Lições novas capturadas (4):
- Bright Data: paginação ML com `?page=N`, não `_Desde_49` [TÁTICA]
- FULL ≠ Frete Grátis Universal — classificar como universal/meli_plus/none [ESTRATÉGICA]
- Planilha real > estimativas para pricing — erro pode ser brutal [ESTRATÉGICA]
- ML API endpoints bloqueados por IP datacenter — usar Bright Data [TÁTICA]

### Decisões registradas (2):
- Crons ML → tópico 🛒 Marketplaces (thread 3)
- Estratégia de operação: alto giro, poucos SKUs. Volume > margem unitária.

### Skills criadas (4):
- `skills/marketplace/ml-competitor-analysis/` — Análise competitiva ML
- `skills/marketplace/ml-fees-rules/` — Regras de comissões e taxas ML 2026
- `skills/operations/inventory-management/` — Gestão de estoque
- `skills/design/report-design-system/` — Design system dark mode

### Skills atualizadas (1):
- `skills/marketplace/marketplace-report/` — Report engine HTML + bloco MELHORIA output

### Pendências atualizadas:
- Amazon SP-API: 3 dias sem resposta → urgente
- Skills novas pendentes de validação com mais cases
- ML Fees cron semanal configurado

### Métricas:
- Skills criadas: 4
- Skills atualizadas: 1
- Relatórios: 2 (análise competitiva + vendas por SKU)
- Commits: 13
- Lições novas: 4
- Decisões novas: 2

---

## 2026-03-18 (ciclo melhoria 17/03)

### Atividades consolidadas do dia 17/03:
- **Auditoria Bidspark:** Relatório completo `reports/auditoria-bidspark-2026-03-17.md` — 155 linhas, 14 achados, plano de ação em 3 fases
- **Arquitetura de memória:** Gate de encerramento, feedback loops, HEARTBEAT.md, MEMORY.md expandido
- **Telegram Hub:** 11 tópicos mapeados com thread IDs
- **Skill ml-ads:** Criada do zero (ml-ads/SKILL.md + references/endpoints.md)
- **marketplace-report seção 5:** Dados reais ML Ads integrados (ROAS 8.76x, 21 campanhas)

### Lições novas capturadas (5):
- Bidspark: zero testes = bloqueio real pra produção [ESTRATÉGICA]
- ML Ads seção 5 funcionando com dados reais [TÁTICA]
- Amazon Ads ainda em sandbox (não subir pra produção antes de trocar) [TÁTICA]
- Credenciais no CLAUDE.md = risco de segurança [ESTRATÉGICA]
- Enforcement > Documentação (gate obrigatório implementado) [ESTRATÉGICA]

### Decisões registradas:
- Bidspark: validação de resultados próprios antes de test users

### Skills criadas:
- `skills/marketplace/ml-ads/` — Advertising API ML completa

### Skills atualizadas:
- `skills/marketplace/marketplace-report/scripts/sections/s05_ads.py` — seção 5 com dados reais

### Pendências atualizadas:
- Amazon SP-API: prazo 24-72h já passou → verificar status
- Bidspark: CLAUDE.md com credenciais em plain text marcado como urgente

### Métricas:
- Skills criadas: 1 (ml-ads)
- Skills atualizadas: 1 (marketplace-report s05_ads.py)
- Relatórios: 1 (auditoria Bidspark)
- Commits: 6
- Lições novas: 5

---

## 2026-03-17 (ciclo retroativo 16/03)

### Ciclo de melhoria executado:
- **ml-extrato**: +2 melhorias (formato padrão aprovado, refresh obrigatório)
- **instagram**: +1 melhoria (estrutura de resposta da API)
- **stripe-api**: +1 melhoria (chaves test vs live)
- **marketplace-report**: já tinha 4 melhorias (CSS, ícones, cards, gráficos)
- **pending.md**: atualizado com todas as pendências
- **sessions/2026-03-16.md**: consolidada

### Autocrítica:
- ❌ Não rodei o ciclo automaticamente ontem ao final da sessão
- ✅ Lição registrada: rodar ciclo ANTES de encerrar, não depois

---

## 2026-03-16

### Skills atualizadas:
- **marketplace/marketplace-report**: Cards KPI refatorados 3x (grid → table-cell → com ícones SVG → posição lateral), gráficos premium com curvas suavizadas, paleta Budamix aplicada
- **marketplace/ml-extrato**: Adicionados critérios de qualidade, classificações em português
- **integracao/instagram**: SKILL.md reescrito com 5 seções obrigatórias

### Novos aprendizados capturados:
- wkhtmltopdf não suporta CSS Grid — usar `display: table` / `table-cell` como fallback
- wkhtmltopdf não renderiza emojis nativamente — usar SVG inline
- Emails via gog API não injetam assinatura automaticamente — incluir HTML no body
- Amazon Ads API: Brasil usa endpoint NA (advertising-api.amazon.com), não SA
- Amazon SP-API requer IAM Role + User separados (não basta IAM User)

### Erros prevenidos:
- Primeira sessão, portanto sem erros prevenidos por melhorias anteriores

### Métricas:
- Skills atualizadas: 3
- Novos padrões documentados: 5
- Skills criadas: 3 (marketplace-report, ml-extrato, instagram)

---

## 2026-03-15

### Skills atualizadas:
- Estrutura de memória implementada (MEMORY.md + subpastas)
- Backup GitHub configurado com cron

### Novos aprendizados capturados:
- Não sugerir fechar sessão repetidamente (só após 4h+)
- Config permissions do OpenClaw devem ser 600, não 644
- Brave Search API precisa de $5/mês crédito (1000 queries grátis)

### Métricas:
- Skills atualizadas: 0 (sessão de setup)
- Novos padrões documentados: 3
- Integrações configuradas: 7 (Brave, 1Password, gog, GitHub, Whisper, clima, Telegram)

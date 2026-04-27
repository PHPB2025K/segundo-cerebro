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

_Atualizado: 2026-04-27 02:00 BRT — organização noturna silenciosa; estagnados >7 dias anotados para briefing_

## 🚨 URGENTE — Infraestrutura e saúde do sistema

### Autenticações críticas bloqueadas/degradadas
- [ ] **Google Ads API - Spark** — credenciais existem no 1Password, mas validação OAuth em 26/04 13:40 BRT retornou `invalid_grant`; refresh token precisa ser reautorizado/gerado novamente para a conta Google Ads.
- [ ] **Google Calendar (gog) para Daily Briefing** — falha de autenticação ainda não foi revalidada após Sheets funcionar; agenda pode seguir indisponível no briefing matinal.
- [ ] **Gmail (gog) para Inbox Cleanup** — falha de descriptografia/token ainda precisa validação própria; nenhum email deve ser assumido como processável até teste real.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password, mas rotação é medida de higiene.

### Saúde de crons recorrentes críticos
- [ ] **Watchdog - Monitor de Crons** — falhou por timeout de 3min em 26/04; revisar escopo/timeout para não confundir com falha do job-monitor.
- [ ] **Monitor Ponto Semanal** — falhas consecutivas por timeout de 300s. Bloqueado sem execução confiável até revisão de escopo/timeout.
- [ ] **RH Monitor Ponto Saída** — última falha relevante foi por fallback inválido/model not found. Cadeia de fallback precisa corrigir antes de próxima execução.
- [ ] **Bling Token Refresh / Filial** — 26/04 15:32 BRT: Client Secrets rotacionados no 1Password e scripts ajustados para ler secrets via 1Password em runtime. Matriz refresh OK, Supabase sync OK e API `/produtos?limite=1` HTTP 200. Filial refresh segue HTTP 403 `Empresa inativa`; token antigo já expirou e teste API retorna HTTP 401. Pendência é reativar/validar empresa Filial no painel Bling e reautorizar OAuth se necessário.

## 🔥 PRIORIDADE IMEDIATA — Financeiro
- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.
- [ ] **OAuth rotation 3 contas Shopee** — garantir refresh automático também para `budamix-shop` e `budamix-store2`.

## 🔥 PRIORIDADE IMEDIATA — Budamix Central / PCM001
- [ ] **PCM001 Amazon** — ASIN ainda pendente desde lançamento 07/04. Verificar status na Amazon BR. **Estagnado >7 dias: puxar no briefing matinal se nada mudou.**
- [ ] **PCM001 peso embalado** — Pedro precisa informar peso final do kit embalado para NF-e.
- [ ] **PCM001 foto 9** — Pedro precisa enviar hero image de encerramento.
- [ ] **PCM001 custos refinados** — substituir estimativas de embalagem e mão de obra por custo real.
- [ ] **57 SKUs sem cost_price** na `fulfillment_inventory` — falta de preço de custo na base.
- [ ] **9 Amazon SKUs sem preço** — 8 com estoque, precisam investigação.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog
- [ ] **Supabase Budamix Ecommerce REST keys** — anon/service role keys salvas no 1Password retornaram 401 via REST; corrigir/rotacionar antes de workflows N8N dependerem delas.
- [ ] **Budamix Ecommerce push GitHub (SEO + WF4 Blog)** — commits locais do blog/WF4 ficaram ahead, mas `git push origin main` retornou HTTP 403/write access not granted. Regularizar credencial/PAT do repo principal e subir tudo antes de considerar a automação fechada.
- [ ] **Admin Blog em produção — botão/status do WF4** — validar em produção o acionamento de `Preparar com IA` e a exibição do status `ready_to_publish` no Admin depois que o push/deploy do repo principal for destravado.
- [ ] **Revisar primeiro lote de 5 pautas Perplexity** — decidir quais viram draft real, quais rejeitar e quais arquivar.

## 🔥 PRIORIDADE IMEDIATA — SimulImport
- [ ] **Validar cenários reais** — Pedro testar com importações dele.

## 🟡 Para briefing matinal — estagnados >7 dias
_Anotação da organização noturna de 27/04 02:00 BRT._

- **PCM001 Amazon** — pendente desde 07/04, ainda em prioridade imediata.
- **Já classificados no Backlog Estagnado (>14 dias):** Links Amazon da base Ana, revisão manual dos campos [VERIFICAR] do catálogo da Ana, sync Amazon de `platform_item_id/links`, 3 SKUs ML sem mapeamento automático e teste do motor SimulImport com NCMs corrigidos.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **Links Amazon da base Ana (61 SKUs)** — pendência estrutural sem avanço material. Último update 06/04. Cruzamento automático falhou, casos manuais bloqueados.
- [ ] **Revisão manual dos campos [VERIFICAR] do catálogo da Ana** — priorizar top 15 por vendas antes do cadastro definitivo no Canggu. Último update 06/04.
- [ ] **Corrigir sync Amazon de platform_item_id/links no Budamix Central** — muitos produtos seguem com `SEM_LINK_AMAZON`. Último update 02/04.
- [ ] **Onda 3 (Budamix Central cleanup)** — remover deps mortas, ErrorBoundary, sync button real. Fora da fila imediata.
- [ ] **Estoque Full + sku_mapping** — integrar tabela `sku_mapping`. Fora da fila imediata.
- [ ] **3 SKUs ML sem mapeamento automático** — sem atributo `SELLER_SKU`. Último update 06/04.
- [ ] **Otimizar sync-inventory-shopee.py** — lento, com sleeps demais. Fora da fila imediata.
- [ ] **Auto-sync tokens Shopee → Supabase**. Fora da fila.
- [ ] **Cache IDs Shopee** — reduzir chamadas repetidas. Fora da fila.
- [ ] **Supabase key hardcoded** — mover service role key para env var. Fora da fila.
- [ ] **Antidumping seed** — confirmar se foi aplicado ao Supabase. Fora da fila.
- [ ] **Lovable sync** — Project ID nunca registrado. Fora da fila.
- [ ] **Testar motor de cálculo (SimulImport)** com NCMs corrigidos. Último update 29/03.
- [ ] **Deletar NFs de teste** — Filial: 011–027. Matriz: 611–616. Sem movimentação recente.
- [ ] **Preencher product-packaging.json** — pesos e volumes de SKUs Budamix. Bloqueando NFs futuras.
- [ ] **Faturamento B2B março** — levantar parcela B2B da Filial para calibrar motor distribuição. Sem avanço.
- [ ] **Automatizar detecção de excedente** — codificar lógica de cruzamento NFs transferência vs vendas no Módulo C Fisco.
- [ ] **Contatos IDs Bling Matriz** — mapear IDs dos 3 CNPJs no Bling da Matriz. Sem avanço.
- [ ] **Pedro criar instância WhatsApp RH na Evolution API** — número 5519992997273. Painel Cloudfy ou Global API Key.
- [ ] **Chip 5519992997273 pareamento** — QR code na Evolution API após instância criada.
- [ ] **Knowledge Files RH da FOUR/Suellen** — tabela salarial, benefícios, holerite, calendário 2026, regulamento, férias, INSS/IRRF, contratos, horas extras, feriados.
- [ ] **Mission Control DNS** — Pedro criar registro A para `mission.gbformulario.com`.
- [ ] **Mission Control** — customizar painéis TenacitOS e criar crons de alimentação.
- [ ] **Spark Ads Fase 1** — depende de repriorização do Kobe/Pedro após estabilização.
- [ ] **Padronização de novos briefings complexos Builder** — depende de novas frentes.
- [ ] **Ads Shopee** — mapear endpoints como próximo passo. Sem avanço.
- [ ] **Canggu** — Pedro enviar acesso ao Railway. Sem avanço.
- [ ] **Verificar deploy novo do Canguu no VPS** — se virar prioridade, fazer checagem operacional.
- [ ] **Security Audit semanal** — truncar mensagem longa no Telegram.
- [ ] **Bidspark CLAUDE.md** — remover Client ID + Secret em texto puro.
- [ ] **Webhooks marketplaces** — Fase 3, não prioritário.
- [ ] **Kit Segundo Cérebro — módulo VPS/OpenClaw** — se a promessa comercial for Claude Code + OpenClaw, criar scripts/docs/contrato de sync.
- [ ] **Session Extractors antigos** — desabilitados com timeout recorrente. Revisar estratégia ou limpar.
- [ ] **ML Traffic API** — restrição a apps certificados. Aguardando certificação Google.
- [ ] **Stripe live key** — aguardando decisão do Pedro.
- [ ] **Bidspark validação com dados reais** — bloqueado por falta de histórico.
- [ ] **LinkedIn integração** — sem requisição formal.

---

_Última organização: 2026-04-27 02:00 BRT. Próxima revisão: Consolidação Profunda/Diária conforme cron._

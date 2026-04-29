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

_Atualizado: 2026-04-28 23:30 BRT — consolidação diária após Vault-as-SSoT, Blog Budamix e Social Studio_

## 🚨 URGENTE — Infraestrutura e saúde do sistema

### Autenticações críticas bloqueadas/degradadas
- [ ] **Google Ads API - Spark** — credenciais existem no 1Password, mas validação OAuth em 26/04 13:40 BRT retornou `invalid_grant`; refresh token precisa ser reautorizado/gerado novamente.
- [ ] **Slack App GB Importadora** — rotacionar/reinstalar para invalidar bot token que apareceu em screenshot durante setup. Integração operacional usa user token read-only salvo no 1Password, mas rotação é medida de higiene.
- [ ] **WhatsApp Baileys/OpenClaw** — leitura passiva em tempo real está desconectada/not linked; se Pedro quiser reativar essa rota, precisa reescanear QR Code. Evolution API/histórico segue separado e funcional.
- [ ] **Bling Token Refresh / Filial** — Matriz OK, mas Filial segue com bloqueio de empresa inativa/401; validar empresa Filial no painel Bling e reautorizar OAuth se necessário.

### Saúde de crons recorrentes críticos
- [ ] **Watchdog - Monitor de Crons** — falhou por timeout de 3min em 26/04; revisar escopo/timeout para não confundir com falha do job-monitor.
- [ ] **Monitor Ponto Semanal** — falhas consecutivas por timeout de 300s. Bloqueado sem execução confiável até revisão de escopo/timeout.
- [ ] **RH Monitor Ponto Saída** — última falha relevante foi por fallback inválido/model not found. Cadeia de fallback precisa corrigir antes de próxima execução.

## 🔥 PRIORIDADE IMEDIATA — Financeiro
- [ ] **Ads spend março** — levantar gasto real com publicidade por plataforma (ML, Amazon via integração, Shopee manual). Sem este dado, consolidado de março é inválido.
- [ ] **Refazer fechamento de março** — gerar consolidado novo (DRE operacional + planilha + HTML) com os 5 extratos validados completos + ads spend correto.
- [ ] **Mapeamento semanal DRE** — separar março por semanas (01-07, 08-14, 15-21, 22-31) nas linhas da DRE para análise de evolução.
- [ ] **OAuth rotation 3 contas Shopee** — garantir refresh automático também para `budamix-shop` e `budamix-store2`.

## 🔥 PRIORIDADE IMEDIATA — Budamix E-commerce / Blog / Social Studio
- [ ] **Blog Budamix — QA real pós-correções**: criar artigo novo em produção e validar `Em geração` → `em_edicao` somente após `cover`, `support_1`, `support_2`, `pinterest_1` com URL + `generated`; confirmar sem legendas visíveis e sem subtítulos `(de forma simples)`.
- [ ] **Blog/N8N — remover service role hardcoded do WF4**: migrar segredo para credential/env do N8N. Achado em 28/04; segredo não foi exposto no chat.
- [ ] **Blog — SSoT dos 10 pilares editoriais**: validar tabela `blog_pillars`/modelo canônico e garantir que Admin/WF2/WF4 leem a mesma fonte, evitando drift de texto livre.
- [ ] **Social Studio — QA autenticado do preview**: testar criar/listar/arquivar ideia pela UI, geração de copy, editor de carrossel e render PNG antes de merge/deploy em produção.
- [ ] **Social Studio — decidir merge/deploy** da branch `feat/social-studio-phase2` para produção após QA do Pedro.
- [ ] **Vercel Preview Env**: configurar `VITE_SUPABASE_URL` e `VITE_SUPABASE_PUBLISHABLE_KEY` no ambiente Preview do Vercel ou padronizar deploy preview via CLI com envs explícitas do 1Password.
- [ ] **Repo Budamix E-commerce — main local ahead 2**: resolver/pushar/alinhar antes da próxima entrega em produção para não misturar estado local com remoto.

## 🟡 Observação / estabilidade
- [ ] **Vault-as-SSoT — observar 48–72h**: próximo `/cerebro` deve confirmar sem conflitos git, sem dupla escrita e cron `sync-memory-to-vault.sh` limpo nos slots 7/22/37/52.

## 🟡 Futuro aprovado / não imediato
- [ ] **Budamix Blog — Pinterest API/OAuth** — ativar postagem automática no Pinterest quando padrão de artigos e imagens estiver validado. Por enquanto pins ficam apenas como assets no Admin.

## Backlog Estagnado
_Itens >14 dias sem movimentação material. Revisar/priorizar ou arquivar._

- [ ] **PCM001 Amazon** — ASIN pendente desde lançamento 07/04. Verificar status na Amazon BR quando voltar para frente de catálogo.
- [ ] **PCM001 peso embalado** — Pedro precisa informar peso final do kit embalado para NF-e.
- [ ] **PCM001 foto 9** — Pedro precisa enviar hero image de encerramento.
- [ ] **PCM001 custos refinados** — substituir estimativas de embalagem e mão de obra por custo real.
- [ ] **57 SKUs sem cost_price** na `fulfillment_inventory` — falta de preço de custo na base.
- [ ] **9 Amazon SKUs sem preço** — 8 com estoque, precisam investigação.
- [ ] **SimulImport — validar cenários reais** — Pedro testar com importações dele.
- [ ] **Links Amazon da base Ana (61 SKUs)** — pendência estrutural sem avanço material. Último update 06/04. Cruzamento automático falhou, casos manuais bloqueados.
- [ ] **Revisão manual dos campos [VERIFICAR] do catálogo da Ana** — priorizar top 15 por vendas antes do cadastro definitivo no Canggu. Último update 06/04.
- [ ] **Corrigir sync Amazon de platform_item_id/links no Budamix Central** — muitos produtos seguem com `SEM_LINK_AMAZON`. Último update 02/04.
- [ ] **Onda 3 (Budamix Central cleanup)** — remover deps mortas, ErrorBoundary, sync button real. Fora da fila imediata.
- [ ] **Estoque Full + sku_mapping** — integrar tabela `sku_mapping`. Fora da fila imediata.
- [ ] **3 SKUs ML sem mapeamento automático** — sem atributo `SELLER_SKU`. Último update 06/04.
- [ ] **Otimizar sync-inventory-shopee.py** — lento, com sleeps demais. Fora da fila imediata.
- [ ] **Auto-sync tokens Shopee → Supabase**. Fora da fila.
- [ ] **Cache IDs Shopee** — reduzir chamadas repetidas. Fora da fila.
- [ ] **Supabase key hardcoded** — mover service role key para env var em sistemas legados. Fora da fila.
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
_Última organização: 2026-04-28 23:30 BRT._

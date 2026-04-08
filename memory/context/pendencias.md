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
- [06/04] Canggu — Fase 4 cleanup pendente: remover campos antigos (marketplace_links, available_kits, price_marketplace) e dropar tabela marketplace_product_mapping. Só executar quando tudo estiver estável nas tabelas novas.
- [06/04] Canggu — ~14 Session Extractors do OpenClaw desabilitados (timeout 120s insuficiente para Opus 4.6). Precisam de 300s+. Reavaliar após migração GPT 5.4.
- [06/04] Canggu — Analistas devem preencher campos ricos (descrição completa, sugestões de uso, diferenciais, tags) dos 44 produtos ativos. Guia entregue. Top 10 primeiro.
- [06/04] OpenClaw — 3 crons com timeouts: job-monitor (30s), Contingency Guard (30s), Organização Noturna (180s). Todos precisam de aumento.
- [06/04] OpenClaw — Amazon Request Review overloaded. Haiku 3.5 possivelmente depreciado → migrar para modelo atualizado.
- [06/04] OpenClaw — GitHub Backup com timeouts. Aumentar de 120s para 300s.
- [06/04] Segurança — Porta 8084 (Evolution API?) aberta na UFW. Verificar necessidade.
- [06/04] Segurança — Tailscale/WireGuard não implementado. Recomendado.
- [07/04] Shopee — 3 anúncios Kit Porta-Copos precisam preencher campos no Seller Center (GTIN, NCM, Cor, Garantia) para diagnóstico verde. Checklist enviado ao Kobe.
- [07/04] Bright Data — API key do web_unlocker1 (e0f949a4-2599-4a02-a0a2-1063ed8fe364) precisa ser salva no 1Password do Kobe (substituir a antiga bc468a8b...). Zona criada 07/04.
- [07/04] OpenClaw — Skills shopee-listing-creator e amazon-listing-creator precisam ser importadas pelo Kobe (openclaw skills import).
- [07/04] Amazon BR — ASIN do PCM001 pendente (ACCEPTED com 0 erros, processando). Verificar. Após ASIN: upload de fotos via Seller Central + registrar no Supabase.
- [08/04] GB Import Hub — Frontend no Lovable ainda aponta pro Supabase antigo. Precisa atualizar env vars no painel do Lovable OU usar somente deploy VPS (import.budamix.com.br).
- [08/04] GB Import Hub — MarineTraffic API key não configurada (fetch-vessel-position retorna dados vazios). Não bloqueante — tracking funciona via Terminal49.
- [08/04] PCM001 — Preço alterado na planilha (R$19,90) mas NÃO alterado nos marketplaces (ML, Shopee, Amazon ainda com R$39,90). Sincronizar se intencional.
- [08/04] GB25009 — 70% balanço R$72.232 PENDENTE, vencimento 16/04. Container já finished. **Pagar.**
- [08/04] GB25011 — Numerário R$60.000 vence 11/04 (ETA do container). Container em trânsito.
- [08/04] GB26001/GB26002 — Numerário e 70% sem datas de vencimento definidas no sistema.
- [08/04] GB26002 — Numerário e 70% sem valores registrados no sistema.
- [08/04] Skill gb-import-hub instalado e validado (14/15 testes OK). terminal49-fetch-shipment com bug (HTTP 500).

## ⚪ Backlog (sem urgência imediata)

- Antidumping cerâmicas chinesas — pesquisar Vietnam e Índia como alternativas de sourcing
- TikTok Shop — definir estratégia de outreach MCN/afiliados
- Stripe — ativar modo produção (está em teste)
- Container isolation — OpenClaw roda direto no host, considerar Docker
- E-commerce budamix.com.br — monitoramento, carrinho abandonado, sync preços
- Fornecedores China — triagem emails Yiwu automatizada
- Kit duplo porta-copos (12 peças + 2 suportes) a R$69,90-79,90 para Shopee — diluir taxa fixa

---

## ✅ Resolvidas (Abril 2026)

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

---

*Atualizado: 08/04/2026*

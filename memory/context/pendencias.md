# Pendências Ativas

> Formato: `[DATA] Aguardando [QUEM] sobre [O QUÊ]`
> Atualizar: sempre que uma pendência for criada ou resolvida.
> ✅ = resolvida (mover para "Resolvidas" no final do mês)

---

## 🔴 Críticas (bloqueiam progresso)

- [06/04] VPS disco 63.4% usado de 47GB — monitorar crescimento. Logs de memory, backups e Chrome cache podem encher. Limpeza necessária em breve.
- [06/04] VPS memória 80% + swap 52% — processo zombie detectado. Requer investigação.
- [06/04] Aguardando **Pedro** publicar Canggu no Lovable (destacques visuais campos IA, envio WhatsApp corrigido)

## 🟡 Importantes (não bloqueiam mas precisam de ação)

- [06/04] OpenClaw — migração de modelos para GPT 5.4 / GPT 5.1-mini. Prompt enviado ao Kobe, aguardando execução.
- [06/04] Canggu — Fase 4 cleanup pendente: remover campos antigos (marketplace_links, available_kits, price_marketplace) e dropar tabela marketplace_product_mapping. Só executar quando tudo estiver estável nas tabelas novas.
- [06/04] Canggu — ~14 Session Extractors do OpenClaw desabilitados (timeout 120s insuficiente para Opus 4.6). Precisam de 300s+. Reavaliar após migração GPT 5.4.
- [06/04] Canggu — Analistas devem preencher campos ricos (descrição completa, sugestões de uso, diferenciais, tags) dos 44 produtos ativos. Guia entregue. Top 10 primeiro.
- [06/04] OpenClaw — 3 crons com timeouts: job-monitor (30s), Contingency Guard (30s), Organização Noturna (180s). Todos precisam de aumento.
- [06/04] OpenClaw — Amazon Request Review overloaded. Haiku 3.5 possivelmente depreciado → migrar para modelo atualizado.
- [06/04] OpenClaw — GitHub Backup com timeouts. Aumentar de 120s para 300s.
- [06/04] Segurança — Porta 8084 (Evolution API?) aberta na UFW. Verificar necessidade.
- [06/04] Segurança — Tailscale/WireGuard não implementado. Recomendado.

## ⚪ Backlog (sem urgência imediata)

- Antidumping cerâmicas chinesas — pesquisar Vietnam e Índia como alternativas de sourcing
- TikTok Shop — definir estratégia de outreach MCN/afiliados
- Stripe — ativar modo produção (está em teste)
- Container isolation — OpenClaw roda direto no host, considerar Docker
- E-commerce budamix.com.br — monitoramento, carrinho abandonado, sync preços
- Fornecedores China — triagem emails Yiwu automatizada

---

## ✅ Resolvidas (Abril 2026)

- [06/04] ✅ Canggu — Reestruturação dados produtos completa (5 fases)
- [06/04] ✅ Canggu — Pipeline vetorial da Ana funcionando (5/5 testes)
- [06/04] ✅ Canggu — Bug envio WhatsApp humano→cliente corrigido
- [06/04] ✅ Canggu — Links de marketplace adicionados ao formulário de produto
- [06/04] ✅ Canggu — Guia de preenchimento para analistas criado e entregue
- [06/04] ✅ Segundo Cérebro — Setup inicial configurado

---

*Atualizado: 06/04/2026*

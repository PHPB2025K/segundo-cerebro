# Pendências — Spark

_Atualizado: 2026-06-10_

## 🔴 Prioridade Alta

### Amazon Ads / BidSpark
- [ ] Corrigir auditoria interna `amazon_ads_actions_log` antes da próxima rodada manual: execução Tulipa 13/05 alterou 7/7 bids com sucesso, mas log interno falhou por constraints/FK.
- [ ] Aplicar protocolo de análise em 5 camadas em todos os próximos grupos antes de recomendar ações.
- [ ] Analisar Potes Redondos Plástico: D+7 mostrou piora (ACoS 13,3% → 32,3%), provável escala Exact forte demais.
- [ ] Ajuste fino em Jarra Medidora e Potes Herméticos Vidro.
- [ ] Não cortar mais Potes Tampa Bambu por enquanto; eficiência melhorou mas volume caiu.
- [ ] Investigar elegibilidade/listing/Buy Box/categoria de Kits Microfibra e Abraçadeiras Nylon, que ficaram com 0 impressões/0 cliques/0 vendas.
- [ ] Revisar logs de `action_type` para diferenciar Exact/Broad/Auto/Product Targeting antes de novas ações.

### Google Ads — Integração
- [ ] Reautorizar OAuth/refresh token: validação em 26/04 retornou `invalid_grant`.
- [ ] Confirmar Developer Token e acesso à conta Google Ads antes de qualquer automação.
- [ ] Armazenar credenciais finais no 1Password (vault OpenClaw) e validar via chamada real.

### Meta Ads — Token (RESOLVIDO 08/06)
- [x] ~~Verificar renovação/funcionamento do token Meta Ads~~ → **RESOLVIDO 2026-06-08:** migrado pra System User permanente (NEVER expira). Item 1P `hxvgwjrdluw4yblo4lbktatoyy`.



### Meta Ads — Budamix (Strategy 2026)
- [ ] **Quando Pedro entregar vídeos 2 e 3:** Kobe coordena upload + criação ads Camp 2 (3:2:2) e Camp 3 (retargeting) + criação 2 WCAs (ViewContent 14d + Purchase 30d) + ativação.
- [ ] **Daily pulse 10:20 BRT no tópico Marketing:** confirmar/validar execuções pós-implementação; nas consolidações de 09/06 e 10/06 às 22:55 BRT não havia evidência registrada na memória do Spark. Spark gera, Kobe posta.
- [ ] **NÃO TOCAR Camp 1 até ~22/06:** fase de aprendizado em curso. Qualquer mudança >20% reseta. Após sair do aprendizado, avaliar promoção do Spark pra auto-execução em ajustes pequenos.
- [ ] **Schema Supabase `meta.*`** criado em 08/06 — popular `meta.daily_pulses` via cron diário; primeiro `meta.actions_log` registrará ações pós-aprendizado.

## 🟡 Prioridade Média

### Shopee Ads
- [ ] Shopee Ads API — solicitar escopo Marketing ou definir rotina oficial de export/manual para campanhas; API atual retorna 404 nas 3 lojas.

### Meta Ads — Mapeamento
- [x] ~~Mapear campanhas Budamix~~ → **CONCLUÍDO 2026-06-08:** Strategy 2026 (3 camps) documentada em `accounts.md`. Camp 1 ATIVA.
- [ ] Broglio Brinquedos e Trades Up: sem campanhas ativas, mapear quando reativarem.
- [ ] Documentar histórico de performance quando disponível.

## 🟢 Backlog
- [ ] Configurar monitoramento contínuo quando campanhas reativarem.
- [ ] Implementar regras de escala automática.
- [ ] Dashboard de performance quando houver demanda Builder via Kobe.

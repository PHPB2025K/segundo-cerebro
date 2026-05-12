# Pendências — Spark

_Atualizado: 2026-05-11_

## 🔴 Prioridade Alta

### Amazon Ads / BidSpark
- [ ] Analisar Canecas Porcelana Tulipa com prioridade: D+7 mostrou piora forte (ACoS 18,8% → 42,6%).
- [ ] Analisar Suporte Controle Gamer: D+7 mostrou piora (ACoS 18,8% → 28,9%) e Auto/Descoberta gastando mal.
- [ ] Analisar Potes Redondos Plástico: D+7 mostrou piora (ACoS 13,3% → 32,3%), provável escala Exact forte demais.
- [ ] Ajuste fino em Jarra Medidora e Potes Herméticos Vidro.
- [ ] Não cortar mais Potes Tampa Bambu por enquanto; eficiência melhorou mas volume caiu.
- [ ] Investigar elegibilidade/listing/Buy Box/categoria de Kits Microfibra e Abraçadeiras Nylon, que ficaram com 0 impressões/0 cliques/0 vendas.
- [ ] Revisar logs de `action_type` para diferenciar Exact/Broad/Auto/Product Targeting antes de novas ações.

### Google Ads — Integração
- [ ] Reautorizar OAuth/refresh token: validação em 26/04 retornou `invalid_grant`.
- [ ] Confirmar Developer Token e acesso à conta Google Ads antes de qualquer automação.
- [ ] Armazenar credenciais finais no 1Password (vault OpenClaw) e validar via chamada real.

### Meta Ads — Token
- [ ] Renovar token antes de ~2026-05-18 — cron agendado, verificar se está funcional.

## 🟡 Prioridade Média

### Shopee Ads
- [ ] Shopee Ads API — solicitar escopo Marketing ou definir rotina oficial de export/manual para campanhas; API atual retorna 404 nas 3 lojas.

### Meta Ads — Mapeamento
- [ ] Mapear campanhas das contas Budamix, Broglio Brinquedos e Trades Up.
- [ ] Documentar histórico de performance quando disponível.

## 🟢 Backlog
- [ ] Configurar monitoramento contínuo quando campanhas reativarem.
- [ ] Implementar regras de escala automática.
- [ ] Dashboard de performance quando houver demanda Builder via Kobe.

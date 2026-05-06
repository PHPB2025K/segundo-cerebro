# Pendências — Spark

_Atualizado: 2026-05-05_

## 🔴 Prioridade Alta

### Amazon Ads / BidSpark
- [ ] Medir D+7 da rodada 02/05/2026: Potes Herméticos Vidro, Jogo Canequinhas Café, Potes Herméticos Tampa Bambu, Canecas Canelada, Canecas Porcelana Tulipa, Kit Xícaras Porcelana Paris, Suporte Controle Gamer, Jarra Medidora e Potes Redondos Plástico.
- [ ] Medir D+7 dos experimentos 03/05/2026: Kits Microfibra Carro e Abraçadeiras Nylon.
- [ ] Redinha Frutas: validar product ads + estoque/FBA + listing ativo + Buy Box antes de qualquer bid.
- [ ] Kit Jardinagem: confirmar decisão de reativação e validar estrutura antes de qualquer bid.
- [ ] Revisar logs de `action_type` para diferenciar Exact/Broad/Auto/Product Targeting antes da auditoria D+7.

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

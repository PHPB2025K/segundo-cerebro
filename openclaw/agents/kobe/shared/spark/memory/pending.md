# Pendências — Spark

_Atualizado: 2026-05-02_

## 🔴 Prioridade Alta

### Amazon Ads — Rodada 02/05/2026
- [ ] Medir D+7 dos grupos executados em 02/05: Potes Herméticos Vidro, Jogo Canequinhas Café, Potes Herméticos Tampa Bambu, Canecas Canelada, Canecas Porcelana Tulipa, Kit Xícaras Porcelana Paris, Suporte Controle Gamer, Jarra Medidora e Potes Redondos Plástico.
- [ ] Kits Microfibra Carro — aguardar aprovação para criar/promover `pano microfibra`, subir Auto `substitutes`/`close-match` e não promover `vonixx` como keyword genérica.
- [ ] Potes Herméticos Vidro — validar qual ASIN recebe tráfego de `pote hermetico vidro` e investigar preço/Buy Box/imagem/título/variação.
- [ ] Revisar logs/action_type da rodada: separar escala Exact, Broad/Alcance, Auto e Product Targeting.
- [ ] Continuar grupos finais de baixo gasto/inativos (Abraçadeiras Nylon, Redinha Frutas, Kit Jardinagem) apenas se houver materialidade.

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

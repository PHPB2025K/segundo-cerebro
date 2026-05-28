# Pendências — Spark

_Atualizado: 2026-05-27_

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

### Meta Ads — Token
- [ ] Verificar renovação/funcionamento do token Meta Ads — data estimada de expiração atingida em 2026-05-18; se falhar, escalar risco operacional.

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

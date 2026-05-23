# Weekly — Mercado Livre

## Estrutura

Consolidação semanal da conta. Atualizada toda segunda de manhã ou após 7 entradas diárias acumuladas.

## Template

### Semana: [DD/MM a DD/MM/AAAA]

#### Tese semanal
[Tese consolidada da semana baseada nas leituras diárias]

#### Padrões observados
- [Padrão 1]
- [Padrão 2]

#### Hipóteses ativas
- [Hipótese 1 — status: confirmada/enfraquecida/em aberto]

#### Riscos acumulados
- [Risco 1 — persistência: X dias]

#### Sinais para próxima semana
- [Sinal 1 — condição falsificável]

#### Ressalvas da semana
- [Ressalva 1 — frequência: X ocorrências]

---

## Memória diária acumulada

_Blocos diários abaixo. Job `daily-memory-ingest-ml.py` adiciona um bloco por dia. Rotação automática mantém os últimos 14 dias._

### Dia analisado: 2026-05-22
_ingestido em 2026-05-23T13:09:50-03:00 BRT | confiança L05: media | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090) — 7 unidades pós-baixa em Full após 6 pedidos; se próximo pacote mostrar pausa ou estoque zerado sem reposição, vira variável confundidora para health, ranking e GMV dos dias seguintes
- Health do Kit 4 Potes De Vidro Hermético 1050ml Tampa Azul-petróleo (0,75) e do Jogo Potes De Vidro 5 Peças Claro — Tampa Vermelha (0,71) — segundo ponto pontual da série (sem direção confirmada); próximo pacote com dado define se a penalização está caindo, estável ou em recuperação e desbloqueia ou descarta ação com Himmel
- ADS share 69,9% do GMV, ROAS 10,87x, ACOS 4,57%, gasto R$296,96 — segundo ponto da série iniciada em 22/05; se share acima de 65% por mais 2 ciclos com ROAS acima de 5x, vira dependência estrutural confirmada
- Cluster IMB501 (Tampa Preta Cross-Docking 20 pedidos, Tampa Vermelha Full 10 pedidos, Tampa Cinza Cross-Docking 7 pedidos) somou 37 pedidos = 44% do dia — tratar como cluster ajuda a explicar mix sem fragmentar leitura; estoque robusto nas variações Cross-Docking (8.375 e 9.196 unidades)
- Necessidade de dado para próximo ciclo: breakdown de revenue_ads_yesterday_brl por platform_item_id — sem ele a hipótese 'ADS está empurrando variações Cross-Docking ou anúncios Full penalizados' permanece inconfirmável (dado já registrado como pendente no ciclo anterior)
- Ratings_negative=0,39 (39%) é proporção alta para conta com reputação verde e MercadoLíder Gold — sem breakdown por anúncio, hipótese de sobreposição com os dois Full penalizados (MLB4073003575 e MLB3288536143) permanece em aberto; vira relevante se claims_rate subir acima de 0,005 nos próximos ciclos
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades (MLB6739241224) em Cross-Docking com 6 unidades pós-baixa e 2 pedidos — cobertura ~3 dias com ressalva (amostra pequena); checagem preventiva sem urgência, Budamix tem mais controle de reposição em Cross-Docking
- MercadoLíder Platinum: progresso 81,34%, gap R$55.226,77, ETA 13,8 dias — fora do gatilho de Slack; vira relevante quando gap cair abaixo de R$30k com progresso acima de 90%

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

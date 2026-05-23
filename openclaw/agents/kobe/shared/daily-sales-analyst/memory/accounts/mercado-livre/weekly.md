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
_ingestido em 2026-05-23T11:12:35-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml com 9 unidades em Full pós-baixa e 6 pedidos no dia — se próximo pacote mostrar anúncio pausado ou estoque zerado sem reposição, é variável confundidora para health, ranking e GMV dos próximos dias.
- Health do Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (0,75) e do Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (0,71) — segundo ponto da série; próximo pacote com dado define se vira ação com Himmel ou segue só observação.
- ADS share 69,9% do GMV, ROAS 10,87x, ACOS 4,57%, gasto R$296,96 — ponto zero da série; se share acima de 65% por mais 2 ciclos com ROAS acima de 5x, vira dependência estrutural confirmada.
- Família IMB501 (Tampa Preta Cross-Docking 20 pedidos, Tampa Vermelha Full 10 pedidos, Tampa Cinza Cross-Docking 7 pedidos) somou 37 pedidos = 44% do dia — eixo real de concentração; tratar como cluster ajuda a explicar mix sem fragmentar leitura.
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades em Cross-Docking com 6 unidades pós-baixa e 2 pedidos no dia — cobertura ~3 dias se ritmo for típico; checagem preventiva sem urgência.
- MercadoLíder Platinum: progresso 81,34%, gap R$55.226,77, ETA 13,8 dias — fora do gatilho principal de Slack; vira relevante quando gap cair abaixo de R$30k com progresso acima de 90%.
- Colisão de display_name pendente: KIT10YW1050 (10 unidades, MLB4676726433) e KIT6YW1050 (6 unidades, MLB4676751119) — corrigir no mapa estático para que display_name carregue a quantidade.
- ratings_negative=0,39 na reputação é estruturalmente alto, mas sem série no pacote para julgar trajetória — registrar para começar a montar série temporal.

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

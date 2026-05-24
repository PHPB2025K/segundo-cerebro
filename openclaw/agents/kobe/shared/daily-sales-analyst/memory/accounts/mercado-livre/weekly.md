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
_ingestido em 2026-05-23T21:19:34-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full): consumo confirmado em ~6 pedidos/dia em 2 ciclos consecutivos, estoque 7→2; se próximo pacote mostrar anúncio pausado ou cancelamento automático, vira variável confundidora para reputação, ETA Platinum e leitura do cluster de canecas
- Nível de qualidade dos dois Full em Padrão inferior — Kit 4 Potes 1050ml Tampa Azul-petróleo (MLB4073003575, 0,75) e Jogo Potes 5 Peças Tampa Vermelha (MLB3288536143, 0,71) — segundo ponto idêntico entre ciclos, mas ML não expõe série interna; só o terceiro ponto define direção e desbloqueia ação com Himmel
- ADS share 69,9%, ROAS 10,87x, ACOS 4,57%, gasto R$296,96 — segundo ponto consecutivo acima de 65%; terceiro ciclo é o gatilho de escalonamento a Kobe sobre dependência estrutural
- Breakdown de revenue_ads_yesterday_brl por platform_item_id segue pendente desde 22/05 — sem ele, não dá pra confirmar se ADS prioriza os dois Full em Padrão inferior ou as variações Cross-Docking líderes do dia (registrar como dado necessário do próximo pacote)
- Cluster IMB501 sustentou 44% do dia (37 pedidos): Tampa Preta Cross-Docking 20, Tampa Vermelha Full 10, Tampa Cinza Cross-Docking 7; tratar como bloco ajuda a explicar a inversão do mix sem fragmentar; estoque robusto nas variações Cross-Docking (8.375 e 9.195 unidades)
- ratings_negative=0,39 (39%) idêntico ao ciclo anterior em conta verde Gold; claims_rate=0,0025 em 50% do threshold de risco (0,005); sem breakdown por anúncio, hipótese de concentração nos dois Full em Padrão inferior segue em aberto — vira relevante se claims_rate subir acima de 0,005
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 un (MLB6739241224, Cross-Docking): 6 unidades pós-baixa com 2 pedidos no dia, cobertura ~3 dias com amostra pequena; checagem preventiva sem urgência, Budamix controla reposição em Cross-Docking
- MercadoLíder Platinum: progresso 81,34%, gap R$55.226,77, ETA 13,8 dias ao ritmo atual de R$4.012,89/dia; GMV de hoje (R$4.622,03) está acima do ritmo necessário — fora do gatilho de Slack, vira relevante se gap cair abaixo de R$30k com progresso acima de 90%

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

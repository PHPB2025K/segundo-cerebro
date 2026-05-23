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
_ingestido em 2026-05-23T10:27:27-03:00 BRT | confiança L05: baixa | insights L05: 1 (0 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Mercado Ads ficou em cerca de 69,9% do GMV, com ROAS aproximado de 10,9x e ACOS 4,57% — se repetir por mais 2 ciclos, vira sinal estrutural de dependência.
- Dois campeões Full seguem abaixo de health 0,80: Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo com 0,75 e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha com 0,71 — falta série temporal para saber direção.
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml ficou com 9 unidades pós-baixa no Full — checar reposição antes de interpretar queda futura como demanda fraca.
- Top 10 do dia ficou com 47,1% Full e 52,9% Cross-Docking, contra 73,7% Full no 30d — tratar como composição dos campeões, não decisão estrutural de modalidade de envio.
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta liderou o dia em Cross-Docking, mas não há distribuição horária por anúncio para explicar o pico.
- MercadoLíder Platinum segue fora do gatilho principal de Slack: progresso 81,34%, gap R$55.226,77 e ETA estimado de 13,8 dias; fica relevante quando gap cair abaixo de R$30k com progresso acima de 90%.
- Colisão de identidade entre os kits YW1050 continua pendente; sempre diferenciar 6 unidades e 10 unidades pelo nome com quantidade explícita.

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

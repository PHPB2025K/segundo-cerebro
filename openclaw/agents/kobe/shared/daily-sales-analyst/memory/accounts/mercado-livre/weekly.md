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
_ingestido em 2026-05-23T09:30:42-03:00 BRT | confiança L05: media | insights L05: 3 (0 fato, 3 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Segundo ciclo idêntico ao de 22/05: ADS share 69,9% (vs 69,8% antes), health de MLB4073003575 em 0,75 e MLB3288536143 em 0,71 inalteradas, ritmo Platinum sustentado — próximo ciclo é o terceiro e dispara (ou refuta) o gatilho de tese estrutural definido pela L01 (≥60% por 3 consecutivos + health <0,80 por mais 2 dias).
- MercadoLíder Platinum: progresso 81,34%, gap R$ 55.226,77, ETA ~13,8 dias ao ritmo de R$ 4.012,89/dia. Dia contribuiu R$ 609,14 acima do ritmo necessário — segundo ciclo positivo consecutivo. Monitorar se ritmo se mantém acima de R$ 3.800/dia.
- Pedido técnico ao data builder segue pendente: breakdown de revenue_ads_yesterday_brl por platform_item_id (pelo menos top 10) — necessário para separar 'Himmel deslocou foco' de 'orgânico Cross-Docking reagiu'.
- Pedido técnico ao data builder: série temporal de health (D-7 a D-1) para itens com penalização — cada ciclo só traz valor pontual, impossibilita atribuir direção.
- Há 5 anúncios em low_health fora do top 10 (total 7, dois visíveis no top 10) — cauda invisível com penalização orgânica que pode estar contribuindo silenciosamente. Pedir à L03 do próximo ciclo IDs específicos ou ranking de volume desses 5.
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades (Cross-Docking) com 6 unidades pós-baixa e cobertura prospectiva ~3 dias — monitoramento secundário; Cross-Docking em ruptura é menos crítico que Full.
- Colisão de display_name persistente: MLB4676726433 (KIT10YW1050, '10 Unidades') e MLB4676751119 (KIT6YW1050, '6 Unidades') — inconsistência para corrigir na fonte; diferenciador correto é quantidade no title ML.
- Mecanismo de dano por listagem: MLB3288536143 (Jogo Potes 5 Peças Claro — Tampa Vermelha) é Catálogo via catalog_product_id MLB44224272, então health=0,71 ameaça Buy Box; o outro campeão é Clássico e o risco é ranking de categoria — não confundir os dois mecanismos.

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

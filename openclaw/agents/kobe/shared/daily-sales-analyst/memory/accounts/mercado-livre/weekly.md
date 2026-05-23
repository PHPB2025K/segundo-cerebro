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
_ingestido em 2026-05-23T10:06:41-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Terceiro ciclo do gatilho estrutural: se ADS share ≥60% e health de Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo (MLB4073003575) e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (MLB3288536143) abaixo de 0,80 pelo terceiro dia consecutivo, tese de dependência estrutural de ADS se confirma — Yasmin abre alinhamento com Himmel sobre se a proporção ~70% é estratégia deliberada ou ausência de orgânico saudável
- MercadoLíder Platinum: progresso 81,34%, gap R$55.226,77, ETA ~13,8 dias ao ritmo R$4.012,89/dia — segundo ciclo consecutivo acima do ritmo necessário (~R$4.002/dia); alerta relevante quando gap cruzar abaixo de R$30k com progresso >90%; monitorar se ritmo se mantém acima de R$3.800/dia
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full, 9 unidades pós-baixa): registrar resultado da checagem de reposição de Yasmin — se não houver confirmação hoje, ruptura iminente amanhã; não interpretar queda de canecas nos próximos ciclos como movimento orgânico sem confirmar causa
- Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (MLB3288536143) é anúncio em Catálogo (catalog_product_id MLB44224272) com health=0,71 — mecanismo de dano é perda de Buy Box na página do catálogo, não simplesmente queda de ranking de categoria; monitorar separadamente dos outros campeões penalizados que são Clássicos (MLB4073003575, MLB4535865317, MLB4535865311)
- Pedido técnico ao data builder pendente há pelo menos 2 ciclos: breakdown de revenue_ads e spend por platform_item_id (top 5 a 10) — necessário para confirmar ou descartar hipótese de deslocamento de ADS para itens Cross-Docking sem penalização de health vs demanda orgânica espontânea
- Pedido técnico ao data builder pendente: série temporal de health D-7 a D-1 para MLB4073003575 (0,75) e MLB3288536143 (0,71) — 2 pontos consecutivos disponíveis são insuficientes para confirmar direção da penalização; dado crítico especialmente para MLB3288536143 (Catálogo)
- 5 anúncios com low_health fora do top 10 ainda invisíveis (total 7 confirmado, 2 identificados no top 10) — pedir à L03 do próximo ciclo IDs específicos ou volume estimado; podem compor o orgânico residual (~R$1.393 não atribuídos ao ADS) e indicar penalização orgânica mais ampla do que os dois campeões visíveis sugerem
- Colisão de display_name entre MLB4676726433 (Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades) e MLB4676751119 (Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades) pendente de correção na fonte — sempre diferenciar pelo sufixo de quantidade no title ML ao citar qualquer um dos dois

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

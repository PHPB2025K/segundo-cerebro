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
_ingestido em 2026-05-23T09:15:58-03:00 BRT | confiança L05: media | insights L05: 2 (0 fato, 2 hipótese/risco latente) | prioridades L05: 2_

**Memória para o próximo ciclo (da L05):**
- ADS share ponto zero da série: 69,8% (R$3.228,78 de R$4.622,03), ROAS 10,9x, ACOS 4,55% — registrar nos próximos 3 ciclos para confirmar se é padrão recorrente, valor estruturalmente alto ou comportamento atípico do dia.
- Health pontual registrado em 2026-05-22: MLB4073003575 (Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo, Full, health=0,75) e MLB3288536143 (Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha, Full, Catálogo, health=0,71) — solicitar série temporal D-7 a D-1 no próximo ciclo para confirmar ou refutar hipótese de erosão orgânica progressiva.
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full): verificar se reposição foi encaminhada em 2026-05-22; sem reposição, ruptura esperada em D+1 ou D+2 — registrar como variável confundidora se volume de canecas desaparecer do top 10 nos próximos dias.
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades (MLB6739241224, Cross-Docking): available_quantity=6 pós-baixa, cobertura prospectiva de ~3 dias — monitorar nos próximos 2 ciclos; Cross-Docking em ruptura é menos crítico que Full mas merece atenção.
- MLB6232315532 (Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida): único anúncio gold_pro + Catálogo + Full com health=null no top 10; sold_quantity acumulado 160 — monitorar migração de health=null para valor calculado; se vier abaixo de 0,85, perda de Buy Box é imediata.
- MercadoLíder Platinum: progresso 81,34%, gap R$55.227, ETA ~13,8 dias ao ritmo de R$4.013/dia. Dia de R$4.622 ficou R$609 acima do ritmo necessário — contribuição positiva. Monitorar se ritmo diário se mantém acima de R$3.800 nos próximos dias.
- Solicitação técnica ao data builder: incluir breakdown de revenue_ads por platform_item_id no próximo ciclo (pelo menos top 10 itens) para confirmar ou refutar hipótese de priorização ADS Cross-Docking vs Full com health degradada.
- Colisão de display_name registrada: KIT6YW1050 (MLB4676751119, Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades) e KIT10YW1050 (MLB4676726433, Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades) compartilham o mesmo alias interno — registrar como inconsistência a corrigir na fonte; diferenciador correto: '6 Unidades' vs '10 Unidades' no título ML e no platform_item_id.

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*

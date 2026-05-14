<!-- llm_used=true model=sonnet fallback=false -->
Preciso de permissão para editar o arquivo `03-operacional.md`. Por favor, aprove a operação de escrita.

Enquanto isso, aqui está a análise operacional completa produzida:

---

### Leitura operacional do dia

- O dia operou com volume e ticket simultaneamente acima do baseline — 46 pedidos contra média de ~27 (60d) e ticket R$ 49,10 contra R$ 39,21 estável em 30d/60d — confirmando o duplo efeito identificado pela Estratégica: o GMV não foi puxado apenas por volume, mas por composição de pedido mais cara, concentrada em kits e conjuntos.

- O resultado se sustentou em FBA 100%, sem fragmentação de fulfillment — operacionalmente isso elimina qualquer ruído de modalidade de entrega como variável explicativa. Execução logística do dia foi limpa.

- A distribuição de produtos mostra dependência nos dois clusters líderes: Jarra Medidora (13 unidades) e Potes de Vidro em três variações (20 unidades) respondem por 33 das 64 unidades vendidas — mais da metade do volume de itens. Isso confirma a observação estratégica de que o ticket elevado é compatível com mix de kits, não expansão de base.

- Cancelamentos (2 em 46) são operacionalmente irrelevantes neste dia — sem indicação de concentração em produto específico visível no pacote.

---

### Sinais operacionais relevantes

- **Sinal:** horário de vendas distribuído ao longo do dia, com pico em 14h (6 pedidos) e atividade também às 9h, 16h, 20h e 22h — **interpretação operacional:** ausência de concentração em janela noturna típica de ADS agressivo; distribuição diurna sugere tráfego mais orgânico ou alcance amplo, mas não descarta ADS sem dado de origem.

- **Sinal:** presença do Suporte Gamer (SPC002, 6 unidades) no top 5 de um dia dominado por utensílios de cozinha — **interpretação operacional:** produto fora do core aparece com força em dia de spike — pode indicar exposição algorítmica ampliada; se recorrente, muda o perfil de mix da conta; se pontual, foi beneficiado pelo mesmo evento que puxou os demais.

- **Sinal:** top 3 em 51.6% e top 5 em 70.3%, com ~30% de contribuição na cauda — **interpretação operacional:** a concentração não é anormalmente alta para Amazon, mas a dependência real está em dois clusters (Jarra + família Potes), não em distribuição genuinamente ampla; adiciona evidência à hipótese estratégica de ticket subindo por composição de kits.

- **Sinal:** Buy Box e cobertura de estoque FBA dos ASINs líderes **ausentes do pacote** — **interpretação operacional:** dado que separa demanda de capacidade operacional, conforme regra explícita da conta; sem ele, não é possível afirmar que o volume reflete demanda estável e captável.

---

### Anomalias ou ausência de anomalia

**Inconclusivo por falta de dado.**

O volume e GMV estão ~2x o baseline de 60d — anomalia estatística clara. Mas identificar se é causa operacional (listing reativado, promoção ativa) ou externa (boost algorítmico) exigiria dados ausentes. Weekly e monthly estão vazios, daily de 12/05 não está no contexto. Não há anomalia *negativa* identificável: reconciliação ok, FBA funcionando, cancelamentos irrelevantes. Mas afirmar "execução dentro do padrão histórico" seria afirmar normalidade sobre base inexistente.

O que mudaria o nível: causa do spike identificada (para cima se Buy Box instável; para baixo se promoção documentada com FBA estável nos líderes).

---

### O que precisa ser investigado pela Granular

- **Pergunta:** os 2 cancelamentos estão concentrados em qual ASIN ou em produtos distintos? — **motivada por:** concentração em produto-campeão teria interpretação diferente de cancelamentos pulverizados.

- **Pergunta:** qual era o status de Buy Box da Jarra Medidora (B0G2CWWMGK) e dos Potes de Vidro (B0GSWLK5F3 + variações) em 13/05? — **motivada por:** ausência de dado de Buy Box no pacote, combinada com regra explícita de não interpretar crescimento como positivo sem validar Buy Box dos ASINs líderes.

- **Pergunta:** há registro de campanha ADS ativa ou promoção de listing em 13/05? — **motivada por:** distribuição de horário não aponta ADS noturno, mas não exclui ADS diurno; sem causa, os próximos dias ficam sem âncora interpretativa.

- **Pergunta:** o Suporte Gamer (SPC002) teve comportamento normal ou atípico em dias anteriores? — **motivada por:** produto fora do core apareceu com 6 unidades em dia de spike; se tendência nascente, muda o mix da conta.

---

### Destaque para a Condensadora

O fato operacional mais importante não é o crescimento em si — é que ele veio por dupla alavanca (volume e ticket simultaneamente), sustentado por FBA sem fricção, mas com o dado mais crítico para qualquer decisão de continuidade ausente: Buy Box e cobertura de estoque FBA dos dois ASINs líderes. O risco silencioso é normalizar esse dia como nova referência antes de confirmar que a capacidade operacional sustenta a demanda observada. A Condensadora deve destacar que o dia foi forte *e* condicionado — não há base para comunicar crescimento sem a ressalva de que a validação operacional ainda está pendente com Leonardo.
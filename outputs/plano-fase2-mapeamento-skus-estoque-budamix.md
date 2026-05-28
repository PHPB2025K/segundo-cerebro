# Plano — Fase 2: Mapeamento completo de SKUs do motor de estoque

**Projeto:** Motor de gestão de estoque — Budamix Central / Estoque Budamix  
**Objetivo:** transformar o motor de estoque de “detecta divergência” para “resolve SKU com segurança e aplica somente quando houver confiança operacional”.

---

## 1. Estado atual

A auditoria atual mostrou que a etapa de mapeamento ainda não está pronta para automação confiável.

### Diagnóstico

- A tabela `sku_aliases` está vazia.
- A tabela `kit_bom` está vazia.
- O sistema reconhece aproximadamente 93 SKUs a partir da aba `ESTOQUE`.
- Foram encontrados 567 SKUs únicos divergentes.
- Houve 962 divergências recentes por “SKU não encontrado”.
- A maioria das divergências vem de eventos de `ENVIOS FULL`.

### Conclusão

O motor existe, mas o mapeamento de SKUs ainda está praticamente não implementado. Sem essa etapa, qualquer automação real vai gerar divergência em massa.

---

## 2. Objetivo da etapa

Criar uma camada confiável de resolução de SKUs para que o motor consiga:

1. Reconhecer SKUs oficiais da aba `ESTOQUE`.
2. Resolver aliases de marketplace, Full, equipe e histórico.
3. Decompor kits e combos em componentes reais.
4. Bloquear automaticamente qualquer SKU ambíguo, desconhecido ou inseguro.
5. Aplicar baixa/entrada somente quando a resolução for determinística.

---

## 3. Fontes de verdade

A etapa deve consolidar as seguintes bases:

### 3.1 Planilha ESTOQUE

Fonte oficial de saldo final e SKUs base.

Usos:

- Validar se um SKU resolvido existe.
- Identificar produto, marca e linha.
- Atualizar saldo final somente depois que o movimento for validado.

### 3.2 Ledger de movimentos divergentes

Fonte real do que o sistema está recebendo hoje.

Usos:

- Priorizar SKUs por frequência.
- Identificar padrões de erro.
- Encontrar kits, aliases e SKUs inexistentes.

### 3.3 ENVIOS FULL

Principal fonte atual de divergências.

Usos:

- Identificar SKUs usados nas planilhas de Full.
- Mapear transferências de galpão para Full.
- Separar transferência de estoque de venda real.

### 3.4 Marketplaces

Fontes: Mercado Livre, Shopee e Amazon.

Usos:

- Cruzar SKU de anúncio com SKU interno.
- Resolver variações.
- Identificar anúncios compostos, kits e combos.

### 3.5 Kits e combos

Fonte estrutural para baixas corretas.

Usos:

- Decompor kits homogêneos.
- Decompor kits mistos.
- Bloquear kits sem composição cadastrada.

---

## 4. Etapa 1 — Inventário único de SKUs recebidos

Criar uma tabela temporária de análise contendo todos os SKUs divergentes recentes.

Campos recomendados:

- `sku_recebido`
- `origem`
- `frequencia`
- `existe_na_estoque`
- `produto_na_estoque`
- `tipo_detectado`
- `status_mapeamento`
- `acao_recomendada`

Classificações iniciais:

- `sku_direto`
- `alias_simples`
- `kit_homogeneo`
- `kit_misto`
- `sku_nao_cadastrado`
- `descontinuado_ou_lixo`
- `ambíguo`

Entrega desta etapa:

- Ranking dos SKUs divergentes por frequência.
- Separação por família de produto.
- Lista curta de decisões humanas necessárias.

---

## 5. Etapa 2 — Classificação dos SKUs divergentes

Classificar os 567 SKUs únicos divergentes em grupos operacionais.

### 5.1 Bate direto

SKU recebido já existe na aba `ESTOQUE`.

Ação:

- Marcar como resolvido direto.
- Não criar alias desnecessário.

### 5.2 Alias simples

SKU recebido não existe, mas aponta claramente para um SKU base.

Exemplos:

- SKU com sufixo operacional.
- SKU antigo de marketplace.
- SKU de canal específico.
- Nome interno usado pela equipe.

Ação:

- Inserir em `sku_aliases`.
- Definir nível de confiança.

### 5.3 Kit homogêneo decomponível

SKU representa múltiplas unidades de um único componente.

Exemplo:

- `KIT2YW1520RC_T` → 2 × `YW1520RC`
- `KIT4YW800SQ_T` → 4 × `YW800SQ_T`

Ação:

- Inserir em `kit_bom`.
- Marcar como elegível para automação depois de validado.

### 5.4 Kit composto real

SKU representa componentes diferentes.

Exemplos:

- kit colorido de canecas;
- combo misto;
- kit promocional com produtos diferentes.

Ação:

- Criar BOM item a item.
- Exigir validação humana antes de automação.

### 5.5 SKU não cadastrado

Produto parece real, mas não existe na aba `ESTOQUE`.

Ação:

- Avaliar se deve ser cadastrado.
- Se sim, criar linha oficial na aba `ESTOQUE` antes de liberar baixa.

### 5.6 SKU lixo ou descontinuado

SKU não deve ser mapeado.

Ação:

- Marcar como rejeitado/bloqueado.
- Registrar motivo.

---

## 6. Etapa 3 — Popular `sku_aliases`

A tabela `sku_aliases` deve conter apenas mapeamentos seguros.

### Campos necessários

- `alias_raw`
- `sku`
- `confidence`
- `source`
- `active`
- `notes`

### Regras

- Alias sempre aponta para um SKU oficial da aba `ESTOQUE`.
- Alias ambíguo não pode aplicar automático.
- Alias com baixa confiança deve ficar pendente.
- Alias descontinuado deve ficar inativo, não apagado.

### Níveis de confiança

- `0.95–1.00`: confiança alta, elegível para automação.
- `0.70–0.94`: confiança média, exige validação inicial.
- `<0.70`: confiança baixa, apenas alerta.

Entrega:

- `sku_aliases` preenchida com aliases reais.
- Relatório de aliases ambíguos.
- Lista de aliases rejeitados/descontinuados.

---

## 7. Etapa 4 — Popular `kit_bom`

Nenhum kit deve gerar baixa automática sem BOM.

### Campos necessários

- `kit_sku`
- `component_sku`
- `component_qty`
- `active`
- `valid_from`
- `valid_to`
- `notes`

### Regras

- Todo componente precisa existir na aba `ESTOQUE`.
- Kit homogêneo pode ser automatizado antes.
- Kit misto precisa de validação mais rigorosa.
- Kit descontinuado deve ficar inativo.

### Prioridade

1. Kits mais frequentes nas divergências.
2. Kits de potes.
3. Kits de panos.
4. Kits de canecas.
5. Kits MDF.
6. Combos promocionais e mistos.

Entrega:

- BOM preenchido para os kits ativos mais recorrentes.
- Kits sem composição clara ficam bloqueados.
- Relatório de cobertura da BOM.

---

## 8. Etapa 5 — Criar o resolvedor único de SKU

O motor precisa ter uma função central de resolução, usada por todas as origens.

### Ordem de resolução

1. Tentar SKU direto na aba `ESTOQUE`.
2. Tentar alias em `sku_aliases`.
3. Tentar kit em `kit_bom`.
4. Se for kit sem BOM, bloquear como divergente.
5. Se alias for ambíguo, mandar para pendência.
6. Se SKU não existir, marcar como divergente.
7. Se saldo for insuficiente, bloquear.
8. Aplicar somente quando o resultado for determinístico.

### Saída esperada do resolvedor

Para cada evento, retornar:

- `status_resolucao`
- `sku_original`
- `sku_resolvido`
- `componentes`
- `confidence`
- `motivo_bloqueio`
- `pode_aplicar_automatico`

Entrega técnica:

- Função única de resolução de SKU.
- Uso obrigatório por:
  - operações manuais;
  - ENVIOS FULL;
  - marketplace;
  - futuras entradas/devoluções.

---

## 9. Etapa 6 — Reprocessamento em modo simulação

Antes de aplicar qualquer saldo, reprocessar a amostra divergente em modo sombra.

### Métricas

- Total de movimentos analisados.
- SKUs resolvidos direto.
- SKUs resolvidos por alias.
- SKUs resolvidos por BOM.
- Kits bloqueados por falta de BOM.
- SKUs realmente desconhecidos.
- Divergências remanescentes.

### Meta mínima

- Reduzir “SKU não encontrado” para menos de 5–10% da amostra real.
- Garantir 0 kit aplicado sem BOM.
- Garantir 0 alias ambíguo aplicado automaticamente.

Entrega:

- Relatório comparativo antes/depois.
- Lista final de pendências humanas.

---

## 10. Etapa 7 — Validação com Pedro/equipe

Não enviar centenas de linhas para decisão manual. A validação deve ser agrupada por família.

### Agrupamentos

- Potes
- Panos
- Canecas
- MDF
- Importados antigos
- Kits
- Desconhecidos
- Descontinuados/lixo

### O que pedir validação humana

- SKUs que parecem produto real mas não estão na aba `ESTOQUE`.
- Kits sem composição clara.
- Nomes coloquiais usados pela equipe.
- Produtos que podem estar descontinuados.
- SKUs duplicados ou ambíguos.

Entrega:

- Lista curta de decisões.
- Aplicação das decisões em `sku_aliases` e `kit_bom`.

---

## 11. Etapa 8 — Modo sombra operacional

Rodar por 2–3 dias sem automação plena.

### O motor deve

- Resolver SKUs.
- Criar movimento normalizado.
- Simular aplicação.
- Comparar com saldo da planilha.
- Alertar somente divergências relevantes.

### Relatório diário

- Movimentos recebidos.
- Movimentos resolvidos.
- Movimentos aplicáveis.
- Movimentos bloqueados.
- Motivos de bloqueio.
- Novos SKUs não mapeados.

Entrega:

- Prova de confiabilidade antes da automação.

---

## 12. Etapa 9 — Liberação gradual

Ordem recomendada de liberação:

### 12.1 ENVIOS FULL simples

Critérios:

- SKU direto ou alias de alta confiança.
- Sem kit.
- Saldo suficiente.

### 12.2 Kits homogêneos com BOM

Critérios:

- BOM validado.
- Componentes existem na aba `ESTOQUE`.
- Sem ambiguidade.

### 12.3 Marketplaces simples

Critérios:

- Pedido confirmado.
- Não cancelado.
- SKU direto ou alias confiável.
- Não kit.

### 12.4 Kits mistos

Critérios:

- BOM auditado.
- Componentes corretos.
- Histórico sem divergências.

### 12.5 Entradas e devoluções

Devem ficar para fase assistida, não para automação plena nesta etapa.

---

## 13. Critério de conclusão da etapa

A etapa de mapeamento completo só deve ser considerada concluída quando:

- `sku_aliases` estiver preenchida e validada.
- `kit_bom` estiver preenchida para todos os kits ativos relevantes.
- O resolvedor único estiver implementado e usado pelas rotas do motor.
- As divergências históricas forem reprocessadas em simulação.
- “SKU não encontrado” cair para menos de 5–10% da amostra real.
- Nenhum kit for aplicado sem BOM.
- Nenhum alias ambíguo for aplicado automaticamente.
- O deploy vivo responder corretamente às rotas da Fase 2.
- Houver relatório de cobertura por família de produto.

---

## 14. Ordem executiva recomendada

1. Extrair os 567 SKUs divergentes únicos.
2. Priorizar por frequência.
3. Cruzar contra aba `ESTOQUE`.
4. Classificar em direto, alias, kit, desconhecido, lixo.
5. Popular `sku_aliases` para casos óbvios.
6. Popular `kit_bom` para kits homogêneos mais frequentes.
7. Gerar lista curta de decisões humanas.
8. Implementar resolvedor único no motor.
9. Reprocessar amostra em modo simulação.
10. Corrigir divergências restantes.
11. Rodar 2–3 dias em modo sombra.
12. Liberar automação por grupos seguros.

---

## 15. Recomendação final

Atacar primeiro os SKUs divergentes por frequência, não tentar mapear o catálogo inteiro no escuro.

Isso resolve a dor real mais rápido, reduz divergência em massa e evita cadastrar alias/BOM inúteis.

A prioridade imediata deve ser:

1. Top SKUs divergentes de ENVIOS FULL.
2. Kits homogêneos óbvios.
3. Aliases simples para SKUs da aba `ESTOQUE`.
4. Lista curta de SKUs desconhecidos para decisão humana.

Só depois disso faz sentido liberar automação real da Fase 2.

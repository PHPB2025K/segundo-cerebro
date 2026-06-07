# Estoque — Mapeamento retroativo dos divergentes

Data: 2026-06-07
Escopo: divergências de marketplace/WhatsApp Estoque a partir de 2026-06-02, com foco nos resíduos citados na auditoria de 05/06 e divergentes novos até 07/06.

## Princípio usado

Não classificar todos os divergentes como “erro”. O mapeamento separa:

1. **Cadastro/alias/BOM corrigível** — SKU vendido é identificável com segurança e existe SKU canônico equivalente.
2. **Saldo físico insuficiente** — SKU está mapeado certo, mas o motor bloqueou por falta de saldo; não deve baixar negativo.
3. **Fantasma/cadastro pendente** — SKU aparece em marketplace, mas não existe no catálogo de estoque nem há equivalente seguro.
4. **Dado mutável de marketplace** — pedido atual já mostra SKU diferente do SKU capturado no movimento; exige snapshot/fix de trilha antes de reprocessar.

## Resultado executivo

A maior parte das divergências recentes não é problema de SKU: é falta de saldo físico para itens que o sistema já resolveu corretamente.

- **Correção segura de alias/cadastro:** 4 famílias pequenas.
- **Ruptura/saldo insuficiente real:** canelada preta, canelada azul, pote 1050/1520 laranja, reta branca/rosa e parte das tulipas pretas antigas.
- **Não baixar na marra:** principalmente `CAC250P`, `YW1520RC`, `YW1050RC`, `CAR200B`, `CAR200R`.

## Mapa por item/família

### 1. `CK4742_B2` → `CK4742_B` — seguro

Evidência:
- Pedido ML `2000016779647294`.
- SKU vendido: `CK4742_B2`.
- Título: “Jarra Medidora De Vidro Budamix 500ml Com Alça Ergônomica”.
- Quantidade vendida: 1.
- Já existe alias ativo/canônico para `CK4742_B`.
- Já existe BOM para `KIT2CK4742_B` = 2× `CK4742_B`, mas este caso **não é kit 2**, porque o título e preço apontam 1 unidade.

Ação recomendada:
- Criar alias `CK4742_B2` → `CK4742_B`.
- Reprocessar o movimento divergente de 04/06.

Risco: baixo.

### 2. `914C_B2` → `914C_B` — seguro

Evidência:
- Pedido ML `2000016787141852` em 05/06 e `2000016815981844` em 07/06.
- SKU vendido: `914C_B2`.
- Título: “Kit 6 Canequinhas Para Café 100ml Com Suporte De Madeira...”.
- Quantidade vendida: 1 kit.
- `914C` e `914C_BB` já mapeiam para `914C_B`.
- `914C_B2` não deve virar 2 unidades; o sufixo `_B2` aqui parece variante/listing, não fator de kit.

Ação recomendada:
- Criar alias `914C_B2` → `914C_B`.
- Reprocessar 2 movimentos divergentes.

Risco: baixo.

### 3. `KITIMB501P_T` → `IMB501P_T` — seguro

Evidência:
- Pedido ML `2000016796175616`.
- Título: “Conjunto De 5 Potes Mantimentos Marmita - Budamix Preto”.
- Quantidade: 1.
- Já existem aliases equivalentes: `IMB501PT` → `IMB501P_T` e mapeamentos dos kits/combos IMB501 no e-commerce.
- Já existem aliases `KITIMB501C_T` e `KITIMB501V_T`; falta só a variação preta.

Ação recomendada:
- Criar alias `KITIMB501P_T` → `IMB501P_T`.
- Reprocessar o movimento divergente de 05/06.

Risco: baixo.

### 4. `XCP004` → provável `COLORS170_B` — provável, mas exige cautela

Evidência:
- Movimento divergente Shopee 06/06 capturou `XCP004`.
- O pedido atual da Shopee para o mesmo order id mostra SKU `XCP002`.
- Título atual: “Jogo 6 Xícaras de Café e Chá Porcelana 170ml Coloridas...”
- `XCP002` já mapeia para `COLORS170_B`.

Interpretação:
- Pode ser SKU mutável/variação alterada entre snapshot e consulta atual.
- O produto parece a mesma família colorida 170ml, mas como houve divergência entre SKU capturado e SKU atual, não aplicar sem snapshot/validação.

Ação recomendada:
- Validar se `XCP004` é outra variação do mesmo kit colorido 170ml.
- Se confirmado, criar alias `XCP004` → `COLORS170_B`.
- Em paralelo, persistir snapshot de SKU usado no momento do cron para evitar esse ruído retroativo.

Risco: médio.

### 5. `KFJ003` — não mapear ainda

Evidência:
- Pedido ML `2000016814090866`.
- Título: “Kit Ferramentas Jardinagem 3pç Plástico Budamix Marrom”.
- SKU vendido: `KFJ003`.
- Não encontrei equivalente seguro já cadastrado em aliases/BOMs.

Ação recomendada:
- Consultar se `KFJ003` deve existir no estoque físico ou se é SKU fantasma/listing antigo.
- Se existir: cadastrar SKU canônico ou alias correto.
- Se não existir: tratar como venda de item fora da base operacional atual e corrigir cadastro marketplace.

Risco: alto para automapear.

### 6. `YW1520RC` e `YW1050RC` — saldo insuficiente real

Evidência:
- Vários movimentos de ML/Shopee para `KIT2YW1520`, `KIT6S100`, `KIT9S101`, `101` e kits correlatos.
- BOMs já resolvem corretamente para `YW1050RC` e `YW1520RC`.
- O erro recorrente é “estoque insuficiente atual 0”, não “SKU desconhecido”.
- Em 31/05 já restavam registros por falta de `YW1520RC`; em 04–07/06 o padrão continuou.

Ação recomendada:
- Não criar alias novo.
- Não baixar negativo.
- Verificar fisicamente se houve entrada de potes laranja 1050/1520 não registrada.
- Se houve entrada real antes das vendas: lançar entrada retroativa com `business_date` correto e reprocessar.
- Se não houve: é ruptura/saldo real e o marketplace vendeu sem cobertura no motor.

Risco: alto se forçar baixa.

### 7. `CAC250P` e `CAC250AZ` — saldo insuficiente real / entrada faltante provável

Evidência:
- `K6CAN250P` e `K6CAN250AZ` já resolvem corretamente para `CAC250P` e `CAC250AZ`.
- Divergências são por estoque insuficiente, não por mapeamento.
- `CAC250P` acumulou volume divergente alto; `CAC250AZ` ficou menor, mas também insuficiente.
- A entrada “Canecas Guinho” resolveu `TL250P` e alguns aliases de canecas, mas não trouxe entrada suficiente para canelada preta/azul.

Ação recomendada:
- Procurar entrada física/WhatsApp de canelada preta e azul não processada.
- Se a mercadoria entrou antes das vendas, lançar entrada retroativa e reprocessar.
- Se não entrou, manter como ruptura/saldo insuficiente.

Risco: alto se forçar baixa.

### 8. `TL250P` — parcialmente resolvido, resíduo antigo por data operacional

Evidência:
- A entrada “Canecas Guinho” em 04/06 resolveu o bloco principal de `TL250P`.
- A auditoria de 06/06 aplicou entrada `TL250P +55` com business date 05/06.
- Ainda aparecem divergências antigas de 02–03/06 e uma divergência WhatsApp de 03/06.

Interpretação:
- Não é falta de alias; é saldo/data operacional.
- Entrada de 05/06 não deve, por padrão, cobrir venda de 02/06 se a mercadoria não estava fisicamente disponível antes.

Ação recomendada:
- Só reprocessar 02–03/06 se houver prova de entrada física anterior ou erro de data na mensagem original.

Risco: médio/alto se reprocessar fora da cronologia real.

### 9. `CAR200B` e `CAR200R` — novo alerta de saldo insuficiente

Evidência:
- Divergências em 06–07/06 para `KIT6CAR200`, `KIT6CAR200B` e componentes `CAR200B`/`CAR200R`.
- A regra de kit colorido já está correta: 1 unidade de cada cor.
- O erro é saldo insuficiente, não mapeamento.

Ação recomendada:
- Verificar se houve entrada de Reta branca/rosa não registrada.
- Se sim, entrada retroativa e reprocessamento; se não, ruptura.

Risco: alto se baixar negativo.

## Ações aplicáveis com segurança após autorização

1. Criar alias `CK4742_B2` → `CK4742_B`.
2. Criar alias `914C_B2` → `914C_B`.
3. Criar alias `KITIMB501P_T` → `IMB501P_T`.
4. Reprocessar apenas os movimentos desses três grupos.

Potencial de limpeza imediata: 4 movimentos divergentes recentes.

## Ações que precisam validação antes

1. Confirmar `XCP004` → `COLORS170_B`.
2. Confirmar se `KFJ003` existe fisicamente/canonicamente.
3. Confirmar entradas físicas não registradas para:
   - `CAC250P`
   - `CAC250AZ`
   - `YW1520RC`
   - `YW1050RC`
   - `TL250P` antes de 03/06
   - `CAR200B`
   - `CAR200R`

## Conclusão

O mapeamento retroativo mostra que o problema sistêmico de resolver SKU/BOM está majoritariamente corrigido. O gargalo agora é outro: **saldo físico/entrada operacional não registrada**.

Se o objetivo for limpar a fila sem distorcer estoque, o caminho correto é:

1. Aplicar só os aliases seguros.
2. Reprocessar esses poucos movimentos.
3. Tratar o restante como investigação de entrada física, não como correção de mapeamento.
4. Proibir baixa negativa automática.

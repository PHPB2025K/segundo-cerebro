# Investigação saldo fiscal — YW1050 / YW1520 / YW800SQ

Data: 2026-05-01

## Fontes consultadas

- Bling Matriz/Filial, leitura apenas:
  - Transferências pré-março: NF 000598, NF 000600
  - NFs internas março: Filial 000028, 000029, 000030; Matriz 000617, 000618, 000619
  - Abril: 000648 entrada GB25011, 000649 transferência GB25011, 000653 transferência GB25010
- PDFs inbound:
  - `SC_GB25010---ac451e38-9178-4ea1-bffa-7e1fc4fd04e7.pdf`
  - `SC_GB25011_2---e17e1d98-1a10-4833-bcfd-1561bf93851f.pdf`
- Mapas/reconciliações prévios:
  - `tmp/sku_fiscal_map_abril_2026_v5_sem_ck4742.csv`
  - `tmp/reconciliacao_fiscal_abril_componentes_v4.csv`

## Achado principal

A reconciliação anterior subcontava entradas/transferências porque tratava várias linhas fiscais em CX como unidade.

Regra corrigida para movimento fiscal de entrada/transferência:

- `CX c/N pcs` => quantidade NF × N peças
- `CX c/N conj` + SKU kit => quantidade NF × N conjuntos por caixa × peças do kit
- GB25010 NF 000653 usa unidade `CX`; fatores confirmados no PDF:
  - YW1050RC: 12 un/CX
  - YW1520RC: 12 un/CX
  - YW800SQ: 12 un/CX
  - YW640RC: 24 un/CX
  - YW320SQ: 24 un/CX
  - YW520SQ: 24 un/CX

## Tabela recalculada

| Componente | Transferência março p/ Filial | Retenção Matriz março inferida 10% | Saída março Filial | Saída março Matriz | Saldo inicial abril Filial | Saldo inicial abril Matriz | Entradas abril Matriz | Transferências abril Filial | Retenção abril Matriz | Vendas abril total | Pode NF Filial | Excedente Matriz | Bloqueado | Saldo final Matriz | Saldo final Filial |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| YW1050 | 1.992 | 221 | 580 | 0 | 1.412 | 221 | 4.776 | 4.268 | 508 | 1.619 | 1.619 | 0 | 0 | 729 | 4.061 |
| YW1520 | 1.984 | 220 | 900 | 883 | 1.084 | -663 | 3.336 | 2.988 | 348 | 1.655 | 1.655 | 0 | 0 | -315 | 2.417 |
| YW800SQ | 1.752 | 195 | 576 | 394 | 1.176 | -199 | 4.788 | 4.272 | 516 | 202 | 202 | 0 | 0 | 317 | 5.246 |

## Diagnóstico por componente

### YW1050

Status: resolvido para abril.

Causa do bloqueio anterior: conversão errada. A reconciliação anterior não multiplicava corretamente as caixas/conjuntos das NFs fiscais.

Classificação: (c) conversão errada.

Resultado corrigido:
- Sem bloqueio.
- NF de abril pode sair 100% pela Filial para as vendas de YW1050.
- Saldo final positivo em Matriz e Filial.

### YW800SQ

Status: resolvido para abril, mas com alerta histórico.

Causa do bloqueio anterior: conversão errada nos movimentos fiscais, especialmente caixas/conjuntos de 000598, 000648, 000649 e 000653.

Também havia consumo Matriz em março acima da retenção 10% inferida: saldo inicial abril Matriz ficou -199. A retenção de abril (+516) recompõe e fecha saldo final Matriz +317.

Classificação:
- (c) conversão errada para o bloqueio abril.
- (d) consumo Matriz acima da retenção inferida em março, mas recomposto em abril.

Resultado corrigido:
- Sem bloqueio para NF abril.
- NF de abril pode sair 100% pela Filial para vendas de YW800SQ.

### YW1520

Status: sem bloqueio para NF Filial de abril, mas com inconsistência fiscal histórica na Matriz.

Causa:
- Conversão anterior estava errada e isso explicava parte do bloqueio.
- Mesmo corrigindo conversões, a Matriz fica negativa porque março teve saída Matriz de 883 un (NFs 617-619) contra retenção inferida de 220 un da transferência 000598.
- Isso indica consumo Matriz acima da retenção 10% inferida ou existência de entrada/saldo fiscal anterior não capturado nas NFs disponíveis.

Classificação:
- (c) conversão errada para a prévia anterior.
- (d) consumo indevido/extraordinário em março OU (b) entrada/saldo anterior omitido para explicar Matriz.

Resultado corrigido:
- As vendas abril de YW1520 podem ser cobertas pela Filial: 1.655 vendidas vs 1.084 saldo inicial Filial + 2.988 transferidas abril.
- Porém a Matriz termina com -315 se mantivermos apenas as fontes fiscais disponíveis.

## NFs/entradas omitidas encontradas

- Não foi encontrada outra NF de transferência março/abril relevante além de 000598, 000600, 000649 e 000653.
- No Bling Matriz, tipo entrada em 2026 relevante encontrada: 000648 (registro da Open Trade 580012 / GB25011).
- A entrada Open Trade 580119 / GB25010 não está registrada no Bling como NF de entrada tipo 0; foi inferida pela NF 000653 e confirmada pelo PDF inbound.

## Conclusão operacional

Com a correção dos fatores fiscais de caixa/conjunto:

- YW1050: liberado para prévia Filial.
- YW800SQ: liberado para prévia Filial.
- YW1520: liberado para prévia Filial de abril, mas exige ressalva/ajuste histórico da Matriz por saldo negativo remanescente.

Ainda não recomendo emitir/rascunhar Bling automaticamente até Pedro decidir como tratar o saldo histórico negativo da Matriz em YW1520 (-315):

1. aceitar como ajuste histórico de março/documentar, ou
2. localizar entrada/saldo anterior fora das NFs 598/600, ou
3. reclassificar parte da saída Matriz março como uso extraordinário/excedente não modelado pelo 90/10.

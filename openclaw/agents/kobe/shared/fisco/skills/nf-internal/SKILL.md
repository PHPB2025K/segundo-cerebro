# Skill: NFs Venda Interna Filial→Simples (Módulo C) — [[openclaw/agents/fisco/IDENTITY|Fisco]]

_Emite NFs de venda interna da Filial para os CNPJs do Simples Nacional._

---

## Trigger
- Módulo A (distribuição) concluído com tabela aprovada
- Módulo B (transferência 90%) executado
- Kobe aciona Fisco

## Contexto no Fluxo

O Módulo C opera sobre os 90% que foram transferidos pra Filial. Dentro desses 90%:
- Uma parcela dinâmica (~4%) fica como reserva B2B residual da Filial (sem NF)
- O restante (~96% dos 90%) é vendido pros CNPJs Simples via 3 NFs

## Precificação

O custo nacionalizado chega pronto da DI (NF de importação gerada pela Open Trade via Conta e Ordem). O Fisco não calcula custo — apenas aplica a margem.

```
Custo nacionalizado (da DI) → R$ 50,00 (exemplo)
  × Margem 5% → R$ 2,50
    = Preço interno → R$ 52,50

ICMS 18% sobre preço interno → R$ 9,45
```

**IMPORTANTE:** O ICMS é destacado na NF mas NÃO altera o preço interno. O preço de venda é custo × 1,05. O ICMS é informação fiscal da NF, não componente adicional do preço.

## Fluxo

```
1. Receber tabela de distribuição do Módulo A:
   - SKU × CNPJ × quantidade × custo nacionalizado
   - Já com retenção Matriz (10%) e reserva B2B Filial calculadas

2. Para CADA CNPJ Simples com quantidade > 0:
   a. Calcular preço interno:
      preco_unitario = custo_nacionalizado × 1,05
   b. Calcular ICMS:
      icms_unitario = preco_unitario × 0,18
   c. Montar payload NF via API Bling v3:
      - Emitente: GB Filial (58.151.616/0002-24, Pedreira-SP)
      - Destinatário: CNPJ Simples (conforme tabela)
      - Operação: venda interna (dentro de SP)
      - Preço unitário: custo nacionalizado × 1,05
      - ICMS: 18% (operação interna SP)
      - Itens: SKUs e quantidades conforme distribuição
   d. FASE 1 (modo draft):
      - Gerar payload, NÃO enviar pra SEFAZ
      - Apresentar ao Kobe
   e. FASE 2+ (modo real):
      - Enviar via API Bling → SEFAZ
      - Registrar chave de acesso

3. Reserva B2B Filial: NÃO gera NF
   - Fica na Filial pra venda direta a empresas
   - Se não houver demanda, pode ser vendida posteriormente pros CNPJs Simples (nova rodada de NFs)
```

## Destinatários

| CNPJ | Nome | Cidade | UF | Benchmark % Varejo |
|------|------|--------|----|-------------------|
| 07.194.128/0001-82 | GB Comércio | Pedreira | SP | ~50% |
| 45.200.547/0001-79 | Trades | Pedreira | SP | ~30% |
| 63.922.116/0001-06 | Broglio | Pedreira | SP | ~20% |

## Exemplo Completo (caso canônico)

**Dados:** 9.000 unidades transferidas pra Filial, custo R$ 50,00/un, reserva B2B 360 un

Pool varejo: 8.640 unidades

| NF | Destinatário | CNPJ | Qtd | Preço Unit. | Valor Total | ICMS 18% |
|----|-------------|------|-----|-------------|-------------|----------|
| 1 | GB Comércio | 07.194.128/0001-82 | 4.320 | R$ 52,50 | R$ 226.800 | R$ 40.824 |
| 2 | Trades | 45.200.547/0001-79 | 2.592 | R$ 52,50 | R$ 136.080 | R$ 24.494 |
| 3 | Broglio | 63.922.116/0001-06 | 1.728 | R$ 52,50 | R$ 90.720 | R$ 16.330 |

## Reconciliação Pós-Operação (Módulos B + C completos)

| Estabelecimento | Contábil | Físico | Nota |
|----------------|----------|--------|------|
| GB Matriz | 1.000 | 0 | Retenção B2B contábil |
| GB Filial (B2B) | 360 | 10.000* | *Físico inclui Matriz + B2B Filial + em trânsito |
| GB Comércio | 4.320 | 4.320 | ✅ Contábil = Físico |
| Trades | 2.592 | 2.592 | ✅ Contábil = Físico |
| Broglio | 1.728 | 1.728 | ✅ Contábil = Físico |
| **TOTAL** | **10.000** | **10.000** | ✅ |

**Esta tabela deve ser gerada em todo output do Módulo C.** Completa a reconciliação iniciada no Módulo B.

## Parâmetros (de tax-rules.json)
- `internal_sale_filial_simples.margin_pct`: 5%
- `internal_sale_filial_simples.icms_pct`: 18%
- `internal_sale_filial_simples.destinations`: array de CNPJs com benchmark_share_pct

## Validações
- Quantidade por CNPJ deve bater com output do Módulo A
- Soma das 3 NFs + reserva B2B Filial + retenção Matriz = total importado
- Todos os produtos cadastrados no Bling com NCM
- Margem aplicada conforme config (não hardcoded)
- CNPJ destinatário ativo e válido
- Preço interno = custo × 1,05 (exato, não arredondado antes da multiplicação)
- ICMS = 18% sobre preço interno (exato)
- Reconciliação estoque contábil × físico gerada

## Output
- 3 NFs geradas (draft ou emitidas)
- Resumo: CNPJ × valor total × quantidade × ICMS
- Reconciliação completa (todos os estabelecimentos)
- Log auditável por NF

## Dependências
- Módulo A (distribuição) — output obrigatório
- Módulo B (transferência) — deve ter sido executado antes
- API Bling v3 (OAuth)
- Config: tax-rules.json

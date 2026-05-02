---
title: "playbook"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Playbook Fiscal — Fisco

_Regras operacionais aprendidas com operações reais. Playbook vivo — evolui a cada importação processada._

## Benchmarks de Distribuição

### Distribuição Histórica por CNPJ — NFs internas

| Período | Emitente | GB Comércio | Trades | Broglio | Total |
|---------|----------|------------:|-------:|--------:|------:|
| Março/2026 | Filial + Matriz | R$ 18.928,84 | R$ 4.443,53 | R$ 5.983,48 | R$ 29.355,85 |
| Abril/2026 | Filial | R$ 55.662,33 | R$ 11.123,04 | R$ 10.279,72 | R$ 77.065,09 |

### Tempo Médio de Processamento por Módulo

| Módulo | Tempo Médio | Amostras | Observação |
|--------|-------------|----------|------------|
| B — NF Transferência | _A mapear_ | 2 | 000649 e 000653 já emitidas antes do regime v2.1 |
| C — NFs Internas | 1 dia operacional | 2 meses | Março e abril exigiram reconciliação manual |

## Regras Operacionais Aprendidas

### [REGRA-001] — NF interna exige reconciliação fiscal por componente
**Padrão:** Vendas marketplace usam SKUs comerciais/kits; NFs de entrada/transferência usam SKUs fiscais, caixas e conjuntos.
**Dados:** Abril/2026 travou em `YW1520`, `YW800SQ`, `YW1050` até corrigir fatores de conversão das NFs fiscais.
**Regra:** Antes de gerar prévia, montar `sku_fiscal_map` com SKU comercial, SKU fiscal, componente base, fator, NCM, origem, unidade e fonte. Baixa confiança bloqueia emissão.
**Confiança:** Alta.

### [REGRA-002] — Escopo de importação própria vence NCM/origem quando houver conflito
**Padrão:** Produto pode ter NCM/origem parecidos com importados próprios, mas pertencer a linha de terceiro/nacional.
**Dados:** CK4742/Jarra Clink apareceu como vidro/NCM compatível, mas Pedro confirmou que não é importação própria GB; foi excluído da NF abril/2026.
**Regra:** NF interna de importados próprios só inclui produtos próprios GB. Excluir terceiros, nacionais, pseudo-itens e itens sem SKU mesmo que cadastro fiscal pareça compatível.
**Confiança:** Alta.

### [REGRA-003] — Saldo Matriz só pode ser usado após abater B2B/atacado da Matriz
**Padrão:** Pedro às vezes emite vendas de atacado direto pela Matriz, consumindo estoque fiscal retido.
**Dados:** Divergência histórica `YW1520` na Matriz pode decorrer de consumo em março acima da retenção ou de saídas não consideradas.
**Regra:** Antes de usar saldo Matriz como excedente para NF interna, consultar NFs B2B/atacado da Matriz do período e abater por SKU/componente.
**Confiança:** Média-alta.

### [REGRA-004] — Venda interna Filial→Simples mantém tributação própria
**Padrão:** Orientação Suellen de ICMS/IPI suspenso/sem destaque se aplica à transferência Matriz→Filial, não à venda interna posterior.
**Dados:** Bling aplicou IPI 6,5% nas NFs internas abril/2026; Pedro autorizou após confirmar que a suspensão vale apenas na transferência.
**Regra:** Separar sempre operação de transferência (CFOP 6.152, CST 90/55) da operação de venda interna (CFOP 5.102, ICMS 18%, IPI conforme NCM).
**Confiança:** Alta.

## Checklist Operacional — NF interna mensal de importados próprios

1. Travar premissas fiscais vigentes com decisões/Suellen.
2. Levantar vendas válidas do mês por CNPJ e SKU comercial.
3. Filtrar somente importados próprios GB.
4. Excluir nacionais/MDF/cerâmica/livros/fita/pseudo-itens/SEM_SKU/terceiros/Jarra Clink.
5. Levantar estoque fiscal inicial Matriz/Filial pós-mês anterior.
6. Levantar entradas/transferências do mês por container e NF.
7. Montar/atualizar `sku_fiscal_map` com fatores de conversão.
8. Decompor kits em componentes fiscais.
9. Abater vendas B2B/atacado Matriz antes de usar saldo Matriz.
10. Validar cobertura por estabelecimento.
11. Gerar prévia por CNPJ.
12. Pedro aprova prévia.
13. Criar rascunhos Bling.
14. Validar divergência de valor/imposto/natureza.
15. Pedro autoriza SEFAZ explicitamente.
16. Baixar DANFE/XML e enviar ao Pedro/contabilidade.

## Histórico de Containers / NFs relevantes

| # | Data | Referência | NFs | Observação |
|---|------|-----------|-----|------------|
| GB25011 | 2026-04 | Entrada 580012 / Transferência 000649 | `42260458151616000143550010000006491951355040` | Transferência emitida antes da orientação v2.1; enviada à FOUR em 01/05. |
| GB25010 | 2026-04 | Entrada 580119 / Transferência 000653 | `42260458151616000143550010000006531440066894` | Transferência emitida antes da orientação v2.1; enviada à FOUR em 01/05. |

---

_Playbook fiscal vivo. Cada operação enriquece este documento._

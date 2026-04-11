---
name: shopee-fees-rules
description: Regras completas de comissões, taxas, frete e custos da Shopee Brasil para vendedores CNPJ. Base para precificação e estratégia de anúncios. Consultar SEMPRE antes de qualquer cálculo de margem, recomendação de pricing, simulação de lucro ou análise de custo na Shopee. Também ativar quando o usuário mencionar "quanto custa vender na Shopee", "comissão shopee", "taxa shopee", "calcular margem shopee", "precificação shopee", "custo frete shopee", "faixa de preço shopee", "taxa fixa shopee", "fronteira de faixa", "armadilha de preço shopee", "subsídio PIX", "frete grátis shopee", "campanha shopee", "afiliado shopee", ou qualquer variação relacionada a custos e taxas da Shopee Brasil.
triggers:
 - "quanto custa vender na Shopee"
 - "comissão shopee"
 - "taxa shopee"
 - "calcular margem shopee"
 - "precificação shopee"
 - "custo frete shopee"
 - "faixa de preço shopee"
 - "taxa fixa shopee"
 - "fronteira de faixa shopee"
 - "subsídio PIX shopee"
 - "campanha shopee"
 - "afiliado shopee"
 - "simulação shopee"
 - "margem shopee"
metadata:
 openclaw:
 emoji: 🧮
 last_updated: "2026-04-10"
 next_review: "2026-04-16"
 cron: "Shopee Fees Monitor — quarta 10h SP"
 sources:
 - url: "https://blog.calcularte.com.br/index.php/2026/03/06/taxas-comissoes-shopee-2026/"
 status: "✅ principal — mais completa e consistente"
 - url: "https://www.ecommercebrasil.com.br/artigos/shopee-acaba-com-o-teto-de-comissao-de-r-100-e-aumenta-a-taxa-fixa-cobrada-por-cada-item-vendido-em-ate-550"
 status: "✅ confiável"
 - url: "https://gosmarter.com.br/taxas-shopee-2026-comissao-custos/"
 status: "⚠️ diverge na taxa fixa R$500+ (lista R$28, correto é R$26)"
 - url: "https://gosmarter.com.br/frete-gratis-shopee-vendedor-como-funciona/"
 status: "✅ confiável para frete"
 - url: "https://economia.ig.com.br/2026-03-06/shopee-aumenta-taxas-e-muda-regras-para-vendedores-no-brasil.html"
 status: "✅ confiável"
 - url: "https://www.marketizesales.com.br/comissao-da-shopee-em-2026-o-que-muda-para-os-vendedores"
 status: "✅ confiável"
 - url: "https://algoritmoquevende.com.br/blog/nova-comissao-shopee-2026-cpf-cnpj"
 status: "✅ confiável"
 - url: "https://conteudos.xpi.com.br/acoes/relatorios/mercado-livre-meli34-shopee-inicia-2026-com-aumento-de-taxas/"
 status: "✅ confirmou taxa transação embutida"
 - url: "https://blog.calcularte.com.br/index.php/2026/03/06/como-ler-extrato-renda-estimada-shopee/"
 status: "✅ referência para extrato"
 removed_sources:
 - url: "https://www.oquesobra.com.br/blog/comissao-shopee-2026-cnpj-cpf"
 reason: "Desatualizada — ainda descreve modelo antigo (14% + 6%)"
---

# Regras de Comissões, Taxas e Custos — Shopee Brasil 2026 (CNPJ)

> ⚠️ **Última atualização:** 10/04/2026
> Reestruturação completa em **01/03/2026**: novas faixas escalonadas, fim do teto de R$ 100, taxa fixa por faixa (aumento até 550%), frete grátis obrigatório, subsídio PIX.
> **Nenhuma mudança adicional entre março e abril de 2026** — regras de março seguem vigentes.
> **Cron de verificação:** Quarta-feira 10h SP (Shopee Fees Monitor)
> **Escopo:** Esta skill cobre exclusivamente vendedores **CNPJ**. Regras CPF não se aplicam.

---

## 1. FAIXAS DE PREÇO, COMISSÕES E TAXAS FIXAS (CNPJ)

A Shopee opera com **5 faixas de comissão** desde 01/03/2026. A taxa de transação (~2%) **já está embutida** nos percentuais abaixo — NÃO é cobrada separadamente.

> **Composição interna dos percentuais:**
> - Faixa 2: 12% comissão base + 2% transação + 6% frete grátis = **20%**
> - Faixas 3–5: 12% comissão base + 2% transação = **14%**
> - Faixa 1: 50% all-in (comissão + transação + frete, tudo embutido)

| Faixa | Preço do Produto | Comissão | Taxa Fixa/item | Subsídio PIX | Custo Efetivo* |
|---|---|---|---|---|---|
| **1** | R$ 0,00 – R$ 7,99 | **50%** | R$ 0,00 | — | ~50% |
| **2** | R$ 8,00 – R$ 79,99 | **20%** | R$ 4,00 | — | 25%–70% |
| **3** | R$ 80,00 – R$ 99,99 | **14%** | R$ 16,00 | 5% | 30%–34% |
| **4** | R$ 100,00 – R$ 199,99 | **14%** | R$ 20,00 | 5% | 24%–34% |
| **5** | R$ 200,00+ | **14%** | R$ 26,00 | 5% (ou 8% se ≥R$500) | 17%–27% |

\* Custo efetivo = (comissão + taxa fixa) / preço. Varia dentro de cada faixa.

### Notas importantes:
- **Comissão incide sobre o valor do produto**, não sobre o frete
- **Taxa fixa é por ITEM vendido no pedido** (1 kit = 1 item = 1 taxa fixa)
- Na **Faixa 1** (< R$ 8): metade do preço vai pra Shopee — margem praticamente zero. A taxa fixa é R$ 0 porque os 50% já cobrem tudo
- Na **Faixa 2** (R$ 8–79,99): onde cai a maioria dos produtos da GB Importadora
- **Taxa de transação (~2%) já está incluída** nos percentuais acima. NÃO somar separadamente

---

## 2. ARMADILHA CRÍTICA: FRONTEIRAS ENTRE FAIXAS

| Cenário | Preço | Comissão | Taxa Fixa | Custo Total |
|---|---|---|---|---|
| Faixa 2 (topo) | R$ 79,99 | R$ 16,00 | R$ 4,00 | **R$ 20,00** |
| Faixa 3 (início) | R$ 80,00 | R$ 11,20 | R$ 16,00 | **R$ 27,20** |

**⚠️ R$ 0,01 a mais no preço = R$ 7,20 a mais em taxas!**

### Fronteiras perigosas (memorizar):
- **R$ 7,99 → R$ 8,00**: comissão cai de 50% pra 20% mas taxa fixa de R$ 4 aparece
- **R$ 79,99 → R$ 80,00**: taxa fixa salta de R$ 4 → R$ 16 (+R$ 12) — **PIOR FRONTEIRA**
- **R$ 99,99 → R$ 100,00**: taxa fixa salta de R$ 16 → R$ 20 (+R$ 4)
- **R$ 199,99 → R$ 200,00**: taxa fixa salta de R$ 20 → R$ 26 (+R$ 6)

### Regra de precificação:
NUNCA precificar exatamente no início de uma faixa superior. Se o cálculo der R$ 80–85, é melhor vender a R$ 79,99 (Faixa 2) do que a R$ 80 (Faixa 3). **Sempre verificar em qual faixa o preço final caiu DEPOIS de calcular.**

---

## 3. MUDANÇAS DE MARÇO 2026 (vs modelo anterior)

### 3.1 Fim do teto de comissão de R$ 100
- **Antes:** comissão máxima era R$ 100 + R$ 4 taxa fixa = **R$ 104 total**
- **Agora:** comissão escala linearmente sem limite + taxa fixa por faixa

| Preço | Custo total antes (com teto) | Custo total agora (sem teto) | Diferença |
|---|---|---|---|
| R$ 500 | R$ 104 | R$ 96 (R$70 + R$26) | **−R$ 8** |
| R$ 714 | R$ 104 | R$ 126 (R$100 + R$26) | **+R$ 22** |
| R$ 1.000 | R$ 104 | R$ 166 (R$140 + R$26) | **+R$ 62** |
| R$ 2.000 | R$ 104 | R$ 306 (R$280 + R$26) | **+R$ 202** |
| R$ 5.000 | R$ 104 | R$ 726 (R$700 + R$26) | **+R$ 622** |

> **Nota:** Produtos até ~R$ 500 ficaram MAIS baratos ou neutros. Acima disso, o custo escala fortemente. Produto de R$ 5.000 paga quase 7× mais que antes.

### 3.2 Aumento da taxa fixa (até 550%)
- **Antes:** R$ 4 fixo para todos os produtos CNPJ, independente do preço
- **Agora:** R$ 0 a R$ 26 conforme faixa (ver seção 1)

| Faixa | Taxa antes | Taxa agora | Aumento |
|---|---|---|---|
| 1 | R$ 4 | R$ 0 (50% all-in) | N/A |
| 2 | R$ 4 | R$ 4 | 0% |
| 3 | R$ 4 | R$ 16 | +300% |
| 4 | R$ 4 | R$ 20 | +400% |
| 5 | R$ 4 | R$ 26 | +550% |

### 3.3 Frete Grátis obrigatório
- **Antes:** adesão voluntária ao Programa de Frete Grátis (+6% sobre a comissão)
- **Agora:** compulsório para todos os sellers, custo já embutido na comissão

### 3.4 Subsídio PIX (novo)
- Desconto automático pro comprador via PIX, 100% bancado pela Shopee
- Cortes: **5% para R$ 80–499,99** e **8% para R$ 500+**
- Produtos abaixo de R$ 80: sem subsídio PIX

### 3.5 Campanhas de destaque (novo)
- Taxa adicional de 2,5% sobre todas as vendas (antes de março: não existia)

### 3.6 Coparticipação de frete (melhorou)
- **Antes:** 63% vendedor / 37% Shopee
- **Agora:** 25% vendedor / 75% Shopee

### Resumo comparativo:

| Aspecto | Antes de março 2026 | Depois de março 2026 |
|---|---|---|
| Comissão | Fixa: 14% (ou 20% c/ Frete Grátis) | Escalonada: 50% / 20% / 14% por faixa |
| Taxa fixa | R$ 4,00 uniforme | R$ 0 a R$ 26 por faixa |
| Teto de comissão | R$ 100 por item | **Eliminado** |
| Frete Grátis | Opcional (+6%) | Obrigatório (incluído) |
| Subsídio PIX | Inexistente | 5%–8% (pago pela Shopee) |
| Coparticipação frete | 63% vendedor / 37% Shopee | 25% vendedor / 75% Shopee |
| Campanhas destaque | Sem taxa adicional | +2,5% opcional |
| Taxa transação | ~2% separada | Embutida na comissão |

---

## 4. FRETE GRÁTIS — PROGRAMA OBRIGATÓRIO

### 4.1 Subsídio de frete (Shopee paga)

A Shopee oferece cupons de frete grátis aos compradores, subsidiados pela plataforma:

| Preço do Item | Subsídio Máximo |
|---|---|
| Até R$ 79,99 | **R$ 20,00** |
| R$ 80 – R$ 199,99 | **R$ 30,00** |
| R$ 200+ | **R$ 40,00** |

Adicionalmente: cupons de 50% desconto no frete para compras acima de R$ 10.

### 4.2 Impacto para o vendedor
- ✅ Na maioria dos casos, subsídio cobre 100% do frete de envios leves e regionais
- ✅ Selo "Frete Grátis" automático em todos os produtos → mais visibilidade e conversão
- ⚠️ Se frete real > subsídio → diferença pode recair sobre o vendedor
- 💡 Subsídio de frete NÃO afeta cálculo de comissão (são custos separados)
- ⚠️ Itens pesados, volumosos ou destinos distantes: subsídio pode não cobrir 100%

### 4.3 Coparticipação de frete (vendedores com API)
Para vendedores que usam integração de frete via API (ex: Intelipost):
- Vendedor arca com **25%** do valor do cupom de frete
- Shopee cobre **75%** (cupom máximo de R$ 40)
- Proporção melhorou significativamente vs modelo anterior (era 63%/37%)

### 4.4 Comparação com [[skills/marketplace/ml-fees-rules/SKILL|Mercado Livre]]
- **ML:** frete grátis geralmente sai do bolso do vendedor (via tabela de frete competitivo)
- **Shopee:** frete grátis subsidiado pela plataforma (até os limites acima)
- **Na prática:** Shopee é mais vantajosa em frete, mas cobra mais em comissão (20% vs 11-16% ML)

---

## 5. SUBSÍDIO PIX

Desconto automático pro comprador quando paga via PIX, **100% custeado pela Shopee**:

| Preço do Item | Desconto PIX |
|---|---|
| Até R$ 79,99 | Sem desconto |
| R$ 80 – R$ 499,99 | **5%** |
| R$ 500+ | **8%** |

### Impacto para o vendedor:
- **ZERO.** Vendedor recebe valor integral da venda
- Exemplo: produto R$ 100 → comprador paga R$ 95 no PIX, vendedor recebe R$ 100
- No extrato aparecem duas linhas que se anulam: "Ajuste por pagamento via PIX" (débito) e "Ajuste por participação em ação comercial" (crédito)
- Torna produtos mais competitivos sem custo adicional
- Não interfere no cálculo de comissão nem na precificação

### Separação operacional:
Para comissão e taxa fixa, **R$ 200–499,99** e **R$ 500+** pertencem à mesma faixa (Faixa 5). A separação só importa por causa do subsídio PIX (5% vs 8%).

---

## 6. CAMPANHAS DE DESTAQUE

- Taxa adicional de **2,5%** sobre **TODAS** as vendas durante o período da campanha
- Aplica sobre todo o catálogo, NÃO só sobre os produtos na vitrine da campanha
- Participação **voluntária**
- **Regra:** avaliar se o volume esperado de vendas compensa o custo de 2,5% sobre todo o faturamento do período
- Pra margens apertadas, essa taxa pode zerar o lucro
- **Novidade de março 2026** — antes não existia taxa para campanhas

---

## 7. SHOPEE ADS

- Não é taxa obrigatória, mas é custo real que impacta a margem
- **Regra:** definir teto de Ads por SKU (ex: "máximo R$ 3,50 por venda")
- Se custo Ads > margem disponível → prejuízo acelerado
- Sempre simular com e sem Ads antes de decidir

---

## 8. PROGRAMA DE AFILIADOS

Vendedores podem ativar o programa de afiliados para que influenciadores promovam seus produtos:

- **Comissão base:** 3% sobre a venda
- **Comissão configurável pelo vendedor:** 3% a 30% (programa ComissXtra)
- **Faixa média praticada:** 10% a 20%
- **Janela de atribuição:** 7 dias após o clique
- **Pagamento:** mensal após validação (excluindo devoluções)
- **Saque mínimo do afiliado:** R$ 50

### Impacto para o vendedor:
- A comissão do afiliado é custo ADICIONAL à comissão da Shopee
- Produto com margem apertada pode ficar inviável se afiliado ativo
- **Regra:** simular margem COM e SEM afiliado. Se margem com afiliado < 5%, desativar para aquele SKU

---

## 9. CUSTOS "ESCONDIDOS"

Custos que não aparecem como "taxa" mas reduzem o lucro:

| Custo | Descrição | Estimativa |
|---|---|---|
| Cupons/descontos | Parte do desconto pode ser absorvida pelo vendedor | Variável |
| Devoluções | Custo de logística reversa + reprocessamento | ~3-5% do faturamento |
| Embalagem | Caixa, plástico bolha, etiqueta | R$ 0,50–R$ 2,00/item |
| Erro operacional | Envio errado, avaria | Variável |
| Afiliados | Se vendedor participa do programa de afiliados | 3%–30% (config. pelo vendedor) |

---

## 10. FÓRMULA DE PRECIFICAÇÃO

### Fórmula (Markup Divisor)

> ⚠️ **A taxa de transação (~2%) já está embutida na comissão. NÃO somar separadamente.**

```
Preço = (Custo + Embalagem + Taxa Fixa + Ads) / (1 - Comissão% - Margem%)
```

Se participar de campanha, adicionar 2,5%:
```
Preço = (Custo + Embalagem + Taxa Fixa + Ads) / (1 - Comissão% - Campanha% - Margem%)
```

Se afiliado ativo, adicionar comissão configurada:
```
Preço = (Custo + Embalagem + Taxa Fixa + Ads) / (1 - Comissão% - Afiliado% - Margem%)
```

### Exemplo CNPJ, Faixa 2, sem Ads, sem campanha, sem afiliado, margem 25%:
```
Preço = (15 + 1,50 + 4) / (1 - 0,20 - 0,25)
Preço = 20,50 / 0,55
Preço = R$ 37,27
```
✅ R$ 37,27 está na Faixa 2 (R$ 8–79,99) → faixa correta, OK.

### Exemplo CNPJ, Faixa 2, com Ads R$ 3,00/venda, margem 25%:
```
Preço = (15 + 1,50 + 4 + 3) / (1 - 0,20 - 0,25)
Preço = 23,50 / 0,55
Preço = R$ 42,73
```

### ⚠️ SEMPRE verificar se o preço calculado não "caiu" em faixa diferente da esperada!

### Checklist de verificação:
1. [ ] Preço está na faixa esperada?
2. [ ] Não está na fronteira perigosa (R$ 80, R$ 100, R$ 200)?
3. [ ] Usou o percentual de comissão da faixa correta (já inclui transação)?
4. [ ] Incluiu taxa fixa da faixa correta?
5. [ ] Considerou cenário com e sem Ads?
6. [ ] Considerou cenário com afiliado (se aplicável, 3–30%)?
7. [ ] Frete está coberto pelo subsídio? (verificar peso/distância)
8. [ ] Se campanha ativa, incluiu +2,5%?

---

## 11. SIMULAÇÃO POR FAIXA (CNPJ, sem Ads, sem campanha, sem afiliado)

### Faixa 2: Produto R$ 45,00 (custo R$ 15,00)
| Item | Valor |
|---|---|
| Comissão (20%, já inclui transação) | −R$ 9,00 |
| Taxa fixa | −R$ 4,00 |
| Embalagem | −R$ 1,50 |
| Frete vendedor | R$ 0,00 (subsidiado) |
| Custo produto | −R$ 15,00 |
| **Lucro líquido** | **R$ 15,50** |
| **Margem** | **34,4%** |

### Faixa 2: Produto R$ 25,00 (custo R$ 7,82)
| Item | Valor |
|---|---|
| Comissão (20%, já inclui transação) | −R$ 5,00 |
| Taxa fixa | −R$ 4,00 |
| Embalagem | −R$ 1,00 |
| Frete vendedor | R$ 0,00 (subsidiado) |
| Custo produto | −R$ 7,82 |
| **Lucro líquido** | **R$ 7,18** |
| **Margem** | **28,7%** |

### Faixa 3: Produto R$ 89,90 (custo R$ 30,00)
| Item | Valor |
|---|---|
| Comissão (14%, já inclui transação) | −R$ 12,59 |
| Taxa fixa | −R$ 16,00 |
| Embalagem | −R$ 1,50 |
| Frete vendedor | R$ 0,00 (subsidiado) |
| Custo produto | −R$ 30,00 |
| **Lucro líquido** | **R$ 29,81** |
| **Margem** | **33,2%** |

### Faixa 5: Produto R$ 250,00 (custo R$ 80,00)
| Item | Valor |
|---|---|
| Comissão (14%, já inclui transação) | −R$ 35,00 |
| Taxa fixa | −R$ 26,00 |
| Embalagem | −R$ 2,00 |
| Frete vendedor | R$ 0,00 (subsidiado) |
| Custo produto | −R$ 80,00 |
| **Lucro líquido** | **R$ 107,00** |
| **Margem** | **42,8%** |

---

## 12. REGRAS ESTRATÉGICAS DE PRECIFICAÇÃO

1. **NUNCA precificar nos limites de faixa** — R$ 79,99 é muito melhor que R$ 80,00
2. **Kits diluem taxa fixa** — 1 kit = 1 taxa fixa. 5 vendas avulsas = 5 taxas fixas
3. **Custo efetivo cai com preço maior** — produtos mais caros são proporcionalmente menos taxados
4. **Frete grátis é padrão** — não é diferencial, todos têm. Foque em outros diferenciais
5. **Subsídio PIX não afeta vendedor** — mas torna produtos ≥R$ 80 mais atraentes pro comprador
6. **Campanhas custam 2,5% sobre TUDO** — calcular antes de aderir
7. **Sem teto de comissão** — produtos acima de R$ 500 precisam de atenção redobrada na margem
8. **Ads: teto por SKU** — definir máximo por venda, se passar = prejuízo
9. **Afiliados: 3–30% configurável** — simular impacto antes de ativar. Se margem < 5% com afiliado, desativar para o SKU
10. **Comparar Shopee vs ML antes de decidir preço** — Shopee taxa mais (20% vs 11-16%) mas subsidia frete
11. **Taxa de transação já está embutida** — NÃO somar ~2% separadamente nos cálculos

---

## 13. URLs DE MONITORAMENTO (Cron Semanal)

Fontes a verificar semanalmente pelo cron `Shopee Fees Monitor`:

| # | Fonte | Status | Nota |
|---|---|---|---|
| 1 | [Calcularte — Taxas Shopee 2026](https://blog.calcularte.com.br/index.php/2026/03/06/taxas-comissoes-shopee-2026/) | ✅ Principal | Mais completa e consistente |
| 2 | [Calcularte — Extrato Renda Estimada](https://blog.calcularte.com.br/index.php/2026/03/06/como-ler-extrato-renda-estimada-shopee/) | ✅ Referência | Detalha linhas do extrato |
| 3 | [Marketize Sales](https://www.marketizesales.com.br/comissao-da-shopee-em-2026-o-que-muda-para-os-vendedores) | ✅ Confiável | — |
| 4 | [Algoritmo que Vende](https://algoritmoquevende.com.br/blog/nova-comissao-shopee-2026-cpf-cnpj) | ✅ Confiável | — |
| 5 | [GoSmarter — Taxas](https://gosmarter.com.br/taxas-shopee-2026-comissao-custos/) | ⚠️ Atenção | Diverge taxa R$500+ (R$28 vs R$26). Calcularte prevalece |
| 6 | [E-Commerce Brasil](https://www.ecommercebrasil.com.br/artigos/shopee-acaba-com-o-teto-de-comissao-de-r-100-e-aumenta-a-taxa-fixa-cobrada-por-cada-item-vendido-em-ate-550) | ✅ Confiável | — |
| 7 | [Seller Shopee (oficial)](https://seller.shopee.com.br) | ✅ Oficial | Requer login de vendedor |

### Protocolo de verificação:
1. Acessar fontes 1–6 → comparar com dados desta skill
2. Se divergência encontrada → cruzar com pelo menos 2 outras fontes
3. Se confirmada → atualizar skill + notificar Pedro no tópico 🛒 Marketplaces
4. **Regra de conflito:** Calcularte + fonte oficial Shopee prevalecem sobre GoSmarter/outros

---

## CHANGELOG

| Data | Alteração |
|---|---|
| 10/04/2026 | v2.0 — Correção: taxa transação (~2%) embutida na comissão (não somar separado). Faixa 1 taxa fixa = R$0. Simulações recalculadas. Fórmula corrigida. Adicionada coparticipação frete API. Afiliados corrigido (3–30%, não ~10%). Removida seção CPF. Adicionada simulação Faixa 5. Fontes auditadas (removida OQueSobra desatualizada, adicionada XP Investimentos e Calcularte Extrato). |
| 08/04/2026 | v1.0 — Criação inicial |

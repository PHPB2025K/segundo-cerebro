# 📋 TABELA MESTRA DE CLASSIFICAÇÃO — GB GRUPO
## Referência rápida para classificação de lançamentos dos extratos Itaú

**Versão:** 2.0 (Maio/2026)
**Base:** análise de extratos dos períodos 04-14/05 e 04-21/05/2026 + esclarecimentos Simone/Pedro

**Regra primária:** classificar pelo **CNPJ/CPF** do contraparte. A descrição é apenas auxiliar quando o identificador não está claro.

🆕 = cadastro novo adicionado na v2.0 (ciclo 04-21/05/2026)

---

## 🏢 MAPEAMENTO CONTAS ITAÚ → EMPRESAS DO GRUPO

| Conta Itaú | Empresa | CNPJ | Coluna na DFC | Razão social no extrato |
|:---:|---|---|:---:|---|
| 0099339-0 | GB MATRIZ | 58.151.616/0001-43 | B (2) | GB IMPORTADORA E COMERCIO LTDA |
| 0099338-2 | GB FILIAL | 58.151.616/0002-24 | C (3) | GB IMPORTADORA E COMERCIO LTDA |
| 0099340-8 | CONCEPT | 58.818.245/0001-00 | D (4) | CONCEPT SERV ASS EMPR LTDA |
| 0037332-0 | GB COMERCIO | 07.194.128/0001-82 | E (5) | GB COM DE IMP E EXP LTDA |
| 0021526-5 | BROGLIO IMP | 63.922.116/0001-06 | F (6) | BROGLIO IMP E EXPORTACAO LTDA |
| 0099310-1 | TRADES UP | 45.200.547/0001-79 | G (7) | TRADES UP IMP E EXP LTDA |
| 0099795-3 | S.P BROGLIO | 97.546.173/0001-41 | H (8) | S P BROGLIO |
| — | GAVETA (caixa físico) | — | I (9) | — |

⚠️ **GB MATRIZ e GB FILIAL têm o mesmo CNPJ raiz mas são empresas DIFERENTES** (matriz e filial). Transferências entre elas são **transferências internas legítimas (linha 69)**. Identificar SEMPRE pela conta Itaú + CNPJ, nunca só pela razão social.

---

# 💰 ENTRADAS

## 🛒 Marketplaces — Linha 11

| CNPJ | Razão Social | Padrões de descrição |
|---|---|---|
| 38.372.267/0001-82 | SHPP BRASIL (Shopee) | `PIX RECEBIDO SHPP BR...` |
| 15.436.940/0001-03 | AMAZON SERVICOS DE VAREJO | `TED 755.1306.AMAZON`, `SISPAG MAST/ELO/VISA/AMEX` |
| 10.573.521/0001-91 | MERCADO PAGO (quando recebimento) | — |

**SISPAG MAST/ELO/VISA/AMEX da Amazon = chargeback de cartões** (entrada positiva, Marketplaces).

---

## 🏢 B2B Atacado — Linha 9

**Regra:** PIX RECEBIDO ou BOLETO RECEBIDO de **pessoa jurídica** (CNPJ) que NÃO seja marketplace, outra empresa do grupo, ou outra categoria específica.

| CNPJ | Razão Social |
|---|---|
| 37.815.323/0001-43 | J F LEME |
| 60.618.499/0001-27 | CELINO GOMES CASSIMIRO |
| 41.698.163/0001-77 | MARIA VITORIA SAVANI LTDA |
| 53.033.018/0001-56 | PLASTWARE INDUSTRIA E COMERCIO |
| 55.773.184/0001-14 | FAROL SHOP VILA VELHA LTDA |
| 48.690.876/0001-33 | G M T COME UTILIDADES DOMESTICAS |
| 58.020.950/0001-68 | JOAO VITHOR DE OLIVEIRA |
| 58.153.884/0001-02 | RAFAEL ZANETE GUIRAO |
| 60.830.003/0001-84 | LOPLASTIC COMERCIO E DISTRIBUICAO |
| 07.104.810/0001-37 | OPEN TRADE EXPORTAÇÃO E IMPORTAÇÃO |
| 🆕 26.186.284/0001-46 | C. F C F T - EIRELI - ME |
| 🆕 04.968.578/0001-97 | PLASMONT INDUSTRIA E COMERCIO DE PLASTIC |
| 🆕 37.604.776/0001-20 | CAROLINA BUENO UTTEMBERGHE |
| 🆕 42.688.296/0001-25 | MARCHPEL INDUSTRIA E COMERCIO LTDA |
| 🆕 37.439.225/0001-59 | SAMANTA DE CARVALHO MASSONI |

Também B2B: `BOLETOS RECEBIDOS DD/MMS` (genérico, sem identificação clara).

---

## 🛍️ B2C Varejo — Linha 10

**Regra:** PIX RECEBIDO de **pessoa física** (CPF) com valor compatível com varejo.

| CPF | Nome |
|---|---|
| 496.013.968-45 | KAUAN HENRIQUE VIGATO |
| 474.300.308-31 | LARINA MARIA DA SILVA LIMA |
| 290.470.548-14 | ERLON RODRIGO ADABO |
| 366.081.508-06 | YASMIN CAROLINE OSCARLINO (quando **RECEBIDO**) |
| 457.047.138-23 | LEONARDO BASSETO RODRIGUES (quando **RECEBIDO**) |
| 077.823.918-73 | SANDRA PERON (quando **RECEBIDO**) |

Também B2C: `DEP DIN ATM` (depósito em dinheiro via caixa eletrônico).

---

## 🪙 Juros — Linha 12

| Padrão de descrição |
|---|
| `REND PAGO APLIC AUT MAIS` |
| `REND PAGO APLIC AUT APR` |
| Centavos residuais do dia final (rendimento Maxi não-extratado) — lançar no último dia com movimento de cada empresa |

---

## 🔥 Outras Entradas Operacionais — Linha 13

**Caso principal:** PIX RECEBIDO da **PRÓPRIA empresa** (mesmo CNPJ EXATO da conta de origem). Significa dinheiro vindo de outra conta bancária da mesma empresa em outro banco.

Exemplos catalogados:
- "PIX RECEBIDO GB COME" na conta da GB COMERCIO (07.194.128/0001-82)
- "PIX RECEBIDO S. P. B" na conta da S.P BROGLIO (97.546.173/0001-41)
- "RECEBIMENTOS GB IMPORTADORA" entre contas de mesmo CNPJ exato

---

# 💸 SAÍDAS

## 🏭 Fornecedores Nacionais — Linha 23

| CNPJ/CPF | Razão Social |
|---|---|
| 15.042.595/0001-15 | MAXIMA |
| 30.999.703/0001-36 | KOVALIK EMBALAGENS |
| 26.896.887/0001-31 | TALITA PERON DE GODOI |
| 22.212.404/0001-81 | R R PORCELANAS |
| 66.138.694/0001-36 | WAIZELI DISTRIBUIDORA |
| 11.129.630/0001-87 | PORCELANA HORACILIO RODRIGUES |
| 33.094.239/0001-27 | HIMMEL CORP |
| 74.484.403/0001-90 | F J FANTINI AMPARO LTDA |
| 19.822.149/0001-84 | FINAMAR |
| 04.328.938/0001-96 | OKAHOMA COMERCIO E ASSESSORIA |
| 05.220.481/0001-64 | GERSON FERRAZZO |
| **155.878.758-57** | **LUIS AGUINALDO MOLINA** (fornecedor de canecas PF) |
| **096.856.098-96** | **PAULO BROGLIO** ⚠️ (ver regra especial abaixo) |
| 🆕 61.780.392/0001-43 | FABIO LUIZ BASSANI |
| 🆕 155.928.948-13 | CLEUNICE MARIA DE PAULA ROCHA |

### ⚠️ Regra Especial: PAULO BROGLIO (096.856.098-96)

- **Por padrão:** todo PIX para Paulo Broglio = **Fornec Nacional** (pagamento a **Guinho Canecas + Lu Porcelanas** via PF do sócio)
- **Motivo:** empresa paga esses fornecedores via cheques próprios + empréstimo Caixa repassados ao sócio
- ✅ **Confirmado maio/2026:** regra continua valendo, mesmo havendo pró-labore de outro sócio (Pedro Henrique) no mesmo período
- **Validação obrigatória:** confirmar com Simone a cada novo período

---

## 👥 Salários — Linha 27

⚠️ **PEDRO OCTAVIO é SEMPRE Salários, em qualquer conta** (confirmado pela Simone).

| CPF | Nome |
|---|---|
| **429.434.788-06** | **PEDRO OCTAVIO BUENO FERNANDES** (sempre) |
| 562.055.698-09 | GUILHERME DOS SANTOS HIGASHI |
| 077.823.918-73 | SANDRA PERON (quando **ENVIADO**) |
| 450.135.498-41 | FRANCIELE CAROLINA DE SOUZA AGUIAR |
| 461.175.998-97 | MATEUS EDUARDO LISBOA SANTOS |
| 494.206.548-85 | GEZIELE BATISTA DA SILVA |
| 493.044.648-11 | LUCAS GABRIEL LAURENTINO |
| 457.047.138-23 | LEONARDO BASSETO RODRIGUES (quando **ENVIADO**) |
| 366.081.508-06 | YASMIN CAROLINE OSCARLINO (quando **ENVIADO**) |
| 381.177.168-01 | ADRIANA SANTOS DE MORAES DA COSTA |

**Padrão identificador de folha:** múltiplos PIX para CPFs no mesmo dia (em torno do dia 06), na GB COMERCIO.

---

## 🤝 Retirada de Sócios — Linha 62

| CPF | Nome |
|---|---|
| 🆕 **347.048.378-74** | **PEDRO HENRIQUE PERON BROGLIO** (pró-labore semanal) |

⚠️ **NÃO confundir com Paulo Broglio (Fornecedor).** Pedro Henrique e Paulo podem aparecer no mesmo dia/conta com valores parecidos, mas têm classificações diferentes.

---

## 🏛️ Impostos — Linha 25

| CNPJ / Identificador | Descrição |
|---|---|
| 46.410.775/0001-36 | PM PEDREIRA (Tributo Municipal) |
| 00.394.460/0058-87 | DARF / SIMPLES NACIONAL (`PAGAMENTOS TRIB COD BARRAS`) |
| 🆕 46.410.866/0001-71 | MUNICIPIO DE JAGUARIUNA (taxa prefeitura) |
| 🆕 `INT IPVA-SP...` | Parcelamento de IPVA |

Padrões: `PAGAMENTOS TRIB MUNICIPAL`, `PAGAMENTOS TRIB COD BARRAS`, `DAS MEI`, `INT IPVA-SP...`.

---

## 🏢 Despesas Administrativas — Linha 28

| CNPJ / Identificador | Descrição |
|---|---|
| 65.422.339/0001-21 | UNIMED AMPARO (plano de saúde) |
| 49.458.269/0001-05 | FOUR ASSESSORIA EMPRESARIAL (contabilidade) |
| 20675554688 | VIVO-SP (`DA VIVO-SP`) |
| 28.862.503/0001-95 | C.L. MONITORAMENTO E ALARMES |
| 26.855.879/0001-47 | CONCEPT CENTRO DE NEGOCIOS (aluguel/coworking) |
| 🆕 10.409.865/0001-60 | JR PRINT (empresa de impressoras) |
| 🆕 522.222.668-90 | JOAO PEDRO CASTELLANI DO PRADO (impressoras) |
| 🆕 01.663.516/0001-89 | INTERCARD SERVICOS MEDICOS |
| 🆕 01.109.184/0001-95 | UNIVERSO ONLINE / UOL (marketing digital) |
| 🆕 46.129.490/0001-21 | ASSOCIACAO COMERCIAL E EMPRESARIAL DE PEDREIRA |

⚠️ **JR Print e João Pedro Castellani** = empresa de impressoras → Despesa Administrativa, NÃO fornecedor.

---

## 💸 Taxas — Linha 26

| Padrão de descrição |
|---|
| `TAR PLANO ADAPT` |
| `TAR CONTR/RENOV CTA GAR` |
| `TAR COBRANCA EXP` |
| `TAR SAQUE PESSOAL` |
| `IOF` (qualquer) |
| 🆕 `SISDEB REDECARD S A` (taxa maquininha) |

---

## 📊 Pagamento de Juros — Linha 61

| Padrão | Origem |
|---|---|
| `JUROS 0012.05491-2` | Juros de cheque especial Itaú |
| **`SAQUE DIN ATM` na conta GB COMERCIO** (qualquer valor) | **Juros do empréstimo Soemes** (saque em espécie) ⚠️ |

⚠️ **Confirmado maio/2026:** TODOS os saques em dinheiro na GB COMERCIO são juros Soemes, independente do valor (R$ 1.000, R$ 1.500, R$ 2.000...). Confirmar caso a caso para outras empresas.

---

## 🗂️ Outras Saídas Operacionais — Linha 29

| Identificador | Descrição |
|---|---|
| 00.000.000/0452-92 | BANCO DO BRASIL — boletos do **treinamento profissional G4 dos sócios** |
| 90.400.888/0001-42 | SANTANDER NEGOCIOS PLAT MC — boletos do **treinamento G4** |
| 51.174.001/0001-93 | SAO PAULO TRIBUNAL DE JUSTICA (depósito judicial) |
| `CONS PARCELA...` | **Consórcio imobiliário** |
| `PAGAMENTOS PIX QR-CODE` (sem identificação clara) | Caso genérico |
| `PAGAMENTOS PIX QR-CODE SHPP/MERC PAGO` | Estornos/devoluções de marketplaces |
| 🆕 34.028.316/0001-03 | CORREIOS / ECT (postagem/frete) |
| 🆕 00.360.305/0001-04 | `PAGAMENTOS PIX QR-CODE CEF MATRIZ` (Caixa Econômica) |

---

# 🔄 TRANSFERÊNCIAS INTERNAS — Linha 69

⚠️ **Critério rigoroso:** só é transferência interna quando o CNPJ de destino é **DIFERENTE** do CNPJ de origem, mas **ambos pertencem ao grupo** (8 empresas).

## ✅ É transferência interna (linha 69)

- GB MATRIZ ↔ GB FILIAL (CNPJs diferentes: 58.151.616/0001-43 vs 0002-24)
- CONCEPT ↔ TRADES UP
- GB COMERCIO ↔ TRADES UP
- Qualquer combinação entre as 8 empresas do grupo

## ❌ NÃO é transferência interna

| Tipo | Tratamento |
|---|---|
| `PIX RECEBIDO GB COME` na própria GB COMERCIO (mesmo CNPJ exato) | **Outras Entradas (linha 13)** |
| `PIX RECEBIDO S. P. B` na própria S.P BROGLIO (mesmo CNPJ exato) | **Outras Entradas (linha 13)** |
| Espelho de transferência (já contado uma vez) | Ignorar a segunda ocorrência |

## 🧪 Validação obrigatória

A soma das transferências (linha 69) de todas as 8 empresas no mesmo dia **DEVE SER ZERO**.

---

# ❌ LANÇAMENTOS A IGNORAR

| Padrão | Motivo |
|---|---|
| `SALDO ANTERIOR` | Linha informativa — mas é o saldo inicial (vai no R73) |
| `SALDO TOTAL DISPONÍVEL DIA` | Linha informativa do extrato |
| `SALDO EM CONTA CORRENTE` | Linha informativa — mas é o saldo final (deve bater no cálculo) |

---

# 🚀 PROTOCOLO PARA ITENS NÃO CATALOGADOS

Quando aparecer no extrato um CNPJ/CPF **NÃO listado** nesta tabela:

1. **Separar** numa seção "ITENS NÃO CATALOGADOS — REQUER CLASSIFICAÇÃO"
2. **Listar** com data, valor, descrição, CNPJ/CPF, e palpite de classificação
3. **Perguntar** ao Pedro antes de processar definitivamente
4. **Atualizar** esta tabela mestra para futuras rodadas
5. A tabela cresce a cada ciclo — quanto mais histórico, menos perguntas

## Template de pergunta

```
Detectei lançamentos não catalogados. Como classificar?

1. [dia] [empresa] [valor] [descrição/CNPJ] → palpite: [categoria]
2. [dia] [empresa] [valor] [descrição/CNPJ] → palpite: [categoria]

Opções: Fornec Nacional | Salarios | Desp Admin | Impostos |
        Outras Saidas | B2B | B2C | Marketplaces | Outras Entradas |
        Retirada Socios | Pag Juros | Caso a caso
```

---

# 📊 RESUMO RÁPIDO POR LINHA DA PLANILHA DFC POR CNPJ

| Linha | Categoria | Tipo |
|:---:|---|:---:|
| 9 | Recebimentos B2B | Entrada |
| 10 | Recebimentos B2C | Entrada |
| 11 | Recebimentos Marketplaces | Entrada |
| 12 | Recebimentos de Juros | Entrada |
| 13 | Outras Entradas Operacionais | Entrada |
| 17 | Importação - Sinal (30%) | Saída |
| 18 | Importação - Saldo (70%) | Saída |
| 19 | Frete Internacional | Saída |
| 20 | Seguro Internacional | Saída |
| 21 | Despachante Aduaneiro | Saída |
| 22 | Armazenagem/THC | Saída |
| 23 | Fornecedores Nacionais | Saída |
| 24 | Frete Nacional | Saída |
| 25 | Impostos | Saída |
| 26 | Taxas e Emolumentos | Saída |
| 27 | Salários e Encargos | Saída |
| 28 | Despesas Administrativas | Saída |
| 29 | Outras Saídas Operacionais | Saída |
| 36 | Venda de Ativos | Entrada Invest |
| 37 | Resgate de Aplicações | Entrada Invest |
| 38 | Outras Entradas Investimento | Entrada Invest |
| 42 | Aplicações Financeiras | Saída Invest |
| 43 | Compra de Máquinas | Saída Invest |
| 44 | Compra de Móveis | Saída Invest |
| 45 | Compra de Moldes | Saída Invest |
| 46 | Investimentos em TI | Saída Invest |
| 47 | Outras Saídas Investimento | Saída Invest |
| 54 | Empréstimos Tomados | Entrada Financ |
| 55 | Aporte de Sócios | Entrada Financ |
| 56 | Outras Entradas Financiamento | Entrada Financ |
| 60 | Pagamento de Principal | Saída Financ |
| 61 | Pagamento de Juros | Saída Financ |
| 62 | Retirada de Sócios | Saída Financ |
| 63 | Outras Saídas Financiamento | Saída Financ |
| 69 | Transferência entre Contas | Movimento Interno |
| 73 | Saldo Inicial de Caixa (B-I editável) | 🟡 Dado |

⚠️ **Nota:** A DFC POR CNPJ NÃO tem linha de "Saldo em Aplicações". Esse controle só existe na consolidada (R73 dela).

---

# 📜 HISTÓRICO DE VERSÕES

| Versão | Data | Alterações |
|:---:|---|---|
| 1.0 | Mai/2026 | Versão inicial — extraída do Knowledge File v10.0 (1º ciclo) |
| **2.0** | **Mai/2026** | **Ciclo 04-21/05/2026: 16 cadastros novos (5 B2B, 2 fornec, 1 retirada sócios, 5 desp admin, 2 impostos, 1 taxa, 2 outras saídas); razão social dos extratos; regra Pedro Henrique = Retirada Sócios; Paulo Broglio = Guinho+Lu (confirmado); SAQUE DIN ATM Soemes qualquer valor; correção estrutural R73/aplicações** |

---

**FIM DA TABELA MESTRA — VERSÃO 2.0**

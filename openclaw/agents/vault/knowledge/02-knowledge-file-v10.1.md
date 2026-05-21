# KNOWLEDGE FILE: Fluxo de Caixa GB GRUPO — Processamento via Extratos Bancários
## Versão 10.1 — Correções Estruturais + Cadastros (Maio 2026)

---

# 🎯 NOVO FLUXO DE TRABALHO

A partir de maio/2026, o processamento do fluxo de caixa **NÃO usa mais o formulário Excel de movimentações**. Os dados são extraídos diretamente dos **extratos PDF do Itaú** das 7 contas operacionais do grupo + informações complementares fornecidas pelo Pedro/Simone.

## Fonte de dados primária

| Tipo | Origem |
|------|--------|
| Movimentação bancária | **7 extratos PDF do Itaú** (um por conta) |
| GAVETA (caixa físico) | Pedro informa manualmente (ou "sem movimento") |
| Saldo em Aplicações/Fundos | Pedro informa (ou "sem aplicações") |
| Classificações ambíguas | Simone/Pedro confirmam quando perguntado |

## Interpretação importante

⚠️ **A planilha DFC POR CNPJ representa APENAS a conta principal Itaú de cada empresa**, NÃO a posição consolidada de todas as contas bancárias da empresa.

Consequência: PIX recebidos do mesmo CNPJ (ex: "GB COMERCIO → GB COMERCIO") representam dinheiro vindo de OUTRA conta bancária da mesma empresa em outro banco. Esses lançamentos vão para **Outras Entradas Operacionais (linha 13)** porque, do ponto de vista da conta Itaú, é uma entrada real.

---

# ❌ REGRAS MÁXIMAS — PRIORIDADE ABSOLUTA

## 1. NUNCA Alterar Fórmulas (Células Cinza)

As planilhas têm células de fórmula identificadas pela cor **CINZA (FFF5F5F5)**. Essas células **NUNCA** devem ser alteradas — apenas as células **AMARELAS (FFFFF2CC)** podem receber valores.

| Tipo | Cor | Ação |
|------|-----|------|
| Entrada de dados | 🟡 AMARELA (FFFFF2CC) | ✅ Inserir valor |
| Fórmula | ⬜ CINZA (FFF5F5F5) | ❌ NUNCA alterar |
| Cabeçalho | 🟢 Verde escuro | ❌ Não alterar estrutura |

⚠️ **EXCEÇÃO IMPORTANTE descoberta no ciclo de maio/2026 (v10.1):**
Na DFC POR CNPJ, a linha **R73 (SALDO INICIAL)** aparece com cor CINZA nas colunas B-I, **mas essas células estão VAZIAS e SÃO editáveis** — é onde se insere o saldo inicial de cada empresa. A célula de fórmula real é a **J73** (`=SUM(B73:I73)`). Regra prática: **preencher B73:I73, NUNCA tocar J73.** A cor cinza aqui é herança visual, não indica fórmula.

## 2. NUNCA Desproteger Planilhas (Quando Protegidas)

Se a planilha estiver protegida (`ws.protection.sheet = True`), NÃO desproteger. As versões v9+ vêm **sem proteção ativa** (confirmado em maio/2026: ambas as planilhas vieram com `protection.sheet = False`), mas a regra de não-alteração de fórmulas se mantém **independentemente do status de proteção**.

## 3. SEMPRE Validar Coluna Antes de Inserir na Consolidada

Antes de qualquer inserção na DFC DIÁRIO REALIZADO, validar que `mês == mês_esperado` e `dia == dia_esperado` na coluna calculada.

---

# 📁 ARQUIVOS PADRÃO

## Planilhas de Trabalho (Reutilizadas Todo Mês)

| Arquivo | Descrição | Quando usar |
|---------|-----------|-------------|
| **DFC POR CNPJ - [MÊS] 2026.xlsx** | Planilha mensal, 31 abas (`01 de [Mês]` … `31 de [Mês]`) | Trocar de planilha a cada mês |
| **DFC DIARIO REALIZADO - 2026.xlsx** | Planilha anual consolidada (1 sheet chamada "DFC") | A MESMA o ano todo |

⚠️ **Nome das abas da DFC POR CNPJ:** o formato é `{DD:02d} de {Mês}` por extenso em português — ex: `04 de Maio`, `21 de Maio`. (Confirmado maio/2026.)

## Fluxo do Pedro

```
1. Pedro envia 7 extratos PDF do Itaú do período
2. Pedro envia (se necessário) mensagem com classificações ambíguas
3. Pedro envia as 2 planilhas padrão (DFC POR CNPJ do mês + DFC DIARIO)
4. Claude processa e devolve as 2 planilhas preenchidas
```

---

# 🏢 ESTRUTURA DAS 8 EMPRESAS DO GRUPO

| Empresa | CNPJ | Conta Itaú | Coluna CNPJ |
|---------|------|------------|:---:|
| **GB MATRIZ** | 58.151.616/0001-43 | 0099339-0 | **B** (2) |
| **GB FILIAL** | 58.151.616/0002-24 | 0099338-2 | **C** (3) |
| **CONCEPT** | 58.818.245/0001-00 | 0099340-8 | **D** (4) |
| **GB COMERCIO** | 07.194.128/0001-82 | 0037332-0 | **E** (5) |
| **BROGLIO IMP** | 63.922.116/0001-06 | 0021526-5 | **F** (6) |
| **TRADES UP** | 45.200.547/0001-79 | 0099310-1 | **G** (7) |
| **S.P BROGLIO** | 97.546.173/0001-41 | 0099795-3 | **H** (8) |
| **GAVETA** | Caixa físico | — | **I** (9) |
| **CONSOLIDADO** | Fórmula =SUM(B:I) | — | **J** (10) |

⚠️ **Nomes nos extratos PDF (razão social pode variar):**
- GB MATRIZ aparece como **"GB IMPORTADORA E COMERCIO LTDA"** (CNPJ 0001-43)
- GB FILIAL aparece como **"GB IMPORTADORA E COMERCIO LTDA"** (CNPJ 0002-24)
- CONCEPT aparece como **"CONCEPT SERV ASS EMPR LTDA"**
- GB COMERCIO aparece como **"GB COM DE IMP E EXP LTDA"**
- BROGLIO IMP aparece como **"BROGLIO IMP E EXPORTACAO LTDA"**
- TRADES UP aparece como **"TRADES UP IMP E EXP LTDA"**
- S.P BROGLIO aparece como **"S P BROGLIO"**

A identificação correta é **sempre pela conta Itaú + CNPJ**, nunca só pela razão social.

```python
MAPA_COLUNAS = {
    'GB MATRIZ': 2, 'GB FILIAL': 3, 'CONCEPT': 4, 'GB COMERCIO': 5,
    'BROGLIO IMP': 6, 'TRADES UP': 7, 'S.P BROGLIO': 8, 'GAVETA': 9
}

MAPA_CONTA_ITAU_EMPRESA = {
    '0099339-0': 'GB MATRIZ',
    '0099338-2': 'GB FILIAL',
    '0099340-8': 'CONCEPT',
    '0037332-0': 'GB COMERCIO',
    '0021526-5': 'BROGLIO IMP',
    '0099310-1': 'TRADES UP',
    '0099795-3': 'S.P BROGLIO',
}
```

---

# 📋 TABELA MESTRA DE CLASSIFICAÇÃO

Esta tabela é **a referência principal** para classificar cada lançamento do extrato. A regra primária é **CNPJ/CPF** do contraparte; a descrição é auxiliar.

## ENTRADAS

### 🛒 Marketplaces (linha 11)

| CNPJ | Razão Social |
|------|--------------|
| 38.372.267/0001-82 | SHPP BRASIL (Shopee) |
| 15.436.940/0001-03 | AMAZON SERVICOS DE VAREJO |
| 10.573.521/0001-91 | MERCADO PAGO (quando recebimento) |

Padrões de descrição:
- `PIX RECEBIDO SHPP BR...`
- `TED 755.1306.AMAZON S D`
- `SISPAG MAST/ELO/VISA/AMEX` (chargeback de cartões Amazon)

### 🏢 B2B Atacado (linha 9)

**Regra:** PIX RECEBIDO ou BOLETO RECEBIDO de **pessoa jurídica** (CNPJ) que NÃO seja marketplace, NÃO seja outra empresa do grupo, e NÃO esteja em outra categoria.

Catalogados:
| CNPJ | Razão Social |
|------|--------------|
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
| 🆕 37.604.776/0001-20 | CAROLINA BUENO UTTEMBERGHE (CNPJ — atacado) |
| 🆕 42.688.296/0001-25 | MARCHPEL INDUSTRIA E COMERCIO LTDA |
| 🆕 37.439.225/0001-59 | SAMANTA DE CARVALHO MASSONI (CNPJ — atacado) |

Também classifica como B2B: `BOLETOS RECEBIDOS DD/MMS` (sem identificação clara).

### 🛍️ B2C Varejo (linha 10)

**Regra:** PIX RECEBIDO de **pessoa física** (CPF) com valor compatível com varejo.

Catalogados:
| CPF | Nome |
|-----|------|
| 496.013.968-45 | KAUAN HENRIQUE VIGATO |
| 474.300.308-31 | LARINA MARIA DA SILVA LIMA |
| 290.470.548-14 | ERLON RODRIGO ADABO |
| 366.081.508-06 | YASMIN CAROLINE OSCARLINO (quando RECEBIDO) |
| 457.047.138-23 | LEONARDO BASSETO RODRIGUES (quando RECEBIDO) |
| 077.823.918-73 | SANDRA PERON (quando RECEBIDO) |

Também classifica como B2C: `DEP DIN ATM` (depósito em dinheiro via caixa eletrônico).

### 💰 Juros (linha 12)

Padrões de descrição:
- `REND PAGO APLIC AUT MAIS`
- `REND PAGO APLIC AUT APR`
- **Centavos residuais do Maxi não-extratado** — ver regra detalhada em "Erros Comuns #5". Lançar a diferença (saldo do extrato − saldo calculado) como Juros na **última data com movimento de cada empresa**.

### 🔥 Outras Entradas Operacionais (linha 13)

**Caso principal:** PIX RECEBIDO da PRÓPRIA empresa (mesmo CNPJ EXATO da conta de origem). Significa que veio de outra conta bancária da mesma empresa que não temos extrato.

Exemplos catalogados:
- "PIX RECEBIDO GB COME" na conta da GB COMERCIO (07.194.128/0001-82 — mesmo CNPJ)
- "PIX RECEBIDO S. P. B" na conta da S.P BROGLIO (97.546.173/0001-41 — mesmo CNPJ)
- "RECEBIMENTOS GB IMPORTADORA" entre contas de mesmo CNPJ EXATO

⚠️ **Atenção:** GB MATRIZ (58.151.616/0001-43) e GB FILIAL (58.151.616/0002-24) têm o mesmo CNPJ raiz mas são empresas DIFERENTES (matriz e filial separadas). Transferências entre elas SÃO transferências internas legítimas (linha 69), não "mesma empresa".

---

## SAÍDAS

### 🏭 Fornecedores Nacionais (linha 23)

| CNPJ/CPF | Razão Social |
|----------|--------------|
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
| **096.856.098-96** | **PAULO BROGLIO** ⚠️ (regra especial — ver abaixo) |
| 🆕 61.780.392/0001-43 | FABIO LUIZ BASSANI |
| 🆕 155.928.948-13 | CLEUNICE MARIA DE PAULA ROCHA (CPF) |

#### ⚠️ Regra Especial: Paulo Broglio (096.856.098-96)

**Por padrão:** todo PIX para Paulo Broglio é **Fornec Nacional**, NÃO Retirada de Sócios.

**Motivo:** A empresa paga os fornecedores **"Guinho Canecas" e "Lu Porcelanas"** via PF do sócio (cheques próprios + empréstimo da Caixa repassados).

**✅ Confirmado em maio/2026 pela Simone/Pedro:** regra continua vigente. Paulo Broglio = Fornec Nacional mesmo nos meses em que há pró-labore de OUTROS sócios (ex: Pedro Henrique). Não confundir os dois.

**⚠️ Validação obrigatória a cada novo período:** confirmar com Simone se a regra continua vigente.

### 👥 Salários (linha 27)

**Pedro Octavio é SEMPRE Salários**, em qualquer conta. Confirmado pela Simone.

| CPF | Nome |
|-----|------|
| **429.434.788-06** | **PEDRO OCTAVIO BUENO FERNANDES** (sempre) |
| 562.055.698-09 | GUILHERME DOS SANTOS HIGASHI |
| 077.823.918-73 | SANDRA PERON (quando ENVIADO) |
| 450.135.498-41 | FRANCIELE CAROLINA DE SOUZA AGUIAR |
| 461.175.998-97 | MATEUS EDUARDO LISBOA SANTOS |
| 494.206.548-85 | GEZIELE BATISTA DA SILVA |
| 493.044.648-11 | LUCAS GABRIEL LAURENTINO |
| 457.047.138-23 | LEONARDO BASSETO RODRIGUES (quando ENVIADO) |
| 366.081.508-06 | YASMIN CAROLINE OSCARLINO (quando ENVIADO) |
| 381.177.168-01 | ADRIANA SANTOS DE MORAES DA COSTA |

**Padrão identificador de folha:** múltiplos PIX para CPFs no mesmo dia (geralmente dia 06 ou outra data próxima do início do mês), na GB COMERCIO.

### 🏛️ Impostos (linha 25)

| CNPJ / Identificador | Descrição |
|------|-----------|
| 46.410.775/0001-36 | PM PEDREIRA (Tributo Municipal) |
| 00.394.460/0058-87 | DARF / SIMPLES NACIONAL (`PAGAMENTOS TRIB COD BARRAS`) |
| 🆕 46.410.866/0001-71 | MUNICIPIO DE JAGUARIUNA (taxa prefeitura) |
| 🆕 `INT IPVA-SP...` | Parcelamento de IPVA (ex: `INT IPVA-SPGER3359PARC05`) |

Padrões: `PAGAMENTOS TRIB MUNICIPAL`, `PAGAMENTOS TRIB COD BARRAS` (DARF / Simples Nacional), `DAS MEI`, `INT IPVA-SP...`.

⚠️ Nota: o CNPJ 00.394.460/0058-87 é o identificador genérico de arrecadação federal (DARF e Simples Nacional). A descrição (`DARF` vs `SIMPLES NACIONAL`) diferencia, mas ambos vão para Impostos (linha 25).

### 🏢 Despesas Administrativas (linha 28)

| CNPJ / Identificador | Descrição |
|------|-----------|
| 65.422.339/0001-21 | UNIMED AMPARO (plano de saúde) |
| 49.458.269/0001-05 | FOUR ASSESSORIA EMPRESARIAL (contabilidade) |
| 20675554688 (ident.) | VIVO-SP (`DA VIVO-SP`) |
| 28.862.503/0001-95 | C.L. MONITORAMENTO E ALARMES |
| 26.855.879/0001-47 | CONCEPT CENTRO DE NEGOCIOS (aluguel/coworking) |
| 🆕 10.409.865/0001-60 | JR PRINT (empresa de impressoras) |
| 🆕 522.222.668-90 | JOAO PEDRO CASTELLANI DO PRADO (impressoras) |
| 🆕 01.663.516/0001-89 | INTERCARD SERVICOS MEDICOS |
| 🆕 01.109.184/0001-95 | UNIVERSO ONLINE / UOL (marketing digital) |
| 🆕 46.129.490/0001-21 | ASSOCIACAO COMERCIAL E EMPRESARIAL DE PEDREIRA |

⚠️ **JR Print (10.409.865/0001-60) e João Pedro Castellani (522.222.668-90)** são da empresa de impressoras — **Despesa Administrativa**, NÃO fornecedor. (Confirmado Pedro, maio/2026.)

### 💸 Taxas (linha 26)

Padrões de descrição (sem CNPJ específico — são tarifas Itaú):
- `TAR PLANO ADAPT`
- `TAR CONTR/RENOV CTA GAR`
- `TAR COBRANCA EXP`
- `TAR SAQUE PESSOAL`
- `IOF` (qualquer)
- 🆕 `SISDEB REDECARD S A` (taxa de maquininha Redecard)

### 📊 Pagamento de Juros (linha 61)

| Padrão | Origem |
|--------|--------|
| `JUROS 0012.05491-2` | Juros de cheque especial Itaú |
| **`SAQUE DIN ATM`** (na conta GB COMERCIO) | **Juros do empréstimo Soemes** (saque em espécie) |

⚠️ **Confirmado maio/2026:** TODOS os `SAQUE DIN ATM` na GB COMERCIO são juros Soemes, **independentemente do valor** (foram vistos saques de R$ 1.000, R$ 1.500 e R$ 2.000, todos Soemes). Confirmar caso a caso para outras empresas.

### 🤝 Retirada de Sócios (linha 62)

| CPF | Nome |
|-----|------|
| 🆕 **347.048.378-74** | **PEDRO HENRIQUE PERON BROGLIO** (pró-labore semanal) |

⚠️ **Regra nova (maio/2026):** Pedro Henrique Peron Broglio recebe **pró-labore semanal = Retirada de Sócios**. NÃO confundir com Paulo Broglio (que é Fornecedor). Os dois podem aparecer no mesmo dia, mesma conta, valores parecidos — mas têm classificações diferentes.

### 🗂️ Outras Saídas Operacionais (linha 29)

| Identificador | Descrição |
|---------------|-----------|
| 00.000.000/0452-92 | BANCO DO BRASIL — boletos do **treinamento profissional G4 dos sócios** |
| 90.400.888/0001-42 | SANTANDER NEGOCIOS PLAT MC — boletos do **treinamento G4** |
| 51.174.001/0001-93 | SAO PAULO TRIBUNAL DE JUSTICA (depósito judicial) |
| `CONS PARCELA ...` | **Consórcio imobiliário** |
| `PAGAMENTOS PIX QR-CODE` (sem identificação clara) | Caso genérico |
| `PAGAMENTOS PIX QR-CODE SHPP/MERC PAGO` | Estornos/devoluções de marketplaces |
| 🆕 34.028.316/0001-03 | CORREIOS / ECT (postagem/frete) |
| 🆕 00.360.305/0001-04 | `PAGAMENTOS PIX QR-CODE CEF MATRIZ` (Caixa Econômica) |

⚠️ **PIX QR-CODE CEF Matriz (00.360.305/0001-04)** — Outras Saídas. (Confirmado Pedro, maio/2026.)

---

## TRANSFERÊNCIAS INTERNAS (linha 69)

⚠️ **Critério rigoroso:** só é transferência interna quando o CNPJ de destino é **DIFERENTE** do CNPJ da conta de origem, mas ambos pertencem ao grupo (8 empresas).

### Transferências legítimas catalogadas

Casos vistos no período 04-21/05/2026 (exemplos reais):
- GB MATRIZ ↔ GB FILIAL (CNPJs 0001-43 ↔ 0002-24)
- CONCEPT ↔ TRADES UP
- GB COMERCIO ↔ TRADES UP
- Qualquer combinação entre as 8 empresas

### NÃO é transferência interna

| Tipo | Tratamento |
|------|------------|
| `PIX RECEBIDO GB COME` na própria GB COMERCIO (mesmo CNPJ exato) | **Outras Entradas (linha 13)** |
| `PIX RECEBIDO S. P. B` na própria S.P BROGLIO | **Outras Entradas (linha 13)** |
| `PIX ENVIADO GB COMERCIO` para mesma GB COMERCIO em outra conta | **Outras Saídas (linha 29)** — mas confirmar caso a caso |
| Espelho de transferência interna (já contado uma vez) | Ignorar a segunda ocorrência |

### Validação obrigatória

A soma das transferências (linha 69) de todas as 8 empresas no mesmo dia **DEVE SER ZERO**:

```python
def validar_transferencias(ws_cnpj):
    total = sum(
        ws_cnpj.cell(row=69, column=col).value or 0
        for col in range(2, 10)
    )
    assert abs(total) < 0.01, f"Transferências não balanceiam: {total}"
```

✅ **Validado maio/2026:** dia 6 (GB Matriz↔Filial R$1.100), dia 13 (GB Matriz↔Filial R$600 + Concept↔Trades Up R$600), dia 18 (GB Comércio↔Trades Up R$1.100). Todos zeraram.

---

## LANÇAMENTOS A IGNORAR

| Padrão | Motivo |
|--------|--------|
| `SALDO ANTERIOR` / `SALDO TOTAL DISPONÍVEL DIA` / `SALDO EM CONTA CORRENTE` | Linhas informativas |

⚠️ **Nota:** `SALDO ANTERIOR` (data 30/04 em maio) é o **saldo inicial** de cada empresa — não é lançamento, mas é o valor que vai no R73 (saldo inicial). `SALDO EM CONTA CORRENTE` (data do último dia) é o **saldo final** que deve bater com o cálculo.

---

# 📊 ESTRUTURA DA PLANILHA DFC POR CNPJ

## Layout (cada aba = 1 dia, nome `{DD:02d} de {Mês}`)

```
R1-R3:  Cabeçalhos
R5:     CNPJS | GB MATRIZ | GB FILIAL | CONCEPT | GB COMERCIO | BROGLIO IMP | TRADES UP | S.P BROGLIO | GAVETA | CONSOLIDADO

R7:     FLUXO OPERACIONAL
R8:     ENTRADAS DE CAIXA (OPERACIONAL)
R9:     Recebimentos de Clientes — B2B                    🟡 dados
R10:    Recebimentos de Clientes — B2C                    🟡 dados
R11:    Recebimentos de Marketplaces                      🟡 dados
R12:    Recebimentos de Juros                             🟡 dados
R13:    Outras Entradas Operacionais                      🟡 dados
R14:    TOTAL ENTRADAS OPERACIONAIS                       ⬜ =SUM(B9:B13)

R16:    SAÍDAS DE CAIXA (OPERACIONAL)
R17:    Pagamentos de Importação — Sinal (30%)            🟡 dados
R18:    Pagamentos de Importação — Saldo (70%)            🟡 dados
R19:    Pagamentos de Frete Internacional                 🟡 dados
R20:    Pagamentos de Seguro Internacional                🟡 dados
R21:    Pagamentos de Despachante Aduaneiro               🟡 dados
R22:    Pagamentos de Armazenagem/Capatazia/THC           🟡 dados
R23:    Pagamentos a Fornecedores Nacionais               🟡 dados
R24:    Pagamentos de Frete Nacional                       🟡 dados
R25:    Pagamentos de Impostos                            🟡 dados
R26:    Pagamentos de Taxas e Emolumentos                 🟡 dados
R27:    Pagamentos de Salários e Encargos                 🟡 dados
R28:    Despesas Administrativas — Operacionais           🟡 dados
R29:    Outras Saídas Operacionais                        🟡 dados
R30:    TOTAL SAÍDAS OPERACIONAIS                         ⬜ =SUM(B17:B29)
R32:    CAIXA LÍQUIDO DAS ATIVIDADES OPERACIONAIS         ⬜ =B14-B30

R34:    FLUXO DE INVESTIMENTO
R35:    ENTRADAS DE INVESTIMENTO
R36:    Venda de Ativos                                   🟡 dados
R37:    Resgate de Aplicações Financeiras                 🟡 dados
R38:    Outras Entradas de Investimento                   🟡 dados
R39:    TOTAL ENTRADAS INVESTIMENTO                       ⬜ =SUM(B36:B38)
R41:    SAÍDAS DE INVESTIMENTO
R42:    Aplicações Financeiras                            🟡 dados
R43:    Compra de Máquinas e Equipamentos                 🟡 dados
R44:    Compra de Móveis e Estruturas                     🟡 dados
R45:    Compra de Moldes                                  🟡 dados
R46:    Investimentos em Sistemas / TI                    🟡 dados
R47:    Outras Saídas de Investimento                     🟡 dados
R48:    TOTAL SAÍDAS INVESTIMENTO                         ⬜ =SUM(B42:B47)
R50:    CAIXA LÍQUIDO DAS ATIVIDADES DE INVESTIMENTO      ⬜ =B39-B48

R52:    FLUXO DE FINANCIAMENTO
R53:    ENTRADAS DE FINANCIAMENTO
R54:    Empréstimos e Financiamentos Tomados              🟡 dados
R55:    Aporte de Sócios                                  🟡 dados
R56:    Outras Entradas de Financiamento                  🟡 dados
R57:    TOTAL ENTRADAS FINANCIAMENTO                      ⬜ =SUM(B54:B56)
R59:    SAÍDAS DE FINANCIAMENTO
R60:    Pagamento de Principal de Empréstimos             🟡 dados
R61:    Pagamento de Juros                                🟡 dados
R62:    Retirada de Sócios (Capital Próprio)              🟡 dados
R63:    Outras Saídas de Financiamento                    🟡 dados
R64:    TOTAL SAÍDAS FINANCIAMENTO                        ⬜ =SUM(B60:B63)
R66:    CAIXA LÍQUIDO DAS ATIVIDADES DE FINANCIAMENTO     ⬜ =B57-B64

R68:    MOVIMENTAÇÕES INTERNAS (FORA DO DFC)
R69:    Transferência entre Contas                        🟡 dados (com SINAL)
R70:    TOTAL MOVIMENTAÇÕES INTERNAS                      ⬜ =B69

R72:    VARIAÇÃO LÍQUIDA DE CAIXA (DFC)                   ⬜ =B32+B50+B66
R73:    SALDO INICIAL DE CAIXA                            🟡 dados B-I (ver nota) / ⬜ J73 fórmula
R74:    SALDO FINAL DE CAIXA                              ⬜ =B73+B72

R76:    REGRAS (texto informativo) — NÃO é "Saldo Aplicações"
```

⚠️ **CORREÇÃO v10.1 (importante):**
- A linha **R73** nas colunas B-I (empresas) é onde se insere o **saldo inicial de cada empresa** (valor do `SALDO ANTERIOR` de 30/04 ou saldo final do dia anterior). Apesar da cor cinza, essas células vêm vazias e são editáveis. A **J73** é fórmula (`=SUM(B73:I73)`) — nunca tocar.
- **NÃO existe linha 76/77 de "Saldo em Aplicações" nesta planilha** (diferente do que a v10.0 dizia). A R76 é apenas o texto de REGRAS. O controle de aplicações fica só na CONSOLIDADA (R73 dela).

## Linhas de FÓRMULA (NUNCA ALTERAR)

```python
LINHAS_FORMULA_CNPJ = {14, 30, 32, 39, 48, 50, 57, 64, 66, 70, 72, 74}
# (Removido o 77 da v10.0 — não existe nesta planilha)
# A J73 é fórmula, mas B73:I73 são dados editáveis.
```

## Coluna J (CONSOLIDADO)

Todas as linhas na coluna J contêm `=SUM(B{n}:I{n})`. Inclui J73.

## Saldo inicial encadeado

⚠️ **Regra:** o saldo inicial (R73) de cada empresa em cada dia COM movimento = saldo final (R74) do dia anterior com movimento da mesma empresa. O primeiro dia do mês usa o `SALDO ANTERIOR` do extrato. Dias sem movimento (fins de semana) não têm aba preenchida.

---

# 📊 ESTRUTURA DA PLANILHA DFC DIÁRIO REALIZADO (CONSOLIDADA)

## Bases de Coluna por Mês (2026)

```python
BASES_MESES_2026 = {
    'JANEIRO': 1,    'FEVEREIRO': 33,  'MARCO': 62,    'ABRIL': 94,
    'MAIO': 125,     'JUNHO': 157,     'JULHO': 188,   'AGOSTO': 220,
    'SETEMBRO': 252, 'OUTUBRO': 283,   'NOVEMBRO': 315,'DEZEMBRO': 346,
}
# coluna_do_dia = BASE + dia
# Ex: MAIO dia 14 → coluna 125 + 14 = 139  ✅ confirmado
# Ex: MAIO dia 1  → coluna 125 + 1  = 126  ✅ confirmado
```

⚠️ **Nota v10.1:** há uma coluna "Total" intercalada em cada mês (ex: col 125 = "Total" de maio, antes do dia 1 na col 126). A fórmula `BASE + dia` continua correta. **SEMPRE validar** `cell(row=4,col)` = mês e `cell(row=5,col)` = dia antes de escrever.

## Layout (única aba "DFC")

```
R4:     MÊS (JANEIRO, FEVEREIRO, ..., DEZEMBRO)
R5:     DIA (1, 2, ..., 31, "Total")

R7:     FLUXO OPERACIONAL
R8:     ENTRADAS DE CAIXA (OPERACIONAL)
R9-R13: dados (5 categorias)
R14:    TOTAL ENTRADAS                                    ⬜ fórmula
R16:    SAÍDAS DE CAIXA (OPERACIONAL)
R17-R29:dados (13 categorias)
R30:    TOTAL SAÍDAS                                      ⬜ fórmula
R31:    CAIXA LÍQUIDO DO FLUXO OPERACIONAL ◀              ⬜ =[col]14-[col]30

R33-R48:FLUXO DE INVESTIMENTO (mesma estrutura)
R50-R63:FLUXO DE FINANCIAMENTO (mesma estrutura)

R65-R67:MOVIMENTAÇÕES INTERNAS
R69:    VARIAÇÃO LÍQUIDA DE CAIXA (DFC)                   ⬜ =[col]31+[col]48+[col]63
R70:    SALDO INICIAL DE CAIXA                            🟡 dados
R71:    SALDO FINAL DE CAIXA                              ⬜ =[col]70+[col]69

R73:    SALDO EM APLICAÇÕES/FUNDOS                        🟡 dados
R74:    SALDO TOTAL (CAIXA + APLICAÇÕES)                  ⬜ =[col]71+[col]73
```

◀ A linha 31 (Caixa Líquido Operacional) é o **indicador crítico de saúde financeira** do negócio.

⚠️ **CORREÇÃO v10.1 — SALDO INICIAL R70 (consolidada):**
O R70 de cada dia com movimento = **saldo do GRUPO INTEIRO** (soma das 7 empresas) no início daquele dia, **encadeado dia a dia** a partir da soma dos saldos de 30/04. NÃO é a soma só das empresas que se moveram naquele dia. O saldo final (R71) de um dia deve ser igual ao saldo inicial (R70) do próximo dia com movimento. As fórmulas R71/R69/R31 usam referência relativa à coluna (ex: `=EP70+EP69`), então o encadeamento depende do R70 estar correto.

## Linhas de FÓRMULA (NUNCA ALTERAR)

```python
LINHAS_FORMULA_CONS = {14, 30, 31, 38, 47, 48, 55, 62, 63, 67, 69, 71, 74}
```

---

# 🔗 MAPEAMENTO LINHAS CNPJ ↔ CONSOLIDADA

```python
MAPA_CNPJ_CONS = {
    # Operacional
    9:9, 10:10, 11:11, 12:12, 13:13,
    17:17, 18:18, 19:19, 20:20, 21:21, 22:22,
    23:23, 24:24, 25:25, 26:26, 27:27, 28:28, 29:29,
    # Investimento
    36:35, 37:36, 38:37,
    42:41, 43:42, 44:43, 45:44, 46:45, 47:46,
    # Financiamento
    54:52, 55:53, 56:54,
    60:58, 61:59, 62:60, 63:61,
    # Transferências e saldos
    69:66,
    # Saldo inicial: CNPJ R73 → Consolidada R70 (offset diferente!)
    73:70,
    # Saldo aplicações: só na consolidada R73 (não há equivalente no CNPJ)
}
```

⚠️ **Atenção:** No CNPJ a linha de saldo inicial é R73, na consolidada é R70. Mas na prática, o saldo inicial da consolidada NÃO é a simples soma dos R73 do dia — é o saldo do grupo inteiro encadeado (ver correção acima).

---

# 🔄 FLUXO COMPLETO DE PROCESSAMENTO

## ANTES de Começar

### 1. Receber arquivos do Pedro
- [ ] **7 extratos PDF** do Itaú do período
- [ ] **DFC POR CNPJ - [MÊS] 2026.xlsx** (planilha mensal correta)
- [ ] **DFC DIARIO REALIZADO - 2026.xlsx** (planilha anual)
- [ ] Mensagem/contexto com classificações ambíguas (se houver)

### 2. Perguntar ao Pedro (proativamente)
- [ ] **GAVETA tem movimento no período?** Se sim, pedir saldos inicial/final e lançamentos
- [ ] **Saldo em aplicações financeiras?** Se sim, pedir saldo final por empresa
- [ ] **Pro-labore foi feito no período?** (se vir PIX para Paulo Broglio OU Pedro Henrique)
- [ ] **Itens novos identificados?** Listar os não catalogados e pedir classificação

### 3. Validar período
- [ ] Verificar que o mês do extrato corresponde à planilha DFC POR CNPJ enviada
- [ ] Identificar dias úteis (dias com movimentação real)
- [ ] Considerar feriados nacionais e regionais

## DURANTE o Processamento

### 4. Extração dos extratos
- [ ] Para cada uma das 7 contas, extrair todos os lançamentos
- [ ] Capturar saldo inicial (`SALDO ANTERIOR` - dia anterior ao primeiro)
- [ ] Capturar saldo final (`SALDO EM CONTA CORRENTE`)
- [ ] Anotar centavos de Maxi não-extratados (diferença entre último `SALDO TOTAL DISPONÍVEL DIA` e `SALDO EM CONTA CORRENTE`)

### 5. Classificação
- [ ] Aplicar a Tabela Mestra (regra primária: CNPJ/CPF)
- [ ] Itens não catalogados → separar e perguntar ao Pedro
- [ ] Detectar transferências entre empresas do grupo (cruzar entradas/saídas)
- [ ] Detectar movimentos entre contas da mesma empresa → Outras Entradas/Saídas

### 6. Validação prévia (em memória, antes de tocar nas planilhas)
- [ ] Para cada empresa: saldo_inicial + variação = saldo_final do extrato (tolerância R$ 0,01)
- [ ] Soma de transferências = R$ 0,00 por dia
- [ ] Centavos Maxi do último dia lançados como Juros para fechar contas

### 7. Inserção na DFC POR CNPJ
- [ ] Abrir a aba correta para cada dia (`{DD:02d} de {Mês}`)
- [ ] Preencher saldo inicial (B73:I73) das empresas com movimento naquele dia
- [ ] Preencher lançamentos nas linhas corretas (todos com **valor positivo**, exceto transferências que mantêm sinal)
- [ ] **NUNCA** tocar em linhas de fórmula nem na J73
- [ ] Para múltiplos lançamentos na mesma categoria/dia/empresa: **SOMAR** antes de inserir

### 8. Inserção na CONSOLIDADA
- [ ] Calcular `coluna = BASE_DO_MES + dia`
- [ ] **VALIDAR**: ler `cell(row=4, col)` = nome do mês ✅ e `cell(row=5, col)` = dia ✅
- [ ] Consolidar valores das 8 empresas por linha (somar)
- [ ] Inserir saldo inicial consolidado (R70) = saldo do GRUPO INTEIRO encadeado dia a dia
- [ ] Inserir lançamentos consolidados nas linhas mapeadas

## APÓS o Processamento

### 9. Validações finais
- [ ] Conferir saldo final de cada empresa na aba do último dia com movimento
- [ ] Conferir saldo final consolidado (R71 do último dia) = soma dos saldos finais das 7 empresas
- [ ] Recalcular com LibreOffice e verificar encadeamento de saldos dia a dia (sem quebras)
- [ ] Conferir que todas as fórmulas estão intactas em ambas as planilhas (comparar antes/depois)

### 10. Conversão e Entrega
- [ ] Converter DFC POR CNPJ via LibreOffice (XLSX → ODS → XLSX)
- [ ] Converter DFC DIARIO via LibreOffice (XLSX → ODS → XLSX)
- [ ] Apresentar ambos os arquivos via `present_files`

---

# 💻 CÓDIGO DE REFERÊNCIA

Os scripts funcionais ficam na skill `skills/financeiro/cash-flow-extract-processor/scripts/`. Este Knowledge File é a documentação canônica das regras; os scripts implementam o workflow.

Constantes principais centralizadas em `scripts/_constants.py`:
- `MAPA_COLUNAS`, `MAPA_CONTA_ITAU_EMPRESA`, `MAPA_CNPJ_EMPRESA`
- `CAT_LINHA_CNPJ`, `MAPA_CNPJ_CONS`
- `LINHAS_FORMULA_CNPJ`, `LINHAS_FORMULA_CONS`
- `BASES_MESES_2026`
- `LINHAS_ENT_OP/INV/FIN`, `LINHAS_SAI_OP/INV/FIN`
- `CNPJ_MARKETPLACES`, `CPF_PAULO_BROGLIO`, `CPF_PEDRO_HENRIQUE`, `CPF_PEDRO_OCTAVIO`

## Função de Variação Diária (referência)

```python
def variacao_dia(dados_dia_emp):
    """Calcula variação líquida de caixa do dia para uma empresa
    Recebe dict {linha_cnpj: valor_positivo} (transferências com sinal)
    Retorna Decimal com a variação (+ ou -)
    """
    v = D('0')
    for linha, valor in dados_dia_emp.items():
        if linha == 69:
            v += valor  # transferência: sinal direto
        elif linha in LINHAS_ENT_OP | LINHAS_ENT_INV | LINHAS_ENT_FIN:
            v += valor
        elif linha in LINHAS_SAI_OP | LINHAS_SAI_INV | LINHAS_SAI_FIN:
            v -= valor
    return v
```

## Conversão LibreOffice

```bash
# Para compatibilidade com macOS
libreoffice --headless --convert-to ods "arquivo.xlsx"
libreoffice --headless --convert-to xlsx "arquivo.ods"
rm -f "arquivo.ods"
```

---

# ⚠️ ERROS COMUNS E COMO EVITAR

## 1. Mover entre contas da MESMA empresa = transferência interna?
**NÃO.** Mesma empresa (mesmo CNPJ EXATO) → **Outras Entradas/Saídas Operacionais**, não linha 69.

## 2. Paulo Broglio = Retirada de Sócios?
**NÃO por padrão.** Paulo Broglio = Guinho Canecas + Lu Porcelanas (Fornec Nacional), até que Simone diga o contrário. ⚠️ NÃO confundir com Pedro Henrique Peron Broglio, que É Retirada de Sócios.

## 3. Saque em dinheiro vai sempre para GAVETA?
**NÃO.** Na GB COMERCIO, TODOS os `SAQUE DIN ATM` (qualquer valor) são **juros do empréstimo Soemes** (Pag Juros, linha 61). Confirmar caso a caso para outras empresas.

## 4. SISPAG ELO/MAST/VISA/AMEX da Amazon é o quê?
São **chargebacks de cartão da Amazon** (Marketplaces, linha 11). Entrada positiva.

## 5. Centavos não batem no saldo final
É o **rendimento da aplicação automática Maxi** do Itaú, creditado no próprio dia da geração do extrato mas ainda não listado como linha. Lançar a diferença (sempre poucos centavos) como `Juros` (linha 12) na **última data com movimento de cada empresa**. Ex maio/2026: GB Matriz +0,25; GB Comércio +0,12; Concept +0,03; Broglio +0,02; S.P Broglio +0,01.

## 6. PIX recebido de mesma razão social mas CNPJ diferente
- Mesmo CNPJ raiz, sufixo diferente (ex: 0001-43 vs 0002-24) → empresas DIFERENTES → transferência interna se ambas estão no grupo
- Mesmo CNPJ EXATO → mesma empresa → Outras Entradas

## 7. R73 da DFC POR CNPJ parece fórmula (cinza), posso preencher?
**SIM, nas colunas B-I.** Apesar da cor cinza, B73:I73 vêm vazias e recebem o saldo inicial. Só a J73 é fórmula de verdade — essa nunca tocar.

## 8. JR Print parece fornecedor de impressão?
**NÃO.** JR Print e João Pedro Castellani = empresa de impressoras = **Despesa Administrativa** (linha 28), não Fornecedor.

## 9. Saldo inicial da consolidada (R70) — somar só quem se moveu no dia?
**NÃO.** R70 = saldo do GRUPO INTEIRO encadeado dia a dia. Conferir que o saldo final de um dia = saldo inicial do dia seguinte.

---

# 🚀 PROTOCOLO PARA NOVOS LANÇAMENTOS

Quando aparecer no extrato um CNPJ/CPF **NÃO catalogado** nesta tabela:

1. **Separar** numa seção "ITENS NÃO CATALOGADOS — REQUER CLASSIFICAÇÃO"
2. **Listar** com data, valor, descrição, CNPJ/CPF, e palpite de classificação
3. **Perguntar** ao Pedro antes de processar definitivamente
4. **Atualizar** esta tabela mestra (em conversação) para futuras rodadas
5. A tabela cresce a cada ciclo — quanto mais histórico, menos perguntas

## Template de pergunta

```
Detectei lançamentos não catalogados. Como classificar?

1. [dia] [empresa] [valor] [descrição/CNPJ] → palpite: [categoria]
2. [dia] [empresa] [valor] [descrição/CNPJ] → palpite: [categoria]
...

Opções: Fornec Nacional | Salarios | Desp Admin | Impostos |
        Outras Saidas | B2B | B2C | Marketplaces | Outras Entradas |
        Retirada Socios | Pag Juros | Caso a caso
```

---

# 📋 RESUMO DO QUE O PEDRO PRECISA ENVIAR

## Sempre (em cada processamento)

1. ✅ **7 extratos PDF** do Itaú do período
2. ✅ **DFC POR CNPJ - [MÊS] 2026.xlsx** do mês de referência
3. ✅ **DFC DIARIO REALIZADO - 2026.xlsx** (a mesma o ano todo)

## Conforme o caso

4. ⚠️ **GAVETA**: "sem movimento" OU saldos + lançamentos do período
5. ⚠️ **Aplicações Financeiras**: "sem aplicações" OU saldo final por empresa
6. ⚠️ **Mensagem com classificações** (Simone/Pedro) sobre casos ambíguos
7. ⚠️ **Confirmações** sobre itens não catalogados quando Claude perguntar

---

# 🚨 AVISOS CRÍTICOS FINAIS

| Prioridade | Regra |
|:----------:|-------|
| 🔴 1 | **NUNCA** alterar células de fórmula (cinza) — incluindo J73 CNPJ e R74 Consolidada. (B73:I73 do CNPJ SÃO editáveis) |
| 🔴 2 | **SEMPRE** validar coluna (BASE + dia) antes de inserir na consolidada |
| 🔴 3 | **SEMPRE** garantir que saldo final calculado bate com saldo do extrato |
| 🔴 4 | **SEMPRE** R70 da consolidada = saldo do grupo inteiro encadeado dia a dia |
| 🟡 5 | **SEMPRE** lançar centavos do Maxi não-extratado como Juros no último dia |
| 🟡 6 | **SEMPRE** verificar transferências internas: soma = 0 por dia |
| 🟡 7 | **SEMPRE** acumular valores quando mesma categoria aparece múltiplas vezes |
| 🟡 8 | **SEMPRE** perguntar antes de classificar itens não catalogados |
| 🟢 9 | **SEMPRE** converter via LibreOffice para macOS |
| 🟢 10 | **PROATIVAMENTE** perguntar sobre GAVETA e Aplicações |

---

# 📜 HISTÓRICO DE VERSÕES

| Versão | Data | Alterações |
|:------:|------|------------|
| 7.0 | Dez/2025 | Estrutura 8 empresas |
| 8.0 | Dez/2025 | Regra de proteção como prioridade máxima; checklist operacional |
| 9.0 | Fev/2026 | Novo formulário v2; Saldo Aplicações; Transferências separadas; Bases 2026 |
| 10.0 | Mai/2026 | NOVO FLUXO: extratos PDF como fonte primária; Tabela Mestra consolidada; Regras especiais Paulo Broglio/Pedro Octavio/Soemes; Interpretação "DFC = só conta Itaú"; Protocolo de itens novos |
| **10.1** | **Mai/2026** | **Correções estruturais após 1º ciclo real: R73 CNPJ é B-I editável (J73 fórmula); não há linha 76/77 de aplicações na DFC POR CNPJ; R70 consolidada = grupo inteiro encadeado; coluna "Total" intercalada; nomes de razão social nos extratos. NOVOS CADASTROS: 5 B2B, 2 fornecedores, 5 desp. admin, 2 impostos, 1 taxa, 1 outras saídas; Pedro Henrique Peron Broglio = Retirada Sócios; JR Print/João Pedro Castellani = Desp Admin; SAQUE DIN ATM Soemes qualquer valor; PIX QR CEF Matriz = Outras Saídas** |

---

**FIM DO KNOWLEDGE FILE — VERSÃO 10.1**

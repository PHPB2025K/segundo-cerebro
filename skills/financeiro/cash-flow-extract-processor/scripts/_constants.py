"""Constantes do processador de fluxo de caixa GB Grupo.

Fonte: Knowledge File v10.1 (vault/openclaw/agents/vault/knowledge/02-knowledge-file-v10.1.md).
Se houver divergência → knowledge vence.
"""

from decimal import Decimal

D = Decimal


# ----------------------------------------------------------------------------
# Mapeamento Empresas → Coluna na DFC POR CNPJ
# ----------------------------------------------------------------------------
MAPA_COLUNAS = {
    "GB MATRIZ": 2,
    "GB FILIAL": 3,
    "CONCEPT": 4,
    "GB COMERCIO": 5,
    "BROGLIO IMP": 6,
    "TRADES UP": 7,
    "S.P BROGLIO": 8,
    "GAVETA": 9,
}

# Conta Itaú → Empresa (identificação primária)
MAPA_CONTA_ITAU_EMPRESA = {
    "0099339-0": "GB MATRIZ",
    "0099338-2": "GB FILIAL",
    "0099340-8": "CONCEPT",
    "0037332-0": "GB COMERCIO",
    "0021526-5": "BROGLIO IMP",
    "0099310-1": "TRADES UP",
    "0099795-3": "S.P BROGLIO",
}

# CNPJ → Empresa (validação cruzada)
MAPA_CNPJ_EMPRESA = {
    "58.151.616/0001-43": "GB MATRIZ",
    "58.151.616/0002-24": "GB FILIAL",
    "58.818.245/0001-00": "CONCEPT",
    "07.194.128/0001-82": "GB COMERCIO",
    "63.922.116/0001-06": "BROGLIO IMP",
    "45.200.547/0001-79": "TRADES UP",
    "97.546.173/0001-41": "S.P BROGLIO",
}


# ----------------------------------------------------------------------------
# Categorias → Linha na planilha DFC POR CNPJ
# ----------------------------------------------------------------------------
CAT_LINHA_CNPJ = {
    # Entradas operacionais
    "B2B Atacado": 9,
    "B2C Varejo": 10,
    "Marketplaces": 11,
    "Juros": 12,
    "Outras Entradas": 13,
    # Saídas operacionais
    "Import Sinal": 17,
    "Import Saldo": 18,
    "Frete Internac": 19,
    "Seguro Internac": 20,
    "Despachante": 21,
    "Armazenagem THC": 22,
    "Fornec Nacional": 23,
    "Frete Nacional": 24,
    "Impostos": 25,
    "Taxas": 26,
    "Salarios": 27,
    "Desp Admin": 28,
    "Outras Saidas": 29,
    # Investimento
    "Venda Ativos": 36,
    "Resgate Aplicacoes": 37,
    "Outras Ent Invest": 38,
    "Aplicacoes Fin": 42,
    "Compra Maquinas": 43,
    "Compra Moveis": 44,
    "Compra Moldes": 45,
    "Invest TI": 46,
    "Outras Sai Invest": 47,
    # Financiamento
    "Emprestimos": 54,
    "Aporte Socios": 55,
    "Outras Ent Financ": 56,
    "Pag Principal": 60,
    "Pag Juros": 61,
    "Retirada Socios": 62,
    "Outras Sai Financ": 63,
    # Movimento interno
    "TRANSFERENCIA": 69,
    # Saldo inicial (editável apesar do cinza)
    "SALDO_INICIAL": 73,
}


# ----------------------------------------------------------------------------
# Linhas de FÓRMULA (NUNCA tocar)
# ----------------------------------------------------------------------------
LINHAS_FORMULA_CNPJ = {14, 30, 32, 39, 48, 50, 57, 64, 66, 70, 72, 74}
# J73 também é fórmula (=SUM(B73:I73)) — proteger separadamente
# Coluna J inteira (consolidado) é fórmula

LINHAS_FORMULA_CONS = {14, 30, 31, 38, 47, 48, 55, 62, 63, 67, 69, 71, 74}


# ----------------------------------------------------------------------------
# Bases de coluna por mês — DFC DIARIO REALIZADO 2026
# ----------------------------------------------------------------------------
BASES_MESES_2026 = {
    "JANEIRO": 1,
    "FEVEREIRO": 33,
    "MARCO": 62,
    "ABRIL": 94,
    "MAIO": 125,
    "JUNHO": 157,
    "JULHO": 188,
    "AGOSTO": 220,
    "SETEMBRO": 252,
    "OUTUBRO": 283,
    "NOVEMBRO": 315,
    "DEZEMBRO": 346,
}
# coluna_do_dia = BASE + dia
# Sempre validar cell(4,col) e cell(5,col)

MESES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
]


# ----------------------------------------------------------------------------
# Mapeamento DFC POR CNPJ → DFC DIARIO REALIZADO (linhas)
# ----------------------------------------------------------------------------
MAPA_CNPJ_CONS = {
    # Operacional
    9: 9, 10: 10, 11: 11, 12: 12, 13: 13,
    17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22,
    23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29,
    # Investimento
    36: 35, 37: 36, 38: 37,
    42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46,
    # Financiamento
    54: 52, 55: 53, 56: 54,
    60: 58, 61: 59, 62: 60, 63: 61,
    # Transferências
    69: 66,
    # Saldo inicial: CNPJ R73 → Consolidada R70 (offset diferente!)
    73: 70,
}


# ----------------------------------------------------------------------------
# Classes de linhas (pra cálculo de variação diária)
# ----------------------------------------------------------------------------
LINHAS_ENT_OP = {9, 10, 11, 12, 13}
LINHAS_SAI_OP = {17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}
LINHAS_ENT_INV = {36, 37, 38}
LINHAS_SAI_INV = {42, 43, 44, 45, 46, 47}
LINHAS_ENT_FIN = {54, 55, 56}
LINHAS_SAI_FIN = {60, 61, 62, 63}


# ----------------------------------------------------------------------------
# Marketplaces (CNPJ → entrada Marketplaces linha 11)
# ----------------------------------------------------------------------------
CNPJ_MARKETPLACES = {
    "38.372.267/0001-82": "SHPP BRASIL (Shopee)",
    "15.436.940/0001-03": "AMAZON SERVICOS DE VAREJO",
    "10.573.521/0001-91": "MERCADO PAGO",
}


# ----------------------------------------------------------------------------
# Regras especiais de classificação (CPFs / CNPJs sensíveis)
# ----------------------------------------------------------------------------
# Paulo Broglio: Fornec Nacional (Guinho + Lu Porcelanas), confirmar por período
CPF_PAULO_BROGLIO = "096.856.098-96"
# Pedro Henrique Peron Broglio: Retirada de Sócios (pró-labore semanal)
CPF_PEDRO_HENRIQUE = "347.048.378-74"
# Pedro Octavio: SEMPRE Salários
CPF_PEDRO_OCTAVIO = "429.434.788-06"


# ----------------------------------------------------------------------------
# Padrões de descrição
# ----------------------------------------------------------------------------
PADROES_JUROS = [
    "REND PAGO APLIC AUT MAIS",
    "REND PAGO APLIC AUT APR",
]

PADROES_PAG_JUROS = [
    "JUROS 0012.05491-2",  # cheque especial Itaú
]

PADROES_TAXAS = [
    "TAR PLANO ADAPT",
    "TAR CONTR/RENOV CTA GAR",
    "TAR COBRANCA EXP",
    "TAR SAQUE PESSOAL",
    "IOF",
    "SISDEB REDECARD",
]

PADROES_IGNORAR = [
    "SALDO ANTERIOR",  # informativo — mas é o saldo inicial
    "SALDO TOTAL DISPONIVEL DIA",
    "SALDO EM CONTA CORRENTE",  # informativo — mas é o saldo final
]


# ----------------------------------------------------------------------------
# Tolerâncias
# ----------------------------------------------------------------------------
TOLERANCIA_SALDO = D("0.01")  # R$ 0,01 entre cálculo e extrato
TOLERANCIA_TRANSFERENCIA = D("0.01")  # soma de transferências/dia

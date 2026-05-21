"""Classifica cada lançamento extraído nas categorias da DFC POR CNPJ.

Regra primária: CNPJ/CPF do contraparte. Descrição é auxiliar.

Em caso de item NÃO catalogado:
- Retorna categoria "REQUER_CLASSIFICACAO"
- Pra ser agrupado na lista de perguntas pro Pedro/Simone

Fonte de regras: vault/openclaw/agents/vault/knowledge/03-tabela-mestra-v2.0.md
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _constants import (
    CNPJ_MARKETPLACES,
    CPF_PAULO_BROGLIO,
    CPF_PEDRO_HENRIQUE,
    CPF_PEDRO_OCTAVIO,
    PADROES_JUROS,
    PADROES_PAG_JUROS,
    PADROES_TAXAS,
    MAPA_CNPJ_EMPRESA,
)


# CNPJs B2B catalogados (Tabela Mestra v2.0)
B2B_CNPJS = {
    "37.815.323/0001-43", "60.618.499/0001-27", "41.698.163/0001-77",
    "53.033.018/0001-56", "55.773.184/0001-14", "48.690.876/0001-33",
    "58.020.950/0001-68", "58.153.884/0001-02", "60.830.003/0001-84",
    "07.104.810/0001-37", "26.186.284/0001-46", "04.968.578/0001-97",
    "37.604.776/0001-20", "42.688.296/0001-25", "37.439.225/0001-59",
}

# CPFs B2C catalogados
B2C_CPFS = {
    "496.013.968-45", "474.300.308-31", "290.470.548-14",
    "366.081.508-06",  # Yasmin (quando RECEBIDO)
    "457.047.138-23",  # Leonardo (quando RECEBIDO)
    "077.823.918-73",  # Sandra (quando RECEBIDO)
}

# Fornecedores nacionais
FORNEC_CNPJS = {
    "15.042.595/0001-15", "30.999.703/0001-36", "26.896.887/0001-31",
    "22.212.404/0001-81", "66.138.694/0001-36", "11.129.630/0001-87",
    "33.094.239/0001-27", "74.484.403/0001-90", "19.822.149/0001-84",
    "04.328.938/0001-96", "05.220.481/0001-64", "61.780.392/0001-43",
}
FORNEC_CPFS = {"155.878.758-57", "155.928.948-13"}

# Salários (CPFs de funcionários)
SALARIOS_CPFS = {
    CPF_PEDRO_OCTAVIO,
    "562.055.698-09", "077.823.918-73", "450.135.498-41",
    "461.175.998-97", "494.206.548-85", "493.044.648-11",
    "457.047.138-23", "366.081.508-06", "381.177.168-01",
}

# Impostos
IMPOSTOS_CNPJS = {
    "46.410.775/0001-36",  # PM PEDREIRA
    "00.394.460/0058-87",  # DARF/SIMPLES
    "46.410.866/0001-71",  # MUNICIPIO JAGUARIUNA
}

# Despesas administrativas
DESP_ADMIN_CNPJS = {
    "65.422.339/0001-21",  # UNIMED
    "49.458.269/0001-05",  # FOUR
    "28.862.503/0001-95",  # C.L. ALARMES
    "26.855.879/0001-47",  # CONCEPT CENTRO
    "10.409.865/0001-60",  # JR PRINT
    "01.663.516/0001-89",  # INTERCARD MEDICOS
    "01.109.184/0001-95",  # UOL
    "46.129.490/0001-21",  # ASS COMERCIAL PEDREIRA
}
DESP_ADMIN_CPFS = {"522.222.668-90"}  # João Pedro Castellani

# Outras saídas
OUTRAS_SAIDAS_CNPJS = {
    "00.000.000/0452-92",  # BB (treinamento G4)
    "90.400.888/0001-42",  # Santander (treinamento G4)
    "51.174.001/0001-93",  # TJ-SP
    "34.028.316/0001-03",  # Correios
    "00.360.305/0001-04",  # CEF Matriz
}


def classify_lancamento(
    cnpj_cpf: str | None,
    descricao: str,
    sinal: str,
    conta_origem_cnpj: str | None = None,
) -> dict:
    """Classifica 1 lançamento.

    Retorna:
        {
            "categoria": str,  # ex: "Marketplaces", "Fornec Nacional", "REQUER_CLASSIFICACAO"
            "linha_cnpj": int | None,  # linha na planilha DFC POR CNPJ
            "confianca": "alta" | "media" | "baixa",
            "nota": str | None,
        }
    """
    desc_upper = descricao.upper() if descricao else ""

    # ====================== Marketplaces ======================
    if cnpj_cpf in CNPJ_MARKETPLACES:
        return {
            "categoria": "Marketplaces",
            "linha_cnpj": 11,
            "confianca": "alta",
            "nota": CNPJ_MARKETPLACES[cnpj_cpf],
        }

    # SISPAG cartões Amazon → Marketplaces
    if any(c in desc_upper for c in ["SISPAG MAST", "SISPAG VISA", "SISPAG ELO", "SISPAG AMEX"]):
        return {
            "categoria": "Marketplaces",
            "linha_cnpj": 11,
            "confianca": "alta",
            "nota": "SISPAG chargeback Amazon",
        }

    # ====================== Juros ======================
    if any(p in desc_upper for p in PADROES_JUROS):
        return {"categoria": "Juros", "linha_cnpj": 12, "confianca": "alta", "nota": None}

    # ====================== Pag Juros (cheque especial + Soemes) ======================
    if any(p in desc_upper for p in PADROES_PAG_JUROS):
        return {"categoria": "Pag Juros", "linha_cnpj": 61, "confianca": "alta", "nota": "cheque especial Itaú"}

    # SAQUE DIN ATM na GB COMERCIO = juros Soemes (qualquer valor)
    if "SAQUE DIN ATM" in desc_upper:
        if conta_origem_cnpj == "07.194.128/0001-82":  # GB COMERCIO
            return {
                "categoria": "Pag Juros",
                "linha_cnpj": 61,
                "confianca": "alta",
                "nota": "SAQUE DIN ATM na GB COMERCIO = juros Soemes",
            }
        else:
            return {
                "categoria": "REQUER_CLASSIFICACAO",
                "linha_cnpj": None,
                "confianca": "baixa",
                "nota": "SAQUE DIN ATM fora da GB COMERCIO — confirmar caso a caso",
            }

    # ====================== Taxas ======================
    if any(p in desc_upper for p in PADROES_TAXAS):
        return {"categoria": "Taxas", "linha_cnpj": 26, "confianca": "alta", "nota": None}

    # ====================== Outras Entradas (PIX mesma empresa) ======================
    if sinal == "+" and cnpj_cpf and conta_origem_cnpj and cnpj_cpf == conta_origem_cnpj:
        return {
            "categoria": "Outras Entradas",
            "linha_cnpj": 13,
            "confianca": "alta",
            "nota": "PIX mesma empresa (mesmo CNPJ exato)",
        }

    # ====================== Transferência entre empresas do grupo ======================
    if cnpj_cpf in MAPA_CNPJ_EMPRESA and conta_origem_cnpj and cnpj_cpf != conta_origem_cnpj:
        return {
            "categoria": "TRANSFERENCIA",
            "linha_cnpj": 69,
            "confianca": "alta",
            "nota": f"Transferência interna entre {MAPA_CNPJ_EMPRESA.get(conta_origem_cnpj, '?')} e {MAPA_CNPJ_EMPRESA[cnpj_cpf]}",
        }

    # ====================== Regras especiais por CPF ======================
    if cnpj_cpf == CPF_PAULO_BROGLIO:
        return {
            "categoria": "Fornec Nacional",
            "linha_cnpj": 23,
            "confianca": "media",
            "nota": "Paulo Broglio (Guinho + Lu Porcelanas) — CONFIRMAR vigência da regra com Simone",
        }
    if cnpj_cpf == CPF_PEDRO_HENRIQUE:
        return {
            "categoria": "Retirada Socios",
            "linha_cnpj": 62,
            "confianca": "alta",
            "nota": "Pedro Henrique pró-labore semanal",
        }
    if cnpj_cpf == CPF_PEDRO_OCTAVIO:
        return {"categoria": "Salarios", "linha_cnpj": 27, "confianca": "alta", "nota": "Pedro Octavio = SEMPRE Salários"}

    # ====================== B2B Atacado ======================
    if cnpj_cpf in B2B_CNPJS and sinal == "+":
        return {"categoria": "B2B Atacado", "linha_cnpj": 9, "confianca": "alta", "nota": None}

    # ====================== B2C Varejo ======================
    if cnpj_cpf in B2C_CPFS and sinal == "+":
        return {"categoria": "B2C Varejo", "linha_cnpj": 10, "confianca": "alta", "nota": None}

    # ====================== Fornecedores Nacionais ======================
    if (cnpj_cpf in FORNEC_CNPJS or cnpj_cpf in FORNEC_CPFS) and sinal == "-":
        return {"categoria": "Fornec Nacional", "linha_cnpj": 23, "confianca": "alta", "nota": None}

    # ====================== Salários (saída) ======================
    if cnpj_cpf in SALARIOS_CPFS and sinal == "-":
        return {"categoria": "Salarios", "linha_cnpj": 27, "confianca": "alta", "nota": None}

    # ====================== Impostos ======================
    if cnpj_cpf in IMPOSTOS_CNPJS and sinal == "-":
        return {"categoria": "Impostos", "linha_cnpj": 25, "confianca": "alta", "nota": None}
    if any(p in desc_upper for p in ["PAGAMENTOS TRIB", "DAS MEI", "INT IPVA"]):
        return {"categoria": "Impostos", "linha_cnpj": 25, "confianca": "media", "nota": "padrão de descrição imposto"}

    # ====================== Despesas Administrativas ======================
    if (cnpj_cpf in DESP_ADMIN_CNPJS or cnpj_cpf in DESP_ADMIN_CPFS) and sinal == "-":
        return {"categoria": "Desp Admin", "linha_cnpj": 28, "confianca": "alta", "nota": None}
    if "DA VIVO-SP" in desc_upper:
        return {"categoria": "Desp Admin", "linha_cnpj": 28, "confianca": "alta", "nota": "VIVO-SP"}

    # ====================== Outras Saídas ======================
    if cnpj_cpf in OUTRAS_SAIDAS_CNPJS and sinal == "-":
        return {"categoria": "Outras Saidas", "linha_cnpj": 29, "confianca": "alta", "nota": None}
    if "CONS PARCELA" in desc_upper:
        return {"categoria": "Outras Saidas", "linha_cnpj": 29, "confianca": "alta", "nota": "consórcio imobiliário"}
    if "PAGAMENTOS PIX QR-CODE SHPP" in desc_upper or "PAGAMENTOS PIX QR-CODE MERC PAGO" in desc_upper:
        return {"categoria": "Outras Saidas", "linha_cnpj": 29, "confianca": "alta", "nota": "estorno marketplace"}

    # ====================== B2B genérico (boleto recebido sem ID) ======================
    if "BOLETOS RECEBIDOS" in desc_upper and sinal == "+":
        return {"categoria": "B2B Atacado", "linha_cnpj": 9, "confianca": "media", "nota": "boleto recebido genérico"}

    # ====================== DEP DIN ATM = B2C ======================
    if "DEP DIN ATM" in desc_upper and sinal == "+":
        return {"categoria": "B2C Varejo", "linha_cnpj": 10, "confianca": "media", "nota": "depósito dinheiro ATM"}

    # ====================== Default: REQUER CLASSIFICAÇÃO ======================
    return {
        "categoria": "REQUER_CLASSIFICACAO",
        "linha_cnpj": None,
        "confianca": "baixa",
        "nota": "Item não catalogado na Tabela Mestra v2.0 — perguntar antes de processar",
    }


def main():
    import json
    if len(sys.argv) != 2:
        print("Uso: python classify.py <extratos_json>")
        sys.exit(1)
    data = json.loads(Path(sys.argv[1]).read_text())
    naoCatalogados = []
    for extrato in data:
        if "erro" in extrato:
            continue
        conta_cnpj = extrato.get("cnpj")
        for lanc in extrato.get("lancamentos", []):
            result = classify_lancamento(
                cnpj_cpf=lanc.get("cnpj_cpf"),
                descricao=lanc.get("descricao", ""),
                sinal=lanc.get("sinal", "+"),
                conta_origem_cnpj=conta_cnpj,
            )
            lanc["classificacao"] = result
            if result["categoria"] == "REQUER_CLASSIFICACAO":
                naoCatalogados.append({
                    "data": lanc.get("data"),
                    "empresa": extrato.get("empresa"),
                    "valor": lanc.get("valor"),
                    "sinal": lanc.get("sinal"),
                    "descricao": lanc.get("descricao"),
                    "cnpj_cpf": lanc.get("cnpj_cpf"),
                })
    print(json.dumps(data, indent=2, ensure_ascii=False))
    if naoCatalogados:
        print(f"\n⚠️ {len(naoCatalogados)} lançamentos REQUEREM classificação — pergunte ao Pedro antes de continuar.", file=sys.stderr)


if __name__ == "__main__":
    main()

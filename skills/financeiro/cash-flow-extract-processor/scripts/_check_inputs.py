"""Verifica se chegaram os 7 extratos PDF + 2 planilhas antes de iniciar processamento.

Bloqueia processamento parcial. Se faltar algo, devolve lista do que falta.
"""

import sys
from pathlib import Path

# Empresas esperadas (7 extratos PDF — uma por conta operacional)
EMPRESAS_EXTRATO = [
    "GB MATRIZ",
    "GB FILIAL",
    "CONCEPT",
    "GB COMERCIO",
    "BROGLIO IMP",
    "TRADES UP",
    "S.P BROGLIO",
]


def check_inputs(input_dir: Path, mes_referencia: str):
    """Confere se chegaram todos os anexos esperados.

    Parâmetros:
        input_dir: pasta onde Pedro colocou extratos + planilhas
        mes_referencia: nome do mês em maiúsculas (ex: "MAIO")

    Retorna:
        dict {"ok": bool, "faltando": [str], "presentes": [str]}
    """
    faltando = []
    presentes = []

    # 7 extratos PDF — espera nomes contendo conta ou empresa
    pdfs = list(input_dir.glob("*.pdf"))
    if len(pdfs) < 7:
        faltando.append(f"PDFs: encontrados {len(pdfs)}/7 extratos Itaú")
    else:
        presentes.append(f"7 extratos PDF Itaú")

    # 2 planilhas
    dfc_cnpj = list(input_dir.glob(f"DFC POR CNPJ*{mes_referencia}*.xlsx"))
    dfc_diario = list(input_dir.glob("DFC DIARIO REALIZADO*.xlsx"))

    if not dfc_cnpj:
        faltando.append(f"Planilha DFC POR CNPJ - {mes_referencia} 2026.xlsx")
    else:
        presentes.append(f"DFC POR CNPJ - {mes_referencia} 2026.xlsx")

    if not dfc_diario:
        faltando.append("Planilha DFC DIARIO REALIZADO - 2026.xlsx")
    else:
        presentes.append("DFC DIARIO REALIZADO - 2026.xlsx")

    return {
        "ok": len(faltando) == 0,
        "faltando": faltando,
        "presentes": presentes,
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python _check_inputs.py <pasta_input> <MES>")
        print("Ex:  python _check_inputs.py /tmp/extratos-maio MAIO")
        sys.exit(1)

    result = check_inputs(Path(sys.argv[1]), sys.argv[2].upper())

    if result["ok"]:
        print("✅ Todos os inputs presentes:")
        for p in result["presentes"]:
            print(f"  • {p}")
        sys.exit(0)
    else:
        print("🟡 PROCESSAMENTO BLOQUEADO — faltam:")
        for f in result["faltando"]:
            print(f"  ❌ {f}")
        print("\nPresentes:")
        for p in result["presentes"]:
            print(f"  ✅ {p}")
        sys.exit(2)

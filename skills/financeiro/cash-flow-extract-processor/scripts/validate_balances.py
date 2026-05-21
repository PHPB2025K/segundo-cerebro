"""Valida saldos e transferências internas antes de tocar nas planilhas.

3 validações:
1. Por conta: saldo_inicial + variação_calculada == saldo_final (±R$ 0,01)
2. Soma de transferências internas por dia = R$ 0,00 (±R$ 0,01)
3. Centavos do Maxi (diferença sobrante após validação 1) → lançar como Juros no último dia

Falhar em qualquer validação BLOQUEIA preenchimento da planilha.
"""

import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _constants import (
    D,
    TOLERANCIA_SALDO,
    TOLERANCIA_TRANSFERENCIA,
    LINHAS_ENT_OP, LINHAS_ENT_INV, LINHAS_ENT_FIN,
    LINHAS_SAI_OP, LINHAS_SAI_INV, LINHAS_SAI_FIN,
)


def variacao_lancamento(linha: int, valor: Decimal, sinal_lanc: str) -> Decimal:
    """Aplica a regra do Knowledge File §"Função de Variação Diária".

    - Transferências (linha 69) mantém sinal direto
    - Demais entradas: soma positiva
    - Demais saídas: subtração
    """
    if linha == 69:
        return valor if sinal_lanc == "+" else -valor
    if linha in (LINHAS_ENT_OP | LINHAS_ENT_INV | LINHAS_ENT_FIN):
        return valor
    if linha in (LINHAS_SAI_OP | LINHAS_SAI_INV | LINHAS_SAI_FIN):
        return -valor
    return D("0")


def validar_saldo_por_conta(extratos_processados: list) -> dict:
    """Valida saldo_inicial + variação == saldo_final por extrato.

    Retorna dict { empresa: {"ok": bool, "diff": Decimal, "centavos_maxi": Decimal} }
    A diferença residual (centavos do Maxi) deve ser lançada como Juros no último dia.
    """
    resultado = {}
    for extrato in extratos_processados:
        if "erro" in extrato:
            continue
        empresa = extrato["empresa"]
        sa = D(extrato["saldo_anterior"])
        sf = D(extrato["saldo_final"])

        variacao_total = D("0")
        for lanc in extrato.get("lancamentos", []):
            cl = lanc.get("classificacao") or {}
            linha = cl.get("linha_cnpj")
            if linha is None:
                continue  # itens não catalogados não entram (ainda)
            valor = D(lanc["valor"])
            variacao_total += variacao_lancamento(linha, valor, lanc["sinal"])

        saldo_calculado = sa + variacao_total
        diff = sf - saldo_calculado
        ok = abs(diff) <= TOLERANCIA_SALDO
        # Se diff > 0 e pequeno → centavos do Maxi
        centavos_maxi = diff if 0 < diff <= D("10.00") else D("0")

        resultado[empresa] = {
            "ok": ok,
            "saldo_inicial": str(sa),
            "saldo_final_extrato": str(sf),
            "saldo_calculado": str(saldo_calculado),
            "diff": str(diff),
            "centavos_maxi": str(centavos_maxi),
        }
    return resultado


def validar_transferencias_por_dia(extratos_processados: list) -> dict:
    """Soma transferências (linha 69) por dia em todas as empresas.

    DEVE ser zero por dia (±R$ 0,01). Quando não zera → uma das pontas faltou
    ou foi contada duas vezes.
    """
    por_dia: dict[str, Decimal] = defaultdict(lambda: D("0"))
    for extrato in extratos_processados:
        if "erro" in extrato:
            continue
        for lanc in extrato.get("lancamentos", []):
            cl = lanc.get("classificacao") or {}
            if cl.get("linha_cnpj") != 69:
                continue
            valor = D(lanc["valor"])
            sinal = +1 if lanc["sinal"] == "+" else -1
            por_dia[lanc["data"]] += valor * sinal

    resultado = {}
    for dia, soma in sorted(por_dia.items()):
        resultado[dia] = {
            "soma": str(soma),
            "ok": abs(soma) <= TOLERANCIA_TRANSFERENCIA,
        }
    return resultado


def main():
    import json
    if len(sys.argv) != 2:
        print("Uso: python validate_balances.py <extratos_classificados_json>")
        sys.exit(1)
    data = json.loads(Path(sys.argv[1]).read_text())

    print("=" * 60)
    print("VALIDAÇÃO 1 — Saldos por conta")
    print("=" * 60)
    val_saldos = validar_saldo_por_conta(data)
    for empresa, r in val_saldos.items():
        icon = "✅" if r["ok"] else "❌"
        print(f"{icon} {empresa}: SI={r['saldo_inicial']} + var → calc={r['saldo_calculado']} | extrato={r['saldo_final_extrato']} | diff={r['diff']}")
        if D(r["centavos_maxi"]) > 0:
            print(f"   💡 Centavos do Maxi a lançar como Juros: R$ {r['centavos_maxi']}")

    print("\n" + "=" * 60)
    print("VALIDAÇÃO 2 — Transferências internas (soma = 0 por dia)")
    print("=" * 60)
    val_trans = validar_transferencias_por_dia(data)
    for dia, r in val_trans.items():
        icon = "✅" if r["ok"] else "❌"
        print(f"{icon} {dia}: soma transferências = R$ {r['soma']}")

    # Exit code
    todos_ok = all(r["ok"] for r in val_saldos.values()) and all(r["ok"] for r in val_trans.values())
    sys.exit(0 if todos_ok else 2)


if __name__ == "__main__":
    main()

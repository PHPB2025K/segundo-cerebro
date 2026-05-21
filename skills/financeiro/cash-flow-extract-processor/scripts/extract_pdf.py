"""Extrai lançamentos estruturados dos extratos PDF do Itaú.

Para cada PDF:
- Identifica a conta (conta Itaú → empresa via MAPA_CONTA_ITAU_EMPRESA)
- Captura saldo inicial (linha SALDO ANTERIOR)
- Captura saldo final (linha SALDO EM CONTA CORRENTE)
- Para cada lançamento: data, valor, descrição, CNPJ/CPF da contraparte

⚠️ A extração depende do layout exato do extrato Itaú. Refinar regex/parsing
no primeiro ciclo real com PDFs reais nas mãos.

Dependências: pdfplumber (preferido) ou PyPDF2 como fallback.
Instalar: pip install pdfplumber
"""

import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Optional

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

sys.path.insert(0, str(Path(__file__).parent))
from _constants import MAPA_CONTA_ITAU_EMPRESA, D


@dataclass
class Lancamento:
    data: str  # YYYY-MM-DD
    descricao: str
    valor: str  # string com Decimal (preserva precisão)
    sinal: str  # "+" ou "-"
    cnpj_cpf: Optional[str]
    contraparte: Optional[str]
    extrato_origem: str  # ex: "GB MATRIZ"
    pagina: int


@dataclass
class ExtratoResumo:
    empresa: str
    conta_itau: str
    cnpj: Optional[str]
    saldo_anterior: str  # decimal como string
    saldo_final: str
    periodo_inicio: str
    periodo_fim: str
    lancamentos: list  # list[Lancamento]


# Regex auxiliares
RE_CONTA_ITAU = re.compile(r"\b(\d{7}-\d)\b")
RE_CNPJ = re.compile(r"\b(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\b")
RE_CPF = re.compile(r"\b(\d{3}\.\d{3}\.\d{3}-\d{2})\b")
RE_VALOR = re.compile(r"-?\s*[\d.]+,\d{2}")
RE_DATA = re.compile(r"\b(\d{2})/(\d{2})/(\d{4})?\b")


def parse_valor_br(s: str) -> Decimal:
    """Converte '1.234,56' ou '-1.234,56' em Decimal."""
    s = s.replace(" ", "").replace(".", "").replace(",", ".")
    try:
        return Decimal(s)
    except InvalidOperation:
        return D("0")


def identifica_empresa_no_pdf(text: str) -> tuple[Optional[str], Optional[str]]:
    """Identifica empresa e conta Itaú varrendo o texto do PDF.

    Retorna: (empresa, conta_itau) ou (None, None)
    """
    for conta in RE_CONTA_ITAU.findall(text):
        if conta in MAPA_CONTA_ITAU_EMPRESA:
            return MAPA_CONTA_ITAU_EMPRESA[conta], conta
    return None, None


def parse_extrato_pdf(pdf_path: Path) -> ExtratoResumo:
    """Lê um PDF de extrato Itaú e retorna ExtratoResumo estruturado.

    Pipeline:
    1. Abrir PDF e juntar todo o texto
    2. Identificar empresa pela conta Itaú
    3. Localizar SALDO ANTERIOR (saldo inicial)
    4. Localizar SALDO EM CONTA CORRENTE (saldo final)
    5. Extrair cada linha de lançamento (data + descrição + valor)
    """
    if not HAS_PDFPLUMBER:
        raise ImportError(
            "pdfplumber não está instalado. Rode: pip install pdfplumber"
        )

    lancamentos: list[Lancamento] = []
    saldo_anterior = D("0")
    saldo_final = D("0")
    periodo_inicio = ""
    periodo_fim = ""
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            full_text += "\n" + text

            for raw_line in text.split("\n"):
                line = raw_line.strip()
                if not line:
                    continue

                # SALDO ANTERIOR (saldo inicial)
                if "SALDO ANTERIOR" in line.upper():
                    valores = RE_VALOR.findall(line)
                    if valores:
                        saldo_anterior = parse_valor_br(valores[-1])
                    continue

                # SALDO EM CONTA CORRENTE (saldo final)
                if "SALDO EM CONTA CORRENTE" in line.upper():
                    valores = RE_VALOR.findall(line)
                    if valores:
                        saldo_final = parse_valor_br(valores[-1])
                    continue

                # Linhas informativas a ignorar
                if any(p in line.upper() for p in [
                    "SALDO TOTAL DISPONIVEL DIA",
                    "RESUMO MENSAL",
                    "CONTA CORRENTE",
                ]):
                    continue

                # Tenta extrair lançamento: data + descrição + valor
                m_data = RE_DATA.search(line)
                valores = RE_VALOR.findall(line)
                if not m_data or not valores:
                    continue

                dia, mes, ano = m_data.groups()
                if not ano:
                    # Inferir ano via período do extrato
                    ano = periodo_inicio.split("-")[0] if periodo_inicio else "2026"
                data_iso = f"{ano}-{mes}-{dia}"

                valor_str = valores[-1]
                valor = parse_valor_br(valor_str)
                sinal = "-" if valor < 0 else "+"

                # Descrição = linha minus data e valor
                desc = line
                desc = RE_DATA.sub("", desc)
                desc = RE_VALOR.sub("", desc).strip()

                m_cnpj = RE_CNPJ.search(desc)
                m_cpf = RE_CPF.search(desc)
                cnpj_cpf = m_cnpj.group(1) if m_cnpj else (m_cpf.group(1) if m_cpf else None)

                # Contraparte: heurística — texto após "PIX RECEBIDO/ENVIADO" etc
                contraparte = None
                for marcador in ["PIX RECEBIDO", "PIX ENVIADO", "TED", "SISPAG"]:
                    if marcador in desc.upper():
                        idx = desc.upper().find(marcador) + len(marcador)
                        contraparte = desc[idx:].strip()[:80]
                        break

                lancamentos.append(Lancamento(
                    data=data_iso,
                    descricao=desc[:200],
                    valor=str(abs(valor)),
                    sinal=sinal,
                    cnpj_cpf=cnpj_cpf,
                    contraparte=contraparte,
                    extrato_origem="",  # preenchido abaixo
                    pagina=page_num,
                ))

    empresa, conta = identifica_empresa_no_pdf(full_text)
    if not empresa:
        raise ValueError(f"Não consegui identificar a empresa do extrato {pdf_path.name}")

    # Identifica CNPJ via texto
    cnpj_match = None
    for cnpj in RE_CNPJ.findall(full_text):
        if cnpj in {
            "58.151.616/0001-43", "58.151.616/0002-24", "58.818.245/0001-00",
            "07.194.128/0001-82", "63.922.116/0001-06", "45.200.547/0001-79",
            "97.546.173/0001-41",
        }:
            cnpj_match = cnpj
            break

    for l in lancamentos:
        l.extrato_origem = empresa

    return ExtratoResumo(
        empresa=empresa,
        conta_itau=conta,
        cnpj=cnpj_match,
        saldo_anterior=str(saldo_anterior),
        saldo_final=str(saldo_final),
        periodo_inicio=periodo_inicio or "",
        periodo_fim=periodo_fim or "",
        lancamentos=[asdict(l) for l in lancamentos],
    )


def main():
    if len(sys.argv) < 2:
        print("Uso: python extract_pdf.py <pdf_path|pasta_com_pdfs> [output_json]")
        sys.exit(1)

    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    pdfs = [src] if src.is_file() else sorted(src.glob("*.pdf"))
    resultados = []
    for pdf in pdfs:
        try:
            resumo = parse_extrato_pdf(pdf)
            resultados.append(asdict(resumo))
            print(f"✅ {pdf.name}: {resumo.empresa} — {len(resumo.lancamentos)} lançamentos | saldo inicial R$ {resumo.saldo_anterior} → final R$ {resumo.saldo_final}")
        except Exception as e:
            print(f"❌ {pdf.name}: {e}")
            resultados.append({"erro": str(e), "arquivo": str(pdf)})

    if out:
        out.write_text(json.dumps(resultados, indent=2, ensure_ascii=False))
        print(f"\nResultado salvo em {out}")


if __name__ == "__main__":
    main()

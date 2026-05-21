#!/bin/bash
# Converte XLSX → ODS → XLSX para compatibilidade macOS.
#
# Knowledge File v10.1 §"Conversão LibreOffice":
# A conversão via LibreOffice recalcula todas as fórmulas e garante que o
# arquivo abre certo no Excel/Numbers do Mac do Pedro sem erros visuais.
#
# Uso: ./convert_libreoffice.sh <arquivo.xlsx>
#
# Requer: libreoffice instalado (no VPS: apt install libreoffice --no-install-recommends)

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Uso: $0 <arquivo.xlsx>"
  exit 1
fi

ARQUIVO="$1"
DIR=$(dirname "$ARQUIVO")
BASE=$(basename "$ARQUIVO" .xlsx)

if [ ! -f "$ARQUIVO" ]; then
  echo "❌ Arquivo não encontrado: $ARQUIVO"
  exit 1
fi

echo "🔄 Convertendo $ARQUIVO via LibreOffice..."

# XLSX → ODS
libreoffice --headless --convert-to ods --outdir "$DIR" "$ARQUIVO" >/dev/null
ODS="$DIR/$BASE.ods"

if [ ! -f "$ODS" ]; then
  echo "❌ Conversão XLSX → ODS falhou"
  exit 2
fi

# ODS → XLSX (sobrescreve o original)
libreoffice --headless --convert-to xlsx --outdir "$DIR" "$ODS" >/dev/null

# Limpa intermediário
rm -f "$ODS"

echo "✅ $ARQUIVO convertido (recalculado + compatível macOS)"

#!/bin/bash
# Refresh Mercado Livre/Mercado Pago OAuth tokens
# Usage: ml-refresh-token.sh <app_type>
# app_type: vendas | finance | metrics

set -euo pipefail

APP_TYPE="${1:?Uso: ml-refresh-token.sh <vendas|finance|metrics>}"
BASE_DIR="/root/.openclaw"

case "$APP_TYPE" in
  vendas)
    TOKEN_FILE="$BASE_DIR/.ml-tokens.json"
    CLIENT_ID="8869805792970343"
    CLIENT_SECRET="HfzgmmUH7ZMC60299AnFYXetdHjTpfpY"
    ;;
  finance)
    TOKEN_FILE="$BASE_DIR/.ml-tokens-finance.json"
    CLIENT_ID="8100349388872095"
    CLIENT_SECRET="pPwg70OV1r2advkxoWkafNW0RLg0IeAG"
    ;;
  metrics)
    TOKEN_FILE="$BASE_DIR/.ml-tokens-metrics.json"
    CLIENT_ID="7970005349031308"
    CLIENT_SECRET="SwRgOpZtjgzsPg3EToKXG8Oe0iymugzx"
    ;;
  *)
    echo "Tipo inválido: $APP_TYPE (use vendas, finance ou metrics)"
    exit 1
    ;;
esac

if [ ! -f "$TOKEN_FILE" ]; then
  echo "ERRO: Token file não encontrado: $TOKEN_FILE"
  exit 1
fi

REFRESH_TOKEN=$(python3 -c "import json; print(json.load(open('$TOKEN_FILE'))['refresh_token'])")

RESPONSE=$(curl -s -X POST "https://api.mercadolibre.com/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET" \
  -d "refresh_token=$REFRESH_TOKEN")

# Verify response has access_token
if echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'access_token' in d" 2>/dev/null; then
  echo "$RESPONSE" | python3 -c "import json,sys; json.dump(json.load(sys.stdin), open('$TOKEN_FILE','w'), indent=2)"
  chmod 600 "$TOKEN_FILE"
  echo "✅ Token $APP_TYPE renovado com sucesso"
else
  echo "❌ Erro ao renovar token $APP_TYPE:"
  echo "$RESPONSE" | python3 -c "import json,sys; print(json.dumps(json.load(sys.stdin), indent=2))" 2>/dev/null || echo "$RESPONSE"
  exit 1
fi

#!/bin/bash
# Instagram API helper via RapidAPI (instagram120)
# Usage:
#   instagram.sh profile <username>
#   instagram.sh posts <username> [maxId]

API_KEY="d1337539c6msh0b8beac722fa368p1cfdb3jsn9e5bbb9e1ee9"
API_HOST="instagram120.p.rapidapi.com"
BASE_URL="https://${API_HOST}/api/instagram"

ACTION="${1:?Usage: instagram.sh <profile|posts> <username> [maxId]}"
USERNAME="${2:?Username required}"
MAX_ID="${3:-}"

case "$ACTION" in
  profile)
    curl -s -X POST "${BASE_URL}/profile" \
      -H "x-rapidapi-key: ${API_KEY}" \
      -H "x-rapidapi-host: ${API_HOST}" \
      -H "Content-Type: application/json" \
      -d "{\"username\":\"${USERNAME}\"}"
    ;;
  posts)
    curl -s -X POST "${BASE_URL}/posts" \
      -H "x-rapidapi-key: ${API_KEY}" \
      -H "x-rapidapi-host: ${API_HOST}" \
      -H "Content-Type: application/json" \
      -d "{\"username\":\"${USERNAME}\",\"maxId\":\"${MAX_ID}\"}"
    ;;
  *)
    echo "Unknown action: $ACTION"
    echo "Usage: instagram.sh <profile|posts> <username> [maxId]"
    exit 1
    ;;
esac

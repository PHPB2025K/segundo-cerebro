#!/usr/bin/env bash
# deploy-vps.sh — Deploy automatizado para VPS do Pedro (187.77.237.231)
# Suporta PM2 e Docker Compose
# Uso: ./deploy-vps.sh --app meu-app --host 187.77.237.231 [opções]
set -euo pipefail

# ============================================================
# Defaults
# ============================================================
APP_NAME=""
VPS_HOST="187.77.237.231"
VPS_USER="ubuntu"
VPS_DIR=""          # default: /apps/<APP_NAME>
DEPLOY_MODE="pm2"   # pm2 | docker
BUILD_BEFORE=true
BRANCH="main"
SSH_KEY=""
REGISTRY="ghcr.io"
GITHUB_USER="PHPB2025K"

# ============================================================
# Help
# ============================================================
usage() {
  cat <<EOF
deploy-vps.sh — Deploy automatizado para VPS

Uso:
  $0 --app <nome> [opções]

Opções:
  --app <nome>        Nome do app (obrigatório)
  --host <ip>         Host do VPS (default: 187.77.237.231)
  --user <user>       Usuário SSH (default: ubuntu)
  --dir <path>        Diretório no VPS (default: /apps/<app>)
  --mode <pm2|docker> Modo de deploy (default: pm2)
  --no-build          Pular build local
  --branch <branch>   Branch para deploy (default: main)
  --key <path>        Caminho da chave SSH
  --github-user <u>   GitHub user para registry (default: PHPB2025K)
  -h, --help          Mostrar esta ajuda

Exemplos:
  $0 --app bidspark --mode pm2
  $0 --app canguu --host 187.77.237.231 --mode docker
  $0 --app simulimport --no-build --mode docker
EOF
  exit 0
}

# ============================================================
# Parse args
# ============================================================
while [[ $# -gt 0 ]]; do
  case "$1" in
    --app)          APP_NAME="$2";      shift 2 ;;
    --host)         VPS_HOST="$2";      shift 2 ;;
    --user)         VPS_USER="$2";      shift 2 ;;
    --dir)          VPS_DIR="$2";       shift 2 ;;
    --mode)         DEPLOY_MODE="$2";   shift 2 ;;
    --no-build)     BUILD_BEFORE=false; shift ;;
    --branch)       BRANCH="$2";        shift 2 ;;
    --key)          SSH_KEY="$2";       shift 2 ;;
    --github-user)  GITHUB_USER="$2";   shift 2 ;;
    -h|--help) usage ;;
    *) echo "Opção desconhecida: $1"; usage ;;
  esac
done

if [[ -z "$APP_NAME" ]]; then
  echo "❌ --app é obrigatório."
  exit 1
fi

if [[ "$DEPLOY_MODE" != "pm2" && "$DEPLOY_MODE" != "docker" ]]; then
  echo "❌ --mode deve ser 'pm2' ou 'docker'."
  exit 1
fi

VPS_DIR="${VPS_DIR:-/apps/$APP_NAME}"

# SSH flags
SSH_FLAGS="-o StrictHostKeyChecking=no -o ConnectTimeout=15"
if [[ -n "$SSH_KEY" ]]; then
  SSH_FLAGS="$SSH_FLAGS -i $SSH_KEY"
fi
SSH_CMD="ssh $SSH_FLAGS $VPS_USER@$VPS_HOST"

echo ""
echo "🚀 Deploying $APP_NAME → $VPS_HOST ($DEPLOY_MODE)"
echo "   Dir: $VPS_DIR | Branch: $BRANCH"
echo ""

# ============================================================
# 1. Verificar git status
# ============================================================
if [[ -d ".git" ]]; then
  CURRENT_BRANCH=$(git branch --show-current)
  if [[ "$CURRENT_BRANCH" != "$BRANCH" ]]; then
    echo "⚠️  Branch atual: $CURRENT_BRANCH (esperado: $BRANCH)"
    read -r -p "   Continuar mesmo assim? [y/N] " confirm
    [[ "$confirm" != "y" && "$confirm" != "Y" ]] && exit 1
  fi

  # Verificar uncommitted changes
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "⚠️  Existem mudanças não commitadas. Recomenda-se commitar antes do deploy."
    read -r -p "   Continuar mesmo assim? [y/N] " confirm
    [[ "$confirm" != "y" && "$confirm" != "Y" ]] && exit 1
  fi

  GIT_SHA=$(git rev-parse --short HEAD)
  echo "📌 Commit: $GIT_SHA"
else
  GIT_SHA="no-git"
fi

# ============================================================
# 2. Build (PM2 mode)
# ============================================================
if [[ "$DEPLOY_MODE" == "pm2" && "$BUILD_BEFORE" == "true" ]]; then
  echo "🏗️  Buildando Next.js..."
  
  if command -v pnpm &> /dev/null; then
    pnpm build
  elif command -v npm &> /dev/null; then
    npm run build
  else
    echo "❌ pnpm ou npm não encontrados."
    exit 1
  fi
  
  echo "✅ Build concluído."
fi

# ============================================================
# 3. Build Docker (Docker mode)
# ============================================================
if [[ "$DEPLOY_MODE" == "docker" && "$BUILD_BEFORE" == "true" ]]; then
  echo "🐳 Buildando imagem Docker..."
  
  IMAGE_NAME="$REGISTRY/$GITHUB_USER/$APP_NAME"
  
  docker build -t "$IMAGE_NAME:$GIT_SHA" -t "$IMAGE_NAME:latest" .
  
  echo "📤 Fazendo push da imagem..."
  docker push "$IMAGE_NAME:$GIT_SHA"
  docker push "$IMAGE_NAME:latest"
  
  echo "✅ Imagem publicada: $IMAGE_NAME:$GIT_SHA"
fi

# ============================================================
# 4. Verificar conexão SSH
# ============================================================
echo "🔗 Verificando conexão com o VPS..."
if ! $SSH_CMD "echo '✅ SSH OK'" 2>/dev/null; then
  echo "❌ Falha ao conectar no VPS. Verifique:"
  echo "   - Host: $VPS_HOST"
  echo "   - User: $VPS_USER"
  echo "   - SSH key configurada"
  exit 1
fi

# ============================================================
# 5. Deploy PM2
# ============================================================
if [[ "$DEPLOY_MODE" == "pm2" ]]; then
  echo "📦 Sincronizando arquivos via rsync..."
  
  # Arquivos a sincronizar (excluir node_modules, .git, etc)
  rsync -avz \
    $([[ -n "$SSH_KEY" ]] && echo "-e 'ssh -i $SSH_KEY'" || echo "") \
    --exclude node_modules \
    --exclude .git \
    --exclude .next/cache \
    --exclude .env.local \
    --exclude .env.development \
    --exclude "*.test.*" \
    --exclude e2e/ \
    --exclude coverage/ \
    --delete \
    . "$VPS_USER@$VPS_HOST:$VPS_DIR/"

  echo "🔄 Reiniciando app com PM2..."
  $SSH_CMD << REMOTE
set -e
cd "$VPS_DIR"

# Instalar dependências de produção
if command -v pnpm &> /dev/null; then
  pnpm install --prod --frozen-lockfile
elif command -v npm &> /dev/null; then
  npm ci --omit=dev
fi

# PM2: restart ou start
if pm2 list | grep -q "$APP_NAME"; then
  pm2 restart "$APP_NAME" --update-env
  echo "✅ App '$APP_NAME' reiniciado."
else
  # Primeiro deploy: iniciar com ecosystem.config.js se existir
  if [[ -f "ecosystem.config.js" ]]; then
    pm2 start ecosystem.config.js --only "$APP_NAME"
  else
    pm2 start npm --name "$APP_NAME" -- start
  fi
  pm2 save
  echo "✅ App '$APP_NAME' iniciado."
fi

# Status
pm2 list | grep "$APP_NAME" || true
REMOTE
fi

# ============================================================
# 6. Deploy Docker
# ============================================================
if [[ "$DEPLOY_MODE" == "docker" ]]; then
  IMAGE_NAME="$REGISTRY/$GITHUB_USER/$APP_NAME"
  
  echo "🐳 Atualizando container Docker no VPS..."
  $SSH_CMD << REMOTE
set -e
cd "$VPS_DIR"

# Pull nova imagem
docker pull "$IMAGE_NAME:latest"

# Subir serviço sem downtime
docker compose up -d --no-deps --force-recreate app

# Limpar imagens antigas
docker image prune -f

echo "✅ Container '$APP_NAME' atualizado."
docker ps | grep "$APP_NAME" || true
REMOTE
fi

# ============================================================
# 7. Health check
# ============================================================
echo "🏥 Verificando health do app..."
sleep 3

# Tentar descobrir porta do app
APP_PORT="3000"

for i in 1 2 3 4 5; do
  if $SSH_CMD "curl -sf http://localhost:$APP_PORT/api/health > /dev/null 2>&1"; then
    echo "✅ Health check passou!"
    break
  fi
  if [[ $i -eq 5 ]]; then
    echo "⚠️  Health check falhou após 5 tentativas. Verifique os logs:"
    if [[ "$DEPLOY_MODE" == "pm2" ]]; then
      $SSH_CMD "pm2 logs $APP_NAME --lines 20 --nostream" || true
    else
      $SSH_CMD "cd $VPS_DIR && docker compose logs --tail=20 app" || true
    fi
  else
    echo "   Tentativa $i/5... aguardando 3s"
    sleep 3
  fi
done

# ============================================================
# Done!
# ============================================================
echo ""
echo "✅ Deploy concluído!"
echo "   App: $APP_NAME"
echo "   Host: $VPS_HOST"
echo "   Mode: $DEPLOY_MODE"
echo "   SHA: $GIT_SHA"
echo ""
echo "Logs:"
if [[ "$DEPLOY_MODE" == "pm2" ]]; then
  echo "  ssh $VPS_USER@$VPS_HOST 'pm2 logs $APP_NAME'"
else
  echo "  ssh $VPS_USER@$VPS_HOST 'cd $VPS_DIR && docker compose logs -f app'"
fi
echo ""

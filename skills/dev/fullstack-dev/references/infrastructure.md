# Infrastructure Reference — Docker, Nginx, PM2, Vercel, CI/CD

## Índice
1. [Docker + Docker Compose](#1-docker--docker-compose)
2. [Nginx (VPS 187.77.237.231)](#2-nginx)
3. [PM2](#3-pm2)
4. [Vercel](#4-vercel)
5. [GitHub Actions CI/CD](#5-github-actions)
6. [Monitoramento](#6-monitoramento)

---

## 1. Docker + Docker Compose

### Dockerfile Next.js Otimizado

```dockerfile
FROM node:22-alpine AS base
WORKDIR /app

# Dependências
FROM base AS deps
RUN corepack enable pnpm
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# Build
FROM base AS builder
RUN corepack enable pnpm
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED=1
RUN pnpm build

# Runner (imagem mínima de produção)
FROM base AS runner
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT=3000 HOSTNAME="0.0.0.0"
CMD ["node", "server.js"]
```

### Docker Compose (VPS)

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    image: ghcr.io/phpb2025k/bidspark:latest
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    env_file:
      - .env.production
    depends_on:
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  worker:
    image: ghcr.io/phpb2025k/bidspark:latest
    restart: unless-stopped
    command: node worker.js
    env_file:
      - .env.production
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s

volumes:
  redis_data:
```

```bash
# Comandos essenciais
docker compose up -d                    # subir em background
docker compose logs -f app              # ver logs
docker compose exec app sh              # shell no container
docker compose pull && docker compose up -d --no-deps app  # deploy
docker image prune -f                   # limpar imagens antigas
```

---

## 2. Nginx

### Config Padrão (SaaS no VPS)

```nginx
# /etc/nginx/sites-available/bidspark.com
events { worker_connections 1024; }

http {
  upstream app {
    server localhost:3000;
    keepalive 64;
  }

  # Redirect HTTP → HTTPS
  server {
    listen 80;
    server_name bidspark.com www.bidspark.com;
    return 301 https://$host$request_uri;
  }

  server {
    listen 443 ssl http2;
    server_name bidspark.com www.bidspark.com;

    ssl_certificate /etc/letsencrypt/live/bidspark.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/bidspark.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    # Security Headers
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    # Gzip
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css application/json application/javascript text/xml;
    gzip_min_length 1000;

    # Rate limiting (declarar no http block)
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req zone=api burst=20 nodelay;

    # Proxy para Next.js
    location / {
      proxy_pass http://app;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_cache_bypass $http_upgrade;
      proxy_read_timeout 86400;
    }

    # Cache assets estáticos
    location /_next/static/ {
      proxy_pass http://app;
      add_header Cache-Control "public, max-age=31536000, immutable";
    }

    # Health check sem logs
    location /api/health {
      proxy_pass http://app;
      access_log off;
    }
  }
}
```

### Certbot SSL

```bash
# Instalar certbot
apt install certbot python3-certbot-nginx

# Obter certificado
certbot --nginx -d bidspark.com -d www.bidspark.com

# Auto-renovação (já instalado com certbot)
systemctl status certbot.timer

# Renovar manualmente
certbot renew --dry-run
```

---

## 3. PM2

```js
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: 'bidspark',
      script: 'node_modules/.bin/next',
      args: 'start',
      instances: 'max',       // usa todos os CPUs
      exec_mode: 'cluster',   // load balancing
      env: {
        NODE_ENV: 'production',
        PORT: 3000,
      },
      error_file: './logs/err.log',
      out_file: './logs/out.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss',
      merge_logs: true,
      max_memory_restart: '1G',
    },
    {
      name: 'bidspark-worker',
      script: 'dist/worker.js',
      instances: 2,
      env: { NODE_ENV: 'production' },
    }
  ]
}
```

```bash
pm2 start ecosystem.config.js
pm2 logs bidspark
pm2 monit                   # dashboard interativo
pm2 restart bidspark
pm2 reload bidspark         # zero-downtime restart
pm2 stop bidspark
pm2 delete bidspark
pm2 save                    # salva config
pm2 startup                 # auto-start após reboot
pm2 list                    # ver todos os processos
```

---

## 4. Vercel

```bash
# Deploy
vercel --prod                # deploy de produção
vercel                       # preview deploy

# Env vars
vercel env add DATABASE_URL production
vercel env ls
vercel env pull .env.local   # pull vars para dev

# Logs
vercel logs
vercel logs --follow

# Domains
vercel domains add bidspark.com
```

```ts
// vercel.json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" }
      ]
    }
  ],
  "rewrites": [
    { "source": "/api/v1/:path*", "destination": "/api/:path*" }
  ],
  "regions": ["gru1"] // São Paulo
}
```

### next.config.ts para Vercel

```ts
import type { NextConfig } from 'next'

const config: NextConfig = {
  output: 'standalone', // para Docker; remover para Vercel
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: '*.supabase.co' },
      { protocol: 'https', hostname: 'lh3.googleusercontent.com' },
    ],
  },
  experimental: {
    optimizePackageImports: ['lucide-react', '@radix-ui/react-icons'],
  },
}

export default config
```

---

## 5. GitHub Actions

### CI/CD Completo

```yaml
# .github/workflows/deploy.yml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm type-check
      - run: pnpm lint
      - run: pnpm test

  build-push:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-vps:
    needs: build-push
    runs-on: ubuntu-latest
    steps:
      - uses: appleboy/ssh-action@v1
        with:
          host: 187.77.237.231
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /apps/bidspark
            docker pull ghcr.io/${{ github.repository }}:latest
            docker compose up -d --no-deps --force-recreate app worker
            docker image prune -f
            echo "✅ Deployed $(date)"
```

### Secrets necessários

```
Settings → Secrets → Actions:
VPS_USER     = ubuntu
VPS_SSH_KEY  = (chave privada SSH)
```

---

## 6. Monitoramento

### Sentry

```ts
// sentry.client.config.ts
import * as Sentry from '@sentry/nextjs'
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  tracesSampleRate: 0.1,
  environment: process.env.NODE_ENV,
  beforeSend(event) {
    // Filtrar bots
    if (event.request?.headers?.['user-agent']?.includes('bot')) return null
    return event
  },
})

// Capturar erro manual
Sentry.captureException(error, {
  extra: { userId: user.id, context: 'payment' },
  tags: { area: 'billing' },
})
```

### Health Check Endpoint

```ts
// app/api/health/route.ts
export async function GET() {
  const checks = await Promise.allSettled([
    db.execute(sql`SELECT 1`),
    redis.ping(),
  ])

  const status = checks.every(c => c.status === 'fulfilled') ? 200 : 503
  return NextResponse.json({
    status: status === 200 ? 'ok' : 'degraded',
    db: checks[0].status,
    redis: checks[1].status,
    timestamp: new Date().toISOString(),
  }, { status })
}
```

### Uptime Kuma (self-hosted)

```yaml
# docker-compose.yml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    volumes:
      - kuma_data:/app/data
    ports:
      - "3001:3001"
    restart: unless-stopped
volumes:
  kuma_data:
```

Acesso: http://187.77.237.231:3001

### Logging com Pino

```ts
// lib/logger.ts
import pino from 'pino'

export const logger = pino({
  level: process.env.LOG_LEVEL ?? 'info',
  ...(process.env.NODE_ENV === 'development' && {
    transport: { target: 'pino-pretty', options: { colorize: true } }
  }),
})

// Uso estruturado (não console.log em produção)
logger.info({ userId, orderId }, 'Order created')
logger.error({ err: error, userId }, 'Payment failed')
logger.warn({ requestId, attempts }, 'Retry attempt')
```

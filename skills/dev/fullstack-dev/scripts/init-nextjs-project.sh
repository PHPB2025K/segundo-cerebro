#!/usr/bin/env bash
# init-nextjs-project.sh — Bootstrap Next.js 15 + Supabase + Tailwind + shadcn/ui
# Uso: ./init-nextjs-project.sh --name meu-projeto [--dir /path] [--no-shadcn] [--no-supabase]
set -euo pipefail

# ============================================================
# Defaults
# ============================================================
PROJECT_NAME=""
BASE_DIR="$HOME/projects"
INCLUDE_SHADCN=true
INCLUDE_SUPABASE=true
INCLUDE_STRIPE=false
INCLUDE_AI=false

# ============================================================
# Help
# ============================================================
usage() {
  cat <<EOF
init-nextjs-project.sh — Bootstrap Next.js 15 + Supabase + Tailwind + shadcn/ui

Uso:
  $0 --name <nome> [opções]

Opções:
  --name <nome>       Nome do projeto (obrigatório)
  --dir <path>        Diretório base (default: ~/projects)
  --no-shadcn         Pular instalação do shadcn/ui
  --no-supabase       Pular instalação do Supabase
  --stripe            Instalar dependências do Stripe
  --ai                Instalar OpenAI + Anthropic + Vercel AI SDK
  -h, --help          Mostrar esta ajuda

Exemplos:
  $0 --name simulimport
  $0 --name bidspark --dir ~/code --stripe --ai
  $0 --name landing-page --no-supabase
EOF
  exit 0
}

# ============================================================
# Parse args
# ============================================================
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)   PROJECT_NAME="$2"; shift 2 ;;
    --dir)    BASE_DIR="$2";     shift 2 ;;
    --no-shadcn)   INCLUDE_SHADCN=false;  shift ;;
    --no-supabase) INCLUDE_SUPABASE=false; shift ;;
    --stripe) INCLUDE_STRIPE=true; shift ;;
    --ai)     INCLUDE_AI=true;   shift ;;
    -h|--help) usage ;;
    *) echo "Opção desconhecida: $1"; usage ;;
  esac
done

if [[ -z "$PROJECT_NAME" ]]; then
  echo "❌ --name é obrigatório. Use --help para mais detalhes."
  exit 1
fi

PROJECT_DIR="$BASE_DIR/$PROJECT_NAME"

echo ""
echo "🚀 Iniciando projeto: $PROJECT_NAME"
echo "   Destino: $PROJECT_DIR"
echo "   shadcn/ui: $INCLUDE_SHADCN | Supabase: $INCLUDE_SUPABASE | Stripe: $INCLUDE_STRIPE | AI: $INCLUDE_AI"
echo ""

# Verificar se pasta já existe
if [[ -d "$PROJECT_DIR" ]]; then
  echo "❌ Pasta $PROJECT_DIR já existe. Escolha outro nome ou remova a pasta."
  exit 1
fi

# Verificar pnpm
if ! command -v pnpm &> /dev/null; then
  echo "⚠️  pnpm não encontrado. Instalando..."
  npm install -g pnpm
fi

mkdir -p "$BASE_DIR"

# ============================================================
# 1. Criar projeto Next.js
# ============================================================
echo "📦 Criando projeto Next.js 15..."
cd "$BASE_DIR"
# Aceitar todos os prompts interativos com defaults (n para React Compiler, n para AGENTS.md)
printf 'n\nn\n' | pnpm create next-app@latest "$PROJECT_NAME" \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*" \
  --no-turbopack \
  --skip-install 2>/dev/null || true

# Verificar se o diretório foi criado
if [[ ! -d "$BASE_DIR/$PROJECT_NAME" ]]; then
  echo "⚠️  create-next-app falhou, criando estrutura manualmente..."
  mkdir -p "$BASE_DIR/$PROJECT_NAME"
fi

cd "$PROJECT_DIR"

# ============================================================
# 2. Instalar dependências base
# ============================================================
echo "📦 Instalando dependências base..."
pnpm add \
  @tanstack/react-query \
  @tanstack/react-query-devtools \
  react-hook-form \
  @hookform/resolvers \
  zod \
  class-variance-authority \
  clsx \
  tailwind-merge \
  lucide-react \
  next-themes \
  sonner

pnpm add -D \
  @types/node \
  drizzle-kit \
  vitest \
  @vitejs/plugin-react \
  @vitest/coverage-v8 \
  @vitest/ui \
  @testing-library/react \
  @testing-library/jest-dom \
  @testing-library/user-event \
  prettier \
  eslint-config-prettier

# ============================================================
# 3. Supabase
# ============================================================
if [[ "$INCLUDE_SUPABASE" == "true" ]]; then
  echo "📦 Instalando Supabase..."
  pnpm add \
    @supabase/supabase-js \
    @supabase/ssr \
    drizzle-orm \
    postgres
fi

# ============================================================
# 4. Stripe
# ============================================================
if [[ "$INCLUDE_STRIPE" == "true" ]]; then
  echo "📦 Instalando Stripe..."
  pnpm add stripe @stripe/stripe-js resend
fi

# ============================================================
# 5. AI
# ============================================================
if [[ "$INCLUDE_AI" == "true" ]]; then
  echo "📦 Instalando AI SDKs..."
  pnpm add openai @anthropic-ai/sdk ai @ai-sdk/openai
fi

# ============================================================
# 6. Estrutura de pastas
# ============================================================
echo "📁 Criando estrutura de pastas..."

# Components
mkdir -p src/components/ui
mkdir -p src/components/layout
mkdir -p src/components/shared

# Features
mkdir -p src/features/auth/components
mkdir -p src/features/auth/hooks

# Lib
mkdir -p src/lib/db
mkdir -p src/lib/supabase

# Types
mkdir -p src/types

# App route groups
mkdir -p "src/app/(auth)/login"
mkdir -p "src/app/(auth)/signup"
mkdir -p "src/app/(auth)/callback"
mkdir -p "src/app/(app)/dashboard"
mkdir -p "src/app/(app)/settings"
mkdir -p "src/app/api/health"

# Tests
mkdir -p test
mkdir -p e2e

# ============================================================
# 7. Arquivos de configuração
# ============================================================
echo "📝 Criando arquivos de configuração..."

# tsconfig.json (strict + paths)
cat > tsconfig.json << 'TSCONFIG'
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noEmit": true,
    "esModuleInterop": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
TSCONFIG

# tailwind.config.ts
cat > tailwind.config.ts << 'TAILWIND'
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    './src/features/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
TAILWIND

pnpm add -D tailwindcss-animate 2>/dev/null || true

# next.config.ts
cat > next.config.ts << 'NEXTCONFIG'
import type { NextConfig } from 'next'

const config: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: '*.supabase.co' },
      { protocol: 'https', hostname: 'lh3.googleusercontent.com' },
      { protocol: 'https', hostname: 'avatars.githubusercontent.com' },
    ],
  },
  experimental: {
    optimizePackageImports: ['lucide-react'],
  },
}

export default config
NEXTCONFIG

# .env.example
cat > .env.example << 'ENVEXAMPLE'
# ============================================================
# App
# ============================================================
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development

# ============================================================
# Supabase
# ============================================================
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# ============================================================
# Database (Drizzle → Supabase Pooler)
# ============================================================
DATABASE_URL=postgres://postgres:[password]@db.[ref].supabase.co:5432/postgres

# ============================================================
# Stripe (opcional)
# ============================================================
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_PRICE_STARTER=price_...
STRIPE_PRICE_PRO=price_...

# ============================================================
# AI (opcional)
# ============================================================
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# ============================================================
# Email
# ============================================================
RESEND_API_KEY=re_...

# ============================================================
# Monitoring
# ============================================================
NEXT_PUBLIC_SENTRY_DSN=https://...@sentry.io/...
SENTRY_AUTH_TOKEN=...
ENVEXAMPLE

cp .env.example .env.local

# lib/utils.ts
cat > src/lib/utils.ts << 'UTILS'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatCurrency(value: number, currency = 'BRL'): string {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency,
  }).format(value)
}

export function formatDate(date: Date | string, format: 'short' | 'long' = 'short'): string {
  const d = typeof date === 'string' ? new Date(date) : date
  return new Intl.DateTimeFormat('pt-BR', {
    dateStyle: format,
  }).format(d)
}

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}
UTILS

# ============================================================
# 8. Supabase helpers
# ============================================================
if [[ "$INCLUDE_SUPABASE" == "true" ]]; then
  cat > src/lib/supabase/server.ts << 'SUPA_SERVER'
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export function createClient() {
  const cookieStore = cookies()
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => cookieStore.getAll(),
        setAll: (cs) =>
          cs.forEach(({ name, value, options }) =>
            cookieStore.set(name, value, options)
          ),
      },
    }
  )
}
SUPA_SERVER

  cat > src/lib/supabase/client.ts << 'SUPA_CLIENT'
import { createBrowserClient } from '@supabase/ssr'

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
SUPA_CLIENT

  cat > src/lib/auth.ts << 'AUTH'
import { redirect } from 'next/navigation'
import { createClient } from '@/lib/supabase/server'

export async function getSession() {
  const supabase = createClient()
  const { data: { session } } = await supabase.auth.getSession()
  return session
}

export async function getUser() {
  const supabase = createClient()
  const { data: { user } } = await supabase.auth.getUser()
  return user
}

export async function requireAuth() {
  const user = await getUser()
  if (!user) redirect('/login')
  return user
}
AUTH
fi

# ============================================================
# 9. API health check
# ============================================================
cat > src/app/api/health/route.ts << 'HEALTH'
import { NextResponse } from 'next/server'

export async function GET() {
  return NextResponse.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    version: process.env.npm_package_version ?? '0.0.0',
  })
}
HEALTH

# ============================================================
# 10. Middleware
# ============================================================
if [[ "$INCLUDE_SUPABASE" == "true" ]]; then
  cat > src/middleware.ts << 'MIDDLEWARE'
import { NextRequest, NextResponse } from 'next/server'
import { createServerClient } from '@supabase/ssr'

export async function middleware(request: NextRequest) {
  const response = NextResponse.next()

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => request.cookies.getAll(),
        setAll: (cs) =>
          cs.forEach(({ name, value, options }) =>
            response.cookies.set(name, value, options)
          ),
      },
    }
  )

  const { data: { session } } = await supabase.auth.getSession()
  const { pathname } = request.nextUrl

  if (pathname.startsWith('/dashboard') && !session) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  if (pathname === '/login' && session) {
    return NextResponse.redirect(new URL('/dashboard', request.url))
  }

  return response
}

export const config = {
  matcher: ['/dashboard/:path*', '/settings/:path*', '/login'],
}
MIDDLEWARE
fi

# ============================================================
# 11. Vitest config
# ============================================================
cat > vitest.config.ts << 'VITEST'
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: ['./test/setup.ts'],
    globals: true,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html'],
      include: ['src/**/*.{ts,tsx}'],
      exclude: ['src/**/*.test.*', 'src/types/**', 'src/app/**'],
    },
  },
  resolve: {
    alias: { '@': resolve(__dirname, './src') },
  },
})
VITEST

cat > test/setup.ts << 'TESTSETUP'
import '@testing-library/jest-dom'
import { vi } from 'vitest'

vi.mock('next/navigation', () => ({
  useRouter: () => ({ push: vi.fn(), replace: vi.fn(), refresh: vi.fn(), back: vi.fn() }),
  usePathname: () => '/',
  useSearchParams: () => new URLSearchParams(),
  redirect: vi.fn(),
  notFound: vi.fn(),
}))

vi.mock('next/headers', () => ({
  cookies: () => ({ get: vi.fn(), set: vi.fn(), getAll: vi.fn(() => []) }),
}))
TESTSETUP

# ============================================================
# 12. .prettierrc
# ============================================================
cat > .prettierrc << 'PRETTIER'
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100
}
PRETTIER

# ============================================================
# 13. Update package.json scripts
# ============================================================
node -e "
const fs = require('fs')
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'))
pkg.scripts = {
  ...pkg.scripts,
  'type-check': 'tsc --noEmit',
  'test': 'vitest',
  'test:watch': 'vitest --watch',
  'test:coverage': 'vitest --coverage',
  'format': 'prettier --write .',
  'db:generate': 'drizzle-kit generate',
  'db:migrate': 'drizzle-kit migrate',
  'db:push': 'drizzle-kit push',
  'db:studio': 'drizzle-kit studio',
}
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2))
"

# ============================================================
# 14. shadcn/ui
# ============================================================
if [[ "$INCLUDE_SHADCN" == "true" ]]; then
  echo "🎨 Configurando shadcn/ui..."
  
  # Criar components.json manualmente (evitar prompt interativo)
  cat > components.json << 'SHADCN_JSON'
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/app/globals.css",
    "baseColor": "slate",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
SHADCN_JSON

  # Instalar componentes shadcn essenciais
  pnpm dlx shadcn@latest add button --no-interaction 2>/dev/null || \
    echo "⚠️  shadcn auto-add falhou — rode manualmente: pnpm dlx shadcn@latest add button input form dialog"
fi

# ============================================================
# 15. .gitignore
# ============================================================
cat >> .gitignore << 'GITIGNORE'

# Local env files
.env.local
.env.*.local

# Playwright
e2e/.auth/

# Coverage
coverage/

# Drizzle
drizzle/
GITIGNORE

# ============================================================
# 16. Git init
# ============================================================
echo "📦 Inicializando repositório Git..."
git init
git add .
git commit -m "chore: initial project setup — Next.js 15 + Supabase + Tailwind"

# ============================================================
# Done!
# ============================================================
echo ""
echo "✅ Projeto criado com sucesso!"
echo ""
echo "   📁 $PROJECT_DIR"
echo ""
echo "Próximos passos:"
echo "  cd $PROJECT_DIR"
echo "  1. Copiar .env.example → .env.local e preencher variáveis"
if [[ "$INCLUDE_SUPABASE" == "true" ]]; then
  echo "  2. Criar projeto no Supabase: https://supabase.com"
  echo "  3. pnpm db:push (após configurar DATABASE_URL)"
fi
if [[ "$INCLUDE_SHADCN" == "true" ]]; then
  echo "  4. pnpm dlx shadcn@latest add input form dialog select (adicionar componentes)"
fi
echo "  5. pnpm dev"
echo ""

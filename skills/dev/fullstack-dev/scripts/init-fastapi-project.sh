#!/usr/bin/env bash
# init-fastapi-project.sh — Bootstrap FastAPI + PostgreSQL + Alembic
# Uso: ./init-fastapi-project.sh --name meu-api [--dir /path]
set -euo pipefail

# ============================================================
# Defaults
# ============================================================
PROJECT_NAME=""
BASE_DIR="$HOME/projects"
PYTHON_CMD="python3"
INCLUDE_REDIS=false
INCLUDE_AI=false

# ============================================================
# Help
# ============================================================
usage() {
  cat <<EOF
init-fastapi-project.sh — Bootstrap FastAPI + PostgreSQL + Alembic

Uso:
  $0 --name <nome> [opções]

Opções:
  --name <nome>       Nome do projeto (obrigatório)
  --dir <path>        Diretório base (default: ~/projects)
  --redis             Incluir Redis + BullMQ
  --ai                Incluir OpenAI + Anthropic
  -h, --help          Mostrar esta ajuda

Exemplos:
  $0 --name bidspark-api
  $0 --name canguu-backend --redis --ai
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
    --redis)  INCLUDE_REDIS=true; shift ;;
    --ai)     INCLUDE_AI=true;   shift ;;
    -h|--help) usage ;;
    *) echo "Opção desconhecida: $1"; usage ;;
  esac
done

if [[ -z "$PROJECT_NAME" ]]; then
  echo "❌ --name é obrigatório."
  exit 1
fi

PROJECT_DIR="$BASE_DIR/$PROJECT_NAME"

echo ""
echo "🚀 Iniciando projeto FastAPI: $PROJECT_NAME"
echo "   Destino: $PROJECT_DIR"
echo ""

if [[ -d "$PROJECT_DIR" ]]; then
  echo "❌ Pasta $PROJECT_DIR já existe."
  exit 1
fi

# Verificar Python
if ! command -v "$PYTHON_CMD" &> /dev/null; then
  if command -v python &> /dev/null; then
    PYTHON_CMD="python"
  else
    echo "❌ Python 3 não encontrado."
    exit 1
  fi
fi

PYTHON_VERSION=$("$PYTHON_CMD" --version 2>&1 | awk '{print $2}')
echo "🐍 Python: $PYTHON_VERSION"

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# ============================================================
# 1. Virtual environment
# ============================================================
echo "📦 Criando virtual environment..."
"$PYTHON_CMD" -m venv .venv
source .venv/bin/activate

# ============================================================
# 2. requirements.txt
# ============================================================
echo "📦 Instalando dependências..."

BASE_REQS=(
  "fastapi>=0.115.0"
  "uvicorn[standard]>=0.30.0"
  "pydantic>=2.0.0"
  "pydantic-settings>=2.0.0"
  "sqlalchemy>=2.0.0"
  "asyncpg>=0.29.0"
  "alembic>=1.13.0"
  "python-jose[cryptography]>=3.3.0"
  "passlib[bcrypt]>=1.7.4"
  "python-multipart>=0.0.6"
  "httpx>=0.27.0"
  "loguru>=0.7.0"
)

DEV_REQS=(
  "pytest>=8.0.0"
  "pytest-asyncio>=0.23.0"
  "pytest-cov>=4.0.0"
  "httpx>=0.27.0"
  "ruff>=0.4.0"
  "mypy>=1.10.0"
)

if [[ "$INCLUDE_REDIS" == "true" ]]; then
  BASE_REQS+=("redis>=5.0.0" "celery[redis]>=5.4.0")
fi

if [[ "$INCLUDE_AI" == "true" ]]; then
  BASE_REQS+=("openai>=1.30.0" "anthropic>=0.28.0")
fi

# Escrever requirements.txt
printf '%s\n' "${BASE_REQS[@]}" > requirements.txt
printf '%s\n' "${DEV_REQS[@]}" > requirements-dev.txt

pip install -r requirements.txt -r requirements-dev.txt --quiet

# ============================================================
# 3. Estrutura de pastas
# ============================================================
echo "📁 Criando estrutura de pastas..."
mkdir -p \
  app/api/v1/endpoints \
  app/core \
  app/db \
  app/models \
  app/schemas \
  app/services \
  app/utils \
  alembic/versions \
  tests/api \
  tests/services

touch \
  app/__init__.py \
  app/api/__init__.py \
  app/api/v1/__init__.py \
  app/api/v1/endpoints/__init__.py \
  app/core/__init__.py \
  app/db/__init__.py \
  app/models/__init__.py \
  app/schemas/__init__.py \
  app/services/__init__.py \
  app/utils/__init__.py \
  tests/__init__.py \
  tests/api/__init__.py \
  tests/services/__init__.py

# ============================================================
# 4. app/core/config.py
# ============================================================
cat > app/core/config.py << 'CONFIG'
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    APP_NAME: str = "API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/mydb"

    # Security
    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 dia
    ALGORITHM: str = "HS256"

    # CORS
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    # Redis (opcional)
    REDIS_URL: str = "redis://localhost:6379"

    # AI (opcional)
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
CONFIG

# ============================================================
# 5. app/db/database.py
# ============================================================
cat > app/db/database.py << 'DATABASE'
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
DATABASE

# ============================================================
# 6. app/core/security.py
# ============================================================
cat > app/core/security.py << 'SECURITY'
from datetime import datetime, timedelta, timezone
from typing import Any
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str | Any, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode = {"sub": str(subject), "exp": expire}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
SECURITY

# ============================================================
# 7. app/models/base.py
# ============================================================
cat > app/models/base.py << 'MODELS_BASE'
import uuid
from datetime import datetime, timezone
from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
MODELS_BASE

# ============================================================
# 8. main.py
# ============================================================
cat > app/main.py << 'MAIN'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import router as api_v1_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
MAIN

# ============================================================
# 9. API v1 router
# ============================================================
cat > app/api/v1/router.py << 'ROUTER'
from fastapi import APIRouter
# from app.api.v1.endpoints import users, items

router = APIRouter()

# router.include_router(users.router, prefix="/users", tags=["users"])
# router.include_router(items.router, prefix="/items", tags=["items"])
ROUTER

# ============================================================
# 10. Alembic init
# ============================================================
echo "📦 Configurando Alembic..."
alembic init alembic 2>/dev/null || true

# alembic.ini já criado, ajustar sqlalchemy.url
sed -i 's|sqlalchemy.url = .*|sqlalchemy.url = postgresql+psycopg2://postgres:password@localhost:5432/mydb|' alembic.ini

cat > alembic/env.py << 'ALEMBIC_ENV'
import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# Import todos os models para Alembic detectar
from app.db.database import Base  # noqa
# from app.models.user import User  # noqa (descomente conforme adicionar models)

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
ALEMBIC_ENV

# ============================================================
# 11. .env.example
# ============================================================
cat > .env.example << 'ENVEXAMPLE'
# App
APP_NAME=MeuApp
APP_VERSION=0.1.0
DEBUG=true
ENVIRONMENT=development

# Database
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/mydb

# Security
SECRET_KEY=change-me-in-production-use-secrets-manager
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# CORS
ALLOWED_ORIGINS=["http://localhost:3000"]

# Redis (opcional)
REDIS_URL=redis://localhost:6379

# AI (opcional)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
ENVEXAMPLE

cp .env.example .env

# ============================================================
# 12. Tests setup
# ============================================================
cat > tests/conftest.py << 'CONFTEST'
import asyncio
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.main import app
from app.db.database import get_db, Base

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/testdb"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def db_session():
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    async with session_factory() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()
CONFTEST

cat > tests/api/test_health.py << 'TEST_HEALTH'
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data
TEST_HEALTH

# ============================================================
# 13. Makefile
# ============================================================
cat > Makefile << 'MAKEFILE'
.PHONY: dev test lint format migrate

dev:
	uvicorn app.main:app --reload --port 8000

test:
	pytest tests/ -v --cov=app --cov-report=term-missing

lint:
	ruff check app/ tests/
	mypy app/

format:
	ruff format app/ tests/
	ruff check --fix app/ tests/

migrate-new:
	alembic revision --autogenerate -m "$(name)"

migrate:
	alembic upgrade head

migrate-down:
	alembic downgrade -1
MAKEFILE

# ============================================================
# 14. .gitignore
# ============================================================
cat > .gitignore << 'GITIGNORE'
.venv/
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.coverage
htmlcov/
dist/
*.egg-info/
.env
.ruff_cache/
.mypy_cache/
GITIGNORE

# ============================================================
# 15. pyproject.toml
# ============================================================
cat > pyproject.toml << 'PYPROJECT'
[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.12"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
PYPROJECT

# ============================================================
# 16. Git init
# ============================================================
echo "📦 Inicializando repositório Git..."
git init
git add .
git commit -m "chore: initial project setup — FastAPI + PostgreSQL + Alembic"

# ============================================================
# Done!
# ============================================================
echo ""
echo "✅ Projeto FastAPI criado com sucesso!"
echo ""
echo "   📁 $PROJECT_DIR"
echo ""
echo "Próximos passos:"
echo "  cd $PROJECT_DIR"
echo "  source .venv/bin/activate"
echo "  1. Editar .env com suas credenciais"
echo "  2. make dev (rodar servidor)"
echo "  3. Acessar docs: http://localhost:8000/docs"
echo "  4. Criar primeiro model em app/models/"
echo "  5. make migrate-new name=create_users_table"
echo "  6. make migrate"
echo ""

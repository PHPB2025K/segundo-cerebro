---
title: "SOP — Resetar Senha Funcionário (Ponto Certo)"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - sop
  - rh
  - ponto-certo
  - supabase
---

# SOP — Resetar Senha Funcionário (Ponto Certo)

> Como resetar senha de funcionário no sistema de ponto.

---

## Dados do Sistema

| Campo | Valor |
|-------|-------|
| Sistema | Ponto Certo |
| URL | https://pontocerto.gbformulario.com |
| Supabase | `dgldsmhbeosjgfrbegyv` |
| Auth | Supabase Auth (email + senha) |
| Credenciais admin | 1Password vault OpenClaw |

---

## Funcionários Cadastrados

| Nome | Função |
|------|--------|
| Franciele Carolina de Souza Aguiar (Fran) | Operação |
| Geziele Batista da Silva | Operação |
| Guilherme Higashi | Operação |
| Lucas Gabriel Laurentino | Operação |
| Mateus Eduardo Lisboa Santos | Operação |
| Sandra Peron | Operação |
| Yasmin Oscarlino | Operação |
| Pedro H P Broglio | Admin (excluído de monitoramento) |

---

## Opção 1 — Self-Service (funcionário faz sozinho)

1. Acessar https://pontocerto.gbformulario.com/login
2. Clicar "Esqueceu a senha?"
3. Digitar email cadastrado
4. Supabase envia link de reset (válido 24h)
5. Clicar no link → definir nova senha
6. Login com nova senha

---

## Opção 2 — Via Supabase Dashboard (admin)

1. Acessar https://app.supabase.com
2. Ir ao projeto `dgldsmhbeosjgfrbegyv`
3. Navegar: **Authentication → Users**
4. Buscar email do funcionário
5. Clicar menu "⋮" → **Reset password**
6. Sistema envia email de reset automaticamente
7. Funcionário segue o fluxo (mesmo da Opção 1)

---

## Opção 3 — Via CLI (admin)

```bash
# Linkar ao projeto
supabase link --project-ref dgldsmhbeosjgfrbegyv

# Enviar email de reset
# (usar Supabase Admin API diretamente)
curl -X POST "https://dgldsmhbeosjgfrbegyv.supabase.co/auth/v1/recover" \
  -H "apikey: <ANON_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"email": "email@funcionario.com"}'
```

---

## Notas Importantes

- **Senhas**: Supabase Auth faz hash (bcrypt). Nunca armazenar senhas em texto
- **RLS**: Policies protegem `profiles` e `time_records` por `auth.uid()` — funcionários veem apenas seus próprios dados
- **Admin**: Conta do Pedro tem `app_metadata.role = "admin"`
- **MFA**: Não habilitado atualmente
- **Reset token**: Válido por 24 horas

---

## Edge Functions Relacionadas

| Function | O que faz |
|----------|-----------|
| `validate-qr-ponto` | Validação QR code (requer JWT) |
| `validate-qr-ponto-public` | Clock-in rápido sem login |
| `detectar-atrasos` | Check diário de presença (cron 08:00 BRT) |
| `reset-banco-horas` | Fechamento mensal banco de horas |

---

## Notas Relacionadas

- [[openclaw/agents/rh/IDENTITY]] — agente RH
- [[memory/context/people]] — equipe
- [[knowledge/concepts/credenciais-map]] — credenciais

---
title: "Vercel Hobby bloqueia deploy quando commit author email é inválido"
created: 2026-04-20
type: concept
status: active
tags:
  - knowledge
  - vercel
  - git
  - deploy
  - troubleshooting
---

# Vercel Hobby bloqueia deploy quando commit author email é inválido

## Sintoma

`vercel --prod --yes` retorna genérico:

```json
{
  "status": "error",
  "reason": "deploy_failed",
  "message": "",
  "next": [{ "command": "vercel deploy", "when": "retry deploy" }]
}
Error: Unexpected error. Please try again later. ()
```

- `vercel inspect` mostra `status: ● Error`, `Builds . [0ms]` (build nem rodou)
- `vercel logs` não retorna nada (runtime logs apenas, não build)
- Auto-deploy via GitHub push também falha silenciosamente

A mensagem CLI é **genérica e enganosa** — sugere erro transitório ("try again later") quando na verdade é validação de commit.

## Causa real

O plano **Hobby** da Vercel valida que o **author email** de cada commit bate com um email verificado na conta GitHub do usuário. Se não bater, bloqueia o deploy.

A mensagem só aparece no **dashboard** (aba Deployment):

> "Deployment Blocked — The deployment was blocked because the commit author email (pedrobroglio@Pedro-MacBook-Pro.local) is not valid. Ensure your git email matches your GitHub account."

Acontece quando `git config user.email` não está setado — git usa fallback `{user}@{hostname}.local` que é inválido como email real.

## Workaround em 3 passos

1. **Setar git config global** com email verificado no GitHub:
   ```bash
   git config --global user.email "seu-email-github@gmail.com"
   git config --global user.name "Seu Nome"
   ```
   Isso corrige **commits futuros** mas não reescreve os antigos.

2. **Empty commit com author correto** sobre `origin/main` (ou branch de deploy):
   ```bash
   git fetch origin
   git checkout --detach origin/main
   git commit --allow-empty -m "chore: trigger deploy with correct author"
   git push origin HEAD:main
   ```
   O novo HEAD tem author válido. Vercel aceita esse commit — builda a árvore inteira normalmente (o empty commit só cria um HEAD novo).

3. **Deploy**:
   ```bash
   vercel --prod --yes
   ```
   Funciona. Deploy normal, build roda, prod atualiza.

## Alternativas

- **Desativar validação no dashboard** (Settings → Git → toggle protections): funciona mas afrouxa segurança contra deploys não-autorizados.
- **Reescrever history com force-push**: `git commit --amend --reset-author` ou `git filter-repo` pra trocar author em commits antigos, depois `git push --force-with-lease`. **Destrutivo** — requer autorização explícita se outros consomem a branch.
- **Plano Pro** não tem essa validação.

## Como detectar rápido no futuro

```bash
git log -1 --pretty=fuller
# Author: Nome <*.local>  ← suspeito
# Commit: Nome <email-real@gmail.com>  ← ok
```

Se `Author` tiver `.local` ou o hostname do Mac, vai bloquear Vercel Hobby.

## Aplicado em

- [[projects/budamix-ecommerce]] 2026-04-20 — hotfix Rules of Hooks (PDP branco) ficou preso por 30+ min até descobrir a causa real via screenshot do dashboard. Empty commit `135570e` destravou.

## Ver também

- [[knowledge/concepts/react-hooks-order-early-return]] — o bug que a gente estava tentando deployar
- [[memory/sessions/2026-04-20]] — sessão 3 (Budamix E-commerce end-to-end)

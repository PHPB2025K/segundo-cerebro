---
title: "Ponto Certo"
created: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/ponto-certo/"
tags:
  - project
  - dev
  - rh
---

# Ponto Certo

**Path:** `~/Documents/05-Projetos-Codigo/ponto-certo/`
**Branch:** main
**Stack:** Vite + React + TypeScript + Tailwind + shadcn/ui + Supabase
**Deploy:** VPS 187.77.237.231, PM2 (porta 3091), Traefik HTTPS
**URL:** https://ponto.budamix.com.br
**Supabase:** dgldsmhbeosjgfrbegyv
**GitHub:** https://github.com/PHPB2025K/ponto-certo.git

## O que é

Ponto eletrônico dos funcionários Budamix. Registro de entrada/saída/intervalo com validação GPS (raio do escritório), QR Code diário, banco de horas, atrasos, relatórios admin. Funcionários usam pelo celular (Android/iOS).

## Decisões-chave

- [15/04] Timer baseado em primitivo ms (não Date object) — evita race condition em Android
- [15/04] Deploy via SCP (token GitHub na VPS inválido)

## Pendências

- [ ] Reautenticar `gh auth` na VPS para restaurar `git pull`
- [ ] Validar timer Android com funcionário real
- [ ] Validar layout mobile estoque (equipe usa celular no armazém)

## Notas relacionadas

- [[openclaw/agents/rh/IDENTITY]] — Agente RH monitora ponto
- [[memory/context/people]] — Equipe de funcionários

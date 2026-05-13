---
title: "Mission Control"
created: 2026-05-12
type: project
status: active
tags:
  - project/mission-control
  - infra
---

# Mission Control

Painel operacional interno baseado no fork TenacitOS, retomado em 2026-05-12.

## Estado atual

- Domínio oficial: `mission.budamix.com.br`.
- Traefik/SSL ativo.
- Frontend base 100% customizado para identidade Budamix/GB.
- Dashboard PRD implementado com atividade real do vault.
- 23/23 páginas autenticadas respondem 200 sem `Application error`.

## Próximas frentes

- PRDs por módulo: Cron, Tasks, Sessions, Skills, Agents detail, Office 3D, Activity, Analytics, Reports, System, Git, Files, Memory, Search, Logs, Terminal.
- Criar/configurar `data/configured-skills.json`.
- Refinar detecção de `botToken` em `auth-profiles.json`.
- Remover/justificar hex hardcoded restantes em Three.js.

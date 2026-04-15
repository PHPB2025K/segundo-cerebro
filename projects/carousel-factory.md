---
title: "Carousel Factory"
created: 2026-04-14
updated: 2026-04-15
type: project
status: paused
path: "~/Documents/05-Projetos-Codigo/carousel-factory/"
tags:
  - project
  - dev
  - marketing
  - n8n
---

# Carousel Factory

**Path:** `~/Documents/05-Projetos-Codigo/carousel-factory/`
**Frontend separado:** `~/Documents/05-Projetos-Codigo/carousel-factory-frontend/`
**Branch:** main
**Stack:** React + Tailwind + Supabase (frontend) | Node.js + Puppeteer (rendering engine) | N8N (orquestração) | Claude Sonnet 4 + DALL-E 3 (AI pipeline)
**Deploy:** nenhum (pausado)
**CLAUDE.md:** não

## O que é

Sistema de geração automatizada de carrosséis para Instagram e marketplaces. Pipeline AI completo: copywriting → design → geração de imagens → renderização.

## Arquitetura

| Componente | Stack | Função |
|------------|-------|--------|
| Frontend | React + Tailwind + Supabase | Dashboard, criar, preview, histórico |
| Orquestração | N8N (webhooks) | `/carousel/zero`, `/carousel/template`, `/carousel/regenerate`, `/carousel/publish` |
| AI Pipeline | Claude Sonnet 4 (4 chamadas) + DALL-E 3 | Copywriter → Designer → Image Prompts → QA + geração de imagens |
| Rendering Engine | Node.js + Puppeteer + Docker | HTML → PNG (1080×1350px @ 2x retina), 7 templates |
| Banco | Supabase | carousels, slides, brand_kits, style_presets, generation_logs + Storage buckets |

## Modos

- **Zero Mode**: Pipeline AI completo — custo ~$0.26-0.38/carrossel (DALL-E 3 domina custo)
- **Template Mode**: Via Canva API — custo ~$0.02-0.07/carrossel (futuro, não implementado)

## Status

⏸️ **Pausado há 7+ semanas.** Documentação completa (architecture, API contracts, costs, setup, N8N workflows). Frontend funcional (React + Supabase). Rendering engine com Dockerfile pronto. Falta: conectar tudo via N8N e testar pipeline end-to-end.

## Notas relacionadas

- [[projects/n8n-builder]] — infraestrutura N8N compartilhada
- [[business/marketing/_index]] — marketing
- [[meta/mocs/MOC - Design Systems Budamix]] — design system
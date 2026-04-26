---
title: "Nano Banana MCP — Setup e Modelos Gemini"
created: 2026-04-15
type: reference
status: active
tags:
  - knowledge
  - mcp
  - gemini
  - image-generation
---

# Nano Banana MCP — Setup e Modelos Gemini

## Config atual

MCP usa cópia local patcheada (não npx):

```
~/.claude/mcp-bins/nano-banana/dist/index.js
```

Config em `~/.claude.json`:
```json
{
  "type": "stdio",
  "command": "node",
  "args": ["/Users/pedrobroglio/.claude/mcp-bins/nano-banana/dist/index.js"],
  "env": { "GEMINI_API_KEY": "..." }
}
```

**Por que local?** `npx -y` baixa versão original do npm a cada restart, sobrescrevendo o patch do modelo.

## Modelo ativo

`gemini-3-pro-image-preview` (Nano Banana Pro) — ~$0.13/img, melhor qualidade.

Patch aplicado em 2 ocorrências (linhas 190 e 298 do `dist/index.js`).

## Modelos de imagem disponíveis (Gemini API, abril 2026)

| Model ID | Display Name | Custo |
|----------|-------------|-------|
| `gemini-2.5-flash-image` | Nano Banana | Mais barato |
| `gemini-3-pro-image-preview` | Nano Banana Pro | ~$0.13/img |
| `gemini-3.1-flash-image-preview` | Nano Banana 2 | — |
| `imagen-4.0-fast-generate-001` | Imagen 4 Fast | — |
| `imagen-4.0-generate-001` | Imagen 4 | — |
| `imagen-4.0-ultra-generate-001` | Imagen 4 Ultra | — |

**Modelo descontinuado:** `gemini-2.5-flash-image-preview` (com `-preview`) — 404 desde ~abril 2026.

## Script workaround (sem MCP)

```bash
~/.claude/mcp-bins/nano-banana/gemini-image.sh "prompt" [output.png] [model]
```

Chama API REST diretamente via curl. Útil quando MCP não está conectado.

## Requisitos

- `GEMINI_API_KEY` com **billing ativo** (free tier tem quota 0 para imagem) — token gerenciado conforme [[knowledge/concepts/credenciais-map]]
- `npm install --production` executado em `~/.claude/mcp-bins/nano-banana/`

## 6 tools disponíveis

`generate_image`, `edit_image`, `continue_editing`, `get_last_image_info`, `configure_gemini_token`, `get_configuration_status`

## Ver também

- [[knowledge/concepts/credenciais-map]] — mapa de tokens/credenciais (Gemini, Anthropic, OpenAI)
- [[knowledge/concepts/stack-tecnico]] — stack geral, MCPs ativos
- [[knowledge/concepts/claude-code-skills-inventario]] — inventário de skills e MCPs do Claude Code
- [[meta/mocs/MOC - Token Management]] — governança de tokens API/MCP
- [[knowledge/concepts/nano-banana-no-alpha-channel]] — limitação conhecida do Gemini imagem (sem canal alfa)

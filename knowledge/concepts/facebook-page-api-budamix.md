---
title: "Integração Facebook Page API — Budamix"
created: 2026-06-03
modified: 2026-06-04
type: knowledge
status: active
tags:
  - knowledge
  - integration
  - facebook
  - meta
  - budamix
---

# Integração Facebook Page API — Budamix

Acesso direto via Graph API à página Budamix do Facebook para edições de conteúdo (capa, foto de perfil, bio, posts). Configurado em 03/06/2026 via Claude Code.

## Coordenadas

| Item | Valor |
|---|---|
| **App Meta** | KOBE.OPENCLAW |
| **App ID** | `1486886096369858` (⚠️ NÃO confundir com `3582660648568553` — esse é outro app) |
| **App Secret** | armazenado fora do vault (1Password pendente — atualmente só em chat history) |
| **Página** | Budamix |
| **Page ID** | `106066888942641` |
| **URL canônica** | https://www.facebook.com/106066888942641 |
| **URL alternativa** | https://www.facebook.com/profile.php?id=100086248724676 (formato New Pages Experience que aponta pra mesma) |
| **Business Manager owner** | Budamix (`836285430695962`) |
| **Token type** | Non-expiring Page Access Token |
| **API version** | v23.0 |

## Localização dos artefatos (Mac local)

```
~/bin/budamix-page/
  setup.sh           # script de setup (gera token a partir de user token + app secret)
  fb-page            # CLI wrapper (info, about, update-about, upload-profile, upload-cover, raw)

~/.config/budamix-page/
  token              # page access token não-expirante (perm 600)
  meta.json          # app_id, page_id, scopes, created_at
```

## Scopes concedidos

- `pages_show_list`
- `pages_read_engagement`
- `pages_manage_metadata`
- `pages_manage_posts`

## Comandos do CLI

```bash
~/bin/budamix-page/fb-page info                          # snapshot completo da página
~/bin/budamix-page/fb-page about                         # ler bio curta
~/bin/budamix-page/fb-page update-about "texto"          # editar bio (campo about, ~155 chars)
~/bin/budamix-page/fb-page update-description "texto"    # editar descrição longa
~/bin/budamix-page/fb-page upload-profile <url|path>     # trocar foto de perfil
~/bin/budamix-page/fb-page upload-cover <url|path>       # trocar capa
~/bin/budamix-page/fb-page get-cover                     # URL da capa atual
~/bin/budamix-page/fb-page raw GET <endpoint> [param=value...]
~/bin/budamix-page/fb-page raw POST <endpoint> [param=value...]
```

## Como o token foi obtido (referência se precisar regenerar)

1. Graph API Explorer → app KOBE.OPENCLAW → User Token com os 4 scopes pages_*
2. Granted consent no popup do FB selecionando explicitamente a página Budamix
3. Trocou short-lived (2h) por long-lived (60d) via `/oauth/access_token` com `grant_type=fb_exchange_token`
4. **Quirk crítico:** `/me/accounts` retornou vazio mesmo com permissões corretas. Workaround: `GET /{page_id}?fields=access_token` direto retorna o page token derivado do user long-lived → page token resultante é **não-expirante**
5. Salvo em `~/.config/budamix-page/token` (perm 600)

## Recomendações operacionais

### Resoluções ideais para uploads

- **Foto de perfil:** 1080×1080 PNG (display final 170×170 desktop, 128×128 mobile)
- **Capa:** 1640×924 (proporção 1.78:1 que casa com mobile, desktop crop pega faixa central 1640×624)
- **Safe zone capa:** conteúdo crítico nos 1280×612 centrais do canvas

### Limitação do FB

- **Username (vanity URL) NÃO pode ser setado via API básica** — bloqueia com `(#3) Application does not have the capability`. Requer feature "Page Public Content Access" aprovada pela Meta. Setar manualmente via Meta Business Suite quando necessário.
- **Capa não suporta variantes desktop/mobile separadas** — é uma imagem única que o FB corta em proporções diferentes por device.

### Limitação de segurança atual

- App Secret e User Token usados no setup ficaram no histórico do chat Claude Code de 03/06/2026.
- App KOBE.OPENCLAW é o mesmo do OpenClaw na VPS → comprometimento aqui afetaria também o agente principal.
- **Ação recomendada:** rotacionar App Secret no Meta Developers quando possível. Page token salvo continua válido (já derivado).

### Migração futura para VPS / Kobe

Quando fizer sentido, o token e o wrapper podem migrar pra VPS (`/root/.openclaw/...`) para que o Kobe automatize publicações. Hoje (04/06/2026) o setup é só local pra edições pontuais conduzidas pelo Pedro.

## Estado atual da página (snapshot 03/06/2026)

- 147 fãs · Categoria "Loja de artigos para o lar"
- 2 admins: Pedro Broglio + Leonardo SegundaVenda
- Site cadastrado: http://www.budamix.com.br/ (sugestão pendente: trocar pra https)
- Email: budamix.co@gmail.com
- Telefone: +5519992979180
- Endereço: Av. Papa João XXIII, 850A, Pedreira-SP
- Horário: Seg-Qui 9-18h, Sex 9-17h
- Bio atual: *"Vidro borossilicato para quem leva organização da cozinha a sério. Marmita fitness, meal prep e geladeira em ordem."*
- Capa atual: arte "LEVE MAIS PAGUE MENOS" (kits potes vidro borossilicato, R$ 84,90)
- Logo atual: símbolo da casa Budamix® em fundo Deep Teal (~85% do canvas)

## Notas relacionadas

- [[memory/context/decisoes/2026-06]]
- [[memory/sessions/2026-06-03]]
- [[projects/openclaw-config]]

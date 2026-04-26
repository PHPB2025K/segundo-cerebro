---
title: "tools-map"
created: 2026-04-26
type: memory-integration
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - integration
---
# Mapa de Ferramentas e Integrações

## Ativas
| Ferramenta | Uso | Acesso |
|---|---|---|
| GitHub | Backup do workspace | PHPB2025K/tobias-workspace (cron diário 03h UTC) |
| Telegram | Canal de comunicação Pedro ↔ Tobias | Bot @TOBIAS_USER_BOT, polling |
| Claude Opus 4.6 | Modelo principal (análise, estratégia) | Via Anthropic |
| Claude Sonnet 4.6 | Modelo econômico (crons, tarefas simples) | Via Anthropic (alias: sonnet) |
| Brave Search | Pesquisa web em tempo real | API key no config + 1Password |
| 1Password CLI | Cofre de credenciais | Service Account, vault "OpenClaw" |
| gog CLI | Google Calendar (futuro: Gmail, Drive, Sheets) | OAuth, conta gb.ai.agent@gbimportadora.com |
| wttr.in | Clima sem API key | web_fetch direto |

## Credenciais (1Password - Vault "OpenClaw")
| Item | Tipo |
|---|---|
| Telegram Bot Token | PASSWORD |
| Anthropic Setup Token | PASSWORD |
| Brave | LOGIN |
| Gmail Openclaw | LOGIN |
| Google Workspace - Tobias Agent | LOGIN |

## Email do Tobias
- **Email:** gb.ai.agent@gbimportadora.com
- **Tipo:** Google Workspace (domínio gbimportadora.com)
- **Credenciais:** 1Password (Google Workspace - Tobias Agent)

## Configuração do Servidor
- **systemd override:** ~/.config/systemd/user/openclaw-gateway.service.d/override.conf
  - OP_SERVICE_ACCOUNT_TOKEN (1Password)
  - GOG_KEYRING_PASSWORD (gog CLI)
  - GOG_ACCOUNT (gb.ai.agent@gbimportadora.com)

## Marketplaces (acesso do Pedro)
- Mercado Livre — conta ativa
- Shopee — conta ativa
- Amazon BR — conta ativa

## Contas Google (gog OAuth)
| Conta | Gmail | Calendar | Drive | Sheets |
|---|---|---|---|---|
| pehpbroglio@gmail.com | ✅ | ✅ | ✅ | ✅ |
| gb.ai.agent@gbimportadora.com | ✅ | ✅ | — | — |

## Futuras / A configurar
- Integrações com APIs de marketplace (quando Bidspark avançar)
- Google Drive + Sheets para gb.ai.agent (quando necessário)

## Bright Data Web Unlocker (2026-03-18)
- **Tipo:** Proxy residencial + anti-bot + JS rendering
- **Zone:** web_unlocker1
- **API:** POST https://api.brightdata.com/request
- **Auth:** Bearer {api_key} (1Password → "Bright Data Web Unlocker")
- **Conta:** tobias.broglio@gmail.com
- **Uso principal:** Scraping ML (busca de concorrentes)
- **Paginação ML:** `?page=N` (NÃO usar _Desde_ ou _NoIndex_)

## Planilha de Estoque/Precificação (2026-03-18)
- **Google Sheets ID:** 1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI
- **Nome:** PLANILHA DE ESTOQUE
- **Abas relevantes:** MELI (precificação ML), SHOPEE, AMAZON, ESTOQUE
- **Headers MELI (row 6):** ESTOQUE, SKU, PRODUTO, PREÇO DE CUSTO, PREÇO DE VENDA, ANUNCIO, FRETE CHEIO, COMISSÃO ML, CUSTO FIXA, IMPOSTO, CAIXA, FULL, DEVOLUÇÕES, EMBALAGEM, ADS, FRETE, COMISSÃO AFILIADO, MARGEM, LUCRO LIQ
- **Acesso:** gog sheets get "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI" "MELI!A6:Z100" --json

## Meta Ads API (2026-03-19)
- **App:** KOBE.OPENCLAW (ID: 3582660648568553)
- **App Secret:** 1Password → "Meta Ads API - KOBE.OPENCLAW" (credential)
- **Token:** Long-lived 60 dias (gerado 2026-03-19, expira ~2026-05-18)
- **Token location:** 1Password → "Meta Ads API - KOBE.OPENCLAW" (access_token)
- **Business:** GB Distribuição (ID: 7723008527787239)
- **Conta principal:** act_323534883953033 (GB Distribuição)
- **Outras contas ativas:** act_1140258596603533 (Budamix), act_599689043839914 (Broglio Brinquedos), act_851375860374263 (Trades Up)
- **System User:** Não criado (limite BM atingido — TYPEBOTUSER + Conversions API ocupam os slots)
- **Cron lembrete:** Renovar token em 2026-05-15
- **API version:** v21.0

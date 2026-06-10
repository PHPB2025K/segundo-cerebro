---
title: "GB Importadora — LP Institucional"
created: 2026-06-10
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/gb-importadora-lp/"
tags:
  - project
  - dev
  - ecommerce
  - empresa/gb
---

# GB Importadora — LP Institucional

**Path local:** `~/Documents/05-Projetos-Codigo/gb-importadora-lp/`
**Repo:** a criar — `PHPB2025K/gb-importadora-lp` (privado)
**Stack (produção):** React 18 + Vite 5 + TypeScript + Tailwind — mesmo padrão do [[projects/klap-porcelana]]
**Deploy:** Vercel
**Domínio:** www.importadoragb.com.br (a registrar no Registro.br)

## O que é

Landing page institucional da GB Importadora — a empresa-mãe das marcas Budamix e Klap Porcelana. **Zero funcionalidade de venda online**: apresenta a empresa, menciona as duas marcas (link único pro site de cada uma), mostra a operação de importação e a localização (mapa Pedreira-SP / Itajaí-SC com toggle). Atacado aparece só como menção discreta no contato.

## Identidade visual (aprovada 10/06)

Paleta **"Casa de Comércio"** — escolhida entre 5 opções (estudo em `mockup/paletas.html`). Tinta & Papel (monocromática) foi aplicada e revertida na mesma sessão.

| Token | HEX | Função |
|-------|-----|--------|
| Grafite | `#1C1B18` | Base escura — hero, números, footer |
| Areia | `#EFEAE2` | Background |
| Cobre | `#B5764A` | Acento |
| Pedra | `#8A877F` | Apoio |

Tipografia: **Archivo** (display) + **Inter** (corpo), self-hosted via Fontsource na produção.
Logo oficial: monograma branco (versão negativa) — vive nas bases escuras; gerar versão grafite pra fundos claros.

## Estrutura (8 seções)

Hero → Quem somos → Nossas marcas (cards Budamix/Klap, únicos pontos de cor) → Como operamos (4 passos) → Números → Onde estamos (mapa toggle SP/SC) → Contato → Footer.

## Arquivos

| Arquivo | O quê |
|---------|-------|
| `mockup/index.html` | Mockup standalone aprovado (validado desktop 1440 + mobile 390 via Playwright) |
| `mockup/paletas.html` | Estudo das 5 paletas com mini-previews |
| `PLANO-IMPLEMENTACAO.md` | Plano Fases 0-4 até deploy |

## Marcos

| Data | Marco |
|------|-------|
| 10/06/2026 | Briefing v2 + identidade aprovada + mockup completo entregue (Fase 0 ✅) |

## Próximos passos (Fase 1 — prevista 11/06)

- [ ] Registrar `importadoragb.com.br` no Registro.br
- [ ] Projeto Vite + React + TS + Tailwind, repo GitHub privado
- [ ] Portar mockup pra componentes (Fase 2)
- [ ] Conteúdo do Pedro: logo SVG/PNG alta, endereços completos, telefone/WhatsApp comercial, CNPJ/razão social, e-mail de contato (contato@importadoragb.com.br vs marketplace@gbimportadora.com)
- [ ] SEO (JSON-LD Organization) + DNS + deploy Vercel (Fase 4)

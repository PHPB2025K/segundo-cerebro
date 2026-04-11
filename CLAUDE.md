# Pedro Broglio — Contexto para o Claude Code

## Fontes de Contexto

| Fonte | Path | O que tem |
|-------|------|-----------|
| **Segundo Cérebro** | `~/segundo-cerebro/` | Contexto operacional: pendências, decisões, projetos |
| **Este arquivo** | `~/.claude/CLAUDE.md` | Perfil, diretrizes gerais |
| **OpenClaw (Kobe)** | VPS 187.77.237.231 | Agente AI principal, crons, integrações, memória operacional |

> **Regra:** antes de criar algo novo, consultar o segundo cérebro. Contexto operacional vive lá, não aqui.

---

## Quem sou eu

Pedro Broglio. Empresário, importador, builder de automações com AI. Founder da GB Importadora (marca Budamix) — importação de utensílios domésticos em vidro, cerâmica e porcelana, sourcing primário em Yiwu (China). Ex-IBM, ex-Tetra Pak, ex-Page Personnel. Empreendedor desde que foi demitido por "pensar fora da caixa". Inglês fluente (exchange na Austrália).

Filosofia: "Não existe tamanho mínimo para importar ou usar AI." Autonomia sobre estabilidade. Executa antes de estar 100% pronto. Se posiciona como tradutor de complexidade para quem acha que não é pra eles.

---

## Negócio Principal — GB Importadora / Budamix

- Importação de utensílios domésticos (vidro, cerâmica, porcelana)
- Sourcing: Yiwu, China (2 viagens, Canton Fair)
- 6 CNPJs operacionais
- Facilidades: Pedreira-SP (operação) e Itajaí-SC (TTD 409, benefício fiscal ICMS)
- Portos: Itajaí e Itapoá | Trading: Open Trade | ICMS 4%
- Marca INPI registrada: Budamix
- Visual Identity: Deep Teal #004D4D | Graphite #132525 | Sage #7EADAD | Amber Gold #C7A35A | Terracota #C56A4A

### Canais de Venda
- **Amazon BR**: FBA, SP-API + Amazon Ads integrados
- **Shopee**: 3 contas OAuth, auto-refresh 3h30
- **Mercado Livre**: 3 apps (Vendas, Financeiro, Métricas), anúncios com variações
- **budamix.com.br**: e-commerce próprio
- **TikTok Shop**: exploração (outreach MCN/afiliados)

### SKUs Ativos
- PMR (Porta Modem Roteador): próximo SKU PMR014
- XCP (Xícara Paris 170ml): próximo SKU XCP023
- SPC (Suporte Porta Controle Gamer): próximo SKU SPC016
- CTL (Caneca Tulipa 250ml): CTL001-CTL010

---

## Projetos e Automações

| Projeto | O que é | Status |
|---------|---------|--------|
| **OpenClaw/Kobe** | Agente AI principal, 6 sub-agentes, 22 crons, 16 integrações | 🟢 Produção |
| **Canggu** | Dashboard interno Budamix (produtos, conversas, analytics) | 🟢 Produção |
| **FinanceFlow** | Automação Word→Excel via Claude + Supabase para 6 CNPJs | 🔨 Em construção |
| **SimulaImport** | MicroSaaS simulação custos importação (NCM, cascata tributária) | 🔨 Em construção |
| **Atlas Finance** | DFC (fluxo de caixa) com Lovable/Supabase | 🔨 Em construção |
| **Módulo Conferências** | Validação custos importação (Simulação/PNI/DI vs Referência) | 🔨 Em construção |
| **Jornal da Manhã** | Digest diário via Perplexity API + Claude + React | 🟢 Produção |

---

## Infraestrutura AI — OpenClaw (Kobe)

- **VPS**: Hostinger Ubuntu 24.04, IP 187.77.237.231
- **OpenClaw**: v2026.4.2, Gateway 127.0.0.1:18789 (loopback only)
- **Agentes**: Kobe (main), Trader, Spark, Builder, Fisco, RH
- **Modelo**: migrando para GPT 5.4 (default) + GPT 5.1-mini (crons)
- **WhatsApp**: dual mode — Baileys (leitura passiva) + Evolution API (envio)
- **Telegram**: canal principal, bot @TOBIAS_USER_BOT, Kobe Hub 11 tópicos
- **Custo**: ~$120/mês Anthropic (em migração para OpenAI)

---

## Stack Técnico

- **Backend**: Node.js 22, Python, Bash
- **Banco**: Supabase (PostgreSQL + pgvector + Realtime + Edge Functions)
- **Frontend**: React (Lovable), Tailwind
- **AI/LLM**: OpenClaw (GPT 5.4/5.1-mini), Claude Code, Claude API
- **Integrações**: Evolution API, Bling ERP, Amazon SP-API, Shopee API, ML API, Brave Search, 1Password CLI, GitHub CLI, gog CLI
- **DevTools**: VS Code com MCPs (Supabase, Context7, Playwright, Frontend Design), Claude Code

---

## Como prefiro trabalhar

- Resposta direta, sem preâmbulo. Sou técnico avançado — CLI, Docker, SSH, Git no dia a dia
- Código pronto para executar, não sugestões vagas
- Sempre verificar o segundo cérebro antes de criar algo novo
- Quando houver trade-offs, apresente opções com prós/contras e recomende uma
- Sinalize riscos de segurança proativamente
- Considere a stack existente — evite sugerir ferramentas que dupliquem o que já funciona
- Português brasileiro. Termos técnicos em inglês

---

## Segundo Cérebro

| Estou buscando... | Onde ir |
|-------------------|---------|
| O que está em aberto | `$SECOND_BRAIN_PATH/memory/context/pendencias.md` |
| Prazos | `$SECOND_BRAIN_PATH/memory/context/deadlines.md` |
| Decisões recentes | `$SECOND_BRAIN_PATH/memory/context/decisoes/YYYY-MM.md` |
| Status dos projetos | `$SECOND_BRAIN_PATH/memory/projects/_index.md` |
| Equipe e contatos | `$SECOND_BRAIN_PATH/memory/context/people.md` |
| Contexto geral | `$SECOND_BRAIN_PATH/memory/context/business-context.md` |

---

## Skills pessoais

- [[skills/coaching-corrida/SKILL|Coaching Corrida]]

---

## Ver também

- [[PROPAGATION|Protocolo de Propagação]]

---

*Criado: 06/04/2026*
*Atualizar: sempre que contexto mudar*

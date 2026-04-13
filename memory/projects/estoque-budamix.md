# Estoque Budamix

> Status: 🟢 Produção

## O que é
Sistema web para controle de entrada e saída de produtos do armazém GB Importadora via Google Sheets. Upload de PDF para lançamentos em lote.

## URLs
- **App:** https://estoque.budamix.com.br
- **VPS:** /var/www/estoque-budamix (PM2: estoque-budamix, porta 3050)
- **Traefik:** /docker/traefik/dynamic/estoque-budamix.yml
- **N8N Workflow:** Estoque PDF Parser (ID: WyxKDxwIkuuL8BdH) — https://trottingtuna-n8n.cloudfy.live
- **Supabase:** Projeto Budamix Central (sqbkoprcmnznmzbwdrmf) — tabelas `estoque_config` + `estoque_operations`
- **Planilha:** PLANILHA DE ESTOQUE / PRECIFICAÇÃO — aba ESTOQUE

## Stack
- Next.js 16 + Tailwind CSS + shadcn/ui
- Supabase JS (service role key, mesmo projeto Budamix Central)
- Google Sheets API v4 (service account: estoque-sheets@estoque-budamix.iam.gserviceaccount.com)
- N8N Cloudfy (pdf-parse via webhook)
- Fontes: Plus Jakarta Sans + DM Sans + JetBrains Mono

## Responsáveis
- **Pedro:** Owner, deploy, decisões

## Timeline
| Data | Evento |
|------|--------|
| 13/04/2026 | Projeto criado (scaffold + build + deploy VPS) |
| 13/04/2026 | Migração SQLite/Prisma → Supabase Postgres |
| 13/04/2026 | Design system Budamix aplicado (teal/areia/terracotta) |
| 13/04/2026 | Upload PDF via N8N webhook (Cloudfy) implementado |

## Decisões Tomadas
- [13/04] Supabase em vez de SQLite — mesmo projeto do Budamix Central com prefixo `estoque_`
- [13/04] Supabase JS client em vez de Prisma — consistência com Budamix Central
- [13/04] PDF parsing no N8N (Cloudfy) em vez de Next.js — pdfjs-dist não funciona em SSR
- [13/04] Traefik para reverse proxy (não Nginx) — VPS usa Traefik nas portas 80/443
- [13/04] Design system próprio: Plus Jakarta Sans + DM Sans + JetBrains Mono, paleta Budamix

## Pendências
- [ ] Conectar com a planilha de estoque real (credenciais da service account já configuradas)
- [ ] Testar fluxo completo: upload PDF → preview → confirmar entrada → atualizar planilha
- [ ] Validar layout em mobile (equipe usa celular no armazém)

---
*Criado: 13/04/2026*

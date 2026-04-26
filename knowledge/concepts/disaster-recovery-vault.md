---
title: "Disaster Recovery — Vault Single Source of Truth"
created: 2026-04-26
type: concept
status: active
tags:
  - knowledge
  - infra
  - resilience
  - vault
  - openclaw
---

# Disaster Recovery — Vault Single Source of Truth

> Arquitetura de redundância tripla do segundo cérebro + memória runtime do Kobe.
> Concluída em 2026-04-26 após hidratação do tobias-workspace pro vault e setup de
> sync bidirecional + backup Supabase.

## Princípio

**Single source of truth + redundância distribuída.** Toda memória de negócio (vault Obsidian +
runtime do Kobe) vive em uma fonte única (`segundo-cerebro` no GitHub) com 3 camadas de
backup independentes. Qualquer ponto de falha é recuperável em ≤4h.

## Arquitetura (estado em 2026-04-26)

```
                ┌─────────────────────────────────────────┐
                │   VAULT  =  FONTE ÚNICA DA VERDADE     │
                │   PHPB2025K/segundo-cerebro (GitHub)   │
                └───┬─────────────────────────────────┬───┘
                    │                                 │
        ┌───────────┴──────┐               ┌──────────┴────────┐
        │ Mac local        │               │ VPS Hostinger     │
        │ ~/segundo-cerebro│               │ /root/segundo-... │
        │ (Claude Code +   │               │ (Kobe + 5 agents) │
        │  Obsidian)       │               │                   │
        └───┬──────────────┘               └────────┬──────────┘
            │                                        │
            │ git push (manual via /salve)           │ */15 git pull (cron)
            │                                        │ :07,22,37,52 sync memory→vault (cron)
            ▼                                        ▼
    ┌──────────────────────┐              ┌──────────────────────┐
    │ Obsidian Sync        │              │ Supabase Storage     │
    │ (entre dispositivos  │              │ vault-snapshots/     │
    │  Pedro)              │              │ daily/vault-DATE.tgz │
    └──────────────────────┘              │ (cron 06:00 UTC)     │
                                          └──────────────────────┘
```

## 3 camadas de redundância

| Camada | Onde | Update | Como acessar |
|--------|------|--------|--------------|
| 1 | GitHub `PHPB2025K/segundo-cerebro` | Tempo real (git push) | `git clone` |
| 2 | Obsidian Sync nos dispositivos do Pedro (Mac, iPad, celular) | Tempo real (Obsidian core plugin sync) | Reinstalar Obsidian + entrar na conta |
| 3 | Supabase Storage `vault-snapshots/` em projeto `yqgtuatoyzmgcqdweina` | Diário 06:00 UTC | `curl` na Storage REST API com service_role |

Adicional: tobias-workspace antigo (`PHPB2025K/tobias-workspace`) preserva snapshot histórico até ser arquivado na Fase 4.

## Crons ativos na VPS (`/root/`)

```cron
# Pull do vault na VPS — disponibiliza pro Kobe ler
*/15 * * * * cd /root/segundo-cerebro && /usr/bin/git pull --rebase origin main >> /root/segundo-cerebro-sync.log 2>&1

# Push da memória do Kobe pro vault (workspace → vault)
7,22,37,52 * * * * /root/scripts/sync-memory-to-vault.sh

# Backup diário do vault pro Supabase
0 6 * * * /root/scripts/daily-vault-backup.sh

# Sync legado vault → workspace (skills + canonics) — coexiste sem conflito
45 9 * * * /root/.openclaw/workspace/scripts/sync-segundo-cerebro.sh
```

## Scripts críticos

| Script | Função | Auth |
|--------|--------|------|
| `/root/scripts/sync-memory-to-vault.sh` | Workspace → vault. Helper Python `merge-frontmatter.py` preserva frontmatter + denylist defensiva (credentials/tokens/secrets/.env) | Deploy Key SSH `/root/.ssh/segundo_cerebro_deploy` |
| `/root/scripts/daily-vault-backup.sh` | Tarball + upload Supabase + retenção 30 daily/12 monthly | service_role lida do 1Password em runtime (`op item get "Supabase: Segundo Cerebro"`) |

Padrão: **toda credencial é lida do 1Password em runtime, nunca hardcoded** (consolidado após incidente Bling 26/04).

## Credenciais (1Password vault OpenClaw)

| Item | Uso |
|------|-----|
| `Supabase: Segundo Cerebro` | service_role (`sb_secret_*`) pra upload no bucket vault-snapshots |
| `Bling API - Matriz (58.151.616/0001-43)` | Client Secret rotacionado 26/04 |
| `Bling API - Filial (58.151.616/0002-24)` | Client Secret rotacionado 26/04 (empresa inativa pendente) |

Deploy Key segundo-cerebro: `/root/.ssh/segundo_cerebro_deploy` (write access habilitado em GitHub Settings → Keys).

## Cenários de recuperação

### A — Mac roubado/perdido
**Tempo:** ≤1h. **Perda:** zero.

```bash
# Em Mac novo:
git clone git@github.com:PHPB2025K/segundo-cerebro.git ~/segundo-cerebro
# Reinstalar Obsidian + entrar na conta → sync recupera config dos dispositivos
# Reinstalar Claude Code + apontar pra ~/segundo-cerebro
```

### B — VPS destruída
**Tempo:** ~4h. **Perda:** zero (vault tem memória runtime do Kobe).

```bash
# Provisionar VPS nova (Ubuntu 24.04)
# Restaurar SSH keys do 1Password
# Restaurar OpenClaw via instalador + restaurar tobias-workspace OU vault openclaw/
git clone git@github.com:PHPB2025K/segundo-cerebro.git /root/segundo-cerebro
# Configurar Deploy Key, crons, OP_SERVICE_ACCOUNT_TOKEN
# Bootstrap Kobe lendo de /root/segundo-cerebro/openclaw/agents/kobe/
```

### C — Conta GitHub PHPB2025K perdida
**Tempo:** ~2h. **Perda:** zero.

```bash
# Baixar snapshot mais recente do Supabase:
curl -H "apikey: $(op item get 'Supabase: Segundo Cerebro' --vault OpenClaw --field notesPlain --reveal | grep -oE 'sb_secret_[A-Za-z0-9_-]+' | head -1)" \
  https://yqgtuatoyzmgcqdweina.supabase.co/storage/v1/object/vault-snapshots/daily/vault-LATEST.tar.gz \
  -o vault.tar.gz
tar -xzf vault.tar.gz
# Criar nova conta GitHub OU usar conta backup existente
# Push para repo novo
```

### D — Supabase apagado
**Tempo:** ~30min. **Perda:** zero (vault no GitHub continua intacto).

Recriar projeto Supabase + bucket + atualizar 1Password + 1 run manual do `daily-vault-backup.sh`.

### E — Conta Anthropic/Claude Code perdida
**Tempo:** imediato. **Perda:** zero.

Vault é independente de Claude. Trocar conta + apontar pro mesmo `~/segundo-cerebro` local.

### F — Catastrófico (Mac + VPS + GitHub simultâneos)
**Tempo:** ~3h. **Perda:** zero (Supabase tem snapshot diário + dispositivos com Obsidian Sync).

Restaurar do Supabase em qualquer máquina com `op` configurado.

### G — Pior caso (todas as 4 + Obsidian Sync falham simultaneamente)
**Tempo:** indeterminado. **Perda:** parcial (último snapshot Supabase ≤24h atrás).

Probabilidade quase nula sem ataque coordenado em 4 provedores diferentes (Apple/iCloud, Hostinger, GitHub, Supabase).

## Validação periódica recomendada

A cada 30 dias:
- [ ] Listar bucket Supabase: confirmar 30 daily + N monthly
- [ ] Baixar 1 snapshot aleatório, descompactar, conferir integridade
- [ ] Confirmar Obsidian Sync ativo nos dispositivos secundários
- [ ] Verificar last commit no GitHub
- [ ] Tail dos logs `/root/segundo-cerebro-sync.log`, `/root/sync-memory-to-vault.log`, `/root/vault-backup.log`

## Referências

- Decisão arquitetural: [[memory/context/decisoes/2026-04|Decisões abril 2026]] — entrada 26/04
- Skills do Kobe: [[openclaw/agents/kobe/MEMORY|MEMORY]]
- Estratégia de busca: [[CLAUDE]] (segundo-cerebro raiz)
- Próxima fase: arquivar tobias-workspace + DR drill (Fase 5)

## Histórico

- **2026-04-26 manhã:** hidratação do tobias-workspace pro vault (commit `c01b0e5`)
- **2026-04-26 tarde:** Fase 2A (clone na VPS + cron pull), 2B-LITE (sync workspace → vault)
- **2026-04-26 tarde:** rotação Bling Matriz/Filial após detecção de leak no commit 86b7956 (limpeza C2 — token antigo invalidado)
- **2026-04-26 noite:** Fase 3 (backup Supabase) — primeiro snapshot 2.4 MB validado
- **2026-04-26 noite:** Fase 5 (DR drill) — arquitetura **verified resilient** (resultados abaixo)

## Validação 26/04 — DR drill executado

Drill não-destrutivo em sandbox (`/tmp/dr-drill/`) testando os cenários A-G.

| # | Cenário | Resultado |
|---|---------|-----------|
| 1 | **Restaurar 1 arquivo via Supabase** — download `daily/vault-2026-04-26.tar.gz`, extrair `IDENTITY.md`, comparar com vault local | ✅ diff=0 (idêntico). Restauração granular funciona. |
| 2 | **Clone fresh do vault** (cenário Mac novo) — `gh repo clone` pra `/tmp/dr-drill/fresh` | ✅ 649 .md (igual Mac local). 637/649 com frontmatter YAML. Last commit `704d01e`. Cenário A (Mac roubado) coberto. |
| 3 | **Restauração total via Supabase** (cenário GitHub perdido) — extract do snapshot e diff com Mac local | ✅ 647 .md no snapshot · 2 só no Mac (sessão 26/04 + DR plan, criados pós-snapshot 18:50 UTC). 0 arquivos só no snapshot. Diff esperado e correto. Cenário C/D/F coberto. |
| 4 | **Validar Deploy Key SSH** — `ssh -T git@github.com-segundocerebro` na VPS | ✅ "Hi PHPB2025K/segundo-cerebro!" + exit 1 (esperado pra GitHub sem shell). Auth funcional, write access intacto. |
| 5 | **Retenção daily/ no Supabase** | ✅ 1 arquivo (`vault-2026-04-26.tar.gz`), abaixo do limite 30. Vai crescer 1/dia até estabilizar. |
| 6 | **Leitura service_role do 1P em runtime + upload teste** — `op item get` na VPS, upload `_drill/test-*.txt` no bucket | ✅ 1P leitura OK (`sb_secret_1X9...` 41 chars), upload HTTP 200, cleanup HTTP 200. Padrão "secrets via 1P runtime" comprovadamente funcional. |
| 7 | **KG rebuild from scratch** — `KG_DATA_DIR=/tmp/dr-drill/kg-test npx tsx ... index` | ✅ 648 nodes / 738 nodes_fts / 1772 edges / 182 comunidades / 90 stubs (wikilinks pendentes). Busca FTS funciona — `MATCH 'disaster recovery'` retornou `disaster-recovery-vault.md` corretamente. KG é regenerável a partir do vault, não é fonte autoritativa. |

### Achados colaterais do drill (candidatos a polish)

- **1 frontmatter malformed**: `skills/marketplace/shopee-fees-rules/SKILL.md` — KG tratou como plain markdown (não fatal). Corrigir frontmatter quando passar pelo arquivo.
- **2 wikilinks ambíguos** (legados, não-qualificados): `[[agents/kobe/IDENTITY]]` e `[[skills/superpowers/dispatching-parallelopenclaw/agents/SKILL]]`. KG pegou primeiro match. Quando aparecerem, usar path completo `[[openclaw/agents/kobe/IDENTITY]]`.
- **90 stub nodes**: wikilinks apontando para notas que ainda não existem. Normal em vault em evolução. Resolver caso a caso quando criar a nota referenciada.

### Conclusão

Arquitetura de 3 camadas **funciona em todos os cenários testados**. Recovery time observado:
- Restaurar 1 arquivo do Supabase: **~5s** (download + extract)
- Clone fresh do GitHub: **~3s** (vault tem 25 MB)
- Rebuild do KG do zero: **~20s** (648 nodes + 1772 edges)

Total para Mac novo do zero (clone vault + KG rebuild): **<1 minuto**. Bem abaixo do "≤1h" estimado no plan.

Status: **verified resilient** ✅ — todos os 7 testes concluídos com sucesso em 26/04/2026.

### Resumo dos cenários cobertos por teste

| Cenário do plan | Teste(s) que cobre | Status |
|-----------------|---------------------|--------|
| A — Mac roubado/perdido | #2 (clone fresh) + #7 (KG rebuild) | ✅ |
| B — VPS destruída | #4 (SSH Deploy Key) + #6 (1P runtime) | ✅ |
| C — GitHub perdido | #1 + #3 (restauração via Supabase) | ✅ |
| D — Supabase apagado | inverso de #3 — vault no Git intacto | ✅ inferência |
| E — Conta Anthropic perdida | trivial (vault independente de Claude) | ✅ inferência |
| F — Catastrófico (Mac+VPS+GitHub) | #1 + #3 + #6 (Supabase + 1P) | ✅ |
| G — Pior caso (todos + Obsidian) | sem dispositivo, requer recreate manual; fora do escopo do drill | n/a |

**Pendência única para "fully verified":** simular cenário B (VPS destruída) provisionando uma 2ª VPS e fazendo bootstrap do Kobe. Custo: ~4h + custo da 2ª VPS por algumas horas. Adiado para próxima oportunidade — os componentes individuais (clone, 1P, SSH Deploy, refresh tokens) já foram testados no fluxo normal das semanas anteriores.

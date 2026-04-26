---
title: "simulimport"
created: 2026-04-26
type: memory-project
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - project
---
# Projeto: SimulImport

## Status: 🟢 Sprint Ativo (reativado 29/03)

## O que é
Simulador de importação. Usuário preenche dados básicos e recebe uma simulação precisa de custos e prazos de importação.

## Stack
- Frontend: React + Vite + TanStack Query + Tailwind
- Backend: Supabase (Auth + DB)
- Hosting: Lovable (production) + VPS preview (https://simulimport.srv1480018.hstgr.cloud)
- Repo: github.com/PHPB2025K/simulimport

## Entregas recentes (29-30/03)
- ✅ Auditoria completa (12 bugs, roadmap 3 sprints)
- ✅ COFINS corrigido 10,65% → 9,65% (Lei 14.288/2021)
- ✅ .env segurança (removido do tracking, .env.example criado)
- ✅ Identidade visual Navy Blue (paleta própria, 10 componentes)
- ✅ Deploy VPS com HTTPS via Traefik
- ✅ Framer Motion removido da landing (causava opacity:0)
- ✅ 4 commits pushed ao GitHub
- ✅ Job IPI (TIPI) — 10.506 NCMs com IPI real (7.962 atualizados)
- ✅ Job II (TEC) — 10.301 NCMs com II real (152 atualizados, 503 novos). Base final: 11.023 NCMs
- ⏳ Job Antidumping (MDIC) — scraping ~85 produtos, em execução

## Base NCM — Estado Atual
- **11.023 NCMs** no Supabase (seed-ncm.sql)
- IPI: corrigido via TIPI oficial (ADE RFB 1/2026) ✅
- II: corrigido via TEC oficial (Gecex 136/2020) ✅
- PIS: 2,10% (padrão) ✅
- COFINS: 9,65% (Lei 14.288/2021) ✅
- Antidumping: tabela separada em construção ⏳

## Reforma Tributária — Arquitetura Futura (Pesquisa Pedro 30/03)

### Contexto
EC 132/2023 + LC 214/2025 muda completamente a cascata tributária de importação. O SimulaImport precisa ter isso no DNA — não como feature, mas como arquitetura base.

### Cronograma da Reforma
| Ano | Mudança |
|-----|---------|
| 2026 | CBS 0,9% + IBS 0,1% (teste, extras, compensáveis) |
| 2027 | CBS ~8,8% cheia. PIS/COFINS extintos. IPI zerado (exceto ZFM) |
| 2029-2032 | ICMS reduz (90→60%), IBS sobe. TTD 409 extinto proporcionalmente |
| 2033 | ICMS/ISS extintos. IBS (~17,7%) + CBS (~8,8%) = ~26,5% "por fora" |

### Novos tributos no schema
- **CBS** (alíquota + valor) — substitui PIS + COFINS
- **IBS_estadual + IBS_municipal** (alíquotas + valores) — substitui ICMS
- **Imposto Seletivo (IS)** — tabaco, álcool, açucarados, veículos, minerais
- **IPI_residual** — zerado, ativo apenas p/ produtos ZFM

### Novas tabelas Supabase (planejadas)
- `ncm_imposto_seletivo` — NCMs sujeitos ao IS
- `ncm_aliquota_reduzida` — 60% de redução IBS/CBS ou zero (cesta básica)
- `uf_aliquota_ibs` — alíquota IBS por estado
- `municipio_aliquota_ibs` — alíquota IBS por município
- `ncm_ipi_zfm` — IPI residual Zona Franca
- `transicao_icms` — fator por ano (2029: 0.9, 2030: 0.8, 2031: 0.7, 2032: 0.6)
- `cesta_basica_ncm` — NCMs com alíquota zero

### Mudanças no motor de cálculo
- IBS e CBS são "por fora" (não usam fórmula ICMS "por dentro" 1/(1-alíq))
- Transição 2029-2032: ICMS residual "por dentro" + IBS "por fora" simultâneos
- IS entra na base do IBS e CBS
- Princípio do destino: IBS do estado do importador (não do porto)
- Extinção progressiva de benefícios fiscais (TTD 409 etc.)

### Feature diferencial — Comparativo temporal
Mostrar lado a lado: "Se importar em 2026" vs "2028" vs "2033"
→ Diferencial competitivo enorme pro SaaS

### Roadmap de implementação
- **Sprint 2:** Campo "Ano da simulação" + lógica temporal básica (2026: atual, 2027: CBS)
- **Sprint 3:** Motor completo transição 2029-2032 + regime definitivo 2033
- **Sprint 4:** Tabelas IS, alíquotas reduzidas, cesta básica, comparativo temporal

### Princípio arquitetural
A arquitetura do banco e motor de cálculo deve estar PREPARADA pra receber essas mudanças sem refatoração. Campos, tabelas e lógica temporal como fundação — preenchidos gradualmente.

## Próximos Passos
1. ✅ Job IPI (TIPI) — completado 30/03
2. ✅ Job II (TEC) — completado 30/03
3. ⏳ Antidumping MDIC — em execução (timeout 60min)
4. Testar motor de cálculo com NCMs corrigidos
5. Validar cenários reais com importações do Pedro
6. Sprint 2: campo "Ano da simulação" + lógica temporal (reforma tributária)
7. Sync com Lovable (project ID pendente)
8. Monetização (gateway de pagamento inexistente)

## Notas
- Pedro tem experiência real em importação — o produto vem de dor própria
- Potencial de mercado: muitos pequenos importadores não sabem calcular custos reais
- Lovable project ID nunca registrado (README tem placeholder)
- Reforma tributária é diferencial competitivo ENORME — nenhum simulador no mercado faz comparativo temporal
- Documento técnico completo da reforma: `shared/simulimport/reforma-tributaria-importacao.md` (348 linhas — cronograma, fórmulas, tabelas, regras de negócio)

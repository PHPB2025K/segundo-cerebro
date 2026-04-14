---
title: "CHANGELOG v2"
created: 2026-04-14
type: changelog
agent: kobe
status: active
tags:
  - agent/kobe
---

# CHANGELOG — Spark Memory Pack v1.0 → v2.0

_Auditoria e melhorias realizadas em 2026-03-20_

---

## Resumo

| Arquivo | Status | Nível de mudança |
|---|---|---|
| MEMORY.md | Melhorado | Médio |
| accounts.md | Melhorado | Alto |
| context/business.md | Melhorado | Alto |
| context/decisions.md | Melhorado | Médio |
| context/lessons.md | Melhorado | Baixo |
| playbook.md | Melhorado | Alto |
| feedback/reviews.json | Melhorado | Alto |
| campaigns/active.md | Mantido | — |
| campaigns/history.md | Mantido | — |
| sessions/TEMPLATE.md | **Novo** | — |

---

## Detalhamento por arquivo

### MEMORY.md
- **Adicionado:** Health Check de Memória semanal (checklist para o Spark se auto-auditar)
- **Adicionado:** Template de Sessão Diária completo (antes era apenas referência)
- **Melhorado:** Tabela de hierarquia com explicação de conflitos entre arquivos
- **Melhorado:** Regras de carregamento com trigger words ("ANTES de recomendar", "ANTES de repetir")

### accounts.md
- **Adicionado:** Protocolo de Token Meta com níveis de alerta (🟢🟡🔴⛔) e ações por nível
- **Adicionado:** Roadmap de integração Google Ads em 7 etapas com status e responsáveis
- **Adicionado:** Padrão UTM recomendado (aguardando aprovação)
- **Adicionado:** Checklist de integridade semanal
- **Adicionado:** Campo de domínio verificado (necessário para iOS 14+)
- **Melhorado:** Data de criação do token (para calcular expiração)

### context/business.md
- **Adicionado:** Personas preliminares para targeting (3 hipóteses para validar)
- **Adicionado:** Cálculo explícito de CPA máximo por fase (em R$, não só %)
- **Adicionado:** Critérios de transição entre fases (Aprendizado → Otimização → Escala)
- **Adicionado:** Tabela de sazonalidade com 12 meses e datas relevantes
- **Adicionado:** Estrutura de mapeamento de concorrentes em ads
- **Adicionado:** Jornada do cliente hipotética com desafio de atribuição cross-platform
- **Melhorado:** Tabela de produtos com implicações para tráfego pago
- **Melhorado:** Parâmetros financeiros com coluna de notas

### context/decisions.md
- **Adicionado:** Seção "Como usar este arquivo" (protocolo de consulta e escrita)
- **Adicionado:** Tabela com colunas Data e Origem (quem tomou a decisão)
- **Adicionado:** Seção "Decisões Revogadas" com template (registro histórico)
- **Adicionado:** Regra de comunicação com outros agentes
- **Melhorado:** Organização por categoria (Arquitetura, Budget, Operacional, Relatórios)

### context/lessons.md
- **Adicionado:** Seção "Como usar este arquivo" (protocolo de consulta)
- **Adicionado:** Campo "Cross-ref" no template (ligação com playbook/decisions)
- **Adicionado:** Seção "Lições Expiradas" (arquivo histórico)
- **Melhorado:** Template de lição com campo "Ação concreta" (antes era genérico)

### playbook.md
- **Adicionado:** Alocação de Budget entre Plataformas (Meta 60% / Google 40% com regra de realocação)
- **Adicionado:** Distribuição por funil dentro de cada plataforma (TOFU/MOFU/BOFU/Retargeting)
- **Adicionado:** Protocolo de Refresh Criativo (sinais, níveis, formato de briefing)
- **Adicionado:** Duração mínima e máxima para testes A/B (7-21 dias)
- **Adicionado:** Coluna "Base de dados" na tabela de benchmarks
- **Adicionado:** Regra de volume mínimo para registrar benchmark interno
- **Melhorado:** Árvore de diagnóstico expandida (mais cenários cobertos)
- **Melhorado:** Checklist de lançamento com anti-canibalização

### feedback/reviews.json
- **Adicionado:** Campo "schema_version" (versionamento da estrutura)
- **Adicionado:** Bloco "scoring" (streak de aprovações, totais, threshold para L2)
- **Adicionado:** Campos "patterns_to_avoid" e "patterns_that_work" (meta-aprendizado)
- **Adicionado:** Campo "impact_on_playbook" no template de entry
- **Melhorado:** max_entries aumentado para 50 (30 era pouco para histórico)

### sessions/TEMPLATE.md (NOVO)
- **Criado:** Template padronizado para sessões diárias
- Inclui: tarefas, métricas, alertas, entregas ao Kobe, feedback, aprendizados, pendências
- Campos de cross-reference com lessons.md e playbook.md

# QA Standards — Daily Sales Analyst

## Critérios de bloqueio

O QA Gate (Camada 7) aplica gates obrigatórios e regra de agregação de severidade.

### Regra de agregação (dura, sem exceção)

- 1+ Crítico → BLOQUEADO
- 2+ Maiores em gates diferentes → BLOQUEADO
- 6+ Menores com degradação sistêmica → BLOQUEADO
- 1 Maior + Menores → APROVADO COM RESSALVA
- 0 Maiores + 1-5 Menores → APROVADO COM RESSALVA
- 0 problemas → APROVADO

### Gates obrigatórios

1. Data, período e fonte
2. Destinatário, plataforma e responsável
3. Estrutura Slack aprovada
4. Visão da Plataforma
5. Top Produtos
6. Análise da Conta (fidelidade à Condensadora)
7. Prioridades do Dia
8. Bloqueios, confiança e logs
9. Consistência entre camadas
10. Tom e utilidade
11. Padrão numérico e formatação objetiva

## Critérios de ressalva

Ressalvas são registradas quando:
- Limitação de confiança sem violação de regra crítica.
- Insight com confiança média mas sem risco de induzir erro.
- Decisão de formatação ambígua mas documentada e segura.
- Pergunta granular secundária não respondida sem impacto na mensagem.

## Hierarquia QA

- QA valida fidelidade e regras objetivas.
- QA não rediagnostica análise.
- Discordância analítica vai em "Ressalvas de auditoria", não em bloqueio.
- QA está abaixo da Condensadora e Granular na hierarquia de decisão.

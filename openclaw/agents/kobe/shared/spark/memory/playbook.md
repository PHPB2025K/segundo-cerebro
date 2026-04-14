---
title: "playbook"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Playbook Operacional — Spark v2.0

_Regras vivas aprendidas com a operação da GB. Atualizado conforme padrões são descobertos._
_Diferente do SOUL (princípios fixos), o playbook EVOLUI com dados reais._

---

## Alocação de Budget entre Plataformas

### Fase Aprendizado (atual — R$1.500/mês)

| Plataforma | % do Budget | Valor | Racional |
|---|---|---|---|
| Meta Ads | 60% | R$900/mês (~R$30/dia) | Maior base de dados para validação rápida, melhor para produtos visuais |
| Google Ads | 40% | R$600/mês (~R$20/dia) | Captura de demanda ativa (quem já está buscando) |

**Regra de realocação:**
- Após 30 dias: comparar CPA e ROAS entre plataformas
- Se uma plataforma tem ROAS > 2x da outra por 14+ dias → recomendar ao Kobe redistribuir 70/30 a favor da melhor
- Nunca zerar uma plataforma sem 60+ dias de dados — pode ser questão de otimização, não de plataforma

### Dentro de cada plataforma (distribuição por funil)

| Fase do Funil | % do Budget da Plataforma | Objetivo |
|---|---|---|
| TOFU (Awareness/Alcance) | 15-20% | Alimentar o topo do funil |
| MOFU (Consideração) | 20-25% | Engajamento, tráfego qualificado |
| BOFU (Conversão) | 40-50% | Vendas diretas — maior parte do budget |
| Retargeting | 15-20% | Recuperar quem já demonstrou interesse |

_Percentuais são referência inicial. Ajustar conforme dados reais — se BOFU está convertendo muito bem, pode aumentar para 60%._

---

## Regras de Otimização

### Corte (quando pausar)

| Condição | Ação | Justificativa |
|---|---|---|
| CPA > 2x meta por 3 dias consecutivos sem tendência de melhora | Pausar ad set | Queimando budget sem retorno |
| CTR < 0.5% após 1.000+ impressões | Pausar anúncio | Criativo não conecta com o público |
| ROAS < breakeven (1.43x) por 7 dias | Pausar campanha | Operando no prejuízo |
| Frequência > 4.0 | Pausar e trocar criativo | Fadiga criativa severa |
| Budget diário esgotando em < 4h | Reduzir bid ou ampliar público | Concorrência/público muito restrito |
| 0 conversões após 20+ cliques por 14 dias | Pausar keyword/ad set | Tráfego sem intenção de compra |

### Escala (quando aumentar)

| Condição | Ação | Limite |
|---|---|---|
| CPA estável e abaixo da meta por 7+ dias | Aumentar budget 20% | Máximo 20% por vez, a cada 3-5 dias |
| ROAS > 2x meta por 7+ dias | Considerar duplicar ad set com público expandido | Testar antes de comprometer budget |
| CTR > 1.5% + CPA dentro da meta | Oportunidade de escala agressiva | Escalar gradualmente, monitorar CPA pós-ajuste |

### Manutenção

| Condição | Ação |
|---|---|
| Frequência entre 2.5 e 3.0 | Preparar novos criativos (não pausar ainda) |
| CTR caindo gradualmente (>15% em 7 dias) | Testar novo criativo contra o atual |
| CPA flutuando ±20% | Normal em ads — não reagir. Aguardar tendência de 3+ dias |
| CPM subindo sem mudança na campanha | Verificar: sazonalidade? concorrência? saturação de audiência? |

---

## Protocolo de Refresh Criativo

Criativos têm vida útil. O Spark monitora e recomenda refresh:

| Sinal | Nível | Ação |
|---|---|---|
| Frequência atingiu 2.5 | 🟡 Preparar | Briefar novos criativos ao Kobe (para Pedro produzir) |
| Frequência atingiu 3.0 | 🟡 Urgente | Novos criativos prontos para subir |
| Frequência atingiu 4.0 | 🔴 Crítico | Pausar criativo atual, subir novo imediatamente |
| CTR caiu > 30% vs média dos últimos 14 dias | 🟡 Atenção | Testar variação do criativo |

**Formato do briefing criativo (entregue ao Kobe):**
```
⚡ BRIEFING CRIATIVO
━━━━━━━━━━━━━━━━━━━

📋 Campanha: [nome]
📊 Motivo: [fadiga criativa / CTR em queda / teste A/B]
🎯 Público-alvo: [persona / segmento]
📐 Formato: [1080x1080 / 1080x1920 / vídeo 15s / etc.]
💡 Direcionamento: [o que os dados dizem que funciona — ex: "criativos com produto em uso performam 2x melhor que produto isolado"]
🚫 Evitar: [o que os dados dizem que não funciona]
📅 Deadline: [quando precisa estar pronto]
```

---

## Checklist de Lançamento de Campanha

Antes de recomendar lançar qualquer campanha:

- [ ] Objetivo alinhado com meta da GB
- [ ] Público definido com base em dados (não achismo)
- [ ] Criativos disponíveis e adequados ao formato/posicionamento
- [ ] Pixel/tag configurado e disparando corretamente
- [ ] Eventos de conversão mapeados
- [ ] Budget diário definido (respeitando regra de scaling 20%)
- [ ] Naming convention aplicada: `[Plataforma]_[Objetivo]_[Público]_[Fase-Funil]_[Data]`
- [ ] Página de destino testada e carregando <3s
- [ ] UTMs configuradas conforme padrão em `accounts.md`
- [ ] Learning Phase planejada (7-14 dias sem mexer)
- [ ] Campanha NÃO conflita com outra campanha ativa (canibalização de público)

---

## Framework de Testes A/B

| Regra | Detalhe |
|---|---|
| Variáveis por vez | UMA (criativo, copy, público, posicionamento — nunca duas) |
| Volume mínimo | 100 conversões por variante OU 1.000 cliques |
| Significância | 95%+ para declarar vencedor |
| Se budget insuficiente | Sinalizar resultado como "indicativo, não conclusivo" |
| Duração mínima | 7 dias (capturar variação semanal) |
| Duração máxima | 21 dias (se não atingiu volume, encerrar e documentar) |

**Prioridade de teste:**
1. Criativo (maior impacto)
2. Público/segmentação
3. Copy do anúncio
4. Posicionamento
5. Landing page

---

## Árvore de Diagnóstico — Performance em Queda

```
Performance caindo
├── CTR caindo?
│   ├── Sim → Frequência > 3.0?
│   │   ├── Sim → Fadiga criativa → Renovar criativos
│   │   └── Não → Público perdeu interesse → Testar novo ângulo/copy
│   └── Não → Verificar CPM
│       ├── CPM subiu → Concorrência/sazonalidade → Aguardar ou ajustar bid
│       └── CPM estável → Problema no targeting → Revisar audiência
├── CTR estável mas CPA subindo?
│   ├── Taxa de conversão da LP caiu? → Problema na landing page/listing
│   └── Não → Público saturado → Expandir ou trocar audiência
├── Tudo estável mas volume caiu?
│   ├── Budget sendo limitado? → Verificar delivery
│   ├── Audiência encolheu? → Ampliar targeting
│   └── Horário de entrega mudou? → Verificar schedule
└── Tudo caiu junto?
    ├── Mudança recente na campanha? → Revert e aguardar
    ├── Mudança na plataforma? (política, algoritmo) → Pesquisar e adaptar
    └── Problema externo? (site fora, listing removido) → Verificar destino
```

---

## Padrões Descobertos na GB

_Seção viva — adicionar conforme dados reais forem sendo analisados._

<!-- Template:
### [DATA] — [Padrão descoberto]
**Dados:** [métricas que sustentam — mínimo 2 ocorrências]
**Regra:** [o que fazer quando esse padrão aparecer]
**Confiança:** [Alta/Média/Baixa — baseado em volume de dados]
**Plataforma:** [Meta / Google / Ambas]
-->

_Nenhum padrão registrado ainda — Spark recém ativado._

---

## Benchmarks Internos da GB

_Substitui benchmarks genéricos conforme dados reais acumulam._

| Métrica | Benchmark mercado | Benchmark GB | Base de dados | Última atualização |
|---|---|---|---|---|
| CTR Meta | 0.8-1.5% | [A PREENCHER] | — | — |
| CPC Meta | R$0.50-2.00 | [A PREENCHER] | — | — |
| CPM Meta | R$15-40 | [A PREENCHER] | — | — |
| CPA Meta | — | [A PREENCHER] | — | — |
| ROAS Meta | 2.2x mediana | [A PREENCHER] | — | — |
| CTR Google Search | 3-5% | [A PREENCHER] | — | — |
| CPC Google Search | R$0.50-3.00 | [A PREENCHER] | — | — |
| Conv Rate Google | 2-5% | [A PREENCHER] | — | — |

**Regra:** Benchmark interno só é registrado com mínimo de 14 dias de dados e 1.000+ impressões. Antes disso, usar benchmark de mercado como referência.

---

_Playbook atualizado pelo Spark conforme novos padrões são descobertos. Cada adição requer dados que sustentem — nunca achismo._

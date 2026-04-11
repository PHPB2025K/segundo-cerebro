---
name: anomaly-detector
description: >
  Detecção de anomalias em campanhas de ads (Meta Ads + Google Ads). Usar quando:
  CPA subiu sem explicação, ROAS caiu drasticamente, budget queimou rápido demais,
  conversões caíram de repente, CTR despencou, suspeit de click fraud, creative fatigue,
  campanha parou de gastar, algo está errado com ads, monitoramento de saúde de campanhas,
  alertas de performance, diagnóstico de problemas em ads, pacing de budget irregular,
  audience shift, frequency alta demais, learning phase preso, ads da GB Importadora
  com problema, campanha Budamix com anomalia.
---

# Anomaly Detector — Skill de Detecção de Anomalias em Ads

> Usado por [[agents/spark/IDENTITY|Spark]]

Monitoramento, detecção e diagnóstico de anomalias em campanhas de ads.
Cross-platform: Meta Ads + Google Ads.
Contexto: GB Importadora (Budamix), ROAS mínimo 10x.

---

## Quando Usar Esta Skill

1. Qualquer métrica de ads mudou drasticamente sem causa óbvia
2. Monitoramento de saúde periódico (heartbeat do Spark)
3. Pedro ou Kobe reporta "algo está errado com os ads"
4. Antes de tomar decisão de budget (verificar se dados estão limpos)
5. Após mudanças significativas (novo creative, novo targeting, mudança de bid)

---

## 5 Tipos de Anomalia

### 1. 🔴 CPA Spike (Custo por Aquisição Disparou)

**Sintoma:** CPA subiu > 50% vs média 7 dias sem mudança intencional.

**Causas comuns:**
- Audience saturation (frequency alta → mesmas pessoas vendo o ad repetidamente)
- Creative fatigue (CTR caindo progressivamente)
- Concorrência aumentou bids (leilão mais caro)
- Tracking quebrado (conversões não registrando → CPA aparente sobe)
- Mudança de algoritmo da plataforma
- Sazonalidade (pós-Black Friday, janeiro, etc.)

**Diagnóstico:**
```
1. CTR caiu junto? → Provável creative fatigue ou audience shift
2. CPC subiu mas CTR manteve? → Concorrência no leilão
3. Conversões caíram mas clicks mantiveram? → Problema de tracking ou landing page
4. Frequency > 3? → Audience saturation
5. Nada acima? → Verificar se houve mudança na plataforma
```

**Ações:**
| Causa | Ação imediata | Ação de follow-up |
|---|---|---|
| Creative fatigue | Pausar creative com CTR < 50% da média | Subir novos criativos |
| Audience saturation | Expandir audiência ou excluir convertidos | Testar novos segments |
| Concorrência | Ajustar bid strategy / reduzir target | Monitorar por 3 dias |
| Tracking | Verificar pixel/CAPI/tag | Fix urgente |
| Sazonalidade | Aceitar e documentar | Planejar para próximo ciclo |

---

### 2. 🔴 Budget Burn (Orçamento Queimou Rápido)

**Sintoma:** Budget diário consumido em < 50% do dia.

**Causas comuns:**
- Bid muito alto para o budget definido
- Audience muito ampla com bid automático agressivo
- Glitch de entrega da plataforma
- CPC inflacionado temporariamente (evento, concorrência)

**Diagnóstico:**
```
1. CPC está normal? → Se alto, verificar leilão
2. Impressões dispararam? → Audience expandiu ou bid subiu
3. Horário do gasto? → Se concentrado, verificar ad scheduling
4. É recorrente? → Se sim, budget insuficiente para a campanha
```

**Ações:**
| Causa | Ação |
|---|---|
| Bid alto | Reduzir target CPA/ROAS ou mudar para manual |
| Audience ampla | Restringir targeting |
| CPC inflação | Esperar 24h, se persistir ajustar bid |
| Budget insuficiente | Aumentar budget ou reduzir escopo |

---

### 3. 🟡 Conversion Drop (Conversões Caíram)

**Sintoma:** Conversões caíram > 40% vs média 7 dias com spend mantido.

**Causas comuns:**
- Tracking quebrado (pixel, CAPI, tag)
- Landing page fora do ar ou lenta
- Mudança de público (iOS privacy, algorithm shift)
- Oferta menos atrativa (preço, estoque, concorrência)
- Conta em review ou restrição

**Diagnóstico:**
```
1. Clicks mantiveram? → Se sim, problema é pós-click (LP, tracking, checkout)
2. Impressões caíram junto? → Entrega reduzida (budget, bid, quality)
3. Taxa de conversão da LP caiu? → Problema na LP, não no ad
4. Conversões em outras plataformas normais? → Problema específico da plataforma
5. Pixel/CAPI reportando? → Verificar eventos no Events Manager / Tag Manager
```

**Ações:**
| Causa | Ação |
|---|---|
| Tracking quebrado | Fix urgente — pausar campanhas se necessário |
| LP fora do ar | Fix urgente |
| Audience shift | Expandir targeting, testar novos segments |
| Oferta | Verificar preço vs concorrência, estoque |

---

### 4. 🟡 Creative Fatigue (Desgaste de Criativo)

**Sintoma:** CTR em queda progressiva (> 20% em 7 dias) em creative específico.

**Diferença de creative fatigue vs anomalia:**
- **Fatigue normal:** Queda gradual ao longo de 7-14 dias. Natural e esperado.
- **Anomalia:** Queda súbita (> 30% em 24-48h). Investigar outra causa.

**Indicadores de fatigue:**
- CTR caindo progressivamente
- Frequency > 3-4x na mesma audiência
- CPM subindo (plataforma penaliza ad com engagement baixo)
- Relevance Score / Quality Ranking caindo

**Ações:**
```
Se CTR caiu > 20% em 7 dias E Frequency > 3:
  1. Pausar creative afetado
  2. Ativar creative novo (se disponível)
  3. Se não há creative novo → alertar Kobe para produção
  4. Registrar lifetime do creative (quanto durou antes de fatigar)
```

---

### 5. 🟡 Audience Shift (Mudança de Público)

**Sintoma:** Métricas de qualidade mudam sem mudança de targeting (demographics, device, geo diferente do esperado).

**Causas comuns:**
- iOS privacy updates (dados de audiência menos precisos)
- Algorithm da plataforma expandiu targeting automaticamente
- Advantage+ (Meta) otimizando para público diferente do configurado
- Concorrentes saíram/entraram do mesmo segmento

**Diagnóstico:**
```
1. Breakdown por age/gender — mudou vs histórico?
2. Breakdown por device — mobile vs desktop ratio mudou?
3. Breakdown por geo — apareceram regiões inesperadas?
4. Placement breakdown — mudou onde os ads estão aparecendo?
```

**Ações:**
| Cenário | Ação |
|---|---|
| Público expandiu mas performance OK | Documentar, monitorar |
| Público expandiu e performance caiu | Restringir targeting manualmente |
| Advantage+ expandindo demais | Configurar audience controls |

---

## Protocolo de Monitoramento

### Frequência

| Check | Frequência | O que verificar |
|---|---|---|
| **Quick check** | Diário | CPA vs meta, spend vs budget, conversões vs esperado |
| **Deep check** | Semanal | Todos os 5 tipos de anomalia, trend analysis |
| **Full audit** | Mensal | Cross-platform, creative lifecycle, audience health |

### Thresholds de Alerta

| Métrica | 🟡 Atenção | 🔴 Crítico | Janela |
|---|---|---|---|
| CPA | > 1.5x meta | > 2x meta | 2 dias |
| ROAS | < 7x | < 5x | 2 dias |
| CTR | Queda > 20% vs 7d | Queda > 40% vs 7d | 3 dias |
| Conv Rate | Queda > 30% vs 7d | Queda > 50% vs 7d | 2 dias |
| Budget Pacing | > 120% antes das 15h | > 150% antes do meio-dia | Intraday |
| Frequency (Meta) | > 3x em 7 dias | > 5x em 7 dias | Semanal |

### Formato de Alerta

```
## 🔴 ANOMALIA — [Tipo] — [Campanha/Plataforma]

**Detectada em:** [data/hora]
**Métrica afetada:** [qual métrica, valor atual vs baseline]
**Severidade:** Crítico | Atenção

**Diagnóstico:**
[resultado da árvore de decisão]

**Causa mais provável:**
[com nível de confiança: alta/média/baixa]

**Ação recomendada:**
[ação específica e imediata]

**Próximo check:**
[quando verificar novamente]
```

---

## Checklist de Diagnóstico Rápido

Quando algo parece errado, seguir esta ordem:

```
□ 1. TRACKING — Pixel/CAPI/Tag funcionando? Eventos disparando?
□ 2. LANDING PAGE — Carregando? Rápida? Checkout funcional?
□ 3. CONTA — Em review? Restrição? Policy violation?
□ 4. CREATIVE — CTR caindo? Frequency alta?
□ 5. AUDIENCE — Demographics mudaram? Público expandiu?
□ 6. BIDDING — Bid strategy mudou? Target alterado?
□ 7. BUDGET — Pacing normal? Spend concentrado?
□ 8. CONCORRÊNCIA — Novos players? Promoções de concorrentes?
□ 9. SAZONALIDADE — Período naturalmente mais fraco?
□ 10. PLATAFORMA — Instabilidade conhecida? Updates recentes?
```

Se nenhum dos 10 explica → investigação profunda com dados granulares.

---

## Contexto GB

| Parâmetro | Valor |
|---|---|
| ROAS mínimo (meta) | 10x |
| CPA máximo | ~R$100 |
| Ticket médio | R$100-300 |
| Margem bruta | ~70% |
| Meta Ads — status atual | 16 campanhas pausadas |
| Google Ads — status | Integração pendente (sem Developer Token) |

**Nota:** Com todas as campanhas pausadas em Mar/2026, esta skill será ativada quando campanhas retomarem. Enquanto isso, serve como referência para setup de monitoramento.

---

## Referências

- Meta Ads skill: `skills/marketing/meta-ads/SKILL.md`
- Google Ads skill: `skills/marketing/google-ads/SKILL.md`
- Budget optimizer: `skills/marketing/budget-optimizer/SKILL.md`
- Design system: `skills/design/report-design-system/SKILL.md`

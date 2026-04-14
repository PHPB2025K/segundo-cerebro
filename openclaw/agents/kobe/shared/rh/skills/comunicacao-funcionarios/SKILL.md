# SKILL — Comunicação Humanizada com Funcionários (Módulo C) — [[openclaw/agents/rh/IDENTITY|RH]]

## Objetivo

Definir o processo completo de comunicação semanal com funcionários da GB Importadora para alinhamento de irregularidades no ponto eletrônico. Cada interação deve ser humanizada, profissional e seguir um fluxo pré-definido até resolução.

## Ciclo de Comunicação

```
Segunda-feira 10h BRT
    │
    ├─ Cron "Monitor Ponto Semanal" executa
    │   ├─ Consulta Supabase: time_records da semana anterior (seg-sáb)
    │   ├─ Cruza com feriados, férias, licenças
    │   ├─ Classifica irregularidades por funcionário
    │   └─ Agrupa tudo por funcionário
    │
    ├─ Para cada funcionário COM pendências:
    │   ├─ Verifica severidade e histórico
    │   ├─ Compõe mensagem consolidada em chunks
    │   ├─ Envia via Evolution API (send-whatsapp.py)
    │   ├─ Registra no Supabase
    │   └─ Notifica Pedro no Telegram (thread 10)
    │
    └─ Gera relatório semanal consolidado no Telegram
```

**Funcionários sem pendências NÃO recebem mensagem.** Silêncio = tudo OK.

## Quando Usar Esta Skill

- **Segunda 10h**: Cron Monitor Ponto Semanal (uso primário)
- **Qualquer dia**: Quando funcionário responder mensagem via WhatsApp
- **Sob demanda**: Quando Pedro solicitar comunicação específica
- **NÃO usar**: Para enviar mensagens de ponto fora de segunda sem autorização do Pedro

## Janela de Comunicação

| Dia | Horário permitido | Uso |
|-----|-------------------|-----|
| Segunda | 10:00 BRT | Envio do alinhamento semanal |
| Seg-Sex | 08:00 — 18:00 BRT | Processamento de respostas dos funcionários |
| Sáb | 08:00 — 12:00 BRT | Processamento de respostas (se houver) |
| Dom e Feriados | BLOQUEADO | Nenhuma comunicação |

---

## FASE 1: Análise da Semana

### Coleta de Dados
O cron consulta o Supabase (time_records) para TODOS os funcionários, cobrindo segunda a sábado da semana anterior.

Query batch (otimização GPT-5.4 — uma query só):
```
SELECT * FROM time_records 
WHERE date BETWEEN '[segunda anterior]' AND '[sábado anterior]'
ORDER BY employee_id, date
```

### Classificação de Irregularidades

Para cada dia de cada funcionário, verificar:

```
TIPO A — Falta de marcação (1-3 batidas ausentes no dia)
TIPO B — Atraso (entrada após 07:10)
TIPO C — Saída antecipada (antes do horário sem justificativa prévia)
TIPO D — Falta completa (nenhuma marcação no dia, sem aviso)
TIPO E — Jornada incompleta (intervalo não registrado ou menor que 1h)
TIPO F — Padrão recorrente (3+ irregularidades na semana OU 2+ semanas consecutivas com pendências)
```

### Verificações Obrigatórias Antes de Classificar

1. **É feriado?** → Consultar calendário. Se sim, ignorar o dia.
2. **Funcionário está de férias/licença?** → Consultar people.md. Se sim, ignorar.
3. **É sábado e o funcionário não trabalha sábado?** → Verificar jornada. Se não trabalha, ignorar.
4. **Existe justificativa prévia?** → Funcionário avisou antes? Verificar WhatsApp recente.
5. **Já foi comunicado sobre essa semana?** → Verificar histórico. Se sim, aguardar resposta.

---

## FASE 2: Composição da Mensagem Semanal

### Regra de Ouro
UMA mensagem consolidada por funcionário. Todas as pendências da semana numa conversa fluida. NUNCA enviar mensagens separadas por dia.

### Estrutura por Volume de Pendências

**1 pendência (tom casual):**
```
[Chunk 1] Saudação + "alinhamento da semana passada"
[Chunk 2] "No geral ficou tudo certo" + menção à pendência
[Chunk 3] Pergunta sobre o que houve
[Chunk 4] Encerramento positivo
```

**2-3 pendências (tom profissional):**
```
[Chunk 1] Saudação + "alinhamento da semana passada"
[Chunk 2] "Achei algumas coisas pra gente acertar"
[Chunk 3] Pendência 1 — dia + descrição
[Chunk 4] Pendência 2 — dia + descrição
[Chunk 5] (Pendência 3 se houver)
[Chunk 6] Pedido de retorno
[Chunk 7] Encerramento
```

**4+ pendências ou TIPO F (tom firme, flag Pedro):**
```
[Chunk 1] Saudação
[Chunk 2] "Preciso alinhar com você algumas questões da semana"
[Chunk 3] Resumo dos atrasos (agrupados)
[Chunk 4] Outras pendências (batidas faltantes)
[Chunk 5] Reconhecimento de que imprevistos acontecem + pedido de contexto
[Chunk 6] Pedido de retorno por dia
[Chunk 7] "Fico no aguardo"
```

---

## Templates Detalhados por Tipo

### TIPO A — Falta de Marcação

**1ª ocorrência na semana (casual):**
```
Chunk 1: "Bom dia, [Nome]! Tudo bem? Passando do RH pra alinhar a semana passada."
Chunk 2: "No geral ficou tudo certo, só um detalhe. Na [dia da semana] ([DD/MM]) ficou faltando a marcação de [entrada/saída/intervalo]."
Chunk 3: "Pode ter sido o app ou esquecimento, acontece! Me conta o que houve que eu ajusto aqui 👍"
```

**Múltiplas faltas de marcação na semana:**
```
Chunk 1: "Bom dia, [Nome]! Tudo certo?"
Chunk 2: "Passando pra alinhar o ponto da semana passada. Ficaram faltando algumas marcações."
Chunk 3: "[Dia da semana] ([DD/MM]): faltou a marcação de [tipo]."
Chunk 4: "[Dia da semana] ([DD/MM]): faltou a marcação de [tipo]."
Chunk 5: "Consegue me dar um retorno sobre esses dias? Se for problema no app, me avisa que a gente vê uma solução."
```

### TIPO B — Atraso

**Atraso(s) leve(s) — até 20min:**
```
Chunk 1: "Bom dia, [Nome]!"
Chunk 2: "Só um alinhamento rápido sobre a semana passada."
Chunk 3: "Na [dia] ([DD/MM]) a entrada foi às [HH:MM], [X] minutinhos depois do horário."
Chunk 4: "Nada grave, só pra manter o registro certinho. Se tiver acontecido algo, me avisa que eu anoto."
```

**Atraso(s) significativo(s) — >30min:**
```
Chunk 1: "Bom dia, [Nome]. Tudo bem?"
Chunk 2: "Preciso alinhar com você sobre o ponto da semana passada."
Chunk 3: "Na [dia] ([DD/MM]) a entrada foi registrada às [HH:MM], com [X] minutos de diferença."
Chunk 4: "Aconteceu alguma coisa? Trânsito, consulta, imprevisto?"
Chunk 5: "Me conta pra eu registrar a justificativa."
```

**Múltiplos atrasos na semana (tom firme):**
```
Chunk 1: "Oi, [Nome]. Tudo certo?"
Chunk 2: "Preciso conversar sobre os horários da semana passada."
Chunk 3: "Foram [X] atrasos: [dia] às [HH:MM], [dia] às [HH:MM], [dia] às [HH:MM]."
Chunk 4: "Entendo que imprevistos acontecem, mas quando são vários na mesma semana, preciso entender o que está rolando."
Chunk 5: "Tem alguma situação que está dificultando chegar no horário? Mudança de rota, transporte?"
Chunk 6: "Me dá um retorno que a gente resolve."
```

### TIPO C — Saída Antecipada

```
Chunk 1: "Oi, [Nome]! Tudo certo?"
Chunk 2: "Vi que na [dia] ([DD/MM]) a saída foi às [HH:MM], [X] minutos antes do horário."
Chunk 3: "Teve algum motivo? Consulta, imprevisto, liberação?"
Chunk 4: "Me avisa pra eu registrar aqui."
```

### TIPO D — Falta Completa

**ATENÇÃO**: Tipo D detectado no compliance diário é escalado imediatamente para Pedro (Telegram). A mensagem abaixo só é enviada na segunda SE Pedro não tomou ação antes.

```
Chunk 1: "Oi, [Nome]. Tudo bem com você?"
Chunk 2: "Na semana passada, não encontrei marcação de ponto na [dia] ([DD/MM])."
Chunk 3: "Aconteceu alguma coisa? Fiquei preocupado."
Chunk 4: "Quando puder, me dá um retorno pra eu saber como registrar."
```

### TIPO E — Jornada Incompleta (Intervalo)

```
Chunk 1: "Oi, [Nome]! Tudo bem?"
Chunk 2: "Sobre a semana passada: na [dia] ([DD/MM]) a marcação de [início/fim do intervalo] não apareceu."
Chunk 3: "Você fez o intervalo normalmente? Às vezes é só o app que falha."
Chunk 4: "Me confirma o horário que eu ajusto."
```

### TIPO F — Padrão Recorrente

**2+ semanas consecutivas com pendências (requer aprovação Pedro):**

ANTES de enviar, notificar Pedro no Telegram:
```
⚠️ Padrão recorrente detectado — [Nome]
Semana anterior: [X] irregularidades ([lista])
Semana retrasada: [X] irregularidades ([lista])
[Semanas anteriores se houver]
Devo enviar mensagem de alinhamento? Aguardo seu OK.
```

Mensagem (SOMENTE após aprovação do Pedro):
```
Chunk 1: "Oi, [Nome]. Tudo bem?"
Chunk 2: "Preciso conversar com você sobre uma questão importante."
Chunk 3: "Nas últimas semanas, tenho notado que as pendências no ponto estão se repetindo."
Chunk 4: "Semana passada: [resumo]. Semana retrasada: [resumo]."
Chunk 5: "Não quero que isso vire um problema maior. Tem alguma coisa que a gente pode fazer pra resolver?"
Chunk 6: "Me dá um retorno quando puder. Fico no aguardo."
```

---

## Mensagem Combinada — Múltiplos Tipos

Quando um funcionário tem tipos diferentes na mesma semana (ex: 1 atraso + 1 falta de batida), combine numa única mensagem fluida:

```
Chunk 1: "Bom dia, [Nome]! Tudo certo?"
Chunk 2: "Passando pra alinhar o ponto da semana passada. Achei dois pontos pra gente acertar."
Chunk 3: "Na [dia] ([DD/MM]), a entrada foi às [HH:MM], um pouco depois do horário."
Chunk 4: "E na [dia] ([DD/MM]), ficou faltando a marcação de [tipo]."
Chunk 5: "Consegue me dar um retorno sobre esses dois dias? Assim eu fecho a semana certinha."
```

NÃO envie mensagens separadas. SEMPRE agrupe.

---

## Fluxo de Resposta do Funcionário

Quando o funcionário responder (qualquer dia da semana), processar imediatamente dentro da janela de comunicação.

### Respostas Aceitas Automaticamente

| Resposta do funcionário | Classificação | Ação |
|------------------------|---------------|------|
| "Esqueci de bater" | Operacional | Registrar, ajustar, responder positivamente |
| "App travou / deu erro" | Técnico | Registrar, ajustar, oferecer ajuda |
| "Fui no médico" / "Consulta" | Médico | Registrar, pedir atestado quando possível |
| "Emergência familiar" | Pessoal | Registrar, demonstrar empatia, sem pedir detalhes |
| "Trânsito" / "Chuva" (1ª vez) | Circunstancial | Registrar, aceitar |
| Confirma horário real ("saí às 16:30 mas não bateu") | Correção | Ajustar ponto, confirmar |

**Resposta modelo — justificativa aceita:**
```
Chunk 1: "Entendido, [Nome]! Sem problemas."
Chunk 2: "Já registrei aqui a justificativa. O ponto da semana fica ajustado."
Chunk 3: "Qualquer coisa, é só chamar aqui. Bom trabalho! 👊"
```

### Respostas que Requerem Aprovação do Pedro

| Resposta do funcionário | Classificação | Ação |
|------------------------|---------------|------|
| Não respondeu em 48h | Silêncio | Follow-up gentil |
| Não respondeu em 72h | Silêncio prolongado | Notificar Pedro |
| Resposta vaga ("não sei") | Indefinida | Pedir detalhes uma vez, depois escalar |
| Reclama da empresa/gestão | Conflito | NÃO responder sobre o tema, escalar Pedro |
| Problema pessoal grave | Sensível | Empatia, registrar, escalar Pedro urgente |
| Pede exceção de horário | Solicitação | Informar que vai verificar, escalar Pedro |
| Questiona política de ponto | Questionamento | Explicar brevemente, sem debate |

### Follow-up (48h sem resposta):
```
Chunk 1: "Oi, [Nome]! Passando aqui de novo."
Chunk 2: "Ainda preciso do seu retorno sobre o ponto da semana passada."
Chunk 3: "Quando puder me responder, agradeço! É rapidinho 🙏"
```

### Escalação (72h sem resposta):
```
[NÃO enviar nova mensagem ao funcionário]
[Telegram thread 10]:
"⚠️ [Nome] — sem resposta há 72h sobre ponto semana [DD/MM a DD/MM].
Pendências: [lista].
Mensagem enviada: [data]. Follow-up enviado: [data].
Aguardando orientação."
```

---

## Ajuda Técnica com App Ponto Certo

Se funcionário reportar problema com o app:

```
Chunk 1: "Entendi, [Nome]. Vou te ajudar."
Chunk 2: "Tenta assim:"
Chunk 3: "1. Fecha o app e abre de novo"
Chunk 4: "2. Verifica se GPS e internet estão ligados"
Chunk 5: "3. Se não der, tenta pelo navegador: [URL]"
Chunk 6: "Se continuar com erro, me manda um print que eu resolvo por aqui."
```

---

## Reconhecimento Positivo

Funcionário com 4+ semanas consecutivas sem nenhuma pendência:

```
Chunk 1: "Oi, [Nome]! Tudo bem?"
Chunk 2: "Só passando pra dar um toque positivo: seu ponto tá impecável, parabéns! 🎯"
Chunk 3: "Faz diferença quando todo mundo colabora. Valeu!"
```

Regra: enviar no máximo 1 vez por mês. Não enviar para todos de uma vez (espaçar entre segundas).

---

## Relatório Semanal (Telegram, thread 10)

Enviado após o processamento das mensagens na segunda 10h:

```
📋 Ponto Semanal — [DD/MM] a [DD/MM/YYYY]

👥 Funcionários ativos: [total]
📅 Dias úteis na semana: [X]

✅ Sem pendências: [X] funcionários
📩 Com pendências: [X] funcionários ([X] mensagens enviadas)

Detalhamento:
• [Nome]: [X] atraso(s), [X] batida(s) faltante(s) — severidade [low/medium/high]
• [Nome]: [X] atraso(s) — severidade [low]

⏳ Respostas pendentes de semanas anteriores: [X]
🔄 Resolvidos esta semana: [X]

🚨 Flags para atenção:
• [Nome] — padrão recorrente (2ª semana)
• [Nome] — falta sem aviso [dia] (já notificado no dia [data])

🏦 Banco de horas geral: [resumo — X positivos, X negativos, X zerados]
📈 Tendência: [melhorando/estável/piorando] vs semana anterior
```

---

## Registro no Supabase

Toda comunicação semanal deve ser registrada:

```json
{
  "employee_id": "uuid",
  "week_start": "2026-04-07",
  "week_end": "2026-04-12",
  "irregularities": [
    {"date": "2026-04-08", "type": "A", "detail": "falta clock_out"},
    {"date": "2026-04-10", "type": "B", "detail": "atraso 25min, entrada 07:25"}
  ],
  "message_sent_at": "2026-04-14T10:00:00-03:00",
  "message_chunks": ["chunk1", "chunk2", "..."],
  "severity": "low",
  "response_received_at": null,
  "response_text": null,
  "justification_status": "pending",
  "follow_up_sent": false,
  "resolved": false,
  "pedro_notified": false,
  "requires_pedro_approval": false,
  "notes": ""
}
```

---

## Limites de Automação

### O agente pode fazer sozinho:
- Analisar ponto da semana anterior e compor mensagens
- Enviar mensagens consolidadas na segunda-feira (até 3 irregularidades, sem padrão recorrente)
- Aceitar justificativas operacionais, técnicas e médicas
- Ajustar ponto quando funcionário confirma horário real
- Enviar follow-up de 48h
- Gerar relatórios semanais
- Enviar reconhecimento positivo (1x/mês)

### O agente PRECISA de aprovação do Pedro:
- TIPO F (padrão recorrente — 2+ semanas consecutivas)
- 4+ irregularidades na mesma semana
- TIPO D (falta completa sem aviso) — comunicação via WhatsApp
- Funcionário sem resposta há 72h
- Funcionário reporta conflito ou problema grave
- Qualquer ação que envolva desconto, advertência ou consequência
- Solicitações de exceção (horário flexível, jornada diferente)

---

## Otimizações GPT-5.4

- Ao analisar a semana, faça UMA query batch ao Supabase para todos os funcionários e todos os dias. NÃO faça query por dia ou por funcionário.
- Gere TODAS as mensagens (todos os funcionários) de uma vez como array de objetos, depois envie sequencialmente.
- Cache people.md no início da sessão.
- Para decisões de tom, siga a tabela ESTRITAMENTE. Não improvise.
- Ao compor mensagens combinadas (múltiplos tipos), priorize pela severidade: D > F > B > A > E > C.
- NUNCA copie um template literalmente. Adapte datas, nomes, horários, tipo.
- Varie saudações entre funcionários (rodízio: "Bom dia", "Oi", "E aí", "Fala") para não parecer copy-paste.

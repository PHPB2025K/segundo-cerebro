---
title: "2026-04-07-context-restore"
created: 2026-04-26
type: memory
agent: kobe
status: active
tags:
 - agent/kobe
 - memory
---
# Session: 2026-04-07 10:29:16 UTC

- **Session Key**: agent:main:telegram:group:-1003730816228:topic:13
- **Session ID**: c46a7658-1eb4-46e4-9189-10dba32b505c
- **Source**: telegram

## Conversation Summary

assistant: ✅ New session started · model: openai-codex/gpt-5.4
user: A new session was started via /new or /reset. Run your Session Startup sequence - read the required files before responding to the user. Then greet the user in your configured persona, if one is provided. Be yourself - use your defined voice, mannerisms, and mood. Keep it to 1-3 sentences and ask what they want to do. If the runtime model differs from default_model in the system prompt, mention the default model. Do not mention internal steps, files, tools, or reasoning.
Current time: Monday, April 6th, 2026 — 8:43 PM (UTC) / 2026-04-06 20:43 UTC

[Bootstrap truncation warning]
Some workspace bootstrap files were truncated before injection.
Treat Project Context as partial and read the relevant files directly if details seem missing.
- AGENTS.md: 20933 raw -> 18110 injected (~13% removed; max/file).
- If unintentional, raise agents.defaults.bootstrapMaxChars and/or agents.defaults.bootstrapTotalMaxChars.
assistant: [[reply_to_current]] Só um segundo, alinhando o contexto pra não responder no escuro.
assistant: [[reply_to_current]] Kobe na escuta. Tô alinhado no contexto recente e pronto pra tocar o que precisar — o que vamos resolver agora?
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4499",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:19 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Quero que você avalie e aplique um playbook para restaurar o contexto de um agente OpenClaw após troca de modelo.

Cenário:
Existe um agente que usa memória persistente + GitHub como segundo cérebro. Após trocar de modelo, ele passou a demonstrar perda de continuidade, menor aderência ao contexto e piora na execução.

Hipótese central:
O problema não é apenas o modelo. Pode haver desalinhamento entre:
- indexação atual
- retrieval semântico
- boot de contexto
- memória recente
- padrões de uso do novo modelo

Quero que você trabalhe com este playbook:

1. Reindexação forçada
Executar:
openclaw memory index --force

Objetivo:
- reprocessar todos os arquivos de memória
- recriar embeddings do zero
- recalibrar o espaço vetorial
- melhorar a coerência entre retrieval e o novo padrão de uso do modelo

2. Warm-up do agente
Depois da troca de modelo e da reindexação:
- conversar alguns minutos com o agente
- injetar contexto real
- relembrar projetos, decisões, preferências e tarefas atuais
- só depois começar tarefas críticas

Objetivo:
- criar contexto recente dominante
- fazer a memória recente pesar mais que o histórico antigo
- reduzir desalinhamento inicial

3. Revisão do boot
Verificar se o agente está lendo corretamente os arquivos-base no início da sessão.

4. Revisão do GitHub como fonte de verdade
Verificar se o fluxo está consistente:
- pull
- leitura de contexto relevante
- execução
- validação
- registro
- push

5. Revisão do flush antes da compactação
Verificar se decisões, lições, projetos, pendências e nota diária estão sendo salvos antes do contexto ser compactado.

Quero que você entregue:
- diagnóstico técnico claro
- explicação objetiva de por que a reindexação ajuda mesmo sem trocar embedding model
- explicação objetiva de por que o warm-up ajuda
- checklist de correção
- quick wins imediatos
- recomendações práticas para qualquer usuário que queira restaurar o contexto do próprio agente após trocar de modelo

Quero resposta prática, sem teoria desnecessária.
assistant: [[reply_to_current]] Vou validar isso no ambiente e aplicar o playbook de forma objetiva: reindexação, checagem do boot, fluxo de memória/GitHub e o que muda de verdade depois da troca de modelo.
assistant: [[reply_to_current]] Aplicando a parte operacional agora. Vou reindexar a memória, checar o que o OpenClaw está carregando no boot e validar onde o fluxo de contexto pode estar quebrando.
assistant: [[reply_to_current]] Achei um sinal importante: o runtime está acusando “no bootstrap files”. Se isso estiver valendo pro agente afetado, não é só perda semântica — é boot fraco mesmo. Vou fechar essa confirmação e te devolvo o diagnóstico já com o que corrige mais rápido.
assistant: [[reply_to_current]] ✅ Apliquei a parte que dá ganho imediato: a reindexação forçada foi concluída com sucesso em todos os agentes.

*Diagnóstico técnico claro*
- O problema muito provavelmente não é só “modelo pior”.
- O quadro é compatível com falha composta: boot fraco/parcial + retrieval desatualizado + memória recente sem dominância + GitHub não refletindo 100% do estado atual.
- Hoje há mudanças locais ainda não consolidadas; então, se o agente usa GitHub como segundo cérebro, esse cérebro pode estar atrasado.
- O sinal mais preocupante é o boot: quando o agente começa frio ou com contexto-base incompleto, a troca de modelo amplifica a perda de continuidade.
- Resumo: reindex ajuda bastante, mas *não salva sozinho* se o boot e o flush de memória estiverem frouxos.

*Por que a reindexação ajuda mesmo sem trocar o embedding model*
- Porque ela reconstrói o índice em cima do estado atual dos arquivos.
- Isso remove chunks obsoletos, incorpora mudanças recentes, reduz ruído de conteúdo velho e realinha a busca semântica com a memória atual.
- Também ajuda quando houve mudança de versão, chunking, organização dos arquivos ou padrão de consulta do novo modelo.
- Em português claro: não troca o cérebro; arruma a memória que o cérebro consulta.

*Por que o warm-up ajuda*
- Porque contexto recente pesa muito mais na execução do que muita gente imagina.
- Depois da troca de modelo, o agente ainda não “entrou no trilho” daquele ambiente.
- Uns minutos de conversa boa fazem projetos ativos, decisões permanentes, preferências e pendências virarem a camada dominante da sessão.
- Isso reduz dependência de retrieval antigo e diminui erro bobo logo no começo.

*Checklist de correção*
- Reindexar logo após troca de modelo.
- Abrir sessão nova e validar se o agente carrega identidade, contexto-base, memória recente e pendências.
- Fazer warm-up curto antes de qualquer tarefa crítica.
- Testar memória do agente com 3 perguntas: quem eu sou, quais são as prioridades atuais, o que está pendente.
- Validar o fluxo GitHub: pull, leitura do contexto relevante, execução, validação, registro, commit/push.
- Garantir flush antes da compactação: decisões, lições, projetos, pendências e nota diária salvos *antes* de resumir a sessão.
- Depois da compactação, reindexar de novo.
- Se houve mudança relevante nos arquivos-base, reiniciar o gateway.

*Quick wins imediatos*
- A reindexação já foi feita.
- Próximo passo mais valioso: abrir uma sessão limpa e fazer 5 minutos de warm-up antes de usar o agente em algo importante.
- Pedir um “recall test” curto antes da primeira tarefa crítica.
- Colocar o GitHub em dia ainda hoje; segundo cérebro atrasado é quase tão ruim quanto segundo cérebro inexistente.
- Se o agente continuar fraco mesmo após warm-up, o gargalo passa a ser boot/config de contexto, não o modelo.

*Recomendação prática pra qualquer usuário restaurar contexto após troca de modelo*
- Troque o modelo.
- Reindexe a memória.
- Abra sessão nova.
- Faça warm-up intencional com projetos, decisões, preferências e pendências atuais.
- Teste memória antes de pedir trabalho sério.
- Execute só tarefas médias primeiro.
- No fim, registre tudo antes da compactação.
- Compactou? Reindexe de novo.
- Mantenha GitHub sempre sincronizado.

Minha leitura final: o playbook está certo, mas eu reforçaria uma regra central — *troca de modelo sem reindex + warm-up + teste de recall é pedir para o agente parecer mais burro do que ele realmente está*.

Se quiser, eu transformo isso agora num SOP enxuto de 1 página pra você reaplicar sempre que trocar modelo.
user: [Queued messages while agent was busy]

---
Queued #1
Conversation info (untrusted metadata):
```json
{
  "message_id": "4504",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:23 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

# PRD — Playbook de Restauração de Contexto após Troca de Modelo no OpenClaw

## 1. Objetivo
Criar um processo simples, replicável e confiável para restaurar contexto, memória operacional e continuidade de agentes OpenClaw após troca de modelo.

## 2. Problema
Após trocar de modelo, alguns agentes passam a operar pior mesmo mantendo a mesma base de memória. Os sintomas mais comuns são:
- perda de continuidade
- piora na recuperação de contexto
- menor aderência a decisões e preferências já salvas
- respostas mais desalinhadas
- regressão em tarefas complexas

## 3. Hipótese central
O problema não é apenas o novo modelo. Existe um desalinhamento entre:
- o índice atual de memória
- o padrão de retrieval do novo modelo
- a memória recente da sessão
- o boot de contexto
- o fluxo de uso do GitHub como segundo cérebro

## 4. Tese operacional
Duas ações ajudam muito logo após a troca de modelo:

### 4.1 Reindexação forçada
Executar:
openclaw memory index --force

### 4.2 Warm-up do agente
Após a reindexação:
- conversar alguns minutos com o agente
- reapresentar projetos, decisões, tarefas e preferências atuais
- só depois iniciar tarefas críticas

## 5. Por que a reindexação forçada ajuda
Mesmo sem trocar explicitamente o embedding model, a reindexação ajuda porque:
- reprocessa todos os arquivos de memória
- recria embeddings do zero
- reorganiza o espaço vetorial
- recalibra relações de proximidade semântica
- melhora coerência entre busca e o novo padrão de uso do modelo

Em termos práticos:
O índice anterior pode não estar “errado”, mas pode estar mal calibrado para a forma como o novo modelo formula consultas, interpreta relevância e consome contexto.

## 6. Por que o warm-up ajuda
O warm-up ajuda porque cria um centro de gravidade novo de contexto recente.

Durante esse processo:
- o usuário injeta contexto real e atualizado
- o sistema grava memória recente
- o retrieval passa a priorizar esse contexto fresco
- o agente reduz dependência do histórico antigo mal recuperado

Em termos práticos:
- sem warm-up: modelo novo + memória antiga = mais desalinhamento
- com warm-up: modelo novo + memória recente = melhora rápida de aderência

## 7. Escopo
### Incluído
- reindexação forçada
- warm-up estruturado
- auditoria de boot
- auditoria de retrieval
- auditoria do uso do GitHub como fonte de verdade
- auditoria de flush antes da compactação
- recomendações replicáveis para outros usuários

### Não incluído
- fine-tuning do modelo
- mudanças no provider fora do OpenClaw
- alterações externas sem acesso disponível

## 8. Fluxo recomendado
### Etapa 1 — Reindexação
Rodar:
openclaw memory index --force

### Etapa 2 — Warm-up
Nos primeiros minutos após a troca:
- reapresentar contexto atual
- reforçar decisões importantes
- citar tarefas, projetos e preferências vivas
- evitar começar direto em tarefa crítica

### Etapa 3 — Revisão de boot
Garantir que o agente leia corretamente seus arquivos-base de identidade e contexto no início da sessão.

### Etapa 4 — Revisão do GitHub
Garantir fluxo:
- pull
- leitura do contexto relevante
- execução
- validação
- registro
- push

### Etapa 5 — Revisão de compactação
Garantir flush antes da compactação, salvando:
- decisões
- lições aprendidas
- projetos
- pendências
- nota diária
- índice, quando necessário

## 9. Entregáveis
- diagnóstico técnico claro
- explicação prática do papel da reindexação
- explicação prática do papel do warm-up
- checklist objetivo de correção
- quick wins imediatos
- recomendações replicáveis para outros agentes

## 10. Critérios de aceite
O playbook será considerado bem-sucedido se:
- o agente recuperar melhor o contexto após troca de modelo
- houver melhora perceptível na aderência a preferências e decisões já salvas
- o retrieval passar a encontrar memória relevante com mais consistência
- o usuário conseguir repetir o processo em outros agentes com resultado semelhante

---
Queued #2
Conversation info (untrusted metadata):
```json
{
  "message_id": "4505",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:23 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

## 11. Quick wins imediatos
- rodar openclaw memory index --force após troca de modelo
- fazer warm-up antes de tarefa crítica
- revisar boot dos arquivos-base
- reforçar o uso do GitHub como fonte de verdade
- reforçar flush antes da compactação

## 12. Riscos se não fizer
- agente continuar desalinhado mesmo com memória existente
- repetição de erros já resolvidos
- perda de confiança do usuário
- mais retrabalho
- pior replicabilidade em setups de alunos ou outros agentes

## 13. Instrução final para o agente executor
Quero que você use este playbook para diagnosticar, explicar e corrigir o problema de restauração de contexto após troca de modelo.
Se possível, implemente os ajustes práticos, não apenas explique.
assistant: [[reply_to_current]] Vou transformar isso em ação prática de verdade: validar se esse “boot fraco” é real ou só um status enganoso, e ajustar o que der sem mexer no que não precisa.
assistant: [[reply_to_current]] Vou deixar isso mais robusto no próprio ambiente: criar um bootstrap explícito pra sessões e registrar o playbook de troca de modelo como regra operacional.
assistant: [[reply_to_current]] Fechei os ajustes locais. Só vou confirmar uma coisa final: se a criação do bootstrap novo já aparece no estado do OpenClaw agora ou se isso só entra limpo no próximo ciclo/restart.
assistant: [[reply_to_current]] *Diagnóstico*
- O problema é composto: não era só modelo. Tinha sinal de boot insuficiente + risco de retrieval defasado + memória recente fraca + possível conflito entre workspace local e GitHub remoto.
- A evidência mais forte: o OpenClaw estava reportando ausência de bootstrap; depois do ajuste, passou a reportar bootstrap presente.
- Também há mudanças locais ainda não sincronizadas. Se o agente usa GitHub como segundo cérebro, isso pode criar duas verdades competindo.

*O que já apliquei*
- Reindexação forçada concluída em todos os agentes.
- Backup feito antes das mudanças.
- Criei um bootstrap explícito para sessões.
- Reforcei no startup o playbook pós-troca de modelo: reindexação, warm-up, teste de recall e cuidado extra antes de compactar.
- Registrei o PRD/playbook para reaplicar em outros agentes.

*Por que isso ajuda*
- *Reindexação*: não muda o embedding model, mas reconstrói o índice com o estado atual da memória, remove ruído velho e melhora a chance de o novo modelo encontrar o chunk certo.
- *Warm-up*: cria contexto recente dominante. Na prática, faz o agente “entrar no trilho” antes de encostar em tarefa crítica.

*Checklist de correção*
- Após trocar o modelo, reindexar a memória.
- Fazer 3–5 minutos de warm-up com projetos ativos, decisões fixas, preferências e pendências.
- Rodar um teste de recall curto antes de trabalho importante.
- Garantir disciplina do segundo cérebro: pull, leitura, execução, validação, registro, push.
- Antes de compactar, salvar decisões, lições, projetos, pendências e nota diária.
- Se a memória foi atualizada de forma material, reindexar de novo depois.

*Quick wins imediatos*
- Nunca começar tarefa crítica logo após troca de modelo.
- Sempre fazer um “teste de memória” primeiro: quem eu sou, projetos ativos, prioridades e pendências.
- Se o agente piorar mesmo após isso, olhar boot e GitHub antes de culpar o modelo.

*Recomendação prática pros alunos/outros usuários*
- Troca de modelo → reindexação → warm-up → teste de recall → só depois tarefa crítica.
- Se quiser um warm-up padrão, usa 4 blocos: contexto atual, decisões permanentes, pendências vivas e estilo/preferências.
- Sem esse ritual, o agente parece mais burro do que realmente está.

Se quiser, eu transformo isso agora numa versão ainda mais enxuta: “playbook de 5 minutos” pronto pra copiar e colar pros teus alunos.
assistant: Vou transformar isso em ação prática de verdade: validar se esse “boot fraco” é real ou só um status enganoso, e ajustar o que der sem mexer no que não precisa.
assistant: Vou deixar isso mais robusto no próprio ambiente: criar um bootstrap explícito pra sessões e registrar o playbook de troca de modelo como regra operacional.
assistant: Fechei os ajustes locais. Só vou confirmar uma coisa final: se a criação do bootstrap novo já aparece no estado do OpenClaw agora ou se isso só entra limpo no próximo ciclo/restart.
assistant: *Diagnóstico*
- O problema é composto: não era só modelo. Tinha sinal de boot insuficiente + risco de retrieval defasado + memória recente fraca + possível conflito entre workspace local e GitHub remoto.
- A evidência mais forte: o OpenClaw estava reportando ausência de bootstrap; depois do ajuste, passou a reportar bootstrap presente.
- Também há mudanças locais ainda não sincronizadas. Se o agente usa GitHub como segundo cérebro, isso pode criar duas verdades competindo.

*O que já apliquei*
- Reindexação forçada concluída em todos os agentes.
- Backup feito antes das mudanças.
- Criei um bootstrap explícito para sessões.
- Reforcei no startup o playbook pós-troca de modelo: reindexação, warm-up, teste de recall e cuidado extra antes de compactar.
- Registrei o PRD/playbook para reaplicar em outros agentes.

*Por que isso ajuda*
- *Reindexação*: não muda o embedding model, mas reconstrói o índice com o estado atual da memória, remove ruído velho e melhora a chance de o novo modelo encontrar o chunk certo.
- *Warm-up*: cria contexto recente dominante. Na prática, faz o agente “entrar no trilho” antes de encostar em tarefa crítica.

*Checklist de correção*
- Após trocar o modelo, reindexar a memória.
- Fazer 3–5 minutos de warm-up com projetos ativos, decisões fixas, preferências e pendências.
- Rodar um teste de recall curto antes de trabalho importante.
- Garantir disciplina do segundo cérebro: pull, leitura, execução, validação, registro, push.
- Antes de compactar, salvar decisões, lições, projetos, pendências e nota diária.
- Se a memória foi atualizada de forma material, reindexar de novo depois.

*Quick wins imediatos*
- Nunca começar tarefa crítica logo após troca de modelo.
- Sempre fazer um “teste de memória” primeiro: quem eu sou, projetos ativos, prioridades e pendências.
- Se o agente piorar mesmo após isso, olhar boot e GitHub antes de culpar o modelo.

*Recomendação prática pros alunos/outros usuários*
- Troca de modelo → reindexação → warm-up → teste de recall → só depois tarefa crítica.
- Se quiser um warm-up padrão, usa 4 blocos: contexto atual, decisões permanentes, pendências vivas e estilo/preferências.
- Sem esse ritual, o agente parece mais burro do que realmente está.

Se quiser, eu transformo isso agora numa versão ainda mais enxuta: “playbook de 5 minutos” pronto pra copiar e colar pros teus alunos.
assistant: [[reply_to_current]] Se a tua ideia é *sessão nova limpa*, é isso mesmo: usa */new*.

Pra esse caso de troca de modelo, o fluxo bom fica:
- */new*
- reindexação
- warm-up curto
- só depois tarefa crítica

Se quiser, eu já te deixo o ritual exato de 60 segundos pra rodar logo após o */new*.
user: [Queued messages while agent was busy]

---
Queued #1
System: [2026-04-06 21:24:13 UTC] Exec completed (kind-slu, code 0) :: ─────────────────────────────────┴────────┴─────────┴──────────────┴────────────────────────────────┘ FAQ: https://docs.openclaw.ai/faq Troubleshooting: https://docs.openclaw.ai/t…
System: [2026-04-06 21:24:16 UTC] Exec completed (good-rid, code 0) :: ed Warnings: - telegram default: Config allows unmentioned group messages (requireMention=false). Telegram Bot API privacy mode will block most group messages unless disabled. (In…

Conversation info (untrusted metadata):
```json
{
  "message_id": "4506",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:25 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Kobe?
assistant: [[reply_to_current]] Tô aqui. Fala.
assistant: Tô aqui. Fala.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4515",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:27 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

executou o prompt longo que eu te enviei?
assistant: [[reply_to_current]] Vou checar o histórico rápido pra te responder com precisão.
assistant: [[reply_to_current]] Sim.

Esse PRD entrou em fila enquanto eu ainda estava ocupado, e eu executei a linha principal dele. Não ficou só lido.

O que eu apliquei:
- reindexação forçada
- backup antes das mudanças
- bootstrap explícito pra sessão
- regra de pós-troca de modelo no boot
- playbook/PRD registrado no ambiente

Resumo: executei, sim. Se quiser, eu te separo agora o que já está valendo imediatamente e o que só fica 100% limpo na próxima sessão.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4518",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:31 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

veja a continuação do que deve ser feito + os arquivos do kit mencionado, na sequencia

Arquitetura: Claude Code + OpenClaw

Local (seu Mac):
○ Claude Code rodando no terminal
○ Clone do repositório em ~/segundo-cerebro/amora-cos
○ Skills em ~/.claude/skills/ (/cerebro, /rotina, /salve)
○ Hook de SessionStart: toda vez que abre o Claude Code, roda git pull automaticamente
VPS (OpenClaw):
○ Servidor Linux com acesso via ssh openclaw (usando Tailscale para VPN)
○ Mesmo repositório clonado em /root/.openclaw/workspace-amora-cos/
○ Amora rodando de forma autônoma com ~60 crons agendados
○ Integrações ativas: Telegram, Slack, Gmail, Buffer, Stripe, Supabase
○ 1Password CLI para credenciais
A ponte:
○ Repositório privado no GitHub (okjpg/repo-amora-cos)
○ Ambos os lados puxam e empurram para o mesmo repo
○ Local: git pull no boot + git push no /salve
○ VPS: cron a cada 30min fazendo git add . && git commit && git push
Como o sync funciona na prática
Bruno abre Claude Code
→ brain-boot.sh roda
→ git pull (pega o que Amora fez no VPS)
→ contexto carregado
Bruno trabalha, toma decisões, atualiza arquivos
Bruno roda /salve
→ arquivos atualizados
→ git push
→ VPS vai puxar na próxima rodada do cron
Enquanto isso no VPS, Amora:
→ executa crons (analytics, reports, content ops)
→ escreve memory/sessions/YYYY-MM-DD.md
→ faz push a cada 30min
Os arquivos são a memória compartilhada. Nenhum dos dois lados "envia mensagem" para o outro — a comunicação é via Git.
O que roda onde

Como montar do zero

Passo 1 — Criar o repositório
Repo privado no GitHub. Estrutura: memory/, skills/, scripts/, content/.
(mesma que ensino no mini-curso)

Passo 2 — Configurar o local
Clone o repo em ~/segundo-cerebro. Configure SECOND_BRAIN_PATH. 
Instale as skills. Configure o hook SessionStart com brain-boot.sh. 

Isso está coberto no kit que criamos.
LINK:[https://drive.google.com/drive/folders/1zZaLyBSrqj7MKNK0Cm4YdaRtHuZd0JNX?usp=sharing](https://drive.google.com/drive/folders/1zZaLyBSrqj7MKNK0Cm4YdaRtHuZd0JNX?usp=sharing)

Passo 3 — Provisionar o VPS
Servidor Linux (DigitalOcean, Hetzner, qualquer um). 
Instale Claude Code CLI, Node.js, Python, Git, 1Password CLI. 
Configure Tailscale para acesso seguro via ssh seuservidor.

Passo 4 — Clonar o repo no VPS
git clone[ https://github.com/SEU_USUARIO/SEU_REPO.git](https://github.com/SEU_USUARIO/SEU_REPO.git) /root/workspace

Passo 5 — Configurar o agente autônomo no VPS
Crie o SOUL.md (identidade do agente), CLAUDE.md (contexto), e os primeiros skills. 
Configure crons via crontab -e — cada cron chama um skill via Claude Code CLI:
0 9 * * 1-5 claude --no-interactive "execute /skill-name" >> /var/log/agent.log 2>&1

Passo 6 — Configurar o sync bidirecional
Cron no VPS a cada 30min:
*/30 * * * * cd /root/workspace && git pull --rebase && git add . && git commit -m "sync: auto" && git push

Passo 7 — Conectar integrações no VPS
Gmail via OAuth, Slack via webhook, Telegram via bot token — todas as credenciais via 1Password CLI (op read "op://Vault/Item/field").

O que torna esse setup poderoso
Você tem dois "modos" de uso:
Interativo (local): você fala com o Claude Code diretamente, toma decisões, gera conteúdo, faz análises. O contexto está todo ali.

Autônomo (VPS): enquanto você dorme, o agente roda crons, envia relatórios, processa dados, mantém o segundo cérebro atualizado. Na manhã seguinte você abre
o Claude Code e o git pull traz tudo que o agente fez.

A chave é que o Git é o protocolo de comunicação entre os dois. Não tem API entre eles, não tem fila de mensagens — só arquivos commitados. Simples e
resiliente.
assistant: [[reply_to_current]] Vou olhar duas coisas em sequência: a continuação do teu texto e o conteúdo acessível desse kit pra mapear o que ainda falta.
assistant: [[reply_to_current]] O link do Drive não abriu direto por fetch. Vou procurar o kit pelo que já ficou registrado aqui e pelos nomes/arquivos associados.
assistant: [[reply_to_current]] Achei o texto-base no histórico. Agora vou tentar mapear o kit pelo Drive por outro caminho e, se não vier, te devolvo a sequência do que falta de forma fechada mesmo sem o índice do Drive.
assistant: [[reply_to_current]] Vi a continuação. A ordem certa do que ainda falta fechar é essa: 1) contrato de sync sem gambiarra — local faz pull no boot e push só no /salve; VPS faz pull com rebase antes de escrever, usa trava pra não rodar duas vezes e só faz commit se houve mudança; 2) bootstrap dos dois lados — identidade, contexto, pendências e sessão recente carregados sempre; 3) skillset local fechado — /cerebro, /rotina e /salve com papéis bem separados; 4) runner autônomo no VPS — crons, logs, restart, healthcheck e backup; 5) só depois plugar Gmail, Slack, Telegram, Buffer, Stripe e Supabase. O ponto crítico aqui é o sync: push cego no VPS a cada 30 min é pedir conflito. Tem que ser pull + rebase + lock + commit condicional.

Do kit mencionado, pelo teu texto, os arquivos centrais na sequência são estes: README de começo rápido; brain-boot.sh; exemplo do hook SessionStart; skill /cerebro; skill /rotina; skill /salve; template de SOUL.md; template de CLAUDE.md; estrutura-base de memory; script de sync do VPS; exemplo de crontab; guia de 1Password; guia de Tailscale/SSH; exemplos de integrações; e um arquivo de convenções operacionais dizendo quem escreve o quê, quando faz flush de memória e quando faz push. Se faltar qualquer um desses, o kit fica “bonito”, mas não fica replicável.

Não consegui listar o conteúdo exato do Drive daqui porque o índice da pasta não abriu por fetch. Então, honestamente: eu tenho a arquitetura e consigo te fechar o kit ideal, mas não consigo ainda confirmar 1:1 os nomes reais que estão lá dentro. Se você mandar print da pasta ou export da lista de arquivos, eu te devolvo na sequência: “arquivo por arquivo, o que existe, o que falta e o que precisa corrigir”.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4519",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:31 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

Dúvidas
- Bruno, não entendi nada. Por onde começar? Fique tranquilo. Basta jogar para seu agente esse texto + KIT no Google drive
- Bruno, qual o benefício de fazer isso? Você pode continuar usando o Claude para trabalhar no computador e usar o Openclaw (no meu caso uso com ChatGPT) para trabalhar também. São 2 LLM’s que se complementam.
- Bruno, qual o nível de dificuldade para montar esse segundo cérebro? Médio/avançado. Se você está iniciando esta jornada, não recomendo este caminho.
- Bruno, só funciona com o github ou da para usar outra ferramenta (ex: obsidian): Da para usar com outras ferramentas, mas eu recomendo muito o github.
assistant: [[reply_to_current]] Eu deixaria esse bloco assim, mais claro e mais forte:

- *Bruno, não entendi nada. Por onde começar?*  
Começa pelo texto-base + o kit. Entrega os dois para o agente e pede a montagem na ordem certa: ambiente local, repositório, VPS, sync e integrações. Você não precisa entender a arquitetura inteira antes de começar.

- *Bruno, qual o benefício de fazer isso?*  
Você passa a ter dois modos de operação ao mesmo tempo: um agente trabalhando com você no computador e outro rodando de forma autônoma no servidor. Um ajuda na execução ao vivo; o outro toca rotina, memória, relatórios e tarefas recorrentes.

- *Bruno, qual o nível de dificuldade para montar esse segundo cérebro?*  
Médio para avançado. Se você ainda está começando com terminal, Git, VPS e integrações, eu não recomendo começar por aqui.

- *Bruno, só funciona com GitHub ou dá para usar outra ferramenta, como Obsidian?*  
Dá para adaptar a outras ferramentas, mas eu recomendo fortemente GitHub. Se quiser usar Obsidian, ótimo — mas como interface. Como protocolo de sync, versionamento e histórico, Git continua sendo a melhor base.

Se quiser, eu pego agora esse FAQ inteiro e reescrevo no teu tom, já em versão final de página de vendas/aula.
user: [media attached: 3 files]
[media attached 1/3: /root/.openclaw/media/inbound/README---57d5a428-2d87-4825-99c8-409e5cc9b321.md (text/markdown) | /root/.openclaw/media/inbound/README---57d5a428-2d87-4825-99c8-409e5cc9b321.md]
[media attached 2/3: /root/.openclaw/media/inbound/skills---fe451624-7d5c-48cb-8bce-e2da2e55e507.zip (application/zip) | /root/.openclaw/media/inbound/skills---fe451624-7d5c-48cb-8bce-e2da2e55e507.zip]
[media attached 3/3: /root/.openclaw/media/inbound/templates---d83b9435-869a-4bc1-b3cd-b3bec2f0f5b7.zip (application/zip) | /root/.openclaw/media/inbound/templates---d83b9435-869a-4bc1-b3cd-b3bec2f0f5b7.zip]
To send an image back, prefer the message tool (media/path/filePath). If you must inline, use MEDIA:https://example.com/image.jpg (spaces ok, quote if needed) or a safe relative path like MEDIA:./image.jpg. Avoid absolute paths (MEDIA:/...) and ~ paths — they are blocked for security. Keep caption in the text body.
Conversation info (untrusted metadata):
```json
{
  "message_id": "4520",
  "sender_id": "5510943376",
  "conversation_label": "Kobe Hub id:-1003730816228 topic:13",
  "sender": "Pedro",
  "timestamp": "Mon 2026-04-06 21:31 UTC",
  "group_subject": "Kobe Hub",
  "topic_id": "13",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Pedro (5510943376)",
  "id": "5510943376",
  "name": "Pedro"
}
```

[Telegram Kobe Hub id:-1003730816228 topic:13 Mon 2026-04-06 21:31 UTC] Pedro (5510943376): <media:document>

<file name="README---57d5a428-2d87-4825-99c8-409e5cc9b321.md" mime="text/markdown">
# Segundo Cérebro para Claude Code
### Sistema /cerebro + /rotina + /salve

> Um repositório (ou pasta local) que funciona como memória persistente do Claude Code. 
> Três skills que transformam qualquer sessão em trabalho acumulativo.

---

## O que é esse sistema

O problema padrão com o Claude Code: cada sessão começa do zero. Você re-explica contexto, re-toma decisões, perde o fio da meada.

Esse sistema resolve isso com três skills:

| Skill | Quando usar | O que faz |
|-------|-------------|-----------|
| `/cerebro` | Início de sessão | Carrega todo o contexto (pendências, projetos, decisões recentes, últimas sessões) |
| `/rotina` | Manhã | Cockpit do dia: emails, agenda, tarefas, métricas — tudo em uma tela |
| `/salve` | Fim de sessão | Flush: salva decisões, pendências, projetos, cria log, faz commit/push |

**O loop:** `/cerebro` → trabalha → `/salve` → amanhã `/cerebro` já sabe tudo que aconteceu.

---

## Você já tem notas organizadas em algum lugar?

Não precisa construir do zero. Existem dois caminhos:

### Caminho A — Tenho arquivos/notas (Notion export, Obsidian, pasta com markdowns...)

1. Coloque sua pasta onde está
2. Configure `SECOND_BRAIN_PATH` apontando para ela
3. Instale as skills
4. Rode `/cerebro` — ele vai **mapear o que existe**, identificar o que está faltando e criar só os arquivos ausentes, sem tocar no que você já tem

### Caminho B — Começo do zero

Siga o passo a passo completo abaixo.

Em ambos os casos, o sistema funciona com o que tiver. Ele usa os arquivos que encontrar e ignora o que não existe.

---

## Pré-requisitos

### Claude Code
Baixe e instale em [claude.ai/download](https://claude.ai/download).

> Se preferir instalar via terminal, você precisa do **Node.js** (baixe em [nodejs.org](https://nodejs.org)) e depois rode:
> ```bash
> npm install -g @anthropic-ai/claude-code
> ```

### Git
Verifique se já tem instalado abrindo o terminal e rodando `git --version`. Se não tiver, baixe em [git-scm.com](https://git-scm.com).

### Conta no GitHub (opcional, mas recomendado)
Para backup e sincronização entre máquinas. Crie gratuitamente em [github.com](https://github.com). 
Sem GitHub, o sistema funciona 100% local — você só não tem backup automático.

---

## Instalação

> **Mac/Linux:** use o Terminal. 
> **Windows:** use o PowerShell (comandos alternativos indicados abaixo) ou instale o WSL (recomendado para acesso completo).

---

### Passo 1 — Criar a pasta do segundo cérebro

**Mac/Linux:**
```bash
mkdir -p ~/segundo-cerebro/memory/context/decisoes
mkdir -p ~/segundo-cerebro/memory/projects
mkdir -p ~/segundo-cerebro/memory/sessions
mkdir -p ~/segundo-cerebro/scripts
touch ~/segundo-cerebro/memory/sessions/.gitkeep
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force "$HOME\segundo-cerebro\memory\context\decisoes"
New-Item -ItemType Directory -Force "$HOME\segundo-cerebro\memory\projects"
New-Item -ItemType Directory -Force "$HOME\segundo-cerebro\memory\sessions"
New-Item -ItemType Directory -Force "$HOME\segundo-cerebro\scripts"
New-Item -ItemType File "$HOME\segundo-cerebro\memory\sessions\.gitkeep"
```

> **Já tem uma pasta com notas?** Pule este passo e use a pasta que já tem no próximo.

---

### Passo 2 — Copiar os templates

Vá até a pasta deste kit (onde você descompactou):

**Mac/Linux:**
```bash
cd ~/Downloads/segundo-cerebro-kit
cp -r templates/* ~/segundo-cerebro/
```

**Windows (PowerShell):**
```powershell
cd "$HOME\Downloads\segundo-cerebro-kit"
Copy-Item -Recurse templates\* "$HOME\segundo-cerebro\"
```

> **Já tem notas:** copie apenas os arquivos que você não tiver. O `/cerebro` vai identificar o que está faltando quando você rodar pela primeira vez.

---

### Passo 3 — Preencher seus dados

Abra a pasta `~/segundo-cerebro` no seu editor (VS Code, Notion, qualquer editor de texto) e edite:

- **`CLAUDE.md`** — o mais importante. Substitua `[SEU NOME]` e preencha seus projetos, equipe e contexto geral. O Claude usa isso em todas as sessões.
- **`memory/context/business-context.md`** — visão geral dos seus negócios ou projetos
- **`memory/context/people.md`** — equipe e contatos relevantes

Os outros arquivos você preenche conforme usa. Pode deixar com os placeholders por enquanto — o sistema funciona com arquivos vazios.

---

### Passo 4 — Configurar a variável de ambiente

Isso diz ao Claude onde está seu segundo cérebro.

**Mac/Linux:** Abra `~/.zshrc` (no Mac) ou `~/.bashrc` (no Linux/bash) em qualquer editor e adicione no final:
```bash
export SECOND_BRAIN_PATH="$HOME/segundo-cerebro"
```
Depois aplique: `source ~/.zshrc`

> Não sabe qual shell usa? Rode `echo $SHELL`. Se mostrar `/bin/zsh`, edite `.zshrc`. Se mostrar `/bin/bash`, edite `.bashrc`.

**Windows (PowerShell):**
```powershell
# Variável permanente (persiste após reiniciar)
[System.Environment]::SetEnvironmentVariable("SECOND_BRAIN_PATH", "$HOME\segundo-cerebro", "User")
```
Feche e reabra o PowerShell para ativar.

> **Pasta diferente?** Substitua `$HOME/segundo-cerebro` pelo caminho real da sua pasta. 
> Para descobrir o caminho: **Mac/Linux:** `echo $HOME` | **Windows:** `echo $HOME` ou `$env:USERPROFILE`

---

### Passo 5 — Instalar as skills

**Mac/Linux:**
```bash
mkdir -p ~/.claude/skills/cerebro ~/.claude/skills/rotina ~/.claude/skills/salve

# (ainda dentro da pasta segundo-cerebro-kit)
cp skills/cerebro/SKILL.md ~/.claude/skills/cerebro/
cp skills/rotina/SKILL.md ~/.claude/skills/rotina/
cp skills/salve/SKILL.md ~/.claude/skills/salve/
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\cerebro"
New-Item -ItemType Directory -Force "$HOME\.claude\skills\rotina"
New-Item -ItemType Directory -Force "$HOME\.claude\skills\salve"

Copy-Item skills\cerebro\SKILL.md "$HOME\.claude\skills\cerebro\"
Copy-Item skills\rotina\SKILL.md "$HOME\.claude\skills\rotina\"
Copy-Item skills\salve\SKILL.md "$HOME\.claude\skills\salve\"
```

---

### Passo 6 — Configurar o Git (opcional, para backup e sync)

Se quiser backup no GitHub:

```bash
cd ~/segundo-cerebro
git init
git add .
git commit -m "setup: estrutura inicial do segundo cérebro"
```

Crie um repositório privado em [github.com/new](https://github.com/new) e conecte:
```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git push -u origin main
```

Sem isso, o `/salve` ainda funciona — só não faz push para o remoto.

---

### Passo 7 — Testar

Abra o Claude Code e digite:
```
/cerebro
```

Na primeira vez, ele vai:
1. Detectar o que já existe na sua pasta
2. Listar o que está faltando
3. Perguntar se quer criar os arquivos ausentes
4. Configurar o hook de boot automático (opcional)

---

## Como usar no dia a dia

### Início de sessão
```
/cerebro
```
Carrega todo o contexto. Você vê o estado atual do seu segundo cérebro em segundos.

Para ver detalhes, diga:
- `mostra pendências` → lista completa
- `mostra projetos` → status de todos os projetos
- `mostra deadlines` → prazos próximos
- `mostra [nome do projeto]` → detalhes de um projeto

### Manhã
```
/rotina
```
Cockpit completo: emails, agenda, tarefas, métricas. Define o Top 3 do dia, bloqueia no calendar se quiser.

### Fim de sessão
```
/salve
```
Salva tudo que mudou, cria log da sessão, faz commit e push (se tiver Git configurado).

---

## Estrutura do segundo cérebro

Os arquivos que o sistema usa (todos opcionais — use só os que fizerem sentido pra você):

```
segundo-cerebro/
├── CLAUDE.md # Quem você é — Claude lê em todo projeto
├── PROPAGATION.md # O que atualizar quando algo muda
├── scripts/
│ └── brain-boot.sh # Script de sync automático ao abrir Claude
└── memory/
 ├── context/
 │ ├── pendencias.md # Tudo em aberto (🔴 crítico, 🟡 importante)
 │ ├── deadlines.md # Prazos
 │ ├── business-context.md # Visão geral dos seus projetos/negócios
 │ ├── people.md # Equipe e contatos
 │ └── decisoes/
 │ └── YYYY-MM.md # Decisões do mês
 ├── projects/
 │ ├── _index.md # Status de todos os projetos
 │ └── {nome-projeto}.md # 1 arquivo por projeto (criado pelo /salve)
 └── sessions/
 └── YYYY-MM-DD.md # Log de cada sessão (criado pelo /salve)
```

**Mínimo para funcionar:** qualquer pasta com `SECOND_BRAIN_PATH` apontando pra ela. O resto vai sendo criado conforme você usa.

---

## Personalizando o /rotina

Edite `~/.claude/skills/rotina/SKILL.md` e localize as marcações `[CONFIGURAR]`:

- **Fuso horário** — padrão `America/Sao_Paulo`; troque pelo seu (ex: `America/Bogota`, `Europe/Lisbon`)
- **Métricas** — adicione queries para seus negócios (SaaS, e-commerce, planilhas...)
- **Tasks no Notion** — configure os IDs das suas databases
- **Metas de conteúdo** — ajuste plataformas e frequências

---

## Configurando MCPs (para /rotina completo)

MCPs são integrações que permitem ao Claude acessar serviços externos. São opcionais.

Todas as configurações vão em `~/.mcp.json`. Se não existir, crie o arquivo.

> **Dica:** Não sabe configurar? Abra o Claude Code e peça: *"me ajuda a configurar o MCP do Gmail"*. Ele te guia passo a passo.

### Gmail
Repositório: [github.com/GongRzhe/Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)

### Google Calendar
Repositório: [github.com/nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)

### Notion
Repositório oficial: [github.com/makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)

### Como adicionar ao ~/.mcp.json

Exemplo de estrutura (adicione os servidores que quiser):
```json
{
 "mcpServers": {
 "gmail": { ... },
 "google-calendar": { ... },
 "notion": { ... }
 }
}
```

Cada repositório tem as instruções de configuração específicas.

---

## Dúvidas frequentes

**P: Não tenho negócio. Funciona para outras áreas?** 
R: Sim. Use `business-context.md` para qualquer contexto: carreira, estudos, projetos pessoais, pesquisa. A estrutura é a mesma.

**P: Já tenho notas no Notion / Obsidian. Preciso migrar tudo?** 
R: Não. Você pode exportar o que quiser para markdown e colocar na pasta, ou simplesmente criar os arquivos-chave (pendencias.md, business-context.md) do zero com o resumo do que já tem. O `/cerebro` vai mapear o que existe e sugerir o que falta.

**P: Precisa de GitHub?** 
R: Não. O sistema funciona local. GitHub só adiciona backup e sync entre máquinas.

**P: O /rotina funciona sem MCPs?** 
R: Sim. Sem Gmail: seção de email indisponível. Sem Calendar: agenda indisponível. Pendências, projetos e deadlines sempre funcionam.

**P: Como o Claude "lembra" entre sessões?** 
R: Não é memória do modelo — é o Git (ou sua pasta local). Cada sessão lê os arquivos que o `/salve` da sessão anterior atualizou.

**P: Estou no Windows. Funciona?** 
R: Funciona para os passos de configuração via PowerShell (comandos listados acima). O script `brain-boot.sh` de sync automático **requer WSL** (Windows Subsystem for Linux) para rodar — sem ele, você apenas não terá o git pull automático ao abrir o Claude, mas tudo mais funciona. 
Para instalar WSL: abra o PowerShell como administrador e rode `wsl --install`, reinicie, e siga os passos normalmente dentro do Ubuntu instalado.

**P: O fuso horário do /rotina está errado.** 
R: Edite `~/.claude/skills/rotina/SKILL.md` e substitua `America/Sao_Paulo` pelo seu fuso. Lista completa: [wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

**P: Posso ter mais de um segundo cérebro?** 
R: Sim. Mude `SECOND_BRAIN_PATH` para outra pasta. Útil para separar contextos (trabalho / pessoal).

---

## Próximos passos

1. Rode `/cerebro` — ele mapeia o que existe e configura o que falta
2. Preencha o `CLAUDE.md` com seus dados reais (é o arquivo mais importante)
3. Faça uma sessão de trabalho normal com o Claude
4. Rode `/salve` no final
5. Abra uma nova sessão e rode `/cerebro` — o contexto vai estar lá

---

*Sistema criado por Bruno Okamoto. Inspirado no conceito de "segundo cérebro" do Tiago Forte, adaptado para Claude Code.*
</file>
assistant: [[reply_to_current]] Agora sim. Vou abrir o README e destrinchar o conteúdo dos dois zips pra te dizer exatamente: o que o kit já resolve, o que está faltando e o que eu corrigiria.
assistant: [[reply_to_current]] Extraí o kit. Vou ler os 3 skills e os templates-chave pra te devolver um diagnóstico fechado, não chute.
assistant: [[reply_to_current]] Falta só conferir a qualidade dos templates de memória. Aí eu te digo com segurança se esse kit está “vendável” ou se ainda está cru.
assistant: [[reply_to_current]] Agora ficou claro.

*Leitura honesta do kit:* ele está **bom como kit de segundo cérebro para Claude Code local**. O README está bem didático, os 3 comandos têm lógica clara e os templates estão organizados. O que veio de fato no pacote foi:
- 3 skills: *cerebro*, *rotina*, *salve*
- templates de contexto: pendências, deadlines, business context, people, decisões
- índice de projetos
- `CLAUDE.md`
- `PROPAGATION.md`
- `brain-boot.sh`

*O ponto importante:* esse kit **não entrega ainda a arquitetura Claude Code + OpenClaw que você descreveu antes**. Ele entrega bem a camada local. O pedaço VPS/autônomo não veio aqui. Estão faltando justamente os arquivos mais críticos dessa segunda metade:
- guia e estrutura do lado OpenClaw/VPS
- script de sync seguro no servidor
- padrão de cron/automações
- contrato de “quem escreve o quê” entre local e VPS
- healthcheck / logs / rollback
- setup de integrações e credenciais
- documentação da arquitetura Git como barramento entre os dois lados

*Minha conclusão:* como produto, ele está **coerente**, mas hoje vende uma promessa maior do que o conteúdo realmente entregue. Se você posicionar como “kit local para Claude Code com memória persistente”, está bom. Se quiser vender como “Claude Code + OpenClaw + segundo cérebro autônomo”, ainda falta o *módulo VPS*. E eu corrigiria mais 3 coisas:
- o `brain-boot.sh` hoje despeja pendências + última sessão inteira; isso pode inflar contexto demais
- o `/salve` está otimista demais com Git e branch remota; precisa fallback melhor
- o README precisa separar claramente *modo básico (local)* de *modo avançado (local + VPS + OpenClaw)*

Se quiser, eu faço agora o próximo passo útil: te entrego uma lista exata de *arquivos que faltam criar* pra esse kit realmente fechar a promessa “Claude Code + OpenClaw”.

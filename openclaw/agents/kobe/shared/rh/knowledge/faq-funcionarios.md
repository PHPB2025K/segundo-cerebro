---
title: "FAQ Funcionários"
created: 2026-04-30
type: knowledge
agent: kobe
domain: rh
status: active
tags:
  - agent/kobe
  - rh
  - faq
  - knowledge
---

# FAQ — Atendimento a Funcionários (Agente RH)

> **Documento canônico de respostas.** Este é o ÚNICO arquivo que o agente RH deve usar
> pra responder perguntas espontâneas dos funcionários. Se a resposta não está aqui
> nem em `regras-ponto-certo.md` ou `jornadas-individuais.md` ou `politica-sabado-trabalhado.md`,
> o agente DEVE responder "Não tenho essa informação aqui comigo no momento" e escalar.
>
> **Tom:** profissional, claro, cordial, com formatação WhatsApp (negrito `*texto*`,
> itálico `_texto_`). Respostas curtas (3-5 linhas idealmente).

---

## 🔐 ACESSO AO SISTEMA

### "Como acesso o Ponto Certo?"
**Resposta:**
```
O sistema é acessado pelo link:
🔗 https://ponto.budamix.com.br

Você loga com seu *email cadastrado* e a senha que você configurou.
Funciona pelo celular (Android/iOS) ou navegador.
```

### "Esqueci minha senha"
**Resposta:**
```
Sem problemas! Pra resetar:

1. Vai em https://ponto.budamix.com.br/login
2. Clica em *"Esqueceu a senha?"*
3. Coloca seu email e clica em enviar
4. Você vai receber um link no email pra criar uma nova senha

O link vale por 24h. Se não chegar, confere o spam ou me chama aqui.
```

### "Não chegou o email de reset"
**Resposta:**
```
Olha duas coisas:
• Pasta de *spam* ou *promoções* do seu email
• Confirma se o email está certo (deve ser o mesmo que cadastramos)

Se mesmo assim não chegar, me confirma aqui qual email você usa que eu reseto manualmente.
```

### "Qual é meu login?"
**Ação técnica:** consultar `profiles.email WHERE id = <user_id>` no Supabase.
**Resposta:**
```
Seu login é: *<email>*
```

### "Primeiro acesso, qual é a senha?"
**Resposta (caso tenha sido cadastrado recentemente):**
```
Quando você foi cadastrado, te enviamos uma senha provisória aqui no WhatsApp.
Se não localizar, me chama que eu reseto pra uma nova provisória.

No primeiro login, o sistema vai pedir pra você definir uma senha sua (mínimo 6 caracteres).
```

---

## 📱 APP E GPS

### "O app travou / não abre"
**Resposta:**
```
Tenta nessa ordem:
1. Fecha o navegador completamente e abre de novo
2. Se ainda travar, limpa o cache do navegador
3. Verifica se o GPS e a internet estão ligados
4. Confirma que você deu permissão de localização pro site

Se continuar com problema, me manda um print da tela que eu te ajudo.
```

### "GPS não pega / diz que estou fora do escritório"
**Resposta:**
```
A validação de GPS exige que você esteja no escritório (raio de 50m).

Verifica:
• GPS ligado no celular
• Permissão de localização habilitada pro navegador/site
• Internet funcionando

Se você *está* no escritório e mesmo assim dá erro, me chama que eu vejo no sistema o que tá pegando.
```

### "Bati o ponto mas não apareceu na lista"
**Ação técnica:** consultar `time_records WHERE user_id = ... AND recorded_at >= today`.
**Resposta (se confirmar que existe):**
```
Conferi aqui e a marcação foi registrada sim! Às *<HH:MM>*.
Às vezes a tela demora alguns segundos pra atualizar — tenta dar refresh.
```

**Resposta (se não existir):**
```
Conferi aqui e essa marcação não chegou no sistema. Pode ter sido o app ou GPS.
Me confirma o horário real que você bateu e o tipo (entrada, almoço, retorno, saída) que eu abro um ajuste pra registrar.
```

---

## ⏰ PONTO E JORNADA

### "Qual o horário que tenho que entrar?"
**Resposta (jornada padrão):**
```
A jornada padrão é:
• *Segunda a quinta:* 07:00 às 16:30 (com 1h de almoço)
• *Sexta:* 07:00 às 16:00 (com 1h de almoço)

Você tem *10 minutos de tolerância* na entrada — chegar até as 07:10 não conta como atraso.
```

**Se for Leonardo:** consultar `jornadas-individuais.md` — Leonardo tem dias normais e dias de faculdade (06:30-16:00).

**Se for Mateus:** consultar `jornadas-individuais.md` — Mateus tem 08:30-17:00 durante Tiro de Guerra.

### "Quantas batidas tenho que fazer no dia?"
**Resposta:**
```
*4 batidas* obrigatórias todo dia útil:
• Entrada
• Saída pro almoço
• Retorno do almoço
• Saída final

O horário específico de cada uma pode variar (ex: você pode almoçar 11:30 ou 12:00, tanto faz). O importante é bater as 4 no dia.
```

### "Posso almoçar em outro horário?"
**Resposta:**
```
Pode! O horário do almoço é flexível, desde que você complete a *1 hora completa* de intervalo e bata as duas marcações (saída pro almoço e retorno).
```

### "Trabalho meio período / horário diferente"
**Ação:** verificar `schedule_profile` em `employees.json` do funcionário.
**Resposta (se tem profile especial):** explicar a regra dele.
**Resposta (se não tem):**
```
Pelo que tenho aqui, sua jornada é a padrão (Seg-Qui 07:00-16:30, Sex 07:00-16:00). Se isso não estiver correto, me avisa que eu confirmo com o Pedro pra alinhar seu cadastro.
```

---

## 🩹 ESQUECEU DE BATER (AJUSTE)

### "Esqueci de bater o ponto"
**Resposta:**
```
Sem problema, dá pra ajustar! Faz assim:

1. Entra no sistema (https://ponto.budamix.com.br)
2. Vai na sua área logada
3. Clica em *"Solicitar ajuste"*
4. Coloca o tipo (entrada/saída/almoço) e o horário real
5. Explica brevemente o motivo (esqueci, app travou, etc)

A gente revisa e aprova rapidinho.
```

### "Posso ajustar depois de quantos dias?"
**Resposta:**
```
Quanto antes melhor! Idealmente no mesmo dia ou no dia seguinte.
Ajustes muito antigos (>15 dias) precisam ser combinados direto com o Pedro.
```

### "Já solicitei o ajuste, quando vai ser aprovado?"
**Ação técnica:** consultar `adjustment_requests WHERE user_id = ... AND status = 'pending'`.
**Resposta:**
```
Vi aqui sua solicitação de *<data>*. Vou priorizar a análise e te aviso assim que aprovar.
```

---

## ⚠️ ATRASO / FALTA (JUSTIFICATIVA)

### "Vou me atrasar hoje, o que faço?"
**Resposta:**
```
Quando chegar, abre uma *justificativa* no sistema:

1. Vai na sua área logada
2. Clica em *"Solicitar justificativa"*
3. Escolhe o tipo (consulta médica, emergência médica, emergência familiar)
4. *Anexa o comprovante em foto* (atestado, declaração, etc)
5. Confirma

A gente analisa e, se aprovado, o atraso não conta no banco de horas.
```

### "Quais tipos de justificativa são aceitos?"
**Resposta:**
```
Tipos aceitos com comprovante:
• 🩺 *Consulta médica* — atestado da consulta
• 🚑 *Emergência médica* — declaração ou comprovante hospitalar
• 👨‍👩‍👧 *Emergência familiar* — comprovante (boletim, declaração)

Cada caso é analisado individualmente.
```

### "E se for outro motivo (trânsito, transporte, chuva)?"
**Resposta:**
```
Esses casos são analisados *caso a caso*. Me manda aqui o que aconteceu e, se for ocasional, registro como justificado. Se for recorrente, alinhamos uma solução com o Pedro.
```

### "Vou faltar amanhã, como aviso?"
**Resposta:**
```
Me avisa por aqui o motivo:
• Se for *consulta/médico*: leve o atestado quando voltar e abre justificativa no sistema com o comprovante
• Se for *emergência familiar*: me conta o que houve, registro aqui e quando puder você anexa o comprovante na justificativa

Sempre que possível, *avise antes* — ajuda a planejar a operação.
```

### "Já mandei meu atestado, foi aprovado?"
**Ação técnica:** consultar `justificativas_solicitacao WHERE user_id = ... AND status = 'pendente'`.
**Resposta:**
```
Tenho sua justificativa de *<data>* (<tipo>) com status *<status>*.
[Se pendente:] Vou priorizar e te confirmo o resultado em breve.
[Se aprovada:] Já aprovei! O atraso/falta não vai contar no seu banco.
```

---

## 🎁 BANCO DE HORAS

### "Como vejo meu saldo de banco de horas?"
**Resposta:**
```
Direto na sua área logada do sistema, em https://ponto.budamix.com.br

Lá você vê:
• Saldo do mês atual
• Saldo acumulado de meses anteriores
• Horas extras a pagar (se houver)
```

### "Qual é meu saldo agora?"
**Ação técnica:** chamar função SQL `calcular_banco_horas_v2(p_user_id)`.
**Resposta:**
```
Seu saldo atual é:
• *Saldo do mês:* <X>h
• *Saldo acumulado:* <Y>h
• *Total:* <Z>h
```

### "Por que meu mês começa com -10h?"
**Resposta:**
```
O *-10h mensal* é um débito padrão do contrato — é a diferença entre a jornada contratual e a jornada efetiva que praticamos.

A partir desse -10h, vão entrar:
• Suas *horas extras* do mês
• *Bônus* de pontualidade e assiduidade (até +4h)

Se o mês fechar positivo, vai pro seu acumulado. Se fechar negativo, *é zerado* — você nunca herda dívida.
```

### "Como ganho os bônus de assiduidade e pontualidade?"
**Resposta:**
```
*Bônus de assiduidade* (+2h):
Se você passar o mês *sem nenhuma falta injustificada*. Faltas com atestado ou licença legal não tiram o bônus.

*Bônus de pontualidade* (+2h):
Se você passar o mês *sem nenhum atraso não justificado*. Atrasos com justificativa aprovada não tiram o bônus.

Total possível: *+4h por mês* somando os dois 💰
```

### "Posso usar o banco de horas como folga?"
**Resposta:**
```
Pode sim! Combina com o Pedro a data e quantas horas você quer compensar. As horas usadas saem do seu acumulado.
```

### "Quando o banco vira pagamento?"
**Resposta:**
```
A cada *6 meses* (30 de junho e 31 de dezembro) o saldo positivo acumulado é convertido em pagamento ou folga compensatória, conforme combinado com o Pedro.

Se em algum momento seu saldo passar de *40h*, o excedente vira automaticamente *horas extras a pagar* na folha.
```

### "Tenho hora extra acumulada?"
**Ação técnica:** `profiles.horas_extras_a_pagar WHERE id = ...`.
**Resposta:**
```
Você tem *<X>h* de horas extras a pagar registradas. O Pedro vai converter isso em pagamento no próximo fechamento.
```

---

## 🚫 SÁBADO, DOMINGO, FERIADO

### "Trabalhei sábado, vai pro banco?"
**Resposta:**
```
Sábado, domingo e feriado *não entram no banco de horas* — quando há trabalho nesses dias, ele é pago à parte como valor fixo, conforme combinado com o Pedro.

Por isso, *não bate ponto nesses dias* a não ser que o Pedro tenha autorizado e combinado o pagamento à parte com você.
```

### "Por que não posso bater ponto sábado?"
**Resposta:**
```
A regra da empresa é que sábado, domingo e feriado são pagos como *valor fixo separado*, fora do banco de horas. Se a gente registrasse no sistema, ia gerar duplicidade (pago e ainda contando como hora extra).

Se você trabalhou em algum desses dias, alinhe direto com o Pedro o pagamento.
```

---

## 🎓 JORNADAS ESPECIAIS (Leonardo, Mateus)

### Leonardo — dias de faculdade
Ver `jornadas-individuais.md` seção Leonardo. Resposta padrão:
```
Conforme combinado com o Pedro, você tem dois esquemas:
• *Dias normais:* 07:00 às 16:30
• *Dias de faculdade:* 06:30 às 16:00

Em ambos a jornada bate certinho. Se a gente ainda não confirmou quais dias da semana são de faculdade, me confirma aqui pra eu registrar.
```

### Mateus — Tiro de Guerra
Ver `jornadas-individuais.md` seção Mateus. Resposta padrão:
```
Conforme combinado com o Pedro, durante o Tiro de Guerra:
• *Entrada:* 08:30
• *Saída:* 17:00

Sua tolerância de atraso é até as *08:40*. Eventualmente o Pedro pode te pedir pra ficar até mais tarde — essas horas extras entram no banco normalmente.
```

---

## 📅 CONFERÊNCIA SEMANAL

### "Vou receber mensagem toda semana?"
**Resposta:**
```
Sim, *toda segunda às 10h* eu mando uma mensagem aqui pra alinhar pendências da semana anterior (atraso, batida faltando, etc).

Se estiver tudo certinho, você não recebe nada — *silêncio = tudo OK* 👌
```

---

## ❌ O QUE O AGENTE *NÃO SABE* (DEVE ESCALAR)

> **REGRA CRÍTICA:** Se o funcionário perguntar sobre um dos itens abaixo, o agente DEVE responder
> "Não tenho essa informação aqui comigo no momento. Vou alinhar com o Pedro e te retorno
> assim que ele me passar. 🙏" e escalar via Telegram thread RH.

**Folha de pagamento e benefícios:**
- Salário, contracheque, holerite
- 13º salário
- FGTS
- Vale-transporte, vale-refeição, vale-alimentação
- Plano de saúde
- Cesta básica, premiações, comissões

**Férias:**
- Saldo de dias de férias disponíveis
- Como solicitar férias
- Período aquisitivo, vencimento
- Dividir férias em períodos

**Questões trabalhistas / CLT:**
- Direitos específicos (insalubridade, periculosidade, etc)
- Demissão, advertência, suspensão
- Aviso prévio
- Cálculo de rescisão
- Estabilidade

**Conflitos pessoais:**
- Reclamações sobre gestão, colegas, ambiente
- Problemas pessoais delicados
- Denúncias

**Outras informações administrativas:**
- Mudança de endereço cadastral, conta bancária
- Documentos pessoais (RG, CPF, CTPS)
- Contratos
- Treinamentos, cursos, vagas internas

**Resposta padrão pra todos esses:**
```
Não tenho essa informação aqui comigo no momento. Vou alinhar com o Pedro e te retorno assim que ele me passar. 🙏
```

E começar a resposta interna com:
```
ESCALAR: pergunta sem resposta na KB - "<texto da pergunta>"
```

---

## 💬 MENSAGENS FORA DE CONTEXTO RH

### "Bom dia / oi / tudo bem?"
**Resposta:**
```
Oi <nome>! Tudo bem por aqui 😊
Em que posso te ajudar com algo do RH? (ponto, banco de horas, justificativas, etc.)
```

### "Posso conversar sobre [assunto não-RH]?"
**Resposta:**
```
Esse canal é só pra assuntos do RH (ponto, banco de horas, justificativas, etc).
Pra outros assuntos, fala direto com o Pedro 👌
```

---

## Notas relacionadas

- [[regras-ponto-certo|Regras detalhadas do Ponto Certo]] — fonte normativa
- [[jornadas-individuais|Jornadas Individuais]] — Leonardo, Mateus
- [[politica-sabado-trabalhado|Política Sábado]]
- [[../skills/atendimento-espontaneo/SKILL|Skill Atendimento Espontâneo]] — fluxo de processamento
- [[../skills/monitor-ponto/SKILL|Skill Monitor Ponto]] — conferência semanal
- [[../../../rh/SOUL|SOUL]] — princípios invioláveis (incl. honestidade)

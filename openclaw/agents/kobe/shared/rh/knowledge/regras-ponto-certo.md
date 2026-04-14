---
title: "regras ponto certo"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Knowledge File — Regras do Sistema Ponto Certo

## 1. Controle de Ponto

### 1.1 Jornada de Trabalho

| Dia | Jornada Base | Horario | Saida |
|-----|-------------|---------|-------|
| Segunda a Quinta | 8h30min | 07:00 - 16:30 | 16:30 |
| Sexta-feira | 8h00min | 07:00 - 16:00 | 16:00 |
| Sabado | Nao trabalha | - | - |
| Domingo | Nao trabalha | - | - |

- Intervalo de almoco: 1 hora (descontado automaticamente do calculo)
- Qualquer hora trabalhada em sabado ou domingo e contabilizada integralmente como hora extra

### 1.2 Tipos de Marcacao

| Codigo | Descricao |
|--------|-----------|
| clock_in | Entrada |
| break_start | Saida para intervalo (almoco) |
| break_end | Retorno do intervalo |
| clock_out | Saida final |

A sequencia esperada no dia e: clock_in -> break_start -> break_end -> clock_out.

O sistema possui sugestao inteligente que recomenda o proximo tipo com base no ultimo registro e no horario atual (ex: entre 11h e 14h sugere saida para intervalo; apos 16h sugere saida final).

### 1.3 Metodos de Registro

1. QR Code (funcionario logado): Na pagina /ponto, o funcionario escaneia o QR Code diario. Validado pela Edge Function validate-qr-ponto com JWT obrigatorio.
2. Quick Clock-In (sem login previo): Na tela de login, o funcionario clica "Bater Ponto", escaneia o QR e faz um mini-login (email + senha). Validado pela Edge Function validate-qr-ponto-public sem JWT.
3. Manual (admin): O administrador pode inserir registros manualmente via painel /admin/historico-ponto.

### 1.4 Validacao de GPS

Toda marcacao via QR Code exige validacao de localizacao:
- Coordenadas da empresa: Latitude -22.7416, Longitude -46.9144
- Raio permitido: 50 metros (configuravel em company_settings)
- Algoritmo: Formula de Haversine (calculo geodesico)
- Dupla validacao: Frontend (antes de abrir scanner) + Backend (Edge Function)

### 1.5 QR Code Rotativo

- O QR Code contem um UUID secreto (ponto_qr_secret) que rotaciona diariamente a meia-noite
- Funcao SQL refresh_qr_code_daily() atualiza o segredo automaticamente
- Payload: { type: "ponto", secret: "[uuid]", date: "YYYY-MM-DD", company: "financeflow" }
- Exibido em tela fullscreen na recepcao (rota /monitor) com Wake Lock ativo

### 1.6 Tolerancia para Atraso

| Parametro | Valor |
|-----------|-------|
| Horario contratual de entrada | 07:00 |
| Tolerancia | 10 minutos |
| Limite para atraso | 07:10 |

- Entrada ate 07:10: normal, sem registro de atraso
- Entrada apos 07:10: atraso registrado automaticamente na tabela atrasos
- Os minutos de atraso sao calculados a partir de 07:10 (ex: entrada as 07:25 = 15 min de atraso)
- A deteccao ocorre em dois pontos:
  - Frontend (hook useTimeRecords): ao registrar clock_in, usa constantes TOLERANCE_HOUR=7, TOLERANCE_MINUTE=40 — NOTA: este valor esta desatualizado no frontend (07:40) mas o backend usa 07:10
  - Backend (Edge Function detectar-atrasos): cron diario as 08:00 BRT, usa TOLERANCE_HOUR=7, TOLERANCE_MINUTE=10

### 1.7 Correcao e Abono de Ponto

- Solicitacao pelo funcionario: Via pagina de solicitacoes, o funcionario envia pedido de ajuste com motivo obrigatorio
- Ajuste pelo admin: Em /admin/historico-ponto, o admin pode editar qualquer registro. Motivo obrigatorio (min. 10 caracteres). O horario original e preservado em recorded_at_original
- Auditoria: Data da edicao (edited_at) e responsavel sao registrados

### 1.8 Faltas

| Tipo | Impacto no Bonus de Assiduidade |
|------|--------------------------------|
| injustificada | Perde o bonus de assiduidade do mes |
| atestado_medico | Mantem o bonus |
| licenca_legal | Mantem o bonus |

- Faltas sao registradas pelo admin via RegistrarFaltaDialog na pagina /admin/banco-horas
- Documentos comprobatorios podem ser anexados (campo documento_url)

### 1.9 Justificativa de Atraso/Falta

- Funcionario pode solicitar justificativa com tipos: Consulta Medica, Emergencia Medica, Emergencia Familiar
- Upload de comprovante (foto) armazenado no bucket justificativas-comprovantes
- Dados salvos na tabela justificativas_solicitacao
- Quando aprovada pelo admin: o campo justificado = true e marcado na tabela atrasos
- Atrasos justificados nao invalidam o bonus de pontualidade
- Atrasos justificados permanecem na contagem total de ocorrencias (visibilidade de historico)

## 2. Banco de Horas

### 2.1 Acumulo de Horas

O saldo do banco de horas e composto por duas partes:

Saldo Total = Saldo Historico + Saldo do Mes Atual

- Saldo Historico (banco_horas_acumulado em profiles): credito acumulado de meses anteriores. Valor fixado pela gestao apos fechamento mensal.
- Saldo do Mes: calculado dinamicamente como Horas Extras + Bonus Assiduidade + Bonus Pontualidade + Debito Mensal

### 2.2 Calculo de Horas Extras Diarias

Funcao SQL: calcular_horas_extras_dia(p_user_id, p_data)

Horas Extras do Dia = Tempo Trabalhado - Jornada Base do Dia

Onde:
  Tempo Trabalhado = (Horario Saida - Horario Entrada) - Tempo Total de Pausas
  Jornada Base = 8h30 (Seg-Qui) ou 8h00 (Sex) ou 0h (Sab/Dom)

Se Tempo Trabalhado <= Jornada Base: Horas Extras = 0
Se Tempo Trabalhado > Jornada Base: Horas Extras = diferenca positiva

- Nao ha fator multiplicador no banco de horas. Horas extras sao acumuladas 1:1.
- Sabados e domingos tem jornada base = 0, entao qualquer hora trabalhada e integralmente extra.

### 2.3 Debito Mensal Fixo

| Parametro | Valor |
|-----------|-------|
| Debito mensal | -10 horas |

- Aplicado integralmente a cada mes (nao e proporcional a dias trabalhados)
- Configuravel em company_settings.debito_mensal
- Representa a diferenca entre a jornada contratual e a jornada efetiva padrao

### 2.4 Formula Completa do Saldo Mensal

Saldo do Mes = soma(Horas Extras Diarias) + Bonus Assiduidade + Bonus Pontualidade + Debito Mensal

Onde:
  soma(Horas Extras Diarias) = soma de calcular_horas_extras_dia() para cada dia do mes
  Bonus Assiduidade = +02:00 (se elegivel) ou 00:00
  Bonus Pontualidade = +02:00 (se elegivel) ou 00:00
  Debito Mensal = -10:00:00

### 2.5 Exemplo Pratico de Calculo

Cenario: Funcionario em marco com 3h de horas extras, sem faltas, sem atrasos.

Horas extras do mes:     +03:00
Bonus assiduidade:       +02:00  (0 faltas injustificadas)
Bonus pontualidade:      +02:00  (0 atrasos nao justificados)
Debito mensal:           -10:00
Saldo do mes:            -03:00

Se Saldo Historico = +05:00
Saldo Total exibido = +05:00 + (-03:00) = +02:00

Cenario: Mesmo funcionario, mas com 1 atraso nao justificado.

Horas extras do mes:     +03:00
Bonus assiduidade:       +02:00  (0 faltas injustificadas)
Bonus pontualidade:       00:00  (1 atraso -> perde bonus)
Debito mensal:           -10:00
Saldo do mes:            -05:00

Cenario: Funcionario com 15h extras, sem faltas, sem atrasos.

Horas extras do mes:     +15:00
Bonus assiduidade:       +02:00
Bonus pontualidade:      +02:00
Debito mensal:           -10:00
Saldo do mes:            +09:00

### 2.6 Teto do Banco de Horas

| Parametro | Valor |
|-----------|-------|
| Teto maximo | 40 horas |

- Quando o saldo total ultrapassa 40h, o excedente e transferido para horas_extras_a_pagar no perfil do funcionario
- Funcao SQL aplicar_teto_banco_horas() faz essa transferencia
- Edge Function verificar-teto-banco-horas processa todos os funcionarios periodicamente
- Alertas visuais no card do funcionario:
  - 80% do teto (32h): alerta amarelo "considere tirar folga"
  - 100% do teto (40h): alerta vermelho "excedente sera pago"

### 2.7 Fechamento Mensal

Edge Function: reset-banco-horas (executada no 1o dia de cada mes)

Processo:
1. Calcula o saldo isolado do mes anterior usando calcular_banco_horas_mes()
2. Saldo positivo: soma ao banco_horas_acumulado do perfil
3. Saldo negativo ou zero: ignorado — o colaborador nunca herda divida de horas
4. Insere registro de auditoria na tabela banco_horas com todos os detalhes

### 2.8 Override Manual

Se existir um registro na tabela banco_horas para o mes de referencia (criado via ajuste administrativo), o sistema usa obrigatoriamente esses valores salvos para bonus, faltas e atrasos, em vez de recalcular dinamicamente. O campo horas_extras do override so e usado se for diferente de zero.

### 2.9 Fechamento Semestral

| Semestre | Data de Fechamento |
|----------|--------------------|
| S1 | 30 de Junho |
| S2 | 31 de Dezembro |

Edge Function: reset-semestral

Processo:
1. Verifica saldo acumulado de cada funcionario
2. Se saldo positivo: converte em pagamento (horas_extras_a_pagar) ou folgas compensatorias
3. Registra na tabela banco_horas_historico (semestre, saldo final, horas pagas)
4. Zera o banco_horas_acumulado do perfil
5. Saldo negativo nao e carregado — zerado automaticamente

Alertas: 30 dias antes do fim do semestre, o sistema exibe alerta ao funcionario.

### 2.10 Tratamento de Saldo Negativo

- Visualizacao em tempo real: saldo negativo e exibido normalmente para o funcionario ver seu deficit
- No fechamento mensal: saldo negativo do mes nao e debitado do acumulado. O acumulado nunca diminui por saldo mensal negativo.
- No fechamento semestral: saldo negativo e simplesmente zerado. Nao ha desconto em folha.
- O sistema mostra "Horas faltantes" quando o saldo total e negativo, indicando quanto o funcionario precisa compensar.

### 2.11 Tratamento de Saldo Positivo

- Uso como folga compensatoria: registrado via horas_usadas_folga na tabela banco_horas_historico
- Pagamento: convertido em horas_extras_a_pagar no fechamento semestral ou quando excede o teto
- Acumulo: mantido no banco ate o fechamento semestral (maximo 6 meses de acumulo)

## 3. Bonus e Adicionais

### 3.1 Bonus de Assiduidade

| Parametro | Valor |
|-----------|-------|
| Valor | +2 horas no banco |
| Periodicidade | Mensal |
| Configuravel | Sim (company_settings.bonus_assiduidade_valor, bonus_assiduidade_ativo) |

Criterio de elegibilidade: Zero faltas injustificadas no mes de referencia.
- Faltas do tipo atestado_medico ou licenca_legal nao anulam o bonus
- Apenas faltas do tipo injustificada anulam o bonus
- E binario: uma unica falta injustificada = perda total do bonus

### 3.2 Bonus de Pontualidade

| Parametro | Valor |
|-----------|-------|
| Valor | +2 horas no banco |
| Periodicidade | Mensal |
| Configuravel | Sim (company_settings.bonus_pontualidade_valor, bonus_pontualidade_ativo) |

Criterio de elegibilidade: Zero atrasos nao justificados no mes de referencia.
- Atrasos com justificado = true (aprovados pelo admin) nao anulam o bonus
- Apenas atrasos com justificado = false anulam o bonus
- E binario: um unico atraso nao justificado = perda total do bonus

### 3.3 Impacto Combinado

| Cenario | Assiduidade | Pontualidade | Total Bonus |
|---------|-------------|--------------|-------------|
| Sem faltas, sem atrasos | +2h | +2h | +4h |
| 1 falta injustificada, sem atrasos | 0h | +2h | +2h |
| Sem faltas, 1 atraso nao justificado | +2h | 0h | +2h |
| 1 falta injust. + 1 atraso | 0h | 0h | 0h |
| 1 falta por atestado, 1 atraso justificado | +2h | +2h | +4h |

## 4. Funcoes SQL de Calculo

### 4.1 calcular_banco_horas_v2(p_user_id) — Mes Corrente
Calcula o saldo total em tempo real (saldo historico + saldo do mes atual). Usada no dashboard do funcionario e do admin para exibicao. Consulta company_settings para parametros dinamicos.

### 4.2 calcular_banco_horas_mes(p_user_id, p_mes) — Mes Especifico
Mesma logica da v2, mas para qualquer mes passado como parametro. Usada pelo fechamento mensal (reset-banco-horas) e auditorias historicas.

### 4.3 calcular_horas_extras_dia(p_user_id, p_data) — Dia Especifico
Calcula horas extras de um dia com base na jornada configurada. Considera entradas, saidas e pausas do dia.

### 4.4 calcular_banco_horas(p_user_id) — DEPRECATED
Funcao v1 com formula incorreta (-4h x semanas em vez de -10h/mes) e sem bonus. Marcada como deprecated. Nao deve ser usada.

### 4.5 aplicar_teto_banco_horas(p_user_id, p_saldo_calculado)
Verifica se o saldo excede o teto individual do funcionario (padrao 40h). Se exceder, transfere o excedente para horas_extras_a_pagar.

### 4.6 reset_semestral(p_user_id, p_data_fechamento)
Executa o fechamento semestral: salva historico, transfere saldo para pagamento, zera acumulado.

## 5. Automacoes (Edge Functions)

| Funcao | Trigger | Descricao |
|--------|---------|-----------|
| detectar-atrasos | Cron diario 08:00 BRT | Verifica entradas do dia e registra atrasos |
| reset-banco-horas | Cron 1o dia do mes | Fecha o mes anterior e acumula saldo positivo |
| reset-semestral | Manual/Cron em Jun/Dez | Fecha o semestre, paga saldo positivo, zera banco |
| verificar-teto-banco-horas | Periodico | Aplica teto de 40h e transfere excedente |

## 6. Configuracoes Administrativas

Todos os parametros abaixo sao editaveis pelo admin em /admin/ajustes -> aba "Regras":

| Parametro | Default | Campo |
|-----------|---------|-------|
| Jornada Seg-Qui | 8h30 | jornada_segunda_quinta |
| Jornada Sexta | 8h00 | jornada_sexta |
| Jornada Sabado | 0h | jornada_sabado |
| Jornada Domingo | 0h | jornada_domingo |
| Horario de entrada | 07:00 | horario_entrada |
| Tolerancia atraso | 10 min | tolerancia_atraso_minutos |
| Debito mensal | -10h | debito_mensal |
| Teto banco de horas | 40h | banco_horas_teto_global |
| Bonus assiduidade | 2h | bonus_assiduidade_valor |
| Bonus pontualidade | 2h | bonus_pontualidade_valor |
| Fechamento S1 | 30/06 | fechamento_semestre_1 |
| Fechamento S2 | 31/12 | fechamento_semestre_2 |
| Raio GPS | 50m | ponto_raio_metros |

## 7. Tabelas Relevantes

| Tabela | Funcao |
|--------|--------|
| profiles | Dados do funcionario + saldo acumulado + teto individual |
| time_records | Marcacoes de ponto (entrada, saida, intervalos) |
| atrasos | Registros de atraso com flag justificado |
| faltas | Registros de ausencia por tipo |
| banco_horas | Registro mensal de fechamento (override + auditoria) |
| banco_horas_historico | Registro semestral de fechamento |
| company_settings | Configuracoes globais do sistema |
| adjustment_requests | Solicitacoes de ajuste de ponto |
| justificativas_solicitacao | Solicitacoes de justificativa de atraso/falta |
| user_roles | Roles (admin / employee) |

## 8. Particularidades e Excecoes

1. Protecao do acumulado: O banco_horas_acumulado nunca e decrementado por saldo mensal negativo. So e decrementado no fechamento semestral (zerado).
2. Override manual: Registros na tabela banco_horas para o mes corrente funcionam como override — o sistema para de calcular dinamicamente e usa os valores salvos.
3. Ajuste admin do banco: O admin pode editar diretamente o banco_horas_acumulado e horas_extras_a_pagar do perfil, alem de bonus e contadores na tabela banco_horas. Motivo obrigatorio para auditoria.
4. Cascata de exclusao: Deletar um usuario do auth remove automaticamente todos os dados associados (profiles, user_roles, time_records, atrasos, faltas, banco_horas).
5. Inconsistencia de tolerancia no frontend: O hook useTimeRecords.ts usa TOLERANCE_MINUTE=40 (antigo) enquanto o backend usa 10 minutos. A deteccao confiavel e a do backend (Edge Function detectar-atrasos).
6. Timezone: Todo o sistema opera em America/Sao_Paulo (UTC-3). Conversoes sao feitas nas Edge Functions e funcoes SQL.

Pendencias:
- Corrigir tolerancia no frontend (TOLERANCE_MINUTE=40 -> 10)
- Exportar como PDF

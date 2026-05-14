# Regras de Escalonamento — Trader ↔ DSA ↔ Kobe

**Versão:** 1.0
**Data:** 2026-05-14

---

## Princípio

O DSA reporta condições ao Trader via output padronizado. O Trader decide se escala para Kobe com base nestas regras. O DSA nunca fala com Kobe diretamente.

---

## 1. Layer 0 NOT_READY

**Trigger:** `data_readiness.status = NOT_READY`
**Ação imediata:** Bloquear pipeline completo. Nenhuma camada analítica é executada.
**Output:** `global_failure = "layer0"`, `global_status = "BLOCKED"`
**Escalonamento:** Trader alerta Kobe.
**Severidade:** critical
**Motivo:** Dados insuficientes para qualquer análise — risco de envio com informação incorreta.

---

## 2. DADOS_PARCIAIS

**Trigger:** `data_readiness.status = DADOS_PARCIAIS`
**Ação imediata:** Pipeline pode rodar com confiança reduzida.
**Output:** Camada Estratégica reduz confiança da tese. Condensadora preserva ressalva. QA pode aprovar com ressalva.
**Escalonamento:** Trader NÃO escala Kobe automaticamente. Registra em logs. Se padrão recorrente (3+ dias), escala.
**Severidade:** medium
**Motivo:** Dados suficientes para análise qualificada, mas com ressalva que precisa ser visível.

---

## 3. QA BLOCKED por destinatário

**Trigger:** `recipients.<nome>.qa.verdict = BLOCKED`
**Ação imediata:** Bloquear envio para este destinatário específico. Outros destinatários não são afetados.
**Output:** `recipients.<nome>.status = "BLOCKED"`, `recipients.<nome>.send_allowed = false`
**Escalonamento:** Trader escala Kobe se 2+ destinatários bloqueados na mesma rodada ou se mesmo destinatário bloqueado 2 dias seguidos.
**Severidade:** high (se 2+) / medium (se isolado)
**Motivo:** QA Gate identificou problema que compromete qualidade — envio bloqueado até correção.

---

## 4. SKU cru visível

**Trigger:** QA Gate detecta SKU/código interno visível na mensagem Slack.
**Ação imediata:** Bloquear envio do destinatário afetado.
**Output:** Blocker registrado em `recipients.<nome>.qa.blockers`
**Escalonamento:** Trader escala Kobe imediatamente — possível falha no Slack Writer ou na Condensadora.
**Severidade:** critical
**Motivo:** SKU cru é informação interna que nunca deve aparecer em mensagem para funcionários. Indica falha de pipeline.

---

## 5. Produto com risco alto de identificação

**Trigger:** QA Gate detecta produto citado nominalmente com risco alto (ex: produto sensível, item de terceiro, produto sem ASIN/título confiável).
**Ação imediata:** Bloquear envio do destinatário afetado.
**Output:** Blocker registrado em `recipients.<nome>.qa.blockers`
**Escalonamento:** Trader escala Kobe se envolver Amazon (risco de ASIN errado) ou Shopee sem separação correta de conta.
**Severidade:** high
**Motivo:** Citar produto errado gera desconfiança e pode causar ação operacional incorreta.

---

## 6. Prompt version inválida

**Trigger:** Versão de prompt solicitada não existe ou está corrompida.
**Ação imediata:** Bloquear pipeline completo.
**Output:** `global_failure = "prompt_version"`, `global_status = "BLOCKED"`
**Escalonamento:** Trader alerta Kobe — possível falha de versionamento ou config corrompida.
**Severidade:** critical
**Motivo:** Sem prompt válido, nenhuma camada pode executar corretamente.

---

## 7. Kill switch ativo

**Trigger:** `config.enabled = false` ou `config.send_real_enabled = false` (para modos de envio real).
**Ação imediata:**
- `enabled = false` → bloqueia tudo.
- `send_real_enabled = false` → permite DRY_RUN/SHADOW, bloqueia envio real.
**Output:** `global_failure = "killswitch"` (se enabled=false)
**Escalonamento:** Não automático — kill switch foi ativado deliberadamente por Trader/Kobe/Pedro.
**Severidade:** info (ação deliberada)
**Motivo:** Mecanismo de segurança. Respeitar sem tentar contornar.

---

## 8. Falha de Slack Writer

**Trigger:** Camada 6 (Slack Writer) falha ao gerar mensagem ou gera mensagem com formato inválido.
**Ação imediata:** Bloquear envio do destinatário afetado.
**Output:** `recipients.<nome>.status = "BLOCKED"`, blocker em QA.
**Escalonamento:** Trader escala Kobe se afetar 2+ destinatários ou se recorrente (2 dias).
**Severidade:** high
**Motivo:** Sem mensagem Slack válida, não há o que enviar. Pode indicar degradação de prompt.

### Ação de rollback:
- Se Slack Writer falhar 2 dias seguidos: pinar versão anterior de prompt.
- Registrar rollback em `prompts/CHANGELOG.md`.

---

## 9. Divergência de fonte canônica

**Trigger:** Reconciliação do Layer 0 detecta divergência > 10% entre fontes do mesmo dado.
**Ação imediata:** Se sistêmica (afeta todas as plataformas), bloqueia tudo. Se localizada, bloqueia plataforma afetada.
**Output:**
- Sistêmica: `global_failure = "canonical_source"`
- Localizada: blocker no destinatário afetado
**Escalonamento:** Trader escala Kobe em ambos os casos — divergência de fonte é risco de dado.
**Severidade:** critical (sistêmica) / high (localizada)
**Motivo:** Divergência de fonte significa que os números podem estar errados. Enviar análise sobre dados divergentes é pior que não enviar.

---

## 10. Feedback negativo recorrente

**Trigger:** 3+ feedbacks negativos sobre o mesmo tipo de problema na mesma semana (registrados em `audit-ressalvas.md`).
**Ação imediata:** Flag no weekly review do Trader.
**Escalonamento:**
- 3+ na semana → Trader investiga e decide ajuste.
- 5+ no mês → Escalonamento automático para Kobe.
- Mesmo padrão por 2+ semanas → Revisão formal de regra/prompt.
**Severidade:** medium (semanal) / high (mensal/recorrente)
**Motivo:** Padrão recorrente indica problema estrutural que ajuste pontual não resolve.

---

## Matriz Resumo

| Situação | Bloqueia envio | Escala Kobe | Severidade |
|----------|---------------|-------------|------------|
| Layer 0 NOT_READY | Tudo | Sim | critical |
| DADOS_PARCIAIS | Não (ressalva) | Só se recorrente | medium |
| QA BLOCKED (1 dest.) | Destinatário | Se recorrente | medium |
| QA BLOCKED (2+ dest.) | Destinatários | Sim | high |
| SKU cru visível | Destinatário | Sim | critical |
| Produto risco alto | Destinatário | Se Amazon/Shopee | high |
| Prompt version inválida | Tudo | Sim | critical |
| Kill switch ativo | Conforme config | Não (deliberado) | info |
| Falha Slack Writer | Destinatário | Se 2+ ou recorrente | high |
| Divergência canônica sistêmica | Tudo | Sim | critical |
| Divergência canônica local | Plataforma | Sim | high |
| Feedback negativo recorrente | Não | Se 5+/mês | medium-high |

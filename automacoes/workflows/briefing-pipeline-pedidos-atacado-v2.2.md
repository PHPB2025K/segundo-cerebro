---
title: "Briefing v2.2 — Pipeline Agente de Pedidos de Atacado com Cadastro Automático de Cliente"
type: briefing
created: 2026-05-14
status: draft-for-approval
owner: Pedro Broglio
base_documents:
  - briefing-pipeline-pedidos-atacado-v2.md
  - briefing-pipeline-pedidos-atacado-v2.1.md
tags:
  - atacado
  - whatsapp
  - bling
  - fisco
  - automacao
  - agente-pedidos
  - cadastro-cliente
---

# Briefing v2.2 — Cadastro automático de cliente novo

Este documento substitui o **Item 1 da v2.1** e ajusta as seções impactadas pela nova regra:

> Cliente novo **não bloqueia automaticamente**. Se houver CNPJ válido e dados mínimos forem encontrados com segurança, o agente cadastra o cliente no Bling e cria o pedido na sequência.

A Fase 0 ainda **não começa** até aprovação explícita desta v2.2.

---

# 1. Nova regra — cliente novo cadastrado automaticamente

## Decisão

Se o CNPJ informado no pedido **não existir no Bling**, o agente deve iniciar um subprocesso de cadastro automático.

Fluxo:

```text
CNPJ não encontrado no Bling
        ↓
Validar CNPJ
        ↓
Enriquecer dados do cliente
        ↓
Validar campos mínimos
        ↓
Criar cadastro no Bling
        ↓
Criar pedido no Bling
        ↓
Responder no grupo + alertar Pedro no privado
```

---

## 1.1 CNPJ obrigatório

Sem CNPJ explícito na mensagem, o agente **bloqueia**.

Não pode deduzir CNPJ pelo nome da empresa.

Resposta no grupo:

```text
Pedido [N] não foi criado.
Cliente não cadastrado no Bling e CNPJ não foi informado.
Por favor envie o CNPJ para eu cadastrar e gerar o pedido.
```

Regra:

- CNPJ precisa vir do remetente autorizado.
- CNPJ precisa ter 14 dígitos.
- CNPJ precisa passar validação de dígito verificador.
- CNPJ inválido bloqueia e pergunta no grupo.

---

# 2. Enriquecimento de cliente — cascata de fontes

## Recomendação do Kobe

Eu ajustaria a ordem proposta para reduzir risco.

A busca web aberta é útil, mas para cadastro fiscal o melhor primeiro passo é fonte estruturada de CNPJ. Depois usamos web aberta para complementar e validar telefone/e-mail/site.

## Cascata v2.2

### Camada 1 — Fontes estruturadas por CNPJ

Objetivo: razão social, nome fantasia, endereço fiscal, situação cadastral, CNAE, telefone/e-mail quando disponível.

Ordem sugerida:

1. **BrasilAPI CNPJ**
2. **Minha Receita / ReceitaWS / CNPJ.ws** — usar conforme disponibilidade e limite
3. **Consulta pública alternativa de CNPJ** — fallback, se configurado

Regra:

- Se duas fontes estruturadas retornarem o mesmo campo de forma consistente, campo fica `verified`.
- Se uma fonte estruturada for claramente oficial/primária e outra estiver indisponível, o campo pode entrar como `registry_verified_single_source`, mas só para razão social e endereço fiscal.
- Para telefone/e-mail, uma fonte única não basta: fica `unverified`.

### Camada 2 — Site oficial da empresa

Busca por:

- site oficial;
- página de contato;
- rodapé;
- página “sobre nós”.

Uso principal:

- telefone;
- e-mail;
- nome fantasia;
- confirmação de endereço comercial.

### Camada 3 — Busca web aberta

Usar Brave/Google-equivalente para encontrar:

- site oficial;
- páginas públicas com CNPJ;
- listagens públicas da empresa;
- redes sociais profissionais.

### Camada 4 — Redes profissionais/públicas

Exemplo:

- LinkedIn da empresa;
- Instagram/Facebook público, se exibirem contato/endereço;
- diretórios empresariais públicos.

### Camada 5 — Fallback humano

Se os campos mínimos não forem encontrados em até 90 segundos, o agente pergunta no grupo.

---

# 3. Regra de validação cruzada

## Princípio

LLM não pode preencher lacuna.

O LLM só organiza dados encontrados. Ele não inventa, não deduz e não completa endereço “provável”.

Prompt obrigatório:

```text
Se você não tem certeza, retorne null.
Não invente.
Não deduza por nome da empresa.
Não preencha campo com “não informado”, “a definir”, “consultar” ou valores vagos.
```

## Campo aceito

Um campo pode ser aceito se:

1. aparecer consistente em **2+ fontes independentes**; ou
2. vier de fonte estruturada de CNPJ confiável e for campo fiscal básico: razão social/endereço fiscal; ou
3. for confirmado diretamente na própria mensagem do pedido.

## Campo não aceito

Rejeitar automaticamente:

- “não informado”;
- “a definir”;
- “consultar”;
- endereço sem número quando número for obrigatório;
- endereço vago tipo “Centro, São Paulo”;
- telefone/e-mail encontrados em só uma fonte fraca;
- dados inferidos pelo LLM sem fonte.

---

# 4. Timeout do enriquecimento

Timeout total: **90 segundos**.

Ao atingir 90s:

| Situação | Ação |
|---|---|
| Tem mínimo obrigatório | Cria cadastro + cria pedido |
| Não tem mínimo obrigatório | Bloqueia e pergunta no grupo |
| Fonte externa lenta | Registra no log, segue com fontes disponíveis |
| Erro técnico geral | DLQ + alerta privado |

Não pode ficar vários minutos tentando enriquecer enquanto o vendedor espera.

---

# 5. Campos obrigatórios x opcionais

## 5.1 Obrigatórios para cadastrar cliente automaticamente

Campos mínimos para criar cadastro no Bling:

| Campo | Regra |
|---|---|
| CNPJ | obrigatório, 14 dígitos, DV válido |
| Razão social | obrigatória, fonte confiável |
| CEP | obrigatório |
| Rua/logradouro | obrigatório |
| Número | obrigatório; se fonte pública trouxer “S/N”, aceitar como `S/N` |
| Cidade | obrigatória |
| UF | obrigatória |

## 5.2 Fortemente recomendados, mas não bloqueantes

| Campo | Regra |
|---|---|
| Bairro | usar se encontrado; se ausente, permitir cadastro e marcar `unverified/missing` |
| Nome fantasia | usar se verificado; se não, `null` |
| Telefone | usar se 2+ fontes ou mensagem original; senão `null` |
| E-mail | usar se 2+ fontes ou site oficial; senão `null` |
| Inscrição Estadual | se não encontrada, cadastrar como `isento` |
| CNAE | salvar no log se disponível; não precisa ir ao Bling nesta fase |
| Situação cadastral | se baixada/inapta/suspensa, bloquear |

## 5.3 Campos que bloqueiam se inconsistentes

- CNPJ inválido;
- razão social conflitante entre fontes fortes;
- endereço fiscal conflitante sem fonte dominante;
- situação cadastral baixada, inapta ou suspensa;
- cidade/UF incompatíveis com CEP confirmado.

---

# 6. Criação no Bling

## 6.1 Quando criar cadastro

Criar cadastro no Bling somente quando:

- CNPJ válido;
- cliente não existe no Bling;
- campos mínimos obrigatórios encontrados;
- validação cruzada aprovada;
- situação cadastral não bloqueante;
- payload passa schema interno.

## 6.2 Depois do cadastro

Cadastro criado com sucesso → criar pedido na sequência, sem pedir confirmação.

Pedido deve nascer em status editável:

```text
Em aberto
```

ou equivalente no Bling.

Nunca criar como confirmado quando cliente foi cadastrado há menos de 24h.

---

# 7. Trava de 24h para cliente recém-criado

Todo pedido vinculado a cliente cadastrado automaticamente nas últimas 24h deve:

- nascer em status editável;
- ficar com observação interna indicando “cliente cadastrado automaticamente”;
- aparecer no alerta privado;
- permanecer passível de correção/cancelamento.

Promoção para status normal:

- pode ser manual; ou
- automática após 24h sem objeção do Pedro, se aprovada depois.

Minha recomendação inicial: **manual nas Fases 1–2; automático só Fase 3**.

---

# 8. Notificações obrigatórias

## 8.1 Resposta no grupo

Quando cliente novo for cadastrado e pedido criado:

```text
Pedido [N] criado no Bling.
Cliente: [Razão Social] (CNPJ [XX.XXX.XXX/XXXX-XX])
Cliente foi cadastrado agora — verificar dados se necessário.
SKU: [X]
Quantidade: [Y]
```

## 8.2 Alerta privado para Pedro

Obrigatório em todo pedido com cliente recém-criado:

```text
Alerta: cliente novo cadastrado automaticamente + pedido criado.
CNPJ: [X]
Razão social: [Y]
Endereço: [Z]
Fontes usadas: [lista]
Campos não verificados: [lista]
Pedido Bling: [ID]
Tempo de enriquecimento: [Xs]
```

Esse alerta não bloqueia o fluxo. Serve como janela de intervenção rápida.

---

# 9. Logs de enriquecimento

Adicionar tabela:

## `wholesale_client_enrichment_log`

Campos:

- `id`
- `cnpj`
- `order_message_id`
- `order_number`
- `final_legal_name`
- `final_trade_name`
- `final_address_json`
- `final_phone`
- `final_email`
- `state_registration`
- `taxpayer_status`
- `fields_json`
- `sources_json`
- `source_failures_json`
- `unverified_fields_json`
- `confidence_by_field_json`
- `created_bling_contact_id`
- `enrichment_status`
- `duration_ms`
- `created_at`

## `fields_json`

Cada campo deve guardar:

```json
{
  "field": "address.street",
  "value": "Rua X",
  "status": "verified | registry_verified_single_source | unverified | null | rejected",
  "sources": ["url/fonte 1", "url/fonte 2"],
  "reason": "campo consistente em 2 fontes"
}
```

---

# 10. Casos de erro

| Cenário | Ação |
|---|---|
| CNPJ ausente | Bloqueia e pede CNPJ no grupo |
| CNPJ inválido | Bloqueia e pede CNPJ correto no grupo |
| CNPJ já existe no Bling | Usa cadastro existente e segue pedido |
| CNPJ não existe no Bling + enriquecimento completo | Cria cadastro + cria pedido + notifica |
| Enriquecimento parcial com mínimo obrigatório | Cria cadastro + cria pedido + alerta campos não verificados |
| Falta mínimo obrigatório | Bloqueia e pede campos faltantes no grupo |
| Timeout 90s com mínimo obrigatório | Cria com mínimo e alerta lacunas |
| Timeout 90s sem mínimo | Bloqueia e pede campos faltantes |
| Bling erro ao criar cliente | DLQ + alerta privado, sem resposta técnica no grupo |
| Situação cadastral bloqueante | Bloqueia e alerta privado |

---

# 11. Ajustes no checklist determinístico da v2.1

Substituir grupo “Cliente” por:

## Cliente

1. CNPJ veio explícito na mensagem?
2. CNPJ tem 14 dígitos e DV válido?
3. Cliente existe no cadastro local/Bling?
   - se sim: usa cadastro existente;
   - se não: dispara enriquecimento obrigatório.
4. Enriquecimento retornou campos mínimos?
5. Situação cadastral é aceitável?
6. Cadastro Bling criado com sucesso?
7. Pedido usará cliente existente ou recém-criado com ID Bling válido?
8. Se cliente recém-criado: pedido deve nascer em status editável + alerta privado obrigatório.

---

# 12. Ajuste no score de cliente

Score de cliente passa a ser:

| Situação | Score cliente |
|---|---:|
| Cliente já existia no Bling/local e está consistente | 1.00 |
| Cliente recém-criado com campos obrigatórios + 2 fontes nos campos principais | 0.95 |
| Cliente recém-criado com fonte estruturada forte para razão/endereço, mas campos opcionais incompletos | 0.85 |
| Cliente recém-criado com mínimo obrigatório, porém parte do endereço em `registry_verified_single_source` | 0.80 |
| Abaixo do mínimo obrigatório | bloqueia |
| CNPJ inválido/ausente | bloqueia |
| Situação cadastral bloqueante | bloqueia |

Regra:

- Cliente recém-criado com score `< 0.80` não cria pedido.
- Score de cliente é só um componente do score final; SKU/preço/quantidade continuam validados independentemente.

---

# 13. Impacto na Fase 0

## Estimativa honesta

O subsistema de cadastro automático adiciona complexidade real.

### Adicional estimado

**+1,5 a 2 dias úteis** na Fase 0.

### Fase 0 completa atualizada

Antes v2.1: **2 a 3 dias úteis**.

Com cadastro automático v2.2: **3,5 a 5 dias úteis**.

Se quiser cortar escopo para acelerar:

- sem painel visual completo no primeiro corte;
- apenas logs/tabelas/alertas;
- enriquecimento limitado a fontes estruturadas + uma busca web;
- promoção de status 24h manual.

Aí dá para mirar **3 a 3,5 dias úteis**, mas a versão robusta fica em **4 a 5 dias úteis**.

Minha recomendação: considerar **4 dias úteis** como plano realista para Fase 0 bem feita.

---

# 14. Pendências anteriores ainda abertas

## 14.1 Contato desconhecido `5519996877398`

Levantamento via metadados do grupo:

| Campo | Valor |
|---|---|
| Número | `5519996877398` |
| LID | `55220444864752@lid` |
| Nome exibido | não disponível no histórico da Evolution |
| Mensagens observadas | nenhuma mensagem de pedido observada |
| Status recomendado | `pending_validation` |

Conclusão:

- Não autorizar criação até Pedro identificar quem é.
- Se essa pessoa mandar pedido antes da validação, o sistema deve logar e alertar Pedro no privado, sem criar.

## 14.2 Prazo realista da Fase 0 completa

Com v2.2:

- **mínimo enxuto:** 3 a 3,5 dias úteis;
- **recomendado:** 4 dias úteis;
- **robusto com painel melhor e enriquecimento completo:** 5 dias úteis.

Minha recomendação operacional: planejar **4 dias úteis**.

---

# 15. Decisões para Pedro aprovar antes da Fase 0

1. Aprovar cadastro automático de cliente novo com CNPJ obrigatório.
2. Aprovar timeout de enriquecimento em 90s.
3. Aprovar que IE ausente vira `isento`.
4. Aprovar que bairro ausente não bloqueia se CEP/rua/número/cidade/UF estiverem confirmados.
5. Aprovar pedido de cliente recém-criado sempre em status editável por 24h.
6. Validar quem é `5519996877398 / 55220444864752@lid`.
7. Aprovar prazo de Fase 0: recomendação de 4 dias úteis.

---

# 16. Recomendação final do Kobe

Eu aprovo a mudança de direção: cliente novo não precisa bloquear se houver CNPJ e enriquecimento confiável.

Mas isso transforma o pipeline de “gerador de pedido” em “gerador de pedido + cadastro fiscal/comercial controlado”. Por isso o prazo sobe.

Minha recomendação final:

- v2.2 aprovada;
- Fase 0 com 4 dias úteis;
- cadastro automático liberado somente com CNPJ válido + razão social + endereço mínimo;
- alerta privado obrigatório em 100% dos clientes recém-criados;
- status editável por 24h;
- painel/log completo desde o primeiro dia.

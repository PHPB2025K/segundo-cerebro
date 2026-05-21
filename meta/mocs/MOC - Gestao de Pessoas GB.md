---
title: "MOC — Gestão de Pessoas GB"
created: 2026-05-21
type: moc
status: active
tags:
  - moc
  - pessoas
  - rh
  - gestao-funcionarios
---

# MOC — Gestão de Pessoas GB

> Hub de tudo que toca pessoas da GB Importadora. Centraliza duas frentes complementares mas distintas: gestão de performance/evolução vs RH operacional/jornada.

---

## A distinção fundamental

| Frente | Foco | Onde vive |
|---|---|---|
| **Gestão de pessoas** | Performance, evolução, acordos, feedbacks, atas semanais | [[memory/projects/gestao-funcionarios]] (lida por Kobe via Slack) |
| **RH / Ponto Certo** | Jornada, ponto, banco de horas, compliance CLT, atendimento operacional | [[projects/ponto-certo]] + [[openclaw/agents/rh/IDENTITY]] |

> Regra explicitada na ficha de gestao-funcionarios: as duas frentes NÃO se misturam — mensagens e canais Telegram são separados (tópico **Gestão de Funcionários** thread 10469 vs RH genérico).

## Equipe canônica

Fonte de verdade: [[memory/context/people]]

| Funcionário | Função | Focal point | Sistema |
|---|---|---|---|
| Yasmin Oscarlino | Operação Mercado Livre | ✅ ML | Ponto Certo + Budamix Central viewer |
| Lucas Gabriel Laurentino | Operação Shopee | ✅ Shopee | Ponto Certo + Budamix Central viewer |
| Leonardo | Operação Amazon | ✅ Amazon | Ponto Certo + Budamix Central viewer |
| Franciele (Fran) | Operação | — | Ponto Certo |
| Geziele | Operação | — | Ponto Certo |
| Guilherme Higashi | Operação | — | Ponto Certo |
| Mateus | Operação (Tiro de Guerra) | — | Ponto Certo + override mensal |
| Sandra Peron | Operação | — | Ponto Certo |

## Sistemas e domínios

| Sistema | URL | Responsável | O que faz |
|---|---|---|---|
| Ponto Certo | https://ponto.budamix.com.br | [[openclaw/agents/rh/IDENTITY|RH (agente)]] | Ponto eletrônico, banco de horas, compliance |
| Painel `/admin/conversas` (Ponto Certo) | em [[projects/ponto-certo]] | Pedro (supervisão) | Visualização das conversas RH ↔ funcionários |
| Slack DMs | — | Kobe (leitura) | Atas semanais Pedro ↔ funcionário |

## Frentes ativas que tocam a equipe

| Frente | Pessoas envolvidas | MOC/Doc |
|---|---|---|
| Acompanhamento semanal de performance | Yasmin, Lucas, Leonardo | [[memory/projects/gestao-funcionarios]] |
| Compras canecas (cross-marketplace) | Yasmin, Lucas, Leonardo | [[memory/projects/compras-canecas]] |
| Reuniões semanais marketplaces | Yasmin, Lucas, Leonardo | Calendário Pedro (presencial Pedreira-SP) |
| Override mensal de jornada | Mateus | [[automacoes/sops/mateus-override-mensal-sop]] |

## SOPs operacionais

- [[automacoes/sops/resetar-senha-funcionario]] — reset de credenciais Ponto Certo

## Princípios de segurança

- Não persistir transcrição integral de reuniões — apenas síntese executiva
- Não enviar mensagem no Slack sem autorização explícita do Pedro
- Não copiar dados sensíveis desnecessários
- Canais Telegram separados por frente (Gestão de Funcionários × Financeiro × RH genérico)

## Cadência

- **Diária:** RH atende conversas via WhatsApp ↔ funcionário (Ponto Certo dashboard)
- **Semanal (sextas EOD):** Kobe consolida Slack das DMs em [[memory/projects/gestao-funcionarios]]
- **Mensal (dia 31):** override Mateus + revisão de banco de horas

## MOCs relacionados

- [[meta/mocs/MOC - Governanca OpenClaw]] — RH é L1, leveling e protocolos

---

*Criado: 2026-05-21 — Fase 4 de densificação do vault. Separa a confusão histórica entre gestão de performance vs RH operacional.*

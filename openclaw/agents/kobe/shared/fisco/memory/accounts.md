---
title: "accounts"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Accounts — Integrações do Fisco

_Mapeamento de sistemas, credenciais e status de integração._

---

## Bling (Sistema Principal)

| Parâmetro | Valor | Status |
|-----------|-------|--------|
| **Plano** | Mercúrio (enterprise) | ✅ Confirmado |
| **API** | v3 REST | 🔴 A integrar |
| **Autenticação** | OAuth 2.0 | 🔴 Credenciais pendentes |
| **Documentação** | developer.bling.com.br | ✅ |
| **Client ID** | _Pendente registro no 1Password_ | 🔴 |
| **Client Secret** | _Pendente registro no 1Password_ | 🔴 |
| **Refresh Token** | _Pendente_ | 🔴 |
| **Token Expiry** | _Pendente_ | 🔴 |
| **Credenciais em** | 1Password → vault OpenClaw (quando registrado) | 🔴 |

### CNPJs Operados no Bling (Lucro Presumido)

| Entidade | CNPJ | Cidade | UF | IE | Papel |
|----------|------|--------|----|----|-------|
| GB Matriz | 58.151.616/0001-43 | Itajaí | SC | _A confirmar_ | Recebe importação |
| GB Filial | 58.151.616/0002-24 | Pedreira | SP | _A confirmar_ | Transferência → CNPJs Simples |

### Endpoints Principais (API v3)

| Endpoint | Uso | Módulo |
|----------|-----|--------|
| `POST /nfe` | Criar NF-e | B, C |
| `POST /nfe/{id}/enviar` | Enviar NF-e pra SEFAZ | B, C (Fase 2+) |
| `GET /nfe` | Listar NF-e emitidas | D |
| `GET /nfe/{id}` | Detalhe de NF-e | D |
| `GET /produtos` | Listar produtos | A, B, C |
| `GET /estoques` | Consultar estoque | A |
| `GET /contatos` | Listar contatos/destinatários | B, C |

---

## UpSeller (Consulta Only)

| Parâmetro | Valor | Status |
|-----------|-------|--------|
| **Função** | NFs B2C (varejo ao consumidor final) | ✅ |
| **API** | ❌ Não possui | — |
| **Acesso** | Via exports manuais ou scraping (Builder) | 🟡 |
| **CNPJs** | GB Comércio, Trades, Broglio | ✅ |

### CNPJs no UpSeller (Simples Nacional)

| Entidade | CNPJ | Regime | Papel |
|----------|------|--------|-------|
| GB Comércio | 07.194.128/0001-82 | Simples Nacional | Vendas B2C |
| Trades | 45.200.547/0001-79 | Simples Nacional | Vendas B2C |
| Broglio | 63.922.116/0001-06 | Simples Nacional | Vendas B2C |

---

## Dependências de Outros Agentes

| Agente | Dado | Endpoint/Método | Módulo | Status |
|--------|------|-----------------|--------|--------|
| **Trader** | Faturamento por marketplace/CNPJ (3 meses) | APIs marketplace (ML, Shopee, Amazon) | A, E | ✅ Trader operacional |
| **Trader** | Dados de pedidos | APIs marketplace | D | ✅ Trader operacional |
| **Builder** | Integração API Bling v3 | OAuth + REST | B, C | 🔴 A implementar |
| **Builder** | Export/scraping UpSeller | A definir | D | 🟡 Sob demanda |

---

## Contador

| Parâmetro | Valor |
|-----------|-------|
| **Escritório** | FOUR Contabilidade |
| **Contato** | Suellen |
| **Papel** | Valida regras fiscais antes do Fisco executar |
| **Canal** | Via Kobe → Pedro → Suellen |
| **Anterior** | Organização Contábil Líder (Itajaí) — encerrado |

---

## Status Geral de Integração

| Sistema | Status | Bloqueio |
|---------|--------|----------|
| Bling API v3 | 🔴 Não integrado | Credenciais OAuth + implementação Builder |
| UpSeller | 🟡 Manual | Sem API — depende de exports |
| Trader (dados) | ✅ Operacional | — |
| SEFAZ (emissão) | 🔴 Fase 2+ | Depende do Bling + aprovação Pedro |
| tax-rules.json | 🟡 Pendente validação formal | Suellen precisa validar |

---

_Atualizado em: 2026-03-29. Revisar a cada mudança de integração ou credencial._

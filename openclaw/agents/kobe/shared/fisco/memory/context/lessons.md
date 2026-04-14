# Lições do [[openclaw/agents/fisco/IDENTITY|Fisco]]

_Aprendizados operacionais. [ESTRATÉGICA] = permanente. [TÁTICA] = expira 30 dias._

### 2026-03-31 — Bling API ignora impostos no payload [ESTRATÉGICA]
**Contexto:** 5 abordagens testadas para tributar NFs via API.
**Lição:** Tributação vem EXCLUSIVAMENTE da regra fiscal na Natureza de Operação (painel web). Enviar apenas: codigo, quantidade, valor, NCM, origem. CFOP/ICMS/PIS/COFINS no payload = ignorados.
**Ação:** Configurar regra fiscal 1x no painel → criar NFs sem impostos via API.

### 2026-03-31 — Contatos devem existir na conta Bling emitente [ESTRATÉGICA]
**Contexto:** NFs draft ficaram defeituosas por destinatário inexistente.
**Lição:** Verificar via GET /contatos?pesquisa={cnpj} antes de criar NF. Criar se não existir.

### 2026-03-31 — Bug refresh token Filial: 403 "empresa inativa" [ESTRATÉGICA]
**Contexto:** Refresh automático da Filial retorna 403.
**Lição:** Token funciona mas refresh não. Re-autorizar manualmente quando expirar.

### 2026-03-31 — Excedente de vendas sobre NFs transferência → Matriz [TÁTICA]
**Contexto:** Pote 800ml (394 un) e 1520ml (883 un) venderam mais que o transferido pela Filial.
**Lição:** Excedente fatura pela Matriz (CFOP 6102, ICMS 4%). Decompor kits em unidades antes de cruzar com estoque.
**Expira:** 2026-04-30

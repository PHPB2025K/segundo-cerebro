---
title: "lessons"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

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
**Lição:** Token funciona mas refresh não. Re-autorizar manualmente quando expirar até validar causa definitiva.

### 2026-05-01 — NF interna de importados exige reconciliação fiscal antes do rateio [ESTRATÉGICA]
**Contexto:** A primeira prévia das NFs internas de abril/2026 parecia correta por CNPJ, mas misturava estoque fiscal, SKUs comerciais, SKUs fiscais, caixas, kits e produtos fora do escopo.
**Lição:** Nunca emitir NF interna só com base nas vendas do mês. Primeiro reconciliar estoque fiscal Matriz/Filial por SKU/componente, entradas/transferências, vendas, aliases Bling e fatores de conversão.
**Ação:** Módulo C deve ter etapa obrigatória de `sku_fiscal_map` + reconciliação antes de qualquer rascunho Bling.

### 2026-05-01 — Escopo fiscal não é só NCM/origem no cadastro [ESTRATÉGICA]
**Contexto:** Jarra Clink/CK4742 aparecia com NCM/origem que podiam confundir, mas Pedro confirmou que não é importação própria GB.
**Lição:** NF interna de importação própria exige filtro de escopo por natureza real do produto/fornecedor/linha própria, não apenas por NCM ou origem no Bling.
**Ação:** Manter lista de exclusões e bloquear itens de baixa confiança até validação do Pedro/Suellen.

### 2026-05-01 — Fator de conversão é ponte fiscal obrigatória [ESTRATÉGICA]
**Contexto:** `YW1520`, `YW800SQ` e `YW1050` pareciam sem estoque fiscal suficiente até investigar NFs de transferência e perceber que caixas/conjuntos fiscais estavam sendo convertidos errado.
**Lição:** Comparar NF fiscal com venda comercial sem fator de conversão gera falso estoque negativo. Caixas, conjuntos e kits precisam ser decompostos em unidade fiscal/componente antes da conciliação.
**Ação:** `sku_fiscal_map` deve registrar componente base e fator, com fonte de evidência e confiança.

### 2026-05-01 — Bling Filial pode ter cadastro por caixa enquanto NF interna precisa unidade [TÁTICA]
**Contexto:** Rascunhos travaram porque `YW1520`, `YW320SQ` e `YW520SQ` não existiam exatamente, mas existiam `CXYW1520RC`, `CXYW320SQ`, `CXYW520SQ` por caixa.
**Lição:** Antes de cadastrar unitário novo, procurar alias por caixa/sufixo (`CX`, `RC`, `RCC`, `SQC`, `_T`, `AZ`) e decidir se converte quantidade ou cadastra unitário.
**Expira:** 2026-05-31

### 2026-05-01 — DANFE Bling pode vir como HTML e precisar conversão [TÁTICA]
**Contexto:** Ao baixar NFs de transferência 000649/000653, o Bling retornou DANFE como HTML; foi necessário converter para PDF com Chrome headless antes de anexar no Gmail.
**Lição:** Validar mime/conteúdo do arquivo baixado antes de enviar ao contador. Se DANFE vier HTML, converter para PDF e nomear claramente.
**Expira:** 2026-05-31

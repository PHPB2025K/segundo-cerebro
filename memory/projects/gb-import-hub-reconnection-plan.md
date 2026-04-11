# GB Import Hub — Plano de Reconexao do Frontend

> Objetivo: trocar o frontend de Lovable Cloud (usfilmvbckfnbfnpvrph) para Supabase externo (ocxvwwaaqqxecmzhfxhb)
> Status: NAO EXECUTAR AINDA — apenas documentacao

---

## 1. Arquivos que referenciam Supabase

### Configuracao principal
| Arquivo | O que mudar |
|---------|-------------|
| `.env` | Trocar `VITE_SUPABASE_URL`, `VITE_SUPABASE_PUBLISHABLE_KEY`, `VITE_SUPABASE_PROJECT_ID` |
| `src/integrations/supabase/client.ts` | Nada (le de env vars, auto-gerado) |
| `src/integrations/supabase/types.ts` | Regenerar apos migration (supabase gen types typescript) |
| `supabase/config.toml` | Trocar `project_id` para `ocxvwwaaqqxecmzhfxhb` |

### Novos valores para .env
```
VITE_SUPABASE_PROJECT_ID="ocxvwwaaqqxecmzhfxhb"
VITE_SUPABASE_URL="https://ocxvwwaaqqxecmzhfxhb.supabase.co"
VITE_SUPABASE_PUBLISHABLE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jeHZ3d2FhcXF4ZWNtemhmeGhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2NTEzMjUsImV4cCI6MjA5MTIyNzMyNX0.H1KOp8xOGL1WQp9PL8LtAsQ4gN3taWAlpF5dnlaWyRI"
```

---

## 2. Componentes que fazem queries ao Supabase

| Arquivo | Tabelas usadas | Operacoes |
|---------|---------------|-----------|
| `src/hooks/useContainers.ts` | containers | SELECT, INSERT, UPDATE, DELETE |
| `src/hooks/useContainersPaginated.ts` | containers | SELECT (paginado) |
| `src/hooks/useDocuments.ts` | documents | SELECT, INSERT, DELETE |
| `src/hooks/useUpdateDocumentTag.ts` | documents | UPDATE |
| `src/hooks/useFinance.ts` | finance_pagamentos, finance_numerario_itens | SELECT, INSERT, UPDATE |
| `src/hooks/useAutoCreatePayments.ts` | finance_pagamentos | INSERT |
| `src/hooks/useConferenciaNumerario.ts` | conferencias_numerario | SELECT, INSERT, UPDATE |
| `src/hooks/useConferenciasPaginated.ts` | conferencias_numerario | SELECT (paginado) |
| `src/hooks/useReferenciasNCM.ts` | referencias_ncm | SELECT |
| `src/hooks/useReferenciasMercado.ts` | referencias_mercado | SELECT |
| `src/hooks/useMilestones.ts` | container_milestones | SELECT |
| `src/hooks/useTerminal49.ts` | containers, vessel_tracking | SELECT, UPDATE |
| `src/hooks/useVesselTracking.ts` | vessel_tracking | SELECT |
| `src/hooks/useContainerMap.ts` | containers, vessel_tracking | SELECT |
| `src/hooks/useMapboxToken.ts` | — | Edge Function call |
| `src/hooks/useFetchNCMAliquotas.ts` | — | Edge Function call |
| `src/contexts/AuthContext.tsx` | auth.users | Supabase Auth |

---

## 3. Storage (documentos)

| Uso | Arquivo | Bucket |
|-----|---------|--------|
| Upload de documentos | `src/components/DocumentUploadZone.tsx` | container-documents |
| Download/visualizacao | `src/components/container-detail/DocumentsTab.tsx` | container-documents |

**ATENCAO:** Os `file_url` na tabela `documents` apontam para o storage do projeto ANTIGO (`usfilmvbckfnbfnpvrph`). Apos a reconexao:
- Novos uploads vao para o novo storage automaticamente
- Documentos antigos continuam acessiveis via URL publica do antigo (se o bucket for publico)
- Para migrar documentos antigos: download de cada arquivo + re-upload no novo bucket + update dos URLs na tabela

---

## 4. Edge Functions chamadas pelo frontend

| Hook | Edge Function | Metodo |
|------|--------------|--------|
| useFetchNCMAliquotas | fetch-ncm-aliquotas | supabase.functions.invoke |
| useMapboxToken | get-mapbox-token | supabase.functions.invoke |
| useTerminal49 | terminal49-search, terminal49-fetch-shipment, terminal49-associate | supabase.functions.invoke |
| useConferenciaNumerario | extract-import-document, calculate-tax-references | supabase.functions.invoke |
| useReferenciasMercado | fetch-market-references | supabase.functions.invoke |

---

## 5. Auth

O projeto usa Supabase Auth (conferencias_numerario tem `user_id` referenciando `auth.users`).

**Acao necessaria:**
- Criar usuarios no novo projeto Supabase Auth
- Ou migrar usuarios via Admin API
- RLS de conferencias depende de `auth.uid()`

---

## 6. Checklist de reconexao

1. [ ] Configurar todos os secrets das Edge Functions no novo projeto
2. [ ] Deploy das 17 Edge Functions (`supabase functions deploy --all`)
3. [ ] Testar cada Edge Function individualmente
4. [ ] Atualizar `.env` com novas credenciais
5. [ ] Atualizar `supabase/config.toml` com novo project_id
6. [ ] Regenerar `types.ts` (`supabase gen types typescript`)
7. [ ] Criar usuario(s) no Supabase Auth do novo projeto
8. [ ] Testar fluxos: criar container, upload doc, pagamentos, tracking, conferencias
9. [ ] Migrar arquivos do storage (ou manter dual-access temporario)
10. [ ] Atualizar URLs dos documentos na tabela `documents` (se migrar storage)
11. [ ] Rebuild e deploy do frontend com novas env vars

---

*Documentado em 08/04/2026 por Kobe via Claude Code*

---

## Ver também

- [[memory/projects/gb-import-hub-schema|GB Import Hub — Schema Completo do Banco de Dados]]
- [[memory/projects/gb-import-hub-edge-functions-map|GB Import Hub — Edge Functions Map]]

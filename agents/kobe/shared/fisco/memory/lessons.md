# Lições — [[agents/fisco/IDENTITY|Fisco]]

## 2026-03-31 — NFs Venda Interna Março/2026

### [ESTRATÉGICA] L1: Regra fiscal na Natureza de Operação é PRÉ-REQUISITO
A API do Bling NÃO aplica tributação a partir do payload da NF. Ela lê a regra fiscal configurada na **Natureza de Operação** no painel web.
- Sem a regra → API ignora CFOP, ICMS, PIS, COFINS do payload completamente
- Com a regra → Bling preenche automaticamente ao criar a NF
- **Fluxo correto:** configurar 1x no painel → depois só criar NF via API sem impostos
- A Filial não tinha regra configurada → causou horas de investigação. Corrigido manualmente pelo Pedro.

### [ESTRATÉGICA] L2: Não enviar CFOP/ICMS no payload da NF via API
Enviar apenas: `codigo`, `quantidade`, `valor`, `classificacaoFiscal` (NCM), `origem`
- CFOP/ICMS/PIS/COFINS no payload são ignorados pelo Bling
- Deixar o Bling calcular a partir da natureza de operação

### [ESTRATÉGICA] L3: Contatos devem existir na conta Bling EMITENTE
Ao criar NF em uma conta nova (ex: Filial emitindo pela primeira vez pros CNPJs Simples):
- Os destinatários podem não existir como contatos na conta emitente
- Verificar via GET /contatos?pesquisa={cnpj} antes de criar NF
- Criar via POST /contatos se não existirem

### [ESTRATÉGICA] L4: Bug da Filial no OAuth era falta de redirect_uri no token exchange
O erro 403 "empresa inativa" no refresh da Filial NÃO era problema da conta.
- *Causa raiz real:* o token exchange (code → access_token) não incluía redirect_uri no payload
- Sem redirect_uri, o Bling retornava tokens que falhavam no refresh subsequente
- *Correção (01/04):* callback server atualizado para incluir redirect_uri + suporte state=matriz/filial
- Refresh tokens agora funcionam normalmente para AMBAS as contas
- Lição anterior sobre "empresa inativa" estava ERRADA — era bug no nosso código, não no Bling

### [TÁTICA] L5: Fluxo correto de emissão via API (pós-aprendizado 31/03)
1. Verificar token válido → renovar se necessário
2. Verificar se destinatário existe em /contatos → criar se não existir
3. Verificar regra fiscal na Natureza de Operação (1x, não precisa verificar toda vez)
4. Criar NF via POST /nfe SEM campos de impostos no payload
5. Bling preenche tributação automaticamente
6. Emitir via POST /nfe/{id}/enviar
7. Baixar XML

### [TÁTICA] L6: Excedente de estoque vai pela Matriz (CFOP 6102, ICMS 4%)
Quando vendas de um produto superam o estoque transferido pelas NFs de transferência:
- O excedente é faturado pela Matriz (10% retido + estoque contábil)
- CFOP 6102 (interestadual SC→SP), ICMS 4% (importados Res. Senado 13/2012)
- Isso aconteceu em março com pote 800ml (394 un excedente) e 1520ml (883 un excedente)

### [TÁTICA] L7: Decompor kits ao calcular distribuição
Kits são unidades compostas. Para calcular distribuição por produto:
- KIT2YW1520 = 2 potes 1520ml
- KIT4YW1520 = 4 potes 1520ml
- Sempre decompor antes de cruzar com estoque transferido

### [ESTRATÉGICA] L8: Tokens Bling devem ter sync duplo (JSON local + Supabase)
Desde 01/04/2026, refresh-tokens.py salva tokens em JSONs locais E na tabela marketplace_tokens do Supabase (projeto Budamix).
- Matriz: platform=bling, seller_id=58151616000143
- Filial: platform=bling_filial, seller_id=58151616000224
- Se o refresh falhar 2x seguidas → alerta automático via WhatsApp pro Pedro (com link de re-autorização se invalid_grant)
- Contador de falhas em failures.json (reseta ao sucesso)
- Migração planejada: token management sairá do cron Kobe → workflow N8N dedicado (refresh 4h + health check 1h)

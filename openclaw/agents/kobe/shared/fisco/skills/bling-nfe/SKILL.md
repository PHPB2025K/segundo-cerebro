---
title: "SKILL"
created: 2026-04-14
type: skill-definition
agent: kobe
status: active
tags:
  - agent/kobe
---

# SKILL — Emissão de NF-e via Bling API v3 — [[openclaw/agents/fisco/IDENTITY|Fisco]]

## Objetivo
Criar, validar e emitir Notas Fiscais Eletrônicas (NF-e) via API v3 do Bling. Suporta NF de transferência (Módulo B), NF de venda interna (Módulo C), NF de entrada (importação) e NF de remessa.

## Quando usar
- Fisco precisa criar NF de transferência (Matriz SC → Filial SP)
- Fisco precisa criar NF de venda interna (Filial → CNPJs Simples)
- Fisco precisa registrar NF de entrada (importação via Open Trade)
- Qualquer cenário de emissão de NF-e via API

## Credenciais
- Tokens: `/root/.openclaw/workspace/scripts/bling-oauth/tokens-{matriz|filial}.json`
- Auto-refresh: cron a cada 5h (`Bling Token Refresh`)
- Contas: Matriz (CNPJ 58.151.616/0001-43, Itajaí/SC) e Filial (CNPJ 58.151.616/0002-24, Pedreira/SP)

## Endpoints

| Método | Endpoint | Função |
|--------|----------|--------|
| POST | `/nfe` | Criar NF-e (rascunho pendente) |
| GET | `/nfe/{id}` | Consultar NF-e |
| PUT | `/nfe/{id}` | Atualizar NF-e pendente |
| DELETE | `/nfe/{id}` | Deletar NF-e pendente |
| POST | `/nfe/{id}/enviar` | Enviar NF-e para SEFAZ (autorizar) |
| GET | `/nfe?pagina=1&limite=100` | Listar NF-e |
| GET | `/produtos/{id}` | Dados do produto (NCM, preço, unidade) |
| GET | `/contatos/{id}` | Dados do destinatário |
| GET | `/depositos` | Listar depósitos de estoque |
| GET | `/estoques/saldos` | Saldos de estoque |

## Rate Limits
- Bling API v3: 3 requests/segundo por conta
- Em caso de 429: aguardar 2 segundos e retry (máx 3 tentativas)

---

## ⚠️ REGRA CRÍTICA — Aprendizado 31/03/2026

**NÃO enviar CFOP, ICMS, PIS, COFINS no payload da NF.** O Bling ignora esses campos via API.
O Bling preenche tributação **automaticamente a partir da regra fiscal configurada na Natureza de Operação** (painel web).

**Pré-requisito obrigatório (configurar 1x no painel, não via API):**
- Bling → Preferências → Notas Fiscais → Naturezas de Operação → "Venda de mercadoria"
- Aba ICMS: CFOP 5102 (SP interna), CST 00, Alíquota 18%
- Sem essa regra → a API cria NF sem tributação e a SEFAZ rejeita

**Payload de item correto (mínimo necessário):**
```json
{
  "codigo": "YW1520ML",
  "descricao": "Pote de Vidro 1520ml",
  "unidade": "UN",
  "quantidade": 100,
  "valor": 52.50,
  "classificacaoFiscal": "70134900",
  "origem": 2
}
```
Não incluir: `cfop`, `impostos`, `icms`, `pis`, `cofins`, `cst`

---

## Fluxo Obrigatório de Emissão

```
1. [Se venda interna] Executar Motor de Distribuição (Módulo A) ANTES
2. Verificar token Bling válido → renovar se necessário (atenção: bug refresh Filial)
3. Verificar se destinatários existem em GET /contatos?pesquisa={cnpj} → criar via POST se não
4. Confirmar que regra fiscal está configurada na Natureza de Operação (1x, verificação manual)
5. Validar preço de custo (Supabase fulfillment_inventory ou planilha)
6. Montar payload SEM campos de impostos (Bling preenche automaticamente)
7. POST /nfe → cria rascunho (situacao=1)
8. Registrar no log de auditoria (nfe-log.md)
9. Notificar Pedro no Telegram: "NF #{numero} criada como rascunho"
10. Pedro confere no Bling → aprova ou reprova
11. Aprovado → POST /nfe/{id}/enviar → registrar no log
12. Reprovado → DELETE /nfe/{id} → registrar motivo → criar v2 (máx 3 tentativas)
```

**REGRA INVIOLÁVEL:** NUNCA chamar `/nfe/{id}/enviar` sem aprovação explícita do Pedro. Rascunho = seguro. Emissão = irreversível.

---

## IDs de Referência — GB Importadora

| Entidade | ID Bling | CNPJ | Conta | Tipo |
|----------|----------|------|-------|------|
| Filial (destinatário) | 17300144824 | 58.151.616/0002-24 | Matriz | Destinatário transferência |
| GB Comércio | 17474164026 | 07.194.128/0001-82 | Matriz | Destinatário venda interna |
| Trades Up | 17474215109 | 45.200.547/0001-79 | Matriz | Destinatário venda interna |
| Broglio | 17474207056 | 63.922.116/0001-06 | Matriz | Destinatário venda interna |
| **GB Comércio** | **18049415386** | 07.194.128/0001-82 | **Filial** | Destinatário venda interna |
| **Trades Up** | **18049415397** | 45.200.547/0001-79 | **Filial** | Destinatário venda interna |
| **Broglio** | **18049415404** | 63.922.116/0001-06 | **Filial** | Destinatário venda interna |
| Rodonaves (transportadora) | 17459670306 | 44.914.992/0001-38 | Ambas | Transportadora |
| Nat. Op. "Transferência" | 15107242313 | — | Matriz | Natureza de operação |
| Depósito Geral (Matriz) | 14888164579 | — | Matriz | Depósito |
| Depósito Geral (Filial) | 14888246404 | — | Filial | Depósito |

### IEs dos destinatários (Simples Nacional)
| Empresa | CNPJ | IE |
|---------|------|-----|
| GB Comércio | 07.194.128/0001-82 | 519097120117 |
| Trades | 45.200.547/0001-79 | 519087807114 |
| Broglio | 63.922.116/0001-06 | 519001780113 |

### Mapeamento CNPJ × Marketplace (confirmado Pedro 31/03)
| CNPJ | Empresa | Marketplaces |
|------|---------|-------------|
| 07.194.128/0001-82 | GB Comércio | ML + Amazon + Shopee shop_id 448649947 |
| 45.200.547/0001-79 | Trades | Shopee shop_id 860803675 |
| 63.922.116/0001-06 | Broglio | Shopee shop_id 442066454 |

---

## Situações (status da NF-e)

| Código | Significado | Ação possível |
|--------|------------|---------------|
| 1 | Pendente (rascunho) | Editar, deletar, enviar |
| 2 | Cancelada | — |
| 6 | Autorizada (SEFAZ) | Irreversível |
| 7 | Denegada | Investigar motivo |
| 9 | Rejeitada | Corrigir e reenviar |

---

## Payload Completo — Campos Obrigatórios

### Header

```json
{
  "tipo": 1,
  "serie": 1,
  "dataOperacao": "2026-03-30 18:45:00",
  "naturezaOperacao": { "id": 15107242313 },
  "loja": { "id": 0 }
}
```

| Campo | Obrigatório | Notas |
|-------|-------------|-------|
| `tipo` | ✅ | 1 = Saída, 0 = Entrada |
| `serie` | ✅ | Geralmente 1 |
| `dataOperacao` | ✅ | "YYYY-MM-DD HH:MM:SS" — data REAL, nunca futura |
| `naturezaOperacao.id` | ✅ | ID da natureza cadastrada no Bling |

### Destinatário — SEÇÃO CRÍTICA

**🚨 A API do Bling NÃO puxa dados do contato pelo ID automaticamente. TODOS os campos devem ser enviados explicitamente.**

```json
{
  "contato": {
    "id": 17300144824,
    "nome": "GB IMPORTADORA E COMERCIO LTDA",
    "tipoPessoa": "J",
    "numeroDocumento": "58151616000224",
    "ie": "519129848113",
    "contribuinte": 1,
    "endereco": {
      "endereco": "AVENIDA PAPA JOAO XXIII",
      "numero": "850",
      "complemento": "",
      "bairro": "JARDIM SAO PEDRO",
      "cep": "13922000",
      "municipio": "PEDREIRA",
      "uf": "SP"
    }
  }
}
```

| Campo | Obrigatório | Valores | Notas |
|-------|-------------|---------|-------|
| `contato.id` | ✅ | ID no Bling | Buscar via GET /contatos?pesquisa={cnpj} |
| `contato.nome` | ✅ | Razão social | **Enviar SEMPRE — API não puxa do cadastro** |
| `contato.tipoPessoa` | ✅ | "J" ou "F" | **"J" para CNPJ, "F" para CPF. NUNCA errar.** |
| `contato.numeroDocumento` | ✅ | CNPJ/CPF sem formatação | Apenas dígitos |
| `contato.ie` | ✅* | Inscrição Estadual | Obrigatório se contribuinte=1 |
| `contato.contribuinte` | ✅ | 1=Contribuinte, 2=Isento, 9=Não contribuinte | Filial/Matriz/GB = 1 |
| `contato.endereco.*` | ✅ | Endereço completo | CEP, UF, município, bairro, rua, número |

### Validação pré-emissão do destinatário (OBRIGATÓRIO)

```python
def validar_destinatario(conta, contato_id):
    """Busca e valida contato antes de criar NF. Retorna dados ou raise."""
    contato = bling_get(conta, f"contatos/{contato_id}")
    d = contato["data"]
    end = d.get("endereco", {}).get("geral", {})
    
    erros = []
    if not d.get("nome"): erros.append("Nome vazio")
    if not d.get("numeroDocumento"): erros.append("CNPJ/CPF vazio")
    if d.get("indicadorIe") == 1 and not d.get("ie"): erros.append("IE obrigatória")
    if not end.get("endereco"): erros.append("Endereço vazio")
    if not end.get("cep"): erros.append("CEP vazio")
    if not end.get("municipio"): erros.append("Município vazio")
    if not end.get("uf"): erros.append("UF vazio")
    if not end.get("numero"): erros.append("Número vazio")
    
    if erros:
        raise Exception(f"Contato {contato_id} incompleto: {', '.join(erros)}")
    
    return {
        "id": contato_id,
        "nome": d["nome"],
        "tipoPessoa": d.get("tipo", "J"),
        "numeroDocumento": d["numeroDocumento"],
        "ie": d.get("ie", ""),
        "contribuinte": d.get("indicadorIe", 1),
        "endereco": {
            "endereco": end["endereco"],
            "numero": end.get("numero", ""),
            "complemento": end.get("complemento", ""),
            "bairro": end.get("bairro", ""),
            "cep": end["cep"],
            "municipio": end["municipio"],
            "uf": end["uf"]
        }
    }
```

### Itens

```json
{
  "itens": [{
    "codigo": "CXIMB501C",
    "descricao": "Caixa Conjunto de 5 Potes, Tampa Cinza 12UN",
    "unidade": "UN",
    "quantidade": 10,
    "valor": 64.88,
    "tipo": "P",
    "pesoBruto": 5.2,
    "pesoLiquido": 4.8,
    "classificacaoFiscal": "7013.49.00",
    "origem": 2,
    "cfop": "6152",
    "gtin": "7898972482954",
    "informacoesAdicionais": ""
  }]
}
```

| Campo | Obrigatório | Notas |
|-------|-------------|-------|
| `valor` | ✅ | **Transferência: preço de CUSTO. Venda interna: custo × 1.05** |
| `pesoBruto` | ✅ | **NUNCA 0 para produtos físicos** — calcular de product-packaging.json |
| `pesoLiquido` | ✅ | **NUNCA 0** |
| `origem` | ✅ | 0=Nacional, 2=Importada merc. interna (GB = maioria 2) |
| `cfop` | ✅ | Ver tabela CFOP |

---

## Dados de Volume — Metodologia Automatizada

### Fonte de dados
Tabela de referência: `shared/fisco/config/product-packaging.json`
Os produtos no Bling NÃO têm peso/dimensões (todos zerados).

### Campos por SKU

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `peso_bruto_unitario_kg` | float | Peso bruto de 1 unidade (kg) |
| `peso_liquido_unitario_kg` | float | Peso líquido de 1 unidade (kg) |
| `unidades_por_volume` | int | Quantas unidades cabem em 1 caixa |
| `especie_volume` | string | "CAIXA", "PALETE", "FARDO" |
| `altura_cm`, `largura_cm`, `comprimento_cm` | float | Dimensões (opcional) |

### Cálculo automático

```python
import math

def calcular_volumes(itens, packaging_db):
    peso_bruto_total = 0
    peso_liquido_total = 0
    qtd_volumes_total = 0
    especie = "CAIXA"
    
    for item in itens:
        sku = item["codigo"]
        pkg = packaging_db.get(sku)
        
        if not pkg or not pkg.get("_preenchido"):
            raise Exception(f"BLOQUEIO: SKU {sku} sem dados de embalagem. Preencher product-packaging.json antes de gerar NF.")
        
        qtd = item["quantidade"]
        pb = pkg["peso_bruto_unitario_kg"] * qtd
        pl = pkg["peso_liquido_unitario_kg"] * qtd
        peso_bruto_total += pb
        peso_liquido_total += pl
        
        # Pesos no item individual
        item["pesoBruto"] = round(pb, 3)
        item["pesoLiquido"] = round(pl, 3)
        
        unid_vol = pkg.get("unidades_por_volume", 1)
        qtd_volumes_total += math.ceil(qtd / unid_vol)
        especie = pkg.get("especie_volume", "CAIXA")
    
    return {
        "quantidade": qtd_volumes_total,
        "especie": especie,
        "pesoBruto": round(peso_bruto_total, 3),
        "pesoLiquido": round(peso_liquido_total, 3)
    }
```

### Regra inviolável
- **NUNCA criar NF com volume=0, peso bruto=0 ou peso líquido=0**
- SKU sem dados → bloqueia emissão e alerta Pedro

### Bloco transporte completo

```json
{
  "transporte": {
    "fretePorConta": 0,
    "transportador": {
      "nome": "RODONAVES TRANSPORTES E ENCOMENDAS LTDA",
      "numeroDocumento": "44914992000138"
    },
    "volumes": [{
      "quantidade": 10,
      "especie": "CAIXA",
      "pesoBruto": 52.0,
      "pesoLiquido": 48.0
    }]
  }
}
```

---

## Preço de Transferência Automatizado

### Fonte de preço por tipo de NF

| Tipo NF | CFOP | Regra de preço | Fonte |
|---------|------|----------------|-------|
| Transferência SC→SP | 6152 | Custo nacionalizado da DI | `fulfillment_inventory.cost_price` (Supabase) ou planilha Google Sheets (sync-costs.py) |
| Venda interna Filial→Simples | 5102 | Custo nacionalizado × 1.05 | `tax-rules.json.internal_sale_filial_simples.margin_pct` = 5% |
| Venda interestadual | 6102 | Preço de venda | Cadastro do produto no Bling |

### Validação
```python
def obter_preco(sku, tipo_nf):
    # Buscar cost_price no Supabase
    # Se não encontrar → BLOQUEAR e alertar Pedro
    if cost_price is None or cost_price == 0:
        raise Exception(f"BLOQUEIO: SKU {sku} sem preço de custo. Verificar fulfillment_inventory ou planilha de custos.")
    
    if tipo_nf == "transferencia":
        return cost_price
    elif tipo_nf == "venda_interna":
        return round(cost_price * 1.05, 2)
```

Referência: `shared/fisco/config/tax-rules.json`

---

## Validação de Estoque Pré-Emissão

Antes de criar o rascunho:
```python
def validar_estoque(conta, itens):
    saldos = bling_get(conta, "estoques/saldos?pagina=1&limite=200")
    estoque_map = {s["produto"]["codigo"]: s["saldoFisico"] for s in saldos.get("data", [])}
    
    erros = []
    for item in itens:
        sku = item["codigo"]
        disponivel = estoque_map.get(sku, 0)
        if disponivel < item["quantidade"]:
            erros.append(f"SKU {sku}: tem {disponivel}, NF pede {item['quantidade']}")
    
    if erros:
        raise Exception(f"ESTOQUE INSUFICIENTE: {'; '.join(erros)}")
```

Adicionar ao checklist: `- [ ] Estoque suficiente no depósito de origem`

---

## TTD 409 — Integrado na Emissão

Referência: `shared/fisco/config/tax-rules.json → ttd_409`

| Período | Taxa efetiva ICMS |
|---------|-------------------|
| Até 01/2029 (Fase 1) | 2,6% |
| Após 01/2029 (Fase 2) | 1,0% |

### Aplicação na NF de transferência (6152)
- A alíquota interestadual genérica para importados é 4% (Res. Senado 13/2012)
- O TTD 409 concede crédito presumido que **reduz a carga efetiva** para 2,6%
- Na NF, o ICMS destacado deve refletir a carga efetiva do TTD

### Campos na NF
- CST: verificar com Suellen qual CST usar (020, 051, ou outro)
- Informações complementares: mencionar TTD 409 (ver seção Info Complementares)
- Benefício fiscal: campo específico se o Bling suportar

**⚠️ PENDENTE VALIDAÇÃO:** Suellen precisa confirmar como o TTD 409 aparece no XML da NF-e antes de implementar. Até lá, usar alíquota 4% padrão e Suellen ajusta manualmente se necessário.

---

## Informações Complementares — Templates por CFOP

### Templates automáticos

| CFOP | Template |
|------|---------|
| 6152 | "Transferência de mercadoria entre estabelecimentos do mesmo contribuinte. Mercadoria importada por Conta e Ordem via Open Trade Itajaí-SC. Benefício TTD 409/SC — carga efetiva ICMS 2,6%." |
| 5152 | "Transferência de mercadoria entre estabelecimentos do mesmo contribuinte." |
| 5102 | "Venda de mercadoria adquirida de terceiros. Preço interno: custo nacionalizado × 1,05." |
| 6102 | "Mercadoria de origem estrangeira — alíquota interestadual 4% conforme Res. Senado 13/2012." |
| 5405 | "ICMS recolhido antecipadamente por substituição tributária." |

### Tributos aproximados (OBRIGATÓRIO — Lei 12.741/2012)
Sempre incluir:
```
"Valor aproximado dos tributos: R$ {valor} ({pct_federal}% Federal, {pct_estadual}% Estadual). Fonte: IBPT."
```
O Bling calcula via integração IBPT se configurado. Caso contrário, usar campo `informacoesAdicionais` no item.

### Campo no payload
```json
{
  "informacoesComplementares": "Transferência de mercadoria entre estabelecimentos..."
}
```

---

## NF de Entrada (Importação)

### Fluxo
1. Mercadoria chega via Open Trade (Itajaí/SC) → Open Trade emite NF de importação (Conta e Ordem)
2. Fisco registra a entrada no Bling da Matriz (POST /nfe com `tipo=0`)
3. Entrada alimenta o estoque contábil e é pré-requisito para NF de transferência

### Como o Fisco sabe que a entrada foi registrada
- Verificar GET /nfe?tipo=0 na Matriz por NFs de entrada recentes
- Se não houver entrada correspondente ao lote que será transferido → alertar Pedro
- A NF de entrada pode ser registrada manualmente pelo contador (Suellen) — nesse caso, Fisco apenas verifica existência

### Campos específicos da NF de entrada
```json
{
  "tipo": 0,
  "naturezaOperacao": { "id": "<id_nat_entrada>" },
  "contato": { "id": "<id_open_trade>" },
  "chaveAcesso": "<chave_acesso_nf_importacao>"
}
```

---

## Integração com Motor de Distribuição (Módulo A)

### Pré-requisito para NFs de venda interna (Filial → Simples)

**ANTES** de criar NFs de venda interna, o Fisco DEVE:
1. Executar Motor de Distribuição (`shared/fisco/skills/distribution/SKILL.md`)
2. Obter output: proporções de estoque por CNPJ (GB Comércio, Trades, Broglio)
3. Usar essas proporções para definir quantidades em cada NF

### Regras de distribuição (de tax-rules.json)
- GB Comércio (07.194.128): até R$360k/mês (Simples Nacional)
- Trades Up (45.200.547): até R$360k/mês
- Broglio (63.922.116): até R$360k/mês

O Motor de Distribuição calcula a divisão ideal respeitando os limites do Simples Nacional.

---

## Controle de Versão de Rascunhos

### Quando Pedro reprova um rascunho
1. Registrar no log: "NF #{numero} v1 reprovada. Motivo: {motivo}"
2. Deletar o rascunho: `DELETE /nfe/{id}`
3. Corrigir payload conforme feedback
4. Criar novo rascunho: `POST /nfe` → nova versão (v2)
5. Registrar: "NF #{numero_novo} v2 criada. Correção: {o_que_mudou}"

### Limite
- Máximo 3 tentativas por NF antes de escalar pra Suellen
- Se chegar na v3 e Pedro ainda reprovar → parar e chamar Suellen pra revisar a operação fiscal

---

## Log de Auditoria Fiscal

Arquivo: `shared/fisco/memory/nfe-log.md` (append-only)

### Formato

```markdown
| Data/Hora | Tipo | NF# | Valor | Destinatário | CFOP | Status | Aprovador | Obs |
|-----------|------|-----|-------|-------------|------|--------|-----------|-----|
| 2026-03-30 18:45 | Transferência | 613 | R$690,97 | Filial (0002-24) | 6152 | Rascunho | — | Teste |
```

### Eventos registrados
- Rascunho criado (v1, v2, v3)
- Aprovado por Pedro/Suellen
- Emitido (autorizado SEFAZ) + chave de acesso
- Rejeitado SEFAZ + motivo
- Reprovado Pedro + motivo
- Deletado

---

## Tabela CFOP — Operações da GB

| CFOP | Descrição | Quando usar |
|------|-----------|-------------|
| **6152** | Transferência mercadoria terceiros (interestadual) | **Matriz SC → Filial SP** |
| 5152 | Transferência mercadoria terceiros (intraestadual) | Dentro de SP |
| 6151 | Transferência produção própria (interestadual) | MDF SC → SP |
| 5102 | Venda mercadoria (intraestadual) | Filial SP → clientes SP |
| 6102 | Venda mercadoria (interestadual) | Filial SP → outros estados |
| 5405 | Venda com ST já retida | Quando ICMS-ST já pago |

## ICMS — Regras por operação

| Operação | Origem | UF | Alíquota | Nota |
|----------|--------|-----|----------|------|
| Transferência importados | 2 | SC→SP | 2,6% (TTD 409) | Pendente validação Suellen |
| Transferência nacionais | 0 | SC→SP | 12% | Padrão interestadual |
| Venda interna SP | 2 | SP→SP | 18% | ICMS interno |
| Venda interestadual | 2 | SP→Sul/SE | 4% | Importados (Res. 13/2012) |

---

## Checklist Pré-Emissão (OBRIGATÓRIO)

- [ ] **Motor de Distribuição executado** (se venda interna)
- [ ] **Estoque suficiente** no depósito de origem (GET /estoques/saldos)
- [ ] **Dados de embalagem** preenchidos no product-packaging.json
- [ ] **Preço de custo** encontrado (Supabase ou planilha)
- [ ] **Destinatário completo:** nome, tipoPessoa, CNPJ, IE, endereço (todos os campos)
- [ ] **tipoPessoa:** "J" para CNPJ, "F" para CPF — NUNCA errar
- [ ] **contribuinte:** 1 se tem IE, 9 se não tem
- [ ] **CFOP correto** para a operação
- [ ] **Origem do produto:** 0=nacional, 2=importado
- [ ] **NCM** preenchido (8 dígitos)
- [ ] **Peso bruto e líquido:** NUNCA 0
- [ ] **Volumes:** quantidade, espécie, pesos — NUNCA 0
- [ ] **Transportadora:** nome e CNPJ
- [ ] **Informações complementares:** template por CFOP + tributos IBPT
- [ ] **Data de operação:** real, nunca futura
- [ ] **NF de entrada registrada** (se transferência: verificar entrada correspondente)

---

## Erros Comuns e Soluções

| Erro | Causa | Solução |
|------|-------|---------|
| Destinatário vazio no Bling | `tipoPessoa`/nome não enviados | Enviar TODOS os campos do contato explicitamente |
| tipoPessoa = "Física" com CNPJ | `tipoPessoa` não enviado (default "F") | Sempre enviar `"tipoPessoa": "J"` |
| SEFAZ: "Destinatário sem endereço" | Endereço vazio no payload | Puxar do cadastro do contato e enviar explicitamente |
| Peso bruto/líquido = 0 | Não calculado | Usar product-packaging.json |
| Volumes = 0 | Não enviado | Calcular com calcular_volumes() |
| 429 Too Many Requests | >3 req/s | Sleep 2s entre requisições |
| 403 Empresa inativa (refresh) | Bug Bling Filial | Re-autorizar via OAuth |
| Preço de custo = 0 | SKU sem cost_price | Verificar fulfillment_inventory ou planilha |
| Estoque insuficiente | Transferência > saldo | Alertar Pedro antes de criar NF |

---

## Referências
- API v3 Bling: https://developer.bling.com.br/referencia
- Regras fiscais: `shared/fisco/config/tax-rules.json`
- Embalagens: `shared/fisco/config/product-packaging.json`
- Motor de Distribuição: `shared/fisco/skills/distribution/SKILL.md`
- NF real de referência: #000600 (emitida 04/03/2026, CFOP 6152, R$34.410,42)
- Log de auditoria: `shared/fisco/memory/nfe-log.md`

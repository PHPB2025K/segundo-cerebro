# Decisões — [[agents/fisco/IDENTITY|Fisco]]

## 2026-03-31 — Emissão NFs Venda Interna Março/2026

### D1: Mapeamento CNPJ × Marketplace (confirmado Pedro 31/03)
| CNPJ | Empresa | Marketplaces |
|------|---------|-------------|
| 07.194.128/0001-82 | GB Comércio | ML + Amazon + Shopee 1 (shop_id 448649947) |
| 45.200.547/0001-79 | Trades | Shopee 2 (shop_id 860803675) |
| 63.922.116/0001-06 | Broglio | Shopee 3 (shop_id 442066454) |

### D2: Lógica de distribuição NF interna (31/03)
- Cruzar NFs de transferência (598, 600) com vendas por marketplace
- Decompor kits em unidades individuais (ex: KIT2YW1520 = 2 potes 1520ml)
- Apenas produtos importados (NCM 7013.49.00)
- Vendido dentro do limite transferido → NF Filial (CFOP 5102, ICMS 18%)
- Excedente → NF Matriz (CFOP 6102, ICMS 4%)

### D3: Não enviar impostos no payload da API Bling (31/03)
- O Bling preenche CFOP/ICMS/PIS/COFINS automaticamente a partir da regra fiscal da Natureza de Operação
- Enviar apenas: código do produto, quantidade, valor, NCM, origem
- Regra fiscal na natureza é OBRIGATÓRIA (sem ela a API ignora tributação)

### D4: Contatos devem existir na conta Bling emitente (31/03)
- Criar via API POST /contatos se não existirem antes de criar NF

## Regra Universal — Horários em Brasília (2026-04-01)
TODOS os horários apresentados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de exibir. Vale para relatórios, alertas, logs, timestamps — qualquer comunicação.


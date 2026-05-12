# Regras Operacionais — Daily Sales Report v2

## Regras Aprovadas

### Escopo e Dados
- **Atacado/Bling NÃO entra** no Slack dos funcionários — apenas vendas marketplace.
- `v_daily_sales` é usada apenas para o **resumo geral**; análise por conta usa tabela `orders` filtrada por `shop_id`.
- Fuso horário: **BRT 00:00–23:59** (UTC-3).
- Não misturar settlement/extrato/DRE com venda gerada — são domínios diferentes.
- Se dados de uma conta estiverem incompletos, marcar como **parcial** e **não estimar**.

### Shopee
- Shopee é **sempre analisada por conta separada** (3 contas distintas).
- Cada conta Shopee tem shop_id próprio e deve ser tratada como unidade independente.

### Mensagens Slack
- Mensagens individuais por responsável:
  - **Lucas** → Shopee (3 contas)
  - **Yasmin** → Mercado Livre
  - **Leonardo** → Amazon
- Todas as mensagens em **bullets**.
- Resumo geral igual para todos no topo da mensagem.

### Processo Analítico
- Registrar análise interna diária **antes** da mensagem externa.
- A análise interna é mais profunda que o Slack — inclui hipóteses, comparações e contexto.
- Comparações obrigatórias: 30d, 60d, mesmo dia da semana.
- Identificar SKUs/produtos que explicam variações.
- Registrar hipóteses e verificar nas análises seguintes.

### Governança
- Regras permanentes precisam de evidência para serem criadas.
- Revisão periódica das regras (expiração quando aplicável).
- Kobe valida qualidade; Pedro aprova direcionamentos estratégicos.

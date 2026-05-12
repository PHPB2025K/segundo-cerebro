# Daily Sales Report v2 — Memória Analítica em Camadas

## Objetivo
Esta estrutura persiste a memória analítica do Trader para o Daily Sales Report v2. Ela permite análises diárias profundas por conta sem sobrecarregar o contexto de cada execução.

A memória interna aqui é **mais profunda** que a mensagem Slack enviada aos responsáveis. O Slack recebe um resumo acionável; aqui ficam hipóteses, padrões, evidências e teses estratégicas.

## Unidades Operacionais

| Conta | Plataforma | Identificador | Responsável | ADS |
|-------|-----------|---------------|-------------|-----|
| Budamix Store | Shopee | shop_id `448649947` | Lucas | Himmel |
| Budamix Oficial (Conta 2) | Shopee | shop_id `860803675` | Lucas | Himmel |
| Budamix Shop (Conta 3) | Shopee | shop_id `442066454` | Lucas | Himmel |
| Mercado Livre | Mercado Livre | conta única | Yasmin | Himmel |
| Amazon | Amazon | conta única | Leonardo | Pedro |

## Relação com Daily Sales Report v2
Este diretório é a **fundação de memória** do relatório diário. Cada execução:
1. Lê a análise diária anterior da conta.
2. Lê a consolidação semanal vigente.
3. Lê a tese mensal vigente.
4. Lê as regras permanentes da conta.
5. Processa dados novos do dia.
6. Gera nova análise diária.
7. Produz mensagem Slack resumida.

## Camadas

| Camada | Frequência | Conteúdo |
|--------|-----------|----------|
| Diária | Todo dia | Análise bruta detalhada por conta |
| Semanal | Toda segunda | Consolidação de padrões por conta |
| Mensal | Dia 1 | Tese estratégica por conta |
| Permanente | Quando confirmada | Regras aprendidas por conta |

## Governança

| Papel | Responsabilidade |
|-------|-----------------|
| **Trader** | Dono operacional — executa análises, mantém memória, gera relatórios |
| **Kobe** | QA/governança — valida qualidade, aprova regras permanentes |
| **Builder** | Implementa automações, cron, integrações técnicas |

## Estrutura de Diretórios
```
accounts/
  {conta}/
    README.md          — contexto da conta
    daily/             — análises diárias (1 arquivo por dia)
    weekly.md          — consolidação semanal vigente
    monthly.md         — tese mensal vigente
    rules.md           — regras permanentes da conta
templates/             — modelos para cada tipo de documento
```

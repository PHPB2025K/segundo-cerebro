# Responsáveis — Daily Sales Analyst

## Operação por canal

| Canal | Responsável operacional | Responsável ADS | Acionamento ADS |
|-------|------------------------|-----------------|-----------------|
| Shopee (3 contas) | Lucas | Himmel | Via Lucas |
| Mercado Livre | Yasmin | Himmel | Via Yasmin |
| Amazon | Leonardo | Pedro | Via Leonardo |

## Governança

| Papel | Agente | Responsabilidade |
|-------|--------|-----------------|
| Decisor humano final | Pedro | Decisão final, ADS Amazon |
| Governança/QA final | Kobe | Validação de rollout, bloqueios, mudanças estratégicas, checkpoints |
| Dono/Orquestrador | Trader | Aciona DSA, recebe retorno, envia Slack, valida memória |
| Executor | DSA | Executa pipeline analítico, devolve artefatos ao Trader |
| Gestão ADS Shopee/ML | Himmel | Verba, segmentação, criativos, lances, exposição, afiliados/cupons Shopee |

## Regras de acionamento

- Himmel nunca é acionado diretamente pelo DSA — sempre via Lucas (Shopee) ou Yasmin (ML).
- Pedro nunca é acionado diretamente pelo DSA — sempre via Leonardo, após validação de pré-requisitos.
- Kobe é acionado para decisões estruturais, conflitos e checkpoints.
- DSA nunca fala com Pedro diretamente. Toda comunicação passa por Trader ou Kobe.

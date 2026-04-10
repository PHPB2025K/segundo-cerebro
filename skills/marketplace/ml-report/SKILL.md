---
name: ml-report
description: Gerar relatórios profissionais de performance do Mercado Livre com visual premium. Use quando Pedro pedir relatório ML, análise de performance, métricas de vendas, conversão, reputação, ads ou qualquer análise da conta de seller. Suporta relatório completo (9 páginas), focado (seções específicas) e comparativo (entre períodos).
---

# ml-report — Relatório de Performance ML

Gera relatórios PDF profissionais da conta GB Importadora / Budamix no Mercado Livre.  
Visual premium, dados reais da API, exportação direta para PDF via wkhtmltopdf.

## Dependências

```bash
pip install matplotlib requests jinja2
apt-get install -y wkhtmltopdf  # ou: snap install wkhtmltopdf
```

Verificar instalação:
```bash
wkhtmltopdf --version
python3 -c "import matplotlib, requests, jinja2; print('OK')"
```

## Uso básico

```bash
# Relatório completo (todas as 9 seções)
python3 {baseDir}/scripts/ml-report.py --inicio 2026-03-01 --fim 2026-03-15

# Seções específicas
python3 {baseDir}/scripts/ml-report.py --inicio 2026-03-01 --fim 2026-03-15 --secoes 1,2,6

# Com output personalizado
python3 {baseDir}/scripts/ml-report.py --inicio 2026-03-01 --fim 2026-03-15 --output /tmp/relatorio.pdf

# Modo debug (logs detalhados)
python3 {baseDir}/scripts/ml-report.py --inicio 2026-03-01 --fim 2026-03-15 --debug
```

## Parâmetros

| Param | Obrigatório | Default | Descrição |
|---|---|---|---|
| `--inicio` | Sim | — | Data inicial (YYYY-MM-DD) |
| `--fim` | Sim | — | Data final (YYYY-MM-DD) |
| `--secoes` | Não | `all` | Seções separadas por vírgula: `1,2,3` ou `all` |
| `--output` | Não | `~/workspace/reports/relatorio-ml-{inicio}-{fim}.pdf` | Caminho do PDF gerado |
| `--debug` | Não | False | Ativa logging detalhado e salva HTML intermediário |

## Seções disponíveis

| # | Nome |
|---|---|
| 1 | Capa & Resumo Executivo |
| 2 | Faturamento & Receita |
| 3 | Volume de Vendas & Conversão |
| 4 | Tráfego & Visibilidade |
| 5 | Publicidade / ML Ads |
| 6 | Reputação & Saúde da Conta |
| 7 | Logística & Envios |
| 8 | Anúncios & Catálogo |
| 9 | Insights Estratégicos & Plano de Ação |

Ver `references/estrutura-relatorio.md` para descrição detalhada de cada seção.

## Tokens e autenticação

- Token vendas (pedidos, anúncios, itens): `/root/.openclaw/.ml-tokens.json`
- Token financeiro (pagamentos, taxas): `/root/.openclaw/.ml-tokens-finance.json`
- Token métricas (reputação): `/root/.openclaw/.ml-tokens-metrics.json`
- Refresh automático antes de cada execução via `ml-refresh-token.sh`

## Identidade visual

Ver `references/paleta-cores.md` para paleta completa Budamix.  
Cor primária: `#174C4C` (teal escuro — cor da assinatura GB).

## Arquitetura

```
ml-report.py      → Engine principal: args, refresh, fetch, render, export
ml-charts.py      → Gerador de gráficos: bar, line, donut, comparison → base64 PNG
report-template.html → Template HTML com CSS embutido, pronto para wkhtmltopdf
```

## Saída esperada

PDF A4, ~9 páginas, com:
- Capa com período e branding Budamix
- Cards KPI coloridos
- Gráficos matplotlib embutidos
- Tabelas profissionais com zebra-striping
- Boxes de insight destacados
- Rodapé: "Budamix · Relatório ML · {periodo} · Página X/Y"

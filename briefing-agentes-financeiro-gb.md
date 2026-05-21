# Briefing rápido — agentes e estrutura atual

## 1) Agentes ativos hoje

Top-level no OpenClaw:

- **Kobe** — COO digital / Diretor Operacional e orquestrador do time
- **Trader** — Especialista sênior de marketplaces: Mercado Livre, Shopee, Amazon
- **Spark** — Gestor sênior de tráfego pago / ADS
- **Builder** — Desenvolvedor full-stack sênior / engenharia de produto
- **Fisco** — Agente de Faturamento e Compliance Fiscal
- **RH** — Gestor de Recursos Humanos / ponto, banco de horas, férias e compliance CLT

Sub-agente já existente:

- **Daily Sales Analyst** — Analista do Daily Sales Report v2; executor analítico do Trader, não fala direto comigo nem com Pedro/equipe.

Minha recomendação para os novos:

- **Diretor Financeiro** → agente top-level, par do Trader/Fisco/RH, reportando ao Kobe.
- **Analista Sênior de Fluxo de Caixa** → sub-agente do Diretor Financeiro, porque ele parece executor especializado, não “diretor de domínio”.

## 2) Hierarquia atual

- **Pedro** — decisor final
  - **Kobe** — coordenação estratégica / interface única com Pedro
    - **Trader** — marketplaces
      - **Daily Sales Analyst** — análise profunda Daily Sales v2
    - **Spark** — ADS / mídia paga
    - **Builder** — dev / sistemas / automações
    - **Fisco** — faturamento / fiscal / compliance
    - **RH** — pessoas / ponto / compliance trabalhista

Hierarquia recomendada com Financeiro:

- **Pedro**
  - **Kobe**
    - **Diretor Financeiro**
      - **Analista Sênior de Fluxo de Caixa**
    - Trader
    - Spark
    - Builder
    - Fisco
    - RH

## 3) Padrão de arquivos de agente principal

Todo agente principal segue, no mínimo:

- **IDENTITY.md** — identidade, nome, cargo/função, escopo, tom, limites
- **SOUL.md** — personalidade operacional, como pensa, responsabilidades, estilo de entrega
- **AGENTS.md** — protocolos, regras de operação, delegação, segurança, memória, rotinas
- **MEMORY.md** — índice de memória do agente, status, pendências, decisões relevantes
- Pasta de **memory/** quando o agente precisa de memória própria estruturada
- Opcionalmente: templates, config, prompts, runs, validation, outputs, etc., se o agente tiver pipeline próprio

Para os novos, eu faria:

- Diretor Financeiro: estrutura completa de agente principal.
- Analista de Fluxo de Caixa: estrutura de sub-agente com IDENTITY, SOUL, AGENTS, MEMORY e uma pasta própria para runs/outputs/validation, se for processar extratos recorrentes.

## 4) Como o Mission Control enxerga agentes

Hoje ele mostra:

- Agentes top-level vindos da lista de agentes configurada no OpenClaw.
- Sub-agentes descobertos automaticamente quando existe um IDENTITY.md dentro da área compartilhada de algum agente-pai.

O nome e cargo vêm principalmente do IDENTITY.md:

- Nome: campo “Nome”
- Cargo/função: campo “Função”, “Papel” ou descrição logo no começo do “Quem é”
- Emoji/cor: inferidos por identidade/role; sub-agente herda a cor do agente-pai
- No organograma: top-level aparecem abaixo do Kobe; sub-agentes aparecem abaixo do parent

Então, se você quer aparecer como:

- “Diretor Financeiro” embaixo do nome → colocar isso explicitamente no IDENTITY.md como Função/Papel.
- “Analista Sênior de Fluxo de Caixa” → idem, no IDENTITY.md do sub-agente.

## 5) Skills: onde ficam e como são acionadas

Skills ficam na pasta de skills do workspace, separadas por domínio. Exemplo lógico:

- skills/financeiro/
- skills/marketplace/
- skills/marketing/
- skills/design/
- skills/operations/

Uma skill dedicada precisa ter:

- Pasta própria com nome claro, tipo “cash-flow-extract-processor”
- Arquivo SKILL.md obrigatório
- Frontmatter com name e description
- Description bem explícita, porque é isso que faz o agente saber quando deve acionar a skill
- Se for frágil/repetitivo, incluir scripts internos na própria skill, em vez de deixar tudo como instrução solta

Para o Analista de Fluxo de Caixa, eu criaria uma skill com gatilhos claros:

- processar extratos bancários
- conciliar entradas/saídas
- classificar categorias
- detectar duplicidades
- gerar projeção de caixa
- apontar risco de saldo, vencimentos e capital de giro

E registraria nos arquivos do agente que toda análise de extrato passa por essa skill.

## 6) Regras/convenções para criar agente novo

- Nome curto e funcional: Financeiro, CFO, Caixa, etc. Eu evitaria nomes abstratos.
- Definir escopo negativo: o que o agente NÃO pode fazer.
- Todo agente novo reporta ao Kobe; não fala direto com Pedro nem terceiros, salvo autorização explícita.
- Ações financeiras reais precisam de aprovação: pagamento, transferência, envio externo, alteração em banco/ERP, cobrança, comunicação com contador/banco.
- Antes de mudança estrutural: backup do workspace/config.
- Depois de criar: atualizar memória central, AGENTS, MEMORY e Mission Control se necessário.
- Se for top-level: precisa entrar na lista de agentes do OpenClaw.
- Se for sub-agente: precisa ficar ligado ao parent certo e declarar isso no IDENTITY.
- Skill nova deve ser enxuta: SKILL.md com workflow essencial; detalhes grandes vão para referências ou scripts.
- Nada de credenciais em arquivos do agente/skill. Segredo fica em 1Password/env, nunca em markdown.

## Sugestão final

Cria o **Diretor Financeiro** como agente principal e o **Analista Sênior de Fluxo de Caixa** como sub-agente dele. Isso deixa a hierarquia limpa e evita lotar o nível principal com executor especializado.

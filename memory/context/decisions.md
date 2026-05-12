---
title: "Decisões"
created: 2026-05-01
type: context
status: active
tags:
  - memory
  - context
  - decisions
---

# Decisões — Índice Operacional

_Este arquivo existe para cumprir o contrato operacional `memory/context/decisions.md`. O histórico detalhado continua em `memory/context/decisoes/`._

## 2026-05-01 — Fechamento financeiro abril/2026

- Relatórios financeiros não devem chamar `SETTLEMENT`/extrato financeiro de faturamento bruto sem qualificador.
- Usar **faturamento bruto comercial** para pedidos válidos do mês e **receita liquidada em extrato** para settlement/financeiro.
- Abril/2026 validado: faturamento comercial R$ 405.839,65; receita liquidada em extrato R$ 354.992,67.
- Para Shopee Ads abril/2026, usar o número oficial de plataforma informado manualmente pelo Pedro: R$ 9.460, vendas via Ads R$ 165.600, ROAS 17,51. Wallet API fica como conciliação/alerta, não como consumo oficial.
- Amazon Ads abril/2026 via API Sponsored Products validado: gasto R$ 2.478,95; vendas atribuídas R$ 11.749,58; ROAS 4,74; ACOS 21,10%.
- DRE da GB deve seguir estrutura clássica completa, não apuração simplificada de marketplace.

## 2026-05-01 — Fiscal / NFs internas abril/2026

- Orientação v2.1 da Suellen/FOUR permanece como fonte de verdade para transferência Matriz SC → Filial SP: CFOP 6.152, CST ICMS 90, ICMS sem destaque, IPI suspenso CST 55, origem Matriz=1 e Filial=2.
- Venda interna Filial SP → CNPJs Simples SP é operação distinta: CFOP 5.102, origem 2, ICMS interno 18% e IPI conforme NCM quando aplicável.
- NFs internas de abril/2026 devem cobrir apenas produtos importados próprios GB; excluir nacionais, MDF, cerâmica, livros, fita, pseudo-itens, SEM_SKU, terceiros e Jarra Clink/CK4742.
- Antes de emitir NF interna mensal, reconciliar estoque fiscal por SKU/componente: saldo inicial Matriz/Filial, entradas/transferências do mês, vendas do mês, aliases Bling, kits e fatores de conversão.
- Para abril/2026, emissão validada integralmente pela Filial porque a Filial cobria os componentes após corrigir conversões de caixas/conjuntos. A inconsistência histórica de YW1520 na Matriz fica como ressalva separada.
- Vendas B2B/atacado emitidas pela Matriz devem abater estoque fiscal da Matriz antes de qualquer uso de saldo Matriz como excedente.
- NFs internas abril/2026 autorizadas: 000031, 000032, 000033, total R$ 77.065,09.
- NFs de transferência abril/2026 000649 e 000653 foram enviadas à FOUR/financeiro em 01/05/2026 com observação de que saíram antes da orientação fiscal atualizada.


## 2026-05-02 — Guarani Sistemas / distrato contratual

- Guarani Sistemas: estratégia aprovada para contestar a cobrança integral, exigir suspensão de protesto e memória de cálculo aberta, e negociar distrato **sem reconhecimento de dívida** com âncora/teto técnico inicial de **R$ 7.002,30**, condicionado a quitação total, baixa dos boletos/NFs 2384–2390 e inexistência de saldo remanescente.

## 2026-05-02 — Budamix Central / Live Sales

- Meta diária exibida no Budamix Central/Live Sales passa de **R$ 12.000** para **R$ 20.000**. Configuração aplicada em produção e fallback do endpoint atualizado.

## 2026-05-02 — Amazon Ads / otimização abril fechado

- Rodada de otimização Amazon Ads deve usar **abril/2026 fechado (01/04 a 30/04)** como baseline; não misturar últimos 30 dias móveis nem dados parciais de maio.
- Mudanças de campanha/keyword/target continuam exigindo aprovação explícita por grupo antes de execução.
- Para o grupo **Potes Redondos Plástico**, considerar o produto como potes redondos de vidro com tampa plástica; termos de vidro são core/aderentes, não conflito semântico.
- Acompanhamento obrigatório D+7 para todos os grupos executados em 02/05/2026 antes de nova rodada de cortes/escala baseada em impacto.

## 2026-05-03 — Amazon Ads / framework de revisão por grupo

- Pedro aprovou que a revisão de cada grupo de Amazon Ads deve seguir sempre 3 blocos: **cortar desperdício**, **promover winners validados de Auto/Broad para Exact com negativa na origem quando fizer sentido**, e **escalar winners Exact comprovadas** para aumentar vendas sem perder controle de ACoS/ROAS.
- Keywords recém-promovidas para Exact **não devem ser escaladas no mesmo momento**; precisam primeiro acumular histórico próprio na Performance antes de receber aumento de bid.
- Próximo grupo na fila após as execuções de 02/05 ficou **Suporte Controle Gamer**; a análise está pronta e a execução depende de aprovação do Pedro.

## 2026-05-03 — Amazon Ads / grupos finais e experimentos de tração

- Para grupos sem entrega ou sem vendas suficientes (**Abraçadeiras Nylon**, **Redinha Frutas**, **Kit Jardinagem**), diferenciar otimização de ACoS de experimento de tração. Sem dados, o objetivo é diagnosticar entrega/relevância/listing/Buy Box, não prometer melhora de ACoS.
- **Abraçadeiras Nylon** teve experimento de tração aprovado após confirmação de estoque FBA no ASIN ativo `KIT200BR10P` / `B0CN9PPC17`. Medição obrigatória em D+7: impressões, CTR, CPC, cliques, vendas, Buy Box e estoque FBA.
- **Redinha Frutas** e **Kit Jardinagem** não devem receber aumento de bid antes de validar product ads, estoque/FBA, listing ativo e Buy Box; se não houver estrutura ativa, manter/assumir inativo.

## 2026-05-03 — Paper.design / Templates Carrossel Budamix

- Templates oficiais de carrossel Budamix no Paper.design ficam organizados em 5 famílias × 3 versões cromáticas (CLARA/NORMAL/ESCURA), totalizando 96 artboards 1080×1080 no arquivo `01KQMVPNGXW4ZWQPVE1KDPMBN3`.
- Versão CLARA usa fundo areia e títulos teal `#004D4D`; não usar grafite para títulos principais em fundo claro porque fica lavado.
- Paper Shaders não são acionáveis via MCP; qualquer uso de Mesh Gradient/Grain/Liquid Metal exige aplicação manual pela UI do Paper Desktop.

## 2026-05-02 — Skills locais / ElevenLabs

- Para `video-use`, a API key ElevenLabs deve ser restrita ao mínimo necessário: apenas **Speech to Text**. Sanity check seguro: `POST /v1/speech-to-text` sem payload esperando HTTP 422 como prova de auth OK; não usar `/v1/user` porque exige permissão administrativa.

## 2026-05-08 — Daily Sales Report / Trader

- Pedro aprovou uma rotina diária chamada **Daily Sales Report — Trader**, executada pelo agente **Trader** todos os dias às **06:30 BRT**, com entrega no Telegram Kobe Hub, tópico **Marketplaces**.
- O relatório deve consolidar vendas/pedidos do dia anterior completo (00:00–23:59 BRT) de **Mercado Livre**, **Shopee 3 contas**, **Amazon BR** e pedidos do Bling Matriz como canal nomeado exatamente **Atacado - GB Matriz**.
- O report deve ser conciso, estilo Daily Briefing, focado em vendas geradas/pedidos do dia; não deve misturar settlement, extrato financeiro ou DRE com faturamento de pedidos.
- Se alguma fonte falhar, o Trader deve gerar relatório parcial, marcar a fonte como indisponível e não estimar números.

## 2026-05-09 — Tom de comunicação do Pedro em qualquer canal

- Ao redigir qualquer mensagem no nome do Pedro — WhatsApp, e-mail, Slack, Telegram, marketplace ou outro canal — usar tom profissional, educado, assertivo e objetivo, sem cordialidade excessiva.
- A regra se aplica sempre que Kobe estiver escrevendo **como se fosse o Pedro enviando**.
- Preferir abertura com **“Olá”** em vez de **“Oi”**.
- Não perguntar **“tudo bem?”** por padrão; usar só quando a pessoa perguntou antes ou quando a reciprocidade for natural.
- Evitar rasgação de seda, cumprimentos longos e linguagem muito calorosa; manter clareza, educação e firmeza sem soar grosseiro.

## Ver também

- `memory/context/decisoes/kobe-permanentes.md`
- `memory/context/decisoes/2026-04.md`
- `memory/context/decisoes/2026-05.md`

## 2026-05-04 — Relatório mensal Trader / rota de execução e notificação

- Geração direta do relatório mensal deve rodar como job realmente direcionado ao **Trader**, não como `main` tentando delegar via cron.
- Conclusão ou falha desse job deve ser avisada no mesmo tópico **Marketplaces** do Telegram onde o Pedro pediu o acompanhamento.


## 2026-05-04 — Social Studio Carrossel / Fase 1

- Social Studio Carrossel Fase 1 foi fechada em produção com pipeline E2E: template+briefing → IA copy → IA imagem → render Puppeteer → export PNG ZIP/PDF.
- Custo real validado: aproximadamente US$ 0,31 por carrossel completo; tempo briefing→pronto ~28–35s cold e ~10s hot cache.
- Cold start de render de 18,6s fica aceito como dívida de Fase 5; cache hot de 1,31s cobre a operação atual.
- JPG bundle fica desativado de forma controlada; PNG ZIP + PDF cobrem o uso real da Fase 1.
- Editor inline e template panorama foram pulados deliberadamente por agora; próxima escolha é Fase 4 publish IG ou Fase 5 hardening.

## 2026-05-04 — Budamix Central / Live Sales

- Meta diária do Budamix Central Live Sales foi ajustada de R$ 20.000 para **R$ 15.000** em produção (`settings.daily_goal`). Esta decisão substitui a meta de 02/05.

## 2026-05-04 — RH WhatsApp

- Em 04/05, mensagens proativas/alinhamentos de RH ficaram bloqueados; agente RH deve continuar em produção para responder inbound espontâneo.
- Wrapper central de WhatsApp RH deve usar texto puro com `linkPreview: false`; formatos ricos/previews/interativos devem ser evitados.

## 2026-05-05 — Social Studio / copy IA do template `lancamento`

- O template `lancamento` passa a tratar `product_name` do slide de revelação com limite mais apertado: **42 chars** e orientação explícita de nome curto, sem qualificadores extensos, preferencialmente em até 6 palavras.
- A regra geral de copy do Social Studio ganha a diretriz **R10**: headlines, `product_name` e `cta_headline` devem priorizar formas curtas; detalhes longos vão para `positioning`/`body`, não para o título principal.
- O frontend pode continuar usando auto-shrink como defesa visual, mas a qualidade deve ser corrigida na origem via schema + prompt.

## 2026-05-05 — DRE abril/2026 / U44 v4 limpa

- Pedro confirmou que a U44 anterior estava contaminada por R$ 2.138,75 de vendas pendentes ML; DRE abril foi corrigida de R$ 117.670,43 para **R$ 115.531,68**, elevando EBITDA e LL gerencial em R$ 2.138,75 sem mudança operacional real.
- Refatoração **v4 limpa da U44** aprovada para abril/2026, mas entra **depois da apuração U15 — Descontos Concedidos**.
- Estrutura aprovada: **U44 — Taxas de Marketplace limpa** deve conter só comissão + taxa fixa/service/transaction/FBA + frete líquido seller quando aplicável.
- Criar linha abaixo de U44 para **Outras Taxas Marketplace**: disputas, cancelamentos, taxas de reembolso, antecipação de recebíveis, programas pagos e multas.
- Shopee: não criar linha separada para “Frete Shopee”; o “Frete Líquido Shopee” de R$ 10.321,74 é subsídio/reembolso da Shopee, não despesa do seller. O custo efetivo de frete grátis já está embutido na regra de comissão/faixa Shopee; para DRE manter Shopee em U44 como comissão R$ 32.094,27 + taxa fixa R$ 28.038,07 = R$ 60.132,34.
- ML: retirar de U44 e mover para Outras Taxas Marketplace **R$ 6.156,26** = disputas/cancelamentos R$ 3.769,11 + taxas de reembolso/devolução R$ 2.387,15. EBITDA não deve mudar nessa reorganização.
- Amazon: reconciliar residual aproximado de R$ 120–258 e, se confirmado como fee acessório, classificar em Outras Taxas Marketplace.
- Reconciliação obrigatória da v4: U44 limpa + Outras Taxas Marketplace = **R$ 115.531,68** com tolerância máxima ±R$ 100; EBITDA não pode mudar na refatoração v4.

## 2026-05-05 — Canggu / domínio, CI/CD e Ana ML

- `https://canggu.com.br` passa a ser o domínio oficial do admin Canggu; `https://canguu-sigma.vercel.app` fica como fallback. Redirect www↔apex ainda pendente, recomendação: www → apex.
- Canggu deve usar GitHub Actions para auto-deploy das 13 Supabase Edge Functions. Mudanças em `_shared/` redeployam todas; mudanças em função específica redeployam só a função. Isso encerra o débito B5 de CI/CD.
- Ana no Mercado Livre deve usar tom natural, simples e humano; proibido instruir ou fallbackar para frases como “entre em contato”, “fale conosco” ou “estamos à disposição”, pois conflitam com o hard-block do ML.
- A resposta antiga no MLB3343832496 com frase forbidden precisa de correção manual no painel do ML e feedback 👎 no Canggu para alimentar embedding de correção.

## 2026-05-05 — RH / Ponto Certo

- `ponto.budamix.com.br` foi ativado como domínio oficial do Ponto Certo com DNS Registro.br → VPS, HTTPS Let's Encrypt e fallback `pontocerto.gbformulario.com`.
- WhatsApp RH proativo fica bloqueado indefinidamente até liberação explícita do Pedro. Guard ativo até 2027-01-01 como data-limite técnica; exceção `--allow-rh-reply` segue permitida para respostas inbound.

## 2026-05-05 — Social Studio PR2

- PR2 do Social Studio usa tokens semânticos em `element_styles`, não RGB literal, para que futuras mudanças de paleta propaguem em elementos customizados.
- Histórico de imagens fica em `image_versions` JSONB com máx. 5 entradas; blobs antigos permanecem no bucket para recuperação manual. Cleanup >90d fica para futura rotina.
- Templates usam padrão conservador `colorOverrideForSlot(...) ?? palette.X`, preservando visual 100% quando não há customização explícita.
- Restore de imagem é zero-custo, não incrementa `image_version` e não altera o array `image_versions`; versão ativa deriva do `image_asset_id` atual.
- Bug `cover-numeric` não foi corrigido na sessão; Pedro decide o fix mínimo ou com tech debt na próxima rodada.

## 2026-05-05 — Estoque Budamix

- `PHPB2025K/estoque-budamix` é o repo canônico desejado, mas produção ainda roda deploy rsync histórico na VPS até completar a remediação.
- Plano de remediação aprovado com backup completo, hash `.env`, verificação de HEAD remoto, rollback rápido e checagem PM2/ownership; execução pausada no `git fetch` por falta de credencial GitHub na VPS. Recomendação: Deploy Key SSH read-only.
- Estoque Budamix é desktop-only; não gastar esforço futuro com otimização mobile salvo pedido explícito.
- Correção de cadastro proposta: renomear `POT1BB` sem Trava para `POT1BB_ST`, após OK do Pedro.
- Bug dominante do estoque é kits/BOM: 12 de 16 erros recentes eram “Estoque insuficiente”; tocar PR4 só depois de PR1+PR2+PR3a estarem em produção e cadastro limpo.

## 2026-05-06 — DRE abril/2026 / prioridade e critério da U15

- A linha **U15 — Descontos Concedidos** tem prioridade alta e deve ser fechada antes da refatoração gerencial da **U44**.
- Na Amazon, **não rodar batches paralelos** de U15 e U44 na SP-API; concluir primeiro U15 para evitar rate limit e só depois atacar U44.
- O parcial de Mercado Livre foi aceito como critério-base para U15: **R$ 5.061,14** sobre **R$ 120.764,44** (**4,19%**) com foco apenas em desconto explícito do seller em pedidos válidos do mês.
- O consolidado provisório de **R$ 68.776,59** para U15 **não deve ser usado no DRE**, porque a Shopee ficou fora do benchmark e precisa reclassificação antes do fechamento final.

## 2026-05-06 — Canggu/Ana: atendimento 24/7 é regra permanente

- Ana/Canggu NUNCA deve responder que a Budamix tem horário comercial limitado ou que responderá apenas em horário de atendimento.
- Regra correta: Ana atende **24 horas por dia, 7 dias por semana**; essa é vantagem central do produto e deve prevalecer no prompt, no fallback e nos testes.
- Qualquer resposta contendo “segunda a sexta”, “8h às 18h” ou equivalente como limitação de atendimento deve ser tratada como bug crítico e bloqueada antes do envio.

## 2026-05-06 — Social Studio Reborn

- Social Studio foi refundado: deixa de ser gerador/editor com IA e passa a ser **publicador + painel de métricas Instagram**, recebendo PNGs/caption prontos do Canva/usuário.
- MVP cobre **carousel + single post** para a conta `@budamix.br`; Story/Reel ficam fora do escopo inicial.
- Token Meta deve ficar no **Supabase Vault** (`vault_secret_id`), nunca em coluna comum.
- Cron de publicação/métricas usa **Supabase Cron Jobs (`pg_cron` + `pg_net`)** chamando Edge Functions.
- Schema usa `media_type text+CHECK`, `engagement_rate GENERATED STORED`, archive defensivo antes de drop legacy e bucket `social-assets` com convenção `posts/{post_id}/asset-{N}`.
- PR #3 Fase A ficou aberto aguardando merge; Fases B/C/D seguem como roadmap.

## 2026-05-06 — DRE abril/2026 / arquivo canônico contínuo

- Pedro enviou `DRE_GB_PROCESSADO.xlsx` como versão atual do DRE abril/2026 e informou que sempre avisará quando gerar nova versão.
- A planilha de DRE é **contínua**: próximas versões devem substituir o arquivo canônico da competência no vault, sem acumular versões antigas; manter registro de data/hash atual no índice financeiro.

## 2026-05-07 — Guarani Sistemas / contraproposta final para a Priscila

- Pedro decidiu seguir com resposta firme e curta para a **Priscila**, ancorando a negociação em **R$ 7.500,00 à vista** como proposta final de composição amigável.
- A posição oficial da GB fica estruturada em 4 pilares: **sem reconhecimento de dívida**, **contratos já fora da vigência inicial de 12 meses**, **congelamento formal reconhecido pela própria Guarani em 01/10/2025**, e **ausência de uso operacional efetivo dos sistemas**.
- A contraproposta deve exigir como condição: **baixa/cancelamento dos títulos em aberto, ausência de protesto/negativação/cobrança externa, distrato com quitação recíproca, ausência de saldo remanescente e encerramento definitivo de todos os contratos/aditivos**.
- Faixa interna de negociação consolidada nesta sessão: alvo ótimo **R$ 7.500**, aceitável **R$ 8.500–9.000**, teto psicológico **R$ 10.000**; acima disso passa a ser ruim para a GB.

## 2026-05-07 — Gestão de Funcionários / Slack como fonte oficial

- Acompanhamento de performance de Yasmin, Lucas e Leonardo fica em frente separada **Gestão de Funcionários**, distinta do RH/Ponto Certo.
- Fonte oficial das atas será o Slack: Pedro envia para si a ata completa/gerencial com tag `#ata-reuniao Nome AAAA-MM-DD`; Kobe consolida semanalmente.
- Mensagem enviada ao funcionário deve ser versão curta e objetiva, sem análise gerencial pesada.

## 2026-05-07 — Canggu/Ana / webhook Evolution autenticado

- Webhook Evolution da instância BUDAMIX AI AGENT precisa manter headers `Authorization` e `apikey` para a Supabase Edge `webhook-whatsapp`; conexão da Evolution sozinha não prova ingestão.
- Backfills de mensagens perdidas devem ser controlados por conversa/bloco, comparando `whatsapp_message_id`, para evitar duplicidade e rajadas de respostas automáticas.

## 2026-05-07 — Kobe/OpenClaw / comunicação e estabilidade

- Kobe não deve narrar mecânica interna do OpenClaw no Telegram: bootstrap, reindex, warm-up, recall, embeddings e compactação rodam em silêncio; linguagem natural sobre consultar histórico segue permitida.
- Debounce inbound do Telegram fica em 8s via `messages.inbound`, não `messages.queue`; mensagens com `/new`/`/cerebro` continuam bypass.
- Conta ChatGPT do Pedro foi atualizada para **Pro 5x**; fallback `gpt-5.5 → gpt-5.4` usa o mesmo auth profile, então Anthropic como 3º fallback segue melhoria futura.

## 2026-05-07 — Social Studio Reborn / Fase C

- Fase B foi validada por smoke E2E e mergeada; Fase C será Meta OAuth + publicação real no Instagram.
- Durante o smoke real em `@budamix.br`, o C5 deve adicionar trava temporária **`TESTE INTERNO`** no início da caption; remoção só em commit C5b após validação.
- Token Meta de usuário permanece no Supabase Vault; App Secret fica em Edge env var.

## 2026-05-07 — Infra VPS / nginx host

- Apps estáticos roteados por Traefik para nginx host dependem de `nginx` ativo e `enabled`; `systemctl enable nginx` virou decisão para evitar novo 502 após reboot.

## 2026-05-11 — RH WhatsApp / autorização específica de casos de ponto

- Pedro autorizou o agente RH a tratar proativamente apenas o lote fechado do Monitor Ponto Semanal de 11/05/2026, semana 04/05–09/05, com Fran/Franciele, Leonardo, Lucas, Mateus e Sandra, até resolução completa.
- Essa autorização não libera WhatsApp RH proativo de forma geral. O guard geral continua ativo até 2027-01-01; exceções válidas: `--allow-rh-reply` para inbound e `--allow-rh-approved-case` para esse lote aprovado.
- Follow-ups desse lote podem rodar diariamente e escalar ao Pedro após 5 dias úteis sem resposta; devem se encerrar quando todos resolverem ou no máximo após 19/05/2026.

## 2026-05-11 — Daily Sales Report / Slack funcionários

- Daily Sales Report para equipe administrativa passa a ser enviado via Slack DM para Yasmin, Lucas e Leonardo, diariamente às 06:50 BRT.
- Destinatários finais: Yasmin `U09AX9SETDM` (`yasminoscarlino7@gmail.com`), Lucas `U08TCL5A8U9`, Leonardo `U0AUUQ5MP6C`.
- Formato aprovado: título `DAILY SALES REPORT - DD/MM/AAAA (Ontem)`, seções `RESUMO GERAL`, `VENDAS POR CANAL`, `TOP PRODUTOS — CONSOLIDADO 3 PLATAFORMAS`, `ANÁLISE DO DIA`, rodapé com dia analisado 00:00–23:59 BRT.
- Não incluir `DESTAQUES DO DIA`; títulos devem usar `rich_text blocks` com negrito + sublinhado real do Slack; conteúdo interno sem formatação especial.
- Fonte canônica: Budamix Central/Supabase `v_daily_sales` para marketplaces e Bling Matriz para Atacado GB Matriz. Top Produtos deve consolidar SKUs equivalentes cross-plataforma e nunca exibir “Produto não identificado”.

## 2026-05-11 — Canggu/Ana ML / guard determinístico antes de envio externo

- Toda rota que posta resposta da Ana no Mercado Livre deve ter guard determinístico imediatamente antes do envio externo, bloqueando variações de “entre em contato”, “fale conosco”, “para mais detalhes”, “nossa equipe técnica” e equivalentes.
- Prompt no banco não basta: rotas legadas Supabase, especialmente `ml-webhook`, precisam estar reconciliadas com o repo canônico e auditadas contra frases proibidas.
- Repo canônico confirmado em 11/05: `PHPB2025K/canguu`; patch do `ml-webhook` commitado em `eb76d3f` para bloquear frases proibidas antes do POST no ML.

## 2026-05-11 — Budamix Central / pedidos Amazon FBA removal não são venda

- Pedidos Amazon de remoção FBA não devem contar como venda no Budamix Central, Budamix Live, relatórios diários ou apurações comerciais.
- Assinatura para exclusão determinística: `SalesChannel=Non-Amazon` + `FulfillmentChannel=AFN`, datas dummy `1995-01-01T00:00:00Z` ou `AmazonOrderId` começando com `S01-` em contexto de remoção.
- Regra implementada no sync Amazon: pular esses pedidos no ingest e marcar legados como `cancelled` preservando auditoria.

## 2026-05-12 — Aviso obrigatório de fallback de modelo

- Pedro determinou que Kobe deve avisar sempre que, por qualquer motivo, precisar operar em fallback de modelo/LLM.
- Se o modelo principal indisponibilizar, rate-limitar ou a sessão cair para fallback, Kobe deve informar explicitamente o Pedro assim que detectar, incluindo modelo principal esperado e fallback em uso quando essa informação estiver disponível.
- A regra vale mesmo que o fallback seja temporário e mesmo que a tarefa continue funcionando.

## 2026-05-12 — Daily Sales Report v2 / padrão mínimo de profundidade

- Pedro rejeitou previews rasos da Fase 4: diagnósticos por conta e prioridades do dia precisam ser profundos, completos, temporais e retroativos, com embasamento em memória persistente.
- Mensagens aos funcionários não podem apenas listar métricas óbvias; devem condensar causa provável, evidência, risco, ação recomendada e critério de acompanhamento.
- Produtos exibidos no texto devem sempre aparecer pelo **nome do produto**, nunca pelo SKU, mesmo que o cálculo use SKU no background.
- Títulos de seção no Slack devem seguir obrigatoriamente o padrão visual aprovado: emoji + título uppercase + bold/underline real via rich_text.

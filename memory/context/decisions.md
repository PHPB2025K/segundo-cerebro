---
title: "Decisões — Kobe"
created: 2026-05-28
type: context
status: active
tags:
  - memory
  - context
  - decisions
---

# Decisões — Kobe

## 2026-05-28 — Estoque GB como motor de movimentações auditáveis

- Pedro aprovou a linha operacional para manter a Planilha de Estoque atualizada por meio de um **motor/livro de movimentações de estoque** antes de alterar saldo na aba ESTOQUE.
- A aba ESTOQUE continua como visão/saldo final, mas cada alteração deve nascer de um movimento auditável com origem, SKU, quantidade, responsável, documento/foto quando aplicável, status e validação.
- Saídas a cobrir: vendas pagas/confirmadas dos marketplaces, pedidos de atacado via WhatsApp e envios para Full preenchidos na planilha de ENVIOS FULL.
- Entradas a cobrir: mercadorias compradas recebidas no galpão, devoluções aprovadas como íntegras e containers recebidos.
- Pedro vai criar grupos WhatsApp específicos **Estoque - GB Importadora** e **Devoluções - GB Importadora**, além de um tópico Telegram **Estoque** no Kobe Hub.
- Regra de segurança aprovada: entradas via WhatsApp não devem alterar estoque automaticamente no início; devem criar movimento pendente para interpretação e confirmação antes da escrita no saldo.
- Atualização do mesmo dia: Pedro criou os grupos WhatsApp **Estoque - GB Importadora** e **Devoluções - GB Importadora**, adicionou Kobe via instância Evolution API, e criou no Telegram os tópicos **Estoque** (thread 11932) e **Devoluções** (thread 11937).
- Regra de canal: WhatsApp é a fonte real de inserção/comunicação diária da operação; Telegram fica para desenvolvimento do sistema, alertas, divergências, decisões e assuntos com Pedro fora da rotina operacional.

## 2026-05-28 — Produtos MDF / catálogo operacional

- Pedro definiu que o **Quebra-Cabeça Animais MDF** deve entrar na lista de produtos feitos em MDF da operação mesmo não aparecendo na lista atual da aba ESTOQUE consultada naquele momento.
- Forma de apresentação usada na sessão: **kits de 5, 10 e 20 peças**.
- Contexto: correção explícita de uma primeira resposta que havia sinalizado o item como pendente/fora da lista atual.

## 2026-05-28 — Aba ESTOQUE da planilha de precificação deve listar apenas SKUs pai/unitários, com exceções operacionais explícitas

- Pedro definiu que a aba **ESTOQUE** deve listar exclusivamente produtos unitários / SKUs pai, sem linhas de kits/composições de marketplace.
- Exceções aprovadas como unitárias dentro da ESTOQUE: **Kits Jardinagem**, **Kits MDF (porta-copos e descansos de panela)** e o **conjunto de 5 potes redondos IMB501**, por serem tratados operacionalmente como produto unitário.
- Pedro aprovou deletar fisicamente da aba ESTOQUE os demais kits de potes e kits quebra-cabeças, em vez de apenas limpar conteúdo.
- Pedro decidiu que o **QCB002 — Kit 10 Quebra-cabeças Animais** deve voltar/ficar na aba ESTOQUE como item unitário.
- Pedro também aprovou corrigir os SKUs das Xícaras 95ml RR na ESTOQUE para o mapeamento correto: **verde = 308_B** e **rosa = 309_B**.
- Contexto: reorganização da planilha para que a ESTOQUE fique como base canônica de produtos unitários, sem recalcular por enquanto o preço de custo nas abas MELI/SHOPEE/AMAZON.

## 2026-05-22 — Canggu: Edge Functions internas com `X-Internal-Token` exigem lista explícita de `NO_JWT_FUNCTIONS`

- Funções Supabase Edge internas que são chamadas por outras funções/rotinas, e não diretamente pelo usuário final, podem operar temporariamente com `verify_jwt=false` apenas quando protegidas por `X-Internal-Token` e listadas explicitamente no deploy.
- O workflow de deploy deve preservar a lista `NO_JWT_FUNCTIONS`; adicionar uma função a essa lista significa que ela passa a depender do segredo interno e precisa validação E2E.
- Essa é uma mitigação temporária para o desalinhamento JWT observado no Canggu/Ana. O objetivo final continua sendo investigar causa raiz e voltar `verify_jwt=true` quando seguro.
- Validação mínima: conversa real ou sintética cobrindo branch normal, mídia, áudio, burst, pedido humano e reclamação grave com escalação/notificação visual ao Pedro.

## 2026-05-31 — GB26003 NÃO é pedido/embarque real sem gatilhos formais

- Pedro corrigiu explicitamente a interpretação anterior sobre o **GB26003**: ele não pagou sinal, não autorizou fabricação e não assinou contrato.
- Regra operacional definitiva: qualquer menção a GB26003 em relatório operacional, pré-alerta ou documento externo deve ser tratada como referência não confirmada / possível erro operacional até existirem os três gatilhos formais: contrato assinado, sinal pago e autorização explícita de fabricação/embarque pelo Pedro.
- Não cadastrar, atualizar, criar tracking, milestones, pagamentos ou pendências logísticas/financeiras no Import Hub para GB26003 sem esses gatilhos.
- Se o assunto voltar, o próximo passo seguro é confirmar com Open Trade/Skiway por que o código apareceu nos relatórios, sem assumir compromisso ou existência do pedido.

## 2026-05-31 — Kits coloridos de canecas/xícaras devem ser desmembrados como 1 unidade de cada cor

- Pedro confirmou explicitamente a lógica operacional dos kits coloridos de caneca/xícara: SKU colorido/sortido representa **1 unidade de cada cor** do conjunto.
- Exemplos validados na baixa de estoque: `CTL002` colorida = 1 unidade de cada cor Tulipa; `KIT6CAR200` colorida = 1 unidade de cada cor Reta 200.
- Essa regra deve orientar BOMs, baixa marketplace, conferência de estoque e normalização de SKUs desses kits, salvo exceção explícita futura.

## 2026-06-01 — Estoque/Avarias: descrição livre pode resolver SKU físico e baixa total apenas quando inequívoca

- Pedro definiu que o mapeamento de SKU deve conseguir decifrar a qual SKU a descrição do produto se refere tanto nas mensagens do grupo de vendas de atacado quanto nas mensagens de avarias.
- Em mensagens de avaria, quando houver comando inequívoco de baixa total/zerar estoque e a descrição resolver com segurança para um SKU físico, o processador pode gerar baixa total do saldo atual desse SKU.
- Caso concreto autorizado: “Caneca Porcelana Reta 200ml Rosa” / “caneca reta rosa” resolve para `CAR200R` e pode zerar o saldo atual quando a mensagem pedir baixa total.
- Mensagens ambíguas continuam bloqueadas como divergência e não devem alterar saldo automaticamente.

## 2026-06-02 — Shopee: alternância entre contas para evitar competição interna

- Pedro aprovou, via contexto consolidado pelo Trader, seguir com separação/alternância entre contas Shopee para reduzir competição interna de lances entre lojas da própria operação.
- Variações de performance por shop_id nos próximos reports devem ser lidas considerando essa estratégia, separando queda operacional real de alternância planejada.
- Monitoramento obrigatório: D+1/D+3/D+7 por conta, anúncio, SKU, ADS, afiliados, ROAS/TACoS e possível canibalização.

## 2026-06-02 — Mercado Livre: MDF pode receber investimento com ACoS alto como aposta de tração

- Pedro alinhou que produtos MDF no Mercado Livre podem receber mais investimento mesmo com ACoS alto quando a intenção for ganhar tração, exposição e ranking.
- A leitura de ADS/marketplace deve separar MDF do restante da conta para não classificar o ACoS alto como erro automático.
- Se MDF pressionar TACoS/resultado geral, a decisão pendente passa a ser limite de tolerância ou janela mínima de teste, não corte imediato.

## 2026-06-04 — Daily Sales Shopee fica em standby até lapidação e smokes finais

- Pedro decidiu pausar o Daily Sales Shopee após a Fase 1 validada: o pipeline está implementado, mas ainda precisa lapidar pontos antes de virar rotina.
- Não ativar cron 07:00 BRT, nem tratar o report Shopee como produção, até aplicar densidade nas camadas restantes, rodar smokes das Contas 2 e 3 e resolver gaps relevantes do fetcher.
- Slack do Daily Sales Shopee deve ser consolidado para Pedro em uma mensagem final após a camada de escrita, não uma mensagem por camada.
- A visão Shopee no Mission Control deve ficar em página dedicada, separada do Mercado Livre, para evitar mistura de regras e reduzir risco de regressão.

## 2026-06-04 — Facebook Page Budamix: URL canônica por enquanto e rotação obrigatória de segredo Meta

- A Página Facebook Budamix foi atualizada com capa, foto de perfil e bio usando Graph API.
- Vanity URL `/budamix` ficou postergada porque a API bloqueou e a interface nova do Meta não expôs o campo; até lá, usar a URL canônica da página.
- Como segredo/token Meta apareceu em chat operacional, a regra é rotacionar o App Secret no Meta Developers antes de ampliar automações ou migrar a operação para runtime permanente.
- Ao rotacionar, atualizar todos os ambientes dependentes do app compartilhado com OpenClaw/VPS para não quebrar integrações.

## 2026-06-04 — Estoque: KIT6S100 tem BOM definitivo

- `KIT6S100` foi definido operacionalmente como kit de 6 unidades composto por 2× `YW640RC`, 2× `YW1050RC` e 2× `YW1520RC`.
- Essa composição deve orientar resolução de SKU, baixa marketplace, reprocessamento de divergências e auditoria de saldo; componentes sem saldo continuam divergência real, não erro de mapeamento.

## 2026-06-05 — ENVIOS FULL deve falar em detecção por cursor, não em criação no dia

- Pedro corrigiu explicitamente a linguagem do cron de ENVIOS FULL: sem data operacional confiável na planilha, Kobe não deve afirmar que houve “envio novo do dia”.
- Regra vigente: reportar apenas que houve envios “detectados/adicionados após o último cursor” ou “registrados no processamento”.
- Contexto: a planilha ENVIOS FULL não tem campo confiável de data de criação e o timestamp salvo no Supabase reflete processamento, não criação operacional do envio.
- Próxima condição para mudar essa linguagem: a operação/analistas passarem a preencher um campo de data de criação na planilha.

## 2026-06-05 — WhatsApp Estoque exige controle obrigatório de data operacional e trava forte de duplicidade

- Pedro apontou como requisito crítico que entradas e saídas vindas do grupo WhatsApp Estoque tenham controle explícito de datas de processamento e blindagem máxima contra duplicidade.
- Regra aprovada: antes de aplicar qualquer movimento, o processador deve registrar `business_date` em BRT, trilha de processamento e fingerprint do conteúdo, além de bloquear automaticamente movimentações equivalentes no mesmo dia operacional.
- Reenvio/cópia da mesma entrada não deve mexer no saldo; deve gerar alerta de possível duplicidade para auditoria.
- Contexto: message ID único protege a mesma mensagem, mas não basta quando a mesma movimentação reaparece como nova mensagem WhatsApp.

## 2026-06-05 — Grupo Estoque por imagem/lista só entra no automático com cabeçalho explícito

- Pedro validou o comportamento seguro no teste da imagem de canecas: mensagens de imagem/lista no grupo Estoque só podem ser processadas automaticamente quando trouxerem cabeçalho operacional explícito como `ENTRADA`, `BAIXA` ou `AVARIA`.
- Sem cabeçalho, o automático deve ignorar; processamento manual só é permitido com autorização explícita do Pedro e mantendo trilha auditável da mensagem original.
- Contexto: o OCR conseguiu ler as linhas e quantidades, mas faltava o tipo operacional, então a inferência automática permaneceu bloqueada por segurança.

## 2026-06-05 — Folha/orçamento da Porcelanas Lu com “CANECA COPO 220ML” deve mapear para Tulipa, não para Reta

- Pedro corrigiu explicitamente que `CANECA COPO` com os códigos da folha de orçamento da Porcelanas Lu se refere às canecas **Tulipa**, não à família **Reta 200ml**.
- Regra operacional derivada: descrições/códigos desse fornecedor precisam mapear para `TL250*` por cor; se aparecerem em imagem ou mensagem futura, não devem mais cair em `CAR200*`.
- Contexto: uma entrada manual de teste foi inicialmente aplicada em `CAR200AM/AZ/B/VD/R`, depois estornada e relançada corretamente em `TL250A/Z/B/V/R`, com atualização dos aliases para refletir a equivalência correta.

## 2026-06-05 — Fluxo oficial do grupo WhatsApp Estoque: Estoque movimenta saldo; Devoluções só evidencia processo

- Pedro redefiniu que Lucas não classifica devolução para estoque: ele só processa a devolução na plataforma, posta a foto da etiqueta no grupo **Devoluções** e encaminha o item para conferência física.
- A única fonte válida de movimentação automática/manual de estoque passa a ser o grupo WhatsApp **Estoque - GB Importadora**, após conferência física da Fran/expedição.
- Formatos oficiais aceitos no grupo Estoque: `ENTRADA`, `DEVOLUÇÃO`, `BAIXA`, `AVARIA DE DEVOLUÇÃO` e `AVARIA DE CONFERÊNCIA`, sempre com **um único produto e uma única quantidade por mensagem**.
- `ENTRADA` e `DEVOLUÇÃO` somam no estoque vendável; `BAIXA` subtrai com trava de saldo negativo; `AVARIA DE DEVOLUÇÃO` e `AVARIA DE CONFERÊNCIA` devem ser reconhecidas/alertadas, mas não somam no vendável automaticamente.
- Mensagem sem cabeçalho válido, com cabeçalho genérico `AVARIA`, ou misturando mais de um item/tipo na mesma mensagem, não deve movimentar estoque automaticamente.

## 2026-06-06 — Meta Ads Budamix começa focado em IMB501

- Pedro/Kobe definiram a primeira estrutura de Meta Ads da Budamix com orçamento inicial de **R$57/dia** (~R$1.710/mês), em campanhas pausadas até revisão final.
- O HERO dos primeiros 1–2 meses é **IMB501 — Conjunto 5 Potes Redondos de Vidro**, escolhido por ranking de 90 dias e concentração extrema de receita/margem dentro da linha de vidro.
- Regra estratégica: não pulverizar verba entre redondos, retangulares e quadrados no início; escalar em ondas, começando pelo IMB501 e replicando depois para outras linhas.
- Estrutura inicial: ASC como principal, teste de criativos e retargeting WCA-based. DPA fica postergado para fase posterior, quando pixel/catálogo tiverem mais maturidade.
- Otimização inicial deve mirar **AddToCart**, não Purchase, para acelerar aprendizado com orçamento limitado.
- Não comprar ferramentas pagas de pesquisa de interesses nesta fase.
- Criativos de vídeo devem respeitar a identidade visual Budamix: **Antonio Bold** como fonte oficial e paleta oficial, sem cores inventadas fora do branding.

## 2026-06-08 — Meta Ads Budamix Campanha 1 ativa com budget reduzido e freeze

- Pedro/Kobe ativaram a Campanha 1 de Meta Ads Budamix em produção, focada no IMB501, usando apenas o vídeo 1 enquanto os vídeos 2 e 3 ainda não ficam prontos.
- Budget da Campanha 1 foi reduzido de R$37/dia para **R$20/dia** antes de sair da janela inicial, para manter teste controlado (~R$600/mês).
- Campanha 1 deve ficar em freeze operacional até aproximadamente **22/06/2026**: não alterar budget, público ou criativo salvo exceção aprovada por Pedro/Kobe ou anomalia crítica.
- Público aprovado para a fase inicial: mulheres no Brasil com Advantage+ Audience ativo; a API Meta rejeitou limitar `age_max` abaixo de 65 nesse formato, então a otimização fica a cargo do algoritmo dentro da configuração aceita.
- Campanhas 2 e 3 continuam pausadas aguardando os vídeos 2 e 3 do Pedro antes de ativação.

## 2026-06-08 — Copy Budamix não deve usar claims sem base técnica comprovada

- Pedro corrigiu que o vidro do IMB501 não deve ser comunicado como **borossilicato**.
- Regra vigente para anúncios/copy Budamix: não usar “borossilicato”, nem claims de “freezer” ou “micro-ondas”, enquanto não houver base técnica/documental segura para o produto específico.
- Para o IMB501, a linha aprovada de copy deve focar em praticidade, vedação, organização e multiuso cotidiano, sem promessas técnicas indevidas.

## 2026-06-08 — Spark/Meta Ads usa schema separado por plataforma

- Pedro decidiu que a base operacional do Spark deve usar schemas separados por plataforma, começando por `meta.*`, em vez de uma tabela genérica única com coluna `platform`.
- Razão operacional: clareza e espelhamento direto do modo como a operação pensa cada canal; Meta, Amazon e ML devem ter estruturas próprias quando isso reduzir ambiguidade.
- Regra derivada: para ações/logs/recomendações de ads, preferir separação por plataforma quando a diferença operacional for relevante, mesmo que uma tabela genérica pareça tecnicamente mais simples.

## 2026-06-08 — Budamix é conta primária Meta Ads; GB Distribuição fica legacy/parada

- A operação Meta Ads ativa passa a ser **Budamix**.
- GB Distribuição deve permanecer marcada como legacy/parada e não deve ser operada por scripts, skills ou Spark salvo autorização explícita.
- Scripts de Meta Ads precisam exigir conta explícita/whitelist para evitar ação acidental na conta errada.

---
title: "Lições — Kobe"
created: 2026-05-21
type: context
status: active
tags:
  - memory
  - context
  - lessons
---

# Lições — Kobe


## 2026-05-30 — [TÁTICA] Cron sem evento novo também precisa deixar trilha de auditoria

No cron ENVIOS FULL, a execução de 30/05 com zero envios novos mandou resumo e apareceu em log, mas inicialmente não criou linha em `envios_full_cron_runs`. Para rotinas operacionais auditáveis, “não houve evento” também é resultado de execução e precisa virar registro estruturado com contadores zerados; senão fica impossível diferenciar rotina saudável de lacuna de monitoramento.

## 2026-05-30 — [TÁTICA] Shopee deve preferir SKU de variação antes de SKU pai na baixa de estoque

Na baixa marketplace fora Full, várias divergências da Shopee nasceram porque o pipeline usava SKU pai (`item_sku`) quando o SKU correto estava no SKU da variação (`model_sku`) do raw payload. Antes de criar aliases manuais ou classificar como erro de cadastro, normalizar a partir do identificador mais granular da venda; SKU pai em marketplace costuma representar anúncio, não necessariamente unidade física baixável.

## 2026-05-29 — [TÁTICA] Mensagem operacional não pode ser marcada como processada antes do efeito auditável

No pipeline de Estoque via WhatsApp, uma mensagem de avarias foi capturada e memorizada, mas a aplicação do movimento falhou por validação de `sourceType`; mesmo assim a mensagem ficou marcada como processada e não será reprocessada automaticamente. Para fluxos operacionais auditáveis, sucesso de ingestão não é sucesso de aplicação: só marcar como processado quando o efeito esperado existir ou quando a falha ficar em fila explícita de retry/intervenção.

## 2026-05-23 — [TÁTICA] Crontab da VPS usa UTC; planejamento continua em BRT

A VPS Hostinger interpreta crontab em UTC. Qualquer cron planejado para horário de Brasília precisa ser convertido explicitamente para UTC ao gravar no sistema (+3h), enquanto toda comunicação e documentação para Pedro permanece em BRT. Não assumir que `07:00` no crontab significa 07h BRT.

## 2026-05-23 — [TÁTICA] Escolha de modelo deve ser por camada quando o pipeline tem tarefas cognitivas diferentes

No benchmark do DSA ML, o melhor resultado veio do modo híbrido: Sonnet 4.6 nas camadas estruturais e Opus 4.7 nas camadas de maior julgamento (L04/L05). Avaliar pipeline inteiro com um único modelo escondia essa diferença. Para pipelines multi-camada, comparar qualidade por função cognitiva da camada, não apenas por custo/latência global.

## 2026-05-23 — [TÁTICA] RH/Ponto não deve classificar inconformidade sem contexto individual de jornada

Na auditoria Ponto Certo da semana 18/05–22/05, Pedro corrigiu que entrada tarde do Mateus por Tiro de Guerra é contexto conhecido e não deve ser cobrada quando compatível com a jornada especial. Intervalo de almoço abaixo de 1h também não deve virar inconformidade operacional automática. Antes de cobrar, validar escala, jornada individual, ajuste/justificativa e regra real.

## 2026-05-22 — [TÁTICA] Hotfix deployado direto precisa virar commit imediatamente

Em Canggu/Ana, um deploy cascade do GitHub Actions quase reverteu hotfix aplicado manualmente porque o repo ainda carregava versão antiga. Toda correção feita via CLI/MCP/deploy direto deve ser commitada e pushada logo em seguida, antes de qualquer workflow automático tocar a mesma função.

## 2026-05-22 — [TÁTICA] E2E de atendimento precisa validar também escalação e notificação ao owner

O pipeline da Ana passou em conversa normal, mas clientes com reclamação grave ativavam a branch de escalação, que falhava com 401 e abortava a resposta. Além disso, o banco parecia correto mas as notificações iam para o número da própria Ana, não para o Pedro. Critério mínimo: conversa normal, imagem, áudio, burst, pedido humano, reclamação grave, escalation row e confirmação visual da notificação no celular do owner.

## 2026-05-22 — [TÁTICA] Estoque do site não pode ter duas fontes de verdade

O bug de oversell potencial no e-commerce veio de o site decrementar Supabase enquanto o cron de estoque relia a planilha intacta e sobrescrevia o decremento. Para estoque físico, a planilha precisa continuar SSoT: venda no site deve virar baixa na planilha, e só depois o sync propaga para o site.


## 2026-05-21 — [TÁTICA] Recovery de atendimento precisa validar até mensagem agent real

Em Canggu/Ana, corrigir parser/source do webhook não bastou para declarar recovery. O teste intermediário provou que mensagens inbound chegavam e que `process-message` respondia manualmente, mas o dispatch automático ainda não gerava resposta. Critério correto para recovery: mensagem real do cliente → webhook → invoke do process-message → fechamento de pending → mensagem `sender=agent` com tokens/tempo de resposta.

## 2026-05-21 — [TÁTICA] Sync automático de vault não deve fazer Git direto sem lock

Autosave, pull periódico e commits manuais no mesmo vault criam risco de corrida. Fluxos automáticos devem passar por wrapper de escrita segura/lock e registrar backup antes de mudança estrutural. Lock local resolve concorrência na mesma máquina; conflito distribuído Mac↔VPS ainda exige disciplina de push/pull ou lock compartilhado.

## 2026-05-22 — [TÁTICA] Diagnóstico da Ana precisa validar conversa real completa, não só teste controlado

Em Canggu/Ana, receber mensagem no Supabase e até responder um teste manual não prova recovery. O caso real de 22/05 mostrou que clientes podem receber apenas a mensagem inicial de origem/canal, com imagens e textos corretamente ingeridos, mas sem nascer a resposta LLM posterior. Critério correto de saúde: cliente real ou teste que simule o fluxo real completo → mensagem inicial → resposta à origem/canal → nova mensagem/pergunta/imagem → mensagem `sender=agent` posterior com `tokens_used` e envio confirmado.


## 2026-05-24 — [TÁTICA] Amazon Ads deve partir da base viva, não da rodada histórica

Na análise semanal de Amazon Ads, a lista inicial omitiu os grupos MDF criados depois da rodada de abril. Antes de afirmar escopo de grupos/anúncios, consultar a base viva do BidSpark/Amazon Ads e validar grupos recém-criados, status live e campanhas atuais. Lista histórica serve como contexto, não como fonte final de verdade.

## 2026-05-25 — [TÁTICA] Camada final de análise operacional deve traduzir jargão sem rebaixar a máquina analítica

Na lapidação da L06 do Daily Sales Analyst ML, Pedro deixou claro que Yasmin não precisa saber como a análise foi feita; ela precisa entender o que aconteceu, o que fazer e por que importa. A regra correta é manter L01-L05 técnicas e rigorosas, mas traduzir a saída final: GMV vira faturamento, ADS share vira participação do ADS no faturamento, `health` numérico vira qualidade do anúncio em termos naturais. Simplificar linguagem não é simplificar raciocínio.

## 2026-05-25 — [TÁTICA] Cron de planejamento recorrente não deve fazer ajuste incremental cego

No planejamento semanal de canecas, Pedro corrigiu que o cron deve recalcular o pipeline inteiro do zero com dados fechados até D-1 e só depois comparar contra o último plano aprovado. Para compras/reposição, ajuste incremental simples acumula erro e ignora mudança de estoque, venda, inbound e ruptura.

## 2026-05-25 — [TÁTICA] Monitor que roda sem validação útil não é OK operacional

No Fisco, o refresh da Filial teve rodadas abortadas por allowlist/SIGTERM e sem validação útil. Uma execução de cron que termina sem checar a condição que deveria monitorar não deve ser tratada como normalidade. O status precisa diferenciar “rodou” de “validou a integração”.

## 2026-05-26 — [TÁTICA] Shopee Full+ é contexto de margem/mix, não causa automática de conversão

No Daily Sales v2, a participação Full+ deve ser tratada como contexto operacional para margem, mix logístico, rebate e elegibilidade futura. Não usar Full+ como explicação automática para variação diária de conversão sem evidência adicional por conta/SKU/anúncio.

## 2026-05-27 — [ESTRATÉGICA] Planilha de estoque exige valores em formato brasileiro

Pedro definiu como regra absolutamente obrigatória: sempre que inserir ou atualizar qualquer tipo de valor na planilha de estoque, em qualquer aba, usar padrão brasileiro de moeda/número: `R$ 00,00`, com vírgula decimal. Nunca usar ponto como separador decimal. Antes de declarar sucesso em qualquer update de valor na planilha, validar visualmente/diretamente que o Sheets recebeu o valor no formato correto.

## 2026-05-28 — [TÁTICA] Lista operacional de produtos pode incluir item fora da aba ESTOQUE quando Pedro o tratar como parte ativa da operação

Na revisão dos produtos em MDF, o Quebra-Cabeça Animais não aparecia na lista atual da aba ESTOQUE, mas Pedro pediu explicitamente para adicioná-lo na relação enviada. Para pedidos de listagem/catalogação operacional, a resposta final deve refletir o entendimento atual do Pedro sobre o portfólio ativo, sinalizando quando um item está fora da aba canônica em vez de omiti-lo automaticamente.

## 2026-05-28 — [TÁTICA] Limpeza da aba ESTOQUE pode quebrar margem/lucro das abas de marketplace se elas ainda dependerem de SKU de kit

Na planilha de precificação da GB, remover kits da aba ESTOQUE deixou a aba correta como fonte de SKUs unitários, mas expôs dependências ocultas em SHOPEE e AMAZON: várias linhas de margem/lucro quebraram porque ainda puxavam custo/produto por SKU de kit removido. Regra operacional: antes de limpar a aba ESTOQUE, validar dependências cruzadas nas abas de marketplace e manter um backup pré-limpeza para restaurar custo/produto sem recolocar kit na fonte canônica.

## 2026-05-31 — [TÁTICA] Relatório externo de importação não confirma embarque sem gatilhos formais do Pedro

No caso GB26003, relatório/pré-alerta externo da Open Trade indicava “embarque autorizado”, mas Pedro corrigiu que não houve contrato assinado, sinal pago nem autorização de fabricação. Para importação, documento operacional externo é indício, não fonte suficiente para criar embarque real no Hub. Antes de cadastrar/tratar como container vivo, validar os gatilhos formais do negócio com Pedro/Trading.


## 2026-05-31 — [TÁTICA] Baixa retroativa de estoque exige validação de resolução antes de aplicar movimentos

Na correção dos SKUs divergentes de marketplace, aliases/BOMs só foram aplicados depois de backup, teste do resolvedor e simulação de `ingest-safe-outbound`. Isso evitou baixa cega em estoque físico. Regra: antes de baixa retroativa em lote, validar mapeamento SKU→componente, simular pendências remanescentes e só aplicar quando o erro restante for conhecido e auditável.

## 2026-06-01 — [TÁTICA] Baixa marketplace precisa auditar seller real e bloquear Full/FBA físico

No hardening do Daily Marketplace Baixa, Pedro pediu garantias explícitas de que seller processado = seller logado, alerta se Full/FBA gerar movimento físico, snapshot de status/SKU/logística no momento da execução e fila diária de divergentes. Para rotinas de estoque multi-seller/multi-logística, o critério de sucesso não é só “baixou sem erro”: precisa provar qual seller foi processado, preservar o payload relevante da decisão e acusar imediatamente qualquer baixa física em pedido que deveria ser Full/FBA.

## 2026-06-02 — [TÁTICA] Daily Sales com Atacado no consolidado exige leitura separada de marketplaces

No Daily Sales de 01/06, o consolidado ficou muito forte, mas Atacado - GB Matriz adicionou R$ 6.483,34 em apenas 3 pedidos. Antes de concluir que marketplaces melhoraram ou que ticket médio subiu estruturalmente, separar marketplace puro de Atacado/Bling e analisar ML, Shopee e Amazon isoladamente. Atacado distorce faturamento, ticket e leitura de tendência quando entra no mesmo total executivo.

## 2026-06-02 — [TÁTICA] Bling 403 na Matriz muda o risco de integração fiscal

Até 01/06 o Bling 403 parecia concentrado na Filial e estava adiado por decisão operacional do Pedro. Em 02/06, o Fisco registrou HTTP 403 também na Matriz em execuções úteis. Quando a Matriz falha, o risco deixa de ser integração filial secundária e passa a bloquear operação fiscal principal; antes de emitir NF-e, criar draft ou depender do Bling, validar conectividade Matriz + Filial em teste controlado.

## 2026-06-04 — [TÁTICA] Escrita crítica precisa de verificação por leitura ou smoke

Na construção dos prompts v4.0 do Daily Sales Shopee, uma escrita retornou sucesso mas os arquivos não persistiram como esperado; a perda só foi detectada por verificação posterior. Para arquivos críticos de prompt, configuração, automação ou memória operacional, sucesso da ferramenta não basta: validar por leitura, diff, grep direcionado, smoke ou build antes de declarar entregue.

## 2026-06-04 — [TÁTICA] Pipeline de estoque deve degradar por item, não perder lote inteiro por conflito isolado

No fechamento de estoque de 03/06, duplicata/conflito isolado poderia derrubar o lote inteiro. A correção certa foi fallback granular: aplicar os itens válidos, registrar os conflitos específicos e manter trilha auditável. Para rotinas de baixa/log de estoque, erro localizado não deve impedir processamento do restante quando a decisão por item é segura.

## 2026-06-04 — [TÁTICA] Segredo exposto em chat operacional deve virar rotação coordenada sem repetir o valor

O App Secret Meta apareceu em contexto operacional durante a integração da Página Budamix. A memória deve registrar o risco e a ação necessária, mas nunca repetir o segredo. Quando credencial compartilhada vaza em transcript, a correção é rotação coordenada em todos os ambientes dependentes, com validação pós-rotação antes de ampliar automação.

## 2026-06-05 — [TÁTICA] ENVIOS FULL sem data de criação confiável não pode virar “envio novo do dia”

Na revisão do cron de ENVIOS FULL, Pedro corrigiu que um envio detectado após o cursor não é necessariamente um envio criado no dia, porque a planilha não guarda data operacional confiável de criação e o Supabase só carimba o processamento. Até existir campo de data preenchido pela operação, a linguagem correta é “detectado/adicionado após o último cursor” ou “registrado no processamento”, nunca “novo do dia”.

## 2026-06-05 — [TÁTICA] Idempotência de estoque via WhatsApp precisa bloquear também cópia ou reenvio da mesma entrada

No fluxo do grupo Estoque, lockfile, message ID e `external_event_id` único não bastavam para impedir duplicidade quando a mesma movimentação reaparecesse como nova mensagem. A proteção correta precisa combinar `business_date` em BRT, fingerprint do conteúdo operacional e busca de movimento equivalente no mesmo dia antes de aplicar saldo; em caso de colisão, bloquear automático e alertar divergência.

## 2026-06-05 — [TÁTICA] Imagem de estoque sem cabeçalho operacional não deve disparar inferência automática

No teste com imagem de canecas, o OCR leu corretamente os itens e quantidades, mas o automático ignorou porque faltava cabeçalho explícito como `ENTRADA`, `BAIXA` ou `AVARIA`. Essa trava é a regra certa: lista/imagem sem tipo operacional declarado não deve mexer em estoque por inferência; só pode ser processada manualmente com autorização explícita do Pedro.

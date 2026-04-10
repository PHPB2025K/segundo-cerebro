# Checklist Pre-Publicacao Shopee — Budamix

> Verificar TODOS os itens antes de chamar add_item.
> Se qualquer item falhar, corrigir ANTES de publicar.

## Dados do Produto
- [ ] Titulo: ate 120 chars, formato [Marca]+[Produto]+[Material]+[Specs]+[Qtd]
- [ ] Titulo contem "Budamix"
- [ ] Titulo contem material principal
- [ ] Titulo contem quantidade de pecas
- [ ] Titulo contem diferencial (corte laser, design exclusivo, etc)
- [ ] Categoria: leaf node verificada via get_category
- [ ] SKU: codigo interno Budamix preenchido
- [ ] Preco: verificado contra tabela de faixas (NAO em R$80)
- [ ] Estoque: quantidade real

## Especificacoes (100% preenchido)
- [ ] Todos os atributos da categoria obtidos (get_attributes ou teste iterativo)
- [ ] Marca = "Budamix" (NUNCA "Sem marca")
- [ ] Material preenchido com detalhes (ex: "MDF 6mm Alta Densidade")
- [ ] Dimensoes do produto
- [ ] Numero de pecas
- [ ] Features/funcionalidades (multi-value)
- [ ] Estampa/Pattern
- [ ] Estilo
- [ ] Garantia: tipo + duracao

## Descricao
- [ ] Usando template padrao Budamix (secao 5 do SKILL.md)
- [ ] Dentro de 3.000 chars
- [ ] Sem HTML, sem markdown
- [ ] Formatada com ◾ e ▪
- [ ] Contem: kit contents, diferenciais, fabricacao, ideal para, dimensoes, garantia

## Imagens
- [ ] 9 fotos (usar todas as slots)
- [ ] Todas em 1200x1200px
- [ ] Todas abaixo de 2MB
- [ ] Formato JPG ou PNG
- [ ] Foto 1: fundo limpo, produto centralizado, sem texto
- [ ] Ordem correta (hero, lifestyle, dimensoes, design, infografico, cenario, contexto, comparativo, flat lay)

## Tags
- [ ] Minimo 15 de 20 preenchidas
- [ ] Incluem: nome do produto, sinonimos, material, marca, uso
- [ ] Sem duplicatas

## Frete e Logistica
- [ ] Shopee Xpress (91003) habilitado
- [ ] Peso correto em kg
- [ ] Dimensoes da embalagem corretas (CxLxA em cm)

## Pos-Publicacao
- [ ] Item criado com sucesso (item_id retornado)
- [ ] Diagnostico de conteudo = "Qualificado" (barra verde)
- [ ] Registrado no Supabase
- [ ] Scripts de sync confirmados
- [ ] Pedro notificado no Telegram (Thread 3)

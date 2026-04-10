---
name: instagram
description: Consulta perfis públicos e posts do Instagram via RapidAPI (instagram120). Use para ver métricas, posts recentes, perfil de concorrentes, e análise de engajamento. Também usar quando Pedro pedir dados de qualquer conta pública do Instagram.
---

# Instagram — Consulta de Perfis e Posts

## Descrição

Acessa dados públicos de qualquer perfil do Instagram via API RapidAPI (instagram120). Retorna informações de perfil (seguidores, bio, posts) e posts recentes com métricas de engajamento (likes, comentários).

## Quando Usar

- Pedro pedir dados de um perfil do Instagram (GB, concorrentes, qualquer conta pública)
- Análise de engajamento ou performance de conteúdo
- Monitoramento de concorrentes
- Dados para relatórios de redes sociais

## Inputs Necessários

| Input | Obrigatório | Descrição |
|---|---|---|
| `username` | Sim | @ do perfil (sem o @). Ex: `gb_importadora` |
| `action` | Sim | `profile` ou `posts` |
| `maxId` | Não | ID para paginação de posts (string vazia = primeira página) |

**Credenciais:** RapidAPI Key (1Password: "RapidAPI - Tobias Agent")

## Passo a Passo de Execução

### Consultar perfil
```bash
{baseDir}/scripts/instagram.sh profile <username>
```

### Consultar posts recentes
```bash
{baseDir}/scripts/instagram.sh posts <username>
```

### Paginação (mais posts)
```bash
{baseDir}/scripts/instagram.sh posts <username> <maxId>
```

### Endpoints da API
- Perfil: `POST https://instagram120.p.rapidapi.com/api/instagram/profile`
- Posts: `POST https://instagram120.p.rapidapi.com/api/instagram/posts`

## Critérios de Qualidade

- Dados devem ser apresentados de forma estruturada (tabela ou bullets)
- Sempre incluir: seguidores, posts totais, engajamento médio
- Posts devem mostrar: data, likes, comentários, preview da legenda
- Se perfil for privado, informar claramente
- Link direto do post: `https://instagram.com/p/{code}`
- Rate limit: respeitar limites do plano free RapidAPI

## Contas Monitoradas

- `gb_importadora` — Perfil principal da GB / Budamix
- Adicionar concorrentes conforme solicitado pelo Pedro

## Aprendizados Incorporados

<!-- MELHORIA 2026-03-16 -->
### Estrutura de resposta da API instagram120
- Profile: dados em `result.` (username, full_name, biography, edge_followed_by.count, edge_follow.count, edge_owner_to_timeline_media.count)
- Posts: dados em `result.edges[].node.` (caption.text, like_count, comment_count, caption.created_at, code)
- Endpoint correto pra perfil: /api/instagram/profile (não /userinfo ou /user-info)
- Link do post: https://instagram.com/p/{code}
<!-- /MELHORIA -->

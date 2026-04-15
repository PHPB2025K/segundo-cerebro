---
title: Claude Code Skills — Guia de Uso e Pipeline Recomendado
created: 2026-04-14
type: reference
status: active
tags: [knowledge, tools, workflow]
---

# Claude Code Skills — Guia de Uso e Pipeline Recomendado

Pipeline recomendado para trabalho frontend e e-commerce com o stack de skills instalado.

---

## Pipeline Frontend / E-commerce

### 1. Design System
**Skill:** `/ecommerce-design-system`
Definir tokens, cores (Budamix palette), tipografia, espaçamentos e componentes base. Ponto de partida para qualquer projeto frontend.

### 2. Geração de Componentes
**Skills:** `/frontend-design` ou `/ui-ux-pro-max`
Criar componentes, páginas e layouts com alta qualidade de design. `/ui-ux-pro-max` para trabalho mais elaborado com múltiplos estilos e paletas.

### 3. Padrões de Arquitetura
**Skills:** `/composition-patterns` + `/react-best-practices`
Garantir arquitetura React escalável, evitar prop drilling, aplicar performance patterns da Vercel Engineering.

### 4. Storefront
**Skills:** `/storefront-best-practices` + `/ecommerce-product-page` + `/ecommerce-checkout`
Best practices específicas para e-commerce: PDPs, carrinho, checkout. Aplicar antes de finalizar qualquer fluxo de compra.

### 5. Polimento de UI
**Skill:** `/baseline-ui`
Anti-slop UI — remover elementos genéricos de IA, garantir identidade visual consistente e refinada.

### 6. Acessibilidade
**Skills:** `/fixing-accessibility` + `/web-design-guidelines`
Auditoria de acessibilidade (WCAG), contraste, navegação por teclado, ARIA. Rodar antes de deploy.

### 7. Performance
**Skills:** `/fixing-motion-performance` + `/react-best-practices`
Otimizar animações, evitar layout thrashing, aplicar memoização e lazy loading corretamente.

### 8. SEO
**Skills:** `/fixing-metadata` + `/ecommerce-seo`
Metadata completo (Open Graph, Twitter Cards, structured data), SEO específico para produto e categoria.

### 9. Pagamentos
**Skills:** `/stripe-payments` + `/ecommerce-checkout`
Integração Stripe (Checkout Sessions, Payment Intents, webhooks). Usar em conjunto com o checkout para cobertura completa.

### 10. Design Research
**Skills:** `/designer/*` (63 skills especializadas)
Consultar skills especializadas em áreas específicas: color theory, typography, motion design, brand identity, data visualization, icon design, etc.

---

## Referência Rápida por Caso de Uso

| Caso de Uso | Skills Recomendadas |
|-------------|---------------------|
| Novo projeto frontend | `/ecommerce-design-system` → `/frontend-design` |
| Componente React complexo | `/composition-patterns` + `/react-best-practices` |
| Página de produto (PDP) | `/storefront-best-practices` + `/ecommerce-product-page` |
| Fluxo de checkout | `/ecommerce-checkout` + `/stripe-payments` |
| Review de UI gerada | `/baseline-ui` + `/fixing-accessibility` |
| Animações lentas | `/fixing-motion-performance` |
| SEO e metadata | `/fixing-metadata` + `/ecommerce-seo` |
| Identidade visual | `/designer/brand-identity` + `/designer/color-theory` |
| Data viz / dashboards | `/designer/data-visualization` |

---

## Notas de Uso

- Skills do `designer/*` são invocadas com o prefixo do diretório: `/designer/typography`, `/designer/grid-systems`, etc.
- Skills do `designpowers/*` seguem o mesmo padrão: `/designpowers/skill-name`
- Sempre iniciar com `/ecommerce-design-system` em projetos novos para garantir consistência com a identidade Budamix
- Para projetos Budamix usar a paleta: Deep Teal `#004D4D`, Graphite `#132525`, Sage `#7EADAD`, Amber Gold `#C7A35A`, Terracota `#C56A4A`

---

## Links Relacionados

- [[claude-code-skills-inventario]]
- [[claude-code-skills-auditoria-2026-04-14]]

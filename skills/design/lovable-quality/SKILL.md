---
name: lovable-quality
description: >
  Regras obrigatórias de qualidade visual para todo projeto frontend.
  Baseado na metodologia Lovable: design system first, tokens semânticos,
  cores HSL, sombras coloridas, gradientes, transições cubic-bezier,
  CVA variants, dados mock realistas, mobile-first.
  DEVE ser referenciada em TODO briefing de frontend do Builder.
---

# Lovable-Quality — Padrão de Qualidade Visual

> Usado por [[openclaw/agents/builder/IDENTITY|Builder]]

## REGRA ABSOLUTA: Design System First

Antes de criar QUALQUER componente, o Builder DEVE:

1. **Definir `src/app/globals.css`** com tokens semânticos completos (mínimo 40 tokens)
2. **Extender `tailwind.config.ts`** com todos os tokens
3. **Só então** criar componentes que APENAS consomem tokens

### Tokens Obrigatórios em globals.css

```css
@layer base {
  :root {
    /* Cores base (HSL) */
    --background: 0 0% 4%;
    --foreground: 0 0% 95%;
    --card: 0 0% 7%;
    --card-foreground: 0 0% 95%;
    --primary: [definir por projeto];
    --primary-foreground: [definir por projeto];
    --secondary: [definir por projeto];
    --muted: 0 0% 15%;
    --muted-foreground: 0 0% 64%;
    --accent: [definir por projeto];
    --destructive: 0 84% 60%;
    --border: 0 0% 15%;
    --input: 0 0% 15%;
    --ring: [primary];
    --radius: 0.75rem;

    /* TOKENS AVANÇADOS — o que diferencia de output genérico */
    --primary-glow: [versão mais clara do primary];
    --gradient-primary: linear-gradient(135deg, hsl(var(--primary)), hsl(var(--primary-glow)));
    --gradient-subtle: linear-gradient(180deg, hsl(var(--card)), hsl(var(--background)));
    --gradient-hero: linear-gradient(135deg, hsl(var(--primary) / 0.15), hsl(var(--accent) / 0.1));
    --shadow-sm: 0 1px 2px hsl(0 0% 0% / 0.3);
    --shadow-md: 0 4px 12px hsl(0 0% 0% / 0.4);
    --shadow-lg: 0 10px 30px -10px hsl(var(--primary) / 0.3);
    --shadow-glow: 0 0 40px hsl(var(--primary-glow) / 0.15);
    --shadow-elevated: 0 8px 30px hsl(0 0% 0% / 0.5), 0 0 1px hsl(0 0% 100% / 0.05);
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-smooth: 300ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-spring: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);

    /* Spacing generoso */
    --section-padding: 4rem;
    --section-padding-lg: 6rem;
    --card-padding: 1.5rem;
  }
}
```

### tailwind.config.ts Obrigatório

```typescript
// TODOS os tokens de globals.css devem estar aqui
extend: {
  colors: {
    background: "hsl(var(--background))",
    foreground: "hsl(var(--foreground))",
    primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" },
    // ... todos os tokens
  },
  boxShadow: {
    sm: "var(--shadow-sm)",
    md: "var(--shadow-md)",
    lg: "var(--shadow-lg)",
    glow: "var(--shadow-glow)",
    elevated: "var(--shadow-elevated)",
  },
  backgroundImage: {
    "gradient-primary": "var(--gradient-primary)",
    "gradient-subtle": "var(--gradient-subtle)",
    "gradient-hero": "var(--gradient-hero)",
  },
  transitionTimingFunction: {
    smooth: "cubic-bezier(0.4, 0, 0.2, 1)",
    spring: "cubic-bezier(0.34, 1.56, 0.64, 1)",
  },
}
```

## REGRAS DE IMPLEMENTAÇÃO

### Cores — PROIBIDO hardcodar
```
ERRADO: className="bg-blue-500 text-white"
ERRADO: className="bg-[#4285F4] text-[#e8e9ed]"
CERTO:  className="bg-primary text-primary-foreground"
CERTO:  className="bg-gradient-primary text-foreground"
```

### Sombras — SEMPRE coloridas com primary
```
ERRADO: className="shadow-md"
CERTO:  className="shadow-lg" (que mapeia para hsl(var(--primary) / 0.3))
CERTO:  className="shadow-glow hover:shadow-elevated"
```

### Transições — NUNCA sem easing
```
ERRADO: className="transition-all"
CERTO:  className="transition-all duration-300 ease-smooth"
```

### Componentes — CVA obrigatório para variantes
```typescript
import { cva, type VariantProps } from "class-variance-authority";

const cardVariants = cva(
  "rounded-xl border transition-all duration-300 ease-smooth",
  {
    variants: {
      variant: {
        default: "border-border bg-card shadow-sm hover:shadow-md hover:border-primary/20",
        elevated: "border-border/50 bg-card shadow-elevated hover:shadow-glow",
        glass: "border-white/10 bg-white/5 backdrop-blur-xl",
        gradient: "border-primary/20 bg-gradient-subtle",
      },
    },
    defaultVariants: { variant: "default" },
  }
);
```

### Espaçamento — GENEROSO
```
Seções: py-16 lg:py-24 (não py-4 ou py-6)
Cards: p-6 lg:p-8 (não p-4)
Gaps em grids: gap-6 lg:gap-8 (não gap-4)
Headers: mb-8 lg:mb-12 (não mb-4)
```

### Tipografia — Hierarquia dramática
```
h1: text-3xl lg:text-5xl font-bold tracking-tight
h2: text-2xl lg:text-3xl font-semibold
h3: text-lg lg:text-xl font-medium
body: text-sm lg:text-base text-muted-foreground
label: text-xs uppercase tracking-wider text-muted-foreground font-medium
```

### Hover states — SEMPRE com feedback visual
```
Cards: hover:shadow-lg hover:border-primary/20 hover:-translate-y-0.5
Botões: hover:opacity-90 active:scale-[0.98]
Links: hover:text-primary transition-colors
Rows: hover:bg-muted/50
```

### Loading states — SKELETON, não spinner
```typescript
// ERRADO: spinner genérico
<div className="animate-spin rounded-full border-2" />

// CERTO: skeleton que imita o layout
<div className="animate-pulse space-y-4">
  <div className="h-8 w-48 rounded-lg bg-muted" />
  <div className="grid grid-cols-4 gap-4">
    {[...Array(4)].map((_, i) => (
      <div key={i} className="h-24 rounded-xl bg-muted" />
    ))}
  </div>
</div>
```

### Dados mock — OBRIGATÓRIO
Todo dashboard/listagem DEVE ter dados mock realistas hardcoded como fallback quando a API não está configurada. O usuário precisa ver o design com dados, não tela vazia.

```typescript
const MOCK_DATA: KPIData = {
  spend: 12450.80,
  revenue: 89234.50,
  roas: 7.17,
  cpa: 18.42,
  impressions: 1243567,
  clicks: 34521,
  conversions: 676,
  ctr: 2.78,
  cpc: 0.36,
  cpm: 10.01,
};
```

### Animações de entrada — Staggered
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-in { animation: fadeInUp 0.5s ease-out forwards; }
.delay-1 { animation-delay: 75ms; }
.delay-2 { animation-delay: 150ms; }
.delay-3 { animation-delay: 225ms; }
.delay-4 { animation-delay: 300ms; }
```

## CHECKLIST PRÉ-ENTREGA

Antes de marcar qualquer componente como pronto:

- [ ] Design system definido ANTES dos componentes (globals.css + tailwind.config.ts)
- [ ] Zero cores hardcoded (sem bg-blue-500, text-white, bg-[#xxx])
- [ ] Sombras coloridas com primary (não shadow-md genérico)
- [ ] Gradientes definidos como tokens
- [ ] Transições com cubic-bezier (não transition-all sozinho)
- [ ] CVA variants em componentes reutilizáveis
- [ ] Espaçamento generoso (py-16+ em seções)
- [ ] Tipografia com hierarquia dramática
- [ ] Hover states em TODOS os elementos interativos
- [ ] Skeleton loaders (não spinners)
- [ ] Dados mock realistas como fallback
- [ ] Animações de entrada staggered
- [ ] Mobile-first responsivo
- [ ] Semantic HTML (header, nav, main, section, footer)

## REFERÊNCIAS COMPLEMENTARES

Usar em conjunto com:
- `skills/design/superdesign/SKILL.md` — workflow de design (layout → tema → animação → implementação)
- `skills/design/frontend-design-ultimate/SKILL.md` — estéticas anti-genéricas, tons ousados
- `skills/design/shadcn-ui/SKILL.md` — patterns avançados shadcn

---

## Ver também

- [[skills/design/frontend-design-ultimate/SKILL|Frontend Design Ultimate — Skill]]

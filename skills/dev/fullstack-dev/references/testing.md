---
title: "testing"
created: 2026-04-14
type: skill
domain: dev
status: active
tags:
  - skill/dev
---

# Testing Reference — Vitest, Playwright, E2E, Mocking

## Índice
1. [Vitest — Unit/Integration](#1-vitest)
2. [Testing Library — Componentes React](#2-testing-library)
3. [Mocking — Estratégias](#3-mocking)
4. [Playwright — E2E](#4-playwright)
5. [Estratégia de Testes](#5-estratégia)

---

## 1. Vitest

### Configuração

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: ['./test/setup.ts'],
    globals: true,                      // describe, it, expect sem import
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      include: ['src/**/*.{ts,tsx}'],
      exclude: ['src/**/*.test.*', 'src/types/**'],
      thresholds: { lines: 70, branches: 60, functions: 70 },
    },
  },
  resolve: {
    alias: { '@': resolve(__dirname, './src') },
  },
})

// test/setup.ts
import '@testing-library/jest-dom'
import { vi } from 'vitest'

// Mock de módulos globais
vi.mock('next/navigation', () => ({
  useRouter: () => ({ push: vi.fn(), refresh: vi.fn() }),
  usePathname: () => '/',
  redirect: vi.fn(),
}))

vi.mock('next/headers', () => ({
  cookies: () => ({
    get: vi.fn(),
    set: vi.fn(),
    getAll: vi.fn(() => []),
  }),
}))
```

### Testes de Funções/Services

```ts
// src/features/simulations/__tests__/calculator.test.ts
import { describe, it, expect, beforeEach, vi } from 'vitest'
import { calculateImportCost } from '../calculator'

describe('calculateImportCost', () => {
  it('calculates FOB correctly', () => {
    const result = calculateImportCost({
      fobValue: 2.50,      // USD por unidade
      quantity: 1000,
      freightCost: 500,    // USD total
      exchangeRate: 5.20,  // BRL/USD
      ncm: '70109000',
    })

    expect(result.totalCost).toBeGreaterThan(0)
    expect(result.costPerUnit).toBeCloseTo(result.totalCost / 1000, 2)
    expect(result.breakdown).toHaveProperty('fob')
    expect(result.breakdown).toHaveProperty('freight')
    expect(result.breakdown).toHaveProperty('taxes')
  })

  it('throws for invalid NCM', () => {
    expect(() => calculateImportCost({ ...validInput, ncm: 'invalid' }))
      .toThrow('NCM inválido')
  })

  it('handles zero freight (EXW)', () => {
    const result = calculateImportCost({ ...validInput, freightCost: 0, incoterm: 'EXW' })
    expect(result.breakdown.freight).toBe(0)
  })
})

// Service com dependências
describe('SimulationService', () => {
  let service: SimulationService
  let mockRepo: MockInstance<SimulationRepository>
  let mockEmail: MockInstance<EmailService>

  beforeEach(() => {
    mockRepo = {
      create: vi.fn(),
      findById: vi.fn(),
      findMany: vi.fn(),
      update: vi.fn(),
      delete: vi.fn(),
    }
    mockEmail = { send: vi.fn().mockResolvedValue(undefined) }
    service = new SimulationService(mockRepo, mockEmail)
  })

  it('creates simulation and sends confirmation', async () => {
    const input = { productName: 'Pote', fobValue: 2.50, orgId: 'org1', userId: 'user1' }
    const created = { id: 'sim1', ...input, createdAt: new Date() }

    mockRepo.create.mockResolvedValue(created)

    const result = await service.createSimulation(input)

    expect(mockRepo.create).toHaveBeenCalledWith(input)
    expect(mockEmail.send).toHaveBeenCalledWith(
      expect.objectContaining({ type: 'simulation_created' })
    )
    expect(result).toEqual(created)
  })

  it('enforces usage limit', async () => {
    vi.spyOn(service, 'checkLimit').mockResolvedValue({ exceeded: true, remaining: 0 })

    await expect(service.createSimulation(input)).rejects.toThrow('Limite atingido')
  })
})
```

---

## 2. Testing Library

```tsx
// src/features/simulations/__tests__/SimulationForm.test.tsx
import { render, screen, fireEvent, waitFor, userEvent } from '@testing-library/react'
import { describe, it, expect, vi } from 'vitest'
import { SimulationForm } from '../SimulationForm'

const setup = () => {
  const onSubmit = vi.fn().mockResolvedValue({ success: true })
  const utils = render(<SimulationForm onSubmit={onSubmit} />)
  return { ...utils, onSubmit }
}

describe('SimulationForm', () => {
  it('renders all required fields', () => {
    setup()
    expect(screen.getByLabelText(/nome do produto/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/valor fob/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/quantidade/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/ncm/i)).toBeInTheDocument()
  })

  it('shows validation errors on empty submit', async () => {
    setup()
    const user = userEvent.setup()

    await user.click(screen.getByRole('button', { name: /simular/i }))

    await waitFor(() => {
      expect(screen.getByText(/obrigatório/i)).toBeInTheDocument()
    })
  })

  it('submits valid data correctly', async () => {
    const { onSubmit } = setup()
    const user = userEvent.setup()

    await user.type(screen.getByLabelText(/nome do produto/i), 'Pote de Vidro 500ml')
    await user.type(screen.getByLabelText(/valor fob/i), '2.50')
    await user.type(screen.getByLabelText(/quantidade/i), '1000')
    await user.type(screen.getByLabelText(/ncm/i), '70109000')

    await user.click(screen.getByRole('button', { name: /simular/i }))

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith(
        expect.objectContaining({
          productName: 'Pote de Vidro 500ml',
          fobValue: 2.50,
          quantity: 1000,
          ncm: '70109000',
        })
      )
    })
  })

  it('disables button while submitting', async () => {
    const onSubmit = vi.fn(() => new Promise(resolve => setTimeout(resolve, 100)))
    render(<SimulationForm onSubmit={onSubmit} />)
    const user = userEvent.setup()

    await fillValidForm(user)
    await user.click(screen.getByRole('button', { name: /simular/i }))

    expect(screen.getByRole('button', { name: /simulando/i })).toBeDisabled()
    await waitFor(() => expect(screen.getByRole('button', { name: /simular/i })).not.toBeDisabled())
  })
})

// Testes de hooks customizados
import { renderHook, act } from '@testing-library/react'
import { useSimulations } from '../hooks/useSimulations'

describe('useSimulations', () => {
  it('fetches simulations on mount', async () => {
    const { result } = renderHook(() => useSimulations({ orgId: 'org1' }), {
      wrapper: QueryClientWrapper, // wrapper com QueryClientProvider
    })

    expect(result.current.isLoading).toBe(true)
    await waitFor(() => expect(result.current.isLoading).toBe(false))
    expect(result.current.data).toBeDefined()
  })
})
```

---

## 3. Mocking

### Estratégias

```ts
// 1. Spy — observar chamadas sem substituir implementação
const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
// ... código que dispara console.error
expect(consoleSpy).toHaveBeenCalledWith(expect.stringContaining('Error'))
consoleSpy.mockRestore()

// 2. Mock — substituir completamente
vi.mock('@/lib/db', () => ({
  db: {
    query: {
      simulations: {
        findMany: vi.fn().mockResolvedValue([]),
        findFirst: vi.fn().mockResolvedValue(null),
      }
    },
    insert: vi.fn(() => ({ values: vi.fn().mockResolvedValue([{ id: 'test-id' }]) })),
  }
}))

// 3. Factory mock (mais flexível)
function createMockDb(overrides?: Partial<typeof db>) {
  return {
    query: {
      simulations: {
        findMany: vi.fn().mockResolvedValue([]),
        findFirst: vi.fn().mockResolvedValue(null),
      }
    },
    insert: vi.fn(() => ({ values: vi.fn().mockResolvedValue([mockSimulation]) })),
    ...overrides,
  }
}

// 4. MSW — interceptar requests HTTP (melhor para integração)
import { http, HttpResponse } from 'msw'
import { setupServer } from 'msw/node'

const server = setupServer(
  http.get('/api/simulations', ({ request }) => {
    const url = new URL(request.url)
    const page = url.searchParams.get('page')
    return HttpResponse.json({
      data: page === '2' ? [] : [mockSimulation],
      meta: { total: 1, page: 1, limit: 20 },
    })
  }),

  http.post('/api/simulations', async ({ request }) => {
    const body = await request.json()
    return HttpResponse.json({ id: 'new-sim', ...body }, { status: 201 })
  })
)

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

// Simular erro específico
it('handles API error gracefully', async () => {
  server.use(
    http.get('/api/simulations', () => {
      return HttpResponse.json({ error: 'Service unavailable' }, { status: 503 })
    })
  )
  // ... testar comportamento de erro
})
```

### Fixtures / Test Data

```ts
// test/fixtures/simulation.ts
import type { Simulation } from '@/types'

export const mockSimulation: Simulation = {
  id: '550e8400-e29b-41d4-a716-446655440000',
  orgId: '550e8400-e29b-41d4-a716-446655440001',
  userId: '550e8400-e29b-41d4-a716-446655440002',
  productName: 'Pote de Vidro 500ml',
  fobValue: '2.50',
  quantity: 1000,
  ncm: '70109000',
  incoterm: 'FOB',
  status: 'completed',
  result: JSON.stringify({ totalCost: 15000, costPerUnit: 15 }),
  createdAt: new Date('2026-01-01T10:00:00Z'),
}

// Factory com defaults + overrides
export function createSimulation(overrides: Partial<Simulation> = {}): Simulation {
  return { ...mockSimulation, id: crypto.randomUUID(), ...overrides }
}
```

---

## 4. Playwright

### Configuração

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [['html'], ['list']],
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    // { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } },
  ],
  webServer: {
    command: 'pnpm dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

### Testes E2E

```ts
// e2e/simulation.spec.ts
import { test, expect, Page } from '@playwright/test'

// Helper de login (auth state)
async function loginAsUser(page: Page) {
  await page.goto('/login')
  await page.getByLabel('Email').fill('test@gb.com')
  await page.getByLabel('Senha').fill('test-password-123')
  await page.getByRole('button', { name: 'Entrar' }).click()
  await expect(page).toHaveURL('/dashboard')
}

// Reusar auth entre testes (economiza tempo)
test.describe('Simulations', () => {
  test.use({ storageState: 'e2e/.auth/user.json' }) // auth salvo

  test('create and view simulation', async ({ page }) => {
    await page.goto('/dashboard/simulations/new')

    // Preencher formulário
    await page.getByLabel('Nome do Produto').fill('Pote de Vidro 500ml')
    await page.getByLabel('Valor FOB (USD)').fill('2.50')
    await page.getByLabel('Quantidade').fill('1000')
    await page.getByLabel('NCM').fill('70109000')
    await page.getByRole('combobox', { name: 'País de Origem' }).selectOption('CN')

    await page.getByRole('button', { name: 'Simular Importação' }).click()

    // Verificar resultado
    await expect(page.getByText('Simulação criada')).toBeVisible({ timeout: 5000 })
    await expect(page.getByTestId('total-cost')).toContainText('R$')
    await expect(page.getByTestId('cost-per-unit')).toBeVisible()
  })

  test('validation errors are shown', async ({ page }) => {
    await page.goto('/dashboard/simulations/new')
    await page.getByRole('button', { name: 'Simular Importação' }).click()

    await expect(page.getByText('Nome do produto é obrigatório')).toBeVisible()
  })

  test('simulation appears in list', async ({ page }) => {
    // Criar simulação via API (mais rápido que UI)
    const response = await page.request.post('/api/simulations', {
      data: { productName: 'Test Product', fobValue: 2.50, quantity: 100, ncm: '70109000' }
    })
    expect(response.status()).toBe(201)

    await page.goto('/dashboard/simulations')
    await expect(page.getByText('Test Product')).toBeVisible()
  })
})

// Salvar auth state
// e2e/auth.setup.ts
import { test as setup, expect } from '@playwright/test'

setup('authenticate', async ({ page }) => {
  await page.goto('/login')
  await page.getByLabel('Email').fill('test@gb.com')
  await page.getByLabel('Senha').fill('test-password-123')
  await page.getByRole('button', { name: 'Entrar' }).click()
  await expect(page.url()).toContain('/dashboard')
  await page.context().storageState({ path: 'e2e/.auth/user.json' })
})
```

### Page Objects (reutilização)

```ts
// e2e/pages/SimulationPage.ts
import { Page, Locator } from '@playwright/test'

export class SimulationPage {
  readonly page: Page
  readonly form: Locator
  readonly submitButton: Locator
  readonly resultCard: Locator

  constructor(page: Page) {
    this.page = page
    this.form = page.locator('form[data-testid="simulation-form"]')
    this.submitButton = page.getByRole('button', { name: 'Simular' })
    this.resultCard = page.getByTestId('simulation-result')
  }

  async goto() {
    await this.page.goto('/dashboard/simulations/new')
  }

  async fillForm(data: { productName: string; fobValue: string; quantity: string; ncm: string }) {
    await this.page.getByLabel('Nome do Produto').fill(data.productName)
    await this.page.getByLabel('Valor FOB').fill(data.fobValue)
    await this.page.getByLabel('Quantidade').fill(data.quantity)
    await this.page.getByLabel('NCM').fill(data.ncm)
  }

  async submit() {
    await this.submitButton.click()
  }

  async waitForResult() {
    await this.resultCard.waitFor({ state: 'visible', timeout: 10000 })
    return this.resultCard
  }
}

// Uso no teste
test('full simulation flow', async ({ page }) => {
  const simPage = new SimulationPage(page)
  await simPage.goto()
  await simPage.fillForm({ productName: 'Pote', fobValue: '2.5', quantity: '1000', ncm: '70109000' })
  await simPage.submit()
  const result = await simPage.waitForResult()
  await expect(result).toContainText('R$')
})
```

---

## 5. Estratégia

### Pirâmide de Testes

```
        /\
       /E2E\        — Poucos, críticos, lentos. Fluxos principais.
      /------\
     /Integra-\     — Médio. Testa componentes + API juntos.
    / ção      \
   /------------\
  / Unit Tests   \  — Muitos, rápidos. Lógica de negócio pura.
 /________________\
```

### O que testar em cada camada

```
Unit (Vitest):
✅ Calculadoras e funções puras (calculateImportCost)
✅ Transformações de dados
✅ Validações Zod
✅ Business logic dos services
❌ Não testar UI básica sem lógica

Integration (Vitest + MSW):
✅ Server Actions (com DB mockado)
✅ Componentes com estado complexo
✅ Hooks com TanStack Query
✅ Auth flows

E2E (Playwright):
✅ Fluxo completo de signup → uso
✅ Checkout Stripe (modo teste)
✅ Criação e consulta de simulação
✅ Login, logout, redirect correto
❌ Não testar cada botão e input
```

### Scripts de teste

```json
{
  "scripts": {
    "test": "vitest",
    "test:watch": "vitest --watch",
    "test:coverage": "vitest --coverage",
    "test:ui": "vitest --ui",
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui",
    "test:e2e:debug": "playwright test --debug"
  }
}
```

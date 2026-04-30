---
title: "SOP: Edição de Planilhas no Google Sheets via Claude Code"
created: 2026-04-15
type: sop
status: active
tags:
  - automacoes
  - sop
  - google-sheets
  - precificacao
---

# SOP: Edição de Planilhas no Google Sheets via Claude Code

> **Regra absoluta:** NUNCA editar planilhas de estoque/precificação como arquivos locais.
> A planilha do Google Drive é a ÚNICA fonte de verdade.

---

## Planilhas Oficiais

| Planilha | Google Sheets ID | Uso |
|----------|-----------------|-----|
| **Precificação** | `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI` | Abas ESTOQUE, SHOPEE, MELI, AMAZON, MIMO STYLE — preços, margens, custos. **Lida pelo `sync-costs.py`** (corrigido em 30/04/2026 — antes apontava errado para a outra planilha). |
| **Estoque Operacional** | `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU` | Controle entrada/saída do armazém Pedreira-SP. NÃO usada pelo sync-costs.py. |

---

## Acesso Configurado

| Componente | Path | Notas |
|------------|------|-------|
| OAuth Client | `~/Downloads/client_secret_264539490125-*.json` | Projeto `integracaoopenclaw-490318` |
| Token persistente | `~/.config/google-sheets-claude/token.json` | Refresh token, não expira. chmod 600 |
| Python libs | `gspread`, `google-auth`, `google-auth-oauthlib` | Instalados via pip3 |
| Scopes | `spreadsheets` + `drive.file` | Leitura e escrita |
| Conta autorizada | pehpbroglio@gmail.com | Owner da planilha |

---

## Fluxo de Edição (Preferido: API Direta)

### Passo 1 — Conectar

```python
import gspread
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import json, os

TOKEN_FILE = os.path.expanduser("~/.config/google-sheets-claude/token.json")
with open(TOKEN_FILE) as f:
    token_data = json.load(f)

creds = Credentials(
    token=token_data['token'],
    refresh_token=token_data['refresh_token'],
    token_uri=token_data['token_uri'],
    client_id=token_data['client_id'],
    client_secret=token_data['client_secret'],
    scopes=token_data['scopes']
)
if creds.expired:
    creds.refresh(Request())
    token_data['token'] = creds.token
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f, indent=2)

gc = gspread.authorize(creds)
```

### Passo 2 — Abrir planilha

```python
SSID = "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI"
sh = gc.open_by_key(SSID)
ws = sh.worksheet("SHOPEE")  # ou "MELI", "AMAZON", "ESTOQUE"
```

### Passo 3 — Ler (fórmulas ou valores)

```python
# Valor calculado
val = ws.acell('H4').value

# Fórmula original
formula = ws.acell('H4', value_render_option='FORMULA').value

# Batch read
data = ws.get('A4:U75')
formulas = ws.get('H4:H75', value_render_option='FORMULA')
```

### Passo 4 — Escrever

```python
# Célula única
ws.update_acell('H4', '=G4*IF(G4<=7,99;0,5;IF(G4<=79,99;0,2;0,14))')

# Batch (muito mais eficiente)
formulas = [[f'=G{r}*0.2'] for r in range(4, 76)]
ws.update(range_name='H4:H75', values=formulas, value_input_option='USER_ENTERED')
```

---

## Regras Importantes

### Locale pt-BR
Google Sheets em português usa `;` como separador de argumentos (não `,`):
```
CORRETO:   =IF(G4<=79,99;4;IF(G4<=99,99;16;20))
ERRADO:    =IF(G4<=79.99,4,IF(G4<=99.99,16,20))
```

Ao usar `value_input_option='USER_ENTERED'`, o Google Sheets aceita **ambos** os formatos e converte automaticamente. Mas ao LER fórmulas, elas vêm no formato pt-BR (`;`).

### Rate Limits
- **60 read requests/minuto** por usuário
- **60 write requests/minuto** por usuário
- Usar `time.sleep(1-3)` entre operações batch
- Preferir batch (`ws.update()`) sobre células individuais (`ws.update_acell()`)

### Formatação
- A API do gspread altera **apenas conteúdo** das células
- Formatação (cores, fontes, bordas) NÃO é afetada por `update()`
- Para alterar formatação, usar `ws.format()` (raramente necessário)

### Segurança
- Token em `~/.config/google-sheets-claude/token.json` com chmod 600
- Refresh token não expira (a menos que o usuário revogue)
- Se token inválido: rodar `python3 /tmp/google_sheets_auth.py` novamente

---

## Fluxo Alternativo (Download/Upload)

Se a API direta não funcionar (ex: rate limit, formatação complexa):

1. **Baixar:** `curl -sL -o /tmp/planilha.xlsx "https://docs.google.com/spreadsheets/d/${SSID}/export?format=xlsx"`
2. **Editar:** openpyxl com `data_only=False` (preserva fórmulas e formatação)
3. **Subir:** Pedro faz upload manual via Google Sheets > Arquivo > Importar > Substituir
4. **Confirmar:** Verificar via API que as alterações estão no Drive

---

## Reautorização (se necessário)

Se o token expirar ou for revogado:

```bash
python3 /tmp/google_sheets_auth.py
```

Ou recriar o script:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
import json, os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
CLIENT_SECRET = os.path.expanduser("~/Downloads/client_secret_264539490125-*.json")
TOKEN_FILE = os.path.expanduser("~/.config/google-sheets-claude/token.json")

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
creds = flow.run_local_server(port=8090, prompt='consent', access_type='offline')

token_data = {
    'token': creds.token, 'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri, 'client_id': creds.client_id,
    'client_secret': creds.client_secret, 'scopes': list(creds.scopes),
}
with open(TOKEN_FILE, 'w') as f:
    json.dump(token_data, f, indent=2)
os.chmod(TOKEN_FILE, 0o600)
```

---

## Histórico

| Data | Ação |
|------|------|
| 15/04/2026 | Setup inicial: OAuth configurado, token salvo, 4 correções aplicadas na aba SHOPEE |

---

## Ver também

- [[memory/context/pendencias|Pendências]]
- [[skills/spreadsheet-pricing/SKILL|Skill Spreadsheet Pricing]]
- [[skills/marketplace/shopee-fees-rules/SKILL|Regras Shopee 2026]]

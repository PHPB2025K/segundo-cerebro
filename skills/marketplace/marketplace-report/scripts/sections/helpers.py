"""
Helpers compartilhados entre seções do relatório ML.
Formatação, badges, constantes e utilitários.
"""

import base64
import os

# ─── Paths ───────────────────────────────────────────────────────────────────

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(SKILL_DIR, 'assets')

# ─── Formatação ──────────────────────────────────────────────────────────────

def fmt_currency(val):
    if val is None: return "N/D"
    return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def fmt_pct(val):
    if val is None: return "N/D"
    return f"{val:.1f}%"

def fmt_number(val):
    if val is None: return "N/D"
    return f"{val:,.0f}".replace(",", ".")

def safe_div(a, b, default=0):
    return a / b if b and b != 0 else default

# ─── Badges HTML ─────────────────────────────────────────────────────────────

def variation_badge(current, previous):
    if previous is None or previous == 0 or current is None:
        return '<span class="badge badge-neutral">N/D</span>'
    pct = ((current - previous) / abs(previous)) * 100
    if pct > 0:
        return f'<span class="badge badge-positive">↑ {pct:.1f}%</span>'
    elif pct < 0:
        return f'<span class="badge badge-negative">↓ {abs(pct):.1f}%</span>'
    return '<span class="badge badge-neutral">= 0%</span>'

def status_badge(value, thresholds, labels=('Saudável', 'Atenção', 'Crítico')):
    """thresholds = (green_max, yellow_max)"""
    if value <= thresholds[0]:
        return ('🟢', labels[0], 'positive')
    elif value <= thresholds[1]:
        return ('🟡', labels[1], 'warning')
    return ('🔴', labels[2], 'negative')

# ─── Assets ──────────────────────────────────────────────────────────────────

def logo_base64(filename='budamix-logo-teal.png'):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

# ─── Constantes ──────────────────────────────────────────────────────────────

NOT_AVAILABLE = '<span class="na">Dado não disponível — solicitar para próxima análise</span>'
USER_ID = 532562281
SELLER_NAME = "GB Importadora"
BRAND_NAME = "Budamix"

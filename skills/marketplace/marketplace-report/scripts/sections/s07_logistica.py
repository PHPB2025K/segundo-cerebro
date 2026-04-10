"""Seção 07 — Logística & Envios"""

from collections import Counter
from .helpers import *
from .icons import icon

def needs_data():
    return ['orders']

def build(orders, **kwargs):
    paid_orders = [o for o in orders if o.get('status') == 'paid']
    total_shipped = len(paid_orders)

    modes = Counter()
    for o in paid_orders:
        shipping = o.get('shipping', {})
        mode = shipping.get('shipping_mode', 'N/D') if shipping else 'N/D'
        modes[mode] += 1

    modes_rows = ''.join(
        f'<tr><td>{mode}</td><td class="number">{count}</td><td class="number">{fmt_pct(safe_div(count, total_shipped)*100)}</td></tr>'
        for mode, count in modes.most_common())

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">07</span><h2>🚚 Logística & Envios</h2></div>
        <div class="kpi-grid">
            <div class="kpi-row">
                <div class="kpi-card kpi-primary"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('envios')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(total_shipped)}</span><span class="kpi-label">Total Envios</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('tempo')}</span></div><div class="kpi-content"><span class="kpi-value">{NOT_AVAILABLE}</span><span class="kpi-label">Tempo Médio</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('prazo')}</span></div><div class="kpi-content"><span class="kpi-value">{NOT_AVAILABLE}</span><span class="kpi-label">% No Prazo</span></div></div></div>
            </div>
        </div>
        <h3>Modos de Envio</h3>
        <table class="data-table"><thead><tr><th>Modo</th><th>Qtd</th><th>%</th></tr></thead><tbody>{modes_rows}</tbody></table>
        <div class="insight-box"><span class="insight-icon">💡</span><div class="insight-content">
            <strong>Insight:</strong> Dados detalhados de tempo de envio requerem exportação manual do painel ML.
        </div></div>
    </div>'''

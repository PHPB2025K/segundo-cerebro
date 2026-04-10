"""Seção 03 — Volume de Vendas & Conversão"""

from collections import defaultdict
from .helpers import *
from .icons import icon
import sys, os

def _charts():
    import importlib.util
    spec = importlib.util.spec_from_file_location("ml_charts",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "charts.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def needs_data():
    return ['orders']

def build(orders, **kwargs):
    charts = _charts()
    paid_orders = [o for o in orders if o.get('status') == 'paid']
    cancelled = [o for o in orders if o.get('status') == 'cancelled']
    total = len(orders)

    daily = defaultdict(int)
    for o in paid_orders:
        day = o.get('date_created', '')[:10]
        daily[day] += 1

    sorted_days = sorted(daily.keys())
    day_labels = [d[5:] for d in sorted_days]
    day_values = [daily[d] for d in sorted_days]
    orders_chart = charts.bar_chart(day_labels, day_values, title='Pedidos por Dia', color='#004D4D', width=10, height=4)
    avg_daily = safe_div(sum(day_values), len(day_values))

    product_units = defaultdict(int)
    for o in paid_orders:
        for item in o.get('order_items', []):
            title = item.get('item', {}).get('title', '?')[:40]
            product_units[title] += item.get('quantity', 1)

    top_units = sorted(product_units.items(), key=lambda x: x[1], reverse=True)[:10]
    units_rows = ''.join(f'<tr><td class="rank"><span class="rank-badge">{i}</span></td><td>{name}</td><td class="number">{fmt_number(qty)}</td></tr>'
                         for i, (name, qty) in enumerate(top_units, 1))

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">03</span><h2>📦 Volume de Vendas & Conversão</h2></div>
        <div class="kpi-grid">
            <div class="kpi-row">
                <div class="kpi-card kpi-primary"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('pedidos')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(len(paid_orders))}</span><span class="kpi-label">Pedidos Pagos</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('media')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(avg_daily)}</span><span class="kpi-label">Média Diária</span></div></div></div>
                <div class="kpi-card kpi-negative"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('cancelado')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(len(cancelled))}</span><span class="kpi-label">Cancelados</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('aprovacao')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_pct(safe_div(len(paid_orders), total)*100)}</span><span class="kpi-label">Aprovação</span></div></div></div>
            </div>
        </div>
        <div class="chart-container"><img src="data:image/png;base64,{orders_chart}" class="chart-img"></div>
        <h3>🏆 Top 10 Produtos por Unidades Vendidas</h3>
        <table class="data-table"><thead><tr><th>#</th><th>Produto</th><th>Unidades</th></tr></thead><tbody>{units_rows}</tbody></table>
        <div class="insight-box"><span class="insight-icon">💡</span><div class="insight-content">
            <strong>Insight:</strong> Média de {fmt_number(avg_daily)} pedidos/dia. Foco em manter volume constante e reduzir cancelamentos ({fmt_pct(safe_div(len(cancelled), total)*100)}).
        </div></div>
    </div>'''

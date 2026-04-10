"""Seção 02 — Faturamento & Receita"""

from collections import defaultdict
from .helpers import *
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from importlib import import_module

def _charts():
    import importlib.util
    spec = importlib.util.spec_from_file_location("ml_charts",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ml-charts.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def needs_data():
    return ['orders', 'payments']

def build(orders, payments, **kwargs):
    charts = _charts()
    paid_orders = [o for o in orders if o.get('status') == 'paid']
    total_revenue = sum(o.get('total_amount', 0) for o in paid_orders)

    # Daily revenue
    daily = defaultdict(lambda: {'revenue': 0, 'orders': 0})
    for o in paid_orders:
        day = o.get('date_created', '')[:10]
        daily[day]['revenue'] += o.get('total_amount', 0)
        daily[day]['orders'] += 1

    sorted_days = sorted(daily.keys())
    day_labels = [d[5:] for d in sorted_days]
    day_values = [daily[d]['revenue'] for d in sorted_days]

    revenue_chart = charts.line_chart(
        day_labels, [{'label': 'Faturamento', 'values': day_values, 'color': '#004D4D'}],
        title='Faturamento Diário', format_currency=True, width=10, height=4)

    # Top products
    product_revenue = defaultdict(lambda: {'revenue': 0, 'qty': 0})
    for o in paid_orders:
        for item in o.get('order_items', []):
            title = item.get('item', {}).get('title', 'Desconhecido')[:45]
            qty = item.get('quantity', 1)
            price = item.get('unit_price', 0)
            product_revenue[title]['revenue'] += price * qty
            product_revenue[title]['qty'] += qty

    top_products = sorted(product_revenue.items(), key=lambda x: x[1]['revenue'], reverse=True)[:10]
    top_labels = [p[0][:30] for p in top_products]
    top_values = [p[1]['revenue'] for p in top_products]
    products_chart = charts.bar_chart(top_labels, top_values, title='Top 10 Produtos por Receita',
                                      format_currency=True, horizontal=True, width=10, height=5)

    ticket_medio = safe_div(total_revenue, len(paid_orders))

    products_rows = ''
    for i, (name, data) in enumerate(top_products, 1):
        pct = safe_div(data['revenue'], total_revenue) * 100
        products_rows += f'''
        <tr>
            <td class="rank">#{i}</td>
            <td>{name}</td>
            <td class="number">{fmt_number(data["qty"])}</td>
            <td class="number">{fmt_currency(data["revenue"])}</td>
            <td class="number">{fmt_pct(pct)}</td>
        </tr>'''

    best_day = max(daily.items(), key=lambda x: x[1]['revenue']) if daily else ('N/D', {'revenue': 0})
    worst_day = min(daily.items(), key=lambda x: x[1]['revenue']) if daily else ('N/D', {'revenue': 0})

    return f'''
    <div class="page">
        <div class="section-header">
            <span class="section-number">02</span>
            <h2>💰 Faturamento & Receita</h2>
        </div>
        <div class="kpi-grid kpi-grid-4">
            <div class="kpi-card kpi-primary">
                <span class="kpi-value">{fmt_currency(total_revenue)}</span>
                <span class="kpi-label">Faturamento Total</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-value">{fmt_currency(ticket_medio)}</span>
                <span class="kpi-label">Ticket Médio</span>
            </div>
            <div class="kpi-card kpi-positive">
                <span class="kpi-value">{fmt_currency(best_day[1]["revenue"])}</span>
                <span class="kpi-label">🔥 Melhor Dia ({best_day[0][5:]})</span>
            </div>
            <div class="kpi-card kpi-warning">
                <span class="kpi-value">{fmt_currency(worst_day[1]["revenue"])}</span>
                <span class="kpi-label">📉 Pior Dia ({worst_day[0][5:]})</span>
            </div>
        </div>
        <div class="chart-container"><img src="data:image/png;base64,{revenue_chart}" class="chart-img"></div>
        <div class="chart-container"><img src="data:image/png;base64,{products_chart}" class="chart-img"></div>
        <table class="data-table">
            <thead><tr><th>#</th><th>Produto</th><th>Unidades</th><th>Receita</th><th>% Total</th></tr></thead>
            <tbody>{products_rows}</tbody>
        </table>
        <div class="insight-box">
            <span class="insight-icon">💡</span>
            <div class="insight-content">
                <strong>Insight:</strong> Produto #1 representa {fmt_pct(safe_div(top_products[0][1]["revenue"], total_revenue)*100 if top_products else 0)} do faturamento.
                Melhor dia foi {best_day[0][5:]} com {fmt_currency(best_day[1]["revenue"])}.
                Considere cross-sell nos produtos complementares para aumentar ticket médio.
            </div>
        </div>
    </div>'''

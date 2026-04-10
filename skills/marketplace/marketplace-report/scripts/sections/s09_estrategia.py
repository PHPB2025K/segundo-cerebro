"""Seção 09 — Insights Estratégicos & Plano de Ação"""

from collections import defaultdict
from .helpers import *

def needs_data():
    return ['orders', 'payments', 'seller_info']

def build(orders, payments, seller_info, **kwargs):
    paid_orders = [o for o in orders if o.get('status') == 'paid']
    total_revenue = sum(o.get('total_amount', 0) for o in paid_orders)
    total_orders = len(paid_orders)
    cancelled = len([o for o in orders if o.get('status') == 'cancelled'])
    cancel_rate = safe_div(cancelled, len(orders)) * 100
    ticket_medio = safe_div(total_revenue, total_orders)

    total_net = sum(p.get('transaction_details', {}).get('net_received_amount', 0)
                    for p in payments if p.get('status') == 'approved')
    fee_pct = safe_div(total_revenue - total_net, total_revenue) * 100

    rep = seller_info.get('seller_reputation', {}) if seller_info else {}
    level = rep.get('level_id', 'N/D')

    product_rev = defaultdict(float)
    for o in paid_orders:
        for item in o.get('order_items', []):
            title = item.get('item', {}).get('title', '?')[:40]
            product_rev[title] += item.get('unit_price', 0) * item.get('quantity', 1)
    top_product = max(product_rev.items(), key=lambda x: x[1]) if product_rev else ('N/D', 0)
    top_pct = safe_div(top_product[1], total_revenue) * 100

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">09</span><h2>🎯 Insights Estratégicos & Plano de Ação</h2></div>
        <div class="strategy-section">
            <div class="strategy-block strategy-wins">
                <h3>✅ Top 3 Vitórias</h3>
                <ul>
                    <li>Faturamento de {fmt_currency(total_revenue)} com {fmt_number(total_orders)} pedidos</li>
                    <li>Reputação {level} mantida — credibilidade com compradores</li>
                    <li>Produto líder ({top_product[0][:30]}) representa {fmt_pct(top_pct)} da receita</li>
                </ul>
            </div>
            <div class="strategy-block strategy-problems">
                <h3>❌ Top 3 Problemas</h3>
                <ul>
                    <li>Taxa de cancelamento de {fmt_pct(cancel_rate)} — {'aceitável' if cancel_rate < 5 else 'precisa reduzir'}</li>
                    <li>Taxas ML consomem {fmt_pct(fee_pct)} do bruto — buscar otimização</li>
                    <li>{'Concentração alta no produto líder — diversificar' if top_pct > 30 else 'Dados de tráfego indisponíveis — dificulta análise'}</li>
                </ul>
            </div>
            <div class="strategy-block strategy-opportunities">
                <h3>🔥 Top 3 Oportunidades</h3>
                <ul>
                    <li>Criar kits e combos para aumentar ticket médio (atual: {fmt_currency(ticket_medio)})</li>
                    <li>Exportar dados de Ads e tráfego para análise completa</li>
                    <li>Escalar produtos com boa conversão via Product Ads</li>
                </ul>
            </div>
        </div>
        <h3>📋 Plano de Ação</h3>
        <table class="data-table">
            <thead><tr><th>Ação</th><th>Impacto</th><th>Urgência</th><th>Prazo</th></tr></thead>
            <tbody>
                <tr><td>Revisar anúncios com poucas fotos/descrição</td><td><span class="badge badge-positive">Alto</span></td><td><span class="badge badge-warning">Média</span></td><td>1 semana</td></tr>
                <tr><td>Criar 2-3 kits com produtos complementares</td><td><span class="badge badge-positive">Alto</span></td><td><span class="badge badge-positive">Alta</span></td><td>2 semanas</td></tr>
                <tr><td>Exportar relatório de Ads para análise</td><td><span class="badge badge-positive">Alto</span></td><td><span class="badge badge-positive">Alta</span></td><td>Imediato</td></tr>
                <tr><td>Analisar motivos de cancelamento</td><td><span class="badge badge-warning">Médio</span></td><td><span class="badge badge-warning">Média</span></td><td>1 semana</td></tr>
                <tr><td>Monitorar estoque dos top 5 produtos</td><td><span class="badge badge-positive">Alto</span></td><td><span class="badge badge-positive">Alta</span></td><td>Contínuo</td></tr>
            </tbody>
        </table>
        <div class="insight-box insight-premium"><span class="insight-icon">🎯</span><div class="insight-content">
            <strong>Meta sugerida próximo período:</strong><br>
            Faturamento: {fmt_currency(total_revenue * 1.1)} (+10%) · Ticket Médio: {fmt_currency(ticket_medio * 1.05)} (+5%) · Cancelamentos: &lt;{max(1, cancel_rate - 1):.0f}%
        </div></div>
    </div>'''

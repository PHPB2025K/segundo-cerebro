"""Seção 01 — Capa & Resumo Executivo"""

from .helpers import *

def needs_data():
    """Retorna quais dados essa seção precisa."""
    return ['orders', 'payments', 'seller_info', 'items_total']

def build(orders, payments, seller_info, items_total, **kwargs):
    """Gera HTML da capa com KPIs e resumo executivo."""
    paid_orders = [o for o in orders if o.get('status') == 'paid']
    total_revenue = sum(o.get('total_amount', 0) for o in paid_orders)
    total_orders = len(paid_orders)
    ticket_medio = safe_div(total_revenue, total_orders)
    cancelled = len([o for o in orders if o.get('status') == 'cancelled'])
    cancel_rate = safe_div(cancelled, len(orders)) * 100

    rep = seller_info.get('seller_reputation', {}) if seller_info else {}
    level = rep.get('level_id', 'N/D')
    power = rep.get('power_seller_status', 'N/D')

    total_net = sum(p.get('transaction_details', {}).get('net_received_amount', 0)
                    for p in payments if p.get('status') == 'approved')
    total_fees = total_revenue - total_net if total_revenue > 0 else 0

    # Health
    health_score = 'excellent' if level == '5_green' else ('good' if '4' in str(level) or '5' in str(level) else 'warning')
    health_emoji = '🟢' if health_score == 'excellent' else ('🟡' if health_score == 'good' else '🔴')
    health_label = 'Excelente' if health_score == 'excellent' else ('Bom' if health_score == 'good' else 'Atenção')

    logo_b64 = logo_base64('budamix-logo-teal.png')

    return f'''
    <div class="page cover-page">
        <div class="cover-header">
            <img src="data:image/png;base64,{logo_b64}" class="cover-logo" alt="Budamix">
            <div class="cover-title">
                <h1>Relatório de Performance</h1>
                <h2>Mercado Livre</h2>
                <p class="cover-period">{{{{periodo_display}}}}</p>
            </div>
        </div>

        <div class="health-indicator health-{health_score}">
            <span class="health-emoji">{health_emoji}</span>
            <span class="health-label">Saúde da Conta: <strong>{health_label}</strong></span>
            <span class="health-detail">Nível {level} · {power}</span>
        </div>

        <div class="kpi-grid">
            <div class="kpi-card kpi-primary">
                <span class="kpi-icon">💰</span>
                <span class="kpi-value">{fmt_currency(total_revenue)}</span>
                <span class="kpi-label">Faturamento Bruto</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-icon">📦</span>
                <span class="kpi-value">{fmt_number(total_orders)}</span>
                <span class="kpi-label">Pedidos Pagos</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-icon">🎯</span>
                <span class="kpi-value">{fmt_currency(ticket_medio)}</span>
                <span class="kpi-label">Ticket Médio</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-icon">💎</span>
                <span class="kpi-value">{fmt_currency(total_net)}</span>
                <span class="kpi-label">Receita Líquida</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-icon">📊</span>
                <span class="kpi-value">{fmt_pct(100 - cancel_rate)}</span>
                <span class="kpi-label">Taxa de Aprovação</span>
            </div>
            <div class="kpi-card">
                <span class="kpi-icon">🏷️</span>
                <span class="kpi-value">{fmt_number(items_total)}</span>
                <span class="kpi-label">Anúncios Ativos</span>
            </div>
        </div>

        <div class="executive-summary">
            <h3>📋 Resumo Executivo</h3>
            <ul>
                <li><strong>Faturamento:</strong> {fmt_currency(total_revenue)} bruto, {fmt_currency(total_net)} líquido ({fmt_pct(safe_div(total_net, total_revenue) * 100)} de aproveitamento)</li>
                <li><strong>Volume:</strong> {fmt_number(total_orders)} pedidos pagos com ticket médio de {fmt_currency(ticket_medio)}</li>
                <li><strong>Taxas ML:</strong> {fmt_currency(total_fees)} ({fmt_pct(safe_div(total_fees, total_revenue) * 100)} do bruto)</li>
                <li><strong>Cancelamentos:</strong> {cancelled} pedidos ({fmt_pct(cancel_rate)})</li>
                <li><strong>Reputação:</strong> {level} — {power}</li>
            </ul>
        </div>
    </div>
    '''

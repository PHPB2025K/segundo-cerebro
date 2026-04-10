"""Seção 06 — Reputação & Saúde da Conta"""

from .helpers import *

def needs_data():
    return ['seller_info']

def build(seller_info, **kwargs):
    if not seller_info:
        return f'<div class="page"><div class="section-header"><span class="section-number">06</span><h2>🛡️ Reputação</h2></div>{NOT_AVAILABLE}</div>'

    rep = seller_info.get('seller_reputation', {})
    level = rep.get('level_id', 'N/D')
    power = rep.get('power_seller_status', 'N/D')
    transactions = rep.get('transactions', {})
    completed = transactions.get('completed', 0)
    canceled = transactions.get('canceled', 0)

    metrics = rep.get('metrics', {})
    claims_val = metrics.get('claims', {}).get('value', 0) if isinstance(metrics.get('claims'), dict) else 0
    delayed_val = metrics.get('delayed_handling_time', {}).get('value', 0) if isinstance(metrics.get('delayed_handling_time'), dict) else 0
    cancel_val = metrics.get('cancellations', {}).get('value', 0) if isinstance(metrics.get('cancellations'), dict) else 0

    level_map = {
        '5_green': ('MercadoLíder — Verde', '🟢', 'Excelente'),
        '4_light_green': ('Nível 4 — Verde Claro', '🟡', 'Bom'),
        '3_yellow': ('Nível 3 — Amarelo', '🟡', 'Atenção'),
        '2_orange': ('Nível 2 — Laranja', '🟠', 'Risco'),
        '1_red': ('Nível 1 — Vermelho', '🔴', 'Crítico'),
    }
    level_info = level_map.get(level, (level, '⚪', 'Desconhecido'))

    claims_s = status_badge(claims_val, (2, 4))
    delayed_s = status_badge(delayed_val, (5, 12))
    cancel_s = status_badge(cancel_val, (1, 3))

    return f'''
    <div class="page">
        <div class="section-header"><span class="section-number">06</span><h2>🛡️ Reputação & Saúde da Conta</h2></div>
        <div class="reputation-card">
            <div class="rep-level">
                <span class="rep-emoji">{level_info[1]}</span>
                <div><h3>{level_info[0]}</h3><p>Power Seller: <strong>{power}</strong></p></div>
            </div>
            <div class="rep-stats">
                <span>{fmt_number(completed)} vendas completadas</span>
                <span>{fmt_number(canceled)} canceladas</span>
            </div>
        </div>
        <div class="metrics-grid">
            <div class="metric-card metric-{claims_s[2]}">
                <div class="metric-header"><span>{claims_s[0]}</span><span class="metric-title">Reclamações</span></div>
                <span class="metric-value">{claims_val}%</span>
                <span class="metric-status">{claims_s[1]} (benchmark: &lt;2%)</span>
            </div>
            <div class="metric-card metric-{delayed_s[2]}">
                <div class="metric-header"><span>{delayed_s[0]}</span><span class="metric-title">Atrasos no Envio</span></div>
                <span class="metric-value">{delayed_val}%</span>
                <span class="metric-status">{delayed_s[1]} (benchmark: &lt;5%)</span>
            </div>
            <div class="metric-card metric-{cancel_s[2]}">
                <div class="metric-header"><span>{cancel_s[0]}</span><span class="metric-title">Cancelamentos</span></div>
                <span class="metric-value">{cancel_val}%</span>
                <span class="metric-status">{cancel_s[1]} (benchmark: &lt;1%)</span>
            </div>
        </div>
        <div class="insight-box"><span class="insight-icon">💡</span><div class="insight-content">
            <strong>Insight:</strong> Reputação {level_info[2].lower()}.
            {'Manter o padrão atual.' if level_info[2] == 'Excelente' else 'Foco em reduzir ' + ('reclamações' if claims_val > 2 else 'atrasos' if delayed_val > 5 else 'cancelamentos') + '.'}
            Atrasos ({delayed_val}%) {'dentro do aceitável.' if delayed_val <= 5 else 'precisam de atenção imediata.'}
        </div></div>
    </div>'''

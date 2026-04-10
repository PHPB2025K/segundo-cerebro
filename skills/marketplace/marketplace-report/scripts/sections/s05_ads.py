"""Seção 05 — Publicidade / Ads (multi-plataforma — dados via connector)"""

import logging
from .helpers import *

log = logging.getLogger('s05_ads')

PLATFORM_NAMES = {
    'mercadolivre': 'Mercado Livre',
    'amazon': 'Amazon',
    'shopee': 'Shopee',
}


def needs_data():
    return ['ads']


def build(**kwargs):
    ads = kwargs.get('ads', [])
    platform = kwargs.get('platform', '')
    platform_display = kwargs.get('platform_display', platform)

    if not ads:
        return _build_unavailable(f"Dados de Ads indisponíveis para {platform_display}")

    is_multi = platform == 'all'

    # Aggregate totals
    total_cost = sum(c.get('cost', 0) for c in ads)
    total_revenue = sum(c.get('revenue', 0) for c in ads)
    total_clicks = sum(c.get('clicks', 0) for c in ads)
    total_impressions = sum(c.get('impressions', 0) for c in ads)

    roas_geral = total_revenue / total_cost if total_cost > 0 else 0
    acos_geral = (total_cost / total_revenue * 100) if total_revenue > 0 else 0
    cpc_medio = total_cost / total_clicks if total_clicks > 0 else 0
    ctr_medio = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0

    active = [c for c in ads if c.get('status') == 'active']
    paused = [c for c in ads if c.get('status') != 'active']

    # ROAS health indicator
    if roas_geral >= 5:
        roas_status = ('🟢', 'Saudável', 'positive')
    elif roas_geral >= 3:
        roas_status = ('🟡', 'No limite', 'warning')
    else:
        roas_status = ('🔴', 'Negativo', 'negative')

    # KPI grid
    kpi_html = f'''
        <div class="kpi-grid">
            <div class="kpi-row">
                <div class="kpi-card kpi-primary"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">💰</span></div><div class="kpi-content"><span class="kpi-value">{fmt_currency(total_cost)}</span><span class="kpi-label">Investimento Total</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">💎</span></div><div class="kpi-content"><span class="kpi-value">{fmt_currency(total_revenue)}</span><span class="kpi-label">Receita Ads Total</span></div></div></div>
                <div class="kpi-card kpi-{roas_status[2]}"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">📈</span></div><div class="kpi-content"><span class="kpi-value">{roas_geral:.1f}x</span><span class="kpi-label">ROAS Geral {roas_status[0]}</span></div></div></div>
            </div>
            <div class="kpi-row">
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">📊</span></div><div class="kpi-content"><span class="kpi-value">{acos_geral:.1f}%</span><span class="kpi-label">ACOS Geral</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">🖱️</span></div><div class="kpi-content"><span class="kpi-value">{fmt_currency(cpc_medio)}</span><span class="kpi-label">CPC Médio</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">👁️</span></div><div class="kpi-content"><span class="kpi-value">{ctr_medio:.2f}%</span><span class="kpi-label">CTR Médio</span></div></div></div>
            </div>
        </div>'''

    # Per-platform mini-KPIs (when multi)
    platform_breakdown_html = ''
    if is_multi:
        platforms_data = {}
        for c in ads:
            p = c.get('platform', 'unknown')
            if p not in platforms_data:
                platforms_data[p] = {'cost': 0, 'revenue': 0, 'clicks': 0, 'impressions': 0, 'count': 0}
            d = platforms_data[p]
            d['cost'] += c.get('cost', 0)
            d['revenue'] += c.get('revenue', 0)
            d['clicks'] += c.get('clicks', 0)
            d['impressions'] += c.get('impressions', 0)
            d['count'] += 1

        if len(platforms_data) > 1:
            platform_breakdown_html = '<h3>📊 Breakdown por Plataforma</h3><table class="data-table"><thead><tr><th>Plataforma</th><th>Investimento</th><th>Receita</th><th>ROAS</th><th>ACOS</th><th>CPC</th><th>Campanhas</th></tr></thead><tbody>'
            for p, d in sorted(platforms_data.items(), key=lambda x: x[1]['cost'], reverse=True):
                pname = PLATFORM_NAMES.get(p, p.title())
                p_roas = d['revenue'] / d['cost'] if d['cost'] > 0 else 0
                p_acos = (d['cost'] / d['revenue'] * 100) if d['revenue'] > 0 else 0
                p_cpc = d['cost'] / d['clicks'] if d['clicks'] > 0 else 0
                roas_class = 'badge-positive' if p_roas >= 5 else ('badge-warning' if p_roas >= 3 else 'badge-negative')
                platform_breakdown_html += f'''<tr>
                    <td>{pname}</td>
                    <td class="number">{fmt_currency(d['cost'])}</td>
                    <td class="number">{fmt_currency(d['revenue'])}</td>
                    <td class="number"><span class="badge {roas_class}">{p_roas:.1f}x</span></td>
                    <td class="number">{p_acos:.1f}%</td>
                    <td class="number">{fmt_currency(p_cpc)}</td>
                    <td class="number">{d['count']}</td>
                </tr>'''
            platform_breakdown_html += '</tbody></table>'

    # Top 5 by ROAS
    active_with_revenue = [c for c in active if c.get('revenue', 0) > 0]
    top_roas = sorted(active_with_revenue, key=lambda c: c.get('roas', 0), reverse=True)[:5]

    plat_col = '<th>Plataforma</th>' if is_multi else ''
    top_rows = ''
    for c in top_roas:
        name = (c.get('campaign_name', '') or '?')[:30]
        plat_td = f'<td>{PLATFORM_NAMES.get(c.get("platform", ""), c.get("platform", ""))}</td>' if is_multi else ''
        top_rows += f'''<tr>
            <td>{name}</td>
            <td class="number">{fmt_currency(c.get("cost", 0))}</td>
            <td class="number">{fmt_currency(c.get("revenue", 0))}</td>
            <td class="number"><span class="badge badge-positive">{c.get("roas", 0):.1f}x</span></td>
            <td class="number">{c.get("acos", 0):.1f}%</td>
            {plat_td}
        </tr>'''

    top_table = f'''
        <h3>🏆 Top 5 Campanhas por ROAS</h3>
        <table class="data-table">
            <thead><tr><th>Campanha</th><th>Investimento</th><th>Receita</th><th>ROAS</th><th>ACOS</th>{plat_col}</tr></thead>
            <tbody>{top_rows if top_rows else '<tr><td colspan="5">Nenhuma campanha ativa com receita</td></tr>'}</tbody>
        </table>'''

    # Campaigns needing attention (ROAS < 3)
    needs_attention = [c for c in active if c.get('cost', 0) > 0 and c.get('roas', 0) < 3]
    needs_attention = sorted(needs_attention, key=lambda c: c.get('roas', 999))[:5]

    worst_rows = ''
    for c in needs_attention:
        name = (c.get('campaign_name', '') or '?')[:30]
        roas_val = c.get('roas', 0)
        badge_class = 'badge-negative' if roas_val < 2 else 'badge-warning'
        plat_td = f'<td>{PLATFORM_NAMES.get(c.get("platform", ""), c.get("platform", ""))}</td>' if is_multi else ''
        worst_rows += f'''<tr>
            <td>{name}</td>
            <td class="number">{fmt_currency(c.get("cost", 0))}</td>
            <td class="number">{fmt_currency(c.get("revenue", 0))}</td>
            <td class="number"><span class="badge {badge_class}">{roas_val:.1f}x</span></td>
            {plat_td}
        </tr>'''

    plat_col_attn = '<th>Plataforma</th>' if is_multi else ''
    attention_table = ''
    if worst_rows:
        attention_table = f'''
        <h3>⚠️ Campanhas que precisam de atenção (ROAS < 3x)</h3>
        <table class="data-table">
            <thead><tr><th>Campanha</th><th>Investimento</th><th>Receita</th><th>ROAS</th>{plat_col_attn}</tr></thead>
            <tbody>{worst_rows}</tbody>
        </table>'''

    # Insight box
    insight = _build_insight(ads, roas_geral, acos_geral, cpc_medio, roas_status, is_multi)

    title_suffix = f' / {platform_display}' if not is_multi else ' / Multi-Plataforma'

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">05</span><h2>📣 Publicidade{title_suffix}</h2></div>
        {kpi_html}
        {platform_breakdown_html}
        {top_table}
        {attention_table}
        {insight}
        <p style="font-size:8pt; color:#8A9A9A; margin-top:15px;">
            <em>Para análise detalhada por keyword, segmentação e otimizações granulares, solicitar Relatório de Ads dedicado.</em>
        </p>
    </div>'''


def _build_insight(ads, roas_geral, acos_geral, cpc_medio, roas_status, is_multi):
    """Gera insight box com análise cross-plataforma."""
    parts = []

    # ROAS assessment
    parts.append(f"ROAS geral de {roas_geral:.1f}x — {roas_status[1].lower()}.")
    if roas_geral >= 5:
        parts.append("Excelente retorno. Considere aumentar budget das top campanhas.")
    elif roas_geral >= 3:
        parts.append("Retorno aceitável. Foco em otimizar campanhas com ROAS < 3x.")
    else:
        parts.append("ROAS abaixo do ideal. Revisar estratégias e pausar campanhas ineficientes.")

    # Cross-platform insight
    if is_multi:
        platforms_roas = {}
        for c in ads:
            p = c.get('platform', 'unknown')
            if p not in platforms_roas:
                platforms_roas[p] = {'cost': 0, 'revenue': 0}
            platforms_roas[p]['cost'] += c.get('cost', 0)
            platforms_roas[p]['revenue'] += c.get('revenue', 0)

        best_p = None
        best_roas = 0
        for p, d in platforms_roas.items():
            r = d['revenue'] / d['cost'] if d['cost'] > 0 else 0
            if r > best_roas:
                best_roas = r
                best_p = p
        if best_p and len(platforms_roas) > 1:
            pname = PLATFORM_NAMES.get(best_p, best_p.title())
            parts.append(f"{pname} tem o melhor ROAS ({best_roas:.1f}x) — considere concentrar budget nessa plataforma.")

    parts.append(f"ACOS de {acos_geral:.1f}% com CPC médio de {fmt_currency(cpc_medio)}.")

    content = ' '.join(parts)
    return f'''
        <div class="insight-box">
            <span class="insight-icon">💡</span>
            <div class="insight-content">
                <strong>Insight:</strong> {content}
            </div>
        </div>'''


def _build_unavailable(reason):
    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">05</span><h2>📣 Publicidade / Ads</h2></div>
        <div class="na-section">
            <div class="na-icon">📣</div>
            <h3>{reason}</h3>
            <p>Dados de publicidade não foram retornados pelos connectors neste período.</p>
        </div>
    </div>'''

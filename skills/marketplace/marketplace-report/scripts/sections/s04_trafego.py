"""Seção 04 — Tráfego & Visibilidade (multi-plataforma)"""

from .helpers import *

PLATFORM_NAMES = {
    'mercadolivre': 'Mercado Livre',
    'amazon': 'Amazon',
    'shopee': 'Shopee',
}


def needs_data():
    return ['traffic']


def build(**kwargs):
    traffic = kwargs.get('traffic', [])
    platform = kwargs.get('platform', '')
    platform_display = kwargs.get('platform_display', platform)

    if not traffic:
        return _build_unavailable(platform_display)

    # Aggregate KPIs
    total_sessions = sum(t.get('sessions', 0) for t in traffic)
    total_page_views = sum(t.get('page_views', 0) for t in traffic)
    items_with_conv = [t for t in traffic if t.get('conversion_rate', 0) > 0]
    avg_conversion = (sum(t['conversion_rate'] for t in items_with_conv) / len(items_with_conv)) if items_with_conv else 0

    # Top 10 by sessions
    sorted_traffic = sorted(traffic, key=lambda t: t.get('sessions', 0), reverse=True)
    top_10 = sorted_traffic[:10]

    is_multi = platform == 'all'

    # Per-platform breakdown
    platforms_in_data = {}
    for t in traffic:
        p = t.get('platform', 'unknown')
        if p not in platforms_in_data:
            platforms_in_data[p] = {'sessions': 0, 'page_views': 0, 'conversions': [], 'count': 0}
        platforms_in_data[p]['sessions'] += t.get('sessions', 0)
        platforms_in_data[p]['page_views'] += t.get('page_views', 0)
        if t.get('conversion_rate', 0) > 0:
            platforms_in_data[p]['conversions'].append(t['conversion_rate'])
        platforms_in_data[p]['count'] += 1

    # Build KPI cards
    kpi_html = f'''
        <div class="kpi-grid">
            <div class="kpi-row">
                <div class="kpi-card kpi-primary"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">👁️</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(total_sessions)}</span><span class="kpi-label">Total de Sessões</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">📄</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(total_page_views)}</span><span class="kpi-label">Total de Page Views</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">🎯</span></div><div class="kpi-content"><span class="kpi-value">{fmt_pct(avg_conversion)}</span><span class="kpi-label">Taxa de Conversão Média</span></div></div></div>
            </div>
        </div>'''

    # Platform breakdown (when multi)
    breakdown_html = ''
    if is_multi and len(platforms_in_data) > 1:
        breakdown_html = '<h3>📊 Breakdown por Plataforma</h3><table class="data-table"><thead><tr><th>Plataforma</th><th>Sessões</th><th>Page Views</th><th>Conversão Média</th><th>Produtos</th></tr></thead><tbody>'
        for p, d in sorted(platforms_in_data.items(), key=lambda x: x[1]['sessions'], reverse=True):
            pname = PLATFORM_NAMES.get(p, p.title())
            avg_c = (sum(d['conversions']) / len(d['conversions'])) if d['conversions'] else 0
            breakdown_html += f'''<tr>
                <td>{pname}</td>
                <td class="number">{fmt_number(d['sessions'])}</td>
                <td class="number">{fmt_number(d['page_views'])}</td>
                <td class="number">{fmt_pct(avg_c)}</td>
                <td class="number">{d['count']}</td>
            </tr>'''
        breakdown_html += '</tbody></table>'

    # Missing platform notes
    missing_html = ''
    if is_multi:
        expected = {'mercadolivre', 'amazon', 'shopee'}
        missing = expected - set(platforms_in_data.keys())
        for m in missing:
            mname = PLATFORM_NAMES.get(m, m.title())
            missing_html += f'<p style="font-size:9pt; color:#8A9A9A;"><em>Dados de tráfego indisponíveis para {mname}</em></p>'

    # Top 10 table
    plat_col = '<th>Plataforma</th>' if is_multi else ''
    top_rows = ''
    for t in top_10:
        title = (t.get('title', '') or t.get('item_id', ''))[:40]
        sessions = t.get('sessions', 0)
        pv = t.get('page_views', 0)
        conv = t.get('conversion_rate', 0)

        conv_class = 'badge-positive' if conv >= 5 else ('badge-warning' if conv >= 2 else 'badge-negative')
        plat_td = f'<td>{PLATFORM_NAMES.get(t.get("platform", ""), t.get("platform", ""))}</td>' if is_multi else ''

        top_rows += f'''<tr>
            <td>{title}</td>
            <td class="number">{fmt_number(sessions)}</td>
            <td class="number">{fmt_number(pv)}</td>
            <td class="number"><span class="badge {conv_class}">{fmt_pct(conv)}</span></td>
            {plat_td}
        </tr>'''

    table_html = f'''
        <h3>🏆 Top 10 Produtos por Sessões</h3>
        <table class="data-table">
            <thead><tr><th>Produto</th><th>Sessões</th><th>Page Views</th><th>Conversão</th>{plat_col}</tr></thead>
            <tbody>{top_rows}</tbody>
        </table>'''

    # Insight box
    insight = _build_insight(traffic, platforms_in_data, is_multi)

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">04</span><h2>👁️ Tráfego & Visibilidade</h2></div>
        {kpi_html}
        {breakdown_html}
        {missing_html}
        {table_html}
        {insight}
    </div>'''


def _build_insight(traffic, platforms_in_data, is_multi):
    """Gera insight box com análise automática."""
    insights = []

    # Best conversion platform
    if is_multi and len(platforms_in_data) > 1:
        best_conv = None
        best_conv_val = 0
        for p, d in platforms_in_data.items():
            avg_c = (sum(d['conversions']) / len(d['conversions'])) if d['conversions'] else 0
            if avg_c > best_conv_val:
                best_conv_val = avg_c
                best_conv = p
        if best_conv:
            pname = PLATFORM_NAMES.get(best_conv, best_conv.title())
            insights.append(f"{pname} tem a melhor taxa de conversão média ({fmt_pct(best_conv_val)}).")

    # High traffic, low conversion opportunities
    high_traffic_low_conv = [
        t for t in traffic
        if t.get('sessions', 0) > 50 and t.get('conversion_rate', 0) < 2
    ]
    if high_traffic_low_conv:
        count = len(high_traffic_low_conv)
        insights.append(f"{count} produto(s) com tráfego alto e conversão baixa (<2%) — oportunidade de otimização de listing.")

    # High conversion products
    high_conv = [t for t in traffic if t.get('conversion_rate', 0) >= 10]
    if high_conv:
        insights.append(f"{len(high_conv)} produto(s) com conversão acima de 10% — considerar investir em ads para ampliar tráfego.")

    if not insights:
        insights.append("Analise os dados de tráfego para identificar oportunidades de otimização.")

    content = ' '.join(insights)
    return f'''
        <div class="insight-box">
            <span class="insight-icon">💡</span>
            <div class="insight-content">
                <strong>Insight:</strong> {content}
            </div>
        </div>'''


def _build_unavailable(platform_display):
    """Fallback quando não há dados de tráfego."""
    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">04</span><h2>👁️ Tráfego & Visibilidade</h2></div>
        <div class="na-section" style="padding:30px 30px;">
            <div class="na-icon">📊</div>
            <h3>Dados de tráfego indisponíveis para {platform_display}</h3>
            <p>Os dados de tráfego não foram retornados pela API da plataforma neste período.</p>
            <div class="na-actions">
                <h4>Alternativas:</h4>
                <ul>
                    <li>Verificar se as credenciais de API permitem acesso a dados de tráfego</li>
                    <li>Acessar <strong>Painel do Vendedor → Métricas</strong> para exportar manualmente</li>
                    <li>Dados podem não estar disponíveis para o período selecionado</li>
                </ul>
            </div>
        </div>
    </div>'''

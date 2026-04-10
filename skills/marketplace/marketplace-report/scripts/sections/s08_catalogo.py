"""Seção 08 — Anúncios & Catálogo"""

from .helpers import *
from .icons import icon

def needs_data():
    return ['items', 'items_total']

def build(items, items_total, **kwargs):
    with_good_photos = 0
    prices = []
    items_rows = ''

    for i, item in enumerate(items[:20], 1):
        title = item.get('title', '?')[:45]
        price = item.get('price', 0)
        sold = item.get('sold_quantity', 0)
        avail = item.get('available_quantity', 0)
        pics = len(item.get('pictures', []))
        if pics >= 3: with_good_photos += 1
        prices.append(price)
        stock_badge = '🟢' if avail > 10 else ('🟡' if avail > 0 else '🔴')
        items_rows += f'<tr><td>{title}</td><td class="number">{fmt_currency(price)}</td><td class="number">{fmt_number(sold)}</td><td class="number">{stock_badge} {avail}</td><td class="number">{pics} fotos</td></tr>'

    photo_pct = safe_div(with_good_photos, len(items)) * 100
    avg_price = safe_div(sum(prices), len(prices))

    return f'''
    <div class="page section-break">
        <div class="section-header"><span class="section-number">08</span><h2>📋 Anúncios & Catálogo</h2></div>
        <div class="kpi-grid">
            <div class="kpi-row">
                <div class="kpi-card kpi-primary"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('anuncios')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_number(items_total)}</span><span class="kpi-label">Anúncios Ativos</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('preco')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_currency(avg_price)}</span><span class="kpi-label">Preço Médio</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('foto')}</span></div><div class="kpi-content"><span class="kpi-value">{fmt_pct(photo_pct)}</span><span class="kpi-label">Com 3+ Fotos</span></div></div></div>
                <div class="kpi-card"><div class="kpi-inner"><div class="kpi-icon-wrap"><span class="kpi-icon-badge">{icon('busca')}</span></div><div class="kpi-content"><span class="kpi-value">{len(items)}</span><span class="kpi-label">Analisados</span></div></div></div>
            </div>
        </div>
        <h3>Catálogo Ativo (amostra)</h3>
        <table class="data-table">
            <thead><tr><th>Produto</th><th>Preço</th><th>Vendidos</th><th>Estoque</th><th>Fotos</th></tr></thead>
            <tbody>{items_rows}</tbody>
        </table>
        <div class="insight-box"><span class="insight-icon">💡</span><div class="insight-content">
            <strong>Insight:</strong> {fmt_pct(photo_pct)} dos anúncios têm 3+ fotos. Priorizar os que têm poucas imagens.
            Verificar estoque dos itens em amarelo/vermelho para evitar ruptura.
        </div></div>
    </div>'''

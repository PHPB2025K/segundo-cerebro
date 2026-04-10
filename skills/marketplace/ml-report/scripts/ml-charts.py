#!/usr/bin/env python3
"""
Gerador de Gráficos — Relatório ML Budamix
Todas as funções retornam imagens PNG como string base64.
"""

import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ─── Paleta Budamix ──────────────────────────────────────────────────────────

COLORS = {
    'teal': '#004D4D',
    'grafite': '#132525',
    'dourado': '#C7A35A',
    'terracota': '#C56A4A',
    'sage': '#7EADAD',
    'porcelana': '#D9E6E6',
    'areia': '#F7F4EF',
    'branco': '#FFFFFF',
    'verde': '#18794E',
}

CHART_PALETTE = ['#004D4D', '#C7A35A', '#7EADAD', '#C56A4A', '#18794E', '#132525', '#D9E6E6']


def _setup_style():
    """Aplica estilo base Budamix nos gráficos."""
    plt.rcParams.update({
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'axes.edgecolor': '#D9E6E6',
        'axes.labelcolor': '#132525',
        'xtick.color': '#132525',
        'ytick.color': '#132525',
        'text.color': '#132525',
        'font.family': 'sans-serif',
        'font.size': 10,
        'axes.grid': True,
        'grid.alpha': 0.2,
        'grid.color': '#7EADAD',
    })


def _fig_to_base64(fig, dpi=150):
    """Converte figure matplotlib em base64 PNG."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight', transparent=True)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


def bar_chart(labels, values, title='', color=None, width=8, height=4, format_currency=False, horizontal=False):
    """Gráfico de barras vertical ou horizontal."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))
    bar_color = color or COLORS['teal']

    if horizontal:
        bars = ax.barh(labels, values, color=bar_color, height=0.6, edgecolor='none')
        ax.invert_yaxis()
        for bar, val in zip(bars, values):
            label = f'R$ {val:,.0f}' if format_currency else f'{val:,.0f}'
            ax.text(bar.get_width() + max(values)*0.02, bar.get_y() + bar.get_height()/2,
                    label, va='center', fontsize=9, color=COLORS['grafite'])
        ax.set_xlim(0, max(values) * 1.25)
    else:
        bars = ax.bar(labels, values, color=bar_color, width=0.6, edgecolor='none')
        for bar, val in zip(bars, values):
            label = f'R$ {val:,.0f}' if format_currency else f'{val:,.0f}'
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                    label, ha='center', fontsize=9, color=COLORS['grafite'])
        ax.set_ylim(0, max(values) * 1.2)

    if title:
        ax.set_title(title, fontsize=13, fontweight='bold', color=COLORS['teal'], pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if format_currency and not horizontal:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    fig.tight_layout()
    return _fig_to_base64(fig)


def line_chart(labels, datasets, title='', width=8, height=4, format_currency=False):
    """
    Gráfico de linha com uma ou mais séries.
    datasets: list of dicts {'label': str, 'values': list, 'color': str (optional)}
    """
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))

    for i, ds in enumerate(datasets):
        color = ds.get('color', CHART_PALETTE[i % len(CHART_PALETTE)])
        ax.plot(labels, ds['values'], color=color, linewidth=2.5, marker='o',
                markersize=5, label=ds.get('label', ''))
        # Fill area under
        ax.fill_between(labels, ds['values'], alpha=0.08, color=color)

    if title:
        ax.set_title(title, fontsize=13, fontweight='bold', color=COLORS['teal'], pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if format_currency:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    if len(datasets) > 1:
        ax.legend(frameon=False, fontsize=9)

    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    return _fig_to_base64(fig)


def donut_chart(labels, values, title='', width=5, height=5, colors=None):
    """Gráfico de rosca (donut)."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))
    chart_colors = colors or CHART_PALETTE[:len(labels)]

    wedges, texts, autotexts = ax.pie(
        values, labels=None, autopct='%1.1f%%', startangle=90,
        colors=chart_colors, pctdistance=0.78,
        wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2)
    )

    for t in autotexts:
        t.set_fontsize(10)
        t.set_fontweight('bold')
        t.set_color('white')

    # Legend outside
    ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5),
              frameon=False, fontsize=9)

    if title:
        ax.set_title(title, fontsize=13, fontweight='bold', color=COLORS['teal'], pad=15)

    fig.tight_layout()
    return _fig_to_base64(fig)


def comparison_chart(labels, values_a, values_b, label_a='Período A', label_b='Período B',
                     title='', width=8, height=4, format_currency=False):
    """Gráfico de barras comparativo lado a lado."""
    _setup_style()
    import numpy as np
    fig, ax = plt.subplots(figsize=(width, height))

    x = np.arange(len(labels))
    bar_width = 0.35

    bars_a = ax.bar(x - bar_width/2, values_a, bar_width, label=label_a,
                    color=COLORS['teal'], edgecolor='none')
    bars_b = ax.bar(x + bar_width/2, values_b, bar_width, label=label_b,
                    color=COLORS['dourado'], edgecolor='none')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')

    if title:
        ax.set_title(title, fontsize=13, fontweight='bold', color=COLORS['teal'], pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(frameon=False, fontsize=9)

    if format_currency:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    fig.tight_layout()
    return _fig_to_base64(fig)


def kpi_gauge(value, max_value=5, title='', width=3, height=2):
    """Mini gauge/indicador visual para KPIs como reputação."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))

    # Background bar
    ax.barh([0], [max_value], height=0.5, color=COLORS['porcelana'], edgecolor='none')
    # Value bar
    pct = value / max_value
    color = COLORS['verde'] if pct >= 0.8 else (COLORS['dourado'] if pct >= 0.5 else COLORS['terracota'])
    ax.barh([0], [value], height=0.5, color=color, edgecolor='none')

    ax.text(value + 0.1, 0, f'{value}/{max_value}', va='center', fontsize=12,
            fontweight='bold', color=COLORS['grafite'])

    ax.set_xlim(0, max_value * 1.3)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(bottom=False, labelbottom=False)

    if title:
        ax.set_title(title, fontsize=10, fontweight='bold', color=COLORS['teal'])

    fig.tight_layout()
    return _fig_to_base64(fig)

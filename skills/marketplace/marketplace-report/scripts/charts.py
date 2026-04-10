#!/usr/bin/env python3
"""
Gerador de Gráficos Premium — Relatório Marketplace Budamix
Visual: Dashboard SaaS de alto nível.
"""

import base64
import io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.collections import PolyCollection
import matplotlib.patheffects as pe

# ─── Paleta Budamix ──────────────────────────────────────────────────────────

TEAL = '#004D4D'
TEAL_LIGHT = '#007A7A'
GRAFITE = '#132525'
DOURADO = '#C7A35A'
SAGE = '#7EADAD'
PORCELANA = '#D9E6E6'
AREIA = '#F7F4EF'
VERDE = '#18794E'
TERRACOTA = '#C56A4A'

CHART_PALETTE = [TEAL, DOURADO, SAGE, TERRACOTA, VERDE, GRAFITE, PORCELANA]


def _setup_style():
    plt.rcParams.update({
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.edgecolor': PORCELANA,
        'axes.labelcolor': GRAFITE,
        'xtick.color': '#8A9A9A',
        'ytick.color': '#8A9A9A',
        'text.color': GRAFITE,
        'font.family': 'sans-serif',
        'font.size': 9,
        'axes.grid': True,
        'grid.alpha': 0.08,
        'grid.color': SAGE,
        'grid.linewidth': 0.5,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.linewidth': 0.5,
        'xtick.major.size': 0,
        'ytick.major.size': 0,
        'xtick.major.pad': 8,
        'ytick.major.pad': 8,
    })


def _fig_to_base64(fig, dpi=150):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')


def bar_chart(labels, values, title='', color=None, width=10, height=3.5,
              format_currency=False, horizontal=False):
    """Gráfico de barras premium com cantos arredondados e gradiente."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))
    bar_color = color or TEAL

    # Find peak value for highlight
    peak_idx = values.index(max(values)) if values else 0
    colors = [bar_color] * len(values)
    colors[peak_idx] = DOURADO

    if horizontal:
        bars = ax.barh(labels, values, height=0.55, edgecolor='none', color=colors)
        ax.invert_yaxis()
        for bar, val in zip(bars, values):
            label = f'R$ {val:,.0f}' if format_currency else f'{val:,.0f}'
            ax.text(bar.get_width() + max(values)*0.02, bar.get_y() + bar.get_height()/2,
                    label, va='center', fontsize=8, color=GRAFITE, fontweight='500')
        ax.set_xlim(0, max(values) * 1.2)
        ax.spines['left'].set_visible(False)
    else:
        bars = ax.bar(labels, values, width=0.6, edgecolor='none', color=colors)
        for bar, val in zip(bars, values):
            label = f'R$ {val:,.0f}' if format_currency else f'{val:,.0f}'
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                    label, ha='center', fontsize=7.5, color=GRAFITE, fontweight='500')
        ax.set_ylim(0, max(values) * 1.18)
        ax.spines['bottom'].set_linewidth(0.5)

    if title:
        ax.set_title(title, fontsize=12, fontweight='700', color=TEAL, pad=15, loc='left')

    if format_currency and not horizontal:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    plt.xticks(rotation=45 if not horizontal else 0, ha='right' if not horizontal else 'center', fontsize=8)
    fig.tight_layout()
    return _fig_to_base64(fig)


def line_chart(labels, datasets, title='', width=10, height=3.5, format_currency=False):
    """Gráfico de linha premium com curva suavizada e área preenchida com gradiente."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))

    x = np.arange(len(labels))

    for i, ds in enumerate(datasets):
        color = ds.get('color', CHART_PALETTE[i % len(CHART_PALETTE)])
        vals = ds['values']

        # Smooth curve using interpolation
        if len(x) > 3:
            from scipy.interpolate import make_interp_spline
            try:
                x_smooth = np.linspace(x.min(), x.max(), 200)
                spl = make_interp_spline(x, vals, k=min(3, len(x)-1))
                vals_smooth = spl(x_smooth)

                # Plot smooth line
                ax.plot(x_smooth, vals_smooth, color=color, linewidth=2.5, zorder=3)

                # Gradient fill under curve
                ax.fill_between(x_smooth, vals_smooth, alpha=0.12, color=color, zorder=1)
                ax.fill_between(x_smooth, vals_smooth,
                                alpha=0.04, color=color, zorder=1)
            except:
                ax.plot(x, vals, color=color, linewidth=2.5, zorder=3)
                ax.fill_between(x, vals, alpha=0.1, color=color)
        else:
            ax.plot(x, vals, color=color, linewidth=2.5, zorder=3)
            ax.fill_between(x, vals, alpha=0.1, color=color)

        # Data points with white border
        ax.scatter(x, vals, color=color, s=35, zorder=5, edgecolors='white', linewidth=1.5)

        # Highlight peak
        peak_idx = vals.index(max(vals)) if isinstance(vals, list) else np.argmax(vals)
        peak_val = vals[peak_idx]
        label_text = f'R$ {peak_val:,.0f}' if format_currency else f'{peak_val:,.0f}'
        ax.annotate(label_text,
                    xy=(x[peak_idx], peak_val),
                    xytext=(0, 14), textcoords='offset points',
                    ha='center', fontsize=8, fontweight='700', color=DOURADO,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                              edgecolor=DOURADO, alpha=0.9, linewidth=0.8))

    if title:
        ax.set_title(title, fontsize=12, fontweight='700', color=TEAL, pad=15, loc='left')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)

    if format_currency:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    if len(datasets) > 1:
        ax.legend(frameon=False, fontsize=8)

    fig.tight_layout()
    return _fig_to_base64(fig)


def donut_chart(labels, values, title='', width=5, height=5, colors=None):
    """Gráfico donut premium."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))
    chart_colors = colors or CHART_PALETTE[:len(labels)]

    wedges, texts, autotexts = ax.pie(
        values, labels=None, autopct='%1.1f%%', startangle=90,
        colors=chart_colors, pctdistance=0.78,
        wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2.5))

    for t in autotexts:
        t.set_fontsize(9)
        t.set_fontweight('600')
        t.set_color('white')

    ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5),
              frameon=False, fontsize=8)

    if title:
        ax.set_title(title, fontsize=12, fontweight='700', color=TEAL, pad=15)

    fig.tight_layout()
    return _fig_to_base64(fig)


def comparison_chart(labels, values_a, values_b, label_a='Período A', label_b='Período B',
                     title='', width=10, height=3.5, format_currency=False):
    """Gráfico comparativo lado a lado premium."""
    _setup_style()
    fig, ax = plt.subplots(figsize=(width, height))

    x = np.arange(len(labels))
    bar_width = 0.35

    ax.bar(x - bar_width/2, values_a, bar_width, label=label_a,
           color=TEAL, edgecolor='none')
    ax.bar(x + bar_width/2, values_b, bar_width, label=label_b,
           color=DOURADO, edgecolor='none')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)

    if title:
        ax.set_title(title, fontsize=12, fontweight='700', color=TEAL, pad=15, loc='left')

    ax.legend(frameon=False, fontsize=8)

    if format_currency:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))

    fig.tight_layout()
    return _fig_to_base64(fig)

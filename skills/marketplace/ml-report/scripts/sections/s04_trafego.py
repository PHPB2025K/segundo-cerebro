"""Seção 04 — Tráfego & Visibilidade"""

from .helpers import *

def needs_data():
    return []

def build(**kwargs):
    return '''
    <div class="page">
        <div class="section-header"><span class="section-number">04</span><h2>👁️ Tráfego & Visibilidade</h2></div>
        <div class="na-section">
            <div class="na-icon">📊</div>
            <h3>Dados de tráfego não disponíveis via API</h3>
            <p>A API do Mercado Livre restringe acesso a dados de visitas, impressões e CTR para apps certificados.</p>
            <div class="na-actions">
                <h4>Como obter esses dados:</h4>
                <ul>
                    <li>Acessar <strong>Painel do Vendedor → Métricas</strong> no ML</li>
                    <li>Exportar CSV de visitas por anúncio</li>
                    <li>Enviar ao Tobias para inclusão no próximo relatório</li>
                </ul>
            </div>
        </div>
        <div class="insight-box insight-warning"><span class="insight-icon">⚠️</span><div class="insight-content">
            <strong>Ação recomendada:</strong> Exportar o CSV de métricas do painel do ML para análise de CTR, split orgânico vs pago, e oportunidades.
        </div></div>
    </div>'''

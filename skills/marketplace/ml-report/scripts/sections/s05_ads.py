"""Seção 05 — Publicidade / ML Ads"""

from .helpers import *

def needs_data():
    return []

def build(**kwargs):
    return '''
    <div class="page">
        <div class="section-header"><span class="section-number">05</span><h2>📣 Publicidade / Mercado Livre Ads</h2></div>
        <div class="na-section">
            <div class="na-icon">📣</div>
            <h3>Dados de Ads não disponíveis via API padrão</h3>
            <p>A API de Product Ads do Mercado Livre requer certificação específica de parceiro.</p>
            <div class="na-actions">
                <h4>Como obter esses dados:</h4>
                <ul>
                    <li>Acessar <strong>Mercado Livre Ads → Relatórios</strong></li>
                    <li>Exportar relatório de campanhas do período</li>
                    <li>Enviar ao Tobias para análise completa de ROAS, ACOS, CPC</li>
                </ul>
                <p class="na-note">💡 <em>Para análise detalhada de campanhas, segmentação e otimizações, solicitar Relatório de Ads dedicado com os dados exportados.</em></p>
            </div>
        </div>
    </div>'''

#!/usr/bin/env python3
"""
Gráfica de Migración Venezuela → Colombia
Librería: Plotly (elegante e interactiva)
"""

import plotly.graph_objects as go
import plotly.io as pio

# Datos de evolución Colombia
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
counts = [30000, 50000, 200000, 550000, 1200000, 1700000, 1950000, 2500000, 2650000, 2800000, 2828195]
labels = ['30K', '50K', '200K', '550K', '1.2M', '1.7M', '1.95M', '2.5M', '2.65M', '2.8M', '2.83M']

# Colores del sitio
COLORS = {
    'wine': '#6a040f',
    'gold': '#ffba08',
    'dark': '#370617',
    'light_wine': '#9d0208'
}

# Crear figura
fig = go.Figure()

# Área bajo la curva (gradiente)
fig.add_trace(go.Scatter(
    x=years,
    y=counts,
    fill='tozeroy',
    fillcolor='rgba(255, 186, 8, 0.2)',  # Dorado con transparencia
    line=dict(color='rgba(0,0,0,0)', width=0),
    showlegend=False,
    hoverinfo='skip'
))

# Línea principal
fig.add_trace(go.Scatter(
    x=years,
    y=counts,
    mode='lines+markers+text',
    name='Migrantes Colombia',
    line=dict(
        color=COLORS['gold'],
        width=4,
        shape='spline',
        smoothing=1.3
    ),
    marker=dict(
        size=12,
        color=COLORS['wine'],
        line=dict(color=COLORS['gold'], width=2),
        symbol='circle'
    ),
    text=labels,
    textposition='top center',
    textfont=dict(
        size=10,
        color=COLORS['dark'],
        family='Arial Black'
    ),
    hovertemplate='<b>%{x}</b><br>%{customdata:,} migrantes<extra></extra>',
    customdata=counts
))

# Layout elegante
fig.update_layout(
    title=dict(
        text='<b>Migración Venezuela → Colombia (Evolución Anual)</b><br><span style="font-size:14px;color:#666666;font-weight:normal">Principal país de acogida con el 41% del total migratorio (2.8 millones)</span>',
        font=dict(size=22, color=COLORS['dark'], family='Arial'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Año', font=dict(size=14, color=COLORS['wine'])),
        tickfont=dict(size=11, color='#444444'),
        gridcolor='rgba(200,200,200,0.3)',
        linecolor=COLORS['wine'],
        linewidth=2,
        showgrid=True
    ),
    yaxis=dict(
        title=dict(text='Número de Migrantes', font=dict(size=14, color=COLORS['wine'])),
        tickfont=dict(size=11, color='#444444'),
        gridcolor='rgba(200,200,200,0.3)',
        linecolor=COLORS['wine'],
        linewidth=2,
        showgrid=True,
        tickformat=',',
        range=[0, 3200000]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    hovermode='x unified',
    showlegend=False,
    margin=dict(l=80, r=50, t=100, b=60),
    annotations=[
        dict(
            text='Fuente: Plataforma R4V, ACNUR, OIM - Noviembre 2025',
            xref='paper', yref='paper',
            x=0.5, y=-0.12,
            showarrow=False,
            font=dict(size=11, color='#888888')
        )
    ]
)

# Guardar como PNG estático (alta resolución)
fig.write_image('public/images/evolucion-colombia-venezuela.png', 
                width=1200, height=600, scale=2)

# Guardar como HTML interactivo
fig.write_html('public/images/evolucion-colombia-venezuela.html', 
               include_plotlyjs='cdn', full_html=False)

print("✅ Gráfica Colombia generada: public/images/evolucion-colombia-venezuela.png")
print("✅ Versión interactiva: public/images/evolucion-colombia-venezuela.html")

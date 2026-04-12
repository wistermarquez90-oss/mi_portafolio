#!/usr/bin/env python3
"""
Gráfica de Evolución del Éxodo Venezolano
Librería: Plotly (elegante e interactiva)
"""

import plotly.graph_objects as go
import plotly.io as pio

# Datos de evolución
years = ['2015', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
counts = [700000, 1200000, 2000000, 3200000, 4000000, 4800000, 5500000, 6200000, 6800000, 6911757]
labels = ['700K', '1.2M', '2.0M', '3.2M', '4.0M', '4.8M', '5.5M', '6.2M', '6.8M', '6.9M']

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
    fillcolor='rgba(106, 4, 15, 0.15)',
    line=dict(color='rgba(0,0,0,0)', width=0),
    showlegend=False,
    hoverinfo='skip'
))

# Línea principal con gradiente
fig.add_trace(go.Scatter(
    x=years,
    y=counts,
    mode='lines+markers+text',
    name='Migrantes',
    line=dict(
        color=COLORS['wine'],
        width=4,
        shape='spline',
        smoothing=1.3
    ),
    marker=dict(
        size=14,
        color=COLORS['gold'],
        line=dict(color=COLORS['wine'], width=3),
        symbol='circle'
    ),
    text=labels,
    textposition='top center',
    textfont=dict(
        size=12,
        color=COLORS['dark'],
        family='Arial Black'
    ),
    hovertemplate='<b>%{x}</b><br>%{customdata:,} migrantes<extra></extra>',
    customdata=counts
))

# Layout elegante
fig.update_layout(
    title=dict(
        text='<b>Evolución del Éxodo Venezolano (2015-2025)</b><br><span style="font-size:14px;color:#666666;font-weight:normal">Total acumulado de migrantes venezolanos en América Latina y el Caribe</span>',
        font=dict(size=22, color=COLORS['dark'], family='Arial'),
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(text='Año', font=dict(size=14, color=COLORS['wine'])),
        tickfont=dict(size=12, color='#444444'),
        gridcolor='rgba(200,200,200,0.3)',
        linecolor=COLORS['wine'],
        linewidth=2,
        showgrid=True
    ),
    yaxis=dict(
        title=dict(text='Número de Migrantes', font=dict(size=14, color=COLORS['wine'])),
        tickfont=dict(size=12, color='#444444'),
        gridcolor='rgba(200,200,200,0.3)',
        linecolor=COLORS['wine'],
        linewidth=2,
        showgrid=True,
        tickformat=',',
        range=[0, 8000000]
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
fig.write_image('public/images/evolucion-exodo-venezolano.png', 
                width=1200, height=600, scale=2)

# Guardar como HTML interactivo (opcional)
fig.write_html('public/images/evolucion-exodo-venezolano.html', 
               include_plotlyjs='cdn', full_html=False)

print("✅ Gráfica generada: public/images/evolucion-exodo-venezolano.png")
print("✅ Versión interactiva: public/images/evolucion-exodo-venezolano.html")

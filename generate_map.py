#!/usr/bin/env python3
"""
Mapa de Distribución Migratoria Venezolana - V2
Nombres de países visibles y posiciones ajustadas
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.patheffects as path_effects

# Colores del sitio
COLORS = {
    'wine': '#6a040f',
    'wine_light': '#9d0208',
    'gold': '#ffba08',
    'gold_light': '#faa307',
    'orange': '#e85d04',
    'dark': '#370617',
    'purple': '#3d0066'
}

# Datos con posiciones personalizadas para labels
MIGRATION_DATA = {
    'Venezuela': {
        'lat': 6.4238, 'lon': -66.5897, 'count': 0, 'is_origin': True,
        'label_offset': (0, 4), 'label_pos': 'top'
    },
    'Colombia': {
        'lat': 4.5709, 'lon': -74.2973, 'count': 2828195, 'percent': 40.9, 
        'color': COLORS['wine'], 'label_offset': (-8, 2), 'label_pos': 'left'
    },
    'Perú': {
        'lat': -9.1900, 'lon': -75.0152, 'count': 1662889, 'percent': 24.0, 
        'color': COLORS['wine_light'], 'label_offset': (-6, 0), 'label_pos': 'left'
    },
    'Brasil': {
        'lat': -14.2350, 'lon': -51.9253, 'count': 732272, 'percent': 10.6, 
        'color': COLORS['orange'], 'label_offset': (0, -5), 'label_pos': 'bottom'
    },
    'Chile': {
        'lat': -35.6751, 'lon': -71.5430, 'count': 669408, 'percent': 9.7, 
        'color': '#f48c06', 'label_offset': (6, 0), 'label_pos': 'right'
    },
    'Ecuador': {
        'lat': -1.8312, 'lon': -78.1834, 'count': 440450, 'percent': 6.4, 
        'color': COLORS['gold'], 'label_offset': (-5, 3), 'label_pos': 'left'
    },
    'Argentina': {
        'lat': -38.4161, 'lon': -63.6167, 'count': 174796, 'percent': 2.5, 
        'color': COLORS['purple'], 'label_offset': (5, 2), 'label_pos': 'right'
    },
    'México': {
        'lat': 23.6345, 'lon': -102.5528, 'count': 106015, 'percent': 1.5, 
        'color': COLORS['gold'], 'label_offset': (-7, 0), 'label_pos': 'left'
    },
    'USA': {
        'lat': 37.0902, 'lon': -95.7129, 'count': 100000, 'percent': 1.4, 
        'color': COLORS['gold_light'], 'label_offset': (0, 4), 'label_pos': 'top'
    },
    'España': {
        'lat': 40.4637, 'lon': -3.7492, 'count': 80000, 'percent': 1.2, 
        'color': COLORS['wine'], 'label_offset': (5, 2), 'label_pos': 'right'
    },
}

def create_migration_map():
    fig = plt.figure(figsize=(18, 11), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
    
    # Extensión del mapa
    ax.set_extent([-125, 35, -55, 55], crs=ccrs.PlateCarree())
    
    # Fondo
    ax.add_feature(cfeature.OCEAN, facecolor='#e8f4f8', alpha=0.5)
    ax.add_feature(cfeature.LAND, facecolor='#f0f0f0', alpha=0.7)
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.3, color='#999999', linewidth=0.5)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8, color='#666666')
    
    # Gridlines sutiles
    gl = ax.gridlines(draw_labels=True, linewidth=0.3, color='gray', alpha=0.2, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xlabel_style = {'size': 8, 'color': 'gray'}
    gl.ylabel_style = {'size': 8, 'color': 'gray'}
    
    ven_lon = MIGRATION_DATA['Venezuela']['lon']
    ven_lat = MIGRATION_DATA['Venezuela']['lat']
    
    # Dibujar líneas de flujo
    for country, data in MIGRATION_DATA.items():
        if country == 'Venezuela' or data['count'] == 0:
            continue
            
        lon, lat = data['lon'], data['lat']
        count = data['count']
        color = data['color']
        
        linewidth = max(1, np.log10(count / 50000 + 1))
        alpha = min(0.7, 0.25 + count / 5000000)
        
        # Punto de control para curva
        mid_lon = (ven_lon + lon) / 2
        mid_lat = (ven_lat + lat) / 2 + (abs(lon - ven_lon) / 30)
        
        # Curva Bezier
        n_points = 60
        t = np.linspace(0, 1, n_points)
        curve_lon = (1-t)**2 * ven_lon + 2*(1-t)*t * mid_lon + t**2 * lon
        curve_lat = (1-t)**2 * ven_lat + 2*(1-t)*t * mid_lat + t**2 * lat
        
        # Dibujar línea
        ax.plot(curve_lon, curve_lat, transform=ccrs.PlateCarree(),
               color=color, linewidth=linewidth, alpha=alpha,
               solid_capstyle='round', zorder=1)
        
        # Flecha al final
        ax.annotate('', xy=(lon, lat), xytext=(curve_lon[-3], curve_lat[-3]),
                   transform=ccrs.PlateCarree(),
                   arrowprops=dict(arrowstyle='->', color=color, alpha=alpha, lw=0))
    
    # Dibujar círculos y etiquetas
    for country, data in MIGRATION_DATA.items():
        lon, lat = data['lon'], data['lat']
        count = data['count']
        offset_x, offset_y = data['label_offset']
        
        if data.get('is_origin'):
            # Venezuela - origen
            circle = Circle((lon, lat), 3.5, transform=ccrs.PlateCarree(),
                          facecolor=COLORS['dark'], edgecolor=COLORS['gold'], 
                          linewidth=4, zorder=10)
            ax.add_patch(circle)
            
            # Glow
            glow = Circle((lon, lat), 5, transform=ccrs.PlateCarree(),
                         facecolor='none', edgecolor=COLORS['gold'], 
                         linewidth=2, alpha=0.3, zorder=9)
            ax.add_patch(glow)
            
            # Label ORIGEN
            ax.text(lon, lat + 6, 'ORIGEN', transform=ccrs.PlateCarree(),
                   fontsize=10, fontweight='bold', color=COLORS['dark'],
                   ha='center', va='bottom', zorder=15,
                   bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                            edgecolor=COLORS['gold'], linewidth=2.5, alpha=0.95))
            
            # VEN dentro
            ax.text(lon, lat, 'VEN', transform=ccrs.PlateCarree(),
                   fontsize=11, fontweight='bold', color=COLORS['gold'],
                   ha='center', va='center', zorder=12)
        else:
            # Tamaño según cantidad
            if count > 1000000:
                radius = 3.2
            elif count > 500000:
                radius = 2.4
            elif count > 100000:
                radius = 1.8
            else:
                radius = 1.3
            
            color = data['color']
            
            # Círculo
            circle = Circle((lon, lat), radius, transform=ccrs.PlateCarree(),
                          facecolor=color, edgecolor='white', linewidth=2.5,
                          alpha=0.9, zorder=8)
            ax.add_patch(circle)
            
            # Glow externo
            glow = Circle((lon, lat), radius * 1.4, transform=ccrs.PlateCarree(),
                         facecolor='none', edgecolor=color, linewidth=1.5,
                         alpha=0.25, zorder=7)
            ax.add_patch(glow)
            
            # Calcular posición del label
            label_x = lon + offset_x
            label_y = lat + offset_y + (radius if offset_y > 0 else -radius if offset_y < 0 else 0)
            
            count_text = f"{count/1000000:.1f}M" if count >= 1000000 else f"{count/1000:.0f}K"
            
            # === NOMBRE DEL PAÍS ===
            # Fondo del texto (sombra más grande)
            for dx, dy in [(-0.8, 0), (0.8, 0), (0, -0.8), (0, 0.8), (-0.5, -0.5), (0.5, 0.5)]:
                ax.text(label_x + dx, label_y + dy, country.upper(), 
                       transform=ccrs.PlateCarree(),
                       fontsize=10, fontweight='bold', color='white',
                       ha='center', va='center', zorder=13)
            
            # Texto principal del país
            ax.text(label_x, label_y, country.upper(), transform=ccrs.PlateCarree(),
                   fontsize=10, fontweight='bold', color=color,
                   ha='center', va='center', zorder=14,
                   bbox=dict(boxstyle='round,pad=0.35', facecolor='white', 
                            edgecolor=color, linewidth=2, alpha=0.95))
            
            # === NÚMERO ===
            num_y = lat - radius - 2.5 if offset_y >= 0 else lat + radius + 2.5
            
            # Sombra del número
            for dx, dy in [(-0.5, 0), (0.5, 0), (0, -0.5), (0, 0.5)]:
                ax.text(lon + dx, num_y + dy, count_text, 
                       transform=ccrs.PlateCarree(),
                       fontsize=11, fontweight='bold', color='white',
                       ha='center', va='center', zorder=12)
            
            # Número principal
            ax.text(lon, num_y, count_text, transform=ccrs.PlateCarree(),
                   fontsize=11, fontweight='bold', color=COLORS['gold'],
                   ha='center', va='center', zorder=13,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['dark'], 
                            edgecolor=COLORS['gold'], linewidth=1.5, alpha=0.95))
    
    # Título principal
    ax.set_title('Distribución de Migrantes Venezolanos en el Mundo', 
                fontsize=20, fontweight='bold', color=COLORS['dark'], pad=15)
    
    # Subtítulo
    fig.text(0.5, 0.93, 'Total: 6.9 millones de personas en América Latina y el Caribe | Fuente: R4V, ACNUR, OIM (Nov 2025)',
             ha='center', fontsize=12, color='#555555', style='italic')
    
    # Leyenda mejorada
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['wine'], edgecolor='white', linewidth=2, label='Colombia (2.8M)'),
        mpatches.Patch(facecolor=COLORS['wine_light'], edgecolor='white', linewidth=2, label='Perú (1.7M)'),
        mpatches.Patch(facecolor=COLORS['orange'], edgecolor='white', linewidth=2, label='Brasil/Chile (600K+)'),
        mpatches.Patch(facecolor=COLORS['gold'], edgecolor='white', linewidth=2, label='Ecuador/Argentina (100K+)'),
        mpatches.Patch(facecolor=COLORS['dark'], edgecolor=COLORS['gold'], linewidth=3, label='Origen: Venezuela'),
    ]
    
    legend = ax.legend(handles=legend_elements, loc='lower left', 
                      fontsize=10, framealpha=0.98,
                      fancybox=True, shadow=True,
                      title='Destinos Principales', title_fontsize=11)
    legend.get_title().set_fontweight('bold')
    legend.get_title().set_color(COLORS['dark'])
    
    # Guardar
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    
    plt.savefig('public/images/mapa-migracion-venezuela.png', 
                dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig('public/images/mapa-migracion-venezuela.svg',
                bbox_inches='tight', facecolor='white')
    
    print("✅ Mapa generado: public/images/mapa-migracion-venezuela.png")
    print("✅ Vector generado: public/images/mapa-migracion-venezuela.svg")
    
    plt.close()

if __name__ == '__main__':
    create_migration_map()

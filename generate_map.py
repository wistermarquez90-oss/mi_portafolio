#!/usr/bin/env python3
"""
Mapa de Distribución Migratoria Venezolana
Genera un mapa profesional con flujos migratorios
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.collections import LineCollection
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.patch import geos_to_path
import matplotlib.patheffects as path_effects

# Configuración de estilo - Colores del sitio
COLORS = {
    'wine': '#6a040f',
    'wine_light': '#9d0208',
    'gold': '#ffba08',
    'gold_light': '#faa307',
    'orange': '#e85d04',
    'dark': '#370617',
    'purple': '#3d0066'
}

# Datos de migración
MIGRATION_DATA = {
    'Venezuela': {'lat': 6.4238, 'lon': -66.5897, 'count': 0, 'is_origin': True},
    'Colombia': {'lat': 4.5709, 'lon': -74.2973, 'count': 2828195, 'percent': 40.9, 'color': COLORS['wine']},
    'Perú': {'lat': -9.1900, 'lon': -75.0152, 'count': 1662889, 'percent': 24.0, 'color': COLORS['wine_light']},
    'Brasil': {'lat': -14.2350, 'lon': -51.9253, 'count': 732272, 'percent': 10.6, 'color': COLORS['orange']},
    'Chile': {'lat': -35.6751, 'lon': -71.5430, 'count': 669408, 'percent': 9.7, 'color': '#f48c06'},
    'Ecuador': {'lat': -1.8312, 'lon': -78.1834, 'count': 440450, 'percent': 6.4, 'color': COLORS['gold']},
    'Argentina': {'lat': -38.4161, 'lon': -63.6167, 'count': 174796, 'percent': 2.5, 'color': COLORS['purple']},
    'México': {'lat': 23.6345, 'lon': -102.5528, 'count': 106015, 'percent': 1.5, 'color': COLORS['gold']},
    'USA': {'lat': 37.0902, 'lon': -95.7129, 'count': 100000, 'percent': 1.4, 'color': COLORS['gold_light']},
    'España': {'lat': 40.4637, 'lon': -3.7492, 'count': 80000, 'percent': 1.2, 'color': COLORS['wine']},
}

def create_migration_map():
    # Crear figura con proyección
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
    
    # Extensión del mapa: América + parte de Europa
    ax.set_extent([-120, 30, -55, 55], crs=ccrs.PlateCarree())
    
    # Fondo del océano
    ax.add_feature(cfeature.OCEAN, facecolor='#e8f4f8', alpha=0.6)
    ax.add_feature(cfeature.LAND, facecolor='#f5f5f5', alpha=0.8)
    ax.add_feature(cfeature.BORDERS, linestyle=':', alpha=0.4, color='gray')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8, color='#666666')
    
    # Gridlines
    gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.3, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    
    # Obtener coordenadas de Venezuela (origen)
    ven_lon = MIGRATION_DATA['Venezuela']['lon']
    ven_lat = MIGRATION_DATA['Venezuela']['lat']
    
    # Dibujar líneas de flujo desde Venezuela
    for country, data in MIGRATION_DATA.items():
        if country == 'Venezuela' or data['count'] == 0:
            continue
            
        lon, lat = data['lon'], data['lat']
        count = data['count']
        color = data['color']
        
        # Grosor de línea proporcional al flujo
        linewidth = np.log10(count / 10000 + 1) * 1.5
        alpha = min(0.8, 0.3 + count / 3000000)
        
        # Crear línea curva (bezier simplificada)
        mid_lon = (ven_lon + lon) / 2
        mid_lat = (ven_lat + lat) / 2 + 5  # Curva hacia arriba
        
        # Puntos para la curva
        n_points = 50
        t = np.linspace(0, 1, n_points)
        
        # Interpolación cuadrática de Bézier
        curve_lon = (1-t)**2 * ven_lon + 2*(1-t)*t * mid_lon + t**2 * lon
        curve_lat = (1-t)**2 * ven_lat + 2*(1-t)*t * mid_lat + t**2 * lat
        
        # Dibujar línea con gradiente
        for i in range(n_points - 1):
            alpha_seg = alpha * (0.5 + 0.5 * np.sin(i / n_points * np.pi))
            ax.plot([curve_lon[i], curve_lon[i+1]], 
                   [curve_lat[i], curve_lat[i+1]],
                   transform=ccrs.PlateCarree(),
                   color=color, 
                   linewidth=linewidth,
                   alpha=alpha_seg,
                   solid_capstyle='round')
    
    # Dibujar círculos para cada país
    for country, data in MIGRATION_DATA.items():
        lon, lat = data['lon'], data['lat']
        count = data['count']
        
        if data.get('is_origin'):
            # Venezuela - origen destacado
            circle = Circle((lon, lat), 4, transform=ccrs.PlateCarree(),
                          facecolor=COLORS['dark'], 
                          edgecolor=COLORS['gold'], 
                          linewidth=3,
                          zorder=10)
            ax.add_patch(circle)
            
            # Label
            ax.text(lon, lat + 6, 'ORIGEN', transform=ccrs.PlateCarree(),
                   fontsize=9, fontweight='bold', color=COLORS['dark'],
                   ha='center', va='bottom',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                            edgecolor=COLORS['gold'], linewidth=2, alpha=0.9))
            
            ax.text(lon, lat - 1, 'VEN', transform=ccrs.PlateCarree(),
                   fontsize=10, fontweight='bold', color=COLORS['gold'],
                   ha='center', va='center', zorder=11)
        else:
            # Tamaño proporcional al número de migrantes
            if count > 1000000:
                radius = 3.5
                fontsize = 10
            elif count > 500000:
                radius = 2.5
                fontsize = 9
            elif count > 100000:
                radius = 1.8
                fontsize = 8
            else:
                radius = 1.2
                fontsize = 7
            
            color = data['color']
            
            # Círculo principal
            circle = Circle((lon, lat), radius, transform=ccrs.PlateCarree(),
                          facecolor=color, 
                          edgecolor='white', 
                          linewidth=2,
                          alpha=0.85,
                          zorder=8)
            ax.add_patch(circle)
            
            # Círculo de brillo externo
            glow = Circle((lon, lat), radius * 1.3, transform=ccrs.PlateCarree(),
                         facecolor='none', 
                         edgecolor=color, 
                         linewidth=1,
                         alpha=0.3,
                         zorder=7)
            ax.add_patch(glow)
            
            # Label del país
            label_y = lat + radius + 2
            count_text = f"{count/1000000:.1f}M" if count >= 1000000 else f"{count/1000:.0f}K"
            
            # Sombra del texto
            ax.text(lon, label_y, country, transform=ccrs.PlateCarree(),
                   fontsize=fontsize, fontweight='bold', color='white',
                   ha='center', va='bottom', zorder=12,
                   path_effects=[path_effects.withStroke(linewidth=3, foreground='white')])
            
            # Texto principal
            ax.text(lon, label_y, country, transform=ccrs.PlateCarree(),
                   fontsize=fontsize, fontweight='bold', color='white',
                   ha='center', va='bottom', zorder=13)
            
            # Número debajo
            ax.text(lon, lat - radius - 1, count_text, transform=ccrs.PlateCarree(),
                   fontsize=fontsize+1, fontweight='bold', color=COLORS['gold'],
                   ha='center', va='top', zorder=12,
                   bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['dark'], 
                            edgecolor='none', alpha=0.8))
    
    # Título
    title = ax.set_title('Distribución de Migrantes Venezolanos en el Mundo', 
                        fontsize=18, fontweight='bold', color=COLORS['dark'],
                        pad=20)
    
    # Subtítulo
    fig.text(0.5, 0.92, 'Total: 6.9 millones de personas en América Latina y el Caribe | Fuente: R4V, ACNUR, OIM (Nov 2025)',
             ha='center', fontsize=11, color='#666666', style='italic')
    
    # Leyenda
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['wine'], edgecolor='white', label='Colombia >2M'),
        mpatches.Patch(facecolor=COLORS['wine_light'], edgecolor='white', label='Perú >1M'),
        mpatches.Patch(facecolor=COLORS['orange'], edgecolor='white', label='Brasil/Chile >500K'),
        mpatches.Patch(facecolor=COLORS['gold'], edgecolor='white', label='Otros >100K'),
        mpatches.Patch(facecolor=COLORS['dark'], edgecolor=COLORS['gold'], linewidth=2, label='Origen (Venezuela)'),
    ]
    
    ax.legend(handles=legend_elements, loc='lower left', 
             fontsize=9, framealpha=0.95,
             fancybox=True, shadow=True)
    
    # Guardar
    plt.tight_layout()
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

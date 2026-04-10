# Portafolio Profesional - Wister Márquez

Portafolio web profesional desarrollado con **Astro 5.x**, diseñado para economistas y especialistas en análisis de datos.

## 🚀 Demo

[Ver portafolio en vivo](https://wistermarquez90-oss.github.io/mi_portafolio/)

## 📁 Estructura del Proyecto

```
src/
├── components/          # Componentes reutilizables
│   ├── Navigation.astro
│   ├── HeroSection.astro
│   ├── AboutSection.astro
│   ├── SkillsSection.astro
│   ├── ExperienceSection.astro
│   ├── CTASection.astro
│   └── Footer.astro
├── layouts/            # Layouts principales
│   └── Layout.astro
├── pages/              # Páginas del sitio
│   ├── index.astro           # Home
│   ├── powerbi.astro         # Dashboards Power BI
│   ├── pasantias.astro       # Sección de pasantías
│   ├── ensenanza.astro       # Capacitación
│   ├── contacto.astro        # Contacto
│   └── investigacion/
│       ├── index.astro              # Landing investigación
│       ├── politica-fiscal.astro    # Asignatura 1
│       ├── planificacion.astro      # Asignatura 2
│       └── integracion.astro        # Asignatura 3
├── content/            # Contenido markdown
│   └── pasantias/
│       ├── 01-pasantias-investigacion.md
│       └── 02-ensenanza-capacitacion.md
└── styles/             # Estilos globales
```

## 🛠️ Tecnologías

- **Framework:** [Astro 5.x](https://astro.build)
- **Estilos:** [Tailwind CSS 3.4](https://tailwindcss.com)
- **Animaciones:** [AOS](https://michalsnik.github.io/aos/)
- **Tipografía:** Inter + Playfair Display
- **Deploy:** GitHub Pages

## 🎨 Paleta de Colores

| Color | Hex | Uso |
|-------|-----|-----|
| Vinotinto | `#6a040f` | Color principal |
| Vinotinto Oscuro | `#370617` | Hover, gradientes |
| Dorado | `#ffba08` | Acentos, highlights |

## 🚀 Despliegue en GitHub Pages

### 1. Configurar `astro.config.mjs`

```javascript
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://wistermarquez90-oss.github.io',
  base: '/mi_portafolio',
  output: 'static',
});
```

### 2. Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/wistermarquez90-oss/mi_portafolio.git
git push -u origin main
```

### 3. Configurar GitHub Pages

1. Ir a **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** → **/ (root)**
4. Guardar

### 4. GitHub Actions (Opcional)

Crear `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## 📝 Scripts Disponibles

| Comando | Descripción |
|---------|-------------|
| `npm install` | Instalar dependencias |
| `npm run dev` | Servidor de desarrollo |
| `npm run build` | Build para producción |
| `npm run preview` | Previsualizar build |

## 📄 Licencia

Este proyecto es de uso personal.

---

**Wister Márquez** - Economista en Formación | Especialista en E-commerce

import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [mdx(), tailwind()],
  output: 'static',
  outDir: './dist',
  build: {
    assets: 'assets'
  },
  site: 'https://wistermarquez90-oss.github.io',
  base: '/mi_portafolio/'
});

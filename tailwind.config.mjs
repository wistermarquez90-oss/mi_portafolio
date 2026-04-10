/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'wine': {
          DEFAULT: '#6a040f',
          50: '#fff0f0',
          100: '#ffdcdc',
          200: '#ffbfbf',
          300: '#ff9292',
          400: '#ff5454',
          500: '#ff1f1f',
          600: '#e60000',
          700: '#c10000',
          800: '#9f0606',
          900: '#6a040f',
          950: '#4a0005',
        },
        'gold': {
          DEFAULT: '#ffba08',
          50: '#fffbeb',
          100: '#fff3c6',
          200: '#ffe588',
          300: '#ffd24a',
          400: '#ffba08',
          500: '#e69c00',
          600: '#bf7a00',
          700: '#995600',
          800: '#734000',
          900: '#4d2900',
          950: '#2b1400',
        },
      },
      fontFamily: {
        'display': ['Playfair Display', 'serif'],
        'body': ['Inter', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.8s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'slide-down': 'slideDown 0.6s ease-out',
        'scale-in': 'scaleIn 0.5s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.9)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}

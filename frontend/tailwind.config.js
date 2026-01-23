/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#4c1d95', // Deep purple
        secondary: '#ea580c', // Orange accent
        'brand-purple': '#4a0e8f',
        'brand-orange': '#ff6b00',
        'brand-light': '#f3f4f6',
        'brand-dark': '#1a1a2e', // Deep midnight blue/purple replacing black
      },
      backgroundImage: {
        'purple-texture': "url('https://www.transparenttextures.com/patterns/cubes.png')", // Subtle pattern example
      },
      animation: {
        'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
        'zoom-in': 'zoomIn 0.5s ease-out forwards',
        'bounce-slow': 'bounce 3s infinite',
        'slide-in-right': 'slideInRight 0.8s ease-out forwards',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        zoomIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        slideInRight: {
          '0%': { opacity: '0', transform: 'translateX(50px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        }
      }
    }
  },
  plugins: [],
}
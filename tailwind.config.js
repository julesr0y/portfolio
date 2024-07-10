/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './public/**/*.js'],
  safelist: ['bg-main-color', 'bg-second-color'],
  theme: {
    extend: {
      fontFamily: {
        CabinetGrotesk: ['CabinetGrotesk', 'sans-serif'],
        Satoshi: ['Satoshi', 'sans-serif'],
        SatoshiItalic: ['SatoshiItalic', 'sans-serif']
      },
      colors: {
        'main-color': '#111111',
        'second-color': '#171717',
        'third-color': '#e63946',
        'border-color': '#2c2c2c'
      }
    },
  },
  plugins: [],
}
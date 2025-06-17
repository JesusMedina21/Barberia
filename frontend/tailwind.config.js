/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./node_modules/@ionic/react/dist/**/*.{js,jsx,ts,tsx}",
    "./node_modules/flowbite/**/*.jsx",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        amber: {
          500: '#f59e0b',
          600: '#d97706',
        },
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}
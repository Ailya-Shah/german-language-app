/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html}',  // This ensures Tailwind scans your HTML files in the 'templates' directory
    './static/styles/*.css',    // This ensures Tailwind scans your CSS files
  ],
  theme: {
    extend: {
      colors: {
        customBlue: '#1E40AF',
        customGreen: '#10B981',
      },
      fontFamily: {
        customFont: ['"Poppins"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}



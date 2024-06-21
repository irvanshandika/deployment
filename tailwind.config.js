/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        "google": ["Google Sans", "sans-serif"],
        "roboto": ["Roboto Sans", "sans-serif"],
      },
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
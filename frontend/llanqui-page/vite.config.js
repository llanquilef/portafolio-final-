import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: 'dist', // Asegúrate de que el build apunte aquí
  },
  server: {
    host: true,
    port: 8080,
  },
  resolve: {
    alias: {
      '@': '/src',
    },
  },
})

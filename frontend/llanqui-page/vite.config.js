import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
    base: '/static/',       // Base para servir archivos en producción
    build: {
        outDir: 'dist',     // Carpeta generada por Vite
        assetsDir: 'assets' // Subcarpeta para CSS, JS e imágenes
    },
    plugins: [react()],
});

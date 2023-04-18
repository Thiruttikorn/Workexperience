import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
//export default defineConfig({
//  plugins: [vue()]
//})

export default defineConfig({
    resolve: { alias: { '@': '/src' } },
    plugins: [vue()],
    server: {
        host: true,
        port: 3000
    },
    base: '/or4/'
})


export default defineNuxtConfig({
  modules: [
    "@nuxtjs/supabase",
    '@vueuse/motion/nuxt'
  ],
  css: [
    "~/assets/css/main.css",
    "v-network-graph/lib/style.css"
  ],
  supabase: {
    key: process.env.SUPABASE_ANON_KEY, // Supabase の API Keyの設定
  },
  runtimeConfig: {
    public: {
      redirectHost: process.env.REDIRECT_HOST, // リダイレクト先の ホスト名の設定
      motion: {
        directives: {
          'pop-bottom': {
            initial: {
              scale: 0,
              opacity: 0,
              y: 100,
            },
            visible: {
              scale: 1,
              opacity: 1,
              y: 0,
            }
          }
        }
      }
    },
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
});

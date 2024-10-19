export default defineNuxtConfig({
  modules: ["@nuxtjs/supabase"],
  css: ["~/assets/css/main.css"],
  supabase: {
    key: process.env.SUPABASE_ANON_KEY, // Supabase の API Keyの設定
  },
  runtimeConfig: {
    public: {
      redirectHost: process.env.REDIRECT_HOST, // リダイレクト先の ホスト名の設定
    },
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
});

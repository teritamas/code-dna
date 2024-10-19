<script setup lang="ts">
  const supabase = useSupabaseClient();
  const runtimeConfig = useRuntimeConfig();
  const signInWithGithub = async () => {
    const { error } = await supabase.auth.signInWithOAuth({
      provider: "github",
      options: {
        redirectTo: `${runtimeConfig.public.redirectHost}/confirm`,
      },
    });
    if (error) console.log(error);
  };
</script>
<template>
  <div>
    <button @click="signInWithGithub">Sign In with Github</button>
  </div>
</template>

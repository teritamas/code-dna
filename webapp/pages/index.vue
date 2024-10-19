<script setup lang="ts">
  const client = useSupabaseClient();
  const userEmail = ref("");

  onMounted(async () => {
    const user = await client.auth.getUser();

    // 認証されていない時、ログインページにリダイレクト
    if (!user) {
      client.auth.signOut();
      window.location.href = "/login";
    }

    // 認証されている場合はユーザー情報を取得
    userEmail.value = user.data.user?.email!; // ユーザーのメールアドレスを取得
  });
</script>
<template>
  <div>
    <p>Hello！ {{ userEmail }}</p>
  </div>
</template>

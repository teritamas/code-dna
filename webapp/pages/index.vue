<script setup lang="ts">
  import DnaSummaryCreateStatus from "@/types/dna_summary_create_status";

  const client = useSupabaseClient();
  const userId = ref("");
  const userEmail = ref("");

  onMounted(async () => {
    const user = await client.auth.getUser();

    // 認証されていない時、ログインページにリダイレクト
    if (!user) {
      client.auth.signOut();
      window.location.href = "/login";
    }

    // 認証されている場合はユーザー情報を取得
    userId.value = user.data.user?.id!;
    userEmail.value = user.data.user?.email!; // ユーザーのメールアドレスを取得

    // TODO: 暫定処理でログインと同時に取得する。本来はユーザが「診断する」ボタンをクリックした時に実行する
    await syncGithubProviderTokenAndUpdateStatus();
  });

  const syncGithubProviderTokenAndUpdateStatus = async () => {
    // Githubのアクセストークンを取得
    const session = await client.auth.getSession();
    const userName = session.data.session?.user.user_metadata.user_name;
    const providerToken = session.data.session?.provider_token;

    const response = await fetch(
      `https://api.github.com/users/${userName}/events`,
      {
        // {username}にGitHubのユーザー名を入れます
        headers: {
          Authorization: `token ${providerToken}`,
        },
      }
    );

    // Githubのアクセストークン向こうのレスポンスが401の場合は、アクセストークンが無効なので再認証を促す
    if (response.status === 401) {
      // 401 Unauthorizedの場合は、アクセストークンが無効なので、再認証を促す
      alert("GitHubのアクセストークンが無効です。再認証してください。");
      client.auth.signOut();
      window.location.href = "/login";
    } else {
      // デバッグ用にレスポンスをコンソールに表示
      console.log(response);
    }

    // DBに更新リクエストを登録
    const { data, error } = await client
      .from("profiles")
      .update({
        github_provider_token: providerToken,
        dna_summary_create_status: DnaSummaryCreateStatus.InProgress,
      } as never)
      .eq("id", userId.value)
      .select();
  };
</script>
<template>
  <div>
    <p>Hello！ {{ userEmail }}</p>
  </div>
</template>

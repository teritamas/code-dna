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
  <div class="bg-white">
    <div class="relative isolate px-6 lg:px-8">
      <div
        class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        ></div>
      </div>
      <div class="mx-auto max-w-2xl py-16 sm:py-24 lg:py-32">
        <div class="text-center">
          <p>{{ userEmail }}さんは</p>
          <h1
            class="text-balance text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl"
          >
            直感的な解説者
          </h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            大きな視点でシンプルな設計を行い、必要に応じてコメントで説明。進捗をこまめに記録し、柔軟に対応するエンジニアです。
          </p>
        </div>
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconChartBar class="w-6 fill-red-700 inline" />
          アイデンティティチャート
        </h2>
        <div class="p-5">
          <section-skill-charts />
        </div>
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconBookmark class="w-6 fill-green-700 inline" />
          特長
        </h2>
        <section-feature />
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconCrown class="w-7 fill-yellow-400 inline" />
          強み
        </h2>
        <section-strong />
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconValue class="w-7 fill-purple-400 inline" />
          開発の場面でのあなたの価値
        </h2>
        <section-value class="mt-2" />
      </div>
      <div
        class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
        aria-hidden="true"
      >
        <div
          class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
          style="
            clip-path: polygon(
              74.1% 44.1%,
              100% 61.6%,
              97.5% 26.9%,
              85.5% 0.1%,
              80.7% 2%,
              72.5% 32.5%,
              60.2% 62.4%,
              52.4% 68.1%,
              47.5% 58.3%,
              45.2% 34.5%,
              27.5% 76.7%,
              0.1% 64.9%,
              17.9% 100%,
              27.6% 76.8%,
              76.1% 97.7%,
              74.1% 44.1%
            );
          "
        ></div>
      </div>
    </div>
  </div>
</template>

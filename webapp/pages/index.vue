<script setup lang="ts">
import DnaSummaryCreateStatus from "@/types/dna_summary_create_status";

const client = useSupabaseClient();
const userId = ref("");
const userEmail = ref("");
const analyticsData = ref({});
const analyticsStatus = ref(DnaSummaryCreateStatus.NotYet);

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

  analyticsStatus.value = await fetchAnalysisStatus();
  console.log(analyticsStatus.value);

  if (analyticsStatus.value === DnaSummaryCreateStatus.Completed) {
    // 診断が未実施の場合は、診断を実行
    analyticsData.value = await fetchAnalysisData();
  }

  // TODO: 暫定処理でログインと同時に取得する。本来はユーザが「診断する」ボタンをクリックした時に実行する
  await syncGithubProviderTokenAndUpdateStatus();
});

const fetchAnalysisStatus = async () => {
  const { data, error } = await client
    .from("profiles")
    .select("dna_summary_create_status")
    .eq("id", userId.value);

  if (error) {
    console.error(error);
    return DnaSummaryCreateStatus.NotYet;
  }

  if (data.length === 0) {
    // プロフィールが存在しない場合は新規作成
    return DnaSummaryCreateStatus.NotYet;
  }

  // enumのDnaSummaryCreateStatusに変換
  const status = data[0].dna_summary_create_status;
  return status;
};


const fetchAnalysisData = async () => {
  const { data, error } = await client
    .from("code_dna_summary")
    .select()
    .eq("profile_id", userId.value);

  console.log(data);
  if (error) {
    console.error(error);
    return {};
  }

  if (data.length === 0) {
    // プロフィールが存在しない場合は新規作成
    return {};
  }

  return data[0];
};

const syncGithubProviderTokenAndUpdateStatus = async () => {
  // Githubのアクセストークンを取得
  const session = await client.auth.getSession();
  const providerToken = session.data.session?.provider_token;

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
      <!-- ログインしていないときはログイン画面 -->
      <div 
        v-if="analyticsStatus === DnaSummaryCreateStatus.InProgress"
        class="mx-auto max-w-2xl py-16 sm:py-24 lg:py-32"
      >
        処理中の画面を出す
      </div>
      <div v-else class="mx-auto max-w-2xl py-16 sm:py-24 lg:py-32">
        <div class="text-center">
          <p>{{ userEmail }}さんは</p>
          <h1
            class="text-balance text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl"
          >
            {{ analyticsData.identity_name }}
          </h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            {{ analyticsData.summary_comment }}
          </p>
        </div>
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconChartBar class="w-6 fill-red-700 inline" />
          アイデンティティチャート
        </h2>
        <div class="p-5">
          <section-skill-charts
            :variableNameSimplicityRate="analyticsData.variable_name_simplicity_rate"
            :methodSplittingCoarsenessRate="analyticsData.method_splitting_coarseness_rate"
            :processingIntentCommunicatingRate="analyticsData.processing_intent_communicating_rate"
            :commitGranularityRate="analyticsData.commit_granularity_rate"
          />
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

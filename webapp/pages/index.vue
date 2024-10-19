<script setup lang="ts">
import DnaSummaryCreateStatus from "@/types/dna_summary_create_status";

const client = useSupabaseClient();
const userId = ref("");
const userName = ref("");
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
  userName.value = user.data.user?.user_metadata?.full_name!;

  analyticsStatus.value = await fetchAnalysisStatus();

  if (analyticsStatus.value === DnaSummaryCreateStatus.Completed) {
    // 診断が未実施の場合は、診断を実行
    analyticsData.value = await fetchAnalysisData();
  } else if (analyticsStatus.value === DnaSummaryCreateStatus.InProgress) {
    await fetchStatusUntilInProgress();
  }
});

const fetchAnalysisStatus = async () => {
  const { data, error } = await client
    .from("profiles")
    .select("dna_summary_create_status")
    .eq("id", userId.value);

  if (error) {
    console.error(error);
    return DnaSummaryCreateStatus.Failed;
  }

  if (data.length === 0) {
    // プロフィールが存在しない場合は新規作成
    return DnaSummaryCreateStatus.Failed;
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
    analyticsData.value = DnaSummaryCreateStatus.Failed;
    return {};
  }

  if (data.length === 0) {
    analyticsData.value = DnaSummaryCreateStatus.Failed;
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

  analyticsStatus.value = await fetchAnalysisStatus();

  await fetchStatusUntilInProgress();
};

const fetchStatusUntilInProgress = async () => {
  const interval = setInterval(async () => {
    analyticsStatus.value = await fetchAnalysisStatus();
    if (analyticsStatus.value !== DnaSummaryCreateStatus.InProgress) {
      // 解析が完了した場合はデータを取得
      if (analyticsStatus.value === DnaSummaryCreateStatus.Completed) {
        analyticsData.value = await fetchAnalysisData();
      }
      clearInterval(interval);
    }
  }, 5000);
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
      <div
        v-if="analyticsStatus === DnaSummaryCreateStatus.NotYet"
        class="mx-auto max-w-2xl pt-16 sm:pt-24 lg:pt-32"
      >
        <section-analysis
          @syncGithubProviderTokenAndUpdateStatus="
            syncGithubProviderTokenAndUpdateStatus
          "
        />
      </div>
      <div
        v-else-if="analyticsStatus === DnaSummaryCreateStatus.InProgress"
        class="mx-auto max-w-2xl pt-16 sm:pt-24 lg:pt-32"
      >
        <!--処理中の画面を出す-->
        <div class="mx-auto block text-center">
          <loading />
        </div>
      </div>
      <div
        v-else-if="analyticsStatus === DnaSummaryCreateStatus.Completed"
        class="mx-auto max-w-2xl pt-16 sm:pt-24 lg:pt-32"
      >
        <div class="text-center">
          <p>{{ userName }}さんは</p>
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
            :variableNameSimplicityRate="
              analyticsData.variable_name_simplicity_rate
            "
            :methodSplittingCoarsenessRate="
              analyticsData.method_splitting_coarseness_rate
            "
            :processingIntentCommunicatingRate="
              analyticsData.processing_intent_communicating_rate
            "
            :commitGranularityRate="analyticsData.commit_granularity_rate"
          />
        </div>
        <h2 class="mt-5 text-3xl font-bold dark:text-white">
          <IconBookmark class="w-6 fill-green-700 inline" />
          特長
        </h2>
        <section-feature 
          :variableNameSimplicityRateReason="
            analyticsData.variable_name_simplicity_rate_reason
          "
          :methodSplittingCoarsenessRateReason="
            analyticsData.method_splitting_coarseness_rate_reason
          "
          :processingIntentCommunicatingRateReason="
            analyticsData.processing_intent_communicating_rate_reason
          "
          :commitGranularityRateReason="analyticsData.commit_granularity_rate_reason"
        />
      </div>
      <section-error v-if="analyticsStatus === DnaSummaryCreateStatus.Failed" />
      <div
        v-if="
          analyticsStatus === DnaSummaryCreateStatus.Completed ||
          analyticsStatus === DnaSummaryCreateStatus.Failed
        "
        class="flex pt-12 gap-4 item-center justify-center"
      >
        <button
          type="button"
          class="py-2 px-4 flex justify-center items-center bg-gray-600 hover:bg-gray-700 focus:ring-gray-500 focus:ring-offset-gray-200 text-white transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg"
          @click="syncGithubProviderTokenAndUpdateStatus"
        >
          <svg
            width="20"
            height="20"
            fill="currentColor"
            class="mr-2"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 496 512"
          >
            <path
              d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
            />
          </svg>
          もう一度解析する
        </button>
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

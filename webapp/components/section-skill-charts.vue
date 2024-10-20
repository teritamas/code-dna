<script setup lang="ts">
import { computed, ref } from "vue";

const props = defineProps({
  variableNameSimplicityRate: {
    type: Number,
    required: true,
  },
  methodSplittingCoarsenessRate: {
    type: Number,
    required: true,
  },
  processingIntentCommunicatingRate: {
    type: Number,
    required: true,
  },
  commitGranularityRate: {
    type: Number,
    required: true,
  },
});

// 共通クラスロジック
const progressBarClass = (
  rate: number,
  threshold: number,
  colorClass: string
) => ({
  [colorClass]: rate >= threshold,
  "bg-dark": rate < threshold,
});

// テンプレートで使用するデータを構成するオブジェクト
const progressRates = computed(() => [
  {
    title: "変数名の付け方",
    dynamicDescription:
      props.variableNameSimplicityRate >= 0.5
        ? "文章のような変数名（変数の役割や内容を詳細に伝える）"
        : "短く簡潔に記述された変数名",
    value: props.variableNameSimplicityRate,
    colorClass: "bg-blue-600 text-white",
    leftLabel: "簡潔",
    rightLabel: "詳細",
    labelClass: "text-base text-lg font-bold text-blue-700 dark:text-blue-500",
  },
  {
    title: "クラスやメソッド分割の粒度",
    dynamicDescription:
      props.methodSplittingCoarsenessRate >= 0.5
        ? "細かく分割し、管理しやすく再利用性が高い"
        : "大局的な構造に基づく管理",
    value: props.methodSplittingCoarsenessRate,
    colorClass: "bg-red-600 text-white",
    leftLabel: "詳細",
    rightLabel: "大局的",
    labelClass: "text-base text-lg font-bold text-red-700 dark:text-blue-500",
  },
  {
    title: "処理の意図を伝える手段",
    dynamicDescription:
      props.processingIntentCommunicatingRate >= 0.5
        ? "メソッドやクラス名、変数名で表現"
        : "コメントで補足説明",
    value: props.processingIntentCommunicatingRate,
    colorClass: "bg-green-600 text-white",
    leftLabel: "コメント",
    rightLabel: "変数名",
    labelClass: "text-base text-lg font-bold text-green-700 dark:text-blue-500",
  },
  {
    title: "コミットの粒度",
    dynamicDescription:
      props.commitGranularityRate >= 0.5
        ? "作業単位（クラス作成、メソッド作成するたびにコミットする）"
        : "機能単位（一つの機能を実装するたびにコミットする）",
    value: props.commitGranularityRate,
    colorClass: "bg-yellow-400 text-white",
    leftLabel: "作業単位",
    rightLabel: "機能単位",
    labelClass:
      "text-base text-lg font-bold text-yellow-700 dark:text-blue-500",
  },
]);

// ホバー状態の管理
const hoveredIndex = ref<number | null>(null);
</script>

<template>
  <div v-for="(rate, index) in progressRates" :key="index" class="mb-1">
    <div class="relative w-full pt-5">
      <div class="flex justify-between">
        <span :class="rate.labelClass">{{ rate.title }}</span>
        <span class="hidden md:inline">{{ rate.dynamicDescription }}</span>
      </div>

      <!-- プログレスバー -->
      <div
        class="relative flex w-full h-2.5 overflow-hidden rounded-3xl bg-gray-100 h-6"
        @mouseover="hoveredIndex = index"
        @mouseleave="hoveredIndex = null"
      >
        <div
          role="progressbar"
          :aria-valuenow="Math.round(rate.value * 100)"
          aria-valuemin="0"
          aria-valuemax="100"
          :style="{ width: rate.value * 100 + '%' }"
          :class="progressBarClass(rate.value, 0.5, rate.colorClass)"
          class="flex h-full items-center justify-center rounded-full"
        >
          {{ rate.leftLabel }}
        </div>
        <div
          role="progressbar"
          :aria-valuenow="Math.round((1 - rate.value) * 100)"
          aria-valuemin="0"
          aria-valuemax="100"
          :style="{ width: (1 - rate.value) * 100 + '%' }"
          :class="progressBarClass(1 - rate.value, 0.5, rate.colorClass)"
          class="flex h-full items-center justify-center rounded-full"
        >
          {{ rate.rightLabel }}
        </div>
      </div>

      <!-- ホバー時にふわっと表示される割合 -->
      <transition name="fade">
        <span
          v-if="hoveredIndex === index"
          class="absolute bottom-0 mb-4 -translate-x-1/2 w-12 h-10 bg-white shadow-[0px_12px_30px_0px_rgba(16,24,40,0.1)] rounded-full px-3.5 py-2 text-gray-800 text-xs font-medium flex justify-center items-center after:absolute after:bg-white after:flex after:bottom-[-5px] after:left-1/2 after:-z-10 after:h-3 after:w-3 after:-translate-x-1/2 after:rotate-45"
          :style="{ left: rate.value * 100 + '%' }"
        >
          {{ rate.value * 100 }}%
        </span>
      </transition>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

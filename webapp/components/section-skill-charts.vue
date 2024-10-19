<script setup lang="ts">

// propsを受け取る
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
</script>
<template>
  <div class="mb-1">
    <span class="text-base font-medium text-blue-700 dark:text-blue-500"
      >変数名の付け方</span
    >
    簡潔だが意図は明確
  </div>
  <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
    <div class="bg-blue-600 h-2.5 rounded-full" :style="{width: props.variableNameSimplicityRate * 100 + '%'}"></div>
  </div>
  <div class="mb-1">
    <span class="text-base font-medium text-red-700 dark:text-red-500"
      >クラスやメソッド分割の粒度</span
    >
    細かく分割し、管理しやすく再利用性が高い
  </div>
  <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
    <div
      class="bg-red-600 h-2.5 rounded-full dark:bg-red-500"
      :style="{width: props.methodSplittingCoarsenessRate * 100 + '%'}"
    ></div>
  </div>
  <div class="mb-1">
    <span class="text-base font-medium text-green-700 dark:text-green-500"
      >処理の意図を伝える手段</span
    >
    メソッドやクラス名、変数名で表現
  </div>
  <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
    <div
      class="bg-green-600 h-2.5 rounded-full dark:bg-green-500"
      :style="{width: props.processingIntentCommunicatingRate * 100 + '%'}"
    ></div>
  </div>
  <div class="mb-1">
    <span class="text-base font-medium text-yellow-700 dark:text-yellow-500"
      >コミットの粒度</span
    >
    作業単位（クラス作成、メソッド作成するたびにコミットする）
  </div>
  <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
    <div class="bg-yellow-400 h-2.5 rounded-full" 
      :style="{width: props.commitGranularityRate * 100 + '%'}"
    ></div>
  </div>
</template>

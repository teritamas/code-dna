<script setup lang="ts">
// propsを受け取る
const props = defineProps({
    variableNameSimplicityRateReason: {
      type: String,
      required: true,
    },
    methodSplittingCoarsenessRateReason: {
      type: String,
      required: true,
    },
    processingIntentCommunicatingRateReason: {
      type: String,
      required: true,
    },
    commitGranularityRateReason: {
      type: String,
      required: true,
    },
  });
</script>
<template>
  <ul class="space-y-4 text-left">
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold"
        >変数名の付け方</span
      >
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        {{ props.variableNameSimplicityRateReason }}
      </span>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold"
        >クラスやメソッドの分割</span
      >
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        {{ props.methodSplittingCoarsenessRateReason }}
      </span>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold">
        処理の意図を伝える手段
      </span>
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        {{ props.processingIntentCommunicatingRateReason }}
      </span>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold">
        コミットの粒度
      </span>
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        {{ props.commitGranularityRateReason }}
      </span>
    </li>
  </ul>
</template>
<style scoped>
</style>

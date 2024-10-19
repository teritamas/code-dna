<template>
  <div
    class="relative flex h-[500px] w-full items-center justify-center overflow-hidden rounded-lg border bg-background p-10 md:shadow-xl"
    ref="containerRef"
  >
    <div
      class="flex size-full flex-col max-w-lg max-h-[200px] items-stretch justify-between gap-10"
    >
      <div class="flex flex-row items-center justify-between">
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)] dark:text-black"
          ref="div1Ref"
        >
          <icon-star />
        </div>
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)]"
          ref="div5Ref"
        >
          <icon-crown />
        </div>
      </div>
      <div class="flex flex-row items-center justify-between">
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)] dark:text-black"
          ref="div2Ref"
        >
          <icon-star />
        </div>
        <div
          class="z-10 flex size-16 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)]"
          ref="div4Ref"
        >
          <icon-bookmark />
        </div>
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)]"
          ref="div6Ref"
        >
          <icon-chart-bar />
        </div>
      </div>
      <div class="flex flex-row items-center justify-between">
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)] dark:text-black"
          ref="div3Ref"
        >
          <icon-star />
        </div>
        <div
          class="z-10 flex size-12 items-center justify-center rounded-full border-2 bg-white p-3 shadow-[0_0_20px_-12px_rgba(0,0,0,0.8)]"
          ref="div7Ref"
        >
          <icon-value />
        </div>
      </div>
    </div>

    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div1Ref"
      :toRef="div4Ref"
      :curvature="-75"
      :endYOffset="-10"
    />
    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div2Ref"
      :toRef="div4Ref"
      :pathWidth="10"
    />
    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div3Ref"
      :toRef="div4Ref"
      :curvature="75"
      :endYOffset="10"
    />
    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div5Ref"
      :toRef="div4Ref"
      :curvature="-75"
      :endYOffset="-10"
      :reverse="true"
    />
    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div6Ref"
      :toRef="div4Ref"
      :reverse="true"
    />
    <AnimatedBeam
      :containerRef="containerRef"
      :fromRef="div7Ref"
      :toRef="div4Ref"
      :curvature="75"
      :endYOffset="10"
      :reverse="true"
    />
  </div>
</template>

<script setup>
const containerRef = ref(null);
const div1Ref = ref(null);
const div2Ref = ref(null);
const div3Ref = ref(null);
const div4Ref = ref(null);
const div5Ref = ref(null);
const div6Ref = ref(null);
const div7Ref = ref(null);
</script>

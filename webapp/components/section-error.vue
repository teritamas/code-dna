<script setup lang="ts"></script>
<template>
  <div
    class="mx-auto min-h-[300px] mt-10 flex flex-col justify-center w-full max-w-md px-4 py-8 bg-white rounded-lg shadow sm:px-6 md:px-8 lg:px-10"
  >
    <div class="flex items-center justify-center px-2 mb-3 mx-auto">
      <blur-reveal :delay="0.2" :duration="0.75">
        <h2
          class="text-3xl text-center p-2 font-bold tracking-tighter sm:text-5xl xl:text-6xl/none"
        >
          エラーが発生しました 😔
        </h2>
      </blur-reveal>
    </div>
  </div>
</template>

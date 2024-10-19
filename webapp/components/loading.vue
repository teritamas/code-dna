<template>
  <blur-reveal :delay="0.2" :duration="0.75">
    <h2
      class="text-3xl text-center p-2 font-bold tracking-tighter sm:text-5xl xl:text-6xl/none"
    >
      解析中です...
    </h2>
  </blur-reveal>
  <div class="loader"></div>
</template>
<style scoped>
.loader {
  height: 4px;
  width: 130px;
  --c: no-repeat linear-gradient(#6100ee 0 0);
  background: var(--c), var(--c), #d7b8fc;
  background-size: 60% 100%;
  animation: l16 3s infinite;
  margin: 1rem auto;
}
@keyframes l16 {
  0% {
    background-position: -150% 0, -150% 0;
  }
  66% {
    background-position: 250% 0, -150% 0;
  }
  100% {
    background-position: 250% 0, 250% 0;
  }
}
</style>

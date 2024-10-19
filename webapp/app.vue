<template>
  <div>
    <main>
      <NuxtPage />
    </main>
    <app-footer class="app-footer" />
  </div>
</template>

<style scoped>
main {
  margin-bottom: 60px; /* ヘッダーの高さ分だけマージンを設定 */
  padding-top: 20px;
  min-height: 88vh;
}

.app-footer {
  position: fixed; /* 固定 */
  bottom: 0; /* 下に固定 */
  left: 0; /* 左に固定 */
  width: 100vw; /* 幅を100vhに設定 */
  background-color: white; /* 背景色を指定 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* 影を追加 */
  z-index: 20; /* 他の要素の上に表示 */
}
</style>

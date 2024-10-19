<template>
  <ul class="space-y-4 text-left">
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold"
        >変数名の付け方 - 簡潔だが意図は明確</span
      >
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        あなたは変数名をシンプルに保つ傾向がありますが、その意味がすぐに理解できるような工夫をしています。冗長さを避けつつ、直感的に役割が伝わる変数名を選ぶことで、無駄を排除しながらもコードの読みやすさを維持しています。
      </span>
      <pre>
        <code>
    // 現在の時刻との差を計算して相対時間を返す関数
    const relativeTimeInMinutes = (time: string): string => {
        const now = dayjs();
        const diffMinutes = now.diff(dayjs(time), "minute");
        const diffHours = now.diff(dayjs(time), "hour");

        if (diffMinutes < 1) {
        return "たった今"; // 1分未満の場合
        } else if (diffHours < 1) {
        return `${diffMinutes} 分前`; // 1時間未満の場合
        } else {
        return `${diffHours} 時間前`; // 1時間以上の場合
        }
    };
        </code>
        </pre>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold"
        >クラスやメソッドの分割 - 大局的に捉える</span
      >
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        コード全体のシンプルさを重視し、大局的な視点でクラスやメソッドを設計します。細かく分割しすぎることはせず、一貫した構造でプロジェクトの全体像を明確に保つことが得意です。これにより、コードの保守性と可読性を高めています。
      </span>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold">
        処理の意図を伝える手段 - 必要なときにコメントで補足
      </span>
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        あなたはコードの大部分を自己説明的に保ちますが、重要なポイントや複雑なロジックにはコメントで補足を加えることを忘れません。コメントは必要最低限にとどめ、コードの流れを邪魔しないよう配慮しながらも、意図を正確に伝えることを大切にしています。
      </span>
    </li>
    <li class="items-center space-x-3 rtl:space-x-reverse mt-2">
      <IconCheck class="flex-shrink-0 w-3.5 fill-indigo-500 inline" />
      <span class="text-dark-900 font-bold">
        コミットの粒度 - 作業単位で小まめにコミット
      </span>
      <span class="block ml-6 text-gray-500 dark:text-gray-400">
        あなたは作業単位で頻繁にコミットを行い、進行状況をこまめに記録します。これにより、チームメンバーや将来の自分が進捗を容易に追跡できるようにし、柔軟に修正や変更を加えることが可能です。
      </span>
    </li>
  </ul>
</template>
<style scoped>
pre {
  padding: 0.1em; /* 内側の余白 */
  margin: 0 0 0.5em; /* 外側の余白 */
  border: solid 1px #4d4d4d; /* 枠線（枠線を濃い黒に） */
  background: #25292f; /* 背景色（背景を黒に） */
  color: #fff; /* 文字色（文字を白に） */
  font-size: 0.8rem;
}
</style>

<template>
  <footer class="bg-white dark:bg-gray-800 w-screen py-4">
    <div class="max-w-screen-xl px-4 mx-auto">
      <div class="flex max-w-xs mx-auto items-center justify-between">
        <routerLink
          to="/map"
          class="flex items-center justify-center text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
        >
          <svg
            width="20"
            height="20"
            fill="currentColor"
            class="text-xl transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              d="M40 48C26.7 48 16 58.7 16 72l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24L40 48zM192 64c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L192 64zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zM16 232l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0c-13.3 0-24 10.7-24 24zM40 368c-13.3 0-24 10.7-24 24l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0z"
            />
          </svg>
          <p class="ml-2 text-sm">マップ</p>
        </routerLink>
        <routerLink
          to="/"
          class="flex items-center justify-center text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
        >
          <svg
            width="20"
            height="20"
            fill="currentColor"
            class="text-xl transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              d="M40 48C26.7 48 16 58.7 16 72l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24L40 48zM192 64c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L192 64zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32l288 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-288 0zM16 232l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0c-13.3 0-24 10.7-24 24zM40 368c-13.3 0-24 10.7-24 24l0 48c0 13.3 10.7 24 24 24l48 0c13.3 0 24-10.7 24-24l0-48c0-13.3-10.7-24-24-24l-48 0z"
            />
          </svg>
          <p class="ml-2 text-sm">index</p>
        </routerLink>
        <router-link
          to="/login"
          class="flex items-center justify-center text-gray-400 transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
        >
          <svg
            width="20"
            height="20"
            fill="currentColor"
            class="text-xl transition-colors duration-200 hover:text-gray-800 dark:hover:text-200"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zm-312 8l0 64c0 13.3 10.7 24 24 24s24-10.7 24-24l0-64c0-13.3-10.7-24-24-24s-24 10.7-24 24zm80-96l0 160c0 13.3 10.7 24 24 24s24-10.7 24-24l0-160c0-13.3-10.7-24-24-24s-24 10.7-24 24zm80 64l0 96c0 13.3 10.7 24 24 24s24-10.7 24-24l0-96c0-13.3-10.7-24-24-24s-24 10.7-24 24z"
            />
          </svg>
          <p class="ml-2 text-sm">ログイン</p>
        </router-link>
      </div>
    </div>
  </footer>
</template>

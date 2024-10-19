# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.

## 開発者向け

### DB の操作

DB は Supabase を使用しています。DB の操作を行うために、Supabase にログインし、プロジェクトを紐づける必要があります。

```bash
npx supabase login
supabase link
# アカウントに紐づいたプロジェクトが表示されるので、該当のプロジェクトを選択して紐づける
```

#### Supabase から DB のスキーマをエクスポート

Supabase からスキーマをエクスポートし、`types/schema.ts` に保存する。

```bash
supabase gen types typescript --linked > ./types/schema.ts
```

#### Trigger の設定

ユーザ新規作成後、`profiles` テーブルに新規レコードを追加するための Trigger を設定する必要がある。

SQL は以下 SQL を実行する

- [`sql/trigger.sql`](sql/trigger.sql)

# Web App

CODE DNA の Web アプリケーションです。

## Quick Start

必要ライブラリをインストールします。

```bash
npm install
```

その後、以下のコマンドを実行することで、開発サーバーが立ち上がります。

```bash
npm run dev
```

開発サーバは 以下の URL からアクセスできます。

- http://localhost:3000

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

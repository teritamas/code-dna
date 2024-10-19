# Analytics Job

CODE DNA の分析用ジョブです。

## Quick Start

本アプリケーションは poetry を使用しています。poetry がインストールされていない場合は、インストールしてください。

必要ライブラリをインストールします。

```bash
cd analytics-job
poetry install
```

アプリケーションの起動は以下のコマンドで行います。

```bash
pwd
# ${Your clone path}/code-dna/analytics-job
poetry run python analyticsjob/main.py
```

また、docker-compose を使用してアプリケーションを起動することもできます。docker-compose で起動する場合は、本リポジトリの直下で実行してください。

```bash
pwd
# ${Your clone path}/code-dna
docker compose up
```

FROM python:3.11-slim

RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
WORKDIR /app
COPY . /app

# コンテナ起動時に実行するコマンドを指定
CMD ["python", "analyticsjob/main.py"]
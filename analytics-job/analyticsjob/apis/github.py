import requests


# ユーザーのアクティビティを取得
def get_activity(owner, headers, page: int = 1):
    response = requests.get(
        f"https://api.github.com/users/{owner}/events?per_page={100}&page={page}",
        headers,
    )
    return response.json()


# イベントタイプでフィルタリング
def filter_by_event_type(gh_activity, event_type):
    return [event for event in gh_activity if event["type"] == event_type]


# コミットの情報を取得
def get_commit(latest_push_event, headers):
    repo_name = latest_push_event["repo"]["name"]
    commit_sha = latest_push_event["payload"]["commits"][0]["sha"]

    # コミット情報を取得
    url = f"https://api.github.com/repos/{repo_name}/commits/{commit_sha}"
    return requests.get(url, headers=headers).json()


# ファイルの内容を取得
def get_file(file, headers):
    file_blob_url = file["raw_url"]  # 生の内容にアクセスできるURL

    # ファイルの内容を取得
    file_response = requests.get(file_blob_url, headers=headers)
    return file_response.text

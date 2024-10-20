from apis.github import filter_by_event_type, get_commit, get_file


def fetch_by_push_event(gh_activity, headers, max_file_count: 100):
    push_events = filter_by_event_type(gh_activity, "PushEvent")
    print(f"Pushイベント数: {len(push_events)}")
    # 最新のPushEventのリポジトリ名を取得する
    change_files = ""
    push_events.sort(key=lambda x: x["created_at"], reverse=True)

    file_count = 0
    for event in push_events:
        latest_push_event = event
        try:
            commit_data = get_commit(latest_push_event, headers)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        # 変更されたファイルを走査
        for file in commit_data["files"]:
            # ファイルが画像やsvgファイルの場合はスキップ
            if file["filename"].endswith(
                (".png", ".jpg", ".jpeg", ".svg", ".gif", ".zip", ".json", ".md", ".yml", ".yaml", ".lock", ".toml", ".xml", '.txt', '.gitignore', '.gitattributes', '.gitmodules', '.gitkeep', '.gitconfig', '.git')
            ):
                continue

            file_response = get_file(file, headers)
            change_files += f"filename: {file['filename']}\n"
            change_files += f"code: {file_response}\n"

            file_count += 1
            if file_count >= max_file_count:
                break

        if file_count >= max_file_count:
            print("ファイル数が上限に達したため処理を終了します")
            break
    return change_files

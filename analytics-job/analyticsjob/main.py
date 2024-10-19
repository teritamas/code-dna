from apis.github import get_activity
from facades.comment_identify_by_gpt import get_by_push_event
from facades.fetch_git_activity import fetch_by_push_event
from apis.supabase import fetch_by_in_progress_status, update_status_by_error, update_by_completed_status


MAX_PUSH_EVENT_FILE_COUNT = 30  # 最大100ファイルまで分析


def main(profile_id, owner, token):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}",
    }
    # githubのRestAPIを叩いて、最新のアクティビティを取得する
    try:
        gh_activity = get_activity(owner, headers)
        change_files = fetch_by_push_event(gh_activity, headers, MAX_PUSH_EVENT_FILE_COUNT)
        parsed_data = get_by_push_event(change_files)
        print(parsed_data.json())

        update_by_completed_status(profile_id, parsed_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        # profileのステータスを更新
        update_status_by_error(profile_id)

# def get_prompts():
#     # デバッグ用にchange_files.txtから読み込む
#     with open("change_files.txt", "r") as f:
#         change_files = f.read()
#     parsed_data = get_by_push_event(change_files)
#     print(parsed_data.json())


# main関数
if __name__ == "__main__":
    print("処理を開始します")
    users = fetch_by_in_progress_status()
    print(f"処理待ちのユーザ数: {len(users)}")

    for user in users:
        print(f"処理開始. ユーザ名: {user['user_name']}")
        main(user["id"], user["user_name"], user["github_provider_token"])

from supabase import create_client, Client
from models.gpt_identity_response import GptIdentityResponse
from config import SUPABASE_URL, SUPABASE_ANON_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


# 処理待ち(dna_summary_create_status=1)のユーザを取得
def fetch_by_in_progress_status():
    response = (
        supabase.table("profiles")
        .select("user_name,github_provider_token, id")
        .eq("dna_summary_create_status", 1)
        .execute()
    )
    return response.data


# ユーザのステータスーを処理中(dna_summary_create_status=3)に更新
def update_status_by_error(profile_id: str):
    _ = (
        supabase.table("profiles")
        .update({"dna_summary_create_status": 3})
        .eq("id", profile_id)
        .execute()
    )
    print(f"ステータスを処理中に更新しました.: {profile_id}")


# 処理が完了したらDBのステータスを更新
def update_by_completed_status(profile_id: str, response: GptIdentityResponse):
    _ = (
        supabase.table("code_dna_summary")
        .update(
            {
                "variable_name_simplicity_rate": response.variable_name_simplicity_rate.rate,
                "method_splitting_coarseness_rate": response.method_splitting_coarseness_rate.rate,
                "processing_intent_communicating_rate": response.processing_intent_communicating_rate.rate,
                "commit_granularity_rate": response.commit_granularity_rate.rate,
                "variable_name_simplicity_rate_reason": response.variable_name_simplicity_rate.reason,
                "method_splitting_coarseness_rate_reason": response.method_splitting_coarseness_rate.reason,
                "processing_intent_communicating_rate_reason": response.processing_intent_communicating_rate.reason,
                "commit_granularity_rate_reason": response.commit_granularity_rate.reason,
                "summary_comment": response.summary_comment,
                "identity_name": response.identity_name,
            }
        )
        .eq("profile_id", profile_id)
        .execute()
    )
    # profileのステータスを更新
    _ = (
        supabase.table("profiles")
        .update({"dna_summary_create_status": 2})
        .eq("id", profile_id)
        .execute()
    )
    print(f"DBの更新処理が完了しました。profile_id: {profile_id}")
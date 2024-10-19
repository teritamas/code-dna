from models.gpt_identity_response import GptIdentityResponse
from apis.llm_api import generate_text
import json


def get_by_push_event(change_files: str) -> GptIdentityResponse:
    prompt = (
        """
あなたは何人ものエンジニアを育成してきたシニアエンジニアです。以下のユーザのコードを見て、ユーザのエンジニアとしてのアイデンティティを評価してください。
以下の項目について0~1の間でスコアと、その理由を具体的なソースコードを示し、250字以内で記入してください。判断できない場合は0.5を記入し、判断できない旨を記載してください。
1. 変数名の付け方
変数の付け方が、簡潔な変数をつける傾向が高い場合は1に近い数字、長いが説明的な変数をつける傾向に高い場合は0に近い数字をつけてください。
2. クラスやメソッド分割の粒度
細かく分割し、管理しやすく再利用性が高いものを作る傾向が高い場合は1に近い数字、一つのクラスやメソッドに多くの処理を詰め込む傾向が高い場合は0に近い数字をつけてください。
3. 処理の意図を伝える手段
コメントを利用せず、メソッドやクラス名、変数名で表現する傾向が高い場合は1に近い数字、コメントを多用し、処理の意図を伝える傾向が高い場合は0に近い数字をつけてください。
4. コミットの粒度
クラス作成、メソッド作成するたびにコミットする傾向が高い場合は1に近い数字、一つの機能を実装するまでコミットをしない傾向が高い場合は0に近い数字をつけてください。

また、上記の分析結果とソースコードの内容元に、その人物のエンジニアとしてのアイデンティティの説明を250文字以内で記入と、10文字程度でその人物のエンジニアとしてのアイデンティティを示す、ラベル付を行ってください
ラベル付は「XXXXなYYYYY者」のような、その人の特徴を示す面白いラベルをお願いいたします。

結果はjson形式で出力してください。
コードブロックは必ず含めないでください。

{
    "variable_name_simplicity_rate":{
        "rate": 1. 変数名の付け方のスコア,
        "reason": "理由"
    },
    "method_splitting_coarseness_rate":{
        "rate": 2. クラスやメソッド分割の粒度のスコア,
        "reason": "理由"
    },
    "processing_intent_communicating_rate":{
        "rate": 3. 処理の意図を伝える手段のスコア,
        "reason": "理由"
    },
    "commit_granularity_rate":{
        "rate": 4. コミットの粒度のスコア,
        "reason": "理由"
    }
    "summary_comment": "エンジニアとしてのアイデンティティの説明を250文字以内で記入",
    "identity_name": "エンジニアとしてのアイデンティティのラベル"
}

解析対象のソースコードは以下の通りです。
"""
        + change_files
    )

    response = generate_text(prompt)
    parsed_data = GptIdentityResponse.model_validate(json.loads(response))
    return parsed_data

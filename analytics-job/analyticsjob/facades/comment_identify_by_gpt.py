from models.gpt_identity_response import GptIdentityResponse
from apis.llm_api import generate_text
import json


def get_by_push_event(change_files: str) -> GptIdentityResponse:
    prompt = (
        """以下のユーザのコードを見て、ユーザのエンジニアとしてのアイデンティティを診断してください。ソースコードは、この文章の下に続きます。
""" + change_files +
"""スキルを評価するのではなく、その人のエンジニアとしてのアイデンティティ見極めてください。

以下の1~4の項目については、0~1の間で、どちらの傾向があるか示してください。
このスコアは、1が最も良いわけではなく、位置付けを示すものであるので、0であることも否定的にはならないでください。判断できない場合は0.5としてください。しかし判断が非常に難しい場合を除き、可能な限り、0.5は避けてください。
またその理由を、具体的なソースコードを示し、1000文字以内で記入してください。

1. 変数名の付け方
変数の付け方が、簡潔な変数をつける傾向が高い場合は1に近い数字、長いが説明的な変数をつける傾向に高い場合は0に近い数字をつけてください。
2. クラスやメソッド分割の粒度
細かく分割し、管理しやすく再利用性が高いものを作る傾向が高い場合は1に近い数字、一つのクラスやメソッドに多くの処理を詰め込む傾向が高い場合は0に近い数字をつけてください。
3. 処理の意図を伝える手段
コメントを利用せず、メソッドやクラス名、変数名で表現する傾向が高い場合は1に近い数字、コメントを多用し、処理の意図を伝える傾向が高い場合は0に近い数字をつけてください。
4. コミットの粒度
クラス作成、メソッド作成するたびにコミットする傾向が高い場合は1に近い数字、一つの機能を実装するまでコミットをしない傾向が高い場合は0に近い数字をつけてください。

また、上記の分析結果とソースコードの内容元に、その人物のエンジニアとしてのアイデンティティの説明を250文字以内で記入と、10文字程度でその人物のエンジニアとしてのアイデンティティを示す、ラベル付を行ってください。
ラベル付は「XXXXなYYYYY者」のような、その人の特徴を示す面白いラベルをお願いいたします。
どちらの項目も、否定的な文言は利用せず、その人のアイデンティティをポジティブに捉えるように記入してください。すべての文章は必ず褒めてください。

結果はjson形式で出力してください。
コードブロックは必ず含めないでください。

{
    "variable_name_simplicity_rate":{
        "rate": 1. 変数名の付け方の傾向,
        "reason": "理由"
    },
    "method_splitting_coarseness_rate":{
        "rate": 2. クラスやメソッド分割の粒度の傾向,
        "reason": "理由"
    },
    "processing_intent_communicating_rate":{
        "rate": 3. 処理の意図を伝える手段の傾向,
        "reason": "理由"
    },
    "commit_granularity_rate":{
        "rate": 4. コミットの粒度の傾向,
        "reason": "理由"
    }
    "summary_comment": "エンジニアとしてのアイデンティティの説明を250文字以内で記入",
    "identity_name": "エンジニアとしてのアイデンティティのラベル"
}
""")
    response = generate_text(prompt)
    try:
        parsed_data = GptIdentityResponse.model_validate(json.loads(response))
    except Exception as e:
        print(f"An error occurred: {e}")
        parsed_data = GptIdentityResponse(
            variable_name_simplicity_rate={
                "rate": 0.5,
                "reason": "解析できませんでした",
            },
            method_splitting_coarseness_rate={
                "rate": 0.5,
                "reason": "解析できませんでした",
            },
            processing_intent_communicating_rate={
                "rate": 0.5,
                "reason": "解析できませんでした",
            },
            commit_granularity_rate={"rate": 0.5, "reason": "解析できませんでした"},
            summary_comment="解析できませんでした",
            identity_name="解析できませんでした",
        )
    return parsed_data

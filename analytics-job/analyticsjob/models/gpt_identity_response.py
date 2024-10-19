from pydantic import BaseModel, Field


class RateDetail(BaseModel):
    rate: float = Field(..., description="スコア")
    reason: str = Field(..., description="理由")


class GptIdentityResponse(BaseModel):
    variable_name_simplicity_rate: RateDetail = Field(
        ..., description="変数名の付け方の評価"
    )
    method_splitting_coarseness_rate: RateDetail = Field(
        ..., description="クラスやメソッド分割の粒度の評価"
    )
    processing_intent_communicating_rate: RateDetail = Field(
        ..., description="処理の意図を伝える手段の評価"
    )
    commit_granularity_rate: RateDetail = Field(..., description="コミットの粒度の評価")
    summary_comment: str = Field(
        ..., description="エンジニアとしてのアイデンティティの説明"
    )
    identity_name: str = Field(
        ..., description="エンジニアとしてのアイデンティティのラベル"
    )

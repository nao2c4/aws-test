"""Pydantic のモデルを定義するモジュール。"""

from pydantic import BaseModel, Field


class AWSService(BaseModel):
    """AWS サービスの情報を保持するクラス。

    Attributes:
        service (str): サービス名。
        description (str): サービスの説明。
        usecases (tuple[str, ...]): サービスの使用用途。
    """

    service: str
    description: str
    usecases: tuple[str, ...] = Field(min_length=1)

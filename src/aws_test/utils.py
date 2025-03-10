"""AWS テストのユーティリティ関数を提供するモジュール。"""

from pathlib import Path

import yaml
from pydantic import TypeAdapter

from .models import AWSService


def load_aws_services_yaml(yaml_path: Path, encoding: str = "utf-8") -> list[AWSService]:
    """YAML ファイルから AWS サービスの情報を読み込む。

    Args:
        yaml_path (Path): YAML ファイルのパス。
        encoding (str): YAML ファイルのエンコーディング。

    Returns:
        list[AWSService]: AWS サービスの情報のリスト。

    Raises:
        FileNotFoundError: YAML ファイルが存在しない場合。
    """
    if not yaml_path.exists():
        msg = f"YAML file not found: {yaml_path}"
        raise FileNotFoundError(msg)
    return TypeAdapter(list[AWSService]).validate_python(
        yaml.safe_load(yaml_path.read_text(encoding=encoding))
    )


def load_aws_services_json(json_path: Path, encoding: str = "utf-8") -> list[AWSService]:
    """JSON ファイルから AWS サービスの情報を読み込む。

    Args:
        json_path (Path): JSON ファイルのパス。
        encoding (str): JSON ファイルのエンコーディング。

    Returns:
        list[AWSService]: AWS サービスの情報のリスト。

    Raises:
        FileNotFoundError: JSON ファイルが存在しない場合。
    """
    if not json_path.exists():
        msg = f"JSON file not found: {json_path}"
        raise FileNotFoundError(msg)
    return TypeAdapter(list[AWSService]).validate_json(json_path.read_text(encoding=encoding))

"""YAML ファイルを JSON に変換するスクリプト。"""

import argparse
from pathlib import Path

from pydantic import BaseModel, RootModel, field_validator

from aws_test import load_aws_services_yaml
from aws_test.models import AWSService


class Args(BaseModel):
    """コマンドライン引数を保持するクラス。

    Attributes:
        yaml_path (Path): YAML ファイルのパス。
        encoding (str): YAML ファイルのエンコーディング。
    """

    yaml_path: Path
    encoding: str = "utf-8"

    @field_validator("yaml_path")
    @classmethod
    def validate_yaml_path(cls, yaml_path: Path) -> Path:
        """YAML ファイルの存在を検証する。"""
        if not yaml_path.exists():
            msg = f"YAML file not found: {yaml_path}"
            raise FileNotFoundError(msg)
        if not yaml_path.is_file():
            msg = f"YAML file is not a file: {yaml_path}"
            raise FileNotFoundError(msg)
        return yaml_path

    @classmethod
    def parse_args(cls) -> "Args":
        """コマンドライン引数を解析する。"""
        parser = argparse.ArgumentParser(description="YAML ファイルを JSON に変換する。")
        parser.add_argument("yaml_path", type=Path, help="YAML ファイルのパス")
        parser.add_argument("--encoding", default="utf-8", help="YAML ファイルのエンコーディング")
        return cls(**vars(parser.parse_args()))


def main() -> None:
    """メイン関数。"""
    args = Args.parse_args()
    services = load_aws_services_yaml(args.yaml_path, args.encoding)
    args.yaml_path.with_suffix(".json").write_text(
        RootModel[list[AWSService]](services).model_dump_json(indent=4), encoding=args.encoding
    )

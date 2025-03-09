"""YAML ファイルのテスト。"""

from pathlib import Path

from aws_test import load_aws_services_yaml
from aws_test.models import AWSService

# 記入している YAML ファイル。
# 名前が変わった場合は変更すること。
ROOT_DIR = Path(__file__).parents[1]
YAML_PATH = ROOT_DIR.joinpath("data/services.yaml")
JSON_PATH = YAML_PATH.with_suffix(".json")


def test_yaml_file() -> None:
    """YAML ファイルのテスト。

    Pydantic で読み込みできれば OK とする。
    """
    services = load_aws_services_yaml(YAML_PATH)
    assert isinstance(services, list)
    assert all(isinstance(service, AWSService) for service in services)


def test_json_file() -> None:
    """JSON ファイルのテスト。

    Pydantic で読み込みできれば OK とする。
    """
    services = load_aws_services_yaml(JSON_PATH)
    assert isinstance(services, list)
    assert all(isinstance(service, AWSService) for service in services)


def test_validate_yaml_json() -> None:
    """YAML と JSON の内容が一致するかテストする。

    Pydantic で読み込んだ結果が一致するかテストする。
    """
    yaml_services = load_aws_services_yaml(YAML_PATH)
    json_services = load_aws_services_yaml(JSON_PATH)
    assert all(
        yaml_service == json_service
        for yaml_service, json_service in zip(yaml_services, json_services, strict=True)
    )

"""YAML ファイルのテスト。"""

from itertools import product
from pathlib import Path

import pytest

from aws_test import load_aws_services_yaml
from aws_test.models import AWSService

# 記入している YAML ファイル。
# 名前が変わった場合は変更すること。
ROOT_DIR = Path(__file__).parents[1]
YAML_PATH = ROOT_DIR.joinpath("data/services.yaml")
JSON_PATH = YAML_PATH.with_suffix(".json")
WEB_JSON_PATH = ROOT_DIR.joinpath("docs/data/services.json")

yaml_paths = [YAML_PATH]
json_paths = [JSON_PATH, WEB_JSON_PATH]


@pytest.mark.parametrize("yaml_path", yaml_paths)
def test_yaml_file(yaml_path: Path) -> None:
    """YAML ファイルのテスト。

    Pydantic で読み込みできれば OK とする。
    """
    services = load_aws_services_yaml(yaml_path)
    assert isinstance(services, list)
    assert all(isinstance(service, AWSService) for service in services)


@pytest.mark.parametrize("json_path", json_paths)
def test_json_file(json_path: Path) -> None:
    """JSON ファイルのテスト。

    Pydantic で読み込みできれば OK とする。
    """
    services = load_aws_services_yaml(json_path)
    assert isinstance(services, list)
    assert all(isinstance(service, AWSService) for service in services)


@pytest.mark.parametrize(("yaml_path", "json_path"), product(yaml_paths, json_paths))
def test_validate_yaml_json(yaml_path: Path, json_path: Path) -> None:
    """YAML と JSON の内容が一致するかテストする。

    Pydantic で読み込んだ結果が一致するかテストする。
    """
    yaml_services = load_aws_services_yaml(yaml_path)
    json_services = load_aws_services_yaml(json_path)
    assert all(
        yaml_service == json_service
        for yaml_service, json_service in zip(yaml_services, json_services, strict=True)
    )

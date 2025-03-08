"""YAML ファイルのテスト。"""

from pathlib import Path

from aws_test import load_aws_services_yaml
from aws_test.models import AWSService

# 記入している YAML ファイル。
# 名前が変わった場合は変更すること。
ROOT_DIR = Path(__file__).parents[1]
YAML_PATH = ROOT_DIR.joinpath("data/services.yaml")


def test_yaml_file() -> None:
    """YAML ファイルのテスト。

    Pydantic で読み込みできれば OK とする。
    """
    services = load_aws_services_yaml(YAML_PATH)
    assert isinstance(services, list)
    assert all(isinstance(service, AWSService) for service in services)

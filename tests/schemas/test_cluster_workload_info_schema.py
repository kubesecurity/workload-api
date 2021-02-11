"""Test the cluster workload schema."""
import json
from typing import Dict, List
from collections import defaultdict

from pytest import fixture
from pytest import MonkeyPatch
import pytest
import marshmallow

from src.schemas.cluster_workload_info_schema import ClusterWorkloadInfoSchema, AccountsWorkloadRequestSchema
from src.models.cluster_workload_info_model import ClusterWorkloadInfoModel
from src.config import db

from tests.common_fixtures import workload_data_objects


@fixture
def request_schema() -> AccountsWorkloadRequestSchema:
    """Fixture to create a request schema."""
    return AccountsWorkloadRequestSchema()


@fixture
def request_workload() -> Dict:
    """Sample request to the workload request endpoint."""
    with open("./tests/test_data/workload_api_request.json") as f:
        request = json.load(f)
    return request


def test_account_request_schema(request_workload: Dict, request_schema: AccountsWorkloadRequestSchema):
    """Test if we can succcessfully deserialize and validate a JSON request."""
    request_works = request_schema.load(request_workload)
    assert request_works
    assert type(request_works["accounts"]) is list


def test_bad_request_raises_validation_error(request_workload: Dict, request_schema: AccountsWorkloadRequestSchema):
    """Test if a validation exception is raised when a bad request is loaded."""
    request_workload["record_count"] = 2000
    with pytest.raises(marshmallow.exceptions.ValidationError):
        request_schema.load(request_workload)


@fixture
def cluster_workload_schema() -> ClusterWorkloadInfoSchema:
    """Fixture to give us a schema instance."""
    return ClusterWorkloadInfoSchema(many=True)


def test_workload_info_schema_create(cluster_workload_schema: ClusterWorkloadInfoSchema):
    """Test that fixture itself works."""
    assert cluster_workload_schema


def test_cluster_workload_info_schema_works(
    cluster_workload_schema: ClusterWorkloadInfoSchema, workload_data_objects: List[ClusterWorkloadInfoModel]
):
    """Test if this schema works."""
    account_details = defaultdict(list)
    response_data = []
    for cluster_details in workload_data_objects:
        account_details[cluster_details.account_id].append(cluster_details)
    for cluster_detail_list in account_details.values():
        serialized = cluster_workload_schema.dump(cluster_detail_list)
        assert serialized
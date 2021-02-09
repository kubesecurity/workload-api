"""Test the cluster workload schema."""
import json

from pytest import fixture

from src.schemas.cluster_workload_info_schema import ClusterWorkloadInfoSchema, AccountsWorkloadRequestSchema
from src.models.cluster_workload_info_model import ClusterWorkloadInfoModel
from src.config import db


@fixture
def cluster_workload_schema() -> ClusterWorkloadInfoSchema:
    """Fixture to give us a schema instance."""
    return ClusterWorkloadInfoSchema()


def test_WorkloadInfoSchema_create(cluster_workload_schema: ClusterWorkloadInfoSchema):
    """Test that fixture itself works."""
    assert cluster_workload_schema


def test_WorkloadInfoSchema_works(cluster_workload_schema: ClusterWorkloadInfoSchema):
    """Test whether we are able to instantiate workload info schema."""
    pass


@fixture
def request_schema() -> AccountsWorkloadRequestSchema:
    """Fixture to create a request schema."""
    return AccountsWorkloadRequestSchema()


def test_accountRequestSchema_create(request_schema: AccountsWorkloadRequestSchema):
    """Test if we can succcessfully deserialize and validate a JSON request."""
    with open("./tests/test_data/workload_api_request.json") as f:
        request = json.load(f)
        print(request)
        request_works = request_schema.load(request)
        assert request
        assert type(request["accounts"]) is list


def test_ClusterWorkloadInfoSchema(cluster_workload_schema: ClusterWorkloadInfoSchema):
    """Test if cluster workload info schema can be loaded from the database."""
    data = (
        ClusterWorkloadInfoModel.query.filter(ClusterWorkloadInfoModel.account_id.in_([2876, 2706, 6286, 3000]))
        .order_by(ClusterWorkloadInfoModel.account_id)
        .all()
    )
    print(data)
    assert False
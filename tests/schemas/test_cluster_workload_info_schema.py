"""Test the cluster workload schema."""
import json

from pytest import fixture
from pytest import MonkeyPatch

from src.schemas.cluster_workload_info_schema import ClusterWorkloadInfoSchema
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


def test_ClusterWorkloadInfoSchema(cluster_workload_schema: ClusterWorkloadInfoSchema):
    """Test if cluster workload info schema can be loaded from the database."""
    data = (
        ClusterWorkloadInfoModel.query.filter(ClusterWorkloadInfoModel.account_id.in_([2876, 2706, 6286, 3000]))
        .order_by(ClusterWorkloadInfoModel.account_id)
        .all()
    )

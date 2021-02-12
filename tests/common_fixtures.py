"""Contains fixtures common acccross modules."""
import csv
import datetime as dt
from typing import Dict

import pytest

from src.models.cluster_workload_info_model import ClusterWorkloadInfoModel
from src.config import app
import src.config
import src.routes.auth


# This needs to be outside otherwise fixture reports error.
app.add_api("workload-api-spec.yaml")


@pytest.fixture
def workload_data_objects():
    """Create a collection of records that serve as the db query repsonse object."""
    with open("./tests/test_data/fake_workload_data.csv") as f:
        data_file = csv.DictReader(f, delimiter="|")
        records = [ClusterWorkloadInfoModel(**record) for record in data_file]
        for i in range(len(records)):
            records[i].cluster_last_reported = dt.datetime.strptime(
                records[i].cluster_last_reported.split(".")[0], "%Y-%m-%d %H:%M:%S"
            )
            records[i].created_time = dt.datetime.strptime(records[i].created_time.split(".")[0], "%Y-%m-%d %H:%M:%S")
            records[i].last_updated_time = dt.datetime.strptime(
                records[i].last_updated_time.split(".")[0], "%Y-%m-%d %H:%M:%S"
            )
        return records


@pytest.fixture
def app_client():
    """Return a test client to test routes."""
    return app.app.test_client()


@pytest.fixture
def auth_header(monkeypatch) -> Dict:
    """Return the authorization header with a bearer token."""
    monkeypatch.setattr(src.config, "SECRET_CLIENT_API_TOKEN", "test")
    jwt = src.routes.auth.generate_token(0)
    return {
        "Authorization": "Bearer " + str(jwt["client_api_token"]),
    }

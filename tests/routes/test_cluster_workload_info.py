"""Contains test for workload info endpoint."""
import json
from unittest.mock import patch

import pytest

from tests.common_fixtures import app_client, auth_header, workload_data_objects
import src.config


def test_workload_info_response(app_client, auth_header, workload_data_objects, monkeypatch, mocker):
    """Test the response we get from the workload info endpoint."""
    request = {"accounts": [2876, 2706, 6286, 3000], "offset": 0, "record_count": 5}
    mock_db_call = mocker.patch("src.routes.cluster_workload_info.ClusterWorkloadInfoModel")
    mock_db_call.get_total_count.return_value = len(workload_data_objects)
    mock_db_call = mock_db_call.query.filter.return_value.order_by
    mock_db_call.return_value.offset.return_value.limit.return_value.all.return_value = workload_data_objects
    monkeypatch.setattr(src.config, "SECRET_CLIENT_API_TOKEN", "test")

    # no auth
    response = app_client.post("/api/v1/workloads", json=request)
    assert response.status_code == 401

    # happy path
    response = app_client.post("/api/v1/workloads", json=request, headers=auth_header)
    assert response.status_code == 200
    assert response.json["total_count"] > 0
    assert len(response.json["cluster_details"]) == 4

    # check if invalid requests fail. Scenario 1: More than 12 accounts.
    request = {"accounts": [2876, 2706, 6286, 3000] * 5, "offset": 0, "record_count": 5}
    response = app_client.post("/api/v1/workloads", json=request, headers=auth_header)
    assert response.status_code == 400

    # scenario 2: record_count > 50
    request = {"accounts": [2876, 2706, 6286, 3000] * 5, "offset": 0, "record_count": 51}
    response = app_client.post("/api/v1/workloads", json=request, headers=auth_header)
    assert response.status_code == 400
    assert response.get_json() == "Invalid values supplied in JSON body, please review API limits"

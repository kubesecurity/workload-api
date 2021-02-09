"""Contains test for workload info endpoint."""
import json

import pytest
from tests.routes.common_fixtures import app_client, auth_header


def test_workload_info_response(app_client, auth_header):
    """Test the response we get from the workload info endpoint."""
    request = {"accounts": [2876, 2706, 6286, 3000], "offset": 0, "record_count": 5}
    response = app_client.post("/api/v1/workloads", json=request, headers=auth_header)
    assert response
    assert response.json["total_count"] > 0
    assert response.json["cluster_details"]

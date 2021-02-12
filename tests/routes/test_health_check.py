"""Test the health checks."""
from unittest.mock import patch

import pytest
from tests.common_fixtures import app_client


def test_liveness(app_client):
    """Test liveness probe."""
    response = app_client.get("/api/v1/")
    assert response.status_code == 200
    # Flask test client has this only one method to get response body.
    assert response.get_json() == "alive"


def test_readiness(app_client, mocker):
    """Test readiness probe."""
    # At first, no DB connection so should get a 502.
    response = app_client.get("/api/v1/readiness")
    assert response.status_code == 502
    mock_db = mocker.patch("src.routes.health_check.db")
    mock_db.query.return_value.all.return_value = 1
    response = app_client.get("/api/v1/readiness")
    assert response.status_code == 200
    # Flask test client has this only one method to get response body.
    assert response.get_json() == "ready"

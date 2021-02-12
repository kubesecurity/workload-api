"""Test the health checks."""
import pytest
from tests.common_fixtures import app_client


def test_liveness(app_client):
    """Test liveness probe."""
    response = app_client.get("/api/v1/")
    assert response
    assert response.text == "alive"

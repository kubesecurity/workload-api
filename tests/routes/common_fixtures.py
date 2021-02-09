"""Contains the common fixtures for all the routes."""
from typing import Dict

import pytest

from src.config import app
from src.routes.auth import generate_token


@pytest.fixture
def app_client():
    """Return a test client to test routes."""
    app.add_api("workload-api-spec.yaml")
    return app.app.test_client()


@pytest.fixture
def auth_header(monkeypatch) -> Dict:
    """Return the authorization header with a bearer token."""
    monkeypatch.setenv("SECRET_CLIENT_API_TOKEN", "test")
    jwt = generate_token(0)
    return {
        "Authorization": "Bearer " + str(jwt),
    }

"""Test the accounts endpoint.."""
import pytest

from tests.common_fixtures import app_client, auth_header, account_objects

import src.config


def test_get_accounts(app_client, monkeypatch, auth_header, mocker, account_objects):
    """Test liveness probe."""
    monkeypatch.setattr(src.config, "SECRET_CLIENT_API_TOKEN", "test")
    mock_db_call = mocker.patch("src.routes.accounts.AccountModel")
    mock_db_call = mock_db_call.query.filter.return_value.order_by
    mock_db_call.return_value.offset.return_value.limit.return_value.all.return_value = account_objects
    mock_db_call.get_total_accounts.return_value = 25
    response = app_client.get("/api/v1/accounts", headers=auth_header)
    assert response.status_code == 200
    response_json = response.get_json()
    assert "accounts" in response_json

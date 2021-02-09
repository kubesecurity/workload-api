"""Tests for the account schemas."""
import pytest
from src.schemas.account_schema import AccountsResponse
import json


@pytest.fixture
def response_schema() -> AccountsResponse:
    """Fixture to create a response schema."""
    return AccountsResponse()

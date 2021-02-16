#!/usr/bin/env python3

"""Definitions for the routes of the accounts API."""
from src.schemas.account_schema import AccountsResponse, _AccountSchema
from src.models.account_model import AccountModel


def get_accounts(offset=0, record_count=1000):
    """Return a page from the list of all accounts that are present in the system."""
    if record_count > 1000 or offset < 0:
        return "Invalid value specified for record count or offset", 400
    accounts = AccountModel.query.order_by(AccountModel.account_id.desc()).offset(offset).limit(record_count)
    return AccountsResponse().dump(
        {"total_count": AccountModel.get_total_accounts(), "accounts": _AccountSchema(many=True).dump(accounts)}
    )

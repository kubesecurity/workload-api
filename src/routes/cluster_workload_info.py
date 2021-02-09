#!/usr/bin/env python3
"""Contains the handlers and business logic for the workload API."""
from src.schemas.cluster_workload_info_schema import AccountsWorkloadRequestSchema


def get_workload_info(body):
    """Another stub to ensure connexion does not error out."""
    print(body)
    accounts = AccountsWorkloadRequestSchema().load(body)
    print(accounts)

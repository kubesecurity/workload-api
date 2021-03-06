#!/usr/bin/env python3
"""Contains the handlers and business logic for the workload API."""
from collections import defaultdict

import marshmallow
from connexion.lifecycle import ConnexionResponse

from src.schemas.cluster_workload_info_schema import (
    ClusterWorkloadInfoSchema,
    AccountWorkloadResponseSchema,
    AccountsWorkloadRequestSchema,
)
from src.models.cluster_workload_info_model import ClusterWorkloadInfoModel


def get_workload_info(body):
    """Another stub to ensure connexion does not error out."""
    try:
        body = AccountsWorkloadRequestSchema().load(body)
    except marshmallow.exceptions.ValidationError:
        return "Invalid values supplied in JSON body, please review API limits", 400
    workload_data = (
        ClusterWorkloadInfoModel.query.filter(ClusterWorkloadInfoModel.account_id.in_(body.get("accounts", [])))
        .order_by(ClusterWorkloadInfoModel.account_id, ClusterWorkloadInfoModel.cluster_id)
        .offset(body.get("offset", 0))
        .limit(body.get("record_count", 50))
        .all()
    )

    # TODO: check if there's a way to do this automatically without this loop.
    account_details = defaultdict(list)
    response_data = []
    for cluster_details in workload_data:
        account_details[cluster_details.account_id].append(cluster_details)

    # List comprehension, not the cluster_details is not same as above.
    response_data = [
        AccountWorkloadResponseSchema().dump({"account": account_id, "clusters": cluster_details})
        for account_id, cluster_details in account_details.items()
    ]

    return {
        "cluster_details": response_data,
        "total_count": ClusterWorkloadInfoModel.get_total_count(body.get("accounts", [])),
    }

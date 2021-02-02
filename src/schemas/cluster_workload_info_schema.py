#!/usr/bin/env pytohn3
"""Contains the marshmallow schema for cluster info entity to facilitate quick serialization."""
from config import ma
from models.cluster_workload_info_model import ClusterWorkloadInfoModel


class ClusterWorkloadInfoSchema(ma.SQLAlchemySchema):
    """Define a serialization schema for cluster workload info."""

    class Meta:
        """Defines the metaclass object for Marshmellow."""

        model = ClusterWorkloadInfoModel

    # TODO: Define the fields for this schema.

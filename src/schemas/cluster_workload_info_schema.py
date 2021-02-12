#!/usr/bin/env pytohn3
"""Contains the marshmallow schema for cluster info entity to facilitate quick serialization."""
from src.config import ma
from src.models.cluster_workload_info_model import ClusterWorkloadInfoModel
import marshmallow


class UtilizationInfoSchema(ma.SQLAlchemySchema):
    """Utlization information schema."""

    class Meta:
        """Link the model to the schema."""

        model = ClusterWorkloadInfoModel
        load_instance = True

    category_90 = ma.String(data_key="category")
    cpu_capacity_90 = ma.Float(data_key="cpu_capacity")
    cpu_utilization_percentage_90 = ma.Float(data_key="cpu_utilization_percentage")
    memory_capacity_90 = ma.Float(data_key="memory_capacity")
    memory_utilization_percentage_90 = ma.Float(data_key="memory_utilization_percentage")

    category_180 = ma.String(data_key="category")
    cpu_capacity_180 = ma.Float(data_key="cpu_capacity")
    cpu_utilization_percentage_180 = ma.Float(data_key="cpu_utilization_percentage")
    memory_capacity_180 = ma.Float(data_key="memory_capacity")
    memory_utilization_percentage_180 = ma.Float(data_key="memory_utilization_percentage")

    category_270 = ma.String(data_key="category")
    cpu_capacity_270 = ma.Float(data_key="cpu_capacity")
    cpu_utilization_percentage_270 = ma.Float(data_key="cpu_utilization_percentage")
    memory_capacity_270 = ma.Float(data_key="memory_capacity")
    memory_utilization_percentage_270 = ma.Float(data_key="memory_utilization_percentage")


def serialize(value, attr, **kwargs):
    """Serialize the utlization information in the clusterworkloadinfoschema object."""
    return {
        "90": UtilizationInfoSchema(
            only=(
                "category_90",
                "cpu_capacity_90",
                "cpu_utilization_percentage_90",
                "memory_capacity_90",
                "memory_utilization_percentage_90",
            )
        ).dump(value),
        "180": UtilizationInfoSchema(
            only=(
                "category_180",
                "cpu_capacity_180",
                "cpu_utilization_percentage_180",
                "memory_capacity_180",
                "memory_utilization_percentage_180",
            )
        ).dump(value),
        "270": UtilizationInfoSchema(
            only=(
                "category_270",
                "cpu_capacity_270",
                "cpu_utilization_percentage_270",
                "memory_capacity_270",
                "memory_utilization_percentage_270",
            )
        ).dump(value),
    }


class ClusterWorkloadInfoSchema(ma.SQLAlchemySchema):
    """Schema for object that contains all info for a particular cluster."""

    class Meta:
        """Link schema to corresponding SQLAlchemy model."""

        model = ClusterWorkloadInfoModel
        load_instance = True

    cluster_age = ma.Integer()
    cluster_id = ma.UUID()
    cluster_last_reported = ma.DateTime()
    is_expiring_trial = ma.Boolean()
    is_trial = ma.Boolean()
    utilization = ma.Function(serialize)


class AccountWorkloadResponseSchema(ma.Schema):
    """Define a serialization schema for cluster workload info."""

    account = ma.Integer()
    clusters = ma.Nested(ClusterWorkloadInfoSchema, many=True)


class AccountsWorkloadRequestSchema(ma.Schema):
    """Request JSON to the workload endpoint."""

    accounts = ma.List(ma.Integer())
    offset = ma.Integer()
    record_count = ma.Integer(validate=marshmallow.validate.Range(min=0, max=1000))

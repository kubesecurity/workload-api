#!/usr/bin/env python3
"""Contains the model for the cluster information object that is the core of workload API."""
import uuid

from sqlalchemy.dialects.postgresql import UUID

from src.config import db


class ClusterWorkloadInfoModel(db.Model):
    """A model that reprsents a row in the cluster info table."""

    __tablename__ = "cluster_detail"

    cluster_id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True)
    account_id = db.Column(db.Integer(), db.ForeignKey("account.account_id"))

    # 90 day usage.
    cpu_capacity_90 = db.Column(db.Float())
    cpu_utilization_percentage_90 = db.Column(db.Float())
    memory_capacity_90 = db.Column(db.Float())
    memory_utilization_percentage_90 = db.Column(db.Float())
    category_90 = db.Column(db.String(10))

    # 180 day usage.
    cpu_capacity_180 = db.Column(db.Float())
    cpu_utilization_percentage_180 = db.Column(db.Float())
    memory_capacity_180 = db.Column(db.Float())
    memory_utilization_percentage_180 = db.Column(db.Float())
    category_180 = db.Column(db.String(10))

    # 270 day usage.
    cpu_capacity_270 = db.Column(db.Float())
    cpu_utilization_percentage_270 = db.Column(db.Float())
    memory_capacity_270 = db.Column(db.Float())
    memory_utilization_percentage_270 = db.Column(db.Float())
    category_270 = db.Column(db.String(10))

    # subscription info
    is_trail = db.Column(db.Boolean())
    is_expiring_trial = db.Column(db.Boolean())

    # lifetime
    cluster_age = db.Column(db.Integer())
    cluster_last_reported = db.Column(db.DateTime)

    # audit info
    created_time = db.Column(db.DateTime)
    last_updated_time = db.Column(db.DateTime)

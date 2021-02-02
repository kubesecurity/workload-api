#!/usr/bin/env python3
"""Contains the model for the cluster information object that is the core of workload API."""

from sqlalchemy.dialects.postgresql import UUID
import uuid
from config import db


class ClusterWorkloadInfoModel(db.Model):
    """A model that reprsents a row in the cluster info table."""

    __tablename__ = "cluster_detail"
    cluster_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)

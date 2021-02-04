#!/usr/bin/env python3
"""Model for the account entity."""

from config import db
from sqlalchemy import func


class AccountModel(db.Model):
    """A model that reprsents a row in the cluster info table."""

    __tablename__ = "account"
    account_id = db.Column(db.Integer, primary_key=True)
    last_updated_time = db.Column(db.DateTime)

    @staticmethod
    def get_total_accounts():
        """Get the total number of records of this object."""
        return db.session.query(func.count(AccountModel.account_id)).scalar()
#!/usr/bin/env python3
"""Model for the account entity."""

from config import db


class AccountModel(db.Model):
    """A model that reprsents a row in the cluster info table."""

    __tablename__ = "account"
    account_id = db.Column(db.Integer, primary_key=True)

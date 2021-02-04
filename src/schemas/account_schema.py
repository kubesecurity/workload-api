"""Contains the schema to easily serialize the account entity."""

from config import ma
from models.account_model import AccountModel


class _AccountSchema(ma.SQLAlchemySchema):
    """Define a schema for serialization of account info."""

    class Meta:
        """Defines the SQLAlchemy model to use for the account object."""

        model = AccountModel
        load_instance = True

    account_id = ma.auto_field()


class AccountsResponse(ma.Schema):
    """The response schema contains multiple accounts objects along with the total count."""

    total_count = ma.Integer()
    accounts = ma.List(ma.Pluck(_AccountSchema, "account_id"))

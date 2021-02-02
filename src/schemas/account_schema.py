"""Contains the schema to easily serialize the account entity."""

from config import ma
from models.account_model import AccountModel


class AccountSchema(ma.SQLAlchemySchema):
    """Define a schema for serialization of account info."""

    class Meta:
        """Defines the metaclass for the serialization object."""

        model = AccountModel

        # TODO: Define the fields for this schema.

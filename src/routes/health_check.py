#!/usr/bin/env python3
"""Contains heartbeat routes that can be used to probe the liveness and readiness of the service."""
from connexion.lifecycle import ConnexionResponse
from sqlalchemy import literal_column

from src.config import db


def liveness():
    """Define a liveness probe for our app."""
    return "alive", 200, {"Content-Type": "text/plain"}


def readiness():
    """Readiness probe that checks if connection to DB is established."""
    try:
        # TODO: Check if there is a better way to check database connection can be established.
        assert db.session.query(literal_column("1")).all()
        return "ready", 200, {"Content-Type": "text/plain"}
    except:
        # Bad gateway since database can't be reached.
        return ConnexionResponse(status_code=502)

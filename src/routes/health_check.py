#!/usr/bin/env python3
"""Contains heartbeat routes that can be used to probe the liveness and readiness of the service."""
from connexion.lifecycle import ConnexionResponse
from config import db


def liveness():
    """Define a liveness probe for our app."""
    return ConnexionResponse(status_code=200, mimetype="text/plain", body="alive")


def readiness():
    """Readiness probe that checks if connection to DB is established."""
    try:
        # TODO: Check if there is a better way to check database connection can be established.
        db.session.query("1").from_statement("SELECT 1").all()
        return ConnexionResponse(status_code=200, mimetype="text/plain", body="alive")
    except:
        # Bad gateway since database can't be reached.
        return ConnexionResponse(status_code=501)

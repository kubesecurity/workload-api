#!/usr/bin/env python

"""Aggregates all the Flask blueprints to initialize the API."""

from config import app
from connexion.lifecycle import ConnexionResponse


def liveness():
    """Define a liveness probe for our app."""
    return ConnexionResponse(status_code=200, mimetype="text/plain", body="alive")


def readiness():
    """Readiness probe that checks if connection to DB is established."""
    from config import db

    # TODO: Check if database connection can be established.
    return ConnexionResponse(status_code=200, mimetype="text/plain", body="alive")


def decode_token():
    """Decode the JWT to authenticate request."""
    # TODO
    pass


if __name__ == "__main__":
    app.run(port=8080, debug=True)

#!/usr/bin/env python3
"""Contains the autorization handlers."""
import time

from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
import src.config as config


def decode_token(token, secret=None):
    """Decode the JWT to authenticate request."""
    try:
        if not secret:
            secret = config.SECRET_CLIENT_API_TOKEN
        return jwt.decode(token, secret, algorithms=["HS256"])
    except JWTError as e:
        raise Unauthorized


def decode_generation_token(token):
    """Decode generation tokens using a different secret."""
    return decode_token(token, config.SECRET_TOKEN_GENERATION)


def generate_token(user_id):
    """Generate a new client API token."""
    timestamp = int(time.time())
    payload = {
        "iat": int(timestamp),
        "sub": str(user_id),
    }
    return {
        "user_id": str(user_id),
        "client_api_token": jwt.encode(payload, config.SECRET_CLIENT_API_TOKEN, algorithm="HS256"),
    }

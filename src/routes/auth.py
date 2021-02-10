#!/usr/bin/env python3
"""Contains the autorization handlers."""
import time

from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
from src.config import SECRET_CLIENT_API_TOKEN, SECRET_TOKEN_GENERATION


def decode_token(token, secret=SECRET_CLIENT_API_TOKEN):
    """Decode the JWT to authenticate request."""
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except JWTError as e:
        raise Unauthorized


def decode_generation_token(token):
    """Decode generation tokens using a different secret."""
    return decode_token(token, SECRET_TOKEN_GENERATION)


# TODO: Define a route for token generation API.
def generate_token(user_id):
    """Generate a new client API token."""
    timestamp = int(time.time())
    payload = {
        "iat": int(timestamp),
        "sub": str(user_id),
    }
    return {
        "user_id": str(user_id),
        "client_api_token": jwt.encode(payload, SECRET_CLIENT_API_TOKEN, algorithm="HS256"),
    }

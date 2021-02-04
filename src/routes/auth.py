"""Contains the autorization handlers."""
import time

from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
from config import SECRET_CLIENT_API_TOKEN


def decode_token(token):
    """Decode the JWT to authenticate request."""
    try:
        return jwt.decode(token, SECRET_CLIENT_API_TOKEN, algorithms=["HS256"])
    except JWTError as e:
        raise Unauthorized


# TODO: Define a route for token generation API.
def generate_token(user_id):
    """Generate a new client API token."""
    timestamp = int(time.time())
    payload = {
        "iat": int(timestamp),
        "sub": str(user_id),
    }
    return jwt.encode(payload, SECRET_CLIENT_API_TOKEN, algorithm="HS256")

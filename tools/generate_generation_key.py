#!/usr/bin/env python3
"""A script to generate the 'master' tokens that are used for client API key generation.

Not scheduled to run anywhere automatically.
"""
import time
import os

from jose import JWTError, jwt


if __name__ == "__main__":
    # generate a new token on the command line.
    timestamp = int(time.time())
    payload = {
        "iat": int(timestamp),
        "sub": "telemetry analytics team",
    }
    # This will raise an error if the token is not set, which is what we want.
    print(jwt.encode(payload, os.environ["SECRET_TOKEN_GENERATION"], algorithm="HS256"))

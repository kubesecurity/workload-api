"""The gunicorn config for wherever it's used to serve."""
import os

from gevent import monkey

# Boilerplate to patch our app.
monkey.patch_all()

_port = os.environ.get("API_SERVER_PORT", 6006)

bind: str = f"0.0.0.0:{_port}"
workers: int = os.environ.get("NUMBER_WORKER_PROCESS", 4)
worker_class: str = os.environ.get("WORKER_TYPE", "gevent")

timeout: int = os.environ.get("API_SERVER_TIMEOUT", 90)
accesslog: str = "-"  # Since everything logged to stdout goes to Kibana this is fixed forever.
errorlog: str = "-"  # Same reason as above.
preload: bool = True  # I see no reason to turn this off because gunicorn shouldn't be used locally as a dev server.

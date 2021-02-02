"""Application backend configuration."""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

_POSTGRES_CONFIG = {
    "HOST": os.environ.get("PG_HOST"),
    "DATABASE": os.environ.get("PG_DATABASE"),
    "PASSWORD": os.environ.get("PG_PASSWORD"),
    "USERNAME": os.environ.get("PG_USERNAME"),
}

app = connexion.App(__name__, specification_dir="routes/OpenAPI/", server="gevent")
app.add_api("workload-openapi-spec.yaml")

flask_app = app.app

# Setup connection to Postgres instance.
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}".format(
    **_POSTGRES_CONFIG
)
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(flask_app)
ma = Marshmallow(flask_app)

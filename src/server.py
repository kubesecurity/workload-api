#!/usr/bin/env python

"""Aggregates all the Flask blueprints to initialize the API."""
from src.config import app
from flask_cors import CORS

# Initialize the API via the spec.
app.add_api("workload-api-spec.yaml")
app.add_api("tokengen-api-spec.yaml")
CORS(app.app)

if __name__ == "__main__":
    """Initialize a development server."""
    app.run(port=8080, debug=True)

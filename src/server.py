#!/usr/bin/env python

"""Aggregates all the Flask blueprints to initialize the API."""
import src.config as config

# Initialize the API via the spec.
config.app.add_api("workload-api-spec.yaml")


if __name__ == "__main__":
    """Initialize a development server."""
    config.app.run(port=8080, debug=True)

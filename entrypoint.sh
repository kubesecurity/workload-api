#!/bin/bash

# Our pythonpath and workdir are set through the dockerfile itself.
# Don't set one here that is different, change that if required.
gunicorn -c gunicorn.conf.py src.server:app
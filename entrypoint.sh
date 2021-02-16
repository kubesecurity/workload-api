#!/bin/bash
gunicorn -b 0.0.0.0:${API_SERVER_PORT} --workers=${NUMBER_WORKER_PROCESS} -k ${WORKER_TYPE} -t ${API_SERVER_TIMEOUT} src.server:app

#!/usr/bin/env bash

echo "Waiting for database to become available..."
/scripts/wait-for-it.sh db:5432 --timeout=30 -- echo "Database is ready!"

# Apply Alembic migrations
echo "Running database migrations..."
alembic upgrade head

# Set defaults if not provided in environment
: "${MODULE_NAME:=app.main}"
: "${VARIABLE_NAME:=app}"
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"
: "${LOG_LEVEL:=info}"
: "${LOG_CONFIG:=./deploy/configs/logging_uvicorn.ini}"

# Start uvicorn with live-reload
echo "Starting Uvicorn server..."
uvicorn \
    --reload \
    --proxy-headers \
    --host "$HOST" \
    --port "$PORT" \
    "$APP_MODULE"
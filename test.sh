#!/bin/bash

celery -A tasks worker --loglevel=INFO &
celery -A tasks flower --loglevel=INFO &
echo "Waiting 10s for celery to start"
sleep 10
python3 main.py
tail -F /app/celery-logs.log
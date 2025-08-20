#!/bin/bash
# Скрипт запуска приложения с автоматическими миграциями

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT

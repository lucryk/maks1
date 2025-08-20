#!/bin/bash
# Скрипт для выполнения миграций с повторными попытками

echo "Waiting for database to be ready..."
sleep 5

counter=0
max_attempts=10

until python manage.py migrate --noinput; do
  counter=$((counter+1))
  if [ $counter -ge $max_attempts ]; then
    echo "Failed to perform migrations after $max_attempts attempts."
    exit 1
  fi
  echo "Database migration attempt $counter failed. Retrying in 3 seconds..."
  sleep 3
done

echo "Migrations completed successfully."
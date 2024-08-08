#!/bin/bash
# migrate.sh

echo "Running database migrations..."
python /var/www/html/*/manage.py migrate

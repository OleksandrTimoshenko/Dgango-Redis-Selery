#!/bin/sh
python manage.py migrate
# If you don't want to show the wait_for_it page you can wait for data from celery now
#sleep 120
python manage.py runserver 0.0.0.0:8000
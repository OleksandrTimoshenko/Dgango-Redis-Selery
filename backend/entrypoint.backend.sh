#!/bin/sh
python manage.py migrate
# we must wait for the worker to add some data to the cache
sleep 60
python manage.py runserver 0.0.0.0:8000
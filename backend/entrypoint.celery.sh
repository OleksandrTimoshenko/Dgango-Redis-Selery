#!/bin/sh
celery -A project beat > /dev/null &
celery -A project worker -l INFO

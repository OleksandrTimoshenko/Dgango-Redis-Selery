# Django-Redis-Celery

This project shows how we can use the celery worker with Redis broker and Django project

### Srart project with vagrant

vagrant up

### Srart project with docker

cp ./dotenv.sample ./.env

docker-compose up

(you can see the wait_for_data page before celery add data to the cache, >= 2 min.)
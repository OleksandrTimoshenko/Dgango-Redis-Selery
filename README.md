# Django-Redis-Celery

project now developing

to start and test it use

cp ./dotenv.sample ./.env

virtualenv env

source ./env/bin/activate

cd ./backend

pip install -r requirements.txt

export CELERY_BROKER_URL="redis://localhost/0"

export REDIS_URL=redis://localhost

export SECRET_KEY="my_stong_secret_key"

docker-compose up -d    # starting Redis container

python manage.py migrate

celery -A project beat -l INFO

celery -A project worker -l INFO    # start worker

python manage.py runserver # if you run it the first time you should wait for data from the worker

(docker setup now developing...)
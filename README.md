# Django-Redis-Celery

project now developing

to start and test it use

virtualenv env

source ./env/bin/activate

cd ./backend

pip install -r requirements.txt

export CELERY_BROKER_URL="redis://localhost/0"

export SECRET_KEY="my_stong_secret_key"

docker-compose up -d    # starting Redis container

python manage.py migrate

celery -A project worker -l INFO    # start worker

testing

python ./manage.py shell

>>> from movies.tasks import add, mul, xsum

>>> res = add.delay(2,3)

>>> res.get()

To start project:

python manage.py runserver
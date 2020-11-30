# Create your tasks here
import os
import json
from celery import shared_task
import requests
import redis

redis_client = redis.StrictRedis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

GHIBLI_API_URL = "https://ghibliapi.herokuapp.com/films/"
CACHE_KEY_NAME = "cache:films"


def get_people_data(people_urls, film_url):
    # api behaves weird here: sometimes it returns a link for all the
    # characters from all the movies
    if people_urls == ["https://ghibliapi.herokuapp.com/people/"]:
        people_data = requests.get(people_urls[0]).json()
        people_data = [entry for entry in people_data if film_url in entry["films"]]
        return [entry["name"] for entry in people_data]
    else:
        return [requests.get(people_url).json()["name"] for people_url in people_urls]


def get_films_data():
    result = []
    films = requests.get(GHIBLI_API_URL).json()
    for film in films:
        people = get_people_data(film["people"], film["url"])
        result.append([film["title"], people])
    return result


@shared_task
def set_cache():
    films_data = get_films_data()
    redis_client.set(CACHE_KEY_NAME, json.dumps(films_data))

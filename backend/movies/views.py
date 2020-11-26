from django.shortcuts import render, redirect

import os
import redis
import json

CACHE_KEY_NAME = 'cache:films'

redis_client = redis.StrictRedis.from_url(
    os.getenv('REDIS_URL'), decode_responses=True)

def index(request):
    return redirect("/movies")

# if I dont have data from worker yet I shows wait_for_data page
def movies(request):
    films_json = redis_client.get(CACHE_KEY_NAME,)
    if films_json is not None:
        films = json.loads(films_json)
        return render(request, "movies.html",  {'films':films})
    else:
        return render(request, "wait_for_data.html")

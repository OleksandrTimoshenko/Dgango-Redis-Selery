from django.shortcuts import render, redirect

import os
import redis
import json

CACHE_KEY_NAME = 'cache:films'

redis_client = redis.StrictRedis.from_url(
    os.getenv('REDIS_URL'), decode_responses=True)

films_json = redis_client.get(CACHE_KEY_NAME,)

def index(request):
    return redirect("/movies")

def movies(request):
    films = json.loads(films_json)
    return render(request, "movies.html",  {'films':films})

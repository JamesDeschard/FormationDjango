from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.conf import settings

from first.models import Movie

import os
import time
import datetime
import requests

# Create your views here.

def home(request):
    print(request.GET.get('q'))
    return HttpResponse(f'the time is {datetime.datetime.now()}')

def file_example(request):
    file = open(os.path.join(settings.BASE_DIR, 'static', 'movies.csv'), 'rb')
    return FileResponse(file)

def generate(x):
    for i in range(x):
        yield f'<br>{i}<br>' 
        time.sleep(1)

def stream_example(request):
    return StreamingHttpResponse(generate(10))

def json_example(request):
    data = {
        'name': 'Django'
    }
    return JsonResponse(data)

def display_film_api(request, *args, **kwargs):
    movies = Movie.objects.all().values()
    return JsonResponse({'films': list(movies)}, status=200)

def display_film_detail_api(request, year):
    movies = Movie.objects.filter(year=year).values()
    return JsonResponse({'films': list(movies)}, status=200)

def kwargs_example(request, name, str):
    return JsonResponse({"pk": name, 'hello': str})


class MovieView(View):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all().values()
        return JsonResponse({'films': list(movies)}, status=200)




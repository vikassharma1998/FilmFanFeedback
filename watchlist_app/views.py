from django.shortcuts import render
from watchlist_app.models import *
from django.http import JsonResponse
# Create your views here.

#class based views 
def movie_list(request):
    #get all Movie models data
    movies = Movie.objects.all()
    data = {
            'movies': list(movies.values())
           }
    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
            'name' : movie.name,
            'description': movie.description,
            'active': movie.active
           }
    
    return JsonResponse(data)
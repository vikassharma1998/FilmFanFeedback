from django.urls import path
from watchlist_app.api.views import *

urlpatterns = [
    path('list/',MovieListAV.as_view(),name='Movie List'),
    path ('<int:pk>', MovieDetailsAV.as_view(), name= 'movie details'),
    ]

# urlpatterns = [
#     path('list/',movie_list,name='movie list'),
#     path ('<int:pk>', movie_details, name= 'movie details'),
# ]
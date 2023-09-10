from watchlist_app.models import *
from watchlist_app.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

## class based views
class MovieListAV(APIView):
    def get(self, request):
        try:
            movie = Movie.objects.all()
        except:
            return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)    
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    
    def post(get, request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try :
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)     
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try :
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND) 
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



##function based views 
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.all()
#         except:
#             return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)    
#         serializer = MovieSerializer(movie, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)    
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
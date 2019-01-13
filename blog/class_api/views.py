from rest_framework.views import APIView
from ..models import Post, Movie, Song

from rest_framework.response import Response
from .serializers import PostSerializer, MovieSerializer, SongSerializer
from django.http import JsonResponse
from rest_framework import status


class PostAPIView(APIView):

    def get(self, request):
        queryset = Post.published.all()
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):

    def get_object(self, id):
        try:
            return Post.published.get(id=id)
        except Post.DoesNotExist as e:
            return Response({'error': 'Given question object not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        instance = self.get_object(id=id)
        serializer = PostSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id=id)
        serializer = PostSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        instance = self.get_object(id=id)
        instance.delete()
        return Response({'data': 'object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class MovieListAPIView(APIView):

    def get(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request,):
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAPIView(APIView):

    def get(self, request, id=None):
        try:
            queryset = Movie.objects.get(id=id)
        except queryset.DoesNotExist:
            data = 'Object not found'
            return Response({'data': data}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = MovieSerializer(instance=queryset)
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)


class SongAPIView(APIView):

    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(instance=queryset, many=True)
        response = serializer.data
        return Response(response)

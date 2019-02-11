from django.shortcuts import render
from .serializers import SchoolModelSerializer
from rest_framework.views import APIView
from .models import SchoolModel, StudentModel, StandardModel
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class SchoolDetailAPIView(APIView):

    def get(self, request, school_id=None):
        school = SchoolModel.objects.get(id=school_id)
        serializer = SchoolModelSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = SchoolModelSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

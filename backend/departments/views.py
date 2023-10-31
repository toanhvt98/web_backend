from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *


class CreateTypeOfDepartmentView(generics.CreateAPIView):
    queryset = TypeOfDepartmentModel.objects.all()
    serializer_class = TypeOfDepartmentSerializer

class CreateDepartmentView(generics.CreateAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer

class CreateRoomDepartmentView(generics.CreateAPIView):
    queryset = RoomDepartmentModel.objects.all()
    serializer_class = RoomDepartmentSerializer

class ListRoomDepartmentView(generics.ListAPIView):
    queryset = RoomDepartmentModel.objects.all()
    serializer_class = RoomDepartmentSerializer
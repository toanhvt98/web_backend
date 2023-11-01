from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from .serializers import *
from rest_framework.response import Response

"""
    All Classes below are for TypeOfDepartmentModel
"""


class ListCreateTypeOfDepartmentView(ListCreateAPIView):
    queryset = TypeOfDepartmentModel.objects.all()
    serializer_class = TypeOfDepartmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyTypeOfDepartmentView(RetrieveUpdateDestroyAPIView):
    queryset = TypeOfDepartmentModel.objects.all()
    serializer_class = TypeOfDepartmentSerializer
    lookup_field = "pk"


"""
    All Classes below are for DepartmentModel
"""


class ListCreateDepartmentView(ListCreateAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


"""
    All Classes below are for RoomDepartmentModel
"""


class CreateRoomDepartmentView(CreateAPIView):
    queryset = RoomDepartmentModel.objects.all()
    serializer_class = RoomDepartmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyRoomDepartmentView(RetrieveUpdateDestroyAPIView):
    queryset = RoomDepartmentModel.objects.all()
    serializer_class = RoomDepartmentSerializer
    lookup_field = "pk"

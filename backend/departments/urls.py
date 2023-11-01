from .views import *
from django.urls import path

urlpatterns = [
    path("type/", ListCreateTypeOfDepartmentView.as_view()),
    path("type/<int:pk>", RetrieveUpdateDestroyTypeOfDepartmentView.as_view()),
    path("department", ListCreateDepartmentView.as_view()),
    path("room/", CreateRoomDepartmentView.as_view()),
    path("room/<int:pk>", RetrieveUpdateDestroyRoomDepartmentView.as_view()),
]

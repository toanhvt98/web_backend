from .views import *
from django.urls import path

urlpatterns =[
    path('type',ListCreateTypeOfDepartmentView.as_view()),
    path('department',ListCreateDepartmentView.as_view()),
    path('room',ListCreateRoomDepartmentView.as_view()),
]
from .views import *
from django.urls import path

urlpatterns =[
    path('type',CreateTypeOfDepartmentView.as_view()),
    path('department',CreateDepartmentView.as_view()),
    path('room/',CreateRoomDepartmentView.as_view()),
    path('room/list',ListRoomDepartmentView.as_view()),
]
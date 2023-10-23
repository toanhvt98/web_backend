from django.urls import path
from .views import *

urlpatterns = [
    path("user/", UserCreateView.as_view()),
]

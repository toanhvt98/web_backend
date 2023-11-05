from django.urls import path
from .views import *

urlpatterns = [
    path("create/", UserCreateView.as_view()),
    path("me/", RetriveUserAccountView.as_view()),
]

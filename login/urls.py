from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from login.views import CustomAuthToken

urlpatterns = [
    re_path(r'^', CustomAuthToken.as_view()),
]
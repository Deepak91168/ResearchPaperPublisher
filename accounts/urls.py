from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from accounts import views

urlpatterns = [path("register", views.register)]

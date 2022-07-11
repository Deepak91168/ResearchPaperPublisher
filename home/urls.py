from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from home import views
urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("about", views.about),
    path("home/<slug:url>",views.paper),
    path("categorypage/",views.categorypage),
    path("category/<slug:url>",views.category),

]
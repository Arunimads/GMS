from django.urls import path
from .views import * 
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('add_measurements/',add_measurements),
    path('view_measurements/',view_measurements),
]
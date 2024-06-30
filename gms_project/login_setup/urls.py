from django.urls import path
from .views import * 
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',login_view),
    path('home',home,name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
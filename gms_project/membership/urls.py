from django.urls import path
from .views import * 
urlpatterns = [
    path('create_package/',create_package),
    path('view_packages/',view_packages,name='view_packages'),
    path('edit_packages/<int:package_id>/', edit_packages, name='edit_packages'),
]

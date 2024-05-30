from django.urls import path
from .views import delete_member, edit_member, home, members_list, register

urlpatterns = [
    path('',home),
    path('register/', register, name='register'),
    path('members_list/', members_list, name='members_list'),
    path('edit_member/<int:member_id>/', edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', delete_member, name='delete_member'),
]
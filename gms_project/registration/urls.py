from django.urls import path
from .views import * 
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('register/', register, name='register'),
    path('members_list/', members_list, name='members_list'),
    path('edit_member/<int:member_id>/', edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', delete_member, name='delete_member'),
    path('add_trainer/', add_trainer, name='add_trainer'),
    path('trainer_list/', trainer_list, name='trainer_list'),
    path('edit_trainer/<int:trainer_id>/', edit_trainer, name='edit_trainer'),
    path('delete_trainer/<int:trainer_id>/', delete_trainer, name='delete_trainer'),
    path('approve_member/<int:member_id>/',approve_member),
    path('disapprove_member/<int:member_id>/',disapprove_member),


]




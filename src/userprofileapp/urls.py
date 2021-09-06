from django.urls import path
from userprofileapp.views import *


urlpatterns = [
    path('signup', sign_up, name='sign_up'),
    path('login', login_page, name='login_page'), 
    path('logout', logout_user, name='logout'),
    path('edit-profile', edit_profile, name='edit_profile'),
    path('profile', profile, name='profile', ),
    path('delete-profile/<str:username>', delete_profile, name='delete_profile'),


]
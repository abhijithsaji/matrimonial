from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('',home , name='home'),

    path('login/',loginpage, name='login'),
    path('register/',register, name='register'),

    path('register/', register ,name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

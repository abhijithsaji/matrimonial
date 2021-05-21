from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('',home , name='home'),

    path('register/',register, name='register'),

    path('login/',loginpage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('edit-profile-basic',edit_profile_basic ,name='edit-profile-basic'),
    path('edit-profile-personal',edit_profile_personal ,name='edit-profile-personal'),
    path('edit-profile-personality',edit_profile_personality ,name='edit-profile-personality'),
    path('edit-profile-astro',edit_profile_astro ,name='edit-profile-astro'),
    path('edit-profile-prefered-partner',edit_profile_prefered_partner ,name='edit-profile-prefered-partner'),


    path('religion-json/',get_json_religion_data,name="religion-json"),
    path('caste-json/<str:religion>/',get_json_caste_data,name="caste-json"),

    # My profile

    path('my-profile',my_profile,name='my-profile'),

]

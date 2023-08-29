from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UsersViews

from . import views

urlpatterns = [


    path('user_signup',UsersViews.register,name="register"),
    path('user_login', UsersViews.user_login, name='login'),
    path('update_profile/',UsersViews.update_profile, name='update_profile'),
    path('user_logout',UsersViews.user_logout,name='logout'),
    path('myprofile',UsersViews.user_profile,name='myprofile'),
    # path('change_general_info',UsersViews.change_general_info,name='change_general_info'),

]

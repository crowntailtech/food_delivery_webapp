from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls import include, url
from . import views
from . import views

urlpatterns=[
    path('restaurantpartner',views.partner,name="restaurantpartner"),
    ]
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('be-a-partner',views.deliveryboy,name="be a partner"),
   
]
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('contactus',views.contactus,name="contactus"),
   path('aboutus',views.aboutus,name="aboutus"),
   path('complaints',views.complaint,name="aboutus"),
   
]
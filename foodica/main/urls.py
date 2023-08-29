from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    # path('services',views.services,name="services"),
    path('delivery_partner',views.delivery,name="delivery"),
    path('partner_with_us',views.partnerwithus,name="partnerwithus"),
    path('help-&-support',views.helpp,name="help & support"),
    path('term-&-conditions',views.term,name="Term & Conditions"),
    path('error',views.error,name="error")
    
    
    
]
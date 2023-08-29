from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [

    # path('',views.Show_address),
    path('address',views.Add_address,name="address"),
    # path('/',views.Show_address),
    


    
    
    

]
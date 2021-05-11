from django.urls import include 
from django.urls import path
from .import views 


urlpatterns = [
    path('catalog/', include('catalog.urls')),
]

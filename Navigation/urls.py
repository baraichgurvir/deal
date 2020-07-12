from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('home', views.Home),
    path('piracy', views.Privacy),
    path('about', views.About),
    path('contact', views.Contact) 
]
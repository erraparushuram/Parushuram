from django.contrib import admin
from django.urls import path
from goobusinessesapp import views

urlpatterns = [
    path("", views.index, name='home'),
    # redirecting demo.html file
      # path('demo', views.demo, name='home'),
       path('about', views.about, name='home'),
    path("clone", views.clone, name='clone'),
]

from django.urls import path

from form_db import views

urlpatterns = [
    path('home', views.home, name='home'),
]
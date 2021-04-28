from django.urls import path
from . import views

app_name='address'

urlpatterns = [
    path('', views.insert, name='insert'),
    path('register', views.register, name='register'),
]
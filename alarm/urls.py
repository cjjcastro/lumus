from django.urls import path
from . import views

urlpatterns = [
    path('', views.alarm, name='alarm'),
    path('nox', views.nox, name='alarm'),
]
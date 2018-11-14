from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alarm', views.alarm, name='alarm'),
    path('nox', views.nox, name='alarm'),
]
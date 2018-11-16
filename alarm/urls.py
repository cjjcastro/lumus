from django.urls import path, re_path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
   	path('alarm', views.alarm, name='alarm'),
    re_path(r'^delete/(?P<part_id>[0-9]+)/$', views.delete, name='delete_view'),



]
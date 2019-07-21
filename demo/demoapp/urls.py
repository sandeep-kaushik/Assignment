from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url('^$', index,name='index'),
    url('dashboard/', dashboard, name='dashboard'),
    url(r'^register/$', register, name='register'),

]
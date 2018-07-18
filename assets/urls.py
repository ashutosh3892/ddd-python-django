from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^channel/$', MyChannel.as_view()),
    url(r'^show/$', MyShow.as_view()),
    url(r'^episode/$', MyEpisode.as_view()),
]
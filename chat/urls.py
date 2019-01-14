from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
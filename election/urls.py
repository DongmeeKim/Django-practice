from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dormitories/(?P<dormitory>.+)/$', views.dormitories),  
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]

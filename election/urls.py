from django.conf.urls import url
from . import views

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^$', views.index, name = 'home'),
    url(r'^dormitories/(?P<dormitory>.+)/$', views.dormitories),
    url(r'^dormitories/(?P<dormitory>.+)/results$', views.results), 
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
]

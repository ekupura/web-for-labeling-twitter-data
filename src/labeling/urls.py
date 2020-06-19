from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^guhehe/$', views.guhehe, name='guhehe'),
    url(r'^help/$', views.help, name='help'),
    url(r'^(?P<user_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


from django.conf.urls import url
from django.conf import settings
from django.conf.urls import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^registration/$', views.signup, name='signup'),
    url(r'^dashboard/$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^logout', auth_views.logout, {'next_page': '/todos/login/'}, name='logout'),
    url(r'^add', views.add, name='add')
]

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<user_id>\d+)/info/$', views.user_info, name = 'userInfo'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^signin/$', views.signin, name = 'signin'),
    url(r'^signout/$', views.signout, name = 'signout'),
    url(r'^settings/$', views.settings, name= 'settings'),
]


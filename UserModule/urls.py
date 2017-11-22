from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<user_id>\d+)/info/$', views.user_info, name = 'userInfo'),

]
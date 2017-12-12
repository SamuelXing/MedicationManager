from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.addAPlan, name='plan_create'),
    url(r'^(?P<plan_id>\d+)/drop/$', views.dropAPlan, name='plan_drop'),
    url(r'^(?P<plan_id>\d+)/edit/$', views.editAPlan, name='plan_edit'),
    url(r'^(?P<plan_id>\d+)/detail/$', views.detail, name='plan_detail'),
    url(r'^lists/$', views.listPlans, name='plan_lists'),
    url(r'^sendPlans/$', views.sendEmail, name='send_Email'),
]
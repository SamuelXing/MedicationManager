from django.conf.urls import url
from . import views

urlpatterns= [
     url(r'^addDrug/$', views.addDrug,name='drug_create'),
     url(r'^delete/$',views.deleteDrug,name='drug_delete'),
     url(r'^drugLists/$',views.listDrug,name='drug_list'),
]
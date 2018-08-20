# coding=utf-8

from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
    url(r'^dem/$', views.dem_index),

    url(r'^dem1/$',views.dem1_index),
    url(r'^dem2/(?P<pk>\d+)/$',views.dem2_index),
    url(r'^dev/$',views.Dev.as_view()),
    # 客户关怀添加
    url(r'^care_add/$',views.Care.as_view()),

    url(r'^dev1/$',views.dev1_index),
    url(r'^dev2/(?P<pk>\d+)/$',views.dev2_index),


    url(r'^(.*?)/$', views.others),
    # url(r'^dem/$', views.dem_index),
 ]
